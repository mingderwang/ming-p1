""" module Simple Factory  """
from abc import ABC, abstractmethod

class Phone(ABC):
    """ class Phone  """
    @abstractmethod
    def show(self):
        """ function show  """

class Samsung(Phone):
    """ class Samsung(Phone)  """
    def show(self):
        """ function show  """
        print(f"This is a Samsung phone with ID: {id(self)}")

class AppleIPhone(Phone):
    """ class AppleIPhone(Phone)  """
    def show(self):
        """ function show  """
        print(f"This is an Apple iphone with ID: {id(self)}")

class PhoneFactory:
    """ class Fonefactory  """
    @classmethod
    def create_type(cls, selected_type):
        """ function create_type  """
        return {
          'iphone': AppleIPhone(),
          'samsung': Samsung(),
        }[selected_type]
