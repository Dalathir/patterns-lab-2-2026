"""
Реализуйте ProtectedMessageProxy.

Proxy должен предоставлять интерфейс BaseMessage, проверять AccessPolicy
и делегировать render() реальному объекту только при наличии доступа.
"""

# TODO: реализуйте ProtectedMessageProxy.
from interfaces import BaseMessage
from security import AccessPolicy, UserContext


class ProtectedMessageProxy(BaseMessage):
    def __init__(self, msg: BaseMessage, role: AccessPolicy, user: UserContext) -> None:
        self._msg = msg
        self._role = role
        self._user = user

    def render(self) -> str:
        if not self._role.is_allowed(self._user):
            raise PermissionError(f"Недостаточно прав")
        return self._msg.render()