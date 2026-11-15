import base64
from messages import Message
from decorators.message_decorator import HeaderDecorator, SignatureDecorator, DateDecorator, Base64Decorator

msg = "Одна ошибка и ты ошибся"


def test_header():
    message = HeaderDecorator(Message(msg), "Запомни, ")
    assert message.render() == "Запомни, " + msg


def test_signature():
    message = SignatureDecorator(Message(msg), " - Джейсон Стетхем")
    assert message.render() == msg + " - Джейсон Стетхем"


def test_date():
    message = DateDecorator(Message(msg), " 15.11.2026")
    assert message.render() == msg + " 15.11.2026"


def test_base64():
    message = Base64Decorator(Message(msg))
    assert message.render() == base64.b64encode(msg.encode()).decode()


def test_combination():
    message = HeaderDecorator(Message(msg), "Запомни, ")
    message = SignatureDecorator(message, " - Джейсон Стетхем")
    message = DateDecorator(message, " 15.11.2026")
    assert message.render() == "Запомни, " + msg + " - Джейсон Стетхем 15.11.2026"
