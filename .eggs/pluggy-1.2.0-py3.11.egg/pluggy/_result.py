"""
Hook wrapper "result" utilities.
"""
from __future__ import annotations

from types import TracebackType
from typing import Callable
from typing import cast
from typing import Generator
from typing import Generic
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

if TYPE_CHECKING:
    from typing import NoReturn


_ExcInfo = Tuple[Type[BaseException], BaseException, Optional[TracebackType]]
_T = TypeVar("_T")


def _raise_wrapfail(
    wrap_controller: (
        Generator[None, _Result[_T], None] | Generator[None, object, object]
    ),
    msg: str,
) -> NoReturn:
    co = wrap_controller.gi_code
    raise RuntimeError(
        "wrap_controller at %r %s:%d %s"
        % (co.co_name, co.co_filename, co.co_firstlineno, msg)
    )


class HookCallError(Exception):
    """Hook was called incorrectly."""


class _Result(Generic[_T]):
    __slots__ = ("_result", "_exception")

    def __init__(
        self,
        result: _T | None,
        exception: BaseException | None,
    ) -> None:
        self._result = result
        self._exception = exception

    @property
    def excinfo(self) -> _ExcInfo | None:
        exc = self._exception
        if exc is None:
            return None
        else:
            return (type(exc), exc, exc.__traceback__)

    @property
    def exception(self) -> BaseException | None:
        return self._exception

    @classmethod
    def from_call(cls, func: Callable[[], _T]) -> _Result[_T]:
        __tracebackhide__ = True
        result = exception = None
        try:
            result = func()
        except BaseException as exc:
            exception = exc
        return cls(result, exception)

    def force_result(self, result: _T) -> None:
        """Force the result(s) to ``result``.

        If the hook was marked as a ``firstresult`` a single value should
        be set, otherwise set a (modified) list of results. Any exceptions
        found during invocation will be deleted.

        This overrides any previous result or exception.
        """
        self._result = result
        self._exception = None

    def force_exception(self, exception: BaseException) -> None:
        """Force the result to fail with ``exception``.

        This overrides any previous result or exception.

        .. versionadded:: 1.1.0
        """
        self._result = None
        self._exception = exception

    def get_result(self) -> _T:
        """Get the result(s) for this hook call.

        If the hook was marked as a ``firstresult`` only a single value
        will be returned, otherwise a list of results.
        """
        __tracebackhide__ = True
        exc = self._exception
        if exc is None:
            return cast(_T, self._result)
        else:
            raise exc.with_traceback(exc.__traceback__)
