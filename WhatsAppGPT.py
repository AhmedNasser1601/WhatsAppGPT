import sys, time, openai
from selenium import webdriver
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class GPT:
    def __init__(self, api_key: str):
        self.conversation = []
        openai.api_key = api_key

    def ask_question(self, question: str) -> str:
        try:
            if question+'\n' == self.conversation[-2]: return
        except:
            pass
        conversation_history = " ".join([str(item) for item in self.conversation])
        response = ""
        while response == "":
            try:
                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=question + " " + conversation_history,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5,
                ).get("choices")[0].get("text").strip()
            except Exception as e:
                self.reset()
                return "ChatGPT could not respond"
        self.conversation.append(question+'\n')
        self.conversation.append(response+'\n')
        return response

    def reset(self):
        self.conversation = []

class WhatsApp:
    def __init__(self, Number:str, chatbot):
        self.number = Number
        self.conversation = chatbot
        self.service = Service(ChromeDriverManager().install())
        self.service.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=self.service)
        self.msgbreak = ""

    def run(self):
        self.driver.get(f"https://web.whatsapp.com/send?phone={self.number}")  # Navigate to the chat page
        
        while len(self.driver.find_elements(By.ID, 'side')) < 1: time.sleep(1)
        time.sleep(2)
        print("Synchronizing messages...")
        
        while (len(self.driver.find_elements(By.XPATH,r"/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/button"))) > 0: time.sleep(1)
        time.sleep(2)
        print("Messages loaded successfully")
        
        self.messages = list()
        while True:
            time.sleep(1)
            elements = self.driver.find_elements(By.XPATH, f"//span[@data-testid='conversation-info-header-chat-title']")
            name = f"{elements[0].text}:" # Get the user's name
            divs = self.driver.find_elements(By.XPATH, f"//div[contains(@data-pre-plain-text, '{name}')]") # Get the user's messages
            
            if divs:
                last_parent = divs[-1] # Get the last div
                child_elements = last_parent.find_elements(By.XPATH, "./*[not(contains(@class, '_1hl2r'))]")
                last_child = child_elements[-1] # Get the last element
                text = last_child.text.replace("\n","")
                
                if text in self.messages:
                    response = self.conversation.question(text) # Pass the message as a question to GPT
                    if response:
                        time.sleep(2)
                        element = self.driver.find_element(By.XPATH, f'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p') # Get the sending element
                        element.clear()
                        element.send_keys(response) # Write the message
                        time.sleep(1)
                        element.send_keys(Keys.ENTER) # Send the response
                    continue
                else: self.messages.append(text)
            else: print("There is no questions!")

if __name__ == "__main__":
    WhatsApp(sys.argv[1], GPT(sys.argv[2])).run()
