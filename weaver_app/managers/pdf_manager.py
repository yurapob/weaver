class PDFManager:
    _instance = None
    selected_files = set()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PDFManager, cls).__new__(cls)
            cls.selected_files = set()
        return cls._instance

    @classmethod
    def add_file(cls, file_path):
        cls.selected_files.add(file_path)

    @classmethod
    def get_files(cls):
        return cls.selected_files