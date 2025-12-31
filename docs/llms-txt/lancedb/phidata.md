# Source: https://docs.lancedb.com/integrations/data/phidata.md

# Phidata

export const PyPlatformsPhidataTranscriptModule = "import re\n\nfrom youtube_transcript_api import YouTubeTranscriptApi\n\ndef smodify(seconds):\n    hours, remainder = divmod(seconds, 3600)\n    minutes, seconds = divmod(remainder, 60)\n    return f\"{int(hours):02}:{int(minutes):02}:{int(seconds):02}\"\n\ndef extract_transcript(youtube_url, segment_duration):\n    # Extract video ID from the URL\n    video_id = re.search(r\"(?<=v=)[\\w-]+\", youtube_url)\n    if not video_id:\n        video_id = re.search(r\"(?<=be/)[\\w-]+\", youtube_url)\n    if not video_id:\n        return None\n\n    video_id = video_id.group(0)\n\n    # Attempt to fetch the transcript\n    try:\n        # Try to get the official transcript\n        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[\"en\"])\n    except Exception:\n        # If no official transcript is found, try to get auto-generated transcript\n        try:\n            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)\n            for transcript in transcript_list:\n                transcript = transcript.translate(\"en\").fetch()\n        except Exception:\n            return None\n\n    # Format the transcript into 120s chunks\n    transcript_text, dict_transcript = format_transcript(\n        transcript, segment_duration\n    )\n    # Open the file in write mode, which creates it if it doesn't exist\n    with open(\"transcript.txt\", \"w\", encoding=\"utf-8\") as file:\n        file.write(transcript_text)\n    return transcript_text, dict_transcript\n\ndef format_transcript(transcript, segment_duration):\n    chunked_transcript = []\n    chunk_dict = []\n    current_chunk = []\n    current_time = 0\n    # 2 minutes in seconds\n    start_time_chunk = 0  # To track the start time of the current chunk\n\n    for segment in transcript:\n        start_time = segment[\"start\"]\n        end_time_x = start_time + segment[\"duration\"]\n        text = segment[\"text\"]\n\n        # Add text to the current chunk\n        current_chunk.append(text)\n\n        # Update the current time with the duration of the current segment\n        # The duration of the current segment is given by segment['start'] - start_time_chunk\n        if current_chunk:\n            current_time = start_time - start_time_chunk\n\n        # If current chunk duration reaches or exceeds 2 minutes, save the chunk\n        if current_time >= segment_duration:\n            # Use the start time of the first segment in the current chunk as the timestamp\n            chunked_transcript.append(\n                f\"[{smodify(start_time_chunk)} to {smodify(end_time_x)}] \"\n                + \" \".join(current_chunk)\n            )\n            current_chunk = re.sub(\n                r\"[\\xa0\\n]\",\n                lambda x: \"\" if x.group() == \"\\xa0\" else \" \",\n                \"\\n\".join(current_chunk),\n            )\n            chunk_dict.append(\n                {\n                    \"timestamp\": f\"[{smodify(start_time_chunk)} to {smodify(end_time_x)}]\",\n                    \"text\": \"\".join(current_chunk),\n                }\n            )\n            current_chunk = []  # Reset the chunk\n            start_time_chunk = (\n                start_time + segment[\"duration\"]\n            )  # Update the start time for the next chunk\n            current_time = 0  # Reset current time\n\n    # Add any remaining text in the last chunk\n    if current_chunk:\n        chunked_transcript.append(\n            f\"[{smodify(start_time_chunk)} to {smodify(end_time_x)}] \"\n            + \" \".join(current_chunk)\n        )\n        current_chunk = re.sub(\n            r\"[\\xa0\\n]\",\n            lambda x: \"\" if x.group() == \"\\xa0\" else \" \",\n            \"\\n\".join(current_chunk),\n        )\n        chunk_dict.append(\n            {\n                \"timestamp\": f\"[{smodify(start_time_chunk)} to {smodify(end_time_x)}]\",\n                \"text\": \"\".join(current_chunk),\n            }\n        )\n\n    return \"\\n\\n\".join(chunked_transcript), chunk_dict\n";

export const PyPlatformsPhidataOpenaiSetup = "import os\n\nimport openai\nfrom phi.assistant import Assistant\nfrom phi.embedder.openai import OpenAIEmbedder\nfrom phi.knowledge.text import TextKnowledgeBase\nfrom phi.llm.openai import OpenAIChat\nfrom phi.vectordb.lancedb import LanceDb\nfrom rich.prompt import Prompt\nfrom transcript import extract_transcript\n\nif \"OPENAI_API_KEY\" not in os.environ:\n    # OR set the key here as a variable\n    openai.api_key = \"sk-...\"\n\n# The code below creates a file \"transcript.txt\" in the directory, the txt file will be used below\nyoutube_url = \"https://www.youtube.com/watch?v=Xs33-Gzl8Mo\"\nsegment_duration = 20\ntranscript_text, dict_transcript = extract_transcript(youtube_url, segment_duration)\n";

export const PyPlatformsPhidataOpenaiKnowledgeBase = "# Create knowledge Base with OpenAIEmbedder in LanceDB\nknowledge_base = TextKnowledgeBase(\n    path=\"transcript.txt\",\n    vector_db=LanceDb(\n        embedder=OpenAIEmbedder(api_key=openai.api_key),\n        table_name=\"transcript_documents\",\n        uri=\"./t3mp/.lancedb\",\n    ),\n    num_documents=10,\n)\n";

export const PyPlatformsPhidataOpenaiAssistant = "# define an assistant with gpt-4o-mini llm and reference to the knowledge base created above\nassistant = Assistant(\n    llm=OpenAIChat(\n        model=\"gpt-4o-mini\",\n        max_tokens=1000,\n        temperature=0.3,\n        api_key=openai.api_key,\n    ),\n    description=\"\"\"You are an Expert in explaining youtube video transcripts. You are a bot that takes transcript of a video and answer the question based on it.\n\n    This is transcript for the above timestamp: {relevant_document}\n    The user input is: {user_input}\n    generate highlights only when asked.\n    When asked to generate highlights from the video, understand the context for each timestamp and create key highlight points, answer in following way -\n    [timestamp] - highlight 1\n    [timestamp] - highlight 2\n    ... so on\n\n    Your task is to understand the user question, and provide an answer using the provided contexts. Your answers are correct, high-quality, and written by an domain expert. If the provided context does not contain the answer, simply state,'The provided context does not have the answer.'\"\"\",\n    knowledge_base=knowledge_base,\n    add_references_to_prompt=True,\n)\n";

export const PyPlatformsPhidataOllamaSetup = "from phi.assistant import Assistant\nfrom phi.embedder.ollama import OllamaEmbedder\nfrom phi.knowledge.text import TextKnowledgeBase\nfrom phi.llm.ollama import Ollama\nfrom phi.vectordb.lancedb import LanceDb\nfrom rich.prompt import Prompt\nfrom transcript import extract_transcript\n\n# The code below creates a file \"transcript.txt\" in the directory, the txt file will be used below\nyoutube_url = \"https://www.youtube.com/watch?v=Xs33-Gzl8Mo\"\nsegment_duration = 20\ntranscript_text, dict_transcript = extract_transcript(youtube_url, segment_duration)\n";

export const PyPlatformsPhidataOllamaKnowledgeBase = "# Create knowledge Base with OllamaEmbedder in LanceDB\nknowledge_base = TextKnowledgeBase(\n    path=\"transcript.txt\",\n    vector_db=LanceDb(\n        embedder=OllamaEmbedder(model=\"nomic-embed-text\", dimensions=768),\n        table_name=\"transcript_documents\",\n        uri=\"./t2mp/.lancedb\",\n    ),\n    num_documents=10,\n)\n";

export const PyPlatformsPhidataOllamaAssistant = "# define an assistant with llama3.1 llm and reference to the knowledge base created above\nassistant = Assistant(\n    llm=Ollama(model=\"llama3.1\"),\n    description=\"\"\"You are an Expert in explaining youtube video transcripts. You are a bot that takes transcript of a video and answer the question based on it.\n\n    This is transcript for the above timestamp: {relevant_document}\n    The user input is: {user_input}\n    generate highlights only when asked.\n    When asked to generate highlights from the video, understand the context for each timestamp and create key highlight points, answer in following way -\n    [timestamp] - highlight 1\n    [timestamp] - highlight 2\n    ... so on\n\n    Your task is to understand the user question, and provide an answer using the provided contexts. Your answers are correct, high-quality, and written by an domain expert. If the provided context does not contain the answer, simply state,'The provided context does not have the answer.'\"\"\",\n    knowledge_base=knowledge_base,\n    add_references_to_prompt=True,\n)\n";

export const PyPlatformsPhidataLoadKnowledgeBase = "assistant.knowledge_base.load(recreate=False)\n";

export const PyPlatformsPhidataDocumentModel = "from typing import Any, Dict, List, Optional\n\nfrom pydantic import BaseModel\n\nclass Document(BaseModel):\n    \"\"\"Model for managing a document\"\"\"\n\n    content: str  # <--- here data of chunk is stored\n    id: Optional[str] = None\n    name: Optional[str] = None\n    meta_data: Dict[str, Any] = {}\n    embedder: Optional[\"Embedder\"] = None\n    embedding: Optional[List[float]] = None\n    usage: Optional[Dict[str, Any]] = None\n";

export const PyPlatformsPhidataCliChat = "assistant.print_response(\"Ask me about something from the knowledge base\")\nwhile True:\n    message = Prompt.ask(f\"[bold] :sunglasses: User [/bold]\")\n    if message in (\"exit\", \"bye\"):\n        break\n    assistant.print_response(message, markdown=True)\n";

[Phidata](https://docs.phidata.com/introduction) is a framework for building **AI Assistants** with long-term memory, contextual knowledge, and the ability to take actions using function calling. It helps turn general-purpose LLMs into specialized assistants tailored to your use case by extending its capabilities using **memory**, **knowledge**, and **tools**.

* **Memory**: Stores chat history in a **database** and enables LLMs to have long-term conversations.
* **Knowledge**: Stores information in a **vector database** and provides LLMs with business context. (Here we will use LanceDB)
* **Tools**: Enable LLMs to take actions like pulling data from an **API**, **sending emails** or **querying a database**, etc.

![example](https://raw.githubusercontent.com/lancedb/assets/refs/heads/main/docs/assets/integration/phidata_assistant.png)

Memory & knowledge make LLMs *smarter* while tools make them *autonomous*.

LanceDB is a vector database and its integration into Phidata makes it easy for us to provide a **knowledge base** to LLMs. It enables us to store information as embeddings and search for the **results** similar to ours using **query**.

<Info>
  **What is a Knowledge Base?**

  Knowledge Base is a database of information that the Assistant can search to improve its responses. This information is stored in a vector database and provides LLMs with business context, which makes them respond in a context-aware manner.

  While any type of storage can act as a knowledge base, vector databases offer the best solution for retrieving relevant results from dense information quickly.
</Info>

Let's see how using LanceDB inside Phidata helps in making LLM more useful:

## Prerequisites: install and import necessary dependencies

**Create a virtual environment**

1. install virtualenv package

<CodeBlock filename="bash" language="bash" icon="terminal">
  pip install virtualenv
</CodeBlock>

2. Create a directory for your project and go to the directory and create a virtual environment inside it.

<CodeBlock filename="bash" language="bash" icon="terminal">
  mkdir phi
</CodeBlock>

<CodeBlock filename="bash" language="bash" icon="terminal">
  cd phi
</CodeBlock>

<CodeBlock filename="bash" language="bash" icon="terminal">
  python -m venv phidata\_
</CodeBlock>

**Activating virtual environment**

1. from inside the project directory, run the following command to activate the virtual environment.

<CodeBlock filename="bash" language="bash" icon="terminal">
  phidata\_/Scripts/activate
</CodeBlock>

**Install the following packages in the virtual environment**

<CodeBlock filename="bash" language="bash" icon="terminal">
  pip install lancedb phidata youtube\_transcript\_api openai ollama numpy pandas
</CodeBlock>

**Create python files and import necessary libraries**

You need to create two files -- `transcript.py` and `ollama_assistant.py` or `openai_assistant.py`

<CodeBlock filename="openai_assistant.py" language="Python" icon="python">
  {PyPlatformsPhidataOpenaiSetup}
</CodeBlock>

<CodeBlock filename="ollama_assistant.py" language="Python" icon="python">
  {PyPlatformsPhidataOllamaSetup}
</CodeBlock>

<CodeBlock filename="transcript.py" language="Python" icon="python">
  {PyPlatformsPhidataTranscriptModule}
</CodeBlock>

<Warning>
  If creating Ollama assistant, download and install Ollama [from here](https://ollama.com/) and then run the Ollama instance in the background. Also, download the required models using `ollama pull <model-name>`. Check out the models [here](https://ollama.com/library)
</Warning>

**Run the following command to deactivate the virtual environment if needed**

<CodeBlock filename="bash" language="bash" icon="terminal">
  deactivate
</CodeBlock>

## **Step 1** - Create a Knowledge Base for AI Assistant using LanceDB

<CodeBlock filename="openai_assistant.py" language="Python" icon="python">
  {PyPlatformsPhidataOpenaiKnowledgeBase}
</CodeBlock>

<CodeBlock filename="ollama_assistant.py" language="Python" icon="python">
  {PyPlatformsPhidataOllamaKnowledgeBase}
</CodeBlock>

Check out the list of **embedders** supported by **Phidata** and their usage [here](https://docs.phidata.com/embedder/introduction).

Here we have used `TextKnowledgeBase`, which loads text/docx files to the knowledge base.

Let's see all the parameters that `TextKnowledgeBase` takes -

| Name            | Type               | Purpose                                                                                                                                                                                              | Default          |
| :-------------- | :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| `path`          | `Union[str, Path]` | Path to text file(s). It can point to a single text file or a directory of text files.                                                                                                               | provided by user |
| `formats`       | `List[str]`        | File formats accepted by this knowledge base.                                                                                                                                                        | `[".txt"]`       |
| `vector_db`     | `VectorDb`         | Vector Database for the Knowledge Base. Phidata provides a wrapper around many vector DBs, you can import it like this - `from phi.vectordb.lancedb import LanceDb`                                  | provided by user |
| `num_documents` | `int`              | Number of results (documents/vectors) that vector search should return.                                                                                                                              | `5`              |
| `reader`        | `TextReader`       | Phidata provides many types of reader objects which read data, clean it and create chunks of data, encapsulate each chunk inside an object of the `Document` class, and return **`List[Document]`**. | `TextReader()`   |
| `optimize_on`   | `int`              | It is used to specify the number of documents on which to optimize the vector database. Supposed to create an index.                                                                                 | `1000`           |

??? Tip "Wonder! What is `Document` class?"
We know that, before storing the data in vectorDB, we need to split the data into smaller chunks upon which embeddings will be created and these embeddings along with the chunks will be stored in vectorDB. When the user queries over the vectorDB, some of these embeddings will be returned as the result based on the semantic similarity with the query.

When the user queries over vectorDB, the queries are converted into embeddings, and a nearest neighbor search is performed over these query embeddings which returns the embeddings that correspond to most semantically similar chunks(parts of our data) present in vectorDB.

Here, a "Document" is a class in Phidata. Since there is an option to let Phidata create and manage embeddings, it splits our data into smaller chunks(as expected). It does not directly create embeddings on it. Instead, it takes each chunk and encapsulates it inside the object of the `Document` class along with various other metadata related to the chunk. Then embeddings are created on these `Document` objects and stored in vectorDB.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPhidataDocumentModel}
</CodeBlock>

However, using Phidata you can load many other types of data in the knowledge base(other than text). Check out [Phidata Knowledge Base](https://docs.phidata.com/knowledge/introduction) for more information.

Let's dig deeper into the `vector_db` parameter and see what parameters `LanceDb` takes -

| Name         | Type                    | Purpose                                                                                                                                                                                                                                          | Default           |
| :----------- | :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| `embedder`   | `Embedder`              | Phidata provides many Embedders that abstract the interaction with embedding APIs and utilize it to generate embeddings. Check out other embedders [here](https://docs.phidata.com/embedder/introduction)                                        | `OpenAIEmbedder`  |
| `distance`   | `List[str]`             | The choice of distance metric used to calculate the similarity between vectors, which directly impacts search results and performance in vector databases.                                                                                       | `Distance.cosine` |
| `connection` | `lancedb.db.LanceTable` | LanceTable can be accessed through `.connection`. You can connect to an existing table of LanceDB, created outside of Phidata, and utilize it. If not provided, it creates a new table using `table_name` parameter and adds it to `connection`. | `None`            |
| `uri`        | `str`                   | It specifies the directory location of **LanceDB database** and establishes a connection that can be used to interact with the database.                                                                                                         | `"/tmp/lancedb"`  |
| `table_name` | `str`                   | If `connection` is not provided, it initializes and connects to a new **LanceDB table** with a specified(or default) name in the database present at `uri`.                                                                                      | `"phi"`           |
| `nprobes`    | `int`                   | It refers to the number of partitions that the search algorithm examines to find the nearest neighbors of a given query vector. Higher values will yield better recall (more likely to find vectors if they exist) at the expense of latency.    | `20`              |

<Note>
  Since we just initialized the KnowledgeBase. The VectorDB table that corresponds to this Knowledge Base is not yet populated with our data. It will be populated in **Step 3**, once we perform the `load` operation.

  You can check the state of the LanceDB table using - `knowledge_base.vector_db.connection.to_pandas()`
</Note>

Now that the Knowledge Base is initialized, , we can go to **step 2**.

## **Step 2** -  Create an assistant with our choice of LLM and reference to the knowledge base.

<CodeBlock filename="openai_assistant.py" language="Python" icon="python">
  {PyPlatformsPhidataOpenaiAssistant}
</CodeBlock>

<CodeBlock filename="ollama_assistant.py" language="Python" icon="python">
  {PyPlatformsPhidataOllamaAssistant}
</CodeBlock>

Assistants add **memory**, **knowledge**, and **tools** to LLMs. Here we will add only **knowledge** in this example.

Whenever we will give a query to LLM, the assistant will retrieve relevant information from our **Knowledge Base**(table in LanceDB) and pass it to LLM along with the user query in a structured way.

* The `add_references_to_prompt=True` always adds information from the knowledge base to the prompt, regardless of whether it is relevant to the question.

To know more about an creating assistant in Phidata, check out [Phidata docs](https://docs.phidata.com/assistants/introduction) here.

## **Step 3** - Load data to Knowledge Base.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPhidataLoadKnowledgeBase}
</CodeBlock>

The above code loads the data to the Knowledge Base(LanceDB Table) and now it is ready to be used by the assistant.

| Name            | Type   | Purpose                                                                              | Default |
| :-------------- | :----- | :----------------------------------------------------------------------------------- | :------ |
| `recreate`      | `bool` | If True, it drops the existing table and recreates the table in the vectorDB.        | `False` |
| `upsert`        | `bool` | If True and the vectorDB supports upsert, it will upsert documents to the vector db. | `False` |
| `skip_existing` | `bool` | If True, skips documents that already exist in the vectorDB when inserting.          | `True`  |

> **Tip · What is upsert?**\
> Upsert is a database operation that combines “update” and “insert”. It updates existing records if a document with the same identifier exists, or inserts new records if no matching record exists. This keeps the knowledge base current without manual checks.

During the Load operation, Phidata directly interacts with the LanceDB library and performs the loading of the table with our data in the following steps -

1. **Creates** and **initializes** the table if it does not exist.

2. Then it **splits** our data into smaller **chunks**.

   > **Question · How do they create chunks?**\
   > **Phidata** provides multiple knowledge-base types depending on the source data. Most of them (except the LlamaIndexKnowledgeBase and LangChainKnowledgeBase) expose a `document_lists` iterator. During the load operation, this iterator reads the input (for example, text files), splits it into chunks, wraps each chunk in a `Document`, and yields lists of those `Document` objects.

3. Then **embeddings** are created on these chunks are **inserted** into the LanceDB Table

   > **Question · How do they insert the chunks into LanceDB?**\
   > Each list of `Document` objects from the previous step is processed as follows:
   >
   > * Generate embeddings for every `Document`.
   > * Clean the `content` field so only the text you care about is persisted.
   > * Prepare a payload with the `id`, the embedding (`vector`), and any metadata needed for retrieval.
   > * Add the prepared rows to the LanceDB table.

4. Now the internal state of `knowledge_base` is changed (embeddings are created and loaded in the table ) and it **ready to be used by assistant**.

## **Step 4** - Start a cli chatbot with access to the Knowledge base

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPhidataCliChat}
</CodeBlock>

For more information and amazing cookbooks of Phidata, read the [Phidata documentation](https://docs.phidata.com/introduction) and also visit [LanceDB x Phidata docmentation](https://docs.phidata.com/vectordb/lancedb).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt