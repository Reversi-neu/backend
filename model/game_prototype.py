from abc import ABC, abstractmethod

# Interface for game prototype
class GamePrototype(ABC):
    @abstractmethod
    def copy(self):
        pass