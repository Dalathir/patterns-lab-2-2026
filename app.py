from messages import Message

from decorators import HeaderDecorator, DateDecorator, SignatureDecorator, Base64Decorator
from proxies.protected_message_proxy import ProtectedMessageProxy
from security import AccessPolicy, UserContext

def main() -> None:
    message = Message("Что говорят крысы, за спиной у кисы")

    # Decorator: сообщение
    decorated = HeaderDecorator(message, "Неважно,")
    decorated = SignatureDecorator(decorated, " - Джейсон Стетхем")
    decorated = DateDecorator(decorated, " 15.11.2026")
    print(decorated.render())
    encoded = Base64Decorator(decorated)
    print(encoded.render())

    # Proxy: успешный доступ
    policy = AccessPolicy("reader")
    reader = UserContext.of("Киса", "reader")
    print(ProtectedMessageProxy(decorated, policy, reader).render())

    # Proxy: отказ в доступе
    guest = UserContext.of("Крыса", "guest")
    try:
        ProtectedMessageProxy(decorated, policy, guest).render()
    except PermissionError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
