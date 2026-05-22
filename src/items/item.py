# THIS FILE CONTAINS THE ABSTRACT BASE CLASS FOR ALL ITEMS
# DEFINES THEIR NAME, DESCRIPTION AND VALUE

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, description, value=0):
        self.name = name
        self.description = description
        self.value = value

    @abstractmethod
    def use(self, target):
        pass