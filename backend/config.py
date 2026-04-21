from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
EMBEDDINGS_DIR = BASE_DIR / "embeddings"
FAISS_INDEX_DIR = EMBEDDINGS_DIR / "faiss_index"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

SIMILARITY_THRESHOLD = 0.6
TOP_K_RESULTS = 1
