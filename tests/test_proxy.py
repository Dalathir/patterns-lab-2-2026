from messages import Message
from decorators import HeaderDecorator, SignatureDecorator
from proxies.protected_message_proxy import ProtectedMessageProxy
from security import AccessPolicy, UserContext

msg = "Слышал, что скупой платит дважды, теперь хочу работать у скупого"


def test_1_proxy_allowed():
    proxy = ProtectedMessageProxy(
        Message(msg),
        AccessPolicy("reader"),
        UserContext.of("Доминик Торетто", "reader"),
    )
    assert proxy.render() == msg


def test_2_proxy_denied():
    proxy = ProtectedMessageProxy(
        Message(msg),
        AccessPolicy("reader"),
        UserContext.of("Дуэйн Джонсон", "guest"),
    )
    try:
        proxy.render()
    except PermissionError:
        pass
    else:
        assert False, "ожидался PermissionError"
