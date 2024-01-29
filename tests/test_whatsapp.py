import unittest

from WhatsAppGPT import WhatsApp
import unittest


class TestWhatsApp(unittest.TestCase):
    def test_reset(self):
        whatsapp = WhatsApp("1234567890", chatbot=None)
        whatsapp.conversation = ["Message 1", "Message 2", "Message 3"]
        whatsapp.reset()
        self.assertEqual(whatsapp.conversation, [])

    # Add more test functions for other methods of the WhatsApp class

if __name__ == "__main__":
    unittest.main()
