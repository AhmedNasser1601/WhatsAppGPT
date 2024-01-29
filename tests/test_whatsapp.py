import unittest

from WhatsAppGPT import WhatsApp
import unittest


class TestWhatsApp(unittest.TestCase):
    def test_reset(self):
        whatsapp = WhatsApp("1234567890", chatbot=None)
        whatsapp.conversation = ["Message 1", "Message 2", "Message 3"]
        whatsapp.reset()
        self.assertEqual(whatsapp.conversation, [])

    def test_send_message(self):
        whatsapp = WhatsApp("1234567890", chatbot=None)
        message = "Hello, how are you?"
        whatsapp.send_message(message)
        self.assertEqual(whatsapp.sent_messages[-1], message)

    def test_receive_message(self):
        whatsapp = WhatsApp("1234567890", chatbot=None)
        message = "Hi there!"
        whatsapp.receive_message(message)
        self.assertEqual(whatsapp.received_messages[-1], message)

    def test_block_contact(self):
        whatsapp = WhatsApp("1234567890", chatbot=None)
        contact_number = "9876543210"
        whatsapp.block_contact(contact_number)
        self.assertTrue(contact_number in whatsapp.blocked_contacts)

    def test_unblock_contact(self):
        whatsapp = WhatsApp("1234567890", chatbot=None)
        contact_number = "9876543210"
        whatsapp.unblock_contact(contact_number)
        self.assertTrue(contact_number not in whatsapp.blocked_contacts)

if __name__ == "__main__":
    unittest.main()
