import tempfile
import shutil
import os


class PDFManager:
    _instance = None
    selected_files = set()
    temp_dir = ""

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PDFManager, cls).__new__(cls)
            cls.temp_dir = tempfile.mkdtemp()
            cls.selected_files = set()
        return cls._instance

    def add_file(self, file_path):
        if os.path.isfile(file_path):
            filename = os.path.basename(file_path)
            temp_file_path = os.path.join(self.temp_dir, filename)
            shutil.copy(file_path, temp_file_path)
            self.selected_files.add(temp_file_path)
        else:
            raise FileNotFoundError(f">>> File not found: {file_path}")

    @classmethod
    def get_files(cls):
        return cls.selected_files

    @classmethod
    def cleanup(cls):
        if cls.temp_dir and os.path.exists(cls.temp_dir):
            shutil.rmtree(cls.temp_dir)