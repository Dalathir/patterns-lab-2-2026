"""
Базовый Decorator и конкретные декораторы необходимо реализовать самостоятельно.

Подсказка: все декораторы должны удовлетворять интерфейсу BaseMessage и
работать с другим объектом BaseMessage через композицию.
"""

# TODO:
# - MessageDecorator
# - HeaderDecorator
# - SignatureDecorator
# - DateDecorator
# - Base64Decorator

import base64
from interfaces import BaseMessage

# базовый
class MessageDecorator(BaseMessage):
    def __init__(self, msg: BaseMessage) -> None:
        self._msg = msg

    def render(self) -> str:
        return self._msg.render()

# заголовок
class HeaderDecorator(MessageDecorator):
    def __init__(self, msg: BaseMessage, header: str) -> None:
        super().__init__(msg)
        self.header = header

    def render(self) -> str:
        return self.header + self._msg.render()

# подпись после
class SignatureDecorator(MessageDecorator):
    def __init__(self, msg: BaseMessage, signature: str) -> None:
        super().__init__(msg)
        self.signature = signature

    def render(self) -> str:
        return self._msg.render() + self.signature

# дата после сообщения
class DateDecorator(MessageDecorator):
    def __init__(self, msg: BaseMessage, date: str) -> None:
        super().__init__(msg)
        self.date = date

    def render(self) -> str:
        return self._msg.render() + self.date

# base64
class Base64Decorator(MessageDecorator):
    def render(self) -> str:
        return base64.b64encode(self._msg.render().encode("utf-8")).decode("utf-8")