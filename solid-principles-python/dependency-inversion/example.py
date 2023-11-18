from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

class EmailSender(MessageSender):
    def send_message(self, message):
        print("Sent Email: ", message)

class SMSMessageSender(MessageSender):
    def send_message(self, message):
        print("Sent SMS: ", message)

class NotificationService:
    def __init__(self, message_sender: MessageSender):
        self.message_sender = message_sender

    def send_notification(self, message):
        self.message_sender.send_message(message)

if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSMessageSender()

    notification_service = NotificationService(email_sender)
    notification_service.send_notification("Email notification sent.")

    notification_service = NotificationService(sms_sender)
    notification_service.send_notification("SMS notification sent.")