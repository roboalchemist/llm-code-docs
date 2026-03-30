# Source: https://docs.vectara.com/docs/developer-quickstart

Title: Quickstart | Vectara Docs

URL Source: https://docs.vectara.com/docs/developer-quickstart

Markdown Content:
Build your first RAG application with Vectara in 5 minutes. You'll upload a d ocument, query it, and get AI-generated answers with citations.

Before you begin, you need:

*   A Vectara account ([sign up free](https://console.vectara.com/signup) - 30-day trial)
*   An API key (created in step 1)

### What you will build[​](https://docs.vectara.com/docs/developer-quickstart#what-you-will-build "Direct link to What you will build")

Follow this workflow to create your first RAG application:

Step 1: Get your API key[​](https://docs.vectara.com/docs/developer-quickstart#step-1-get-your-api-key "Direct link to Step 1: Get your API key")
-------------------------------------------------------------------------------------------------------------------------------------------------

1.   Log in to the [Vectara Console](https://console.vectara.com/).
2.   Navigate to **Authorization**, **API Keys**.
3.   Copy your Personal API key.

**Set the API key as an environment variable:**

`export VECTARA_API_KEY="your_api_key_here"`

caution

Keep your API key secure. Don't commit it to version control or share it publicly.

Step 2: Create a corpus[​](https://docs.vectara.com/docs/developer-quickstart#step-2-create-a-corpus "Direct link to Step 2: Create a corpus")
----------------------------------------------------------------------------------------------------------------------------------------------

A corpus is a container for your documents. Create one with a single API call:

1 curl -X POST https://api.vectara.io/v2/corpora \

2-H "x-api-key: $VECTARA_API_KEY" \?

3-H "Content-Type: application/json" \

4-d '{

5"key": "quickstart-corpus",?

6"name": "Quickstart Corpus",

7"description": "My first corpus"

8}'

**Expected response:**

1{

2"key": "quickstart-corpus",

3"name": "Quickstart Corpus",

4"description": "My first corpus",

5"enabled": true,

6"created_at": "2025-01-15T10:30:00Z"

7}

You now have a corpus ready to store documents.

Step 3: Upload a document[​](https://docs.vectara.com/docs/developer-quickstart#step-3-upload-a-document "Direct link to Step 3: Upload a document")
----------------------------------------------------------------------------------------------------------------------------------------------------

Upload your first document. We'll create a simple structured document:

1 curl -X POST https://api.vectara.io/v2/corpora/quickstart-corpus/documents \

2-H "x-api-key: $VECTARA_API_KEY" \

3-H "Content-Type: application/json" \

4-d '{

5 "type": "structured",?

6 "id": "doc-1",?

7 "title": "Vectara Overview",

8 "sections": [

9 {?

10 "text": "Vectara is the Enterprise Agent Platform, with built-in multi-modal retrieval, orchestration, and

11 always-on governance, deployable on-prem (air-gapped), in your VPC, or as SaaS."

12 },

13 {

14 "text": "Vectara agents deliver answers with source citations, audit trails, and real-time policy enforcement. This enables teams to ship faster with lower risk."

15 }

16 ]

17}'

**Expected response:**

1{

2"id": "doc-1",

3"status": "indexed"

4}

Your document is now indexed and searchable.

Upload files instead

You can also upload files directly (PDF, Word, PowerPoint, etc.) without structuring them:

`curl -X POST https://api.vectara.io/v2/corpora/quickstart-corpus/upload \  -H "x-api-key: $VECTARA_API_KEY" \  -F "file=@document.pdf"`

[Learn more about file uploads →](https://docs.vectara.com/docs/rest-api/upload-file)

Step 4: Query your data[​](https://docs.vectara.com/docs/developer-quickstart#step-4-query-your-data "Direct link to Step 4: Query your data")
----------------------------------------------------------------------------------------------------------------------------------------------

Now query your document and get an AI-generated answer with citations:

1 curl -X POST https://api.vectara.io/v2/query \

2-H "x-api-key: $VECTARA_API_KEY" \

3-H "Content-Type: application/json" \

4-d '{

5 "query": "What is Vectara?",?

6 "search": {

7 "corpora": [

8 {

9 "corpus_key": "quickstart-corpus"?

10 }

11 ],

12 "limit": 5

13 },

14 "generation": {

15 "generation_preset_name": "mockingbird-2.0",?

16 "max_used_search_results": 5

17 }

18}'

**Response:**

1{

2"summary": "Vectara is the Enterprise Agent Platform [1]. It provides RAG capabilities with built-in governance, grounded responses, and factual consistency enforcement [1]. Vectara agents deliver answers with source citations, audit trails, and real-time policy enforcement [2].",?

3"search_results": [?

4 {

5 "text": "Vectara is the Enterprise Agent Platform...",

6 "score": 0.89,

7 "document_id": "doc-1",

8 "document_metadata": {

9 "title": "Vectara Overview"

10 }

11 },

12 {

13 "text": "Vectara agents deliver answers with source citations...",

14 "score": 0.82,

15 "document_id": "doc-1"

16 }

17],

18"factual_consistency_score": 0.95?

19}

Notice:

*   **Citations** (`[1]`, `[2]`) link answers to source documents
*   **Search results** show the matched text snippets
*   **Factual consistency score** (0.95) indicates high accuracy

**Done!** You just built a working RAG application in 4 API calls.

What you just built[​](https://docs.vectara.com/docs/developer-quickstart#what-you-just-built "Direct link to What you just built")
-----------------------------------------------------------------------------------------------------------------------------------

In less than 5 minutes, you:

1.   Created a corpus to store documents
2.   Indexed a document with searchable text
3.   Queried your data with natural language
4.   Got an AI-generated answer with citations

This is the foundation of every Vectara application, from simple Q&A to complex AI agents.

Next steps[​](https://docs.vectara.com/docs/developer-quickstart#next-steps "Direct link to Next steps")
--------------------------------------------------------------------------------------------------------

### Upload real documents[​](https://docs.vectara.com/docs/developer-quickstart#upload-real-documents "Direct link to Upload real documents")

**Upload a PDF, Word doc, or text file:**

1 curl -X POST https://api.vectara.io/v2/corpora/quickstart-corpus/upload \

2-H "x-api-key: $VECTARA_API_KEY" \

3-F "file=@my-document.pdf"

**Learn more:**

*   [Supported file formats](https://docs.vectara.com/docs/build/data-ingestion#supported-file-formats)
*   [Working with tables in PDFs](https://docs.vectara.com/docs/build/working-with-tables)
*   [Add metadata for filtering](https://docs.vectara.com/docs/build/prepare-data/metadata-filters)

### Build with agents[​](https://docs.vectara.com/docs/developer-quickstart#build-with-agents "Direct link to Build with agents")

Transform your RAG application into an intelligent agent:

1 curl -X POST https://api.vectara.io/v2/agents \

2-H "x-api-key: $VECTARA_API_KEY" \

3-H "Content-Type: application/json" \

4-d '{

5 "name": "My First Agent",

6 "description": "An agent that answers questions about my data",

7 "instructions": "You are a helpful assistant. Answer questions based on the provided documents.",

8 "tools": [

9 {

10 "type": "corpora_search",

11 "corpus_key": "quickstart-corpus"

12 }

13 ]

14}'

**Learn more:**

*   [Agent quickstart](https://docs.vectara.com/docs/agents/agents-quickstart)
*   [Agent instructions](https://docs.vectara.com/docs/rest-api/instructions)
*   [Agent tools](https://docs.vectara.com/docs/rest-api/tools)

* * *

### Improve search quality[​](https://docs.vectara.com/docs/developer-quickstart#improve-search-quality "Direct link to Improve search quality")

**Add a reranker to improve relevance:**

1 curl -X POST https://api.vectara.io/v2/query \

2-H "x-api-key: $VECTARA_API_KEY" \

3-H "Content-Type: application/json" \

4-d '{

5 "query": "What is Vectara?",

6 "search": {

7 "corpora": [{"corpus_key": "quickstart-corpus"}],

8 "limit": 25,

9 "reranker": {

10 "type": "customer_reranker",

11 "reranker_name": "Rerank_Multilingual_v1",

12 "limit": 5

13 }

14 },

15 "generation": {

16 "generation_preset_name": "mockingbird-2.0"

17 }

18}'

**Learn more:**

*   [Reranking strategies](https://docs.vectara.com/docs/search-and-retrieval/reranking)
*   [Hybrid search](https://docs.vectara.com/docs/search-and-retrieval#hybrid-search)
*   [Custom prompts](https://docs.vectara.com/docs/prompts/vectara-prompt-engine)

Full example script[​](https://docs.vectara.com/docs/developer-quickstart#full-example-script "Direct link to Full example script")
-----------------------------------------------------------------------------------------------------------------------------------

Copy this complete script to test everything at once:

1#!/bin/bash

2

3

4

5 export VECTARA_API_KEY="your_api_key_here"

6

7

8

9 echo "Creating corpus..."

10 curl -X POST https://api.vectara.io/v2/corpora \

11-H "x-api-key: $VECTARA_API_KEY" \

12-H "Content-Type: application/json" \

13-d '{

14"key": "quickstart-corpus",

15"name": "Quickstart Corpus",

16"description": "My first corpus"

17}'

18

19 echo -e "\n"

20

21

22

23 echo "Uploading document..."

24 curl -X POST https://api.vectara.io/v2/corpora/quickstart-corpus/documents \

25-H "x-api-key: $VECTARA_API_KEY" \

26-H "Content-Type: application/json" \

27-d '{

28"type": "structured",

29"id": "doc-1",

30"title": "Vectara Overview",

Save as `vectara-quickstart.sh`, make it executable with `chmod +x vectara-quickstart.sh`, and run it!
