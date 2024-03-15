from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core.prompts import Prompt
from llama_index.core.chat_engine.condense_question import CondenseQuestionChatEngine
from managers.pdf_manager import PDFManager


class DocumentQueryEngine:
    def __init__(self):
        self.index = self.load_data(PDFManager.temp_dir)
        self.chat_engine = self.create_custom_chat_engine(self.index)

    @staticmethod
    def load_data(input_dir):
        reader = SimpleDirectoryReader(input_dir=input_dir, recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.1))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

    @staticmethod
    def create_custom_chat_engine(index):
        template = (
            "Following Informations : \n"
            "---------------------\n"
            "{context_str}"
            "\n---------------------\n"
            "Please answer the question: {query_str}\n"
        )
        qa_template = Prompt(template)

        query_engine = index.as_query_engine(text_qa_template=qa_template)
        chat_engine = CondenseQuestionChatEngine.from_defaults(
            query_engine=query_engine,
            verbose=False
        )
        return chat_engine

    def ask_question(self, question):
        bot_message = self.chat_engine.chat(question)
        return bot_message
