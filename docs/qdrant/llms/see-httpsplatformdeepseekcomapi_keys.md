# See: https://platform.deepseek.com/api_keys
API_KEY = "<YOUR_DEEPSEEK_KEY>"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def query_deepseek(prompt):
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }

    response = requests.post(
        "https://api.deepseek.com/chat/completions", headers=HEADERS, data=json.dumps(data)
    )

    if response.ok:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

```

and also the query

```python
query_deepseek(prompt)

```

The response is:

```bash
"Building a web service that uses vector embeddings for search involves several components, including data processing, embedding generation, storage, search, and serving the service via an API. Below is a list of tools and technologies you can use for each step:\n\n---\n\n### 1. **Data Processing**\n   - **Python**: For general data preprocessing and scripting.\n   - **Pandas**: For handling tabular data.\n   - **NumPy**: For numerical operations.\n   - **NLTK/Spacy**: For text preprocessing (tokenization, stemming, etc.).\n   - **LLM models**: For generating embeddings if you're using pre-trained models.\n\n---\n\n### 2. **Embedding Generation**\n   - **Pre-trained Models**:\n     - Embeddings (e.g., `text-embedding-ada-002`).\n     - Hugging Face Transformers (e.g., `Sentence-BERT`, `all-MiniLM-L6-v2`).\n     - Google's Universal Sentence Encoder.\n   - **Custom Models**:\n     - TensorFlow/PyTorch: For training custom embedding models.\n   - **Libraries**:\n     - `sentence-transformers`: For generating sentence embeddings.\n     - `transformers`: For using Hugging Face models.\n\n---\n\n### 3. **Vector Storage**\n   - **Vector Databases**:\n     - Pinecone: Managed vector database for similarity search.\n     - Weaviate: Open-source vector search engine.\n     - Milvus: Open-source vector database.\n     - FAISS (Facebook AI Similarity Search): Library for efficient similarity search.\n     - Qdrant: Open-source vector search engine.\n     - Redis with RedisAI: For storing and querying vectors.\n   - **Traditional Databases with Vector Support**:\n     - PostgreSQL with pgvector extension.\n     - Elasticsearch with dense vector support.\n\n---\n\n### 4. **Search and Retrieval**\n   - **Similarity Search Algorithms**:\n     - Cosine similarity, Euclidean distance, or dot product for comparing vectors.\n   - **Libraries**:\n     - FAISS: For fast nearest-neighbor search.\n     - Annoy (Approximate Nearest Neighbors Oh Yeah): For approximate nearest neighbor search.\n   - **Vector Databases**: Most vector databases (e.g., Pinecone, Weaviate) come with built-in search capabilities.\n\n---\n\n### 5. **Web Service Framework**\n   - **Backend Frameworks**:\n     - Flask/Django/FastAPI (Python): For building RESTful APIs.\n     - Node.js/Express: If you prefer JavaScript.\n   - **API Documentation**:\n     - Swagger/OpenAPI: For documenting your API.\n   - **Authentication**:\n     - OAuth2, JWT: For securing your API.\n\n---\n\n### 6. **Deployment**\n   - **Containerization**:\n     - Docker: For packaging your application.\n   - **Orchestration**:\n     - Kubernetes: For managing containers at scale.\n   - **Cloud Platforms**:\n     - AWS (EC2, Lambda, S3).\n     - Google Cloud (Compute Engine, Cloud Functions).\n     - Azure (App Service, Functions).\n   - **Serverless**:\n     - AWS Lambda, Google Cloud Functions, or Vercel for serverless deployment.\n\n---\n\n### 7. **Monitoring and Logging**\n   - **Monitoring**:\n     - Prometheus + Grafana: For monitoring performance.\n   - **Logging**:\n     - ELK Stack (Elasticsearch, Logstash, Kibana).\n     - Fluentd.\n   - **Error Tracking**:\n     - Sentry.\n\n---\n\n### 8. **Frontend (Optional)**\n   - **Frontend Frameworks**:\n     - React, Vue.js, or Angular: For building a user interface.\n   - **Libraries**:\n     - Axios: For making API calls from the frontend.\n\n---\n\n### Example Workflow\n1. Preprocess your data (e.g., clean text, tokenize).\n2. Generate embeddings using a pre-trained model (e.g., Hugging Face).\n3. Store embeddings in a vector database (e.g., Pinecone or FAISS).\n4. Build a REST API using FastAPI or Flask to handle search queries.\n5. Deploy the service using Docker and Kubernetes or a serverless platform.\n6. Monitor and scale the service as needed.\n\n---\n\n### Example Tools Stack\n- **Embedding Generation**: Hugging Face `sentence-transformers`.\n- **Vector Storage**: Pinecone or FAISS.\n- **Web Framework**: FastAPI.\n- **Deployment**: Docker + AWS/GCP.\n\nBy combining these tools, you can build a scalable and efficient web service for vector embedding-based search."

```

### [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#extending-the-prompt) Extending the prompt

Even though the original answer sounds credible, it didn’t answer our question correctly. Instead, it gave us a generic description of an application stack. To improve the results, enriching the original prompt with the descriptions of the tools available seems like one of the possibilities. Let’s use a semantic knowledge base to augment the prompt with the descriptions of different technologies!

```python
results = client.query_points(
    collection_name=collection_name,
    query=models.Document(text=prompt, model=model_name),
    limit=3,
)
results

```

Here is the response:

```bash
QueryResponse(points=[\
    ScoredPoint(id=0, version=0, score=0.67437416, payload={'document': 'Qdrant is a vector database & vector similarity search engine. It deploys as an API service providing search for the nearest high-dimensional vectors. With Qdrant, embeddings or neural network encoders can be turned into full-fledged applications for matching, searching, recommending, and much more!'}, vector=None, shard_key=None, order_value=None),\
    ScoredPoint(id=6, version=0, score=0.63144326, payload={'document': 'SentenceTransformers is a Python framework for state-of-the-art sentence, text and image embeddings. You can use this framework to compute sentence / text embeddings for more than 100 languages. These embeddings can then be compared e.g. with cosine-similarity to find sentences with a similar meaning. This can be useful for semantic textual similar, semantic search, or paraphrase mining.'}, vector=None, shard_key=None, order_value=None),\
    ScoredPoint(id=5, version=0, score=0.6064749, payload={'document': 'FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.'}, vector=None, shard_key=None, order_value=None)\
])

```

We used the original prompt to perform a semantic search over the set of tool descriptions. Now we can use these descriptions to augment the prompt and create more context.

```python
context = "\n".join(r.payload['document'] for r in results.points)
context

```

The response is:

```bash
'Qdrant is a vector database & vector similarity search engine. It deploys as an API service providing search for the nearest high-dimensional vectors. With Qdrant, embeddings or neural network encoders can be turned into full-fledged applications for matching, searching, recommending, and much more!\nFastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.\nPyTorch is a machine learning framework based on the Torch library, used for applications such as computer vision and natural language processing.'

```

Finally, let’s build a metaprompt, the combination of the assumed role of the LLM, the original question, and the results from our semantic search that will force our LLM to use the provided context.

By doing this, we effectively convert the knowledge-oriented task into a language task and hopefully reduce the chances of hallucinations. It also should make the response sound more relevant.

```python
metaprompt = f"""
You are a software architect.
Answer the following question using the provided context.
If you can't find the answer, do not pretend you know it, but answer "I don't know".

Question: {prompt.strip()}

Context:
{context.strip()}

Answer:
"""