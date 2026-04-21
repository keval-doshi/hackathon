from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from backend.config import DATA_DIR, FAISS_INDEX_DIR
from dotenv import load_dotenv

load_dotenv()

headers_to_split_on = [
    ("#", "tool"),
    ("##", "problem")
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
all_docs = []

for md_file in DATA_DIR.glob("*.md"):
    print(f"📄 Reading: {md_file.name}")
    markdown_text = md_file.read_text(encoding="utf-8")
    docs = splitter.split_text(markdown_text)
    for doc in docs:
        doc.metadata["source"] = md_file.name
    all_docs.extend(docs)

print(f"\n✅ Total chunks created: {len(all_docs)}")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(all_docs, embeddings)
FAISS_INDEX_DIR.mkdir(parents=True, exist_ok=True)
vectorstore.save_local(str(FAISS_INDEX_DIR))

print(f"\n🎉 FAISS index saved at: {FAISS_INDEX_DIR}")
