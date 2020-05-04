from typing import Callable, Any
from moretypes import Nil


class Option:
    def get(self) -> Any:
        return Nil


class Something(Option):
    def __init__(self, value):
        self.value = value

    def get(self) -> Any:
        return self.value

    def __str__(self) -> str:
        return "Something({})".format(str(self.value))


class Nothing(Option):
    def __init__(self, value):
        self.value = value

    def get(self) -> Any:
        return self.value

    def __str__(self) -> str:
        return "Nothing({})".format(str(self.value))


def Try(function: Callable) -> Option:
    """
    Try acts as the constructor for objects of type Option. You should never
    call constructors for Something or Nothing directly. The idiomatic way to
    use this companion function is: `x = Try(lambda: add(1, 2))`
    """
    try:
        return Something(function())
    except Exception as e:
        return Nothing(e)
