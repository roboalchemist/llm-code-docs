# setup.py

import os
from dotenv import load_dotenv # remove if not using dotenv
from langchain.vectorstores import Meilisearch
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import JSONLoader

load_dotenv() # remove if not using dotenv