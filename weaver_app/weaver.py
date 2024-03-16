from ui.app import App
from dotenv import load_dotenv
from managers.pdf_manager import PDFManager


if __name__ == "__main__":
    load_dotenv()

    app = App()
    app.mainloop()

    PDFManager.cleanup()