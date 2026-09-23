from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import faiss
import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

text_loader = TextLoader("./state_of_union.txt")
text_document = text_loader.load()
print(text_document[0].page_content[:100])

file_path ="./Michael_Resume.pdf"

pdf_loader = PyPDFLoader(file_path)
pdf_pages = pdf_loader.load_and_split()
print(pdf_pages[0].page_content[:100])

doc_splitter = RecursiveCharacterTextSplitter(chunk_size=1024,chunk_overlap=64)
split_texts = doc_splitter.split_documents(pdf_pages)
print(len(split_texts))

## Not able to run this code having long running time while stop it's give download error.
MODEL_NAME="sentence-transformers/all-MiniLM-L6-v2"
hf_embed = HuggingFaceEmbeddings(model_name=MODEL_NAME)
text = split_texts[0].page_content
hf_embed_result= hf_embed.embed_documents([text])
print(len(hf_embed_result[0]))

