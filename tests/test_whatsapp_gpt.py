import unittest

from WhatsAppGPT import WhatsAppGPT


class TestWhatsAppGPT(unittest.TestCase):
    def test_whatsapp_gpt_instance_creation(self):
        # Test if the WhatsAppGPT instance can be created successfully
        whatsapp_gpt = WhatsAppGPT()
        self.assertIsInstance(whatsapp_gpt, WhatsAppGPT)

    def test_whatsapp_gpt_initial_state(self):
        # Test if the WhatsAppGPT instance has the expected initial state
        whatsapp_gpt = WhatsAppGPT()
        self.assertEqual(whatsapp_gpt.messages, [])

    def test_whatsapp_gpt_handle_input_message(self):
        # Test if the WhatsAppGPT instance can handle different types of input messages
        whatsapp_gpt = WhatsAppGPT()
        whatsapp_gpt.handle_input_message("Hello")
        self.assertEqual(whatsapp_gpt.messages, ["Hello"])

    def test_whatsapp_gpt_generate_response(self):
        # Test if the WhatsAppGPT instance can generate appropriate responses for different input messages
        whatsapp_gpt = WhatsAppGPT()
        whatsapp_gpt.handle_input_message("Hello")
        response = whatsapp_gpt.generate_response()
        self.assertIsInstance(response, str)

    def test_whatsapp_gpt_send_response(self):
        # Test if the WhatsAppGPT instance can send the generated responses successfully
        whatsapp_gpt = WhatsAppGPT()
        whatsapp_gpt.handle_input_message("Hello")
        response = whatsapp_gpt.generate_response()
        success = whatsapp_gpt.send_response(response)
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
