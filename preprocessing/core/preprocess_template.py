from abc import ABC, abstractmethod


class PreprocessTemplate(ABC):

    @abstractmethod
    def read_data(self, *args, **kwargs):
        pass

    def process_data(self, *args, **kwargs):
        pass

    def store_data(self, *args, **kwargs):
        pass
