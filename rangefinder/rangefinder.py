from abc import ABCMeta, abstractmethod
from types import FunctionType
from connection import Dispatcher
from request import Request


class RangeFinder(metaclass=ABCMeta):
    def __init__(self, dispatcher: Dispatcher):
        self._dispatcher = dispatcher

    @property
    def isConnected(self) -> bool:
        return self._dispatcher.isConnected()

    @abstractmethod
    def _sendMessage(self, request: Request):
        pass
