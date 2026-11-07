import os
import pickle

class FileManager:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def path(cls, file_name):
        return os.path.join(cls.BASE_DIR, file_name)

    @classmethod
    def load(cls, file_name):
        path = cls.path(file_name)
        if not os.path.exists(path):
            return []
        with open(path, "rb") as file:
            try:
                return pickle.load(file)
            except (EOFError, pickle.UnpicklingError):
                return []

    @classmethod
    def save(cls, file_name, data):
        path = cls.path(file_name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as file:
            pickle.dump(data, file)
