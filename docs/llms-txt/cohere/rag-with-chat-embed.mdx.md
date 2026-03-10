# Source: https://docs.cohere.com/page/rag-with-chat-embed.mdx

***

title: RAG With Chat Embed and Rerank via Pinecone
slug: /page/rag-with-chat-embed
description: This page contains a basic tutorial on how to build a RAG-powered chatbot.
image:
type: fileId
value: 'https://files.buildwithfern.com/cohere.docs.buildwithfern.com/8ba30b46486ea7bfab24f3e8856d7411d1b745b26e9026abff3ee62af52ce268/assets/images/f1cc130-cohere_meta_image.jpg'
keywords: 'Cohere, retrieval-augmented generation, RAG, chatbot'
----------------------------------------------------------------

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/RAG_with_Chat_Embed_and_Rerank_via_Pinecone.ipynb" />

This notebook shows how to build a RAG-powered chatbot with Cohere's Chat endpoint. The chatbot can extract relevant information from external documents and produce verifiable, inline citations in its responses.

This application will use several Cohere API endpoints:

* Chat: For handling the main logic of the chatbot, including turning a user message into queries, generating responses, and producing citations
* Embed: For turning textual documents into their embeddings representation, later to be used in retrieval (we’ll use the latest, state-of-the-art Embed v4 model)
* Rerank: For reranking the retrieved documents according to their relevance to a query

The diagram below provides an overview of what we’ll build.

Here is a summary of the steps involved.

Initial phase:

* **Step 0**: Ingest the documents – get documents, chunk, embed, and index.

For each user-chatbot interaction:

* **Step 1**: Get the user message
* **Step 2**: Call the Chat endpoint in query-generation mode
* If at least one query is generated
  * **Step 3**: Retrieve and rerank relevant documents
  * **Step 4**: Call the Chat endpoint in document mode to generate a grounded response with citations
* If no query is generated
  * **Step 4**: Call the Chat endpoint in normal mode to generate a response

```python PYTHON
! pip install cohere hnswlib unstructured python-dotenv -q
```

```python PYTHON
import cohere
from pinecone import Pinecone, PodSpec
import uuid
import hnswlib
from typing import List, Dict
from unstructured.partition.html import partition_html
from unstructured.chunking.title import chunk_by_title

co = cohere.Client("COHERE_API_KEY") # Get your API key here: https://dashboard.cohere.com/api-keys
pc = Pinecone(api_key="PINECONE_API_KEY") # (get API key at app.pinecone.io)
```

```python PYTHON
import cohere
import os
import dotenv

dotenv.load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

```

First, we define the list of documents we want to ingest and make available for retrieval. As an example, we'll use the contents from the first module of Cohere's *LLM University: What are Large Language Models?*.

```python PYTHON
raw_documents = [
    {
        "title": "Text Embeddings",
        "url": "https://docs.cohere.com/docs/text-embeddings"},
    {
        "title": "Similarity Between Words and Sentences",
        "url": "https://docs.cohere.com/docs/similarity-between-words-and-sentences"},
    {
        "title": "The Attention Mechanism",
        "url": "https://docs.cohere.com/docs/the-attention-mechanism"},
    {
        "title": "Transformer Models",
        "url": "https://docs.cohere.com/docs/transformer-models"}
]
```

Usually the number of documents for practical applications is vast, and so we'll need to be able to search documents efficiently. This involves breaking the documents into chunks, generating embeddings, and indexing the embeddings, as shown in the image below.

We implement this in the `Vectorstore` class below, which takes the `raw_documents` list as input. Three methods are immediately called when creating an object of the `Vectorstore` class:

`load_and_chunk()`\
This method uses the `partition_html()` method from the `unstructured` library to load the documents from URL and break them into smaller chunks. Each chunk is turned into a dictionary object with three fields:

* `title` - the web page’s title,
* `text` - the textual content of the chunk, and
* `url` - the web page’s URL.

`embed()`\
This method uses Cohere's `embed-v4.0` model to generate embeddings of the chunked documents. Since our documents will be used for retrieval, we set `input_type="search_document"`. We send the documents to the Embed endpoint in batches, because the endpoint has a limit of 96 documents per call.

`index()`\
This method uses the `hsnwlib` package to index the document chunk embeddings. This will ensure efficient similarity search during retrieval. Note that `hnswlib` uses a vector library, and we have chosen it for its simplicity.

```python PYTHON
class Vectorstore:
    """
    A class representing a collection of documents indexed into a vectorstore.

    Parameters:
    raw_documents (list): A list of dictionaries representing the sources of the raw documents. Each dictionary should have 'title' and 'url' keys.

    Attributes:
    raw_documents (list): A list of dictionaries representing the raw documents.
    docs (list): A list of dictionaries representing the chunked documents, with 'title', 'text', and 'url' keys.
    docs_embs (list): A list of the associated embeddings for the document chunks.
    docs_len (int): The number of document chunks in the collection.
    idx (hnswlib.Index): The index used for document retrieval.

    Methods:
    load_and_chunk(): Loads the data from the sources and partitions the HTML content into chunks.
    embed(): Embeds the document chunks using the Cohere API.
    index(): Indexes the document chunks for efficient retrieval.
    retrieve(): Retrieves document chunks based on the given query.
    """

    def __init__(self, raw_documents: List[Dict[str, str]]):
        self.raw_documents = raw_documents
        self.docs = []
        self.docs_embs = []
        self.retrieve_top_k = 10
        self.rerank_top_k = 3
        self.load_and_chunk()
        self.embed()
        self.index()


    def load_and_chunk(self) -> None:
        """
        Loads the text from the sources and chunks the HTML content.
        """
        print("Loading documents...")

        for raw_document in self.raw_documents:
            elements = partition_html(url=raw_document["url"])
            chunks = chunk_by_title(elements)
            for chunk in chunks:
                self.docs.append(
                    {
                        "title": raw_document["title"],
                        "text": str(chunk),
                        "url": raw_document["url"],
                    }
                )

    def embed(self) -> None:
        """
        Embeds the document chunks using the Cohere API.
        """
        print("Embedding document chunks...")

        batch_size = 90
        self.docs_len = len(self.docs)
        for i in range(0, self.docs_len, batch_size):
            batch = self.docs[i : min(i + batch_size, self.docs_len)]
            texts = [item["text"] for item in batch]
            docs_embs_batch = co.embed(
                texts=texts, model="embed-v4.0", input_type="search_document"
            ).embeddings
            self.docs_embs.extend(docs_embs_batch)

    def index(self) -> None:
        """
        Indexes the documents for efficient retrieval.
        """
        print("Indexing documents...")

        index_name = 'rag-01'

        # If the index does not exist, we create it
        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=len(self.docs_embs[0]),
                metric="cosine",
                spec=PodSpec(
                    environment="gcp-starter"
                )
                )

        # connect to index
        self.idx = pc.Index(index_name)

        batch_size = 128

        ids = [str(i) for i in range(len(self.docs))]
        # create list of metadata dictionaries
        meta = self.docs

        # create list of (id, vector, metadata) tuples to be upserted
        to_upsert = list(zip(ids, self.docs_embs, meta))

        for i in range(0, len(self.docs), batch_size):
            i_end = min(i+batch_size, len(self.docs))
            self.idx.upsert(vectors=to_upsert[i:i_end])

        # let's view the index statistics
        print("Indexing complete")


    def retrieve(self, query: str) -> List[Dict[str, str]]:
        """
        Retrieves document chunks based on the given query.

        Parameters:
        query (str): The query to retrieve document chunks for.

        Returns:
        List[Dict[str, str]]: A list of dictionaries representing the retrieved document chunks, with 'title', 'text', and 'url' keys.
        """

        docs_retrieved = []
        query_emb = co.embed(
            texts=[query], model="embed-v4.0", input_type="search_query"
        ).embeddings


        res = self.idx.query(vector=query_emb, top_k=self.retrieve_top_k, include_metadata=True)
        docs_to_rerank = [match['metadata']['text'] for match in res['matches']]

        rerank_results = co.rerank(
            query=query,
            documents=docs_to_rerank,
            top_n=self.rerank_top_k,
            model="rerank-english-v2.0",
        )

        docs_reranked = [res['matches'][result.index] for result in rerank_results.results]

        for doc in docs_reranked:
            docs_retrieved.append(doc['metadata'])

        return docs_retrieved
```

In the code cell below, we initialize an instance of the `Vectorstore` class and pass in the `raw_documents` list as input.

```python PYTHON
vectorstore = Vectorstore(raw_documents)
```

```
Loading documents...
Embedding document chunks...
Indexing documents...
Indexing complete
```

The `Vectorstore` class also has a `retrieve()` method, which we'll use to retrieve relevant document chunks given a query (as in Step 3 in the diagram shared at the beginning of this notebook). This method has two components: (1) dense retrieval, and (2) reranking.

### Dense retrieval

First, we embed the query using the same `embed-v4.0` model we used to embed the document chunks, but this time we set `input_type="search_query"`.

Search is performed by the `knn_query()` method from the `hnswlib` library. Given a query, it returns the document chunks most similar to the query. We can define the number of document chunks to return using the attribute `self.retrieve_top_k=10`.

### Reranking

After semantic search, we implement a reranking step. While our semantic search component is already highly capable of retrieving relevant sources, the [Rerank endpoint](https://cohere.com/rerank) provides an additional boost to the quality of the search results, especially for complex and domain-specific queries. It takes the search results and sorts them according to their relevance to the query.

We call the Rerank endpoint with the `co.rerank()` method and define the number of top reranked document chunks to retrieve using the attribute `self.rerank_top_k=3`. The model we use is `rerank-english-v2.0`.

This method returns the top retrieved document chunks `chunks_retrieved` so that they can be passed to the chatbot.

In the code cell below, we check the document chunks that are retrieved for the query `"multi-head attention definition"`.

## Test Retrieval

```python PYTHON
vectorstore.retrieve("multi-head attention definition")
```

```
[{'text': 'The attention step used in transformer models is actually much more powerful, and it’s called multi-head attention. In multi-head attention, several different embeddings are used to modify the vectors and add context to them. Multi-head attention has helped language models reach much higher levels of efficacy when processing and generating text.',
  'title': 'Transformer Models',
  'url': 'https://docs.cohere.com/docs/transformer-models'},
 {'text': "What you learned in this chapter is simple self-attention. However, we can do much better than that. There is a method called multi-head attention, in which one doesn't only consider one embedding, but several different ones. These are all obtained from the original by transforming it in different ways. Multi-head attention has been very successful at the task of adding context to text. If you'd like to learn more about the self and multi-head attention, you can check out the following two",
  'title': 'The Attention Mechanism',
  'url': 'https://docs.cohere.com/docs/the-attention-mechanism'},
 {'text': 'Attention helps give context to each word, based on the other words in the sentence (or text).',
  'title': 'Transformer Models',
  'url': 'https://docs.cohere.com/docs/transformer-models'}]
```

Next, we implement a class to handle the interaction between the user and the chatbot. It takes an instance of the `Vectorstore` class as input.

The `run()` method will be used to run the chatbot application. It begins with the logic for getting the user message, along with a way for the user to end the conversation.

Based on the user message, the chatbot needs to decide if it needs to consult external information before responding. If so, the chatbot determines an optimal set of search queries to use for retrieval. When we call `co.chat()` with `search_queries_only=True`, the Chat endpoint handles this for us automatically.

The generated queries can be accessed from the `search_queries` field of the object that is returned. Then, what happens next depends on how many queries are returned.

* If queries are returned, we call the `retrieve()` method of the Vectorstore object for the retrieval step. The retrieved document chunks are then passed to the Chat endpoint by adding a `documents` parameter when we call `co.chat()` again.
* Otherwise, if no queries are returned, we call the Chat endpoint another time, passing the user message and without needing to add any documents to the call.

In either case, we also pass the `conversation_id` parameter, which retains the interactions between the user and the chatbot in the same conversation thread. We also enable the `stream` parameter so we can stream the chatbot response.

We then print the chatbot's response. In the case that the external information was used to generate a response, we also display citations.

```python PYTHON
class Chatbot:
    def __init__(self, vectorstore: Vectorstore):
        """
        Initializes an instance of the Chatbot class.

        Parameters:
        vectorstore (Vectorstore): An instance of the Vectorstore class.

        """
        self.vectorstore = vectorstore
        self.conversation_id = str(uuid.uuid4())

    def run(self):
        """
        Runs the chatbot application.

        """
        while True:
            # Get the user message
            message = input("User: ")

            # Typing "quit" ends the conversation
            if message.lower() == "quit":
              print("Ending chat.")
              break
            # else:                       # Uncomment for Google Colab to avoid printing the same thing twice
              # print(f"User: {message}") # Uncomment for Google Colab to avoid printing the same thing twice

            # Generate search queries (if any)
            response = co.chat(message=message,
                               model="command-r",
                               search_queries_only=True)

            # If there are search queries, retrieve document chunks and respond
            if response.search_queries:
                print("Retrieving information...", end="")

                # Retrieve document chunks for each query
                documents = []
                for query in response.search_queries:
                    documents.extend(self.vectorstore.retrieve(query.text))

                # Use document chunks to respond
                response = co.chat_stream(
                    message=message,
                    model="command-r",
                    documents=documents,
                    conversation_id=self.conversation_id,
                )

            # If there is no search query, directly respond
            else:
                response = co.chat_stream(
                    message=message,
                    model="command-r",
                    conversation_id=self.conversation_id,
                )

            # Print the chatbot response, citations, and documents
            print("\nChatbot:")
            citations = []
            cited_documents = []

            # Display response
            for event in response:
                if event.event_type == "text-generation":
                    print(event.text, end="")
                elif event.event_type == "citation-generation":
                    citations.extend(event.citations)
                elif event.event_type == "search-results":
                    cited_documents = event.documents

            # Display citations and source documents
            if citations:
              print("\n\nCITATIONS:")
              for citation in citations:
                print(citation)

              print("\nDOCUMENTS:")
              for document in cited_documents:
                print(document)

            print(f"\n{'-'*100}\n")
```

We can now run the chatbot. For this, we create the instance of `Chatbot` and run the chatbot by invoking the `run()` method.

The format of each citation is:

* `start`: The starting point of a span where one or more documents are referenced
* `end`: The ending point of a span where one or more documents are referenced
* `text`: The text representing this span
* `document_ids`: The IDs of the documents being referenced (`doc_0` being the ID of the first document passed to the `documents` creating parameter in the endpoint call, and so on)

```python PYTHON
chatbot = Chatbot(vectorstore)

chatbot.run()
```

```
Chatbot:
Hello! What's your question? I'm here to help you in any way I can.
----------------------------------------------------------------------------------------------------

Retrieving information...
Chatbot:
Word embeddings associate words with lists of numbers, so that similar words are close to each other and dissimilar words are further away.
Sentence embeddings do the same thing, but for sentences. Each sentence is associated with a vector of numbers in a coherent way, so that similar sentences are assigned similar vectors, and different sentences are given different vectors.

CITATIONS:
start=0 end=15 text='Word embeddings' document_ids=['doc_0']
start=16 end=53 text='associate words with lists of numbers' document_ids=['doc_0']
start=63 end=100 text='similar words are close to each other' document_ids=['doc_0']
start=105 end=139 text='dissimilar words are further away.' document_ids=['doc_0']
start=140 end=159 text='Sentence embeddings' document_ids=['doc_0', 'doc_2']
start=160 end=177 text='do the same thing' document_ids=['doc_0', 'doc_2']
start=198 end=211 text='Each sentence' document_ids=['doc_0', 'doc_2']
start=215 end=250 text='associated with a vector of numbers' document_ids=['doc_0', 'doc_2']
start=256 end=264 text='coherent' document_ids=['doc_2']
start=278 end=295 text='similar sentences' document_ids=['doc_0', 'doc_2']
start=300 end=324 text='assigned similar vectors' document_ids=['doc_0', 'doc_2']
start=330 end=349 text='different sentences' document_ids=['doc_0', 'doc_2']
start=354 end=378 text='given different vectors.' document_ids=['doc_0', 'doc_2']

DOCUMENTS:
{'id': 'doc_0', 'text': 'In the previous chapters, you learned about word and sentence embeddings and similarity between words and sentences. In short, a word embedding is a way to associate words with lists of numbers (vectors) in such a way that similar words are associated with numbers that are close by, and dissimilar words with numbers that are far away from each other. A sentence embedding does the same thing, but associating a vector to every sentence. Similarity is a way to measure how similar two words (or', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_1', 'text': 'Sentence embeddings\n\nSo word embeddings seem to be pretty useful, but in reality, human language is much more complicated than simply a bunch of words put together. Human language has structure, sentences, etc. How would one be able to represent, for instance, a sentence? Well, here’s an idea. How about the sums of scores of all the words? For example, say we have a word embedding that assigns the following scores to these words:\n\nNo: [1,0,0,0]\n\nI: [0,2,0,0]\n\nAm: [-1,0,1,0]\n\nGood: [0,0,1,3]', 'title': 'Text Embeddings', 'url': 'https://docs.cohere.com/docs/text-embeddings'}
{'id': 'doc_2', 'text': 'This is where sentence embeddings come into play. A sentence embedding is just like a word embedding, except it associates every sentence with a vector full of numbers, in a coherent way. By coherent, I mean that it satisfies similar properties as a word embedding. For instance, similar sentences are assigned to similar vectors, different sentences are assigned to different vectors, and most importantly, each of the coordinates of the vector identifies some (whether clear or obscure) property of', 'title': 'Text Embeddings', 'url': 'https://docs.cohere.com/docs/text-embeddings'}

----------------------------------------------------------------------------------------------------

Retrieving information...
Chatbot:
The similarities between words and sentences are both quantitative measures of how close the two given items are. There are two types of similarities that can be defined: dot product similarity, and cosine similarity. These methods can determine how similar two words, or sentences, are.

CITATIONS:
start=54 end=75 text='quantitative measures' document_ids=['doc_0']
start=79 end=88 text='how close' document_ids=['doc_0']
start=124 end=133 text='two types' document_ids=['doc_0', 'doc_4']
start=171 end=193 text='dot product similarity' document_ids=['doc_0', 'doc_4']
start=199 end=217 text='cosine similarity.' document_ids=['doc_0', 'doc_4']
start=236 end=257 text='determine how similar' document_ids=['doc_0', 'doc_4']

DOCUMENTS:
{'id': 'doc_0', 'text': 'Now that we know embeddings quite well, let’s move on to using them to find similarities. There are two types of similarities we’ll define in this post: dot product similarity and cosine similarity. Both are very similar and very useful to determine if two words (or sentences) are similar.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_1', 'text': 'But let me add some numbers to this reasoning to make it more clear. Imagine that we calculate similarities for the words in each sentence, and we get the following:\n\nThis similarity makes sense in the following ways:\n\nThe similarity between each word and itself is 1.\n\nThe similarity between any irrelevant word (“the”, “of”, etc.) and any other word is 0.\n\nThe similarity between “bank” and “river” is 0.11.\n\nThe similarity between “bank” and “money” is 0.25.', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_2', 'text': 'And the results are:\n\nThe similarity between sentences 1 and 2: 6738.2858668486715\n\nThe similarity between sentences 1 and 3: -122.22666955510499\n\nThe similarity between sentences 2 and 3: -3.494608113647928\n\nThese results certainly confirm our predictions. The similarity between sentences 1 and 2 is 6738, which is high. The similarities between sentences 1 and 3, and 2 and 3, are -122 and -3.5 (dot products are allowed to be negative too!), which are much lower.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_3', 'text': 'But let me add some numbers to this reasoning to make it more clear. Imagine that we calculate similarities for the words in each sentence, and we get the following:\n\nThis similarity makes sense in the following ways:\n\nThe similarity between each word and itself is 1.\n\nThe similarity between any irrelevant word (“the”, “of”, etc.) and any other word is 0.\n\nThe similarity between “bank” and “river” is 0.11.\n\nThe similarity between “bank” and “money” is 0.25.', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_4', 'text': 'Now that we know embeddings quite well, let’s move on to using them to find similarities. There are two types of similarities we’ll define in this post: dot product similarity and cosine similarity. Both are very similar and very useful to determine if two words (or sentences) are similar.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_5', 'text': 'And the results are:\n\nThe similarity between sentences 1 and 2: 6738.2858668486715\n\nThe similarity between sentences 1 and 3: -122.22666955510499\n\nThe similarity between sentences 2 and 3: -3.494608113647928\n\nThese results certainly confirm our predictions. The similarity between sentences 1 and 2 is 6738, which is high. The similarities between sentences 1 and 3, and 2 and 3, are -122 and -3.5 (dot products are allowed to be negative too!), which are much lower.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}

----------------------------------------------------------------------------------------------------

Ending chat.
```
