# LlamaIndex Documentation

Source: https://developers.llamaindex.ai/python/framework/changelog/

---

# ChangeLog

## [2025-12-30]

Section titled “[2025-12-30]”

### llama-index-callbacks-agentops [0.4.1]

Section titled “llama-index-callbacks-agentops [0.4.1]”

  * Feat/async tool spec support ([#20338](https://github.com/run-llama/llama_index/pull/20338))

### llama-index-core [0.14.12]

Section titled “llama-index-core [0.14.12]”

  * Feat/async tool spec support ([#20338](https://github.com/run-llama/llama_index/pull/20338))
  * Improve `MockFunctionCallingLLM` ([#20356](https://github.com/run-llama/llama_index/pull/20356))
  * fix(openai): sanitize generic Pydantic model schema names ([#20371](https://github.com/run-llama/llama_index/pull/20371))
  * Element node parser ([#20399](https://github.com/run-llama/llama_index/pull/20399))
  * improve llama dev logging ([#20411](https://github.com/run-llama/llama_index/pull/20411))
  * test(node_parser): add unit tests for Java CodeSplitter ([#20423](https://github.com/run-llama/llama_index/pull/20423))
  * fix: crash in log_vector_store_query_result when result.ids is None ([#20427](https://github.com/run-llama/llama_index/pull/20427))

### llama-index-embeddings-litellm [0.4.1]

Section titled “llama-index-embeddings-litellm [0.4.1]”

  * Add docstring to LiteLLM embedding class ([#20336](https://github.com/run-llama/llama_index/pull/20336))

### llama-index-embeddings-ollama [0.8.5]

Section titled “llama-index-embeddings-ollama [0.8.5]”

  * feat(llama-index-embeddings-ollama): Add keep_alive parameter ([#20395](https://github.com/run-llama/llama_index/pull/20395))
  * docs: improve Ollama embeddings README with comprehensive documentation ([#20414](https://github.com/run-llama/llama_index/pull/20414))

### llama-index-embeddings-voyageai [0.5.2]

Section titled “llama-index-embeddings-voyageai [0.5.2]”

  * Voyage multimodal 35 ([#20398](https://github.com/run-llama/llama_index/pull/20398))

### llama-index-graph-stores-nebula [0.5.1]

Section titled “llama-index-graph-stores-nebula [0.5.1]”

  * feat(nebula): add MENTIONS edge to property graph store ([#20401](https://github.com/run-llama/llama_index/pull/20401))

### llama-index-llms-aibadgr [0.1.0]

Section titled “llama-index-llms-aibadgr [0.1.0]”

  * feat(llama-index-llms-aibadgr): Add AI Badgr OpenAI‑compatible LLM integration ([#20365](https://github.com/run-llama/llama_index/pull/20365))

### llama-index-llms-anthropic [0.10.4]

Section titled “llama-index-llms-anthropic [0.10.4]”

  * add back haiku-3 support ([#20408](https://github.com/run-llama/llama_index/pull/20408))

### llama-index-llms-bedrock-converse [0.12.3]

Section titled “llama-index-llms-bedrock-converse [0.12.3]”

  * fix: bedrock converse thinking block issue ([#20355](https://github.com/run-llama/llama_index/pull/20355))

### llama-index-llms-google-genai [0.8.3]

Section titled “llama-index-llms-google-genai [0.8.3]”

  * Switch use_file_api to Flexible file_mode; Improve File Upload Handling & Bump google-genai to v1.52.0 ([#20347](https://github.com/run-llama/llama_index/pull/20347))
  * Fix missing role from Google-GenAI ([#20357](https://github.com/run-llama/llama_index/pull/20357))
  * Add signature index fix ([#20362](https://github.com/run-llama/llama_index/pull/20362))
  * Add positional thought signature for thoughts ([#20418](https://github.com/run-llama/llama_index/pull/20418))

### llama-index-llms-ollama [0.9.1]

Section titled “llama-index-llms-ollama [0.9.1]”

  * feature: pydantic no longer complains if you pass ‘low’, ‘medium’, ‘h… ([#20394](https://github.com/run-llama/llama_index/pull/20394))

### llama-index-llms-openai [0.6.12]

Section titled “llama-index-llms-openai [0.6.12]”

  * fix: Handle tools=None in OpenAIResponses._get_model_kwargs ([#20358](https://github.com/run-llama/llama_index/pull/20358))
  * feat: add support for gpt-5.2 and 5.2 pro ([#20361](https://github.com/run-llama/llama_index/pull/20361))

### llama-index-readers-confluence [0.6.1]

Section titled “llama-index-readers-confluence [0.6.1]”

  * fix(confluence): support Python 3.14 ([#20370](https://github.com/run-llama/llama_index/pull/20370))

### llama-index-readers-file [0.5.6]

Section titled “llama-index-readers-file [0.5.6]”

  * Loosen constraint on `pandas` version ([#20387](https://github.com/run-llama/llama_index/pull/20387))

### llama-index-readers-service-now [0.2.2]

Section titled “llama-index-readers-service-now [0.2.2]”

  * chore(deps): bump urllib3 from 2.5.0 to 2.6.0 in /llama-index-integrations/readers/llama-index-readers-service-now in the pip group across 1 directory ([#20341](https://github.com/run-llama/llama_index/pull/20341))

### llama-index-tools-mcp [0.4.5]

Section titled “llama-index-tools-mcp [0.4.5]”

  * fix: pass timeout parameters to transport clients in BasicMCPClient ([#20340](https://github.com/run-llama/llama_index/pull/20340))
  * feature: Permit to pass a custom httpx.AsyncClient when creating a BasicMcpClient ([#20368](https://github.com/run-llama/llama_index/pull/20368))

### llama-index-tools-typecast [0.1.0]

Section titled “llama-index-tools-typecast [0.1.0]”

  * feat: add Typecast tool integration with text to speech features ([#20343](https://github.com/run-llama/llama_index/pull/20343))

### llama-index-vector-stores-azurepostgresql [0.2.0]

Section titled “llama-index-vector-stores-azurepostgresql [0.2.0]”

  * Feat/async tool spec support ([#20338](https://github.com/run-llama/llama_index/pull/20338))

### llama-index-vector-stores-chroma [0.5.5]

Section titled “llama-index-vector-stores-chroma [0.5.5]”

  * Fix chroma nested metadata filters ([#20424](https://github.com/run-llama/llama_index/pull/20424))
  * fix(chroma): support multimodal results ([#20426](https://github.com/run-llama/llama_index/pull/20426))

### llama-index-vector-stores-couchbase [0.6.0]

Section titled “llama-index-vector-stores-couchbase [0.6.0]”

  * Update FTS & GSI reference docs for Couchbase vector-store ([#20346](https://github.com/run-llama/llama_index/pull/20346))

### llama-index-vector-stores-faiss [0.5.2]

Section titled “llama-index-vector-stores-faiss [0.5.2]”

  * fix(faiss): pass numpy array instead of int to add_with_ids ([#20384](https://github.com/run-llama/llama_index/pull/20384))

### llama-index-vector-stores-lancedb [0.4.4]

Section titled “llama-index-vector-stores-lancedb [0.4.4]”

  * Feat/async tool spec support ([#20338](https://github.com/run-llama/llama_index/pull/20338))
  * fix(vector_stores/lancedb): add missing ’<’ filter operator ([#20364](https://github.com/run-llama/llama_index/pull/20364))
  * fix(lancedb): fix metadata filtering logic and list value SQL generation ([#20374](https://github.com/run-llama/llama_index/pull/20374))

### llama-index-vector-stores-mongodb [0.9.0]

Section titled “llama-index-vector-stores-mongodb [0.9.0]”

  * Update mongo vector store to initialize without list permissions ([#20354](https://github.com/run-llama/llama_index/pull/20354))
  * add mongodb delete index ([#20429](https://github.com/run-llama/llama_index/pull/20429))
  * async mongodb atlas support ([#20430](https://github.com/run-llama/llama_index/pull/20430))

### llama-index-vector-stores-redis [0.6.2]

Section titled “llama-index-vector-stores-redis [0.6.2]”

  * Redis metadata filter fix ([#20359](https://github.com/run-llama/llama_index/pull/20359))

### llama-index-vector-stores-vertexaivectorsearch [0.3.3]

Section titled “llama-index-vector-stores-vertexaivectorsearch [0.3.3]”

  * feat(vertex-vector-search): Add Google Vertex AI Vector Search v2.0 support ([#20351](https://github.com/run-llama/llama_index/pull/20351))

## [2025-12-04]

Section titled “[2025-12-04]”

### llama-index-core [0.14.10]

Section titled “llama-index-core [0.14.10]”

  * feat: add mock function calling llm ([#20331](https://github.com/run-llama/llama_index/pull/20331))

### llama-index-llms-qianfan [0.4.1]

Section titled “llama-index-llms-qianfan [0.4.1]”

  * test: fix typo ‘reponse’ to ‘response’ in variable names ([#20329](https://github.com/run-llama/llama_index/pull/20329))

### llama-index-tools-airweave [0.1.0]

Section titled “llama-index-tools-airweave [0.1.0]”

  * feat: add Airweave tool integration with advanced search features ([#20111](https://github.com/run-llama/llama_index/pull/20111))

### llama-index-utils-qianfan [0.4.1]

Section titled “llama-index-utils-qianfan [0.4.1]”

  * test: fix typo ‘reponse’ to ‘response’ in variable names ([#20329](https://github.com/run-llama/llama_index/pull/20329))

## [2025-12-02]

Section titled “[2025-12-02]”

### llama-index-agent-azure [0.2.1]

Section titled “llama-index-agent-azure [0.2.1]”

  * fix: Pin azure-ai-projects version to prevent breaking changes ([#20255](https://github.com/run-llama/llama_index/pull/20255))

### llama-index-core [0.14.9]

Section titled “llama-index-core [0.14.9]”

  * MultiModalVectorStoreIndex now returns a multi-modal ContextChatEngine. ([#20265](https://github.com/run-llama/llama_index/pull/20265))
  * Ingestion to vector store now ensures that _node-content is readable ([#20266](https://github.com/run-llama/llama_index/pull/20266))
  * fix: ensure context is copied with async utils run_async ([#20286](https://github.com/run-llama/llama_index/pull/20286))
  * fix(memory): ensure first message in queue is always a user message after flush ([#20310](https://github.com/run-llama/llama_index/pull/20310))

### llama-index-embeddings-bedrock [0.7.2]

Section titled “llama-index-embeddings-bedrock [0.7.2]”

  * feat(embeddings-bedrock): Add support for Amazon Bedrock Application Inference Profiles ([#20267](https://github.com/run-llama/llama_index/pull/20267))
  * fix:(embeddings-bedrock) correct extraction of provider from model_name ([#20295](https://github.com/run-llama/llama_index/pull/20295))
  * Bump version of bedrock-embedding ([#20304](https://github.com/run-llama/llama_index/pull/20304))

### llama-index-embeddings-voyageai [0.5.1]

Section titled “llama-index-embeddings-voyageai [0.5.1]”

  * VoyageAI correction and documentation ([#20251](https://github.com/run-llama/llama_index/pull/20251))

### llama-index-llms-anthropic [0.10.3]

Section titled “llama-index-llms-anthropic [0.10.3]”

  * feat: add anthropic opus 4.5 ([#20306](https://github.com/run-llama/llama_index/pull/20306))

### llama-index-llms-bedrock-converse [0.12.2]

Section titled “llama-index-llms-bedrock-converse [0.12.2]”

  * fix(bedrock-converse): Only use guardrail_stream_processing_mode in streaming functions ([#20289](https://github.com/run-llama/llama_index/pull/20289))
  * feat: add anthropic opus 4.5 ([#20306](https://github.com/run-llama/llama_index/pull/20306))
  * feat(bedrock-converse): Additional support for Claude Opus 4.5 ([#20317](https://github.com/run-llama/llama_index/pull/20317))

### llama-index-llms-google-genai [0.7.4]

Section titled “llama-index-llms-google-genai [0.7.4]”

  * Fix gemini-3 support and gemini function call support ([#20315](https://github.com/run-llama/llama_index/pull/20315))

### llama-index-llms-helicone [0.1.1]

Section titled “llama-index-llms-helicone [0.1.1]”

  * update helicone docs + examples ([#20208](https://github.com/run-llama/llama_index/pull/20208))

### llama-index-llms-openai [0.6.10]

Section titled “llama-index-llms-openai [0.6.10]”

  * Smallest Nit ([#20252](https://github.com/run-llama/llama_index/pull/20252))
  * Feat: Add gpt-5.1-chat model support ([#20311](https://github.com/run-llama/llama_index/pull/20311))

### llama-index-llms-ovhcloud [0.1.0]

Section titled “llama-index-llms-ovhcloud [0.1.0]”

  * Add OVHcloud AI Endpoints provider ([#20288](https://github.com/run-llama/llama_index/pull/20288))

### llama-index-llms-siliconflow [0.4.2]

Section titled “llama-index-llms-siliconflow [0.4.2]”

  * [Bugfix] None check on content in delta in siliconflow LLM ([#20327](https://github.com/run-llama/llama_index/pull/20327))

### llama-index-node-parser-docling [0.4.2]

Section titled “llama-index-node-parser-docling [0.4.2]”

  * Relax docling Python constraints ([#20322](https://github.com/run-llama/llama_index/pull/20322))

### llama-index-packs-resume-screener [0.9.3]

Section titled “llama-index-packs-resume-screener [0.9.3]”

  * feat: Update pypdf to latest version ([#20285](https://github.com/run-llama/llama_index/pull/20285))

### llama-index-postprocessor-voyageai-rerank [0.4.1]

Section titled “llama-index-postprocessor-voyageai-rerank [0.4.1]”

  * VoyageAI correction and documentation ([#20251](https://github.com/run-llama/llama_index/pull/20251))

### llama-index-protocols-ag-ui [0.2.3]

Section titled “llama-index-protocols-ag-ui [0.2.3]”

  * fix: correct order of ag-ui events to avoid event conflicts ([#20296](https://github.com/run-llama/llama_index/pull/20296))

### llama-index-readers-confluence [0.6.0]

Section titled “llama-index-readers-confluence [0.6.0]”

  * Refactor Confluence integration: Update license to MIT, remove requirements.txt, and implement HtmlTextParser for HTML to Markdown conversion. Update dependencies and tests accordingly. ([#20262](https://github.com/run-llama/llama_index/pull/20262))

### llama-index-readers-docling [0.4.2]

Section titled “llama-index-readers-docling [0.4.2]”

  * Relax docling Python constraints ([#20322](https://github.com/run-llama/llama_index/pull/20322))

### llama-index-readers-file [0.5.5]

Section titled “llama-index-readers-file [0.5.5]”

  * feat: Update pypdf to latest version ([#20285](https://github.com/run-llama/llama_index/pull/20285))

### llama-index-readers-reddit [0.4.1]

Section titled “llama-index-readers-reddit [0.4.1]”

  * Fix typo in README.md for Reddit integration ([#20283](https://github.com/run-llama/llama_index/pull/20283))

### llama-index-storage-chat-store-postgres [0.3.2]

Section titled “llama-index-storage-chat-store-postgres [0.3.2]”

  * [FIX] Postgres ChatStore automatically prefix table name with “data_” ([#20241](https://github.com/run-llama/llama_index/pull/20241))

### llama-index-vector-stores-azureaisearch [0.4.4]

Section titled “llama-index-vector-stores-azureaisearch [0.4.4]”

  * `vector-azureaisearch`: check if user agent already in policy before add it to azure client ([#20243](https://github.com/run-llama/llama_index/pull/20243))
  * fix(azureaisearch): Add close/aclose methods to fix unclosed client session warnings ([#20309](https://github.com/run-llama/llama_index/pull/20309))

### llama-index-vector-stores-milvus [0.9.4]

Section titled “llama-index-vector-stores-milvus [0.9.4]”

  * Fix/consistency level param for milvus ([#20268](https://github.com/run-llama/llama_index/pull/20268))

### llama-index-vector-stores-postgres [0.7.2]

Section titled “llama-index-vector-stores-postgres [0.7.2]”

  * Fix postgresql dispose ([#20312](https://github.com/run-llama/llama_index/pull/20312))

### llama-index-vector-stores-qdrant [0.9.0]

Section titled “llama-index-vector-stores-qdrant [0.9.0]”

  * fix: Update qdrant-client version constraints ([#20280](https://github.com/run-llama/llama_index/pull/20280))
  * Feat: update Qdrant client to 1.16.0 ([#20287](https://github.com/run-llama/llama_index/pull/20287))

### llama-index-vector-stores-vertexaivectorsearch [0.3.2]

Section titled “llama-index-vector-stores-vertexaivectorsearch [0.3.2]”

  * fix: update blob path in batch_update_index ([#20281](https://github.com/run-llama/llama_index/pull/20281))

### llama-index-voice-agents-openai [0.2.2]

Section titled “llama-index-voice-agents-openai [0.2.2]”

  * Smallest Nit ([#20252](https://github.com/run-llama/llama_index/pull/20252))

## [2025-11-10]

Section titled “[2025-11-10]”

### llama-index-core [0.14.8]

Section titled “llama-index-core [0.14.8]”

  * Fix ReActOutputParser getting stuck when “Answer:” contains “Action:” ([#20098](https://github.com/run-llama/llama_index/pull/20098))
  * Add buffer to image, audio, video and document blocks ([#20153](https://github.com/run-llama/llama_index/pull/20153))
  * fix(agent): Handle multi-block ChatMessage in ReActAgent ([#20196](https://github.com/run-llama/llama_index/pull/20196))
  * Fix/20209 ([#20214](https://github.com/run-llama/llama_index/pull/20214))
  * Preserve Exception in ToolOutput ([#20231](https://github.com/run-llama/llama_index/pull/20231))
  * fix weird pydantic warning ([#20235](https://github.com/run-llama/llama_index/pull/20235))

### llama-index-embeddings-nvidia [0.4.2]

Section titled “llama-index-embeddings-nvidia [0.4.2]”

  * docs: Edit pass and update example model ([#20198](https://github.com/run-llama/llama_index/pull/20198))

### llama-index-embeddings-ollama [0.8.4]

Section titled “llama-index-embeddings-ollama [0.8.4]”

  * Added a test case (no code) to check the embedding through an actual connection to a Ollama server (after checking that the ollama server exists) ([#20230](https://github.com/run-llama/llama_index/pull/20230))

### llama-index-llms-anthropic [0.10.2]

Section titled “llama-index-llms-anthropic [0.10.2]”

  * feat(llms/anthropic): Add support for RawMessageDeltaEvent in streaming ([#20206](https://github.com/run-llama/llama_index/pull/20206))
  * chore: remove unsupported models ([#20211](https://github.com/run-llama/llama_index/pull/20211))

### llama-index-llms-bedrock-converse [0.11.1]

Section titled “llama-index-llms-bedrock-converse [0.11.1]”

  * feat: integrate bedrock converse with tool call block ([#20099](https://github.com/run-llama/llama_index/pull/20099))
  * feat: Update model name extraction to include ‘jp’ region prefix and … ([#20233](https://github.com/run-llama/llama_index/pull/20233))

### llama-index-llms-google-genai [0.7.3]

Section titled “llama-index-llms-google-genai [0.7.3]”

  * feat: google genai integration with tool block ([#20096](https://github.com/run-llama/llama_index/pull/20096))
  * fix: non-streaming gemini tool calling ([#20207](https://github.com/run-llama/llama_index/pull/20207))
  * Add token usage information in GoogleGenAI chat additional_kwargs ([#20219](https://github.com/run-llama/llama_index/pull/20219))
  * bug fix google genai stream_complete ([#20220](https://github.com/run-llama/llama_index/pull/20220))

### llama-index-llms-nvidia [0.4.4]

Section titled “llama-index-llms-nvidia [0.4.4]”

  * docs: Edit pass and code example updates ([#20200](https://github.com/run-llama/llama_index/pull/20200))

### llama-index-llms-openai [0.6.8]

Section titled “llama-index-llms-openai [0.6.8]”

  * FixV2: Correct DocumentBlock type for OpenAI from ‘input_file’ to ‘file’ ([#20203](https://github.com/run-llama/llama_index/pull/20203))
  * OpenAI v2 sdk support ([#20234](https://github.com/run-llama/llama_index/pull/20234))

### llama-index-llms-upstage [0.6.5]

Section titled “llama-index-llms-upstage [0.6.5]”

  * OpenAI v2 sdk support ([#20234](https://github.com/run-llama/llama_index/pull/20234))

### llama-index-packs-streamlit-chatbot [0.5.2]

Section titled “llama-index-packs-streamlit-chatbot [0.5.2]”

  * OpenAI v2 sdk support ([#20234](https://github.com/run-llama/llama_index/pull/20234))

### llama-index-packs-voyage-query-engine [0.5.2]

Section titled “llama-index-packs-voyage-query-engine [0.5.2]”

  * OpenAI v2 sdk support ([#20234](https://github.com/run-llama/llama_index/pull/20234))

### llama-index-postprocessor-nvidia-rerank [0.5.1]

Section titled “llama-index-postprocessor-nvidia-rerank [0.5.1]”

  * docs: Edit pass ([#20199](https://github.com/run-llama/llama_index/pull/20199))

### llama-index-readers-web [0.5.6]

Section titled “llama-index-readers-web [0.5.6]”

  * feat: Add ScrapyWebReader Integration ([#20212](https://github.com/run-llama/llama_index/pull/20212))
  * Update Scrapy dependency to 2.13.3 ([#20228](https://github.com/run-llama/llama_index/pull/20228))

### llama-index-readers-whisper [0.3.0]

Section titled “llama-index-readers-whisper [0.3.0]”

  * OpenAI v2 sdk support ([#20234](https://github.com/run-llama/llama_index/pull/20234))

### llama-index-storage-kvstore-postgres [0.4.3]

Section titled “llama-index-storage-kvstore-postgres [0.4.3]”

  * fix: Ensure schema creation only occurs if it doesn’t already exist ([#20225](https://github.com/run-llama/llama_index/pull/20225))

### llama-index-tools-brightdata [0.2.1]

Section titled “llama-index-tools-brightdata [0.2.1]”

  * docs: add api key claim instructions ([#20204](https://github.com/run-llama/llama_index/pull/20204))

### llama-index-tools-mcp [0.4.3]

Section titled “llama-index-tools-mcp [0.4.3]”

  * Added test case for issue 19211. No code change ([#20201](https://github.com/run-llama/llama_index/pull/20201))

### llama-index-utils-oracleai [0.3.1]

Section titled “llama-index-utils-oracleai [0.3.1]”

  * Update llama-index-core dependency to 0.12.45 ([#20227](https://github.com/run-llama/llama_index/pull/20227))

### llama-index-vector-stores-lancedb [0.4.2]

Section titled “llama-index-vector-stores-lancedb [0.4.2]”

  * fix: FTS index recreation bug on every LanceDB query ([#20213](https://github.com/run-llama/llama_index/pull/20213))

## [2025-10-30]

Section titled “[2025-10-30]”

### llama-index-core [0.14.7]

Section titled “llama-index-core [0.14.7]”

  * Feat/serpex tool integration ([#20141](https://github.com/run-llama/llama_index/pull/20141))
  * Fix outdated error message about setting LLM ([#20157](https://github.com/run-llama/llama_index/pull/20157))
  * Fixing some recently failing tests ([#20165](https://github.com/run-llama/llama_index/pull/20165))
  * Fix: update lock to latest workflow and fix issues ([#20173](https://github.com/run-llama/llama_index/pull/20173))
  * fix: ensure full docstring is used in FunctionTool ([#20175](https://github.com/run-llama/llama_index/pull/20175))
  * fix api docs build ([#20180](https://github.com/run-llama/llama_index/pull/20180))

### llama-index-embeddings-voyageai [0.5.0]

Section titled “llama-index-embeddings-voyageai [0.5.0]”

  * Updating the VoyageAI integration ([#20073](https://github.com/run-llama/llama_index/pull/20073))

### llama-index-llms-anthropic [0.10.0]

Section titled “llama-index-llms-anthropic [0.10.0]”

  * feat: integrate anthropic with tool call block ([#20100](https://github.com/run-llama/llama_index/pull/20100))

### llama-index-llms-bedrock-converse [0.10.7]

Section titled “llama-index-llms-bedrock-converse [0.10.7]”

  * feat: Add support for Bedrock Guardrails streamProcessingMode ([#20150](https://github.com/run-llama/llama_index/pull/20150))
  * bedrock structured output optional force ([#20158](https://github.com/run-llama/llama_index/pull/20158))

### llama-index-llms-fireworks [0.4.5]

Section titled “llama-index-llms-fireworks [0.4.5]”

  * Update FireworksAI models ([#20169](https://github.com/run-llama/llama_index/pull/20169))

### llama-index-llms-mistralai [0.9.0]

Section titled “llama-index-llms-mistralai [0.9.0]”

  * feat: mistralai integration with tool call block ([#20103](https://github.com/run-llama/llama_index/pull/20103))

### llama-index-llms-ollama [0.9.0]

Section titled “llama-index-llms-ollama [0.9.0]”

  * feat: integrate ollama with tool call block ([#20097](https://github.com/run-llama/llama_index/pull/20097))

### llama-index-llms-openai [0.6.6]

Section titled “llama-index-llms-openai [0.6.6]”

  * Allow setting temp of gpt-5-chat ([#20156](https://github.com/run-llama/llama_index/pull/20156))

### llama-index-readers-confluence [0.5.0]

Section titled “llama-index-readers-confluence [0.5.0]”

  * feat(confluence): make SVG processing optional to fix pycairo install… ([#20115](https://github.com/run-llama/llama_index/pull/20115))

### llama-index-readers-github [0.9.0]

Section titled “llama-index-readers-github [0.9.0]”

  * Add GitHub App authentication support ([#20106](https://github.com/run-llama/llama_index/pull/20106))

### llama-index-retrievers-bedrock [0.5.1]

Section titled “llama-index-retrievers-bedrock [0.5.1]”

  * Fixing some recently failing tests ([#20165](https://github.com/run-llama/llama_index/pull/20165))

### llama-index-tools-serpex [0.1.0]

Section titled “llama-index-tools-serpex [0.1.0]”

  * Feat/serpex tool integration ([#20141](https://github.com/run-llama/llama_index/pull/20141))
  * add missing toml info ([#20186](https://github.com/run-llama/llama_index/pull/20186))

### llama-index-vector-stores-couchbase [0.6.0]

Section titled “llama-index-vector-stores-couchbase [0.6.0]”

  * Add Hyperscale and Composite Vector Indexes support for Couchbase vector-store ([#20170](https://github.com/run-llama/llama_index/pull/20170))

## [2025-10-26]

Section titled “[2025-10-26]”

### llama-index-core [0.14.6]

Section titled “llama-index-core [0.14.6]”

  * Add allow_parallel_tool_calls for non-streaming ([#20117](https://github.com/run-llama/llama_index/pull/20117))
  * Fix invalid use of field-specific metadata ([#20122](https://github.com/run-llama/llama_index/pull/20122))
  * update doc for SemanticSplitterNodeParser ([#20125](https://github.com/run-llama/llama_index/pull/20125))
  * fix rare cases when sentence splits are larger than chunk size ([#20147](https://github.com/run-llama/llama_index/pull/20147))

### llama-index-embeddings-bedrock [0.7.0]

Section titled “llama-index-embeddings-bedrock [0.7.0]”

  * Fix BedrockEmbedding to support Cohere v4 response format ([#20094](https://github.com/run-llama/llama_index/pull/20094))

### llama-index-embeddings-isaacus [0.1.0]

Section titled “llama-index-embeddings-isaacus [0.1.0]”

  * feat: Isaacus embeddings integration ([#20124](https://github.com/run-llama/llama_index/pull/20124))

### llama-index-embeddings-oci-genai [0.4.2]

Section titled “llama-index-embeddings-oci-genai [0.4.2]”

  * Update OCI GenAI cohere models ([#20146](https://github.com/run-llama/llama_index/pull/20146))

### llama-index-llms-anthropic [0.9.7]

Section titled “llama-index-llms-anthropic [0.9.7]”

  * Fix double token stream in anthropic llm ([#20108](https://github.com/run-llama/llama_index/pull/20108))
  * Ensure anthropic content delta only has user facing response ([#20113](https://github.com/run-llama/llama_index/pull/20113))

### llama-index-llms-baseten [0.1.7]

Section titled “llama-index-llms-baseten [0.1.7]”

  * add GLM ([#20121](https://github.com/run-llama/llama_index/pull/20121))

### llama-index-llms-helicone [0.1.0]

Section titled “llama-index-llms-helicone [0.1.0]”

  * integrate helicone to llama-index ([#20131](https://github.com/run-llama/llama_index/pull/20131))

### llama-index-llms-oci-genai [0.6.4]

Section titled “llama-index-llms-oci-genai [0.6.4]”

  * Update OCI GenAI cohere models ([#20146](https://github.com/run-llama/llama_index/pull/20146))

### llama-index-llms-openai [0.6.5]

Section titled “llama-index-llms-openai [0.6.5]”

  * chore: openai vbump ([#20095](https://github.com/run-llama/llama_index/pull/20095))

### llama-index-readers-imdb-review [0.4.2]

Section titled “llama-index-readers-imdb-review [0.4.2]”

  * chore: Update selenium dependency in imdb-review reader ([#20105](https://github.com/run-llama/llama_index/pull/20105))

### llama-index-retrievers-bedrock [0.5.0]

Section titled “llama-index-retrievers-bedrock [0.5.0]”

  * feat(bedrock): add async support for AmazonKnowledgeBasesRetriever ([#20114](https://github.com/run-llama/llama_index/pull/20114))

### llama-index-retrievers-superlinked [0.1.3]

Section titled “llama-index-retrievers-superlinked [0.1.3]”

  * Update README.md ([#19829](https://github.com/run-llama/llama_index/pull/19829))

### llama-index-storage-kvstore-postgres [0.4.2]

Section titled “llama-index-storage-kvstore-postgres [0.4.2]”

  * fix: Replace raw SQL string interpolation with proper SQLAlchemy parameterized APIs in PostgresKVStore ([#20104](https://github.com/run-llama/llama_index/pull/20104))

### llama-index-tools-mcp [0.4.3]

Section titled “llama-index-tools-mcp [0.4.3]”

  * Fix BasicMCPClient resource signatures ([#20118](https://github.com/run-llama/llama_index/pull/20118))

### llama-index-vector-stores-postgres [0.7.1]

Section titled “llama-index-vector-stores-postgres [0.7.1]”

  * Add GIN index support for text array metadata in PostgreSQL vector store ([#20130](https://github.com/run-llama/llama_index/pull/20130))

## [2025-10-15]

Section titled “[2025-10-15]”

### llama-index-core [0.14.5]

Section titled “llama-index-core [0.14.5]”

  * Remove debug print ([#20000](https://github.com/run-llama/llama_index/pull/20000))
  * safely initialize RefDocInfo in Docstore ([#20031](https://github.com/run-llama/llama_index/pull/20031))
  * Add progress bar for multiprocess loading ([#20048](https://github.com/run-llama/llama_index/pull/20048))
  * Fix duplicate node positions when identical text appears multiple times in document ([#20050](https://github.com/run-llama/llama_index/pull/20050))
  * chore: tool call block - part 1 ([#20074](https://github.com/run-llama/llama_index/pull/20074))

### llama-index-instrumentation [0.4.2]

Section titled “llama-index-instrumentation [0.4.2]”

  * update instrumentation package metadata ([#20079](https://github.com/run-llama/llama_index/pull/20079))

### llama-index-llms-anthropic [0.9.5]

Section titled “llama-index-llms-anthropic [0.9.5]”

  * ✨ feat(anthropic): add prompt caching model validation utilities ([#20069](https://github.com/run-llama/llama_index/pull/20069))
  * fix streaming thinking/tool calling with anthropic ([#20077](https://github.com/run-llama/llama_index/pull/20077))
  * Add haiku 4.5 support ([#20092](https://github.com/run-llama/llama_index/pull/20092))

### llama-index-llms-baseten [0.1.6]

Section titled “llama-index-llms-baseten [0.1.6]”

  * Baseten provider Kimi K2 0711, Llama 4 Maverick and Llama 4 Scout Model APIs deprecation ([#20042](https://github.com/run-llama/llama_index/pull/20042))

### llama-index-llms-bedrock-converse [0.10.5]

Section titled “llama-index-llms-bedrock-converse [0.10.5]”

  * feat: List Claude Sonnet 4.5 as a reasoning model ([#20022](https://github.com/run-llama/llama_index/pull/20022))
  * feat: Support global cross-region inference profile prefix ([#20064](https://github.com/run-llama/llama_index/pull/20064))
  * Update utils.py for opus 4.1 ([#20076](https://github.com/run-llama/llama_index/pull/20076))
  * 4.1 opus bedrockconverse missing in funcitoncalling models ([#20084](https://github.com/run-llama/llama_index/pull/20084))
  * Add haiku 4.5 support ([#20092](https://github.com/run-llama/llama_index/pull/20092))

### llama-index-llms-fireworks [0.4.4]

Section titled “llama-index-llms-fireworks [0.4.4]”

  * Add Support for Custom Models in Fireworks LLM ([#20023](https://github.com/run-llama/llama_index/pull/20023))
  * fix(llms/fireworks): Cannot use Fireworks Deepseek V3.1-20006 issue ([#20028](https://github.com/run-llama/llama_index/pull/20028))

### llama-index-llms-oci-genai [0.6.3]

Section titled “llama-index-llms-oci-genai [0.6.3]”

  * Add support for xAI models in OCI GenAI ([#20089](https://github.com/run-llama/llama_index/pull/20089))

### llama-index-llms-openai [0.6.4]

Section titled “llama-index-llms-openai [0.6.4]”

  * Gpt 5 pro addition ([#20029](https://github.com/run-llama/llama_index/pull/20029))
  * fix collecting final response with openai responses streaming ([#20037](https://github.com/run-llama/llama_index/pull/20037))
  * Add support for GPT-5 models in utils.py (JSON_SCHEMA_MODELS) ([#20045](https://github.com/run-llama/llama_index/pull/20045))
  * chore: tool call block - part 1 ([#20074](https://github.com/run-llama/llama_index/pull/20074))

### llama-index-llms-sglang [0.1.0]

Section titled “llama-index-llms-sglang [0.1.0]”

  * Added Sglang llm integration ([#20020](https://github.com/run-llama/llama_index/pull/20020))

### llama-index-readers-gitlab [0.5.1]

Section titled “llama-index-readers-gitlab [0.5.1]”

  * feat(gitlab): add pagination params for repository tree and issues ([#20052](https://github.com/run-llama/llama_index/pull/20052))

### llama-index-readers-json [0.4.2]

Section titled “llama-index-readers-json [0.4.2]”

  * vbump the JSON reader ([#20039](https://github.com/run-llama/llama_index/pull/20039))

### llama-index-readers-web [0.5.5]

Section titled “llama-index-readers-web [0.5.5]”

  * fix: ScrapflyReader Pydantic validation error ([#19999](https://github.com/run-llama/llama_index/pull/19999))

### llama-index-storage-chat-store-dynamodb [0.4.2]

Section titled “llama-index-storage-chat-store-dynamodb [0.4.2]”

  * bump dynamodb chat store deps ([#20078](https://github.com/run-llama/llama_index/pull/20078))

### llama-index-tools-mcp [0.4.2]

Section titled “llama-index-tools-mcp [0.4.2]”

  * 🐛 fix(tools/mcp): Fix dict type handling and reference resolution in … ([#20082](https://github.com/run-llama/llama_index/pull/20082))

### llama-index-tools-signnow [0.1.0]

Section titled “llama-index-tools-signnow [0.1.0]”

  * feat(signnow): SignNow mcp tools integration ([#20057](https://github.com/run-llama/llama_index/pull/20057))

### llama-index-tools-tavily-research [0.4.2]

Section titled “llama-index-tools-tavily-research [0.4.2]”

  * feat: Add Tavily extract function for URL content extraction ([#20038](https://github.com/run-llama/llama_index/pull/20038))

### llama-index-vector-stores-azurepostgresql [0.2.0]

Section titled “llama-index-vector-stores-azurepostgresql [0.2.0]”

  * Add hybrid search to Azure PostgreSQL integration ([#20027](https://github.com/run-llama/llama_index/pull/20027))

### llama-index-vector-stores-milvus [0.9.3]

Section titled “llama-index-vector-stores-milvus [0.9.3]”

  * fix: Milvus get_field_kwargs() ([#20086](https://github.com/run-llama/llama_index/pull/20086))

### llama-index-vector-stores-opensearch [0.6.2]

Section titled “llama-index-vector-stores-opensearch [0.6.2]”

  * fix(opensearch): Correct version check for efficient filtering ([#20067](https://github.com/run-llama/llama_index/pull/20067))

### llama-index-vector-stores-qdrant [0.8.6]

Section titled “llama-index-vector-stores-qdrant [0.8.6]”

  * fix(qdrant): Allow async-only initialization with hybrid search ([#20005](https://github.com/run-llama/llama_index/pull/20005))

## [2025-10-03]

Section titled “[2025-10-03]”

### llama-index-core [0.14.4]

Section titled “llama-index-core [0.14.4]”

  * fix pre-release installs ([#20010](https://github.com/run-llama/llama_index/pull/20010))

### llama-index-embeddings-anyscale [0.4.2]

Section titled “llama-index-embeddings-anyscale [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-embeddings-baseten [0.1.2]

Section titled “llama-index-embeddings-baseten [0.1.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-embeddings-fireworks [0.4.2]

Section titled “llama-index-embeddings-fireworks [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-embeddings-opea [0.2.2]

Section titled “llama-index-embeddings-opea [0.2.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-embeddings-text-embeddings-inference [0.4.2]

Section titled “llama-index-embeddings-text-embeddings-inference [0.4.2]”

  * Fix authorization header setup logic in text embeddings inference ([#19979](https://github.com/run-llama/llama_index/pull/19979))

### llama-index-llms-anthropic [0.9.3]

Section titled “llama-index-llms-anthropic [0.9.3]”

  * feat: add anthropic sonnet 4.5 ([#19977](https://github.com/run-llama/llama_index/pull/19977))

### llama-index-llms-anyscale [0.4.2]

Section titled “llama-index-llms-anyscale [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-azure-openai [0.4.2]

Section titled “llama-index-llms-azure-openai [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-baseten [0.1.5]

Section titled “llama-index-llms-baseten [0.1.5]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-bedrock-converse [0.9.5]

Section titled “llama-index-llms-bedrock-converse [0.9.5]”

  * feat: Additional support for Claude Sonnet 4.5 ([#19980](https://github.com/run-llama/llama_index/pull/19980))

### llama-index-llms-deepinfra [0.5.2]

Section titled “llama-index-llms-deepinfra [0.5.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-everlyai [0.4.2]

Section titled “llama-index-llms-everlyai [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-fireworks [0.4.2]

Section titled “llama-index-llms-fireworks [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-google-genai [0.6.2]

Section titled “llama-index-llms-google-genai [0.6.2]”

  * Fix for ValueError: ChatMessage contains multiple blocks, use ‘ChatMe… ([#19954](https://github.com/run-llama/llama_index/pull/19954))

### llama-index-llms-keywordsai [1.1.2]

Section titled “llama-index-llms-keywordsai [1.1.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-localai [0.5.2]

Section titled “llama-index-llms-localai [0.5.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-mistralai [0.8.2]

Section titled “llama-index-llms-mistralai [0.8.2]”

  * Update list of MistralAI LLMs ([#19981](https://github.com/run-llama/llama_index/pull/19981))

### llama-index-llms-monsterapi [0.4.2]

Section titled “llama-index-llms-monsterapi [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-nvidia [0.4.4]

Section titled “llama-index-llms-nvidia [0.4.4]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-ollama [0.7.4]

Section titled “llama-index-llms-ollama [0.7.4]”

  * Fix `TypeError: unhashable type: 'dict'` in Ollama stream chat with tools ([#19938](https://github.com/run-llama/llama_index/pull/19938))

### llama-index-llms-openai [0.6.1]

Section titled “llama-index-llms-openai [0.6.1]”

  * feat(OpenAILike): support structured outputs ([#19967](https://github.com/run-llama/llama_index/pull/19967))

### llama-index-llms-openai-like [0.5.3]

Section titled “llama-index-llms-openai-like [0.5.3]”

  * feat(OpenAILike): support structured outputs ([#19967](https://github.com/run-llama/llama_index/pull/19967))

### llama-index-llms-openrouter [0.4.2]

Section titled “llama-index-llms-openrouter [0.4.2]”

  * chore(openrouter,anthropic): add py.typed ([#19966](https://github.com/run-llama/llama_index/pull/19966))

### llama-index-llms-perplexity [0.4.2]

Section titled “llama-index-llms-perplexity [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-portkey [0.4.2]

Section titled “llama-index-llms-portkey [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-sarvam [0.2.1]

Section titled “llama-index-llms-sarvam [0.2.1]”

  * fixed Sarvam Integration and Typos (Fixes #19931) ([#19932](https://github.com/run-llama/llama_index/pull/19932))

### llama-index-llms-upstage [0.6.4]

Section titled “llama-index-llms-upstage [0.6.4]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-llms-yi [0.4.2]

Section titled “llama-index-llms-yi [0.4.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-memory-bedrock-agentcore [0.1.0]

Section titled “llama-index-memory-bedrock-agentcore [0.1.0]”

  * feat: Bedrock AgentCore Memory integration ([#19953](https://github.com/run-llama/llama_index/pull/19953))

### llama-index-multi-modal-llms-openai [0.6.2]

Section titled “llama-index-multi-modal-llms-openai [0.6.2]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-readers-confluence [0.4.4]

Section titled “llama-index-readers-confluence [0.4.4]”

  * Fix: Respect cloud parameter when fetching child pages in ConfluenceR… ([#19983](https://github.com/run-llama/llama_index/pull/19983))

### llama-index-readers-service-now [0.2.2]

Section titled “llama-index-readers-service-now [0.2.2]”

  * Bug Fix :- Not Able to Fetch Page whose latest is empty or null ([#19916](https://github.com/run-llama/llama_index/pull/19916))

### llama-index-selectors-notdiamond [0.4.0]

Section titled “llama-index-selectors-notdiamond [0.4.0]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-tools-agentql [1.2.0]

Section titled “llama-index-tools-agentql [1.2.0]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-tools-playwright [0.3.1]

Section titled “llama-index-tools-playwright [0.3.1]”

  * chore: fix playwright tests ([#19946](https://github.com/run-llama/llama_index/pull/19946))

### llama-index-tools-scrapegraph [0.2.2]

Section titled “llama-index-tools-scrapegraph [0.2.2]”

  * feat: update scrapegraphai ([#19974](https://github.com/run-llama/llama_index/pull/19974))

### llama-index-vector-stores-chroma [0.5.3]

Section titled “llama-index-vector-stores-chroma [0.5.3]”

  * docs: fix query method docstring in ChromaVectorStore Fixes #19969 ([#19973](https://github.com/run-llama/llama_index/pull/19973))

### llama-index-vector-stores-mongodb [0.8.1]

Section titled “llama-index-vector-stores-mongodb [0.8.1]”

  * fix llm deps for openai ([#19944](https://github.com/run-llama/llama_index/pull/19944))

### llama-index-vector-stores-postgres [0.7.0]

Section titled “llama-index-vector-stores-postgres [0.7.0]”

  * fix index creation in postgres vector store ([#19955](https://github.com/run-llama/llama_index/pull/19955))

### llama-index-vector-stores-solr [0.1.0]

Section titled “llama-index-vector-stores-solr [0.1.0]”

  * Add ApacheSolrVectorStore Integration ([#19933](https://github.com/run-llama/llama_index/pull/19933))

## [2025-09-24]

Section titled “[2025-09-24]”

### llama-index-core [0.14.3]

Section titled “llama-index-core [0.14.3]”

  * Fix Gemini thought signature serialization ([#19891](https://github.com/run-llama/llama_index/pull/19891))
  * Adding a ThinkingBlock among content blocks ([#19919](https://github.com/run-llama/llama_index/pull/19919))

### llama-index-llms-anthropic [0.9.0]

Section titled “llama-index-llms-anthropic [0.9.0]”

  * Adding a ThinkingBlock among content blocks ([#19919](https://github.com/run-llama/llama_index/pull/19919))

### llama-index-llms-baseten [0.1.4]

Section titled “llama-index-llms-baseten [0.1.4]”

  * added kimik2 0905 and reordered list for validation ([#19892](https://github.com/run-llama/llama_index/pull/19892))
  * Baseten Dynamic Model APIs Validation ([#19893](https://github.com/run-llama/llama_index/pull/19893))

### llama-index-llms-google-genai [0.6.0]

Section titled “llama-index-llms-google-genai [0.6.0]”

  * Add missing FileAPI support for documents ([#19897](https://github.com/run-llama/llama_index/pull/19897))
  * Adding a ThinkingBlock among content blocks ([#19919](https://github.com/run-llama/llama_index/pull/19919))

### llama-index-llms-mistralai [0.8.0]

Section titled “llama-index-llms-mistralai [0.8.0]”

  * Adding a ThinkingBlock among content blocks ([#19919](https://github.com/run-llama/llama_index/pull/19919))

### llama-index-llms-openai [0.6.0]

Section titled “llama-index-llms-openai [0.6.0]”

  * Adding a ThinkingBlock among content blocks ([#19919](https://github.com/run-llama/llama_index/pull/19919))

### llama-index-protocols-ag-ui [0.2.2]

Section titled “llama-index-protocols-ag-ui [0.2.2]”

  * improve how state snapshotting works in AG-UI ([#19934](https://github.com/run-llama/llama_index/pull/19934))

### llama-index-readers-mongodb [0.5.0]

Section titled “llama-index-readers-mongodb [0.5.0]”

  * Use PyMongo Asynchronous API instead of Motor ([#19875](https://github.com/run-llama/llama_index/pull/19875))

### llama-index-readers-paddle-ocr [0.1.0]

Section titled “llama-index-readers-paddle-ocr [0.1.0]”

  * [New Package] Add PaddleOCR Reader for extracting text from images in PDFs ([#19827](https://github.com/run-llama/llama_index/pull/19827))

### llama-index-readers-web [0.5.4]

Section titled “llama-index-readers-web [0.5.4]”

  * feat(readers/web-firecrawl): migrate to Firecrawl v2 SDK ([#19773](https://github.com/run-llama/llama_index/pull/19773))

### llama-index-storage-chat-store-mongo [0.3.0]

Section titled “llama-index-storage-chat-store-mongo [0.3.0]”

  * Use PyMongo Asynchronous API instead of Motor ([#19875](https://github.com/run-llama/llama_index/pull/19875))

### llama-index-storage-kvstore-mongodb [0.5.0]

Section titled “llama-index-storage-kvstore-mongodb [0.5.0]”

  * Use PyMongo Asynchronous API instead of Motor ([#19875](https://github.com/run-llama/llama_index/pull/19875))

### llama-index-tools-valyu [0.5.0]

Section titled “llama-index-tools-valyu [0.5.0]”

  * Add Valyu Extractor and Fast mode ([#19915](https://github.com/run-llama/llama_index/pull/19915))

### llama-index-vector-stores-azureaisearch [0.4.2]

Section titled “llama-index-vector-stores-azureaisearch [0.4.2]”

  * Fix/llama index vector stores azureaisearch fix ([#19800](https://github.com/run-llama/llama_index/pull/19800))

### llama-index-vector-stores-azurepostgresql [0.1.0]

Section titled “llama-index-vector-stores-azurepostgresql [0.1.0]”

  * Add support for Azure PostgreSQL ([#19709](https://github.com/run-llama/llama_index/pull/19709))

### llama-index-vector-stores-qdrant [0.8.5]

Section titled “llama-index-vector-stores-qdrant [0.8.5]”

  * Add proper compat for old sparse vectors ([#19882](https://github.com/run-llama/llama_index/pull/19882))

### llama-index-vector-stores-singlestoredb [0.4.2]

Section titled “llama-index-vector-stores-singlestoredb [0.4.2]”

  * Fix SQLi Vulnerability in SingleStore Db ([#19914](https://github.com/run-llama/llama_index/pull/19914))

## [2025-09-15]

Section titled “[2025-09-15]”

### `llama-index-core` [0.14.2]

Section titled “llama-index-core [0.14.2]”

  * fix: handle data urls in ImageBlock (#19856)
  * fix: Move IngestionPipeline docstore document insertion after transformations (#19849)
  * fix: Update IngestionPipeline async document store insertion (#19868)
  * chore: remove stepwise usage of workflows from code (#19877)

### `llama-index-embeddings-fastembed` [0.5.0]

Section titled “llama-index-embeddings-fastembed [0.5.0]”

  * feat: make fastembed cpu or gpu optional (#19878)

### `llama-index-llms-deepseek` [0.2.2]

Section titled “llama-index-llms-deepseek [0.2.2]”

  * feat: pass context_window to super in deepseek llm (#19876)

### `llama-index-llms-google-genai` [0.5.0]

Section titled “llama-index-llms-google-genai [0.5.0]”

  * feat: Add GoogleGenAI FileAPI support for large files (#19853)

### `llama-index-readers-solr` [0.1.0]

Section titled “llama-index-readers-solr [0.1.0]”

  * feat: Add Solr reader integration (#19843)

### `llama-index-retrievers-alletra-x10000-retriever` [0.1.0]

Section titled “llama-index-retrievers-alletra-x10000-retriever [0.1.0]”

  * feat: add AlletraX10000Retriever integration (#19798)

### `llama-index-vector-stores-oracledb` [0.3.2]

Section titled “llama-index-vector-stores-oracledb [0.3.2]”

  * feat: OraLlamaVS Connection Pool Support + Filtering (#19412)

### `llama-index-vector-stores-postgres` [0.6.8]

Section titled “llama-index-vector-stores-postgres [0.6.8]”

  * feat: Add `customize_query_fn` to PGVectorStore (#19847)

## [2025-09-14]

Section titled “[2025-09-14]”

### `llama-index-core` [0.14.1]

Section titled “llama-index-core [0.14.1]”

  * feat: add verbose option to RetrieverQueryEngine for detailed output (#19807)
  * feat: feat: add support for additional kwargs in `aget_text_embedding_batch` method (#19808)
  * feat: add `thinking_delta` field to AgentStream events to expose llm reasoning (#19785)
  * fix: Bug fix agent streaming thinking delta pydantic validation (#19828)
  * fix: handle positional args and kwargs both in tool calling (#19822)

### `llama-index-instrumentation` [0.4.1]

Section titled “llama-index-instrumentation [0.4.1]”

  * feat: add sync event/handler support (#19825)

### `llama-index-llms-google-genai` [0.4.0]

Section titled “llama-index-llms-google-genai [0.4.0]”

  * feat: Add VideoBlock and GoogleGenAI video input support (#19823)

### `llama-index-llms-ollama` [0.7.3]

Section titled “llama-index-llms-ollama [0.7.3]”

  * fix: Fix bug using Ollama with Agents and None tool_calls in final message (#19844)

### `llama-index-llms-vertex` [0.6.1]

Section titled “llama-index-llms-vertex [0.6.1]”

  * fix: align complete/acomplete responses (#19806)

### `llama-index-readers-confluence` [0.4.3]

Section titled “llama-index-readers-confluence [0.4.3]”

  * chore: Bump version constraint for atlassian-python-api to include 4.x (#19824)

### `llama-index-readers-github` [0.6.2]

Section titled “llama-index-readers-github [0.6.2]”

  * fix: Make url optional (#19851)

### `llama-index-readers-web` [0.5.3]

Section titled “llama-index-readers-web [0.5.3]”

  * feat: Add OlostepWebReader Integration (#19821)

### `llama-index-tools-google` [0.6.2]

Section titled “llama-index-tools-google [0.6.2]”

  * feat: Add optional creds argument to GoogleCalendarToolSpec (#19826)

### `llama-index-vector-stores-vectorx` [0.1.0]

Section titled “llama-index-vector-stores-vectorx [0.1.0]”

  * feat: Add vectorx vectorstore (#19758)

## [2025-09-08]

Section titled “[2025-09-08]”

**NOTE:** All packages have been bumped to handle the latest llama-index-core
version.

### `llama-index-core` [0.14.0]

Section titled “llama-index-core [0.14.0]”

  * breaking: bumped `llama-index-workflows` dependency to 2.0 
    * Improve stacktraces clarity by avoiding wrapping errors in WorkflowRuntimeError
    * Remove deprecated checkpointer feature
    * Remove deprecated sub-workflows feature
    * Remove deprecated `send_event` method from Workflow class (still existing on the Context class)
    * Remove deprecated `stream_events()` methods from Workflow class (still existing on the Context class)
    * Remove deprecated support for stepwise execution

### `llama-index-llms-openai` [0.5.6]

Section titled “llama-index-llms-openai [0.5.6]”

  * feat: add support for document blocks in openai chat completions (#19809)

## [2025-09-06]

Section titled “[2025-09-06]”

### `llama-index-core` [0.13.6]

Section titled “llama-index-core [0.13.6]”

  * chore: remove openai selector from core utils function (#19803)

### `llama-index-llms-cometapi` [0.1.0]

Section titled “llama-index-llms-cometapi [0.1.0]”

  * feat: Add CometAPI LLM integration (#19793)

## [2025-09-04]

Section titled “[2025-09-04]”

### `llama-index-core` [0.13.5]

Section titled “llama-index-core [0.13.5]”

  * feat: add thinking delta field to AgentStream events to expose from LLM responses (#19785)
  * fix: fix path handling in SimpleDirectoryReader and PDFReader path fix (#19794)

### `llama-index-llms-bedrock-converse` [0.9.0]

Section titled “llama-index-llms-bedrock-converse [0.9.0]”

  * feat: add system prompt and tool caching config kwargs to BedrockConverse (#19737)

### `llama-index-llms-litellm` [0.6.2]

Section titled “llama-index-llms-litellm [0.6.2]”

  * fix: Handle missing tool call IDs with UUID fallback (#19789)
  * fix: Fix critical context window calculation (#19787)

### `llama-index-readers-file` [0.5.3]

Section titled “llama-index-readers-file [0.5.3]”

  * fix: fix path handling in SimpleDirectoryReader and PDFReader path fix (#19794)

### `llama-index-storage-chat-store-yugabytedb` [0.1.0]

Section titled “llama-index-storage-chat-store-yugabytedb [0.1.0]”

  * feat: add Yugabytedb chat store (#19768)

### `llama-index-vector-stores-milvus` [0.9.1]

Section titled “llama-index-vector-stores-milvus [0.9.1]”

  * fix: create TextNode if no ‘_node_content’ set (#19772)

### `llama-index-vector-stores-postgres` [0.6.5]

Section titled “llama-index-vector-stores-postgres [0.6.5]”

  * fix: make postgres regex punctuation handling consistent with plainto_tsquery (#19781)

## [2025-09-01]

Section titled “[2025-09-01]”

### `llama-index-core` [0.13.4]

Section titled “llama-index-core [0.13.4]”

  * feat: Add PostgreSQL schema support to Memory and SQLAlchemyChatStore (#19741)
  * feat: add missing sync wrapper of put_messages in memory (#19746)
  * feat: add option for an initial tool choice in FunctionAgent (#19738)
  * fix: Calling ContextChatEngine with a QueryBundle (instead of a string) (#19714)

### `llama-index-embeddings-baseten` [0.1.0]

Section titled “llama-index-embeddings-baseten [0.1.0]”

  * feat: baseten integration (#19710)

### `llama-index-embeddings-ibm` [0.5.0]

Section titled “llama-index-embeddings-ibm [0.5.0]”

  * feat: Support for additional/external urls, make instance_id deprecated (#19749)

### `llama-index-llms-baseten` [0.1.0]

Section titled “llama-index-llms-baseten [0.1.0]”

  * feat: baseten integration (#19710)

### `llama-index-llms-bedrock-converse` [0.8.3]

Section titled “llama-index-llms-bedrock-converse [0.8.3]”

  * feat: add `amazon.nova-premier-v1:0` to BEDROCK_MODELS (#19728)

### `llama-index-llms-ibm` [0.6.0]

Section titled “llama-index-llms-ibm [0.6.0]”

  * feat: Support for additional/external urls, make instance_id deprecated (#19749)

### `llama-index-postprocessor-ibm` [0.3.0]

Section titled “llama-index-postprocessor-ibm [0.3.0]”

  * feat: Support for additional/external urls, make instance_id deprecated (#19749)

### `llama-index-postprocessor-sbert-rerank` [0.4.1]

Section titled “llama-index-postprocessor-sbert-rerank [0.4.1]”

  * fix: fix SentenceTransformerRerank init device (#19756)

### `llama-index-readers-google` [0.7.1]

Section titled “llama-index-readers-google [0.7.1]”

  * feat: raise google drive errors (#19752)

### `llama-index-readers-web` [0.5.1]

Section titled “llama-index-readers-web [0.5.1]”

  * feat: Add ZenRows web reader (#19699)

### `llama-index-vector-stores-chroma` [0.5.2]

Section titled “llama-index-vector-stores-chroma [0.5.2]”

  * feat: add mmr search to chroma (#19731)

### `llama-index-vector-stores-postgres` [0.6.4]

Section titled “llama-index-vector-stores-postgres [0.6.4]”

  * fix: Use the indexed metadata field ‘ref_doc_id’ instead of ‘doc_id’ during deletion (#19759)

### `llama-index-vector-stores-qdrant` [0.8.2]

Section titled “llama-index-vector-stores-qdrant [0.8.2]”

feat: Payload indexes support to QdrantVectorStore (#19743)

## [2025-08-22]

Section titled “[2025-08-22]”

### `llama-index-core` [0.13.3]

Section titled “llama-index-core [0.13.3]”

  * fix: add timeouts on image `.get()` requests (#19723)
  * fix: fix StreamingAgentChatResponse losses message bug (#19674)
  * fix: Fixing crashing when retrieving from empty vector store index (#19706)
  * fix: Calling ContextChatEngine with a QueryBundle (instead of a string) (#19714)
  * fix: Fix faithfulness evaluate crash when no images provided (#19686)

### `llama-index-embeddings-heroku` [0.1.0]

Section titled “llama-index-embeddings-heroku [0.1.0]”

  * feat: Adds support for HerokuEmbeddings (#19685)

### `llama-index-embeddings-ollama` [0.8.2]

Section titled “llama-index-embeddings-ollama [0.8.2]”

  * feat: enhance OllamaEmbedding with instruction support (#19721)

### `llama-index-llms-anthropic` [0.8.5]

Section titled “llama-index-llms-anthropic [0.8.5]”

  * fix: Fix prompt caching with CachePoint (#19711)

### `llama-index-llms-openai` [0.5.4]

Section titled “llama-index-llms-openai [0.5.4]”

  * feat: add gpt-5-chat-latest model support (#19687)

### `llama-index-llms-sagemaker-endpoint` [0.4.1]

Section titled “llama-index-llms-sagemaker-endpoint [0.4.1]”

  * fix: fix constructor region read to not read region_name before is popped from kwargs, and fix assign to super (#19705)

### `llama-index-llms-upstage` [0.6.2]

Section titled “llama-index-llms-upstage [0.6.2]”

  * chore: remove deprecated model(solar-pro) (#19704)

### `llama-index-readers-confluence` [0.4.1]

Section titled “llama-index-readers-confluence [0.4.1]”

  * fix: Support concurrent use of multiple ConfluenceReader instances (#19698)

### `llama-index-vector-stores-chroma` [0.5.1]

Section titled “llama-index-vector-stores-chroma [0.5.1]”

  * fix: fix `get_nodes()` with empty node ids (#19711)

### `llama-index-vector-stores-qdrant` [0.8.1]

Section titled “llama-index-vector-stores-qdrant [0.8.1]”

  * feat: support qdrant sharding (#19652)

### `llama-index-vector-stores-tencentvectordb` [0.4.1]

Section titled “llama-index-vector-stores-tencentvectordb [0.4.1]”

  * fix: Resolve AttributeError in CollectionParams.filter_fields access (#19695)

## [2025-08-14]

Section titled “[2025-08-14]”

### `llama-index-core` [0.13.2]

Section titled “llama-index-core [0.13.2]”

  * feat: allow streaming to be disabled in agents (#19668)
  * fix: respect the value of NLTK_DATA env var if present (#19664)
  * fix: Order preservation and fetching in batch non-cached embeddings in `a/get_text_embedding_batch()` (#19536)

### `llama-index-embeddings-ollama` [0.8.1]

Section titled “llama-index-embeddings-ollama [0.8.1]”

  * fix: Access embedding output (#19635)
  * fix: use normalized embeddings (#19622)

### `llama-index-graph-rag-cognee` [0.3.0]

Section titled “llama-index-graph-rag-cognee [0.3.0]”

  * fix: Update and fix cognee integration (#19650)

### `llama-index-llms-anthropic` [0.8.4]

Section titled “llama-index-llms-anthropic [0.8.4]”

  * fix: Error in Anthropic extended thinking with tool use (#19642)
  * chore: context window for claude 4 sonnet to 1 mln tokens (#19649)

### `llama-index-llms-bedrock-converse` [0.8.2]

Section titled “llama-index-llms-bedrock-converse [0.8.2]”

  * feat: add openai-oss models to BedrockConverse (#19653)

### `llama-index-llms-ollama` [0.7.1]

Section titled “llama-index-llms-ollama [0.7.1]”

  * fix: fix ollama role response detection (#19671)

### `llama-index-llms-openai` [0.5.3]

Section titled “llama-index-llms-openai [0.5.3]”

  * fix: AzureOpenAI streaming token usage (#19633)

### `llama-index-readers-file` [0.5.1]

Section titled “llama-index-readers-file [0.5.1]”

  * feat: enhance PowerPoint reader with comprehensive content extraction (#19478)

### `llama-index-retrievers-bm25` [0.6.3]

Section titled “llama-index-retrievers-bm25 [0.6.3]”

  * fix: fix persist+load for bm25 (#19657)

### `llama-index-retrievers-superlinked` [0.1.0]

Section titled “llama-index-retrievers-superlinked [0.1.0]”

  * feat: add Superlinked retriever integration (#19636)

### `llama-index-tools-mcp` [0.4.0]

Section titled “llama-index-tools-mcp [0.4.0]”

  * feat: Handlers for custom types and pydantic models in tools (#19601)

### `llama-index-vector-stores-clickhouse` [0.6.0]

Section titled “llama-index-vector-stores-clickhouse [0.6.0]”

  * chore: Updates to ClickHouse integration based on new vector search capabilities in ClickHouse (#19647)

### `llama-index-vector-stores-postgres` [0.6.3]

Section titled “llama-index-vector-stores-postgres [0.6.3]”

  * fix: Add other special characters in `ts_query` normalization (#19637)

## [2025-08-08]

Section titled “[2025-08-08]”

### `llama-index-core` [0.13.1]

Section titled “llama-index-core [0.13.1]”

  * fix: safer token counting in messages (#19599)
  * fix: Fix Document truncation in `FunctionTool._parse_tool_output` (#19585)
  * feat: Enabled partially formatted system prompt for ReAct agent (#19598)

### `llama-index-embeddings-ollama` [0.8.0]

Section titled “llama-index-embeddings-ollama [0.8.0]”

  * fix: use /embed instead of /embeddings for ollama (#19622)

### `llama-index-embeddings-voyageai` [0.4.1]

Section titled “llama-index-embeddings-voyageai [0.4.1]”

  * feat: Add support for voyage context embeddings (#19590)

### `llama-index-graph-stores-kuzu` [0.9.0]

Section titled “llama-index-graph-stores-kuzu [0.9.0]”

  * feat: Update Kuzu graph store integration to latest SDK (#19603)

### `llama-index-indices-managed-llama-cloud` [0.9.1]

Section titled “llama-index-indices-managed-llama-cloud [0.9.1]”

  * chore: deprecate llama-index-indices-managed-llama-cloud in favor of llama-cloud-services (#19608)

### `llama-index-llms-anthropic` [0.8.2]

Section titled “llama-index-llms-anthropic [0.8.2]”

  * feat: anthropic citation update to non-beta support (#19624)
  * feat: add support for opus 4.1 (#19593)

### `llama-index-llms-heroku` [0.1.0]

Section titled “llama-index-llms-heroku [0.1.0]”

  * feat: heroku llm integration (#19576)

### `llama-index-llms-nvidia` [0.4.1]

Section titled “llama-index-llms-nvidia [0.4.1]”

  * feat: add support for gpt-oss NIM (#19618)

### `llama-index-llms-oci-genai` [0.6.1]

Section titled “llama-index-llms-oci-genai [0.6.1]”

  * chore: update list of supported LLMs for OCI integration (#19604)

### `llama-index-llms-openai` [0.5.2]

Section titled “llama-index-llms-openai [0.5.2]”

  * fix: fix isinstance check in openai (#19617)
  * feat: add gpt-5 (#19613)

### `llama-index-llms-upstage` [0.6.1]

Section titled “llama-index-llms-upstage [0.6.1]”

  * fix: Fix reasoning_effort parameter ineffective and Add new custom parameters (#19619)

### `llama-index-postprocessor-presidio` [0.5.0]

Section titled “llama-index-postprocessor-presidio [0.5.0]”

  * feat: Support presidio entities (#19584)

### `llama-index-retrievers-bm25` [0.6.2]

Section titled “llama-index-retrievers-bm25 [0.6.2]”

  * fix: BM25 Retriever allow `top_k` value greater than number of nodes added (#19577)
  * feat: Add metadata filtering support to BM25 Retriever and update documentation (#19586)

### `llama-index-tools-aws-bedrock-agentcore` [0.1.0]

Section titled “llama-index-tools-aws-bedrock-agentcore [0.1.0]”

  * feat: Bedrock AgentCore browser and code interpreter toolspecs (#19559)

### `llama-index-vector-stores-baiduvectordb` [0.6.0]

Section titled “llama-index-vector-stores-baiduvectordb [0.6.0]”

  * fix: fix filter operators and add stores_text support (#19591)
  * feat: add wait logic for critical operations (#19587)

### `llama-index-vector-stores-postgres` [0.6.2]

Section titled “llama-index-vector-stores-postgres [0.6.2]”

  * fix: Fixed special character bug in PGVectorStore query (#19621)
  * fix: change ts_query definition to avoid double-stemming (#19581)

## [2025-07-30]

Section titled “[2025-07-30]”

**NOTE:** All packages have been bumped to handle the latest llama-index-core
version.

### `llama-index-core` [0.13.0]

Section titled “llama-index-core [0.13.0]”

  * breaking: removed deprecated agent classes, including `FunctionCallingAgent`, the older `ReActAgent` implementation, `AgentRunner`, all step workers, `StructuredAgentPlanner`, `OpenAIAgent`, and more. All users should migrate to the new workflow based agents: `FunctionAgent`, `CodeActAgent`, `ReActAgent`, and `AgentWorkflow` (#19529)
  * breaking: removed deprecated `QueryPipeline` class and all associated code (#19554)
  * breaking: changed default `index.as_chat_engine()` to return a `CondensePlusContextChatEngine`. Agent-based chat engines have been removed (which was the previous default). If you need an agent, use the above mentioned agent classes. (#19529)
  * fix: Update BaseDocumentStore to not return Nones in result (#19513)
  * fix: Fix FunctionTool param doc parsing and signature mutation; update tests (#19532)
  * fix: Handle empty prompt in MockLLM.stream_complete (#19521)

### `llama-index-embeddings-mixedbreadai` [0.5.0]

Section titled “llama-index-embeddings-mixedbreadai [0.5.0]”

  * feat: Update mixedbread embeddings and rerank for latest sdk (#19519)

### `llama-index-instrumentation` [0.4.0]

Section titled “llama-index-instrumentation [0.4.0]”

  * fix: let wrapped exceptions bubble up (#19566)

### `llama-index-llms-google-genai` [0.3.0]

Section titled “llama-index-llms-google-genai [0.3.0]”

  * feat: Add Thought Summaries and signatures for Gemini (#19505)

### `llama-index-llms-nvidia` [0.4.0]

Section titled “llama-index-llms-nvidia [0.4.0]”

  * feat: add support for kimi-k2-instruct (#19525)

### `llama-index-llms-upstage` [0.6.0]

Section titled “llama-index-llms-upstage [0.6.0]”

  * feat: add new upstage model(solar-pro2) (#19526)

### `llama-index-postprocessor-mixedbreadai-rerank` [0.5.0]

Section titled “llama-index-postprocessor-mixedbreadai-rerank [0.5.0]”

  * feat: Update mixedbread embeddings and rerank for latest sdk (#19519)

### `llama-index-readers-github` [0.8.0]

Section titled “llama-index-readers-github [0.8.0]”

  * feat: Github Reader enhancements for file filtering and custom processing (#19543)

### `llama-index-readers-s3` [0.5.0]

Section titled “llama-index-readers-s3 [0.5.0]”

  * feat: add support for region_name via `client_kwargs` in S3Reader (#19546)

### `llama-index-tools-valyu` [0.4.0]

Section titled “llama-index-tools-valyu [0.4.0]”

  * feat: Update Valyu sdk to latest version (#19538)

### `llama-index-voice-agents-gemini-live` [0.2.0]

Section titled “llama-index-voice-agents-gemini-live [0.2.0]”

  * feat(beta): adding first implementation of gemini live (#19489)

### `llama-index-vector-stores-astradb` [0.5.0]

Section titled “llama-index-vector-stores-astradb [0.5.0]”

  * feat: astradb get nodes + delete nodes support (#19544)

### `llama-index-vector-stores-milvus` [0.9.0]

Section titled “llama-index-vector-stores-milvus [0.9.0]”

  * feat: Add support for specifying partition_names in Milvus search configuration (#19555)

### `llama-index-vector-stores-s3` [0.2.0]

Section titled “llama-index-vector-stores-s3 [0.2.0]”

  * fix: reduce some metadata keys from S3VectorStore to save space (#19550)

### `llama-index-vector-stores-postgres` [0.6.0]

Section titled “llama-index-vector-stores-postgres [0.6.0]”

  * feat: Add support for ANY/ALL postgres operators (#19553)

## [2025-07-22]

Section titled “[2025-07-22]”

### `llama-index-core` [0.12.52.post1]

Section titled “llama-index-core [0.12.52.post1]”

  * fix: do not write system prompt to memory in agents (#19512)

### `llama-index-core` [0.12.52]

Section titled “llama-index-core [0.12.52]”

  * fix: Fix missing prompt in async MultiModalLLMProgram calls (#19504)
  * fix: Properly raise errors from docstore, fixes Vector Index Retrieval for `stores_text=True/False` (#19501)

### `llama-index-indices-managed-bge-m3` [0.5.0]

Section titled “llama-index-indices-managed-bge-m3 [0.5.0]”

  * feat: optimize memory usage for BGEM3Index persistence (#19496)

### `llama-index-readers-web` [0.4.5]

Section titled “llama-index-readers-web [0.4.5]”

  * feat: Add timeout to webpage readers, defaults to 60 seconds (#19503)

### `llama-index-tools-jira-issue` [0.1.0]

Section titled “llama-index-tools-jira-issue [0.1.0]”

  * feat: added jira issue tool spec (#19457)

### `llama-index-vector-stores-azureaisearch` [0.3.10]

Section titled “llama-index-vector-stores-azureaisearch [0.3.10]”

  * chore: add `**kwargs` into AzureAISearchVectorStore super init (#19500)

### `llama-index-vector-stores-neo4jvector` [0.4.1]

Section titled “llama-index-vector-stores-neo4jvector [0.4.1]”

  * fix: Patch Neo4jVector Call version (#19498)

## [2025-07-21]

Section titled “[2025-07-21]”

### `llama-index-core` [0.12.51]

Section titled “llama-index-core [0.12.51]”

  * feat: Enhance FunctionTool with auto type conversion for basic Python types like date when using pydantic fields in functions (#19479)
  * fix: Fix retriever KeyError when using FAISS and other vector stores that do no store text (#19476)
  * fix: add system prompt to memory and use it also for structured generation (#19490)

### `llama-index-readers-azstorage-blob` [0.3.2]

Section titled “llama-index-readers-azstorage-blob [0.3.2]”

  * fix: Fix metadata serialization issue in AzStorageBlobReader (#19491)

## [2025-07-19]

Section titled “[2025-07-19]”

### `llama-index-core` [0.12.50]

Section titled “llama-index-core [0.12.50]”

  * feat: support html table extraction in MarkdownElementNodeParser (#19449)
  * fix/slightly breaking: make `get_cache_dir()` function more secure by changing default location (#19415)
  * fix: resolve race condition in SQLAlchemyChatStore with precise timestamps (#19432)
  * fix: update document store import to use BaseDocumentStore in DocumentContextExtractor (#19466)
  * fix: improve empty retrieval check in vector index retriever (#19471)
  * fix: Fix running workflow agents as MCP servers by adding start event handling to workflow agents (#19470)
  * fix: handle ID type mismatch in various retrievers (#19448)
  * fix: add structured output to multi agent also from secondary constructor + tests (#19435)
  * fix: duplicated `session_id` metadata_filter in VectorMemoryBlock (#19427)
  * fix: make sure to stop agent on function tool return direct (#19413)
  * fix: use a private folder to store NTLK cache (#19444)
  * fix: Update ReAct agent parse error message (#19431)

### `llama-index-instrumentation` [0.3.0]

Section titled “llama-index-instrumentation [0.3.0]”

  * feat: Improve instrumentation span name (#19454)

### `llama-index-llms-bedrock-converse` [0.7.6]

Section titled “llama-index-llms-bedrock-converse [0.7.6]”

  * chore: added llama 4 models in Bedrock Converse, remove llama 3.2 1b and 3b from function calling models (#19434)

### `llama-index-llms-cloudflare-ai-gateway` [0.1.0]

Section titled “llama-index-llms-cloudflare-ai-gateway [0.1.0]”

  * feat: introduce cloudflare ai gateway (#19395)

### `llama-index-llms-google-genai` [0.2.5]

Section titled “llama-index-llms-google-genai [0.2.5]”

  * feat: Add `google_search` Tool Support to GoogleGenAI LLM Integration (#19406)

### `llama-index-readers-confluence` [0.3.2]

Section titled “llama-index-readers-confluence [0.3.2]”

  * refactor: various Confluence reader enhancements (logging, error handling) (#19424)

### `llama-index-readers-service-now` [0.1.0]

Section titled “llama-index-readers-service-now [0.1.0]”

  * feat: added service-now reader (#19429)

### `llama-index-protocols-ag-ui` [0.1.4]

Section titled “llama-index-protocols-ag-ui [0.1.4]”

  * chore: remove some stray debug prints from AGUI (#19469)

### `llama-index-tools-wikipedia` [0.3.1]

Section titled “llama-index-tools-wikipedia [0.3.1]”

  * fix: Remove load_kwargs from `WikipediaToolSpec.load_data` tool (#19464)

### `llama-index-vector-stores-baiduvectordb` [0.3.1]

Section titled “llama-index-vector-stores-baiduvectordb [0.3.1]”

  * fix: pass `**kwargs` to `super().__init__` in BaiduVectorDB (#19436)

### `llama-index-vector-stores-moorcheh` [0.1.1]

Section titled “llama-index-vector-stores-moorcheh [0.1.1]”

  * fix: Update Moorcheh Vector Store namespace resolution (#19461)

### `llama-index-vector-stores-s3` [0.1.0]

Section titled “llama-index-vector-stores-s3 [0.1.0]”

  * feat: s3 vectors support (#19456)

## [2025-07-14]

Section titled “[2025-07-14]”

### `llama-index-core` [0.12.49]

Section titled “llama-index-core [0.12.49]”

  * fix: skip tests on CI (#19416)
  * fix: fix structured output (#19414)
  * Fix: prevent duplicate triplets in SimpleGraphStore.upsert_triplet (#19404)
  * Add retry capability to workflow agents (#19393)
  * chore: modifying raptors dependencies with stricter rules to avoid test failures (#19394)
  * feat: adding a first implementation of structured output in agents (#19337)
  * Add tests for and fix issues with Vector Store node serdes (#19388)
  * Refactor vector index retrieval (#19382)
  * Retriever Query Engine should use async node postprocessors (#19380)

### `llama-index-llms-bedrock-converse` [0.7.5]

Section titled “llama-index-llms-bedrock-converse [0.7.5]”

  * Fix BedrockConverse streaming token counting by handling messageStop … (#19369)

### `llama-index-llms-nvidia` [0.3.5]

Section titled “llama-index-llms-nvidia [0.3.5]”

  * nvidia-llm : Adding support to use llm models outside default list (#19366)

### `llama-index-llms-oci-genai` [0.5.2]

Section titled “llama-index-llms-oci-genai [0.5.2]”

  * Fix bugs in tool calling for OCI generative AI Llama models (#19376)

### `llama-index-postprocessor-flashrank-rerank` [0.1.0]

Section titled “llama-index-postprocessor-flashrank-rerank [0.1.0]”

  * Fix bugs in tool calling for OCI generative AI Llama models (#19376)

### `llama-index-readers-web` [0.4.4]

Section titled “llama-index-readers-web [0.4.4]”

  * fix: avoid SimpleWebPageReader and others to use url as a Document id (#19398)

### `llama-index-storage-docstore-duckdb` [0.1.0]

Section titled “llama-index-storage-docstore-duckdb [0.1.0]”

  * Add DuckDB KV, Document, and Index Store (#19282)

### `llama-index-storage-index-store-duckdb` [0.1.0]

Section titled “llama-index-storage-index-store-duckdb [0.1.0]”

  * Add DuckDB KV, Document, and Index Store (#19282)

### `llama-index-storage-kvstore-duckdb` [0.1.3]

Section titled “llama-index-storage-kvstore-duckdb [0.1.3]”

  * DuckDB: Deadlocks-b-gone (#19401)
  * Improvements for DuckDB thread safety and embed dimension handling (#19391)
  * Add DuckDB KV, Document, and Index Store (#19282)

### `llama-index-vector-stores-duckdb` [0.4.6]

Section titled “llama-index-vector-stores-duckdb [0.4.6]”

  * DuckDB: Deadlocks-b-gone (#19401)
  * Improvements for DuckDB thread safety and embed dimension handling (#19391)
  * DuckDB Async and Faster Cosine Similarity (#19383)
  * DuckDB Small clean-up and add embeddings to returned nodes (#19377)

### `llama-index-vector-stores-moorcheh` [0.1.0]

Section titled “llama-index-vector-stores-moorcheh [0.1.0]”

  * feat: Add Moorcheh vector store integration (#19349)

## [2025-07-09]

Section titled “[2025-07-09]”

### `llama-index-core` [0.12.48]

Section titled “llama-index-core [0.12.48]”

  * fix: convert dict chat_history to ChatMessage objects in AgentWorkflowStartEvent (#19371)
  * fix: Replace ctx.get/set with ctx.store.get/set in Context (#19350)
  * Bump the pip group across 6 directories with 1 update (#19357)
  * Make fewer trips to KV store during Document Hash Checks (#19362)
  * Don’t store Copy of document in metadata and properly return Nodes (#19343)
  * Bump llama-index-core from 0.12.8 to 0.12.41 in /docs in the pip group across 1 directory (#19345)
  * fix: Ensure CallbackManager is applied to default embed_model (#19335)
  * fix publish sub-package workflow (#19338)

### `llama-index-embeddings-huggingface-optimum-intel` [0.3.1]

Section titled “llama-index-embeddings-huggingface-optimum-intel [0.3.1]”

  * Fix IntelEmbedding base.py (#19351)

### `llama-index-indices-managed-lancedb` [0.1.0]

Section titled “llama-index-indices-managed-lancedb [0.1.0]”

  * Fix broken lancedb tests (#19352)

### `llama-index-indices-managed-llamacloud` [0.7.10]

Section titled “llama-index-indices-managed-llamacloud [0.7.10]”

  * vbump llama-cloud (#19355)
  * Fix async retrieval of page figure nodes (#19334)

### `llama-index-llms-google-genai` [0.2.4]

Section titled “llama-index-llms-google-genai [0.2.4]”

  * Add Cached Content Support to GoogleGenAI LLM Integration (#19361)

### `llama-index-llms-oci-genai` [0.5.1]

Section titled “llama-index-llms-oci-genai [0.5.1]”

  * Add support of Image prompt for OCI generative AI Llama models (#19306)

### `llama-index-readers-file` [0.4.11]

Section titled “llama-index-readers-file [0.4.11]”

  * swamp xml for defusedxml (#19342)

### `llama-index-storage-chat-stores-postgres` [0.2.2]

Section titled “llama-index-storage-chat-stores-postgres [0.2.2]”

  * Update asyncpg (#19365)

## [2025-07-06]

Section titled “[2025-07-06]”

### `llama-index-core` [0.12.47]

Section titled “llama-index-core [0.12.47]”

  * feat: add default `max_iterations` arg to `.run()` of 20 for agents (#19035)
  * feat: set `tool_required` to `True` for `FunctionCallingProgram` and structured LLMs where supported (#19326)
  * fix: fix missing raw in agent workflow events (#19325)
  * fix: fixed parsing of empty list in parsing json output (#19318)
  * chore: Deprecate Multi Modal LLMs (#19115) 
    * All existing multi-modal llms are now extensions of their base `LLM` counterpart
    * Base `LLM` classes support multi-modal features in `llama-index-core`
    * Base `LLM` classes use `ImageBlock` internally to support multi-modal features

### `llama-index-cli` [0.4.4]

Section titled “llama-index-cli [0.4.4]”

  * fix: prevent command injection vulnerability in RAG CLI —clear flag (#19322)

### `llama-index-indices-managed-lancedb` [0.1.0]

Section titled “llama-index-indices-managed-lancedb [0.1.0]”

  * feat: Adding an integration for LanceDB MultiModal AI LakeHouse (#19232)

### `llama-index-llms-anthropic` [0.7.6]

Section titled “llama-index-llms-anthropic [0.7.6]”

  * feat: anthropic citations support (#19316)

### `llama-index-llms-oci-genai` [0.5.1]

Section titled “llama-index-llms-oci-genai [0.5.1]”

  * feat: Add support of Image prompt for OCI generative AI Llama models (#19306)

### `llama-index-readers-web` [0.4.3]

Section titled “llama-index-readers-web [0.4.3]”

  * chore: Add firecrawl integration source (#19203)

## [2025-07-02]

Section titled “[2025-07-02]”

### `llama-index-core` [0.12.46]

Section titled “llama-index-core [0.12.46]”

  * feat: Add async delete and insert to vector store index (#19281)
  * fix: Fixing ChatMessage to str handling of empty inputs (#19302)
  * fix: fix function tool context detection with typed context (#19309)
  * fix: inconsistent ref node handling (#19286)
  * chore: simplify citation block schema (#19308)

### `llama-index-embeddings-google-genai` [0.2.1]

Section titled “llama-index-embeddings-google-genai [0.2.1]”

  * chore: bump min google-genai version (#19304)

### `llama-index-embeddings-nvidia` [0.3.4]

Section titled “llama-index-embeddings-nvidia [0.3.4]”

  * fix: embedding model with custom endpoints 404 error (#19295)

### `llama-index-llms-google-genai` [0.2.3]

Section titled “llama-index-llms-google-genai [0.2.3]”

  * chore: bump min google-genai version (#19304)

### `llama-index-tools-mcp` [0.2.6]

Section titled “llama-index-tools-mcp [0.2.6]”

  * fix: configuring resources from the mcp server correctly (#19307)

### `llama-index-voice-agents-elevenlabs` [0.3.0-beta]

Section titled “llama-index-voice-agents-elevenlabs [0.3.0-beta]”

  * fix: Migrating Elevenlabs to adjust it to framework standard (#19273)

## [2025-06-30]

Section titled “[2025-06-30]”

### `llama-index-core` [0.12.45]

Section titled “llama-index-core [0.12.45]”

  * feat: allow tools to output content blocks (#19265)
  * feat: Add chat UI events and models to core package (#19242)
  * fix: Support loading `Node` from ingestion cache (#19279)
  * fix: Fix SemanticDoubleMergingSplitterNodeParser not respecting max_chunk_size (#19235)
  * fix: replace `get_doc_id()` with `id_` in base index (#19266)
  * chore: remove usage and references to deprecated Context get/set API (#19275)
  * chore: deprecate older agent packages (#19249)

### `llama-index-llms-anthropic` [0.7.5]

Section titled “llama-index-llms-anthropic [0.7.5]”

  * feat: Adding new AWS Claude models available on Bedrock (#19233)

### `llama-index-embeddings-azure-openai` [0.3.9]

Section titled “llama-index-embeddings-azure-openai [0.3.9]”

  * feat: Add dimensions parameter to AzureOpenAIEmbedding (#19239)

### `llama-index-embeddings-bedrock` [0.5.2]

Section titled “llama-index-embeddings-bedrock [0.5.2]”

  * feat: Update aioboto3 dependency (#19237)

### `llama-index-llms-bedrock-converse` [0.7.4]

Section titled “llama-index-llms-bedrock-converse [0.7.4]”

  * feat: Update aioboto3 dependency (#19237)

### `llama-index-llms-dashscope` [0.4.1]

Section titled “llama-index-llms-dashscope [0.4.1]”

  * fix: Fix dashscope qwen assistant api Error response problem, extract `tool_calls` info from ChatMessage kwargs to top level (#19224)

### `llama-index-memory-mem0` [0.3.2]

Section titled “llama-index-memory-mem0 [0.3.2]”

  * feat: Adapting Mem0 to new framework memory standard (#19234)

### `llama-index-tools-google` [0.5.0]

Section titled “llama-index-tools-google [0.5.0]”

  * feat: Add proper async google search to tool spec (#19250)
  * fix: Clean up results in GoogleSearchToolSpec (#19246)

### `llama-index-vector-stores-postgres` [0.5.4]

Section titled “llama-index-vector-stores-postgres [0.5.4]”

  * fix: Fix pg vector store sparse query (#19241)

## [2025-06-25]

Section titled “[2025-06-25]”

### `llama-index-core` [0.12.44]

Section titled “llama-index-core [0.12.44]”

  * feat: Adding a `CachePoint` content block for caching chat messages (#19193)
  * fix: fix react system header formatting in workflow agent (#19158)
  * fix: fix ReActOutputParser when no “Thought:” prefix is produced by the LLM (#19190)
  * fix: Fixed string striping in react output parser (#19192)
  * fix: properly handle system prompt for CodeAct agent (#19191)
  * fix: Exclude raw field in AgentStream event to fix potential serialization issue (#19150)
  * chore: Mark older agent architectures in core as deprecated (#19205)
  * chore: deprecate query pipelines in code (#19206)

### `llama-index-embeddings-fastembed` [0.3.5]

Section titled “llama-index-embeddings-fastembed [0.3.5]”

  * feat: Add Batch Support for FastEmbed (#19147)

### `llama-index-embeddings-huggingface` [0.5.5]

Section titled “llama-index-embeddings-huggingface [0.5.5]”

  * feat: Add async batching for huggingface using `asyncio.to_thread` (#19207)

### `llama-index-llms-anthropic` [0.7.4]

Section titled “llama-index-llms-anthropic [0.7.4]”

  * fix: update kwargs for anthropic bedrock (#19169)

### `llama-index-llms-google-genai` [0.2.2]

Section titled “llama-index-llms-google-genai [0.2.2]”

  * fix: Setting up System instruction properly for google genai client (#19196)

### `llama-index-llms-mistralai` [0.6.1]

Section titled “llama-index-llms-mistralai [0.6.1]”

  * fix: Fix image url handling in Mistral AI (#19139)

### `llama-index-llms-perplexity` [0.3.7]

Section titled “llama-index-llms-perplexity [0.3.7]”

  * fix: make api_key use `PPLX_API_KEY` in perplexity llm integration (#19217)

### `llama-index-postprocessor-bedrock-rerank` [0.4.0]

Section titled “llama-index-postprocessor-bedrock-rerank [0.4.0]”

  * fix: Avoid changing ‘top_n’ self attribute at runtime (#19221)

### `llama-index-postprocessor-sbert-rerank` [0.3.2]

Section titled “llama-index-postprocessor-sbert-rerank [0.3.2]”

  * feat: add `cross_encoder_kwargs` parameter for advanced configuration (#19148)

### `llama-index-utils-workflow` [0.3.5]

Section titled “llama-index-utils-workflow [0.3.5]”

  * feat: Adding visualization functions for single/multi agent workflows (#19101)

### `llama-index-vector-stores-azureaisearch` [0.3.8]

Section titled “llama-index-vector-stores-azureaisearch [0.3.8]”

  * feat: Enable forwarding of arbitrary Azure Search SDK parameters in AzureAISearchVectorStore for document retrieval (#19173)

### `llama-index-vector-stores-db2` [0.1.0]

Section titled “llama-index-vector-stores-db2 [0.1.0]”

  * feat: add IBM Db2 vector store (#19195)

### `llama-index-vector-stores-duckdb` [0.4.0]

Section titled “llama-index-vector-stores-duckdb [0.4.0]”

  * feat: refactor DuckDB VectorStore (#19106)

### `llama-index-vector-stores-pinecone` [0.6.0]

Section titled “llama-index-vector-stores-pinecone [0.6.0]”

  * feat: support pinecone v7 (#19163)
  * fix: support python version `>=3.9,<4.0` for `llama-index-vector-stores-pinecone` (#19186)

### `llama-index-vector-stores-qdrant` [0.6.1]

Section titled “llama-index-vector-stores-qdrant [0.6.1]”

  * fix: fix types with IN/NIN filters in qdrant (#19159)

### `llama-index-voice-agents-openai` [0.1.1-beta]

Section titled “llama-index-voice-agents-openai [0.1.1-beta]”

  * feat: Adding beta OpenAI Realtime Conversation integration (#19010)

## [2025-06-18]

Section titled “[2025-06-18]”

### `llama-index-core` [0.12.43]

Section titled “llama-index-core [0.12.43]”

  * feat: Make BaseWorkflowAgent a workflow itself (#19052)
  * fix: make the progress bar of title extractor unified (#19131)
  * fix: Use `get_tqdm_iterable` in SimpleDirectoryReader (#18722)
  * chore: move out Workflows code to `llama-index-workflows` and keeping backward compatibility (#19043)
  * chore: move instrumentation code out to its own package `llama-index-instrumentation` (#19062)

### `llama-index-llms-bedrock-converse` [0.7.2]

Section titled “llama-index-llms-bedrock-converse [0.7.2]”

  * fix: improve empty tool call handling in bedrock converse (#19084)

### `llama-index-llms-openai` [0.4.7]

Section titled “llama-index-llms-openai [0.4.7]”

  * fix: fix building openai responses dicts (#19089, #19094)

### `llama-index-llms-perplexity` [0.3.6]

Section titled “llama-index-llms-perplexity [0.3.6]”

  * feat: Perf/improve robustness of perplexity llm integration (#19022)

### `llama-index-postprocessor-sbert-rerank` [0.3.1]

Section titled “llama-index-postprocessor-sbert-rerank [0.3.1]”

  * feat: Added cache dir to Sentence Transformers post processor (#19097)

### `llama-index-protocols-ag-ui` [0.1.2]

Section titled “llama-index-protocols-ag-ui [0.1.2]”

  * feat: add `ag-ui` protocol support (#19104, #19103, #19102, #18898)

### `llama-index-readers-google` [0.6.2]

Section titled “llama-index-readers-google [0.6.2]”

  * fix: Fix error getting metadata file IDs in google drive reader (#19118)

### `llama-index-readers-hive` [0.3.1]

Section titled “llama-index-readers-hive [0.3.1]”

  * chore: deprecate and remove hive reader (#18990)

### `llama-index-readers-mongodb` [0.3.2]

Section titled “llama-index-readers-mongodb [0.3.2]”

  * feat: Added Async driver for `alazy_load_data` for mongodb reader (#19038)

### `llama-index-storage-chat-store-sqlite` [0.1.1]

Section titled “llama-index-storage-chat-store-sqlite [0.1.1]”

  * fix: sqlite chat store compatibility with sqlalchemy 1.4 (#19067)

### `llama-index-tools-hive` [0.1.0]

Section titled “llama-index-tools-hive [0.1.0]”

  * feat: Add Hive Intelligence search tool (#19029)

### `llama-index-utils-workflow` [0.3.4]

Section titled “llama-index-utils-workflow [0.3.4]”

  * feat: support drawing mermaid diagrams of workflows (#19083)

### `llama-index-vector-stores-lancedb` [0.3.3]

Section titled “llama-index-vector-stores-lancedb [0.3.3]”

  * fix: create table with pre-defined schema (#19064)

### `llama-index-vector-stores-milvus` [0.8.5]

Section titled “llama-index-vector-stores-milvus [0.8.5]”

  * fix: `Connections.connect()` got multiple values for argument `alias` (#19119)

### `llama-index-vector-stores-opengauss` [0.1.0]

Section titled “llama-index-vector-stores-opengauss [0.1.0]”

  * feat: add openGauss integration (#19024)

## [2025-06-11]

Section titled “[2025-06-11]”

### `llama-index-core` [0.12.42]

Section titled “llama-index-core [0.12.42]”

  * fix: pass input message to memory get (#19054)
  * fix: use async memory operations within async functions (#19032)
  * fix: Using uuid instead of hashing for broader compatibility in SQLTableNodeMapping (#19011)

### `llama-index-embeddings-bedrock` [0.5.1]

Section titled “llama-index-embeddings-bedrock [0.5.1]”

  * feat: Update aioboto3 dependency (#19015)

### `llama-index-indices-managed-llama-cloud` [0.7.7]

Section titled “llama-index-indices-managed-llama-cloud [0.7.7]”

  * feat: figure retrieval SDK integration (#19017)
  * fix: Return empty list when argument `raw_figure_nodes` is None type in `page_figure_nodes_to_node_with_score` (#19053)

### `llama-index-llms-mistralai` [0.6.0]

Section titled “llama-index-llms-mistralai [0.6.0]”

  * feat: Add reasoning support to mistralai LLM + magistral (#19048)

### `llama-index-llms-openai` [0.4.5]

Section titled “llama-index-llms-openai [0.4.5]”

  * feat: O3 pro day 0 support (#19030)
  * fix: skip tool description length check in openai response api (#18956)

### `llama-index-llms-perplexity` [0.3.5]

Section titled “llama-index-llms-perplexity [0.3.5]”

  * fix: perplexity llm integration bug fix (#19007)

### `llama-index-multi-modal-llms-openai-like` [0.1.0]

Section titled “llama-index-multi-modal-llms-openai-like [0.1.0]”

  * feat: add openai like multi-modal LLM (#18997)

### `llama-index-postprocessor-bedrock-rerank` [0.3.3]

Section titled “llama-index-postprocessor-bedrock-rerank [0.3.3]”

  * feat: Prefer ‘BedrockRerank’ over ‘AWSBedrockRerank’ (#19016)

### `llama-index-readers-papers` [0.3.1]

Section titled “llama-index-readers-papers [0.3.1]”

  * fix: make filename hashing more robust (#18318)

### `llama-index-tools-artifact-editor` [0.1.0]

Section titled “llama-index-tools-artifact-editor [0.1.0]”

  * feat: Create ArtifactEditorToolSpec for editing pydantic objects (#18989)

### `llama-index-utils-workflow` [0.3.3]

Section titled “llama-index-utils-workflow [0.3.3]”

  * feat: Add label truncation to workflow visualization (#19027)

### `llama-index-vector-stores-opensearch` [0.5.6]

Section titled “llama-index-vector-stores-opensearch [0.5.6]”

  * feat: Add ability to exclude source fields from query response (#19018)

### `llama-index-voice-agents-elevenlabs` [0.2.0-beta]

Section titled “llama-index-voice-agents-elevenlabs [0.2.0-beta]”

  * fix: Docs corrections + integrating tools for ElevenLabs integration (#19014)

## [2025-06-07]

Section titled “[2025-06-07]”

### `llama-index-core` [0.12.41]

Section titled “llama-index-core [0.12.41]”

  * feat: Add MutableMappingKVStore for easier caching (#18893)
  * fix: async functions in tool specs (#19000)
  * fix: properly apply file limit to SimpleDirectoryReader (#18983)
  * fix: overwriting of LLM callback manager from Settings (#18951)
  * fix: Adding warning in the docstring of JsonPickleSerializer for the user to deserialize only safe things, rename to PickleSerializer (#18943)
  * fix: ImageDocument path and url checking to ensure that the input is really an image (#18947)
  * chore: remove some unused utils from core (#18985)

### `llama-index-embeddings-azure-openai` [0.3.8]

Section titled “llama-index-embeddings-azure-openai [0.3.8]”

  * fix: Azure api-key and azure-endpoint resolution fixes (#18975)
  * fix: api_base vs azure_endpoint resolution fixes (#19002)

### `llama-index-graph-stores-ApertureDB` [0.1.0]

Section titled “llama-index-graph-stores-ApertureDB [0.1.0]”

  * feat: Aperturedb propertygraph (#18749)

### `llama-index-indices-managed-llama-cloud` [0.7.4]

Section titled “llama-index-indices-managed-llama-cloud [0.7.4]”

  * fix: resolve retriever llamacloud index (#18949)
  * chore: composite retrieval add ReRankConfig (#18973)

### `llama-index-llms-azure-openai` [0.3.4]

Section titled “llama-index-llms-azure-openai [0.3.4]”

  * fix: api_base vs azure_endpoint resolution fixes (#19002)

### `llama-index-llms-bedrock-converse` [0.7.1]

Section titled “llama-index-llms-bedrock-converse [0.7.1]”

  * fix: handle empty message content to prevent ValidationError (#18914)

### `llama-index-llms-litellm` [0.5.1]

Section titled “llama-index-llms-litellm [0.5.1]”

  * feat: Add DocumentBlock support to LiteLLM integration (#18955)

### `llama-index-llms-ollama` [0.6.2]

Section titled “llama-index-llms-ollama [0.6.2]”

  * feat: Add support for the new think feature in ollama (#18993)

### `llama-index-llms-openai` [0.4.4]

Section titled “llama-index-llms-openai [0.4.4]”

  * feat: add OpenAI JSON Schema structured output support (#18897)
  * fix: skip tool description length check in openai response api (#18956)

### `llama-index-packs-searchain` [0.1.0]

Section titled “llama-index-packs-searchain [0.1.0]”

  * feat: Add searchain package (#18929)

### `llama-index-readers-docugami` [0.3.1]

Section titled “llama-index-readers-docugami [0.3.1]”

  * fix: Avoid hash collision in XML parsing (#18986)

### `llama-index-readers-file` [0.4.9]

Section titled “llama-index-readers-file [0.4.9]”

  * fix: pin llama-index-readers-file pandas for now (#18976)

### `llama-index-readers-gcs` [0.4.1]

Section titled “llama-index-readers-gcs [0.4.1]”

  * feat: Allow newer versions of gcsfs (#18987)

### `llama-index-readers-obsidian` [0.5.2]

Section titled “llama-index-readers-obsidian [0.5.2]”

  * fix: Obsidian reader checks and skips hardlinks (#18950)

### `llama-index-readers-web` [0.4.2]

Section titled “llama-index-readers-web [0.4.2]”

  * fix: Use httpx instead of urllib in llama-index-readers-web (#18945)

### `llama-index-storage-kvstore-postgres` [0.3.5]

Section titled “llama-index-storage-kvstore-postgres [0.3.5]”

  * fix: Remove unnecessary psycopg2 from llama-index-storage-kvstore-postgres dependencies (#18964)

### `llama-index-tools-mcp` [0.2.5]

Section titled “llama-index-tools-mcp [0.2.5]”

  * fix: actually format the workflow args into a start event instance (#19001)
  * feat: Adding support for log recording during MCP tool calls (#18927)

### `llama-index-vector-stores-chroma` [0.4.2]

Section titled “llama-index-vector-stores-chroma [0.4.2]”

  * fix: Update ChromaVectorStore port field and argument types (#18977)

### `llama-index-vector-stores-milvus` [0.8.4]

Section titled “llama-index-vector-stores-milvus [0.8.4]”

  * feat: Upsert Entities supported in Milvus (#18962)

### `llama-index-vector-stores-redis` [0.5.2]

Section titled “llama-index-vector-stores-redis [0.5.2]”

  * fix: Correcting Redis URL/Client handling (#18982)

### `llama-index-voice-agents-elevenlabs` [0.1.0-beta]

Section titled “llama-index-voice-agents-elevenlabs [0.1.0-beta]”

  * feat: ElevenLabs beta integration (#18967)

## [2025-06-02]

Section titled “[2025-06-02]”

### `llama-index-core` [0.12.40]

Section titled “llama-index-core [0.12.40]”

  * feat: Add StopEvent step validation so only one workflow step can handle StopEvent (#18932)
  * fix: Add compatibility check before providing `tool_required` to LLM args (#18922)

### `llama-index-embeddings-cohere` [0.5.1]

Section titled “llama-index-embeddings-cohere [0.5.1]”

  * fix: add batch size validation with 96 limit for Cohere API (#18915)

### `llama-index-llms-anthropic` [0.7.2]

Section titled “llama-index-llms-anthropic [0.7.2]”

  * feat: Support passing static AWS credentials to Anthropic Bedrock (#18935)
  * fix: Handle untested no tools scenario for anthropic tool config (#18923)

### `llama-index-llms-google-genai` [0.2.1]

Section titled “llama-index-llms-google-genai [0.2.1]”

  * fix: use proper auto mode for google-genai function calling (#18933)

### `llama-index-llms-openai` [0.4.2]

Section titled “llama-index-llms-openai [0.4.2]”

  * fix: clear up some field typing issues of OpenAI LLM API (#18918)
  * fix: migrate broken `reasoning_effort` kwarg to `reasoning_options` dict in OpenAIResponses class (#18920)

### `llama-index-tools-measurespace` [0.1.0]

Section titled “llama-index-tools-measurespace [0.1.0]”

  * feat: Add weather, climate, air quality and geocoding tool from Measure Space (#18909)

### `llama-index-tools-mcp` [0.2.3]

Section titled “llama-index-tools-mcp [0.2.3]”

  * feat: Add headers handling to BasicMCPClient (#18919)

## [2025-05-30]

Section titled “[2025-05-30]”

### `llama-index-core` [0.12.39]

Section titled “llama-index-core [0.12.39]”

  * feat: Adding Resource to perform dependency injection in Workflows (docs coming soon!) (#18884)
  * feat: Add `require_tool` param to function calling LLMs (#18654)
  * fix: make prefix and response non-required for hitl events (#18896)
  * fix: SelectionOutputParser when LLM chooses no choices (#18886)

### `llama-index-indices-managed-llama-cloud` [0.7.2]

Section titled “llama-index-indices-managed-llama-cloud [0.7.2]”

  * feat: add non persisted composite retrieval (#18908)

### `llama-index-llms-bedrock-converse` [0.7.0]

Section titled “llama-index-llms-bedrock-converse [0.7.0]”

  * feat: Update aioboto3 dependency to allow latest version (#18889)

### `llama-index-llms-ollama` [0.6.1]

Section titled “llama-index-llms-ollama [0.6.1]”

  * Support ollama 0.5.0 SDK, update ollama docs (#18904)

### `llama-index-vector-stores-milvus` [0.8.3]

Section titled “llama-index-vector-stores-milvus [0.8.3]”

  * feat: Multi language analyzer supported in Milvus (#18901)

## [2025-05-28]

Section titled “[2025-05-28]”

### `llama-index-core` [0.12.38]

Section titled “llama-index-core [0.12.38]”

  * feat: Adding a very simple implementation of an embeddings cache (#18864)
  * feat: Add `cols_retrievers` in NLSQLRetriever (#18843)
  * feat: Add row, col, and table retrievers as args in NLSQLTableQueryEngine (#18874)
  * feat: add configurable allow_parallel_tool_calls to FunctionAgent (#18829)
  * feat: Allow ctx in BaseToolSpec functions, other ctx + tool calling overhauls (#18783)
  * feat: Optimize get_biggest_prompt for readability and efficiency (#18808)
  * fix: prevent DoS attacks in JSONReader (#18877)
  * fix: SelectionOutputParser when LLM chooses no choices (#18886)
  * fix: resuming AgentWorkflow from ctx during hitl (#18844)
  * fix: context serialization during AgentWorkflow runs (#18866)
  * fix: Throw error if content block resolve methods yield empty bytes (#18819)
  * fix: Reduce issues when parsing “Thought/Action/Action Input” ReActAgent completions (#18818)
  * fix: Strip code block backticks from QueryFusionRetriever llm response (#18825)
  * fix: Fix `get_function_tool` in function_program.py when schema doesn’t have “title” key (#18796)

### `llama-index-agent-azure-foundry` [0.1.0]

Section titled “llama-index-agent-azure-foundry [0.1.0]”

  * feat: add azure foundry agent integration (#18772)

### `llama-index-agent-llm-compiler` [0.3.1]

Section titled “llama-index-agent-llm-compiler [0.3.1]”

  * feat: llm-compiler support `stream_step`/`astream_step` (#18809)

### `llama-index-embeddings-google-genai` [0.2.0]

Section titled “llama-index-embeddings-google-genai [0.2.0]”

  * feat: add gemini embeddings tests and retry configs (#18846)

### `llama-index-embeddings-openai-like` [0.1.1]

Section titled “llama-index-embeddings-openai-like [0.1.1]”

  * fix: Pass `http_client` & `async_http_client` to parent for OpenAILikeEmbedding (#18881)

### `llama-index-embeddings-voyageai` [0.3.6]

Section titled “llama-index-embeddings-voyageai [0.3.6]”

  * feat: Introducing voyage-3.5 models (#18793)

### `llama-index-indices-managed-llama-cloud` [0.7.1]

Section titled “llama-index-indices-managed-llama-cloud [0.7.1]”

  * feat: add client support for `search_filters_inference_schema` (#18867)
  * feat: add async methods and blank index creation (#18859)

### `llama-index-llms-anthropic` [0.6.19]

Section titled “llama-index-llms-anthropic [0.6.19]”

  * feat: update for claude 4 support in Anthropic LLM (#18817)
  * fix: thinking + tool calls in anthropic (#18834)
  * fix: check thinking is non-null in anthropic messages (#18838)
  * fix: update/fix claude-4 support (#18820)

### `llama-index-llms-bedrock-converse` [0.6.0]

Section titled “llama-index-llms-bedrock-converse [0.6.0]”

  * feat: add-claude4-model-support (#18827)
  * fix: fixing DocumentBlock usage within Bedrock Converse (#18791)
  * fix: calling tools with empty arguments (#18786)

### `llama-index-llms-cleanlab` [0.5.0]

Section titled “llama-index-llms-cleanlab [0.5.0]”

  * feat: Update package name and models (#18483)

### `llama-index-llms-featherlessai` [0.1.0]

Section titled “llama-index-llms-featherlessai [0.1.0]”

  * feat: featherless-llm-integration (#18778)

### `llama-index-llms-google-genai` [0.1.14]

Section titled “llama-index-llms-google-genai [0.1.14]”

  * fix: Google GenAI token counting behavior, add basic retry mechanism (#18876)

### `llama-index-llms-ollama` [0.5.6]

Section titled “llama-index-llms-ollama [0.5.6]”

  * feat: Attempt to automatically set context window in ollama (#18822)
  * feat: use default temp in ollama models (#18815)

### `llama-index-llms-openai` [0.3.44]

Section titled “llama-index-llms-openai [0.3.44]”

  * feat: Adding new OpenAI responses features (image gen, mcp call, code interpreter) (#18810)
  * fix: Update OpenAI response type imports for latest openai library compatibility (#18824)
  * fix: Skip tool description length check in OpenAI agent (#18790)

### `llama-index-llms-servam` [0.1.1]

Section titled “llama-index-llms-servam [0.1.1]”

  * feat: add Servam AI LLM integration with OpenAI-like interface (#18841)

### `llama-index-observability-otel` [0.1.0]

Section titled “llama-index-observability-otel [0.1.0]”

  * feat: OpenTelemetry integration for observability (#18744)

### `llama-index-packs-raptor` [0.3.2]

Section titled “llama-index-packs-raptor [0.3.2]”

  * Use global `llama_index` tokenizer in Raptor clustering (#18802)

### `llama-index-postprocessor-rankllm-rerank` [0.5.0]

Section titled “llama-index-postprocessor-rankllm-rerank [0.5.0]”

  * feat: use latest rank-llm sdk (#18831)

### `llama-index-readers-azstorage-blob` [0.3.1]

Section titled “llama-index-readers-azstorage-blob [0.3.1]”

  * fix: Metadata and filename in azstorageblobreader (#18816)

### `llama-index-readers-file` [0.4.8]

Section titled “llama-index-readers-file [0.4.8]”

  * fix: reading pptx files from remote fs (#18862)

### `llama-index-storage-kvstore-postgres` [0.3.1]

Section titled “llama-index-storage-kvstore-postgres [0.3.1]”

  * feat: Create PostgresKVStore from existing SQLAlchemy Engine (#18798)

### `llama-index-tools-brightdata` [0.1.0]

Section titled “llama-index-tools-brightdata [0.1.0]”

  * feat: brightdata integration (#18690)

### `llama-index-tools-google` [0.3.1]

Section titled “llama-index-tools-google [0.3.1]”

  * fix: `GmailToolSpec.load_data()` calls search with missing args (#18832)

### `llama-index-tools-mcp` [0.2.2]

Section titled “llama-index-tools-mcp [0.2.2]”

  * feat: enhance SSE endpoint detection for broader compatibility (#18868)
  * feat: overhaul `BasicMCPClient` to support all MCP features (#18833)
  * fix: McpToolSpec fetch all tools given the empty allowed_tools list (#18879)
  * fix: add missing `BasicMCPClient.with_oauth()` kwargs (#18845)

### `llama-index-tools-valyu` [0.2.0]

Section titled “llama-index-tools-valyu [0.2.0]”

  * feat: Update to valyu 2.0.0 (#18861)

### `llama-index-vector-stores-azurecosmosmongo` [0.6.0]

Section titled “llama-index-vector-stores-azurecosmosmongo [0.6.0]”

  * feat: Add Vector Index Compression support for Azure Cosmos DB Mongo vector store (#18850)

### `llama-index-vector-stores-opensearch` [0.5.5]

Section titled “llama-index-vector-stores-opensearch [0.5.5]”

  * feat: add filter support to check if a metadata key doesn’t exist (#18851)
  * fix: dont pass in both `extra_info` and `metadata` in vector store nodes (#18805)

## [2025-05-19]

Section titled “[2025-05-19]”

### `llama-index-core` [0.12.37]

Section titled “llama-index-core [0.12.37]”

  * Ensure `Memory` returns at least one message (#18763)
  * Separate text blocks with newlines when accessing `message.content` (#18763)
  * reset `next_agent` in multi agent workflows (#18782)
  * support sqlalchemy v1 in chat store (#18780)
  * fix: broken hotpotqa dataset URL (#18764)
  * Use `get_tqdm_iterable` in SimpleDirectoryReader (#18722)
  * Pass agent workflow kwargs into start event (#18747)
  * fix(chunking): Ensure correct handling of multi-byte characters during AST node chunking (#18702)

### `llama-index-llms-anthropic` [0.6.14]

Section titled “llama-index-llms-anthropic [0.6.14]”

  * Fixed DocumentBlock handling in OpenAI and Anthropic (#18769)

### `llama-index-llms-bedrock-converse` [0.5.4]

Section titled “llama-index-llms-bedrock-converse [0.5.4]”

  * Fix tool call parsing for bedrock converse (#18781)
  * feat: add missing client params for bedrock (#18768)
  * fix merging multiple tool calls in bedrock converse (#18761)

### `llama-index-llms-openai` [0.3.42]

Section titled “llama-index-llms-openai [0.3.42]”

  * Fixed DocumentBlock handling in OpenAI and Anthropic (#18769)
  * Remove tool-length check in openai (#18784)
  * Add check for empty tool call delta, bump version (#18745)

### `llama-index-llms-openai-like` [0.3.5]

Section titled “llama-index-llms-openai-like [0.3.5]”

  * Remove tool-length check in openai (#18784)

### `llama-index-retrievers-vectorize` [0.1.0]

Section titled “llama-index-retrievers-vectorize [0.1.0]”

  * Add Vectorize retriever (#18685)

### `llama-index-tools-desearch` [0.1.0]

Section titled “llama-index-tools-desearch [0.1.0]”

  * Feature/desearch integration (#18738)

## [2025-05-14]

Section titled “[2025-05-14]”

### `llama-index-core` [0.12.36]

Section titled “llama-index-core [0.12.36]”

  * add support for automatic session_id filtering in vector memory blocks (#18730)
  * Add feature: support for DocumentBlock in chat messages (#18719)
  * Added initial Async methods for BaseIndex (#18711)
  * use fs to check ingestion pipeline path (#18680)
  * add edge case handling in StreamingAgentChatResponse (#18679)

### `llama-index-embeddings-azure-openai` [0.3.5]

Section titled “llama-index-embeddings-azure-openai [0.3.5]”

  * look for azure openai key env var in auzre embeddings (#18703)
  * only get `api_key` if not `use_azure_ad` (#18708)
  * fix typo of the if branch of get `api_key` if not `use_azure_ad` (#18720)

### `llama-index-embeddings-cohere` [0.5.0]

Section titled “llama-index-embeddings-cohere [0.5.0]”

  * Support Cohere V4 embeddings and V2 client (#18464)

### `llama-index-embeddings-fastembed` [0.3.2]

Section titled “llama-index-embeddings-fastembed [0.3.2]”

  * Bugfix: FastEmbedEmbedding was missing code to pass extra arguments to the api (#18695)

### `llama-index-graph-stores-neptune` [0.3.3]

Section titled “llama-index-graph-stores-neptune [0.3.3]”

  * fix: Handle possible OverflowError when getting Neptune node properties (#18687)

### `llama-index-readers-legacy-office` [0.1.1]

Section titled “llama-index-readers-legacy-office [0.1.1]”

  * feat: `legacy_office`, Apache Tika based `.doc` reader (#18649)
  * chore: fix lagecy office reader bloated metadata (#18696)

### `llama-index-retrievers-vectorize` [0.1.0]

Section titled “llama-index-retrievers-vectorize [0.1.0]”

  * Add Vectorize retriever (#18685)

### `llama-index-tools-brightdata` [0.1.0]

Section titled “llama-index-tools-brightdata [0.1.0]”

  * Feature/brightdata integration (#18690)

### `llama-index-tools-mcp` [0.1.3]

Section titled “llama-index-tools-mcp [0.1.3]”

  * MCP one-liners for workflow servers and function tools (#18729)

### `llama-index-tools-openapi` [0.4.0]

Section titled “llama-index-tools-openapi [0.4.0]”

  * feat Improve OpenAPI and Requests tool capabilities and reliability (#18681)

### `llama-index-tools-requests` [0.4.0]

Section titled “llama-index-tools-requests [0.4.0]”

  * feat Improve OpenAPI and Requests tool capabilities and reliability (#18681)

### `llama-index-vector-stores-milvus` [0.8.2]

Section titled “llama-index-vector-stores-milvus [0.8.2]”

  * fix(MilvusVectorStore): use primary key from milvus by its name instead of ‘id’ (#18714)

### `llama-index-vector-stores-postgres` [0.5.3]

Section titled “llama-index-vector-stores-postgres [0.5.3]”

  * Add `IS_EMPTY` support for PGVectorStore (#18667)

### `llama-index-vector-stores-redis` [0.5.1]

Section titled “llama-index-vector-stores-redis [0.5.1]”

  * Adding Async Redis Vector Store support (#18675)

## [2025-05-08]

Section titled “[2025-05-08]”

### `llama-index-core` [0.12.35]

Section titled “llama-index-core [0.12.35]”

  * add support for prefilling partial tool kwargs on `FunctionTool` (#18658)
  * Fix/react agent max iterations skipping (#18634)
  * handling for edge-case serialization in prebuilt workflows like `AgentWorkflow` (#18628)
  * memory revamp with new base class (#18594)
  * add prebuilt memory blocks (#18607)

### `llama-index-embeddings-autoembeddings` [0.1.0]

Section titled “llama-index-embeddings-autoembeddings [0.1.0]”

  * Support for AutoEmbeddings integration from chonkie (#18578)

### `llama-index-embeddings-huggingface-api` [0.3.1]

Section titled “llama-index-embeddings-huggingface-api [0.3.1]”

  * Fix dep versions for huggingface-hub (#18662)

### `llama-index-indices-managed-vectara` [0.4.5]

Section titled “llama-index-indices-managed-vectara [0.4.5]”

  * Bugfix in using cutoff argument with chain reranker in Vectara (#18610)

### `llama-index-llms-anthropic` [0.6.12]

Section titled “llama-index-llms-anthropic [0.6.12]”

  * anthropic citations and tool calls (#18657)

### `llama-index-llms-cortex` [0.3.0]

Section titled “llama-index-llms-cortex [0.3.0]”

  * Cortex enhancements 2 for auth (#18588)

### `llama-index-llms-dashscope` [0.3.3]

Section titled “llama-index-llms-dashscope [0.3.3]”

  * Fix dashscope tool call parsing (#18608)

### `llama-index-llms-google-genai` [0.1.12]

Section titled “llama-index-llms-google-genai [0.1.12]”

  * Fix modifying object references in google-genai llm (#18616)
  * feat(llama-index-llms-google-genai): 2.5-flash-preview tests (#18575)
  * Fix last_msg indexing (#18611)

### `llama-index-llms-huggingface-api` [0.4.3]

Section titled “llama-index-llms-huggingface-api [0.4.3]”

  * Huggingface API fixes for task and deps (#18662)

### `llama-index-llms-litellm` [0.4.2]

Section titled “llama-index-llms-litellm [0.4.2]”

  * fix parsing streaming tool calls (#18653)

### `llama-index-llms-meta` [0.1.1]

Section titled “llama-index-llms-meta [0.1.1]”

  * Support Meta Llama-api as an LLM provider (#18585)

### `llama-index-node-parser-docling` [0.3.2]

Section titled “llama-index-node-parser-docling [0.3.2]”

  * Fix/docling node parser metadata (#186390)

### `llama-index-node-parser-slide` [0.1.0]

Section titled “llama-index-node-parser-slide [0.1.0]”

  * add SlideNodeParser integration (#18620)

### `llama-index-readers-github` [0.6.1]

Section titled “llama-index-readers-github [0.6.1]”

  * Fix: Add follow_redirects=True to GitHubIssuesClient (#18630)

### `llama-index-readers-markitdown` [0.1.1]

Section titled “llama-index-readers-markitdown [0.1.1]”

  * Fix MarkItDown Reader bugs (#18613)

### `llama-index-readers-oxylabs` [0.1.2]

Section titled “llama-index-readers-oxylabs [0.1.2]”

  * Add Oxylabs readers (#18555)

### `llama-index-readers-web` [0.4.1]

Section titled “llama-index-readers-web [0.4.1]”

  * Fixes improper invocation of Firecrawl library (#18646)
  * Add Oxylabs readers (#18555)

### `llama-index-storage-chat-store-gel` [0.1.0]

Section titled “llama-index-storage-chat-store-gel [0.1.0]”

  * Add Gel integrations (#18503)

### `llama-index-storage-docstore-gel` [0.1.0]

Section titled “llama-index-storage-docstore-gel [0.1.0]”

  * Add Gel integrations (#18503)

### `llama-index-storage-kvstore-gel` [0.1.0]

Section titled “llama-index-storage-kvstore-gel [0.1.0]”

  * Add Gel integrations (#18503)

### `llama-index-storage-index-store-gel` [0.1.0]

Section titled “llama-index-storage-index-store-gel [0.1.0]”

  * Add Gel integrations (#18503)

### `llama-index-utils-workflow` [0.3.2]

Section titled “llama-index-utils-workflow [0.3.2]”

  * Fix event colors of draw_all_possible_flows (#18660)

### `llama-index-vector-stores-faiss` [0.4.0]

Section titled “llama-index-vector-stores-faiss [0.4.0]”

  * Add Faiss Map Vector store and fix missing index_struct delete (#18638)

### `llama-index-vector-stores-gel` [0.1.0]

Section titled “llama-index-vector-stores-gel [0.1.0]”

  * Add Gel integrations (#18503)

### `llama-index-vector-stores-postgres` [0.5.2]

Section titled “llama-index-vector-stores-postgres [0.5.2]”

  * add indexed metadata fields (#18595)

## [2025-04-30]

Section titled “[2025-04-30]”

  * Migrate repo from poetry to uv (#18524)

### `llama-index-core` [0.12.34]

Section titled “llama-index-core [0.12.34]”

  * fix: `aextract_table_summaries` cause unwanted output when showprogress is False (#18528)

### `llama-index-embeddings-cohere` [0.4.1]

Section titled “llama-index-embeddings-cohere [0.4.1]”

  * Fix Cohere Embedding Multiprocessing with Custom Endpoint (#18551)

### `llama-index-embeddings-openvino-genai` [0.5.0]

Section titled “llama-index-embeddings-openvino-genai [0.5.0]”

  * add openvino genai embedding (#18569)

### `llama-index-llms-bedrock-converse` [0.5.0]

Section titled “llama-index-llms-bedrock-converse [0.5.0]”

  * Add support for AWS Bedrock Application Inference Profiles (#18549)

### `llama-index-llms-google-genai` [0.1.10]

Section titled “llama-index-llms-google-genai [0.1.10]”

  * 2.5-flash-preview tests + structured predict changes/fixes (#18575)
  * unlock pillow dep in google genai llm (#18533)
  * merge tool messages properly (#18527)

### `llama-index-llms-huggingface-api` [0.4.2]

Section titled “llama-index-llms-huggingface-api [0.4.2]”

  * Add provider support to HuggingFaceInferenceAPI (#18574)

### `llama-index-llms-vllm` [0.5.1]

Section titled “llama-index-llms-vllm [0.5.1]”

  * feat: add is_chat_model option (#18552)

### `llama-index-packs-code-hierarchy` [0.5.1]

Section titled “llama-index-packs-code-hierarchy [0.5.1]”

  * Code Hierarchy Agent Pack Issue with Empty and different encoding based files (#18538)

### `llama-index-postprocessor-cohere-rerank` [0.4.0]

Section titled “llama-index-postprocessor-cohere-rerank [0.4.0]”

  * update default model version to v3.0 in CohereRerank (#18579)

### `llama-index-readers-database` [0.4.0]

Section titled “llama-index-readers-database [0.4.0]”

  * Enhance DatabaseReader with new features and improved documentation (#18537)

### `llama-index-tools-mcp` [0.1.2]

Section titled “llama-index-tools-mcp [0.1.2]”

  * Prevent MCP Connections Hang (#18512)

### `llama-index-vector-stores-opensearch` [0.5.3]

Section titled “llama-index-vector-stores-opensearch [0.5.3]”

  * Add OpensearchVectorClient to conditionally check index existence for AOSS (#18560)

### `llama-index-vector-stores-postgres` [0.5.1]

Section titled “llama-index-vector-stores-postgres [0.5.1]”

  * Implement aget_nodes and adelete in PGVectorStore (#18515)
  * Allow PGVectorStore to allow passing in engines (#18507)

## [2025-04-23]

Section titled “[2025-04-23]”

### `llama-index-core` [0.12.33 / 0.12.33.post1]

Section titled “llama-index-core [0.12.33 / 0.12.33.post1]”

  * bundle newer tiktoken encodings, bump min tiktoken version (#18509)

### `llama-index-vector-stores-milvus` [0.8.1]

Section titled “llama-index-vector-stores-milvus [0.8.1]”

  * Milvus Vector Store: Update metadata filtering demo (#18502)

## [2025-04-21]

Section titled “[2025-04-21]”

### `llama-index-core` [0.12.32]

Section titled “llama-index-core [0.12.32]”

  * Fix media resource serialization (#18496)
  * fix react agent prompt updates (#18494)

### `llama-index-indices-managed-vectara` [0.4.4]

Section titled “llama-index-indices-managed-vectara [0.4.4]”

  * Close “session” in VectaraIndex on GC (#18484)

### `llama-index-llms-openai` [0.3.38]

Section titled “llama-index-llms-openai [0.3.38]”

  * allow content blocks in openai assistant messages (#18495)

### `llama-index-llms-openvino-genai` [0.1.1]

Section titled “llama-index-llms-openvino-genai [0.1.1]”

  * fix the openvino llm initialize issue (#18481)

### `llama-index-vector-stores-milvus` [0.8.0]

Section titled “llama-index-vector-stores-milvus [0.8.0]”

  * MilvusVectorStore: BM25 as default sparse embedding function (#18460)

## [2025-04-16]

Section titled “[2025-04-16]”

### `llama-index-core` [0.12.31]

Section titled “llama-index-core [0.12.31]”

  * Fix/memory multimodal content serialization (#18447)
  * add async to memory and postprocessor base classes (#18438)

### `llama-index-callbacks-arize-pheonix` [0.5.1]

Section titled “llama-index-callbacks-arize-pheonix [0.5.1]”

  * llama index callbacks arize phoenix python version bump (#18466)

### `llama-index-graph-stores-nebula` [0.4.2]

Section titled “llama-index-graph-stores-nebula [0.4.2]”

  * fix nebula index ddl (#18461)

### `llama-index-indices-managed-vectara` [0.4.3]

Section titled “llama-index-indices-managed-vectara [0.4.3]”

  * Added `llm_name` argument for Vectara (#18472)

### `llama-index-llms-cohere` [0.4.1]

Section titled “llama-index-llms-cohere [0.4.1]”

  * expand cohere model support (#18440)

### `llama-index-llms-llama-api` [0.4.0]

Section titled “llama-index-llms-llama-api [0.4.0]”

  * Fix LlamaAPI integration by wrapping OpenAI (#18437)

### `llama-index-llms-perplexity` [0.3.3]

Section titled “llama-index-llms-perplexity [0.3.3]”

  * Update Perplexity Implementation for new models (#18442)

### `llama-index-llms-openai` [0.3.37]

Section titled “llama-index-llms-openai [0.3.37]”

  * Added model names for OpenAI 4.1 support (#18456)
  * o3 and o4-mini support (#18473)
  * Don’t create a sync openai client when using async methods with Azure (#18471)

### `llama-index-storage-chat-store-sqlite` [0.1.0]

Section titled “llama-index-storage-chat-store-sqlite [0.1.0]”

  * Feat add sqlite chat store (#18432)

### `llama-index-vector-stores-ApertureDB` [0.0.1]

Section titled “llama-index-vector-stores-ApertureDB [0.0.1]”

  * Add ApertureDB vector store (#18428)

### `llama-index-vector-stores-elasticsearch` [0.4.3]

Section titled “llama-index-vector-stores-elasticsearch [0.4.3]”

  * implement missing BasePydanticVectorStore methods (#18454)

## [2025-04-10]

Section titled “[2025-04-10]”

### `llama-index-core` [0.12.30]

Section titled “llama-index-core [0.12.30]”

  * Fix multi-agent state formatting (#18417)
  * use to_thread for async reader methods by default (#18418)

### `llama-index-callbacks-arize-pheonix` [0.5.0]

Section titled “llama-index-callbacks-arize-pheonix [0.5.0]”

  * Connect new phoenix tracing option for separate context (#18415)

### `llama-index-graph-stores-nebula` [0.4.1]

Section titled “llama-index-graph-stores-nebula [0.4.1]”

  * fix nebula properties get (#18423)

### `llama-index-llms-openai` [0.3.33]

Section titled “llama-index-llms-openai [0.3.33]”

  * Actually fix pass-by-reference errors in OpenAIResponses (#18420)

## [2024-04-08]

Section titled “[2024-04-08]”

### `llama-index-core` [0.12.29]

Section titled “llama-index-core [0.12.29]”

  * better enforce agent handoffs in AgentWorkflow (#18399)
  * waiting for events refactor to handle multiple `wait_for_event` calls (#18226)
  * fix: 🐛 Replace broken and discontinued `tree_sitter_languages` with `tree_sitter_language_pack` (#18387)
  * Fix the costly pop(0) in SentenceSplitter when parsing numerous texts (#18359)

### `llama-index-embeddings-huggingface` [0.5.3]

Section titled “llama-index-embeddings-huggingface [0.5.3]”

  * add option to toggle progress bars in HuggingFaceEmbedding (#18404)

### `llama-index-embeddings-openai-like` [0.1.0]

Section titled “llama-index-embeddings-openai-like [0.1.0]”

  * Add OpenAILikeEmbedding, update docs (#18364)

### `llama-index-llms-bedrock-converse` [0.4.15]

Section titled “llama-index-llms-bedrock-converse [0.4.15]”

  * feature: add multi-modal support for bedrock converse (#18373)
  * support bedrock converse deepseek r1 (#18371)

### `llama-index-llms-ibm` [0.3.4]

Section titled “llama-index-llms-ibm [0.3.4]”

  * cache watsonx context window (#18350)

### `llama-index-llms-openai` [0.3.31]

Section titled “llama-index-llms-openai [0.3.31]”

  * fix openai json decode error (#18352)
  * enable openai responses override (#18402)

### `llama-index-llms-vertex` [0.4.6]

Section titled “llama-index-llms-vertex [0.4.6]”

  * Add ImageBlock and TextBlock support for Gemini models (#18344)

### `llama-index-graph-stores-kuzu` [0.7.0]

Section titled “llama-index-graph-stores-kuzu [0.7.0]”

  * Update to Kuzu 0.9.0 (#18382)

### `llama-index-indices-managed-llama-cloud` [0.6.11]

Section titled “llama-index-indices-managed-llama-cloud [0.6.11]”

  * remove org id kwarg (#18355)

### `llama-index-readers-microsoft-sharepoint` [0.5.1]

Section titled “llama-index-readers-microsoft-sharepoint [0.5.1]”

  * Fix Sharepoint folder path encoding issue (#18357)

### `llama-index-readers-papers` [0.3.2]

Section titled “llama-index-readers-papers [0.3.2]”

  * fix: use defusexml instead of xml.etree (#18362)

### `llama-index-readers-stripe-docs` [0.3.1]

Section titled “llama-index-readers-stripe-docs [0.3.1]”

  * fix: use defusexml instead of xml.etree (#18362)

### `llama-index-readers-uniprot` [0.1.0]

Section titled “llama-index-readers-uniprot [0.1.0]”

  * Add uniprot reader (#18356)

### `llama-index-readers-web` [0.3.9]

Section titled “llama-index-readers-web [0.3.9]”

  * fix: use defusexml instead of xml.etree (#18362)

### `llama-index-retrievers-galaxia` [0.1.0]

Section titled “llama-index-retrievers-galaxia [0.1.0]”

  * Add GalaxiaRetriever (#18317)

### `llama-index-vector-stores-azureaisearch` [0.3.7]

Section titled “llama-index-vector-stores-azureaisearch [0.3.7]”

  * chore: add title and keywords to semantic config (#18354)

### `llama-index-vector-stores-lancedb` [0.3.2]

Section titled “llama-index-vector-stores-lancedb [0.3.2]”

  * fix overwrite vs append logic in LanceDB (#18405)

### `llama-index-utils-workflow` [0.3.1]

Section titled “llama-index-utils-workflow [0.3.1]”

  * Fix `draw_all_possible_flows` for custom StopEvents (#18347)

## [2025-04-01]

Section titled “[2025-04-01]”

### `llama-index-core` [0.12.28]

Section titled “llama-index-core [0.12.28]”

  * add a code act agent + docs + from-scratch guide (#18329)
  * fix template var mapping for `RichPromptTemplate`, add docs (#18309)
  * Support multi-modal agents in `AgentWorkflow` / `ReActAgent` / `FunctionAgent` / `CodeActAgent` (#18330)
  * fix include Node metadata in hash calculation in new node class (#18303)
  * Fix `Context._events_queue` when loaded from `Context.from_dict` (#18304)
  * docs: add Langfuse instrumentation (#18321)

### `llama-index-embeddings-fastembed` [0.3.1]

Section titled “llama-index-embeddings-fastembed [0.3.1]”

  * add providers kwarg (#18310)

### `llama-index-graph-stores-memgraph` [0.3.1]

Section titled “llama-index-graph-stores-memgraph [0.3.1]”

  * Update Memgraph integration to latest syntax (#18319)

### `llama-index-indices-managed-llama-cloud` [0.6.10]

Section titled “llama-index-indices-managed-llama-cloud [0.6.10]”

  * misc fixes in constructing client (#18323)

### `llama-index-llms-asi` [0.1.0]

Section titled “llama-index-llms-asi [0.1.0]”

  * add asi llm integration (#18292)

### `llama-index-llms-dashscope` [0.3.2]

Section titled “llama-index-llms-dashscope [0.3.2]”

  * Update DashScope integration with new tool handling and dependency version bump (#18311)

### `llama-index-llms-ipex-llm` [0.3.1]

Section titled “llama-index-llms-ipex-llm [0.3.1]”

  * fix IpexLLM constructor error (#18200)

### `llama-index-llms-litellm` [0.4.1]

Section titled “llama-index-llms-litellm [0.4.1]”

  * LiteLLM: better support tools streaming, and support multimodal inputs (#18314)

### `llama-index-readers-obsidian` [0.5.1]

Section titled “llama-index-readers-obsidian [0.5.1]”

  * fix: prevent path traversal from symlinks (#18320)

### `llama-index-readers-papers` [0.3.1]

Section titled “llama-index-readers-papers [0.3.1]”

  * fix: make filename hashing more robust (#18318)

### `llama-index-tools-mcp` [0.1.1]

Section titled “llama-index-tools-mcp [0.1.1]”

  * Fixed case when `json_type` is a list (multiple possible types) (#18306)

### `llama-index-vector-stores-clickhouse` [0.4.1]

Section titled “llama-index-vector-stores-clickhouse [0.4.1]”

  * fix: patch multiple sql-injection vulnerabilities (#18316)

### `llama-index-vector-stores-couchbase` [0.3.1]

Section titled “llama-index-vector-stores-couchbase [0.3.1]”

  * fix: patch multiple sql-injection vulnerabilities (#18316)

### `llama-index-vector-stores-deeplake` [0.3.3]

Section titled “llama-index-vector-stores-deeplake [0.3.3]”

  * fix: patch multiple sql-injection vulnerabilities (#18316)

### `llama-index-vector-stores-jaguar` [0.3.1]

Section titled “llama-index-vector-stores-jaguar [0.3.1]”

  * fix: patch multiple sql-injection vulnerabilities (#18316)

### `llama-index-vector-stores-lantern` [0.3.1]

Section titled “llama-index-vector-stores-lantern [0.3.1]”

  * fix: patch multiple sql-injection vulnerabilities (#18316)

### `llama-index-vector-stores-nile` [0.2.2]

Section titled “llama-index-vector-stores-nile [0.2.2]”

  * fix: patch multiple sql-injection vulnerabilities (#18316)

### `llama-index-vector-stores-milvus` [0.7.2]

Section titled “llama-index-vector-stores-milvus [0.7.2]”

  * [bugfix] Milvus create index when existed (#18315)
  * Add more unit tests for milvus vector store (#18331)

### `llama-index-vector-stores-oracledb` [0.2.1]

Section titled “llama-index-vector-stores-oracledb [0.2.1]”

  * fix: patch multiple sql-injection vulnerabilities (#18316)

### `llama-index-vector-stores-singlestoredb` [0.3.1]

Section titled “llama-index-vector-stores-singlestoredb [0.3.1]”

  * fix: patch multiple sql-injection vulnerabilities (#18316)

## [2025-03-28]

Section titled “[2025-03-28]”

### `llama-index-core` [0.12.27]

Section titled “llama-index-core [0.12.27]”

  * optimize initial imports by lazily importing and loading nltk data (#18289)
  * support postponed type hints in workflow step signatures (#18225)

### `llama-index-llms-litellm` [0.3.1]

Section titled “llama-index-llms-litellm [0.3.1]”

  * feat: added tool calling support for LiteLLM (#18235)

### `llama-index-llms-openai` [0.3.29]

Section titled “llama-index-llms-openai [0.3.29]”

  * Add `OpenAIResponses` class to support OpenAI’s responses API (#18300)
  * type safe structured predict in overridden methods (#18290)

### `llama-index-tools-dappier` [0.1.0]

Section titled “llama-index-tools-dappier [0.1.0]”

  * Add Dappier Real Time Search and AI Recommendations Tools (#18211)

### `llama-index-vector-stores-milvus` [0.7.1]

Section titled “llama-index-vector-stores-milvus [0.7.1]”

  * Milvus Vector Store: Support full-text search by BM25 (#18281)
  * Fix Milvus vector store to handle text field retrieval

## [2025-03-26]

Section titled “[2025-03-26]”

### `llama-index-core` [0.12.26]

Section titled “llama-index-core [0.12.26]”

  * simplify FunctionAgent/ReActAgent usage for single-agent workflows (#18227)
  * Introduce RichPromptTemplate for jinja-like templating (#18178)
  * add implementation for structured llm reranker (#18216)

### `llama-index-embeddings-azure-openai` [0.3.2]

Section titled “llama-index-embeddings-azure-openai [0.3.2]”

  * Fix `api_base` and `azure_deployment` mutually exclusive in `AzureOpenAIEmbedding` class (#18219)
  * Fix `api_base` parameter in `AzureOpenAIEmbedding` class (#18191)

### `llama-index-finetuning` [0.3.1]

Section titled “llama-index-finetuning [0.3.1]”

  * Update to SentenceTransformersFinetuneEngine to expose transformer checkpoint related arguments (#18194)

### `llama-index-llms-dashscope` [0.3.1]

Section titled “llama-index-llms-dashscope [0.3.1]”

  * add `astream_chat` and `astream_complete` for dashscope llm (#18196)

### `llama-index-llms-bedrock` [0.3.8]

Section titled “llama-index-llms-bedrock [0.3.8]”

  * deprecate older google and bedrock packages (#18210)
  * add Bedrock application inference profile support (#18213)
  * Fixed provider-resolution for foundation-model ARNs (#18283)

### `llama-index-llms-bedrock-converse` [0.4.12]

Section titled “llama-index-llms-bedrock-converse [0.4.12]”

  * Do not append None to chat history in bedrock converse (#18206)
  * Add new apac bedrock llms (#18045)
  * handle chat message as user msg in converse chat with tools (#18187)

### `llama-index-llms-gemini` [0.4.13]

Section titled “llama-index-llms-gemini [0.4.13]”

  * Ensure `stream_complete` accumulates text and sets delta (#18246)

### `llama-index-llms-google-genai` [0.1.6]

Section titled “llama-index-llms-google-genai [0.1.6]”

  * deprecate older google and bedrock packages (#18210)
  * fix google genai tool description (#18242)
  * fix: support anyof, optional and union in google-genai (#18231)

### `llama-index-llms-openai` [0.3.27]

Section titled “llama-index-llms-openai [0.3.27]”

  * add o1-pro support (#18207)
  * improve default image quality in openai llm (#18258)

### `llama-index-llms-text-generation-inference` [0.3.2]

Section titled “llama-index-llms-text-generation-inference [0.3.2]”

  * Fix `model_name` validation error in TextGenerationInference, its not requested from TGI endpoint and results in exception (#18234)

### `llama-index-llms-vertx` [0.4.4]

Section titled “llama-index-llms-vertx [0.4.4]”

  * deprecate older google and bedrock packages (#18210)
  * Vertex LLM does not handle FunctionCall tools (#18201)

### `llama-index-readers-file` [0.4.7]

Section titled “llama-index-readers-file [0.4.7]”

  * feat: improve data retrieval by adding headers with the columns for pandas excel reader (#18233)

### `llama-index-storage-chat-store-dynomodb` [0.3.1]

Section titled “llama-index-storage-chat-store-dynomodb [0.3.1]”

  * feat: Add TTL support for DynamoDB chat store (#18084)

### `llama-index-storage-chat-store-redis` [0.4.1]

Section titled “llama-index-storage-chat-store-redis [0.4.1]”

  * Fix Runtime Warning for Coroutine never awaited in Redis chat store (#18274)

### `llama-index-vector-stores-milvus` [0.6.1]

Section titled “llama-index-vector-stores-milvus [0.6.1]”

  * Escape single quotes in milvus filters (#18244)
  * Speed up Milvus async_add (#18243)

### `llama-index-vector-stores-qdrant` [0.6.0]

Section titled “llama-index-vector-stores-qdrant [0.6.0]”

  * update qdrant to always prefer named vectors (#18192)
  * bump qdrant version python deps (#18273)

## [2025-03-18]

Section titled “[2025-03-18]”

### `llama-index-core` [0.12.25]

Section titled “llama-index-core [0.12.25]”

  * Ensuring original text is preserved in CHUNKING_REGEX in splitters (#18054)
  * use SimpleDirectoryReader without llama-index-readers-file package (#18173)
  * Improved Annotations and Error Handling in utils.py and exec_utils.py (#18153)
  * Add `build_semantic_nodes_from_nodes` to SemanticDoubleMergingSplitterNodeParser (#18114)
  * fix: Optimize memory management of the Context object (#18170)
  * fix: allow streaming events from context after workflows ends (#18174)
  * feat: Add a clear method to the Context class (#18136)

### `llama-index-embeddins-clip` [0.4.0]

Section titled “llama-index-embeddins-clip [0.4.0]”

  * unpin ClipEmbedding deps (#18165)

### `llama-index-embeddings-netmind` [0.1.0]

Section titled “llama-index-embeddings-netmind [0.1.0]”

  * add netmind integrations (#18078)

### `llama-index-indices-managed-llama-cloud` [0.6.9]

Section titled “llama-index-indices-managed-llama-cloud [0.6.9]”

  * fix kwargs for LlamaCloudCompositeRetriever (#18141)

### `llama-index-llms-bedrock-converse` [0.4.10]

Section titled “llama-index-llms-bedrock-converse [0.4.10]”

  * Bug fix: Calling tools with no arguments (#18143)
  * add token counts to the chat and achat methods of BedrockConverse (#18148)

### `llama-index-llms-contextual` [0.0.1]

Section titled “llama-index-llms-contextual [0.0.1]”

  * fixes for contextual glm (#18145)

### `llama-index-llms-google-genai` [0.1.4]

Section titled “llama-index-llms-google-genai [0.1.4]”

  * genai image output (#18138)

### `llama-index-llms-langchain` [0.6.1]

Section titled “llama-index-llms-langchain [0.6.1]”

  * Replace deprecated predict with invoke in llama-index-llms-langchain (#18169)

### `llama-index-llms-netmind` [0.1.0]

Section titled “llama-index-llms-netmind [0.1.0]”

  * add netmind integrations (#18078)

### `llama-index-llms-novita` [0.1.0]

Section titled “llama-index-llms-novita [0.1.0]”

  * add NovitaAI llm class (#18134)

### `llama-index-postprocessor-aimon-rerank` [0.1.0]

Section titled “llama-index-postprocessor-aimon-rerank [0.1.0]”

  * AIMon reranker integration into LlamaIndex node postprocessors (#18087)

### `llama-index-readers-mongodb` [0.3.1]

Section titled “llama-index-readers-mongodb [0.3.1]”

  * feat(mongo reader): field_extractors (#18063)

### `llama-index-tools-vectara-query` [0.3.1]

Section titled “llama-index-tools-vectara-query [0.3.1]”

  * Update Vectara Tool for Metadata Changes to VectaraIndex (#18126)

### `llama-index-vector-stores-azurecosmosnosql` [1.3.2]

Section titled “llama-index-vector-stores-azurecosmosnosql [1.3.2]”

  * Fix: AzureCosmosNoSQL vector_store; delete based on `ref_doc_id` (#18120)

### `llama-index-vector-stores-pinecone` [0.4.5]

Section titled “llama-index-vector-stores-pinecone [0.4.5]”

  * bump compatible pinecone version (#18113)

## [2025-03-13]

Section titled “[2025-03-13]”

### `llama-index-core` [0.12.24]

Section titled “llama-index-core [0.12.24]”

  * fix get content node metadata duplicated templates (#18110)
  * remove assert for multimodal llms in multimodal vector store/query engine (#18112)
  * fix: make run_step return all the events produced by a step (#18082)
  * fix(multimodal nodes): check image path is file before open (#18043)

### `llama-index-embeddings-google-genai` [0.1.0]

Section titled “llama-index-embeddings-google-genai [0.1.0]”

  * Google genai embeddings (#18079)

### `llama-index-graph-stores-neptune` [0.3.2]

Section titled “llama-index-graph-stores-neptune [0.3.2]”

  * Fix the TypeError in the upsert_triplet method of the Neptune (#18051)

### `llama-index-indices-managed-vectara` [0.4.2]

Section titled “llama-index-indices-managed-vectara [0.4.2]”

  * Update Vectara Index to return both document level and page level metadata (#17976)

### `llama-index-llms-contextual` [0.1.0]

Section titled “llama-index-llms-contextual [0.1.0]”

  * Contextual Generate model (#17913)

### `llama-index-llms-google-genai` [0.1.3]

Section titled “llama-index-llms-google-genai [0.1.3]”

  * Use GenAI package for google (#17939)
  * fix gemini roles (#18108)
  * fix null model meta references (#18109)
  * [BUG FIX] Google genai vertexai error (#18070)

### `llama-index-memory-mem0` [0.3.0]

Section titled “llama-index-memory-mem0 [0.3.0]”

  * Mem0Memory Integration Issue: Update Required for Mem0 API Parameter Changes (#18066)

### `llama-index-postprocessor-contextual-rerank` [0.1.0]

Section titled “llama-index-postprocessor-contextual-rerank [0.1.0]”

  * Contextual reranker (#18075)

### `llama-index-readers-elasticsearch` [0.3.1]

Section titled “llama-index-readers-elasticsearch [0.3.1]”

  * Fix the redundancy of ElasticsearchReader (#18106)

### `llama-index-readers-google` [0.6.1]

Section titled “llama-index-readers-google [0.6.1]”

  * Use int type for redirect URI port (#18097)

## [2025-03-07]

Section titled “[2025-03-07]”

### `llama-index-core` [0.12.23]

Section titled “llama-index-core [0.12.23]”

  * added `merging_separator` argument to allow for specifying chunk merge separator in semantic splitter (#18027)
  * Add support for running single-agent workflows within the BaseWorkflowAgent class (#18038)
  * Fix the error raised when ReactAgent is created without an explicit system message (#18041)
  * add a field keep_whitespaces to TokenTextSplitter (#17998)
  * do not convert raw tool output to string in AgentWorkflow (#18006)

### `llama-index-embeddings-ollama` [0.6.0]

Section titled “llama-index-embeddings-ollama [0.6.0]”

  * feat: add client_kwargs Parameter to OllamaEmbedding Class (#18012)

### `llama-index-llms-anthropic` [0.6.10]

Section titled “llama-index-llms-anthropic [0.6.10]”

  * anthropic caching and thinking updates (#18039)
  * allow caching of tool results (#18028)
  * support caching of anthropic system prompt (#18008)
  * Ensure resuming a workflow actually works (#18023)
  * [MarkdownNodeParser] Adding customizable header path separator char (#17964)
  * feat: return event instance from run() when stop event is custom (#18001)

### `llama-index-llms-azure-openai` [0.3.2]

Section titled “llama-index-llms-azure-openai [0.3.2]”

  * AzureOpenAI: api_base and azure_endpoint are mutually exclusive (#18037)
  * Add base_url to AzureOpenAI (#17996)

### `llama-index-llms-bedrock-converse` [0.4.8]

Section titled “llama-index-llms-bedrock-converse [0.4.8]”

  * message text is required in boto3 model (#17989)

### `llama-index-llms-ollama` [0.5.3]

Section titled “llama-index-llms-ollama [0.5.3]”

  * Make request_timeout in Ollama LLM optional (#18007)

### `llama-index-llms-mistralai` [0.4.0]

Section titled “llama-index-llms-mistralai [0.4.0]”

  * MistralAI support for multImodal content blocks (#17997)

### `llama-index-readers-file` [0.4.6]

Section titled “llama-index-readers-file [0.4.6]”

  * Bugfix: Use `torch.no grad()` in inference in ImageVisionLLMReader when PyTorch is installed (#17970)

### `llama-index-storage-chat-store-mongo` [0.1.0]

Section titled “llama-index-storage-chat-store-mongo [0.1.0]”

  * Feat/mongo chat store (#17979)

### `llama-index-core` [0.12.23]

Section titled “llama-index-core [0.12.23]”

  * added `merging_separator` argument to allow for specifying chunk merge separator in semantic splitter (#18027)
  * Add support for running single-agent workflows within the BaseWorkflowAgent class (#18038)
  * Fix the error raised when ReactAgent is created without an explicit system message (#18041)
  * add a field keep_whitespaces to TokenTextSplitter (#17998)

## [2025-02-28]

Section titled “[2025-02-28]”

### `llama-index-core` [0.12.22]

Section titled “llama-index-core [0.12.22]”

  * fix agentworkflow tool call tracking on final response (#17968)

### `llama-index-readers-github` [0.6.0]

Section titled “llama-index-readers-github [0.6.0]”

  * Ensure that Github reader uses timeout and retries params (#17959)

### `llama-index-readers-web` [0.3.7]

Section titled “llama-index-readers-web [0.3.7]”

  * chore: update FireCrawlWebReader integration to support extract (#17957)

## [2025-02-27]

Section titled “[2025-02-27]”

### `llama-index-core` [0.12.21]

Section titled “llama-index-core [0.12.21]”

  * fix: remove warnings from workflow tests (#17943)
  * fix: take step workers into account when running a workflow step-wise (#17942)
  * feat: auto-detect custom start and stop events in workflow classes (#17865)
  * Feature/remove retriever tool template override (#17909)
  * only modify delta if ‘Answer:’ was actually detected (#17901)
  * Fix CitationQueryEngine init function for response_synthesizer (#17897)
  * fix ChatSummaryMemoryBuffer._summarize_oldest_chat_history (#17845)
  * fix: make base64 detection more robust across the board (#17930)
  * fix: stepwise execution breaks when steps do async work (#17914)
  * safer workflow cancel + fix restored context bug (#17938)

### `llama-index-cli` [0.4.1]

Section titled “llama-index-cli [0.4.1]”

  * fix: escape user input before shelling out command (#17953)
  * llamaindex-cli to handle glob patterns correctly (#17904)

### `llama-index-embeddings-gaudi` [0.2.1]

Section titled “llama-index-embeddings-gaudi [0.2.1]”

  * fix: Remove cache_dir Pydantic field validation (#17947)

### `llama-index-indices-managed-vectara` [0.4.1]

Section titled “llama-index-indices-managed-vectara [0.4.1]”

  * Support for custom vectara_base_url (#17934)

### `llama-index-llms-anthropic` [0.6.7]

Section titled “llama-index-llms-anthropic [0.6.7]”

  * fix: tools param cannot be Null when calling Anthropic Messages API (#17928)

### `llama-index-llms-bedrock` [0.3.4]

Section titled “llama-index-llms-bedrock [0.3.4]”

  * feat(bedrock): add Claude 3.7 Sonnet model support (#17950)

### `llama-index-llms-bedrock-converse` [0.4.7]

Section titled “llama-index-llms-bedrock-converse [0.4.7]”

  * feat(bedrock converse): add Meta Llama 3.3 70B instruct model support (#17915)

### `llama-index-llms-gemini` [0.4.11]

Section titled “llama-index-llms-gemini [0.4.11]”

  * feat: change maximum allowed model temperature to 2.0 for Gemini (#17886)

### `llama-index-llms-ibm` [0.3.3]

Section titled “llama-index-llms-ibm [0.3.3]”

  * Update WatsonxLLM.metadata property to avoid validation error when model_limits field isn’t present (#17839)

### `llama-index-llms-openai` [0.3.24]

Section titled “llama-index-llms-openai [0.3.24]”

  * add gpt-4.5-preview (#17954)
  * fix: openai-like openai agent streaming over vLLM (#17927)
  * Fix “Invalid value for ‘content’: expected a string, got null.” openai error in case of empty assistant messages (#17921)

### `llama-index-multi-modal-llms-azure-openai` [0.4.0]

Section titled “llama-index-multi-modal-llms-azure-openai [0.4.0]”

  * Refactored to be a light wrapper on top of the normal AzureOpenAI llm (which also supports images using content blocks) to prevent code duplication (#17951)

### `llama-index-multi-modal-llms-huggingface` [0.4.2]

Section titled “llama-index-multi-modal-llms-huggingface [0.4.2]”

  * Support text-only prompts for LlamaMultiModal class (#17855)

### `llama-index-multi-modal-llms-openai` [0.5.0]

Section titled “llama-index-multi-modal-llms-openai [0.5.0]”

  * Refactored to be a light wrapper on top of the normal OpenAI llm (which also supports images using content blocks) to prevent code duplication (#17951)

### `llama-index-postprocessor-ibm` [0.1.0]

Section titled “llama-index-postprocessor-ibm [0.1.0]”

  * feat: Add ibm-watsonx-ai rerank integration (#17900)

### `llama-index-readers-web` [0.3.6]

Section titled “llama-index-readers-web [0.3.6]”

  * fix: respect max_depth in KnowledgeBaseWebReader (#17949)

### `llama-index-retrievers-tldw` [0.0.1]

Section titled “llama-index-retrievers-tldw [0.0.1]”

  * tl;dw AI Integration for Retrievers (#17872)

### `llama-index-tools-valyu` [0.1.0]

Section titled “llama-index-tools-valyu [0.1.0]”

  * feat: Add Valyu Integration (#17892)

### `llama-index-vector-stores-azureaisearch` [0.3.6]

Section titled “llama-index-vector-stores-azureaisearch [0.3.6]”

  * azureaisearch: add default mySemanticConfig as name when creating index (#17908)

### `llama-index-vector-stores-databricks` [0.4.0]

Section titled “llama-index-vector-stores-databricks [0.4.0]”

  * build: support python3=3.9,<4.0 for llama-index-vector-stores-databricks (#17937)

### `llama-index-vector-stores-duckdb` [0.3.1]

Section titled “llama-index-vector-stores-duckdb [0.3.1]”

  * fix: escape params in SQL queries in DuckDB vector store (#17952)

### `llama-index-vector-stores-elasticsearch` [0.4.2]

Section titled “llama-index-vector-stores-elasticsearch [0.4.2]”

  * fix: fix adelete method and add delete_nodes to elasticsearch vector store (#17890)

## [2025-02-25]

Section titled “[2025-02-25]”

### `llama-index-core` [0.12.20]

Section titled “llama-index-core [0.12.20]”

  * feat: Attach more metadata to retrieved image node (#17868)
  * fix: FunctionAgent and ReActAgent error out when LLM response contains no chat messages (#17884)
  * fix: Convert Embedding Functions to Async (#17888)

### `llama-index-networks` [0.6.0]

Section titled “llama-index-networks [0.6.0]”

  * fix: Bump python-jose version (#17866)

### `llama-index-vector-stores-redis` [0.5.0]

Section titled “llama-index-vector-stores-redis [0.5.0]”

  * fix: Update for redisvl 0.4.0 (#17902)

### `llama-index-llms-anthropic` [0.6.6]

Section titled “llama-index-llms-anthropic [0.6.6]”

  * fix: Add support for Claude 3.7-family models (#17905)

### `llama-index-readers-microsoft-outlook-emails` [0.1.1]

Section titled “llama-index-readers-microsoft-outlook-emails [0.1.1]”

  * fix: Import path was incorrect for microsoft_outlook_emails integration (#17867)

### `llama-index-llms-vertex` [0.4.3]

Section titled “llama-index-llms-vertex [0.4.3]”

  * fix: Chat messages with tool calls incorrectly mapping to Vertex message (#17893)

### `llama-index-llms-bedrock-converse` [0.4.6]

Section titled “llama-index-llms-bedrock-converse [0.4.6]”

  * feat: add Claude 3.7 Sonnet model support (#17911)

## [2025-02-17]

Section titled “[2025-02-17]”

### `llama-index-core` [0.12.19]

Section titled “llama-index-core [0.12.19]”

  * Added sync/async Function tool callback (#16637)
  * Tweaked regex for template vars

### `llama-index-experimental` [0.5.4]

Section titled “llama-index-experimental [0.5.4]”

  * Experimental natural language retrievers using duck db (#15642)

### `llama-index-graph-stores-memgraph` [0.3.0]

Section titled “llama-index-graph-stores-memgraph [0.3.0]”

  * fix version on memgraph (#17842)

### `llama-index-indices-managed-llama-cloud` [0.6.7]

Section titled “llama-index-indices-managed-llama-cloud [0.6.7]”

  * Image Metadata Test + Sync Implementation (#17844)

### `llama-index-postprocessor-nvidia-rerank` [0.4.2]

Section titled “llama-index-postprocessor-nvidia-rerank [0.4.2]”

  * NVIDIARerank add http_client parameter to pass custom clients (#17832)

### `llama-index-llms-mistralai` [0.3.3]

Section titled “llama-index-llms-mistralai [0.3.3]”

  * mistral saba support (#17847)

## [2025-02-16]

Section titled “[2025-02-16]”

### `llama-index-core` [0.12.18]

Section titled “llama-index-core [0.12.18]”

  * improve prompt helper multimodal support (#17831)
  * Retain return type from `@dispatcher.span` (#17817)
  * Silence nltk downloader (#17816)
  * Keep a reference to asyncio tasks in `astream_chat()` (#17812)

### `llama-index-indices-managed-llama-cloud` [0.6.6]

Section titled “llama-index-indices-managed-llama-cloud [0.6.6]”

  * include file & page metadata when returning image node from llamacloud retriever (#17823)
  * Improve error logs for llamacloud indices (#17827)

### `llama-index-indices-managed-vertexai` [0.2.1]

Section titled “llama-index-indices-managed-vertexai [0.2.1]”

  * Add textnode metadata (#17814)

### `llama-index-llms-anthropic` [0.6.5]

Section titled “llama-index-llms-anthropic [0.6.5]”

  * feat: ✨ add support to anthropic claude-3-5-haiku-latest model name (#17818)

### `llama-index-llms-openai` [0.3.20]

Section titled “llama-index-llms-openai [0.3.20]”

  * openai developer message fix for older o1 models (#17833)

### `llama-index-readers-microsoft-outlook-emails` [0.1.0]

Section titled “llama-index-readers-microsoft-outlook-emails [0.1.0]”

  * feat: add Microsoft Outlook Email Reader integration (#17829)

### `llama-index-tools-mcp` [0.1.0]

Section titled “llama-index-tools-mcp [0.1.0]”

  * feat: add mcp tool spec (#17795)

### `llama-index-tools-playwright` [0.1.1]

Section titled “llama-index-tools-playwright [0.1.1]”

  * Fix: Change Playwright browser tool from sync to async (#17808)

### `llama-index-vector-stores-azureaisearch` [0.3.5]

Section titled “llama-index-vector-stores-azureaisearch [0.3.5]”

  * Expand AzureAISearchVectorStore filter options (#17811)
  * azureaisearch: prefer using hybrid_top_k over similarity_top_k for hybrid search (#17612)
  * azureaisearch: add default to None for semantic configuration name (#17807)

### `llama-index-vector-stores-mariadb` [0.3.1]

Section titled “llama-index-vector-stores-mariadb [0.3.1]”

  * MariaDB Vector Store Integration: Add tuning parameters and utility functions (#17791)

## [2025-02-11]

Section titled “[2025-02-11]”

### `llama-index-core` [0.12.17]

Section titled “llama-index-core [0.12.17]”

  * Added support for AudioBlocks in chat messages (OpenAI only for now) (#17780)
  * Fix: SimpleDirectoryReader metadata handles timezones inconsistently (#17724)

### `llama-index-agent-openai` [0.4.4]

Section titled “llama-index-agent-openai [0.4.4]”

  * added additional parameters in openai assistant agent (#17729)
  * Avoid async race conditions in `aput_messages` (#17754)

### `llama-index-embeddings-siliconflow` [0.2.1]

Section titled “llama-index-embeddings-siliconflow [0.2.1]”

  * Add retry logic to siliconflow llm and embeddings (#17771)

### `llama-index-graph-rag-cognee` [0.1.3]

Section titled “llama-index-graph-rag-cognee [0.1.3]”

  * Cognee integration version update (#17769)

### `llama-index-graph-stores-neptune` [0.3.1]

Section titled “llama-index-graph-stores-neptune [0.3.1]”

  * fix: update the upsert_triplet method in neptune integration (#17727)

### `llama-index-llms-gemini` [0.4.9]

Section titled “llama-index-llms-gemini [0.4.9]”

  * fix gemini tool choice (#17747)
  * fix gemini multi-turn tool calling (#17764)
  * chore: add tests for latest gemini structured gen (#17762)

### `llama-index-llms-ibm` [0.3.2]

Section titled “llama-index-llms-ibm [0.3.2]”

  * fix: Update `WatsonxLLM.stream_chat()` to adapt to upcoming `ibm-watsonx-ai 1.2.7` and avoid error. (#17772)

### `llama-index-llms-langchain` [0.6.0]

Section titled “llama-index-llms-langchain [0.6.0]”

  * Update the llama-index-llms-langchain to latest langchain API - removes the deprecation warning (#17770)

### `llama-index-llms-ollama` [0.5.2]

Section titled “llama-index-llms-ollama [0.5.2]”

  * Ollama Native Multimodal support with ImageBlocks (#17759)

### `llama-index-llms-openai` [0.3.19]

Section titled “llama-index-llms-openai [0.3.19]”

  * add audio support to openai (#17780)

### `llama-index-llms-openvino-genai` [0.1.0]

Section titled “llama-index-llms-openvino-genai [0.1.0]”

  * Add llama-index-llms-openvino-genai package (#17714)

### `llama-index-llms-siliconflow` [0.2.1]

Section titled “llama-index-llms-siliconflow [0.2.1]”

  * Add retry logic to siliconflow llm and embeddings (#17771)

### `llama-index-readers-whisper` [0.1.0]

Section titled “llama-index-readers-whisper [0.1.0]”

  * Add OpenAI Whisper Reader (#17778)

### `llama-index-retrievers-bm25` [0.5.2]

Section titled “llama-index-retrievers-bm25 [0.5.2]”

  * BM25Retriever: UnicodeError Handling and Encoding Flexibility Improvement (#17643)

### `llama-index-retrievers-kendra` [0.1.0]

Section titled “llama-index-retrievers-kendra [0.1.0]”

  * Add kendra retriever (#17760)

### `llama-index-tools-jira` [0.1.0]

Section titled “llama-index-tools-jira [0.1.0]”

  * Jira tools integration (#17763)

### `llama-index-tools-playwright` [0.1.0]

Section titled “llama-index-tools-playwright [0.1.0]”

  * feat: playwright browser tool (#17706)

### `llama-index-vector-stores-elasticsearch` [0.4.1]

Section titled “llama-index-vector-stores-elasticsearch [0.4.1]”

  * missed keyword suffix for delete query (#17750)

## [2025-01-05]

Section titled “[2025-01-05]”

### `llama-index-core` [0.12.16]

Section titled “llama-index-core [0.12.16]”

  * Be more lenient with leading whitespaces emitted by some models when doing ReAct (#17701)
  * Fix `user_msg` vs `chat_history` AgentWorkflow inputs (#17690)

### `llama-index-embeddings-oci-data-science` [0.1.0]

Section titled “llama-index-embeddings-oci-data-science [0.1.0]”

  * Add OCI Data Science Model Deployment Embedding Integration (#17243)

### `llama-index-embeddings-vllm` [0.1.0]

Section titled “llama-index-embeddings-vllm [0.1.0]”

  * Add vLLM offline inference supports for embedding (#17675)

### `llama-index-embeddings-voyageai` [0.3.5]

Section titled “llama-index-embeddings-voyageai [0.3.5]”

  * small async voyageai fix (#17698)

### `llama-index-llms-gemini` [0.4.7]

Section titled “llama-index-llms-gemini [0.4.7]”

  * gemini 2.0 support (#17720)
  * feat: support basic function call for gemini (google-generativeai) (#17696)

### `llama-index-llms-oci-data-science` [0.1.0]

Section titled “llama-index-llms-oci-data-science [0.1.0]”

  * Add OCI Data Science Model Deployment LLM Integration (#17241)

### `llama-index-llms-oci-genai` [0.3.1]

Section titled “llama-index-llms-oci-genai [0.3.1]”

  * Option to pass auth_file_location, in-order to overwrite default config file location i.e. ~/.oci/config (#17695)

### `llama-index-llms-ollama` [0.5.1]

Section titled “llama-index-llms-ollama [0.5.1]”

  * fix: avoid missing tool calls while streaming

### `llama-index-llms-openai` [0.3.17]

Section titled “llama-index-llms-openai [0.3.17]”

  * fix: max_tokens in O1 (#17703)
  * o3 mini support (#17689)
  * fix max_tokens, add reasoning_effort for openai reasoning models (#17694)

### `llama-index-readers-obsidian` [0.5.0]

Section titled “llama-index-readers-obsidian [0.5.0]”

  * Improved Obsidian Reader (#17699)

### `llama-index-tools-scrapegraph` [0.1.1]

Section titled “llama-index-tools-scrapegraph [0.1.1]”

  * feat: add new scrapegraph endpoint (#17709)

## [2025-01-31]

Section titled “[2025-01-31]”

### `llama-index-core` [0.12.15]

Section titled “llama-index-core [0.12.15]”

  * Add error_on_tool_error param to FunctionCallingLLM.predict_and_call (#17663)
  * Get tool description from pydantic field (#17679)
  * fix: make ctx._events_buffer json-serializable (#17676)
  * feat: allow to exclude empty file simple directory reader (#17656)
  * improve markdown llm output parsing (#17577)
  * small typo fix in the default plan refine prompt (#17644)

### `llama-index-agent-openai` [0.4.3]

Section titled “llama-index-agent-openai [0.4.3]”

  * fix repeated sources when doing parallel tool calling (#17645)

### `llama-index-embeddings-text-embeddings-inference` [0.3.2]

Section titled “llama-index-embeddings-text-embeddings-inference [0.3.2]”

  * Add endpoint parameter to TextEmbeddingsInference (#17598)

### `llama-index-llms-bedrock-converse` [0.4.5]

Section titled “llama-index-llms-bedrock-converse [0.4.5]”

  * fix bedrock function calling (#17658)

### `llama-index-llms-cortex` [0.1.0]

Section titled “llama-index-llms-cortex [0.1.0]”

  * Add Snowflake Cortex Integration (#17585)

### `llama-index-llms-fireworks` [0.3.2]

Section titled “llama-index-llms-fireworks [0.3.2]”

  * Deepseek-r1 is now supported by fireworks (#17657)
  * Deepseek-v3 is now supported by fireworks (#17518)

### `llama-index-llms-gemini` [0.4.5]

Section titled “llama-index-llms-gemini [0.4.5]”

  * adding the chat decorators to async calls (#17678)

### `llama-index-llms-llama-cpp` [0.4.0]

Section titled “llama-index-llms-llama-cpp [0.4.0]”

  * update llama-cpp integration + docs (#17647)

### `llama-index-vector-stores-azureaisearch` [0.3.3]

Section titled “llama-index-vector-stores-azureaisearch [0.3.3]”

  * Feat/fix Azure AI Search Hybrid Semantic Search Unusability due to hardcoded parameter (#17683)

### `llama-index-vector-stores-pinecone` [0.4.4]

Section titled “llama-index-vector-stores-pinecone [0.4.4]”

  * `get_nodes()` now accepts include_values param to return embeddings (#17635)

## [2025-01-25]

Section titled “[2025-01-25]”

### `llama-index-core` [0.12.14]

Section titled “llama-index-core [0.12.14]”

  * Fix agentworkflow handoffs for non-openai llms (#17631)
  * small fixes to the multi-agent workflow demo notebook (#17628)

### `llama-index-embeddings-bedrock` [0.5.0]

Section titled “llama-index-embeddings-bedrock [0.5.0]”

  * Implement async bedrock embeddings (#17610)

### `llama-index-llms-bedrock-converse` [0.4.4]

Section titled “llama-index-llms-bedrock-converse [0.4.4]”

  * Fix prompt stacking in bedrock converse (#17613)

### `llama-index-llms-deepseek` [0.1.0]

Section titled “llama-index-llms-deepseek [0.1.0]”

  * DeepSeek official API LLM (#17625)

### `llama-index-readers-google` [0.6.0]

Section titled “llama-index-readers-google [0.6.0]”

  * GoogleDriveReader support file extensions (#17620)

## [2025-01-23]

Section titled “[2025-01-23]”

### `llama-index-core` [0.12.13]

Section titled “llama-index-core [0.12.13]”

  * Fixing header_path bug re: markdown level vs. stack depth in MarkdownNodeParser (#17602)
  * Advanced text to sql sample rows, adding row retrieval for few-shot prompts (#17479)
  * Made the message role of ReAct observation configurable (#17521)
  * fix reconstructing a tool in AgentWorkflow (#17596)
  * support content blocks in chat templates (#17603)
  * Add contextual retrieval support with a new `DocumentContextExtractor` (#17367)

### `llama-index-graph-stores-memgraph` [0.2.1]

Section titled “llama-index-graph-stores-memgraph [0.2.1]”

  * Vector index support for Memgraph’s integration (#17570)

### `llama-index-graph-stores-neo4j` [0.4.6]

Section titled “llama-index-graph-stores-neo4j [0.4.6]”

  * Improves connections for neo4j objects and adds some tests (#17562)

### `llama-index-indices-managed-llama-cloud` [0.6.4]

Section titled “llama-index-indices-managed-llama-cloud [0.6.4]”

  * Add framework integration for composite retrieval (#17536)

### `llama-index-llms-langchain` [0.5.1]

Section titled “llama-index-llms-langchain [0.5.1]”

  * get valid string when streaming (#17566)

### `llama-index-llms-mistralai` [0.3.2]

Section titled “llama-index-llms-mistralai [0.3.2]”

  * update function calling models in mistral (#17604)

### `llama-index-llms-openai` [0.3.14]

Section titled “llama-index-llms-openai [0.3.14]”

  * fix openai.BadRequestError: Invalid value for ‘content’: expected a string, got null for tool calls (#17556)

### `llama-index-readers-file` [0.4.3]

Section titled “llama-index-readers-file [0.4.3]”

  * Refactor markdown_to_tups method to better handle multi-level headers (#17508)

### `llama-index-readers-web` [0.3.5]

Section titled “llama-index-readers-web [0.3.5]”

  * feat: Agentql Web Loader (#17575)

### `llama-index-tools-linkup-research` [0.3.0]

Section titled “llama-index-tools-linkup-research [0.3.0]”

  * add linkup tool (#17541)

### `llama-index-tools-notion` [0.3.1]

Section titled “llama-index-tools-notion [0.3.1]”

  * fix: correct the input params of “load_data” in NotionPageReader (#17529)

### `llama-index-vector-stores-pinecone` [0.4.3]

Section titled “llama-index-vector-stores-pinecone [0.4.3]”

  * build: 🆙 replace pinecone-client with pinecone package (#17587)

### `llama-index-vector-stores-postgres` [0.4.2]

Section titled “llama-index-vector-stores-postgres [0.4.2]”

  * Add support for halfvec vector type (#17534)

## [2025-01-20]

Section titled “[2025-01-20]”

### `llama-index-core` [0.12.12]

Section titled “llama-index-core [0.12.12]”

  * feat: add AgentWorkflow system to support single and multi-agent workflows (#17237)
  * Fix image-path validation in ImageNode (#17558)

### `llama-index-indices-managed-vectara` [0.4.0]

Section titled “llama-index-indices-managed-vectara [0.4.0]”

  * (breaking change) API Migration (#17545)

### `llama-index-llms-anthropic` [0.6.4]

Section titled “llama-index-llms-anthropic [0.6.4]”

  * feat: support direct PDF handling for Anthropic (#17506)

### `llama-index-llms-fireworks` [0.3.1]

Section titled “llama-index-llms-fireworks [0.3.1]”

  * Deepseek-v3 is now supported by fireworks (#17518)

### `llama-index-llms-stepfun` [1.0.0]

Section titled “llama-index-llms-stepfun [1.0.0]”

  * feat: add stepfun integrations (#17514)

### `llama-index-multi-modal-llms-gemini` [0.5.0]

Section titled “llama-index-multi-modal-llms-gemini [0.5.0]”

  * refact: make GeminiMultiModal a thin wrapper around Gemini (#17501)

### `llama-index-postprocessor-longllmlingua` [0.4.0]

Section titled “llama-index-postprocessor-longllmlingua [0.4.0]”

  * Add longllmlingua2 integration (#17531)

### `llama-index-readers-web` [0.3.4]

Section titled “llama-index-readers-web [0.3.4]”

  * feat: Hyperbrowser Web Reader (#17489)

## [2025-01-15]

Section titled “[2025-01-15]”

### `llama-index-core` [0.12.11]

Section titled “llama-index-core [0.12.11]”

  * fix: bug in MediaResource validator (#17509)
  * handle pandas errors in md to df in MarkdownElementNodeParser (#17511)
  * bugfix: Duplicated citation nodes (#17440)
  * Fixed issue #17397 by updating the markdown format in MarkdownReader (#17429)
  * feat: support adding images to ChatMessage through additional_kwargs (#17477)
  * feat: async semantic splitter noder parser (#17449)
  * more exception handling in schema llm extractor (#17432)

### `llama-index-agent-openai` [0.4.2]

Section titled “llama-index-agent-openai [0.4.2]”

  * Async memory management for OpenAIAgentWorker (#17375)

### `llama-index-embeddings-huggingface` [0.5.0]

Section titled “llama-index-embeddings-huggingface [0.5.0]”

  * multimodal huggingface embeddings support (#17463)

### `llama-index-embeddings-gemini` [0.3.1]

Section titled “llama-index-embeddings-gemini [0.3.1]”

  * add request options to gemini (#17452)

### `llama-index-embeddings-opea` [0.1.0]

Section titled “llama-index-embeddings-opea [0.1.0]”

  * Add support for OPEA LLMs in Llama-Index (#16666)

### `llama-index-embeddings-upstage` [0.4.1]

Section titled “llama-index-embeddings-upstage [0.4.1]”

  * bugfix: Fix upstage embedding available model mapping (#17460)

### `llama-index-graph-stores-neo4j` [0.4.5]

Section titled “llama-index-graph-stores-neo4j [0.4.5]”

  * Fix neo4j schema bug (#17448)

### `llama-index-llms-gemini` [0.4.3]

Section titled “llama-index-llms-gemini [0.4.3]”

  * add request options to gemini (#17452)

### `llama-index-llms-opea` [0.1.0]

Section titled “llama-index-llms-opea [0.1.0]”

  * Add support for OPEA LLMs in Llama-Index (#16666)

### `llama-index-llms-openai` [0.3.13]

Section titled “llama-index-llms-openai [0.3.13]”

  * adjust openai model temperature to accept values between 0 and 2 (#17453)

### `llama-index-multi-modal-llms-bedrock` [0.1.0]

Section titled “llama-index-multi-modal-llms-bedrock [0.1.0]”

  * Add Multi Modal Bedrock Integration (#17451)

### `llama-index-postprocessor-bedrock-rerank` [0.3.1]

Section titled “llama-index-postprocessor-bedrock-rerank [0.3.1]”

  * Change `top_n` if number of input nodes are less (#17374)

### `llama-index-readers-slack` [0.3.1]

Section titled “llama-index-readers-slack [0.3.1]”

  * Added support to allow only public slack channels (#17399)

### `llama-index-storage-chat-store-tablestore` [0.1.0]

Section titled “llama-index-storage-chat-store-tablestore [0.1.0]”

  * Tablestore Support ChatStore/KvStore/DocStore/IndexStore (#17473)

### `llama-index-storage-docstore-tablestore` [0.1.0]

Section titled “llama-index-storage-docstore-tablestore [0.1.0]”

  * Tablestore Support ChatStore/KvStore/DocStore/IndexStore (#17473)

### `llama-index-storage-index-store-tablestore` [0.1.0]

Section titled “llama-index-storage-index-store-tablestore [0.1.0]”

  * Tablestore Support ChatStore/KvStore/DocStore/IndexStore (#17473)

### `llama-index-storage-kvstore-tablestore` [0.1.0]

Section titled “llama-index-storage-kvstore-tablestore [0.1.0]”

  * Tablestore Support ChatStore/KvStore/DocStore/IndexStore (#17473)

### `llama-index-vector-stores-mariadb` [0.3.0]

Section titled “llama-index-vector-stores-mariadb [0.3.0]”

  * Support MariaDB 11.7 in the MariaDB vector store integration (#17497)

### `llama-index-vector-stores-neptune` [0.3.1]

Section titled “llama-index-vector-stores-neptune [0.3.1]”

  * add test, fix missing method (#17485)

### `llama-index-vector-stores-qdrant` [0.4.3]

Section titled “llama-index-vector-stores-qdrant [0.4.3]”

  * Add new operator for Qdrant Vector store (#17490)

## [2024-12-31]

Section titled “[2024-12-31]”

### `llama-index-core` [0.12.10]

Section titled “llama-index-core [0.12.10]”

  * remove asserts from schema llm extractor (#17425)
  * feat: support typing.Annotated for adding parameter descriptions in FunctionTools (#17411)
  * Guess image_mimetype for ImageNode (#17422)

### `llama-index-embeddings-nvidia` [0.3.1]

Section titled “llama-index-embeddings-nvidia [0.3.1]”

  * NVIDIA Support for v2 Embedding & Reranking NIMs #(17410)

### `llama-index-embeddings-openvino` [0.5.1]

Section titled “llama-index-embeddings-openvino [0.5.1]”

  * update deps of OpenVINO packages (#17419)

### `llama-index-multi-modal-llms-openai` [0.4.2]

Section titled “llama-index-multi-modal-llms-openai [0.4.2]”

  * Add support for gpt-4o-2024-08-06 to multi modal llms (#17405)

### `llama-index-packs-raptor` [0.3.1]

Section titled “llama-index-packs-raptor [0.3.1]”

  * Fix for llama_index.packs.raptor tree_traversal retrieval (#17406)

### `llama-index-postprocessor-openvino-rerank` [0.4.1]

Section titled “llama-index-postprocessor-openvino-rerank [0.4.1]”

  * update deps of OpenVINO packages (#17419)

### `llama-index-readers-file` [0.4.2]

Section titled “llama-index-readers-file [0.4.2]”

  * Remove MarkdownReader from the default loaders in SimpleDirectoryReader (#17412)

### `llama-index-core` [0.12.9]

Section titled “llama-index-core [0.12.9]”

  * clean up type hints in schema extractor (#17394)
  * Fix IndexError in LLM Reranking when handling malformed LLM responses (#17353)

### `llama-index-llms-bedrock-converse` [0.4.3]

Section titled “llama-index-llms-bedrock-converse [0.4.3]”

  * Fix Regression on Tools use for Bedrock Converse (#17364)

### `llama-index-llms-sagemaker-endpoint` [0.3.1]

Section titled “llama-index-llms-sagemaker-endpoint [0.3.1]”

  * Pass `aws_region_name` to `get_aws_service_client()` in SageMakerLLM (#12000)

### `llama-index-postprocessor-voyageai-rerank` [0.3.2]

Section titled “llama-index-postprocessor-voyageai-rerank [0.3.2]”

  * VoyageAIRerank constructor fix for truncation (#17343)

### `llama-index-readers-gitlab` [0.3.1]

Section titled “llama-index-readers-gitlab [0.3.1]”

  * Fix: Properly add blob documents from Gitlab Repo (#17392)

### `llama-index-readers-rss` [0.3.2]

Section titled “llama-index-readers-rss [0.3.2]”

  * Fix minor issues in rss (#17351)

### `llama-index-readers-web` [0.3.3]

Section titled “llama-index-readers-web [0.3.3]”

  * fix: prevent infinite recursion in `get_article_urls` (#17360)

### `llama-index-vector-stores-azureaisearch` [0.3.2]

Section titled “llama-index-vector-stores-azureaisearch [0.3.2]”

  * azureaisearch: add semantic search mode support for async queries (#17335)

### `llama-index-vector-stores-azurecosmosnosql` [1.3.1]

Section titled “llama-index-vector-stores-azurecosmosnosql [1.3.1]”

  * fix storeindex cosmosnosql query issue - (BadRequest) (#17385)

### `llama-index-vector-stores-milvus` [0.5.0]

Section titled “llama-index-vector-stores-milvus [0.5.0]”

  * feat: milvus async (#17378)

### `llama-index-vector-stores-opensearch` [0.5.2]

Section titled “llama-index-vector-stores-opensearch [0.5.2]”

  * Fix typo in property name (#17365)
  * bugfix when initializing with async aoss vector store (#17340)

### `llama-index-vector-stores-tablestore` [0.2.2]

Section titled “llama-index-vector-stores-tablestore [0.2.2]”

  * TablestoreVectorStore: support hybrid query, modify some documents. (#17366)
  * TablestoreVectorStore check the Dimension of the embedding when writing it to store. (#17321)

### `llama-index-vector-stores-qdrant` [0.4.2]

Section titled “llama-index-vector-stores-qdrant [0.4.2]”

  * qdrant filter fix for `query_str` is None (#17377)

### `llama-index-vector-stores-weaviate` [1.3.1]

Section titled “llama-index-vector-stores-weaviate [1.3.1]”

  * implement `client_kwargs["custom_batch"]` for weaviate (#17347)

## [2024-12-20]

Section titled “[2024-12-20]”

### `llama-index-core` [0.12.8]

Section titled “llama-index-core [0.12.8]”

  * Fix exclude text in document serialization (#17341)
  * Fix missing aput in awrite_response_to_history (#17338)

### `llama-index-graph-rag-cognee` [0.1.0]

Section titled “llama-index-graph-rag-cognee [0.1.0]”

  * Cognee integration (#17314)

### `llama-index-llms-openai` [0.3.12]

Section titled “llama-index-llms-openai [0.3.12]”

  * Tweak o1 function calling reqs (#17328)

## [2024-12-18]

Section titled “[2024-12-18]”

### `llama-index-core` [0.12.7]

Section titled “llama-index-core [0.12.7]”

  * fix: add a timeout to langchain callback handler (#17296)
  * fix: make Document serialization event more backward compatible (#17312)

### `llama-index-embeddings-voyageai` [0.3.4]

Section titled “llama-index-embeddings-voyageai [0.3.4]”

  * Exposing additional keyword arguments for VoyageAI’s embedding model (#17315)

### `llama-index-llms-keywordsai` [0.1.0]

Section titled “llama-index-llms-keywordsai [0.1.0]”

  * Added KeywordsAI LLM (#16860)

### `llama-index-llms-oci-genai` [0.4.0]

Section titled “llama-index-llms-oci-genai [0.4.0]”

  * Add OCI Generative AI tool calling support (#16888)

### `llama-index-llms-openai` [0.3.11]

Section titled “llama-index-llms-openai [0.3.11]”

  * support new o1 models (#17307)

### `llama-index-postprocessor-voyageai-rerank` [0.3.1]

Section titled “llama-index-postprocessor-voyageai-rerank [0.3.1]”

  * VoyageAI Reranker optional API Key (#17310)

### `llama-index-vector-stores-azureaisearch` [0.3.1]

Section titled “llama-index-vector-stores-azureaisearch [0.3.1]”

  * improve async search client handling (#17319)

### `llama-index-vector-stores-azurecosmosmongo` [0.4.0]

Section titled “llama-index-vector-stores-azurecosmosmongo [0.4.0]”

  * CosmosDB insertion timestamp bugfix (#17290)

### `llama-index-vector-stores-azurecosmosnosql` [1.3.0]

Section titled “llama-index-vector-stores-azurecosmosnosql [1.3.0]”

  * CosmosDB insertion timestamp bugfix (#17290)

## [2024-12-17]

Section titled “[2024-12-17]”

### `llama-index-core` [0.12.6]

Section titled “llama-index-core [0.12.6]”

  * [bug fix] Ensure that StopEvent gets cleared from Context._in_progress[“_done”] after a Workflow run (#17300)
  * fix: add a timeout to langchain callback handler (#17296)
  * tweak User vs tool in react prompts (#17273)
  * refact: Refactor Document to be natively multimodal (#17204)
  * fix: make ImageDocument derive from Document, backward compatible (#17259)
  * fix: accept already base64-encoded data in ImageBlock (#17244)
  * fix(metrics): fixed NDCG calculation and updated previous tests (#17236)
  * fix: remove llama-index-legacy dependency in llama-index-core (#17231)
  * Refined the default documentation generation for function tools (#17208)

### `llama-index-embeddings-voyageai` [0.3.3]

Section titled “llama-index-embeddings-voyageai [0.3.3]”

  * add support for voyageai >=0.3.0 (#17120)
  * Introducting VoyageAI’s new multimodal embeddings model (#17261)
  * VoyageAI multimodal embedding, correction (#17284)

### `llama-index-experimental` [0.5.2]

Section titled “llama-index-experimental [0.5.2]”

  * Fixed import errors for experimental JSONalyzeQueryEngine (#17228)

### `llama-index-grapg-stores-neo4j` [0.4.4]

Section titled “llama-index-grapg-stores-neo4j [0.4.4]”

  * Add cypher corrector and allow graph schema filtering (#17223)
  * Add timeout config to neo4j graph (#17267)
  * Add text and embedding type to neo4j enhanced schema (#17289)

### `llama-index-llms-anthropic` [0.6.3]

Section titled “llama-index-llms-anthropic [0.6.3]”

  * add content blocks to anthropic (#17274)
  * Do not send blank content to anthropic (#17278)
  * Update anthropic type imports for v0.41.0 release (#17299)
  * Fix Anthropic tokenizer protocol (fix by Devin) (#17201)

### `llama-index-llms-bedrock` [0.3.3]

Section titled “llama-index-llms-bedrock [0.3.3]”

  * Add Amazon bedrock guardrails (#17281)

### `llama-index-llms-bedrock-converse` [0.4.2]

Section titled “llama-index-llms-bedrock-converse [0.4.2]”

  * Add Amazon bedrock guardrails (#17281)

### `llama-index-llms-gemini` [0.4.1]

Section titled “llama-index-llms-gemini [0.4.1]”

  * Gemini 2.0 support (#17249)

### `llama-index-llms-mistralai` [0.3.1]

Section titled “llama-index-llms-mistralai [0.3.1]”

  * add tool call id/name to mistral chat messages (#17280)

### `llama-index-llms-nvidia` [0.3.1]

Section titled “llama-index-llms-nvidia [0.3.1]”

  * Adding llama 3.3-70b as function-calling-capable (#17253)

### `llama-index-llms-openai` [0.3.10]

Section titled “llama-index-llms-openai [0.3.10]”

  * fix openai message dicts for tool calls (#17254)

### `llama-index-llms-text-generation-inference` [0.3.1]

Section titled “llama-index-llms-text-generation-inference [0.3.1]”

  * Fix: TGI context window (#17252)

### `llama-index-multi-modal-llms-anthropic` [0.3.1]

Section titled “llama-index-multi-modal-llms-anthropic [0.3.1]”

  * handle more response types in anthropic multi modal llms (#17302)

### `llama-index-readers-confluence` [0.3.1]

Section titled “llama-index-readers-confluence [0.3.1]”

  * Support Confluence cookies (#17276)

### `llama-index-vector-stores-milvus` [0.4.0]

Section titled “llama-index-vector-stores-milvus [0.4.0]”

  * Parse “milvus_search_config” out of “vector_store_kwargs” (#17221)
  * refactor and optimize milvus code (#17229)

### `llama-index-vector-stores-pinecone` [0.4.2]

Section titled “llama-index-vector-stores-pinecone [0.4.2]”

  * Handle empty retrieved Pinecone index values (#17242)

### `llama-index-vector-stores-qdrant` [0.4.1]

Section titled “llama-index-vector-stores-qdrant [0.4.1]”

  * feat: Add NOT filter condition to MetadataFilter and QdrantVectorStore (#17270)

### `llama-index-vector-stores-weaviate` [1.3.0]

Section titled “llama-index-vector-stores-weaviate [1.3.0]”

  * Add async support to weaviate vector store integration (#17220)

## [2024-12-09]

Section titled “[2024-12-09]”

### `llama-index-core` [0.12.5]

Section titled “llama-index-core [0.12.5]”

  * Refined the default description generation for function tools (#17208)

### `llama-index-multi-modal-llms-azure-openai` [0.3.2]

Section titled “llama-index-multi-modal-llms-azure-openai [0.3.2]”

  * fix: relax pin on openai llm dependency (#17210)

### `llama-index-postprocessor-pinecone-native-rerank` [0.1.0]

Section titled “llama-index-postprocessor-pinecone-native-rerank [0.1.0]”

  * feat: integration on pinecone hosted rerankers (#17192)

### `llama-index-tools-scrapegraph` [0.1.0]

Section titled “llama-index-tools-scrapegraph [0.1.0]”

  * Add Scrapegraph tool integration (#17238)

### `llama-index-vector-stores-postgres` [0.3.3]

Section titled “llama-index-vector-stores-postgres [0.3.3]”

  * Update pgvector dependency to version 0.3.6 (#17195)

## [2024-12-08]

Section titled “[2024-12-08]”

### `llama-index-core` [0.12.4]

Section titled “llama-index-core [0.12.4]”

  * Fix sync and async structured streaming (#17194)
  * unpin pydantic to allow 2.8 or greater (#17193)
  * Update core structured predict streaming, add ollama structured predict (#17188)
  * bump tenacity dependency in llama-index-core (#17178)

### `llama-index-indices-managed-vectara` [0.3.1]

Section titled “llama-index-indices-managed-vectara [0.3.1]”

  * Add Verbose to Vectara `as_query_engine` (#17176)

### `llama-index-llms-ollama` [0.5.0]

Section titled “llama-index-llms-ollama [0.5.0]”

  * Update core structured predict streaming, add ollama structured predict (#17188)

### `llama-index-llms-perplexity` [0.3.2]

Section titled “llama-index-llms-perplexity [0.3.2]”

  * Fix message format for perplexity (#17182)

### `llama-index-readers-web` [0.3.1]

Section titled “llama-index-readers-web [0.3.1]”

  * Add possibility to use URI as doc id in WholeSiteReader (#17187)

### `llama-index-vector-stores-chroma` [0.4.1]

Section titled “llama-index-vector-stores-chroma [0.4.1]”

  * BUG FIX: llama-index-vectorstore-chromadb to work with chromadb v0.5.17 (#17184)

## [2024-12-06]

Section titled “[2024-12-06]”

### `llama-index-core` [0.12.3]

Section titled “llama-index-core [0.12.3]”

  * cover SimpleDirectoryReader with unit tests (#17156)
  * docs: rewrite openai image reasoning example without multimodal LLM (#17148)
  * fix(metrics): fixed NDCG calculation and added comprehensive test cases (#17126)
  * feat: improve ImageBlock (#17111)
  * Remove forgotten print in ChatMemoryBuffer (#17114)
  * [FIX] Move JSONalyzeQueryEngine to experimental (#17110)

### `llama-index-embeddings-clip` [0.3.1]

Section titled “llama-index-embeddings-clip [0.3.1]”

  * Unrestrict clip models to use (#17162)

### `llama-index-embeddings-openai` [0.3.1]

Section titled “llama-index-embeddings-openai [0.3.1]”

  * fix/openai-embbeding-retry (#17072)

### `llama-index-embeddings-text-embeddings-inference` [0.3.1]

Section titled “llama-index-embeddings-text-embeddings-inference [0.3.1]”

  * proper auth token in TEI (#17158)

### `llama-index-indices-managed-llama-cloud` [0.6.3]

Section titled “llama-index-indices-managed-llama-cloud [0.6.3]”

  * chore: fix httpx_client typo in LlamaCloudRetriever (#17101)
  * fix: wrong project id variable in LlamaCloudRetriever (#17086)

### `llama-index-llms-bedrock-converse` [0.4.1]

Section titled “llama-index-llms-bedrock-converse [0.4.1]”

  * Adding AWS Nova models to Bedrock Converse (#17139)

### `llama-index-llms-ollama` [0.4.2]

Section titled “llama-index-llms-ollama [0.4.2]”

  * Ollama LLM: Added TypeError exception to `_get_response_token_counts` (#17150)

### `llama-index-llms-sambanovasystems` [0.4.3]

Section titled “llama-index-llms-sambanovasystems [0.4.3]”

  * changes in openai identification in url (#17161)

### `llama-index-memory-mem0` [0.2.1]

Section titled “llama-index-memory-mem0 [0.2.1]”

  * Fix mem0 version check (#17159)

### `llama-index-multi-modal-llms-openai` [0.4.0]

Section titled “llama-index-multi-modal-llms-openai [0.4.0]”

  * fix: make OpenAIMultiModal work with new ChatMessage (#17138)

### `llama-index-postprocessor-bedrock-rerank` [0.3.0]

Section titled “llama-index-postprocessor-bedrock-rerank [0.3.0]”

  * Add AWS Bedrock Reranker (#17134)

### `llama-index-readers-file` [0.4.1]

Section titled “llama-index-readers-file [0.4.1]”

  * update doc id for unstructured reader (#17160)

### `llama-index-retrievers-duckdb-retriever` [0.4.0]

Section titled “llama-index-retrievers-duckdb-retriever [0.4.0]”

  * fix: use prepared statement in DuckDBRetriever (#17092)

### `llama-index-vector-stores-postgres` [0.3.2]

Section titled “llama-index-vector-stores-postgres [0.3.2]”

  * Create tables for pgvector regardless of schema status (#17100)

### `llama-index-vector-stores-weaviate` [1.2.4]

Section titled “llama-index-vector-stores-weaviate [1.2.4]”

  * make alpha not none in weaviate (#17163)
  * Make Weaviate Vector Store integration work with complex properties (#17129)
  * Add support for `IS_EMPTY` metadata filters to Weaviate Vector Store integration (#17128)
  * Make Weaviate Vector Store integration support nested metadata filtering (#17107)

## [2024-11-26]

Section titled “[2024-11-26]”

### `llama-index-core` [0.12.2]

Section titled “llama-index-core [0.12.2]”

  * improve traceback logging for workflows (#17040)
  * Initial version of checkpointing for Workflows (#17006)
  * Fix base component tests (#17062)
  * mark code splitter tests as optional (#17060)
  * update contributing guide and dev deps (#17051)
  * fix Handling of WorkflowDone exception (#17047)

### `llama-index-embeddings-vertex` [0.3.1]

Section titled “llama-index-embeddings-vertex [0.3.1]”

  * remove pyarrow from vertex deps (#16997)

### `llama-index-llms-ibm` [0.3.1]

Section titled “llama-index-llms-ibm [0.3.1]”

  * IBM watsonx.ai acomplete & achat integration (#17034)

### `llama-index-llms-openai` [0.3.2]

Section titled “llama-index-llms-openai [0.3.2]”

  * fixes tool_choice in certain scenarios for openai (#17058)

### `llama-index-llms-perplexity` [0.3.1]

Section titled “llama-index-llms-perplexity [0.3.1]”

  * Fix: update perplexity models, add unit tests and minor fixes (#17045)

### `llama-index-llms-vertex` [0.4.1]

Section titled “llama-index-llms-vertex [0.4.1]”

  * remove pyarrow from vertex deps (#16997)

### `llama-index-multi-modal-llms-huggingface` [0.2.1]

Section titled “llama-index-multi-modal-llms-huggingface [0.2.1]”

  * Add stream_chat and conditionally set AutoModelClass to MllamaForConditionalGeneration (#17031)

### `llama-index-readers-box` [0.3.1]

Section titled “llama-index-readers-box [0.3.1]”

  * Fix box api - mypy breakage (#17061)

### `llama-index-vector-stores-deeplake` [0.3.2]

Section titled “llama-index-vector-stores-deeplake [0.3.2]”

  * deeplake v3 backward compatibility (#17057)

### `llama-index-vector-stores-mongodb` [0.6.0]

Section titled “llama-index-vector-stores-mongodb [0.6.0]”

  * MongoDB Atlas: Adds search index commands and tests/examples of metadata filters (#15265)

### `llama-index-vector-stores-postgres` [0.3.1]

Section titled “llama-index-vector-stores-postgres [0.3.1]”

  * check if schema exists before doing rest of init during pgvector table creation (#17063)

## [2024-11-20]

Section titled “[2024-11-20]”

### `llama-index-core` [0.12.1]

Section titled “llama-index-core [0.12.1]”

  * Pin pydantic to `<2.10` temporarily
  * feat[react-multimodal]: add gemini support for images in MultimodalReActAgentWorker (#16992)

### `llama-index-indices-managed-llama-cloud` [0.6.2]

Section titled “llama-index-indices-managed-llama-cloud [0.6.2]”

  * api_key typo in llama-cloud-index (#17001)

### `llama-index-llms-openai` [0.3.1]

Section titled “llama-index-llms-openai [0.3.1]”

  * Add support for latest gpt-4o model (#17015)

### `llama-index-llms-zhipuai` [0.2.1]

Section titled “llama-index-llms-zhipuai [0.2.1]”

  * zhipuai add stop param to api (#16996)

### `llama-index-multi-modal-llms-mistralai` [0.3.1]

Section titled “llama-index-multi-modal-llms-mistralai [0.3.1]”

  * Add support for mistral latest models (#16991)

### `llama-index-multi-modal-llms-replicate` [0.3.1]

Section titled “llama-index-multi-modal-llms-replicate [0.3.1]”

  * Fix: Correct typo in replicate multi modal package (#16998)

### `llama-index-vector-stores-pinecone` [0.4.1]

Section titled “llama-index-vector-stores-pinecone [0.4.1]”

  * add get_nodes to pinecone (#17007)

## [2024-11-17]

Section titled “[2024-11-17]”

**NOTE:** Updating to v0.12.0 will require bumping every other `llama-index-*`
package! Every package has had a version bump. Only notable changes are below.

### `llama-index-core` [0.12.0]

Section titled “llama-index-core [0.12.0]”

  * Dropped python3.8 support, Unpinned numpy (#16973)
  * Kg/dynamic pg triplet retrieval limit (#16928)

### `llama-index-indices-managed-llama-cloud` [0.6.1]

Section titled “llama-index-indices-managed-llama-cloud [0.6.1]”

  * Add ID support for LlamaCloudIndex & update from_documents logic, modernize apis (#16927)
  * allow skipping waiting for ingestion when uploading file (#16934)
  * add support for files endpoints (#16933)

### `llama-index-indices-managed-vectara` [0.3.0]

Section titled “llama-index-indices-managed-vectara [0.3.0]”

  * Add Custom Prompt Parameter (#16976)

### `llama-index-llms-bedrock` [0.3.0]

Section titled “llama-index-llms-bedrock [0.3.0]”

  * minor fix for messages/completion to prompt (#15729)

### `llama-index-llms-bedrock-converse` [0.4.0]

Section titled “llama-index-llms-bedrock-converse [0.4.0]”

  * Fix async streaming with bedrock converse (#16942)

### `llama-index-multi-modal-llms-nvidia` [0.2.0]

Section titled “llama-index-multi-modal-llms-nvidia [0.2.0]”

  * add vlm support (#16751)

### `llama-index-readers-confluence` [0.3.0]

Section titled “llama-index-readers-confluence [0.3.0]”

  * Permit passing params to Confluence client (#16961)

### `llama-index-readers-github` [0.5.0]

Section titled “llama-index-readers-github [0.5.0]”

  * Add base URL extraction method to GithubRepositoryReader (#16926)

### `llama-index-vector-stores-weaviate` [1.2.0]

Section titled “llama-index-vector-stores-weaviate [1.2.0]”

  * Allow passing in Weaviate vector store kwargs (#16954)

## [2024-11-11]

Section titled “[2024-11-11]”

### `llama-index-core` [0.11.23]

Section titled “llama-index-core [0.11.23]”

  * Fix workflow timeout when streaming and exception happens (#16852)
  * New function for core.multi_modal_llms.generic_utils (#16896)
  * Added docstrings and unit tests for core.multimodal (#16872)
  * actually setting num_workers = num_cpus for ingestion pipeline (#16803)

### `llama-index-embeddings-nvidia` [0.2.5]

Section titled “llama-index-embeddings-nvidia [0.2.5]”

  * skip model validation for nvdev embedding models (#16883)

### `llama-index-embeddings-modelscope` [0.3.0]

Section titled “llama-index-embeddings-modelscope [0.3.0]”

  * Add ModelScope embedding support (#16873)

### `llama-index-graph-stores-kuzu` [0.4.0]

Section titled “llama-index-graph-stores-kuzu [0.4.0]”

  * BREAKING: Update relationship table label nomenclature, existing graphs will need to be recreated (#16886)

### `llama-index-llms-anthropic` [0.4.0]

Section titled “llama-index-llms-anthropic [0.4.0]”

  * use new anthropic token counting api (#16909)

### `llama-index-llms-bedrock-converse` [0.3.8]

Section titled “llama-index-llms-bedrock-converse [0.3.8]”

  * Add inference profile support to Bedrock Converse and add Llama 3.1/3.2 (#16827)

### `llama-index-llms-nvidia` [0.2.7]

Section titled “llama-index-llms-nvidia [0.2.7]”

  * skip model validation for nvdev llm models (#16882)

### `llama-index-llms-modelscope` [0.3.0]

Section titled “llama-index-llms-modelscope [0.3.0]”

  * Fix modelscope ‘pipeline’ referenced before assignment (#16864)

### `llama-index-llms-ollama` [0.3.6]

Section titled “llama-index-llms-ollama [0.3.6]”

  * fix ignoring tool calls in additional kwargs of messages (#16764)

### `llama-index-llms-siliconflow` [0.1.0]

Section titled “llama-index-llms-siliconflow [0.1.0]”

  * add siliconflow llm class (#16861)

### `llama-index-postprocessor-tei-rerank` [0.2.1]

Section titled “llama-index-postprocessor-tei-rerank [0.2.1]”

  * fix top-n parameter in TEI reranker (#16884)

### `llama-index-readers-gitbook` [0.2.0]

Section titled “llama-index-readers-gitbook [0.2.0]”

  * add gitbook reader (#16862)

### `llama-index-readers-google` [0.4.3]

Section titled “llama-index-readers-google [0.4.3]”

  * feat: add relative file path google drive (#16907)

### `llama-index-readers-file` [0.3.0]

Section titled “llama-index-readers-file [0.3.0]”

  * Bump versions and update pypdf dependency to 5.1.0 (#16905)

### `llama-index-vector-stores-azureaisearch` [0.2.9]

Section titled “llama-index-vector-stores-azureaisearch [0.2.9]”

  * Add UserAgent header “llamaindex-python” for azure search (#16895)

### `llama-index-vector-stores-clickhouse` [0.3.2]

Section titled “llama-index-vector-stores-clickhouse [0.3.2]”

  * fix clickhouse init in vector store (#16903)

## [2024-11-05]

Section titled “[2024-11-05]”

### `llama-index-core` [0.11.22]

Section titled “llama-index-core [0.11.22]”

  * bring back support for prompt templates in context chat engines (#16821)
  * Fixed the JSON Format of Generated Sub-Question (double curly brackets) (#16820)
  * markdown splitter improve metadata (#16789)
  * fix empty index + generation synthesizer (#16785)

### `llama-index-embeddings-azure-inference` [0.2.4]

Section titled “llama-index-embeddings-azure-inference [0.2.4]”

  * Support for api_version and Azure AI model inference service (#16802)

### `llama-index-embeddings-gemini` [0.2.2]

Section titled “llama-index-embeddings-gemini [0.2.2]”

  * fix await-async-embeddings (#16790)

### `llama-index-embeddings-siliconflow` [0.1.0]

Section titled “llama-index-embeddings-siliconflow [0.1.0]”

  * add siliconflow embedding class (#16753)

### `llama-index-indices-managed-vectara` [0.2.4]

Section titled “llama-index-indices-managed-vectara [0.2.4]”

  * Hotfix: Chain Query Configuration (#16818)

### `llama-index-llms-anthropic` [0.3.9]

Section titled “llama-index-llms-anthropic [0.3.9]”

  * Add Anthropic Claude Haiku 3.5 to the list of supported Claude models (#16823)

### `llama-index-llms-azure-inference` [0.2.4]

Section titled “llama-index-llms-azure-inference [0.2.4]”

  * Support for api_version and Azure AI model inference service (#16802)

### `llama-index-llms-bedrock` [0.2.6]

Section titled “llama-index-llms-bedrock [0.2.6]”

  * Add Anthropic Claude Haiku 3.5 to the list of supported Claude models for bedrock and bedrock-converse integrations (#16825)

### `llama-index-llms-bedrock-converse` [0.3.7]

Section titled “llama-index-llms-bedrock-converse [0.3.7]”

  * Add Anthropic Claude Haiku 3.5 to the list of supported Claude models for bedrock and bedrock-converse integrations (#16825)

### `llama-index-llms-dashscope` [0.2.5]

Section titled “llama-index-llms-dashscope [0.2.5]”

  * More tolerant definition of LLMMetadata information (#16830)
  * Fix abstract method signature error (#16809)

### `llama-index-llms-vllm` [0.3.0]

Section titled “llama-index-llms-vllm [0.3.0]”

  * remove beam search param for latest vllm (#16817)

### `llama-index-postprocessor-colpali-rerank` [0.1.0]

Section titled “llama-index-postprocessor-colpali-rerank [0.1.0]”

  * Add ColPali as reranker (#16829)

### `llama-index-postprocessor-siliconflow-rerank` [0.1.0]

Section titled “llama-index-postprocessor-siliconflow-rerank [0.1.0]”

  * add siliconflow rerank class (#16737)

### `llama-index-readers-microsoft-onedrive` [0.2.2]

Section titled “llama-index-readers-microsoft-onedrive [0.2.2]”

  * fix: add required_exts for one drive reader (#16822)

### `llama-index-vector-stores-chroma` [0.3.0]

Section titled “llama-index-vector-stores-chroma [0.3.0]”

  * Support breaking changes to filter syntax in latest chroma (#16806)

### `llama-index-vector-stores-pinecone` [0.3.0]

Section titled “llama-index-vector-stores-pinecone [0.3.0]”

  * support sparse embedding models, fix delete for serverless for pinecone (#16819)

## [2024-10-31]

Section titled “[2024-10-31]”

### `llama-index-core` [0.11.21]

Section titled “llama-index-core [0.11.21]”

  * Fixed issue with default value set as None for workflow `ctx.get()` (#16756)
  * fix various issues with react agent streaming (#16755)
  * add unit test for query pipeline (#16749)
  * Fix _merge_ref_doc_kv_pairs duped for-loop (#16739)
  * bugfix: determine if nodes is none when creating index (#16703)
  * fixes LLMRerank default_parse_choice_select_answer_fn parsing issue (#16736)
  * fix return type check on workflows (#16724)
  * Fixing a verbose issue and making sql errors more informative (#16686)

### `llama-index-embeddings-siliconflow` [0.1.0]

Section titled “llama-index-embeddings-siliconflow [0.1.0]”

  * add siliconflow embedding class (#16753)

### `llama-index-graph-stores-falkordb` [0.2.4]

Section titled “llama-index-graph-stores-falkordb [0.2.4]”

  * Multi-Graph-Supported-FalkorDB (#16482)

### `llama-index-llms-anthropic` [0.3.8]

Section titled “llama-index-llms-anthropic [0.3.8]”

  * adding additional claude model name, for vertex AI (#16692)

### `llama-index-llms-bedrock-converse` [0.3.6]

Section titled “llama-index-llms-bedrock-converse [0.3.6]”

  * Added mistral large2 model id in bedrock (#16742)
  * Improve Bedrock Tool Calling (#16723)
  * add new sonnet3.5 to function calling bedrock converse models (#16702)
  * update bedrock models (#16698)

### `llama-index-llms-bedrock` [0.2.5]

Section titled “llama-index-llms-bedrock [0.2.5]”

  * Added mistral large2 model id in bedrock (#16742)
  * add new sonnet3.5 to function calling bedrock converse models (#16702)
  * update bedrock models (#16698)

### `llama-index-llms-cohere` [0.3.2]

Section titled “llama-index-llms-cohere [0.3.2]”

  * Adding support to the new Aya-Expanse models from Cohere (#16733)

### `llama-index-llms-dashscope` [0.2.3]

Section titled “llama-index-llms-dashscope [0.2.3]”

  * DashScope llm support async (#16711)

### `llama-index-llms-nvidia` [0.3.4]

Section titled “llama-index-llms-nvidia [0.3.4]”

  * add nvidia/llama-3.2-nv-embedqa-1b-v1 to set of supported models (#16694)

### `llama-index-llms-pipeshift` [0.1.0]

Section titled “llama-index-llms-pipeshift [0.1.0]”

  * Pipeshift llama index integration (#16610)

### `llama-index-memory-mem0` [0.1.0]

Section titled “llama-index-memory-mem0 [0.1.0]”

  * add Mem0 as a memory (#16708)

### `llama-index-multi-modal-llms-anthropic` [0.2.4]

Section titled “llama-index-multi-modal-llms-anthropic [0.2.4]”

  * Fix anthropic multimodal deps conflict, update models (#16699)

### `llama-index-node-parser-docling` [0.2.0]

Section titled “llama-index-node-parser-docling [0.2.0]”

  * feat: update Docling reader & node parser to Docling v2 (#16677)

### `llama-index-postprocessor-nvidia-rerank` [0.3.3]

Section titled “llama-index-postprocessor-nvidia-rerank [0.3.3]”

  * add nvidia/llama-3.2-nv-rerankqa-1b-v1 to set of supported models (#16695)

### `llama-index-postprocessor-siliconflow-rerank` [0.1.0]

Section titled “llama-index-postprocessor-siliconflow-rerank [0.1.0]”

  * add siliconflow rerank class (#16737)

### `llama-index-readers-docling` [0.2.0]

Section titled “llama-index-readers-docling [0.2.0]”

  * feat: update Docling reader & node parser to Docling v2 (#16677)

### `llama-index-readers-microsoft-onedrive` [0.2.1]

Section titled “llama-index-readers-microsoft-onedrive [0.2.1]”

  * feat: add permissions to one drive metadata (#16646)

### `llama-index-storage-chat-store-azure` [0.2.4]

Section titled “llama-index-storage-chat-store-azure [0.2.4]”

  * Add Managed Identity authentication support for Azure storage components (#16710)
  * Add missing awaits in azure chat store (#16645)

### `llama-index-storage-docstore-azure` [0.2.1]

Section titled “llama-index-storage-docstore-azure [0.2.1]”

  * Add Managed Identity authentication support for Azure storage components (#16710)

### `llama-index-storage-index-store-azure` [0.3.1]

Section titled “llama-index-storage-index-store-azure [0.3.1]”

  * Add Managed Identity authentication support for Azure storage components (#16710)

### `llama-index-storage-kvstore-azure` [0.2.1]

Section titled “llama-index-storage-kvstore-azure [0.2.1]”

  * Add Managed Identity authentication support for Azure storage components (#16710)

### `llama-index-tools-openai-image-generation` [0.3.0]

Section titled “llama-index-tools-openai-image-generation [0.3.0]”

  * Makes the tool more compatible with the options, also for the future (#16676)

### `llama-index-tools-vectara-query` [0.1.0]

Section titled “llama-index-tools-vectara-query [0.1.0]”

  * Add Vectara Query Tool (#16722)

### `llama-index-vector-stores-azureaisearch` [0.2.6]

Section titled “llama-index-vector-stores-azureaisearch [0.2.6]”

  * Allow defining retrievable fields in Azure Vector Store (#16766)
  * feat: add get_nodes azureai search (#16761)
  * Added get_nodes() function in AISearch vector store (#16653)
  * Fix querying for ID in AzureAISearchVectorStore (fixes delete_nodes by node_ids) (#16769)

### `llama-index-vector-stores-hnswlib` [0.2.0]

Section titled “llama-index-vector-stores-hnswlib [0.2.0]”

  * Fixed issue with persistence, rearranged and added new options to construction of HnswlibVectorStore (#16673)

### `llama-index-vector-stores-opensearch` [0.4.1]

Section titled “llama-index-vector-stores-opensearch [0.4.1]”

  * Init OpensearchVectorClient with `os_async_client` (#16767)

### `llama-index-vector-stores-qdrant` [0.3.3]

Section titled “llama-index-vector-stores-qdrant [0.3.3]”

  * chore: add embeddings on qdrant get_nodes return (#16760)

### `llama-index-vector-stores-weaviate` [1.1.3]

Section titled “llama-index-vector-stores-weaviate [1.1.3]”

  * add default ID if node ID is not provided (#16671)

## [2024-10-24]

Section titled “[2024-10-24]”

### `llama-index-core` [0.11.20]

Section titled “llama-index-core [0.11.20]”

  * [actually nothing!]

### `llama-index-embeddings-cohere` [0.3.0]

Section titled “llama-index-embeddings-cohere [0.3.0]”

  * Add support for cohere multi-modal embeddings (#16667)

### `llama-index-embeddings-litellm` [0.2.2]

Section titled “llama-index-embeddings-litellm [0.2.2]”

  * support timeout param in litellmembedding (#16532)

### `llama-index-graph-stores-neo4j` [0.3.5]

Section titled “llama-index-graph-stores-neo4j [0.3.5]”

  * Make neo4j schema refresh configurable (#16651)
  * fix: receive warnings from dbms server in neo4j queries (#16598)

### `llama-index-indices-managed-vectara` [0.2.3]

Section titled “llama-index-indices-managed-vectara [0.2.3]”

  * add chain postprocessing for vectara (#16627)

### `llama-index-llms-anthropic` [0.3.7]

Section titled “llama-index-llms-anthropic [0.3.7]”

  * update anthropic model names (#16643)

### `llama-index-llms-openai` [0.2.16]

Section titled “llama-index-llms-openai [0.2.16]”

  * fix: skip processing of choice.delta when it is None (#16636)

### `llama-index-llms-reka` [0.1.0]

Section titled “llama-index-llms-reka [0.1.0]”

  * Reka llamaindex integration (llm and multi-modal-llm) (#15753)

### `llama-index-multi-modal-llms-reka` [0.1.0]

Section titled “llama-index-multi-modal-llms-reka [0.1.0]”

  * Reka llamaindex integration (llm and multi-modal-llm) (#15753)

### `llama-index-postprocessor-dashscope-rerank` [0.2.1]

Section titled “llama-index-postprocessor-dashscope-rerank [0.2.1]”

  * Fix BUG where the api_key parameter is not set when calling DashScopeRerank (#16665)

### `llama-index-readers-microsoft-sharepoint` [0.3.4]

Section titled “llama-index-readers-microsoft-sharepoint [0.3.4]”

  * add retry logic to requests in cases where access token expires (#16662)

### `llama-index-storage-docstore-mongodb` [0.2.1]

Section titled “llama-index-storage-docstore-mongodb [0.2.1]”

  * fix missing dependency error for mongodb docstore (#16654)

### `llama-index-storage-docstore-couchbase` [0.1.0]

Section titled “llama-index-storage-docstore-couchbase [0.1.0]”

  * Add support for Couchbase for DocStore & IndexStore (#16509)

### `llama-index-storage-kvstore-couchbase` [0.1.0]

Section titled “llama-index-storage-kvstore-couchbase [0.1.0]”

  * Add support for Couchbase for DocStore & IndexStore (#16509)

### `llama-index-storage-index-store-couchbase` [0.1.0]

Section titled “llama-index-storage-index-store-couchbase [0.1.0]”

  * Add support for Couchbase for IndexStore (#16509)

### `llama-index-storage-kvstore-mongodb` [0.2.1]

Section titled “llama-index-storage-kvstore-mongodb [0.2.1]”

  * add missing dependency for mongodb kvstore (#16632)

### `llama-index-utils-workflow` [0.2.2]

Section titled “llama-index-utils-workflow [0.2.2]”

  * Fix drawing for HITL (#16624)

## [2024-10-18]

Section titled “[2024-10-18]”

### `llama-index-core` [0.11.19]

Section titled “llama-index-core [0.11.19]”

  * Raise errors in instrumentation properly when handling asyncio futures (#16603)
  * fix: pass params to VectorStoreQuery properly in PGRetriever (#16586)
  * Fix structured predict type hints (#16585)
  * Add async version of retry_on_exceptions_with_backoff utility (#16374)
  * Refine CONTRIBUTING.md Documentation (#16548)

### `llama-index-embeddings-gaudi` [0.1.0]

Section titled “llama-index-embeddings-gaudi [0.1.0]”

  * Add embedding integration with Intel Gaudi in llama-index-embeddings-gaudi (#16521)

### `llama-index-embeddings-openvino` [0.4.1]

Section titled “llama-index-embeddings-openvino [0.4.1]”

  * Add OpenClip support through OpenVINO embedding (#16554)

### `llama-index-graph-stores-neo4j` [0.3.4]

Section titled “llama-index-graph-stores-neo4j [0.3.4]”

  * fix: remove warnings from dbms server in neo4j queries (#16598)

### `llama-index-llms-ibm` [0.2.2]

Section titled “llama-index-llms-ibm [0.2.2]”

  * IBM watsonx.ai Chat integration + function calling support (#16589)

### `llama-index-llms-mistralai` [0.2.7]

Section titled “llama-index-llms-mistralai [0.2.7]”

  * Add support for mistral latest models (#16571)

### `llama-index-llms-openai` [0.2.15]

Section titled “llama-index-llms-openai [0.2.15]”

  * Added check for fine-tuned models in function_calling method (#16568)
  * allow passing in openai clients directly (#16560)

### `llama-index-llms-replicate` [0.3.0]

Section titled “llama-index-llms-replicate [0.3.0]”

  * Use Replicate streaming API (#16597)

### `llama-index-multi-modal-llms-openvino` [0.1.0]

Section titled “llama-index-multi-modal-llms-openvino [0.1.0]”

  * Add OpenVINO multimodal support (#16567)

### `llama-index-multi-modal-llms-zhipuai` [0.1.0]

Section titled “llama-index-multi-modal-llms-zhipuai [0.1.0]”

  * add zhipuai multi modal llm class (#16551)

### `llama-index-readers-google` [0.4.2]

Section titled “llama-index-readers-google [0.4.2]”

  * Use port of redirect uri in credential file to run local server in GoogleDocsReader (#16327)

### `llama-index-storage-chat-store-postgres` [0.1.0]

Section titled “llama-index-storage-chat-store-postgres [0.1.0]”

  * feat: postgres chat store Integration (#16557)

### `llama-index-storage-chat-store-upstash` [0.1.2]

Section titled “llama-index-storage-chat-store-upstash [0.1.2]”

  * Fix pydantic errors in upstash chat store (#16559)

### `llama-index-vector-stores-azurecosmosmongo` [0.2.2]

Section titled “llama-index-vector-stores-azurecosmosmongo [0.2.2]”

  * Add DiskANN for Azure Cosmos DB Mongo vector store (#16581)

### `llama-index-vector-stores-hnswlib` [0.1.0]

Section titled “llama-index-vector-stores-hnswlib [0.1.0]”

  * Hnswlib Vector Store integration (#16443)

### `llama-index-vector-stores-oceanbase` [0.1.0]

Section titled “llama-index-vector-stores-oceanbase [0.1.0]”

  * Add vector store integration of OceanBase (#16550)

### `llama-index-vector-stores-qdrant` [0.3.2]

Section titled “llama-index-vector-stores-qdrant [0.3.2]”

  * Added optional name of text field in Qdrant vector database. (#16576)

## [2024-10-14]

Section titled “[2024-10-14]”

### `llama-index-core` [0.11.18]

Section titled “llama-index-core [0.11.18]”

  * Handle Empty Nodes List in PG Retrieval while adding text (#16447)
  * Improved text2sql parsing (#16445)

### `llama-index-embeddings-litellm` [0.2.2]

Section titled “llama-index-embeddings-litellm [0.2.2]”

  * support timeout param in litellmembedding (#16532)

### `llama-index-embeddings-zhipuai` [0.1.0]

Section titled “llama-index-embeddings-zhipuai [0.1.0]”

  * add zhipuai embedding class (#16505)

### `llama-index-graph-stores-memgraph` [0.1.0]

Section titled “llama-index-graph-stores-memgraph [0.1.0]”

  * Add Memgraph Graph Store Integration (#16345)

### `llama-index-llms-anthropic` [0.3.6]

Section titled “llama-index-llms-anthropic [0.3.6]”

  * Add anthropic bedrock support (#16478)

### `llama-index-llms-databricks` [0.2.1]

Section titled “llama-index-llms-databricks [0.2.1]”

  * Fix Databricks structured_predict (#16527)

### `llama-index-multi-modal-llms-anthropic` [0.2.3]

Section titled “llama-index-multi-modal-llms-anthropic [0.2.3]”

  * Propagate default_headers in AnthropicMultiModal (#16496)

### `llama-index-readers-document360` [0.1.0]

Section titled “llama-index-readers-document360 [0.1.0]”

  * Added Document360Reader. Contributed by the PLACE team. (#16305)

### `llama-index-readers-zyte-serp` [0.1.0]

Section titled “llama-index-readers-zyte-serp [0.1.0]”

  * Add Zyte serp integration (#16417)

### `llama-index-readers-upstage` [0.2.1]

Section titled “llama-index-readers-upstage [0.2.1]”

  * Added UpstageDocumentParseReader (#16099)

### `llama-index-storage-chat-store-azure` [0.2.2]

Section titled “llama-index-storage-chat-store-azure [0.2.2]”

  * Fix async methods in azure chat store (#16531)

### `llama-index-tools-weather` [0.1.0]

Section titled “llama-index-tools-weather [0.1.0]”

  * Fix format temp function (#16487)

### `llama-index-vector-stores-elasticsearch` [0.3.3]

Section titled “llama-index-vector-stores-elasticsearch [0.3.3]”

  * Add Support for Custom Metadata Keyword Suffix in Elasticsearch Integration (#16519)

### `llama-index-vector-stores-nile` [0.1.0]

Section titled “llama-index-vector-stores-nile [0.1.0]”

  * Add vector store integration for Nile (multi-tenant postgres) (#16437)

### `llama-index-vector-stores-opensearch` [0.4.0]

Section titled “llama-index-vector-stores-opensearch [0.4.0]”

  * Use efficient kNN filtering, fix filtering when input value is array of string (#16393)

### `llama-index-vector-stores-oracledb` [0.1.4]

Section titled “llama-index-vector-stores-oracledb [0.1.4]”

  * Various fixes for Oracle vector store integration (#16536)

### `llama-index-vector-stores-qdrant` [0.3.1]

Section titled “llama-index-vector-stores-qdrant [0.3.1]”

  * Update model name typo in Qdrant utils.py (#16494)

### `llama-index-vector-stores-timescalevector` [0.2.2]

Section titled “llama-index-vector-stores-timescalevector [0.2.2]”

  * fix timescale vector store class (#16539)

### `llama-index-vector-stores-weaviate` [1.1.2]

Section titled “llama-index-vector-stores-weaviate [1.1.2]”

  * Fixed issue for similarity score from Weaviate (#16489)

## [2024-10-08]

Section titled “[2024-10-08]”

### `llama-index-core` [0.11.17]

Section titled “llama-index-core [0.11.17]”

  * Fix ChatMessage serialization with janky openai types (#16410)

### `llama-index-embeddings-gemini` [0.2.1]

Section titled “llama-index-embeddings-gemini [0.2.1]”

  * fix gemini embedding async method (#16369)

### `llama-index-llms-gaudi` [0.1.0]

Section titled “llama-index-llms-gaudi [0.1.0]”

  * Add llm integration with Intel Gaudi in llama-index-llms-gaudi (#16308)

### `llama-index-llms-openai` [0.2.12]

Section titled “llama-index-llms-openai [0.2.12]”

  * don’t include tool calls if there was none (#16408)

### `llama-index-multi-modal-llms-huggingface` [0.1.1]

Section titled “llama-index-multi-modal-llms-huggingface [0.1.1]”

  * LlamaMultiModal class bug fix (#16413)
  * MultiModal.HuggingFaceMultiModal: fix errors and README, add stream_complete (#16376)

### `llama-index-node-parser-docling` [0.1.0]

Section titled “llama-index-node-parser-docling [0.1.0]”

  * feat: add Docling reader and node parser (#16406)

### `llama-index-readers-docling` [0.1.0]

Section titled “llama-index-readers-docling [0.1.0]”

  * feat: add Docling reader and node parser (#16406)

### `llama-index-readers-zyte-serp` [0.1.0]

Section titled “llama-index-readers-zyte-serp [0.1.0]”

  * Add Zyte serp integration (#16417)

### `llama-index-vector-stores-azureaisearch` [0.2.2]

Section titled “llama-index-vector-stores-azureaisearch [0.2.2]”

  * fix(bug): fixed bug with ensuring the metadata_mapping value (#16431)

### `llama-index-vector-stores-objectbox` [0.1.0]

Section titled “llama-index-vector-stores-objectbox [0.1.0]”

  * Add ObjectBox Vector Store Integration (#16314)

## [2024-10-03]

Section titled “[2024-10-03]”

### `llama-index-core` [0.11.16]

Section titled “llama-index-core [0.11.16]”

  * Treat non-dict tool JSON function arguments as empty (instead of unexpected raise) (#16316)
  * Fixing instrumentation for workflows (#16290)
  * (workaround) Suppress token detaching exception during workflow tracing (#16364)
  * Raise warning instead of error when nodes have no content (#16354)
  * Fix typo in BasePGRetriever causing graph context to not be added (#16357)

### `llama-index-embeddings-vertex-endpoint` [0.1.0]

Section titled “llama-index-embeddings-vertex-endpoint [0.1.0]”

  * adding vertex endpoint embedding (#16351)

### `llama-index-llms-fireworks` [0.2.1]

Section titled “llama-index-llms-fireworks [0.2.1]”

  * Adding support in FireworksAI for Meta 3.2 Models: 1b-instruct; 3b-instruct; 11b-vision; 90b-vision (#16349)

### `llama-index-multi-modal-llms-openai` [0.2.1]

Section titled “llama-index-multi-modal-llms-openai [0.2.1]”

  * Refactor OpenAI `update_tool_calls` (#16309)

### `llama-index-vector-stores-milvus` [0.2.7]

Section titled “llama-index-vector-stores-milvus [0.2.7]”

  * Add support for nested MetadataFilters and FilterOperator.IS_EMPTY (#16329)

## [2024-10-02]

Section titled “[2024-10-02]”

### `llama-index-core` [0.11.15]

Section titled “llama-index-core [0.11.15]”

  * added `to_dict()`, `from_dict()` and serializers for workflow context (#16250)
  * Ability to cancel workflow execution with `handler.cancel_run()` (#16320)
  * (breaking) Refactor `WorkflowHandler.run_step()` so user manually emits Event to start next step in workflow (#16277)

### `llama-index-embeddings-oracleai` [0.1.0]

Section titled “llama-index-embeddings-oracleai [0.1.0]”

  * Oraclevs integration (#16161)

### `llama-index-experimental` [0.4.0]

Section titled “llama-index-experimental [0.4.0]”

  * nudge-ft package and add an example for expanding your dataset (#16269)

### `llama-index-llms-anthropic` [0.3.3]

Section titled “llama-index-llms-anthropic [0.3.3]”

  * Add support for prompt caching for Anthropic LLM (#16270)

### `llama-index-llms-gemini` [0.3.6]

Section titled “llama-index-llms-gemini [0.3.6]”

  * Output token usage in raw data for Google Gemini LLMs (#16313)

### `llama-index-llms-openai` [0.2.10]

Section titled “llama-index-llms-openai [0.2.10]”

  * add 4o mini to azure openai models (#16335)

### `llama-index-llms-vertex` [0.3.7]

Section titled “llama-index-llms-vertex [0.3.7]”

  * Rremoving safety settings from generation config for Vertex AI models (#16337)

### `llama-index-multi-modal-llms-huggingface` [0.1.0]

Section titled “llama-index-multi-modal-llms-huggingface [0.1.0]”

  * LlamaIndex Multi_Modal_Llms Integration: Huggingface (#16133)

### `llama-index-readers-minio` [0.2.1]

Section titled “llama-index-readers-minio [0.2.1]”

  * rm extra print statements & replace create tmpfile function (#16291)

### `llama-index-readers-oracleai` [0.1.0]

Section titled “llama-index-readers-oracleai [0.1.0]”

  * Oraclevs integration (#16161)

### `llama-index-readers-web` [0.2.3]

Section titled “llama-index-readers-web [0.2.3]”

  * Add Zyte Web Reader (#16197)

### `llama-index-retrievers-bm25` [0.4.0]

Section titled “llama-index-retrievers-bm25 [0.4.0]”

  * bump deps for latest bm25s version (#16339)
  * Update BM25 retriever to use metadata (#16267)

### `llama-index-storage-chat-store-redis` [0.3.2]

Section titled “llama-index-storage-chat-store-redis [0.3.2]”

  * fix check for async client in redis chat store (#16321)

### `llama-index-storage-chat-store-upstash` [0.1.0]

Section titled “llama-index-storage-chat-store-upstash [0.1.0]”

  * Upstash Storage Chat Store Integration (#16237)

### `llama-index-vector-stores-milvus` [0.2.6]

Section titled “llama-index-vector-stores-milvus [0.2.6]”

  * milvus: always set self._collection (#16306)
  * Fix milvus collection creation with index_config (#16165)

### `llama-index-vector-stores-oracledb` [0.1.0]

Section titled “llama-index-vector-stores-oracledb [0.1.0]”

  * Oracledb integration (#16161)

## `llama-index-vector-stores-postgres` [0.2.6]

Section titled “llama-index-vector-stores-postgres [0.2.6]”

  * Support TEXT_MATCH FilterOperator in Postgres Vector Store (#16304)

## [2024-09-26]

Section titled “[2024-09-26]”

### `llama-index-core` [0.11.14]

Section titled “llama-index-core [0.11.14]”

  * Enhance insert Method in BaseIndex to Support Customizable Transformations (#16206)
  * Ensure ChatMemoryBuffer’s chat history never begins with a TOOL message (#16214)
  * safe prompt helper string formatting (#16219)
  * [Feature Request] Support max concurrent workflow_instance.run() executions (#16215)
  * Workflows + Human In The Loop Dedicated Support (#16220)

### `llama-index-graph-stores-neptune` [0.2.2]

Section titled “llama-index-graph-stores-neptune [0.2.2]”

  * fix NoneType object error when passing in provided client (#16174)

### `llama-index-llms-ollama` [0.3.3]

Section titled “llama-index-llms-ollama [0.3.3]”

  * fix ollama chat missing `keep_alive` (#16182)

### `llama-index-llms-vertex` [0.3.6]

Section titled “llama-index-llms-vertex [0.3.6]”

  * Fix vertex init function (#16216)

### `llama-index-multi-modal-llms-mistral` [0.1.0]

Section titled “llama-index-multi-modal-llms-mistral [0.1.0]”

  * Add support for Mistral Multi modal LLM (#16191)

### `llama-index-readers-jira` [0.3.0]

Section titled “llama-index-readers-jira [0.3.0]”

  * Add pagination support for Jira Reader (#16226)

### `llama-index-vector-stores-azurecosmosmongo` [0.2.1]

Section titled “llama-index-vector-stores-azurecosmosmongo [0.2.1]”

  * Azure Cosmos DB Filtered Vector Search (#16175)

### `llama-index-vector-stores-azurecosmosnosql` [1.1.0]

Section titled “llama-index-vector-stores-azurecosmosnosql [1.1.0]”

  * Azure Cosmos DB Filtered Vector Search (#16175)

### `llama-index-vector-stores-deeplake` [0.2.1]

Section titled “llama-index-vector-stores-deeplake [0.2.1]”

  * Add missing JWT dependency (#16236)

## [2024-09-24]

Section titled “[2024-09-24]”

### `llama-index-core` [0.11.13]

Section titled “llama-index-core [0.11.13]”

  * add option for string node representation during retireval in property graphs (#16100)
  * improve markdown element node parser and structured prediction reliability (#16172)

### `llama-index-graph-stores-neptune` [0.2.1]

Section titled “llama-index-graph-stores-neptune [0.2.1]”

  * Fixed issue where Neptune was adding additional labels (#16137)

### `llama-index-llms-vertext` [0.3.5]

Section titled “llama-index-llms-vertext [0.3.5]”

  * Pass safety_settings to send_message methods to fix settings not being sent to API (#16153)

### `llama-index-readers-box` [0.2.3]

Section titled “llama-index-readers-box [0.2.3]”

  * upgrading box sdk to >= 1.5.0 #16169

### `llama-index-storage-chat-store-dynamodb` [0.2.0]

Section titled “llama-index-storage-chat-store-dynamodb [0.2.0]”

  * Async support for dynamodb (#16139)

### `llama-index-storage-chat-store-redis` [0.3.1]

Section titled “llama-index-storage-chat-store-redis [0.3.1]”

  * Async support for redis (#16139)

### `llama-index-vector-stores-astra-db` [0.3.0]

Section titled “llama-index-vector-stores-astra-db [0.3.0]”

  * Depend on AstraPy 1.5 and above for AstraDBVectorStore (#16164)

## [2024-09-22]

Section titled “[2024-09-22]”

### `llama-index-core` [0.11.12]

Section titled “llama-index-core [0.11.12]”

  * Correct Pydantic warning(s) issed for llm base class (#16141)
  * globally safe format prompt variables in strings with JSON (#15734)
  * account for tools in prompt helper and response synthesizers (#16157)

### `llama-index-readers-google` [0.4.1]

Section titled “llama-index-readers-google [0.4.1]”

  * feat: add drive link to google drive reader metadata (#16156)

### `llama-index-readers-microsoft-sharepoint` [0.3.2]

Section titled “llama-index-readers-microsoft-sharepoint [0.3.2]”

  * Add required_exts option to SharePoint reader (#16152)

### `llama-index-vector-stores-milvus` [0.2.4]

Section titled “llama-index-vector-stores-milvus [0.2.4]”

  * Support user-defined schema in MilvusVectorStore (#16151)

## [2024-09-20]

Section titled “[2024-09-20]”

### `llama-index-core` [0.11.11]

Section titled “llama-index-core [0.11.11]”

  * Use response synthesizer in context chat engines (#16017)
  * Async chat memory operation (#16127)
  * Sql query add option for markdown response (#16103)
  * Add support for Path for SimpleDirectoryReader (#16108)
  * Update chat message class for multi-modal (#15969)
  * fix: `handler.stream_events()` doesn’t yield StopEvent (#16115)
  * pass `hybrid_top_k` in vector retriever (#16105)

### `llama-index-embeddings-elasticsearch` [0.2.1]

Section titled “llama-index-embeddings-elasticsearch [0.2.1]”

  * fix elasticsearch embedding async function (#16083)

### `llama-index-embeddings-jinaai` [0.3.1]

Section titled “llama-index-embeddings-jinaai [0.3.1]”

  * feat: update JinaEmbedding for v3 release (#15971)

### `llama-index-experimental` [0.3.3]

Section titled “llama-index-experimental [0.3.3]”

  * Enhance Pandas Query Engine Output Processor (#16052)

### `llama-index-indices-managed-vertexai` [0.1.1]

Section titled “llama-index-indices-managed-vertexai [0.1.1]”

  * fix incorrect parameters in VertexAIIndex client (#16080)

### `llama-index-node-parser-topic` [0.1.0]

Section titled “llama-index-node-parser-topic [0.1.0]”

  * Add TopicNodeParser based on MedGraphRAG paper (#16131)

### `llama-index-multi-modal-llms-ollama` [0.3.2]

Section titled “llama-index-multi-modal-llms-ollama [0.3.2]”

  * Implement async for multi modal ollama (#16091)

### `llama-index-postprocessor-cohere-rerank` [0.2.1]

Section titled “llama-index-postprocessor-cohere-rerank [0.2.1]”

  * feat: add configurable base_url field in rerank (#16050)

### `llama-index-readers-file` [0.2.2]

Section titled “llama-index-readers-file [0.2.2]”

  * fix bug missing import for bytesio (#16096)

### `llama-index-readers-wordpress` [0.2.2]

Section titled “llama-index-readers-wordpress [0.2.2]”

  * Wordpress: Allow control of whether Pages and/or Posts are retrieved (#16128)
  * Fix Issue 16071: wordpress requires username, password (#16072)

### `llama-index-vector-stores-lancedb` [0.2.1]

Section titled “llama-index-vector-stores-lancedb [0.2.1]”

  * fix hybrid search with latest lancedb client (#16057)

### `llama-index-vector-stores-mongodb` [0.3.0]

Section titled “llama-index-vector-stores-mongodb [0.3.0]”

  * Fix mongodb hybrid search top-k specs (#16105)

## [2024-09-16]

Section titled “[2024-09-16]”

### `llama-index-core` [0.11.10]

Section titled “llama-index-core [0.11.10]”

  * context/result refactor for workflows (#16036)
  * add sparse embedding abstraction (#16018)
  * Fix Pydantic models numeric validation (#16008)
  * Human in loop workflow example (#16011)

### `llama-index-callbacks-opik` [0.1.0]

Section titled “llama-index-callbacks-opik [0.1.0]”

  * opik integration (#16007)

### `llama-index-indices-managed-llama-cloud` [0.3.1]

Section titled “llama-index-indices-managed-llama-cloud [0.3.1]”

  * update llamacloud index with image nodes (#15996)

### `llama-index-indices-managed-vectara` [0.2.2]

Section titled “llama-index-indices-managed-vectara [0.2.2]”

  * Hotfix: Fix Citations Text (#16015)

### `llama-index-llms-huggingface` [0.3.4]

Section titled “llama-index-llms-huggingface [0.3.4]”

  * Fix: unnecessary warning issue in HuggingFace LLM when tokenizer is provided as argument (#16037)

### `llama-index-readers-dashvector` [0.3.0]

Section titled “llama-index-readers-dashvector [0.3.0]”

  * fix: new Data Connector adaption for DashVector (#16028)

### `llama-index-readers-quip` [0.1.0]

Section titled “llama-index-readers-quip [0.1.0]”

  * add quip reader (#16000)

### `llama-index-sparse-embeddings-fastembed` [0.1.0]

Section titled “llama-index-sparse-embeddings-fastembed [0.1.0]”

  * add fastembed sparse embeddings (#16018)

### `llama-index-vector-stores-elasticsearch` [0.2.1]

Section titled “llama-index-vector-stores-elasticsearch [0.2.1]”

  * Fix: get all documents from Elasticsearch KVStore (#16006)

### `llama-index-vector-stores-lancedb` [0.2.3]

Section titled “llama-index-vector-stores-lancedb [0.2.3]”

  * temporarily limit lancedb version (#16045)

### `llama-index-vector-stores-postgres` [0.2.5]

Section titled “llama-index-vector-stores-postgres [0.2.5]”

  * Implement `get_nodes()` on PGVectorStore (#16026)

## [2024-09-12]

Section titled “[2024-09-12]”

### `llama-index-core` [0.11.9]

Section titled “llama-index-core [0.11.9]”

  * Add callback manager to retriever query engine from args (#15990)
  * Do not pass system prompt from fn calling runner to fn calling worker (#15986)
  * fix: Error when parsing react output if tool name contains non-English characters (#15956)

### `llama-index-embeddings-alibabacloud-aisearch` [0.1.0]

Section titled “llama-index-embeddings-alibabacloud-aisearch [0.1.0]”

  * Add four alibabacloud-aisearch llama-index integrations: rerank, node_parser, readers, embeddings (#15934)

### `llama-index-experimental` [0.3.1]

Section titled “llama-index-experimental [0.3.1]”

  * Add NUDGE Finetuning (#15954)

### `llama-index-graph-stores-falkordb` [0.2.2]

Section titled “llama-index-graph-stores-falkordb [0.2.2]”

  * update falkordb client (#15940)

### `llama-index-llms-openai` [0.2.5]

Section titled “llama-index-llms-openai [0.2.5]”

  * Add support for o1 openai models (#15979)
  * force temp to 1.0 for o1 (#15983)

### `llama-index-node-parser-alibabacloud-aisearch` [0.1.0]

Section titled “llama-index-node-parser-alibabacloud-aisearch [0.1.0]”

  * Add four alibabacloud-aisearch llama-index integrations: rerank, node_parser, readers, embeddings (#15934)

### `llama-index-postprocessor-alibabacloud-aisearch-rerank` [0.1.0]

Section titled “llama-index-postprocessor-alibabacloud-aisearch-rerank
[0.1.0]”

  * Add four alibabacloud-aisearch llama-index integrations: rerank, node_parser, readers, embeddings (#15934)

### `llama-index-readers-alibabacloud-aisearch` [0.1.0]

Section titled “llama-index-readers-alibabacloud-aisearch [0.1.0]”

  * Add four alibabacloud-aisearch llama-index integrations: rerank, node_parser, readers, embeddings (#15934)

### `llama-index-vector-stores-opensearch` [0.3.0]

Section titled “llama-index-vector-stores-opensearch [0.3.0]”

  * Differentiate sync and async calls in OpenSearchVectorClient (#15945)

### `llama-index-vector-stores-postgres` [0.2.4]

Section titled “llama-index-vector-stores-postgres [0.2.4]”

  * fix attribute error in PGVectorStore (#15961)
  * add support for engine parameters (#15951)

### `llama-index-vector-stores-wordlift` [0.4.5]

Section titled “llama-index-vector-stores-wordlift [0.4.5]”

  * Catch nest_asyncio errors (#15975)

## [2024-09-09]

Section titled “[2024-09-09]”

### `llama-index-core` [0.11.8]

Section titled “llama-index-core [0.11.8]”

  * feat: Add a retry policy config to workflow steps (#15757)
  * Add doc id to Langchain format conversions (#15928)

### `llama-index-chat-store-dynamodb` [0.1.0]

Section titled “llama-index-chat-store-dynamodb [0.1.0]”

  * Add DynamoDBChatStore (#15917)

### `llama-index-cli` [0.3.1]

Section titled “llama-index-cli [0.3.1]”

  * Fix RagCLI pydantic error (#15931)

### `llama-index-llms-alibabacloud-aisearch` [0.1.0]

Section titled “llama-index-llms-alibabacloud-aisearch [0.1.0]”

  * add llama-index llms alibabacloud_aisearch integration (#15850)

### `llama-index-llms-mistralai` [0.2.3]

Section titled “llama-index-llms-mistralai [0.2.3]”

  * Make default mistral model support function calling with `large-latest` (#15906)

### `llama-index-llms-vertex` [0.3.4]

Section titled “llama-index-llms-vertex [0.3.4]”

  * Add InternalServerError to retry decorator (#15921)

### `llama-index-postprocessor-rankllm-rerank` [0.3.0]

Section titled “llama-index-postprocessor-rankllm-rerank [0.3.0]”

  * Update RankLLM with new rerankers (#15892)

### `llama-index-vector-stores-azurecosmosnosql` [1.0.0]

Section titled “llama-index-vector-stores-azurecosmosnosql [1.0.0]”

  * Adding vector store for Azure Cosmos DB NoSql (#14158)

### `llama-index-readers-microsoft-sharepoint` [0.3.1]

Section titled “llama-index-readers-microsoft-sharepoint [0.3.1]”

  * Fix error handling in sharepoint reader, fix error with download file (#15868)

### `llama-index-vector-stores-wordlift` [0.4.4]

Section titled “llama-index-vector-stores-wordlift [0.4.4]”

  * Adding support for MetadataFilters to WordLift Vector Store (#15905)

### `llama-index-vector-stores-opensearch` [0.2.2]

Section titled “llama-index-vector-stores-opensearch [0.2.2]”

  * Opensearch Serverless filtered query support using knn_score script (#15899)

## [2024-09-06]

Section titled “[2024-09-06]”

### `llama-index-core` [0.11.7]

Section titled “llama-index-core [0.11.7]”

  * Make SentenceSplitter’s secondary_chunking_regex optional (#15882)
  * force openai structured output (#15706)
  * fix assert error, add type ignore for streaming agents (#15887)
  * Fix image document deserialization issue (#15857)

### `llama-index-graph-stores-kuzu` [0.3.2]

Section titled “llama-index-graph-stores-kuzu [0.3.2]”

  * Bug fix for KuzuPropertyGraphStore: Allow upserting relations even when chunks are absent (#15889)

### `llama-index-llms-bedrock-converse` [0.3.0]

Section titled “llama-index-llms-bedrock-converse [0.3.0]”

  * Removed unused llama-index-llms-anthropic dependency from Bedrock Converse (#15869)

### `llama-index-vector-stores-postgres` [0.2.2]

Section titled “llama-index-vector-stores-postgres [0.2.2]”

  * Fix PGVectorStore with latest pydantic, update pydantic imports (#15886)

### `llama-index-vector-stores-tablestore` [0.1.0]

Section titled “llama-index-vector-stores-tablestore [0.1.0]”

  * Add TablestoreVectorStore (#15657)

## [2024-09-05]

Section titled “[2024-09-05]”

### `llama-index-core` [0.11.6]

Section titled “llama-index-core [0.11.6]”

  * add llama-deploy docs to docs builds (#15794)
  * Add oreilly course cookbooks (#15845)

### `llama-index-readers-box` [0.2.1]

Section titled “llama-index-readers-box [0.2.1]”

  * Various bug fixes (#15836)

### `llama-index-readers-file` [0.2.1]

Section titled “llama-index-readers-file [0.2.1]”

  * Update ImageReader file loading logic (#15848)

### `llama-index-tools-box` [0.2.1]

Section titled “llama-index-tools-box [0.2.1]”

  * Various bug fixes (#15836)

### `llama-index-vector-stores-opensearch` [0.2.1]

Section titled “llama-index-vector-stores-opensearch [0.2.1]”

  * Refresh Opensearch index after delete operation (#15854)

## [2024-09-04]

Section titled “[2024-09-04]”

### `llama-index-core` [0.11.5]

Section titled “llama-index-core [0.11.5]”

  * remove unneeded assert in property graph retriever (#15832)
  * make simple property graphs serialize again (#15833)
  * fix json schema for fastapi return types on core components (#15816)

### `llama-index-llms-nvidia` [0.2.2]

Section titled “llama-index-llms-nvidia [0.2.2]”

  * NVIDIA llm: Add Completion for starcoder models (#15802)

### `llama-index-llms-ollama` [0.3.1]

Section titled “llama-index-llms-ollama [0.3.1]”

  * add ollama response usage (#15773)

### `llama-index-readers-dashscope` [0.2.1]

Section titled “llama-index-readers-dashscope [0.2.1]”

  * fix pydantic v2 validation errors (#15800)

### `llama-index-readers-discord` [0.2.1]

Section titled “llama-index-readers-discord [0.2.1]”

  * fix: convert Document id from int to string in DiscordReader (#15806)

### `llama-index-vector-stores-mariadb` [0.1.0]

Section titled “llama-index-vector-stores-mariadb [0.1.0]”

  * Add MariaDB vector store integration package (#15564)

## [2024-09-02]

Section titled “[2024-09-02]”

### `llama-index-core` [0.11.4]

Section titled “llama-index-core [0.11.4]”

  * Add mypy to core (#14883)
  * Fix incorrect instrumentation fields/types (#15752)
  * FunctionCallingAgent sources bug + light wrapper to create agent (#15783)
  * Add text to sql advanced workflow nb (#15775)
  * fix: remove context after streaming workflow to enable streaming again (#15776)
  * Fix chat memory persisting and loading methods to use correct JSON format (#15545)
  * Fix `_example_type` class var being read as private attr with Pydantic V2 (#15758)

### `llama-index-embeddings-litellm` [0.2.1]

Section titled “llama-index-embeddings-litellm [0.2.1]”

  * add dimensions param to LiteLLMEmbedding, fix a bug that prevents reading vars from env (#15770)

### `llama-index-embeddings-upstage` [0.2.1]

Section titled “llama-index-embeddings-upstage [0.2.1]”

  * Bugfix upstage embedding when initializing the UpstageEmbedding class (#15767)

### `llama-index-embeddings-sagemaker-endpoint` [0.2.2]

Section titled “llama-index-embeddings-sagemaker-endpoint [0.2.2]”

  * Fix Sagemaker Field required issue (#15778)

### `llama-index-graph-stores-falkordb` [0.2.1]

Section titled “llama-index-graph-stores-falkordb [0.2.1]”

  * fix relations upsert with special chars (#15769)

### `llama-index-graph-stores-neo4j` [0.3.1]

Section titled “llama-index-graph-stores-neo4j [0.3.1]”

  * Add native vector index support for neo4j lpg and fix vector filters (#15759)

### `llama-index-llms-azure-inference` [0.2.2]

Section titled “llama-index-llms-azure-inference [0.2.2]”

  * fix: GitHub Models metadata retrieval (#15747)

### `llama-index-llms-bedrock` [0.2.1]

Section titled “llama-index-llms-bedrock [0.2.1]”

  * Update `base.py` to fix `self` issues (#15729)

### `llama-index-llms-ollama` [0.3.1]

Section titled “llama-index-llms-ollama [0.3.1]”

  * add ollama response usage (#15773)

### `llama-index-llms-sagemaker-endpoint` [0.2.2]

Section titled “llama-index-llms-sagemaker-endpoint [0.2.2]”

  * Fix Sagemaker Field required issue (#15778)

### `llama-index-multi-modal-llms-anthropic` [0.2.1]

Section titled “llama-index-multi-modal-llms-anthropic [0.2.1]”

  * Support image type detection without knowing the file name (#15763)

### `llama-index-vector-stores-milvus` [0.2.2]

Section titled “llama-index-vector-stores-milvus [0.2.2]”

  * feat: implement get_nodes for MilvusVectorStore (#15696)

### `llama-index-vector-stores-tencentvectordb` [0.2.1]

Section titled “llama-index-vector-stores-tencentvectordb [0.2.1]”

  * fix: tencentvectordb inconsistent attribute name (#15733)

## [2024-08-29]

Section titled “[2024-08-29]”

### `llama-index-core` [0.11.3]

Section titled “llama-index-core [0.11.3]”

  * refact: merge Context and Session to simplify the workflows api (#15709)
  * chore: stop using deprecated `ctx.data` in workflows docs (#15716)
  * fix: stop streaming workflow events when a step raises (#15714)
  * Fix llm_chat_callback for multimodal llms (#15700)
  * chore: Increase unit tests coverage for the workflow package (#15691)
  * fix SimpleVectorStore.from_persist_dir() behaviour (#15534)

### `llama-index-embeddings-azure-openai` [0.2.5]

Section titled “llama-index-embeddings-azure-openai [0.2.5]”

  * fix json serialization for azure embeddings (#15724)

### `llama-index-graph-stores-kuzu` [0.3.0]

Section titled “llama-index-graph-stores-kuzu [0.3.0]”

  * Add KuzuPropertyGraphStore (#15678)

### `llama-index-indices-managed-vectara` [0.2.1]

Section titled “llama-index-indices-managed-vectara [0.2.1]”

  * added new User Defined Function reranker (#15546)

### `llama-index-llms-mistralai` [0.2.2]

Section titled “llama-index-llms-mistralai [0.2.2]”

  * Fix `random_seed` type in mistral llm (#15701)

### `llama-index-llms-nvidia` [0.2.1]

Section titled “llama-index-llms-nvidia [0.2.1]”

  * Add function/tool calling support to nvidia llm (#15359)

### `llama-index-multi-modal-llms-ollama` [0.3.0]

Section titled “llama-index-multi-modal-llms-ollama [0.3.0]”

  * bump ollama client deps for multimodal llm (#15702)

### `llama-index-readers-web` [0.2.1]

Section titled “llama-index-readers-web [0.2.1]”

  * Fix: Firecrawl scraping url response (#15720)

### `llama-index-selectors-notdiamond` [0.1.0]

Section titled “llama-index-selectors-notdiamond [0.1.0]”

  * Adding Not Diamond to llama_index (#15703)

### `llama-index-vector-stores-milvus` [0.2.3]

Section titled “llama-index-vector-stores-milvus [0.2.3]”

  * MMR in Milvus vector stores (#15634)
  * feat: implement get_nodes for MilvusVectorStore (#15696)

## [2024-08-27]

Section titled “[2024-08-27]”

### `llama-index-core` [0.11.2]

Section titled “llama-index-core [0.11.2]”

  * fix tool schemas generation for pydantic v2 to handle nested models (#15679)
  * feat: support default values for nested workflows (#15660)
  * feat: allow FunctionTool with just an async fn (#15638)
  * feat: Allow streaming events from steps (#15488)
  * fix auto-retriever pydantic indent error (#15648)
  * Implement Router Query Engine example using workflows (#15635)
  * Add multi step query engine example using workflows (#15438)
  * start traces for llm-level operations (#15542)
  * Pass callback_manager to init in CodeSplitter from_defaults (#15585)

### `llama-index-embeddings-xinference` [0.1.0]

Section titled “llama-index-embeddings-xinference [0.1.0]”

  * Add Xinference Embedding Class (#15579)

### `llama-index-llms-ai21` [0.3.3]

Section titled “llama-index-llms-ai21 [0.3.3]”

  * Integrations: AI21 function calling Support (#15622)

### `llama-index-llms-anthropic` [0.3.0]

Section titled “llama-index-llms-anthropic [0.3.0]”

  * Added support for anthropic models through GCP Vertex AI (#15661)

### `llama-index-llms-cerebras` [0.1.0]

Section titled “llama-index-llms-cerebras [0.1.0]”

  * Implement Cerebras Integration (#15665)

### `llama-index-postprocessor-nvidia-rerank` [0.3.1]

Section titled “llama-index-postprocessor-nvidia-rerank [0.3.1]”

  * fix downloaded nim endpoint path (#15645)
  * fix llama-index-postprocessor-nvidia-rerank tests (#15643)

### `llama-index-postprocessor-xinference-rerank` [0.1.0]

Section titled “llama-index-postprocessor-xinference-rerank [0.1.0]”

  * add xinference rerank class (#15639)

### `llama-index-vector-stores-alibabacloud-opensearch` [0.2.1]

Section titled “llama-index-vector-stores-alibabacloud-opensearch [0.2.1]”

  * fix set output fields in AlibabaCloudOpenSearchConfig (#15562)

### `llama-index-vector-stores-azureaisearch` [0.2.1]

Section titled “llama-index-vector-stores-azureaisearch [0.2.1]”

  * Upgrade azure-search-documents to 2024-07-01 GA API and Add Support for Scalar and Binary Quantization in Index Creation (#15650)

### `llama-index-vector-stores-neo4j` [0.2.1]

Section titled “llama-index-vector-stores-neo4j [0.2.1]”

  * Neo4j Vector Store: Make Embedding Dimension Check Optional (#15628)

### `llama-inde-vector-stores-milvus` [0.2.1]

Section titled “llama-inde-vector-stores-milvus [0.2.1]”

  * Change the default consistency level of Milvus (#15577)

### `llama-index-vector-stores-elasticsearch` [0.3.2]

Section titled “llama-index-vector-stores-elasticsearch [0.3.2]”

  * Fix the ElasticsearchStore key error (#15631)

## [2024-08-23]

Section titled “[2024-08-23]”

### `llama-index-core` [0.11.1]

Section titled “llama-index-core [0.11.1]”

  * Replacing client-side docs search with algolia (#15574)
  * Add docs on extending workflows (#15573)
  * rename method for nested workflows to add_workflows (#15596)
  * chore: fix @step usage in the core codebase (#15588)
  * Modify the validate function in ReflectionWorkflow example notebook to use pydantic model_validate_json method (#15567)
  * feature: allow concurrent runs of the same workflow instance (#15568)
  * docs: remove redundant pass_context=True from docs and examples (#15571)

### `llama-index-embeddings-openai` [0.2.3]

Section titled “llama-index-embeddings-openai [0.2.3]”

  * fix openai embeddings with pydantic v2 (#15576)

### `llama-index-embeddings-voyageai` [0.2.1]

Section titled “llama-index-embeddings-voyageai [0.2.1]”

  * bump voyage ai embedding client dep (#15595)

### `llama-index-llms-vertex` [0.3.3]

Section titled “llama-index-llms-vertex [0.3.3]”

  * Vertex LLM: Correctly add function calling part to prompt (#15569)
  * Vertex LLM: Remove manual setting of message content to Function Calling (#15586)

## [2024-08-22]

Section titled “[2024-08-22]”

### `llama-index-core` [0.11.0]

Section titled “llama-index-core [0.11.0]”

  * removed deprecated `ServiceContext` — using this now will print an error with a link to the migration guide
  * removed deprecated `LLMPredictor` — using this now will print an error, any existing LLM is a drop-in replacement
  * made `pandas` an optional dependency

### `Everything Else`

Section titled “Everything Else”

  * bumped the minor version of every package to account for the new version of `llama-index-core`

## [2024-08-21]

Section titled “[2024-08-21]”

### `llama-index-core` [0.10.68]

Section titled “llama-index-core [0.10.68]”

  * remove nested progress bars in base element node parser (#15550)
  * Adding exhaustive docs for workflows (#15556)
  * Adding multi-strategy workflow with reflection notebook example (#15445)
  * remove openai dep from core (#15527)
  * Improve token counter to handle more response types (#15501)
  * feat: Allow using step decorator without parentheses (#15540)
  * feat: workflow services (aka nested workflows) (#15325)
  * Remove requirement to specify “allowed_query_fields” parameter when using “cypher_validator” in TextToCypher retriever (#15506)

### `llama-index-embeddings-mistralai` [0.1.6]

Section titled “llama-index-embeddings-mistralai [0.1.6]”

  * fix mistral embeddings usage (#15508)

### `llama-index-embeddings-ollama` [0.2.0]

Section titled “llama-index-embeddings-ollama [0.2.0]”

  * use ollama client for embeddings (#15478)

### `llama-index-embeddings-openvino` [0.2.1]

Section titled “llama-index-embeddings-openvino [0.2.1]”

  * support static input shape for openvino embedding and reranker (#15521)

### `llama-index-graph-stores-neptune` [0.1.8]

Section titled “llama-index-graph-stores-neptune [0.1.8]”

  * Added code to expose structured schema for Neptune (#15507)

### `llama-index-llms-ai21` [0.3.2]

Section titled “llama-index-llms-ai21 [0.3.2]”

  * Integration: AI21 Tools support (#15518)

### `llama-index-llms-bedrock` [0.1.13]

Section titled “llama-index-llms-bedrock [0.1.13]”

  * Support token counting for llama-index integration with bedrock (#15491)

### `llama-index-llms-cohere` [0.2.2]

Section titled “llama-index-llms-cohere [0.2.2]”

  * feat: add tool calling support for achat cohere (#15539)

### `llama-index-llms-gigachat` [0.1.0]

Section titled “llama-index-llms-gigachat [0.1.0]”

  * Adding gigachat LLM support (#15313)

### `llama-index-llms-openai` [0.1.31]

Section titled “llama-index-llms-openai [0.1.31]”

  * Fix incorrect type in OpenAI token usage report (#15524)
  * allow streaming token counts for openai (#15548)

### `llama-index-postprocessor-nvidia-rerank` [0.2.1]

Section titled “llama-index-postprocessor-nvidia-rerank [0.2.1]”

  * add truncate support (#15490)
  * Update to 0.2.0, remove old code (#15533)
  * update default model to nvidia/nv-rerankqa-mistral-4b-v3 (#15543)

### `llama-index-readers-bitbucket` [0.1.4]

Section titled “llama-index-readers-bitbucket [0.1.4]”

  * Fixing the issues in loading file paths from bitbucket (#15311)

### `llama-index-readers-google` [0.3.1]

Section titled “llama-index-readers-google [0.3.1]”

  * enhance google drive reader for improved functionality and usability (#15512)

### `llama-index-readers-remote` [0.1.6]

Section titled “llama-index-readers-remote [0.1.6]”

  * check and sanitize remote reader urls (#15494)

### `llama-index-vector-stores-qdrant` [0.2.17]

Section titled “llama-index-vector-stores-qdrant [0.2.17]”

  * fix: setting IDF modifier in QdrantVectorStore for sparse vectors (#15538)

## [2024-08-18]

Section titled “[2024-08-18]”

### `llama-index-core` [0.10.67]

Section titled “llama-index-core [0.10.67]”

  * avoid nltk 3.9 since its broken (#15473)
  * docs: openllmetry now uses instrumentation (#15443)
  * Fix LangChainDeprecationWarning (#15397)
  * Add get/set API to the Context and make it coroutine-safe (#15152)
  * docs: Cleanlab’s cookbook (#15352)
  * pass kwargs in `async_add()` for vector stores (#15333)
  * escape json in structured llm (#15404)
  * docs: Add JSONAlyze Query Engine using workflows cookbook (#15408)

### `llama-index-embeddings-gigachat` [0.1.0]

Section titled “llama-index-embeddings-gigachat [0.1.0]”

  * Add GigaChat embedding (#15278)

### `llama-index-finetuning` [0.1.12]

Section titled “llama-index-finetuning [0.1.12]”

  * feat: Integrating Azure OpenAI Finetuning (#15297)

### `llama-index-graph-stores-neptune` [0.1.7]

Section titled “llama-index-graph-stores-neptune [0.1.7]”

  * Exposed NeptuneQueryException and added additional debug information (#15448)
  * Fixed issue #15414 and added ability to do partial matchfor Neptune Analytics (#15415)
  * Use backticks to escape label (#15324)

### `llama-index-llms-cohere` [0.2.1]

Section titled “llama-index-llms-cohere [0.2.1]”

  * feat: add tool calling for cohere (#15144)

### `llama-index-packs-corrective-rag` [0.1.2]

Section titled “llama-index-packs-corrective-rag [0.1.2]”

  * Ports over LongRAGPack, Corrective RAG Pack, and Self-Discover Pack to Workflows (#15160)

### `llama-index-packs-longrag` [0.1.1]

Section titled “llama-index-packs-longrag [0.1.1]”

  * Ports over LongRAGPack, Corrective RAG Pack, and Self-Discover Pack to Workflows (#15160)

### `llama-index-packs-self-discover` [0.1.2]

Section titled “llama-index-packs-self-discover [0.1.2]”

  * Ports over LongRAGPack, Corrective RAG Pack, and Self-Discover Pack to Workflows (#15160)

### `llama-index-readers-preprocess` [0.1.4]

Section titled “llama-index-readers-preprocess [0.1.4]”

  * Enhance PreprocessReader (#15302)

## [2024-08-15]

Section titled “[2024-08-15]”

### `llama-index-core` [0.10.66]

Section titled “llama-index-core [0.10.66]”

  * Temporarily revert nltk dependency due to latest version being removed from pypi
  * Add citation query engine with workflows example (#15372)
  * bug: Semantic double merging splitter creates chunks larger thank chunk size (#15188)
  * feat: make `send_event()` in workflows assign the target step (#15259)
  * make all workflow events accessible like mappings (#15310)

### `llama-index-indices-managed-bge-m3` [0.1.0]

Section titled “llama-index-indices-managed-bge-m3 [0.1.0]”

  * Add BGEM3Index (#15197)

### `llama-index-llms-huggingface` [0.2.7]

Section titled “llama-index-llms-huggingface [0.2.7]”

  * update HF’s completion_to_prompt (#15354)

### `llama-index-llms-sambanova` [0.1.0]

Section titled “llama-index-llms-sambanova [0.1.0]”

  * Wrapper for SambaNova (Sambaverse and SambaStudio) with Llama-index (#15220)

### `llama-index-packs-code-hierarchy` [0.1.7]

Section titled “llama-index-packs-code-hierarchy [0.1.7]”

  * Update code_hierarchy.py adding php support (#15145)

### `llama-index-postprocessor-dashscope-rerank` [0.1.4]

Section titled “llama-index-postprocessor-dashscope-rerank [0.1.4]”

  * fix bug when calling llama-index-postprocessor-dashscope-rerank (#15358)

### `llama-index-readers-box` [0.1.2]

Section titled “llama-index-readers-box [0.1.2]”

  * Box refactor: Box File to Llama-Index Document adaptor (#15314)

### `llama-index-readers-gcs` [0.1.8]

Section titled “llama-index-readers-gcs [0.1.8]”

  * GCSReader: Implementing ResourcesReaderMixin and FileSystemReaderMixin (#15365)

### `llama-index-tools-box` [0.1.1]

Section titled “llama-index-tools-box [0.1.1]”

  * Box refactor: Box File to Llama-Index Document adaptor (#15314)
  * Box tools for AI Agents (#15236)

### `llama-index-vector-stores-postgres` [0.1.14]

Section titled “llama-index-vector-stores-postgres [0.1.14]”

  * Check if hnsw index exists (#15287)

## [2024-08-12]

Section titled “[2024-08-12]”

### `llama-index-core` [0.10.65]

Section titled “llama-index-core [0.10.65]”

  * chore: bump nltk version (#15277)

### `llama-index-tools-box` [0.1.0]

Section titled “llama-index-tools-box [0.1.0]”

  * Box tools for AI Agents (#15236)

### `llama-index-multi-modal-llms-gemini` [0.1.8]

Section titled “llama-index-multi-modal-llms-gemini [0.1.8]”

  * feat: add default_headers to Gemini multi-model (#15296)

### `llama-index-vector-stores-clickhouse` [0.2.0]

Section titled “llama-index-vector-stores-clickhouse [0.2.0]”

  * chore: stop using ServiceContext from the clickhouse integration (#15300)

### `llama-index-experimental` [0.2.0]

Section titled “llama-index-experimental [0.2.0]”

  * chore: remove ServiceContext usage from experimental package (#15301)

### `llama-index-extractors-marvin` [0.1.4]

Section titled “llama-index-extractors-marvin [0.1.4]”

  * fix: MarvinMetadataExtractor functionality and apply async support (#15247)

### `llama-index-utils-workflow` [0.1.1]

Section titled “llama-index-utils-workflow [0.1.1]”

  * chore: bump black version (#15288)
  * chore: bump nltk version (#15277)

### `llama-index-readers-microsoft-onedrive` [0.1.9]

Section titled “llama-index-readers-microsoft-onedrive [0.1.9]”

  * chore: bump nltk version (#15277)

### `llama-index-embeddings-upstage` [0.1.3]

Section titled “llama-index-embeddings-upstage [0.1.3]”

  * chore: bump nltk version (#15277)

### `llama-index-embeddings-nvidia` [0.1.5]

Section titled “llama-index-embeddings-nvidia [0.1.5]”

  * chore: bump nltk version (#15277)

### `llama-index-embeddings-litellm` [0.1.1]

Section titled “llama-index-embeddings-litellm [0.1.1]”

  * chore: bump nltk version (#15277)

### `llama-index-legacy` [0.9.48post1]

Section titled “llama-index-legacy [0.9.48post1]”

  * chore: bump nltk version (#15277)

### `llama-index-packs-streamlit-chatbot` [0.1.5]

Section titled “llama-index-packs-streamlit-chatbot [0.1.5]”

  * chore: bump nltk version (#15277)

### `llama-index-embeddings-huggingface` [0.2.3]

Section titled “llama-index-embeddings-huggingface [0.2.3]”

  * Feature: added multiprocessing for creating hf embedddings (#15260)

## [2024-08-09]

Section titled “[2024-08-09]”

### `llama-index-core` [0.10.64]

Section titled “llama-index-core [0.10.64]”

  * fix: children nodes not carrying metadata from source nodes (#15254)
  * Workflows: fix the validation error in the decorator (#15252)
  * fix: strip '''sql (Markdown SQL code snippet) in SQL Retriever (#15235)

### `llama-index-indices-managed-colbert` [0.2.0]

Section titled “llama-index-indices-managed-colbert [0.2.0]”

  * Remove usage of ServiceContext in Colbert integration (#15249)

### `llama-index-vector-stores-milvus` [0.1.23]

Section titled “llama-index-vector-stores-milvus [0.1.23]”

  * feat: Support Milvus collection properties (#15241)

### `llama-index-llms-cleanlab` [0.1.2]

Section titled “llama-index-llms-cleanlab [0.1.2]”

  * Update models supported by Cleanlab TLM (#15240)

### `llama-index-llms-huggingface` [0.2.6]

Section titled “llama-index-llms-huggingface [0.2.6]”

  * add generation prompt to HF chat template (#15239)

### `llama-index-llms-openvino` [0.2.1]

Section titled “llama-index-llms-openvino [0.2.1]”

  * add generation prompt to HF chat template (#15239)

### `llama-index-graph-stores-neo4j` [0.2.14]

Section titled “llama-index-graph-stores-neo4j [0.2.14]”

  * Neo4jPropertyGraphStore.get() check for id prop (#15228)

### `llama-index-readers-file` [0.1.33]

Section titled “llama-index-readers-file [0.1.33]”

  * Fix fs.open path type (#15226)

## [2024-08-08]

Section titled “[2024-08-08]”

### `llama-index-core` [0.10.63]

Section titled “llama-index-core [0.10.63]”

  * add num_workers in workflow decorator to resolve step concurrancy issue (#15210)
  * Sub Question Query Engine as workflow notebook example (#15209)
  * Add Llamatrace to workflow notebooks (#15186)
  * Use node hash instead of node text to match nodes in fusion retriever (#15172)

### `llama-index-embeddings-mistralai` [0.1.5]

Section titled “llama-index-embeddings-mistralai [0.1.5]”

  * handle mistral v1.0 client (#15229)

### `llama-index-extractors-relik` [0.1.1]

Section titled “llama-index-extractors-relik [0.1.1]”

  * Fix relik extractor skip error (#15225)

### `llama-index-finetuning` [0.1.11]

Section titled “llama-index-finetuning [0.1.11]”

  * handle mistral v1.0 client (#15229)

### `llama-index-graph-stores-neo4j` [0.2.14]

Section titled “llama-index-graph-stores-neo4j [0.2.14]”

  * Add neo4j generic node label (#15191)

### `llama-index-llms-anthropic` [0.1.17]

Section titled “llama-index-llms-anthropic [0.1.17]”

  * Allow for images in Anthropic messages (#15227)

### `llama-index-llms-mistralai` [0.1.20]

Section titled “llama-index-llms-mistralai [0.1.20]”

  * handle mistral v1.0 client (#15229)

### `llama-index-packs-mixture-of-agents` [0.1.2]

Section titled “llama-index-packs-mixture-of-agents [0.1.2]”

  * Update Mixture Of Agents llamapack with workflows (#15232)

### `llama-index-tools-slack` [0.1.4]

Section titled “llama-index-tools-slack [0.1.4]”

  * Fixed slack client ref in ToolSpec (#15202)

## [2024-08-06]

Section titled “[2024-08-06]”

### `llama-index-core` [0.10.62]

Section titled “llama-index-core [0.10.62]”

  * feat: Allow None metadata filter by using IS_EMPTY operator (#15167)
  * fix: use parent source node to node relationships if possible during node parsing (#15182)
  * Use node hash instead of node text to match nodes in fusion retriever (#15172)

### `llama-index-graph-stores-neo4j` [0.2.13]

Section titled “llama-index-graph-stores-neo4j [0.2.13]”

  * Neo4j property graph client side batching (#15179)

### `llama-index-graph-stores-neptune` [0.1.4]

Section titled “llama-index-graph-stores-neptune [0.1.4]”

  * PropertyGraphStore support for Amazon Neptune (#15126)

### `llama-index-llms-gemini` [0.2.0]

Section titled “llama-index-llms-gemini [0.2.0]”

  * feat: add default_headers to Gemini model (#15141)

### `llama-index-llms-openai` [0.1.28]

Section titled “llama-index-llms-openai [0.1.28]”

  * OpenAI: Support new strict functionality in tool param (#15177)

### `llama-index-vector-stores-opensearch` [0.1.14]

Section titled “llama-index-vector-stores-opensearch [0.1.14]”

  * Add support for full MetadataFilters in Opensearch (#15176)

### `llama-index-vector-stores-qdrant` [0.2.15]

Section titled “llama-index-vector-stores-qdrant [0.2.15]”

  * feat: Allow None metadata filter by using IS_EMPTY operator (#15167)

### `llama-index-vector-stores-wordlift` [0.3.0]

Section titled “llama-index-vector-stores-wordlift [0.3.0]”

  * Add support for fields projection and update sample Notebook (#15140)

## [2024-08-05]

Section titled “[2024-08-05]”

### `llama-index-core` [0.10.61]

Section titled “llama-index-core [0.10.61]”

  * Tweaks to workflow docs (document `.send_event()`, expand examples) (#15154)
  * Create context manager to instrument event and span tags (#15116)
  * keyval index store index store updated to accept custom collection suffix (#15134)
  * make workflow context able to collect multiples of the same event (#15153)
  * Fix `__str__` method for AsyncStreamingResponse (#15131)

### `llama-index-callbacks-literalai` [1.0.0]

Section titled “llama-index-callbacks-literalai [1.0.0]”

  * feat(integration): add a global handler for Literal AI (#15064)

### `llama-index-extractors-relik` [0.1.0]

Section titled “llama-index-extractors-relik [0.1.0]”

  * Add relik kg constructor (#15123)

### `llama-index-graph-stores-neo4j` [0.1.12]

Section titled “llama-index-graph-stores-neo4j [0.1.12]”

  * fix neo4j property graph relation properties when querying (#15068)

### `llama-index-llms-fireworks` [0.1.9]

Section titled “llama-index-llms-fireworks [0.1.9]”

  * feat: add default_headers to Fireworks llm (#15150)

### `llama-index-llms-gemini` [0.1.12]

Section titled “llama-index-llms-gemini [0.1.12]”

  * Fix: Gemini 1.0 Pro Vision has been official deprecated, switch default model to gemini-1.5-flash (#15000)

### `llama-index-llms-paieas` [0.1.0]

Section titled “llama-index-llms-paieas [0.1.0]”

  * Add LLM for AlibabaCloud PaiEas (#14983)

### `llama-index-llms-predibase` [0.1.7]

Section titled “llama-index-llms-predibase [0.1.7]”

  * Fix Predibase Integration for HuggingFace-hosted fine-tuned adapters (#15130)

## [2024-02-02]

Section titled “[2024-02-02]”

### `llama-index-core` [0.10.60]

Section titled “llama-index-core [0.10.60]”

  * update `StartEvent` usage to allow for dot notation attribute access (#15124)
  * Add GraphRAGV2 notebook (#15119)
  * Fixed minor bug in DynamicLLMPathExtractor as well as default output parsers not working (#15085)
  * update typing for workflow timeouts (#15102)
  * fix(sql_wrapper): dont mention foreign keys when there is none (#14998)

### `llama-index-graph-stores-neo4j` [0.2.11]

Section titled “llama-index-graph-stores-neo4j [0.2.11]”

  * fix neo4j retrieving relation properties (#15111) (#15108)

### `llama-index-llms-vllm` [0.1.9]

Section titled “llama-index-llms-vllm [0.1.9]”

  * Update base.py to use @atexit for cleanup (#15047)

### `llama-index-vector-stores-pinecone` [0.1.9]

Section titled “llama-index-vector-stores-pinecone [0.1.9]”

  * bump pinecone client version deps (#15121)

### `llama-index-vector-stores-redis` [0.2.1]

Section titled “llama-index-vector-stores-redis [0.2.1]”

  * Handle nested MetadataFilters for Redis vector store (#15093)

### `llama-index-vector-stores-wordlift` [0.2.0]

Section titled “llama-index-vector-stores-wordlift [0.2.0]”

  * Update WordLift Vector Store to use new client package (#15045)

## [2024-07-31]

Section titled “[2024-07-31]”

### `llama-index-core` [0.10.59]

Section titled “llama-index-core [0.10.59]”

  * Introduce `Workflow`s for event-driven orchestration (#15067)
  * Added feature to context chat engine allowing previous chunks to be inserted into the current context window (#14889)
  * MLflow Integration added to docs (#14977)
  * docs(literalai): add Literal AI integration to documentation (#15023)
  * expand span coverage for query pipeline (#14997)
  * make re-raising error skip constructor during `asyncio_run()` (#14970)

### `llama-index-embeddings-ollama` [0.1.3]

Section titled “llama-index-embeddings-ollama [0.1.3]”

  * Add proper async embedding support

### `llama-index-embeddings-textembed` [0.0.1]

Section titled “llama-index-embeddings-textembed [0.0.1]”

  * add support for textembed embedding (#14968)

### `llama-index-graph-stores-falkordb` [0.1.5]

Section titled “llama-index-graph-stores-falkordb [0.1.5]”

  * initial implementation FalkorDBPropertyGraphStore (#14936)

### `llama-index-llms-azure-inference` [0.1.1]

Section titled “llama-index-llms-azure-inference [0.1.1]”

  * Fix: Azure AI inference integration support for tools (#15044)

### `llama-index-llms-fireworks` [0.1.7]

Section titled “llama-index-llms-fireworks [0.1.7]”

  * Updates to Default model for support for function calling (#15046)

### `llama-index-llms-ollama` [0.2.2]

Section titled “llama-index-llms-ollama [0.2.2]”

  * toggle for ollama function calling (#14972)
  * Add function calling for Ollama (#14948)

### `llama-index-llms-openllm` [0.2.0]

Section titled “llama-index-llms-openllm [0.2.0]”

  * update to OpenLLM 0.6 (#14935)

### `llama-index-packs-longrag` [0.1.0]

Section titled “llama-index-packs-longrag [0.1.0]”

  * Adds a LlamaPack that implements LongRAG (#14916)

### `llama-index-postprocessor-tei-rerank` [0.1.0]

Section titled “llama-index-postprocessor-tei-rerank [0.1.0]”

  * Support for Re-Ranker via Text Embedding Interface (#15063)

### `llama-index-readers-confluence` [0.1.7]

Section titled “llama-index-readers-confluence [0.1.7]”

  * confluence reader sort auth parameters priority (#14905)

### `llama-index-readers-file` [0.1.31]

Section titled “llama-index-readers-file [0.1.31]”

  * UnstructuredReader use filename as ID (#14946)

### `llama-index-readers-gitlab` [0.1.0]

Section titled “llama-index-readers-gitlab [0.1.0]”

  * Add GitLab reader integration (#15030)

### `llama-index-readers-google` [0.2.11]

Section titled “llama-index-readers-google [0.2.11]”

  * Fix issue with average ratings being a float vs an int (#15070)

### `llama-index-retrievers-bm25` [0.2.2]

Section titled “llama-index-retrievers-bm25 [0.2.2]”

  * use proper stemmer in bm25 tokenize (#14965)

### `llama-index-vector-stores-azureaisearch` [0.1.13]

Section titled “llama-index-vector-stores-azureaisearch [0.1.13]”

  * Fix issue with deleting non-existent index (#14949)

### `llama-index-vector-stores-elasticsearch` [0.2.5]

Section titled “llama-index-vector-stores-elasticsearch [0.2.5]”

  * disable embeddings for sparse strategy (#15032)

### `llama-index-vector-stores-kdbai` [0.2.0]

Section titled “llama-index-vector-stores-kdbai [0.2.0]”

  * Update default sparse encoder for Hybrid search (#15019)

### `llama-index-vector-stores-milvus` [0.1.22]

Section titled “llama-index-vector-stores-milvus [0.1.22]”

  * Enhance MilvusVectorStore with flexible index management for overwriting (#15058)

### `llama-index-vector-stores-postgres` [0.1.13]

Section titled “llama-index-vector-stores-postgres [0.1.13]”

  * Adds option to construct PGVectorStore with a HNSW index (#15024)

## [2024-07-24]

Section titled “[2024-07-24]”

### `llama-index-core` [0.10.58]

Section titled “llama-index-core [0.10.58]”

  * Fix: Token counter expecting response.raw as dict, got ChatCompletionChunk (#14937)
  * Return proper tool outputs per agent step instead of all (#14885)
  * Minor bug fixes to async structured streaming (#14925)

### `llama-index-llms-fireworks` [0.1.6]

Section titled “llama-index-llms-fireworks [0.1.6]”

  * fireworks ai llama3.1 support (#14914)

### `llama-index-multi-modal-llms-anthropic` [0.1.6]

Section titled “llama-index-multi-modal-llms-anthropic [0.1.6]”

  * Add claude 3.5 sonnet to multi modal llms (#14932)

### `llama-index-retrievers-bm25` [0.2.1]

Section titled “llama-index-retrievers-bm25 [0.2.1]”

  * 🐞 fix(integrations): BM25Retriever persist missing arg similarity_top_k (#14933)

### `llama-index-retrievers-vertexai-search` [0.1.0]

Section titled “llama-index-retrievers-vertexai-search [0.1.0]”

  * Llamaindex retriever for Vertex AI Search (#14913)

### `llama-index-vector-stores-deeplake` [0.1.5]

Section titled “llama-index-vector-stores-deeplake [0.1.5]”

  * Improved `deeplake.get_nodes()` performance (#14920)

### `llama-index-vector-stores-elasticsearch` [0.2.3]

Section titled “llama-index-vector-stores-elasticsearch [0.2.3]”

  * Bugfix: Don’t pass empty list of embeddings to elasticsearch store when using sparse strategy (#14918)

### `llama-index-vector-stores-lindorm` [0.1.0]

Section titled “llama-index-vector-stores-lindorm [0.1.0]”

  * Add vector store integration of lindorm (#14623)

### `llama-index-vector-stores-qdrant` [0.2.14]

Section titled “llama-index-vector-stores-qdrant [0.2.14]”

  * feat: allow to limit how many elements retrieve (qdrant) (#14904)

## [2024-07-22]

Section titled “[2024-07-22]”

### `llama-index-core` [0.10.57]

Section titled “llama-index-core [0.10.57]”

  * Add an optional parameter similarity_score to VectorContextRetrieve… (#14831)
  * add property extraction (using property names and optional descriptions) for KGs (#14707)
  * able to attach output classes to LLMs (#14747)
  * Add streaming for tool calling / structured extraction (#14759)
  * fix from removing private variables when copying/pickling (#14860)
  * Fix empty array being send to vector store in ingestion pipeline (#14859)
  * optimize ingestion pipeline deduping (#14858)
  * Add an optional parameter similarity_score to VectorContextRetriever (#14831)

### `llama-index-llms-azure-openai` [0.1.10]

Section titled “llama-index-llms-azure-openai [0.1.10]”

  * Bugfix: AzureOpenAI may fail with custom azure_ad_token_provider (#14869)

### `llama-index-llms-bedrock-converse` [0.1.5]

Section titled “llama-index-llms-bedrock-converse [0.1.5]”

  * feat: ✨ Implement async functionality in BedrockConverse (#14326)

### `llama-index-llms-langchain` [0.3.0]

Section titled “llama-index-llms-langchain [0.3.0]”

  * make some dependencies optional
  * bump langchain version in integration (#14879)

### `llama-index-llms-ollama` [0.1.6]

Section titled “llama-index-llms-ollama [0.1.6]”

  * Bugfix: ollama streaming response (#14830)

### `llama-index-multi-modal-llms-anthropic` [0.1.5]

Section titled “llama-index-multi-modal-llms-anthropic [0.1.5]”

  * align deps (#14850)

### `llama-index-readers-notion` [0.1.10]

Section titled “llama-index-readers-notion [0.1.10]”

  * update notion reader to handle duplicate pages, database+page ids (#14861)

### `llama-index-vector-stores-milvus` [0.1.21]

Section titled “llama-index-vector-stores-milvus [0.1.21]”

  * Implements delete_nodes() and clear() for Weviate, Opensearch, Milvus, Postgres, and Pinecone Vector Stores (#14800)

### `llama-index-vector-stores-mongodb` [0.1.8]

Section titled “llama-index-vector-stores-mongodb [0.1.8]”

  * MongoDB Atlas Vector Search: Enhanced Metadata Filtering (#14856)

### `llama-index-vector-stores-opensearch` [0.1.13]

Section titled “llama-index-vector-stores-opensearch [0.1.13]”

  * Implements delete_nodes() and clear() for Weviate, Opensearch, Milvus, Postgres, and Pinecone Vector Stores (#14800)

### `llama-index-vector-stores-pinecone` [0.1.8]

Section titled “llama-index-vector-stores-pinecone [0.1.8]”

  * Implements delete_nodes() and clear() for Weviate, Opensearch, Milvus, Postgres, and Pinecone Vector Stores (#14800)

### `llama-index-vector-stores-postgres` [0.1.12]

Section titled “llama-index-vector-stores-postgres [0.1.12]”

  * Implements delete_nodes() and clear() for Weviate, Opensearch, Milvus, Postgres, and Pinecone Vector Stores (#14800)

### `llama-index-vector-stores-weaviate` [1.0.2]

Section titled “llama-index-vector-stores-weaviate [1.0.2]”

  * Implements delete_nodes() and clear() for Weviate, Opensearch, Milvus, Postgres, and Pinecone Vector Stores (#14800)

## [2024-07-19]

Section titled “[2024-07-19]”

### `llama-index-core` [0.10.56]

Section titled “llama-index-core [0.10.56]”

  * Fixing the issue where the _apply_node_postprocessors function needs QueryBundle (#14839)
  * Add Context-Only Response Synthesizer (#14439)
  * Fix AgentRunner AgentRunStepStartEvent dispatch (#14828)
  * Improve output format system prompt in ReAct agent (#14814)
  * Remove double curly replacing from output parser utils (#14735)
  * Update simple_summarize.py (#14714)

### `llama-index-tools-azure-code-interpreter` [0.2.0]

Section titled “llama-index-tools-azure-code-interpreter [0.2.0]”

  * chore: read AZURE_POOL_MANAGEMENT_ENDPOINT from env vars (#14732)

### `llama-index-llms-azure-inference` [0.1.0]

Section titled “llama-index-llms-azure-inference [0.1.0]”

  * Azure AI Inference integration (#14672)

### `llama-index-embeddings-azure-inference` [0.1.0]

Section titled “llama-index-embeddings-azure-inference [0.1.0]”

  * Azure AI Inference integration (#14672)

### `llama-index-llms-bedrock-converse` [0.1.5]

Section titled “llama-index-llms-bedrock-converse [0.1.5]”

  * feat: ✨ Implement async functionality in BedrockConverse (#14326)

### `llama-index-embeddings-yandexgpt` [0.1.5]

Section titled “llama-index-embeddings-yandexgpt [0.1.5]”

  * Add new integration for YandexGPT Embedding Model (#14313)

### `llama-index-tools-google` [0.1.6]

Section titled “llama-index-tools-google [0.1.6]”

  * Update docstring for gmailtoolspec’s search_messages tool (#14840)

### `llama-index-postprocessor-nvidia-rerank` [0.1.5]

Section titled “llama-index-postprocessor-nvidia-rerank [0.1.5]”

  * add support for nvidia/nv-rerankqa-mistral-4b-v3 (#14844)

### `llama-index-embeddings-openai` [0.1.11]

Section titled “llama-index-embeddings-openai [0.1.11]”

  * Fix OpenAI Embedding async client bug (#14835)

### `llama-index-embeddings-azure-openai` [0.1.11]

Section titled “llama-index-embeddings-azure-openai [0.1.11]”

  * Fix Azure OpenAI LLM and Embedding async client bug (#14833)

### `llama-index-llms-azure-openai` [0.1.9]

Section titled “llama-index-llms-azure-openai [0.1.9]”

  * Fix Azure OpenAI LLM and Embedding async client bug (#14833)

### `llama-index-multi-modal-llms-openai` [0.1.8]

Section titled “llama-index-multi-modal-llms-openai [0.1.8]”

  * Add support for gpt-4o-mini (#14820)

### `llama-index-llms-openai` [0.1.26]

Section titled “llama-index-llms-openai [0.1.26]”

  * Add support for gpt-4o-mini (#14820)

### `llama-index-llms-mistralai` [0.1.18]

Section titled “llama-index-llms-mistralai [0.1.18]”

  * Add support for mistralai nemo model (#14819)

### `llama-index-graph-stores-neo4j` [0.2.8]

Section titled “llama-index-graph-stores-neo4j [0.2.8]”

  * Fix bug when sanitize is used in neo4j property graph (#14812)
  * Add filter to get_triples in neo4j (#14811)

### `llama-index-vector-stores-azureaisearch` [0.1.12]

Section titled “llama-index-vector-stores-azureaisearch [0.1.12]”

  * feat: add nested filters for azureaisearch (#14795)

### `llama-index-vector-stores-qdrant` [0.2.13]

Section titled “llama-index-vector-stores-qdrant [0.2.13]”

  * feat: Add NOT IN filter for Qdrant vector store (#14791)

### `llama-index-vector-stores-azureaisearch` [0.1.11]

Section titled “llama-index-vector-stores-azureaisearch [0.1.11]”

  * feat: add azureaisearch supported conditions (#14787)
  * feat: azureaisearch support collection string (#14712)

### `llama-index-tools-weather` [0.1.4]

Section titled “llama-index-tools-weather [0.1.4]”

  * Fix OpenWeatherMapToolSpec.forecast_tommorrow_at_location (#14745)

### `llama-index-readers-microsoft-sharepoint` [0.2.6]

Section titled “llama-index-readers-microsoft-sharepoint [0.2.6]”

  * follow odata.nextLink (#14708)

### `llama-index-vector-stores-qdrant` [0.2.12]

Section titled “llama-index-vector-stores-qdrant [0.2.12]”

  * Adds Quantization option to QdrantVectorStore (#14740)

### `llama-index-vector-stores-azureaisearch` [0.1.10]

Section titled “llama-index-vector-stores-azureaisearch [0.1.10]”

  * feat: improve azureai search deleting (#14693)

### `llama-index-agent-openai` [0.2.9]

Section titled “llama-index-agent-openai [0.2.9]”

  * fix: tools are required for attachments in openai api (#14609)

### `llama-index-readers-box` [0.1.0]

Section titled “llama-index-readers-box [0.1.0]”

  * new integration

### `llama-index-embeddings-fastembed` [0.1.6]

Section titled “llama-index-embeddings-fastembed [0.1.6]”

  * fix fastembed python version (#14710)

## [2024-07-11]

Section titled “[2024-07-11]”

### `llama-index-core` [0.10.55]

Section titled “llama-index-core [0.10.55]”

  * Various docs updates

### `llama-index-llms-cleanlab` [0.1.1]

Section titled “llama-index-llms-cleanlab [0.1.1]”

  * Add user configurations for Cleanlab LLM integration (#14676)

### `llama-index-readers-file` [0.1.30]

Section titled “llama-index-readers-file [0.1.30]”

  * race between concurrent pptx readers over a single temp filename (#14686)

### `llama-index-tools-exa` [0.1.4]

Section titled “llama-index-tools-exa [0.1.4]”

  * changes to Exa search tool getting started and example notebook (#14690)

## [2024-07-10]

Section titled “[2024-07-10]”

### `llama-index-core` [0.10.54]

Section titled “llama-index-core [0.10.54]”

  * fix: update operator logic for simple vector store filter (#14674)
  * Add AgentOps integration (#13935)

### `llama-index-embeddings-fastembed` [0.1.5]

Section titled “llama-index-embeddings-fastembed [0.1.5]”

  * chore: update required python version in Qdrant fastembed package (#14677)

### `llama-index-embeddings-huggingface-optimum-intel` [0.1.6]

Section titled “llama-index-embeddings-huggingface-optimum-intel [0.1.6]”

  * Bump version llama-index-embeddings-huggingface-optimum-intel (#14670)

### `llama-index-vector-stores-elasticsearch` [0.2.2]

Section titled “llama-index-vector-stores-elasticsearch [0.2.2]”

  * Added support for custom index settings (#14655)

### `llama-index-callbacks-agentops` [0.1.0]

Section titled “llama-index-callbacks-agentops [0.1.0]”

  * Initial release

### `llama-index-indices-managed-vertexai` [0.0.2]

Section titled “llama-index-indices-managed-vertexai [0.0.2]”

  * Fix #14637 Llamaindex managed Vertex AI index needs to be updated. (#14641)

### `llama-index-readers-file` [0.1.29]

Section titled “llama-index-readers-file [0.1.29]”

  * fix unstructured import in simple file reader (#14642)

## [2024-07-08]

Section titled “[2024-07-08]”

### `llama-index-core` [0.10.53]

Section titled “llama-index-core [0.10.53]”

  * fix handling react usage in `llm.predict_and_call` for llama-agents (#14556)
  * add the missing arg verbose when `ReActAgent` calling `super().__init__` (#14565)
  * fix `llama-index-core\llama_index\core\node_parser\text\utils.py` error when use IngestionPipeline parallel (#14560)
  * deprecate `KnowledgeGraphIndex`, tweak docs (#14575)
  * Fix `ChatSummaryMemoryBuffer` fails to summary chat history with tool callings (#14563)
  * Added `DynamicLLMPathExtractor` for Entity Detection With a Schema inferred by LLMs on the fly (#14566)
  * add cloud document converter (#14608)
  * fix KnowledgeGraphIndex arg ‘kg_triple_extract_template’ typo error (#14619)
  * Fix: Update `UnstructuredElementNodeParser` due to change in unstructured (#14606)
  * Update ReAct Step to solve issue with incomplete generation (#14587)

### `llama-index-callbacks-promptlayer` [0.1.3]

Section titled “llama-index-callbacks-promptlayer [0.1.3]”

  * Conditions logging to promptlayer on successful request (#14632)

### `llama-index-embeddings-databricks` [0.1.0]

Section titled “llama-index-embeddings-databricks [0.1.0]”

  * Add integration embeddings databricks (#14590)

### `llama-index-llms-ai21` [0.3.1]

Section titled “llama-index-llms-ai21 [0.3.1]”

  * Fix MessageRole import from the wrong package in AI21 Package (#14596)

### `llama-index-llms-bedrock` [0.1.12]

Section titled “llama-index-llms-bedrock [0.1.12]”

  * handle empty response in Bedrock AnthropicProvider (#14479)
  * add claude 3.5 sonnet support to Bedrock InvokeAPI (#14594)

### `llama-index-llms-bedrock-converse` [0.1.4]

Section titled “llama-index-llms-bedrock-converse [0.1.4]”

  * Fix Bedrock Converse’s tool use blocks, when there are multiple consecutive function calls (#14386)

### `llama-index-llms-optimum-intel` [0.1.0]

Section titled “llama-index-llms-optimum-intel [0.1.0]”

  * add optimum intel with ipex backend to llama-index-integration (#14553)

### `llama-index-llms-qianfan` [0.1.0]

Section titled “llama-index-llms-qianfan [0.1.0]”

  * add baidu-qianfan llm (#14414)

### `llama-index-llms-text-generation-inference` [0.1.4]

Section titled “llama-index-llms-text-generation-inference [0.1.4]”

  * fix: crash LLMMetadata in model name lookup (#14569)
  * Remove hf embeddings dep from text-embeddings-inference (#14592)

### `llama-index-llms-yi` [0.1.1]

Section titled “llama-index-llms-yi [0.1.1]”

  * update yi llm context_window (#14578)

### `llama-index-readers-file` [0.1.28]

Section titled “llama-index-readers-file [0.1.28]”

  * add fs arg to PandasExcelReader.load_data (#14554)
  * UnstructuredReader enhancements (#14390)

### `llama-index-readers-web` [0.1.22]

Section titled “llama-index-readers-web [0.1.22]”

  * nit: firecrawl fixes for creating documents (#14579)

### `llama-index-retrievers-bm25` [0.2.0]

Section titled “llama-index-retrievers-bm25 [0.2.0]”

  * Update BM25Retriever to use newer (and faster) bm25s library #(14581)

### `llama-index-vector-stores-qdrant` [0.2.11]

Section titled “llama-index-vector-stores-qdrant [0.2.11]”

  * refactor: Don’t swallow exceptions from Qdrant collection_exists (#14564)
  * add support for qdrant bm42, setting sparse + dense configs (#14577)

## [2024-07-03]

Section titled “[2024-07-03]”

### `llama-index-core` [0.10.52]

Section titled “llama-index-core [0.10.52]”

  * fix file reader path bug on windows (#14537)
  * follow up with kwargs propagation in colbert index due to change in parent class (#14522)
  * deprecate query pipeline agent in favor of FnAgentWorker (#14525O)

### `llama-index-callbacks-arize-phoenix` [0.1.6]

Section titled “llama-index-callbacks-arize-phoenix [0.1.6]”

  * support latest version of arize #14526

### `llama-index-embeddings-litellm` [0.1.0]

Section titled “llama-index-embeddings-litellm [0.1.0]”

  * Add support for LiteLLM Proxy Server for embeddings (#14523)

### `llama-index-finetuning` [0.1.10]

Section titled “llama-index-finetuning [0.1.10]”

  * Adding device choice from sentence_transformers (#14546)

### `llama-index-graph-stores-neo4` [0.2.7]

Section titled “llama-index-graph-stores-neo4 [0.2.7]”

  * Fixed ordering of returned nodes on vector queries (#14461)

### `llama-index-llms-bedrock` [0.1.10]

Section titled “llama-index-llms-bedrock [0.1.10]”

  * handle empty response in Bedrock AnthropicProvider (#14479)

### `llama-index-llms-bedrock-converse` [0.1.4]

Section titled “llama-index-llms-bedrock-converse [0.1.4]”

  * Fix Bedrock Converse’s join_two_dicts function when a new string kwarg is added (#14548)

### `llama-index-llms-upstage` [0.1.4]

Section titled “llama-index-llms-upstage [0.1.4]”

  * Add upstage tokenizer and token counting method (#14502)

### `llama-index-readers-azstorage-blob` [0.1.7]

Section titled “llama-index-readers-azstorage-blob [0.1.7]”

  * Fix bug with getting object name for blobs (#14547)

### `llama-index-readers-file` [0.1.26]

Section titled “llama-index-readers-file [0.1.26]”

  * Pandas excel reader load data fix for appending documents (#14501)

### `llama-index-readers-iceberg` [0.1.0]

Section titled “llama-index-readers-iceberg [0.1.0]”

  * Add Iceberg Reader integration to LLamaIndex (#14477)

### `llama-index-readers-notion` [0.1.8]

Section titled “llama-index-readers-notion [0.1.8]”

  * Added retries (#14488)
  * add `list_databases` method (#14488)

### `llama-index-readers-slack` [0.1.5]

Section titled “llama-index-readers-slack [0.1.5]”

  * Enhance SlackReader to fetch Channel IDs from Channel Names/Patterns (#14429)

### `llama-index-readers-web` [0.1.21]

Section titled “llama-index-readers-web [0.1.21]”

  * Add API url to firecrawl reader (#14452)

### `llama-index-retrievers-bm25` [0.1.5]

Section titled “llama-index-retrievers-bm25 [0.1.5]”

  * fix score in nodes returned by the BM25 retriever (#14495)

### `llama-index-vector-stores-azureaisearch` [0.1.9]

Section titled “llama-index-vector-stores-azureaisearch [0.1.9]”

  * add async methods to azure ai search (#14496)

### `llama-index-vector-stores-kdbai` [0.1.8]

Section titled “llama-index-vector-stores-kdbai [0.1.8]”

  * Kdbai rest compatible (#14511)

### `llama-index-vector-stores-mongodb` [0.1.6]

Section titled “llama-index-vector-stores-mongodb [0.1.6]”

  * Adds Hybrid and Full-Text Search to MongoDBAtlasVectorSearch (#14490)

## [2024-06-28]

Section titled “[2024-06-28]”

### `llama-index-core` [0.10.51]

Section titled “llama-index-core [0.10.51]”

  * fixed issue with function calling llms and empty tool calls (#14453)
  * Fix ChatMessage not considered as stringable in query pipeline (#14378)
  * Update schema llm path extractor to also take a list of valid triples (#14357)
  * Pass the kwargs on when `build_index_from_nodes` (#14341)

### `llama-index-agent-dashscope` [0.1.0]

Section titled “llama-index-agent-dashscope [0.1.0]”

  * Add Alibaba Cloud dashscope agent (#14318)

### `llama-index-graph-stores-neo4j` [0.2.6]

Section titled “llama-index-graph-stores-neo4j [0.2.6]”

  * Add MetadataFilters to neo4j_property_graph (#14362)

### `llama-index-llms-nvidia` [0.1.4]

Section titled “llama-index-llms-nvidia [0.1.4]”

  * add known context lengths for hosted models (#14436)

### `llama-index-llms-perplexity` [0.1.4]

Section titled “llama-index-llms-perplexity [0.1.4]”

  * update available models (#14409)

### `llama-index-llms-predibase` [0.1.6]

Section titled “llama-index-llms-predibase [0.1.6]”

  * Better error handling for invalid API token (#14440)

### `llama-index-llms-yi` [0.1.0]

Section titled “llama-index-llms-yi [0.1.0]”

  * Integrate Yi model (#14353)

### `llama-index-readers-google` [0.2.9]

Section titled “llama-index-readers-google [0.2.9]”

  * Creates Data Loader for Google Chat (#14397)

### `llama-index-readers-s3` [0.1.10]

Section titled “llama-index-readers-s3 [0.1.10]”

  * Invalidate s3fs cache in S3Reader (#14441)

### `llama-index-readers-structured-data` [0.1.0]

Section titled “llama-index-readers-structured-data [0.1.0]”

  * Add StructuredDataReader support for xlsx, csv, json and jsonl (#14369)

### `llama-index-tools-jina` [0.1.0]

Section titled “llama-index-tools-jina [0.1.0]”

  * Integrating a new tool called jina search (#14317)

### `llama-index-vector-stores-astradb` [0.1.8]

Section titled “llama-index-vector-stores-astradb [0.1.8]”

  * Update Astra DB vector store to use modern astrapy library (#14407)

### `llama-index-vector-stores-chromadb` [0.1.10]

Section titled “llama-index-vector-stores-chromadb [0.1.10]”

  * Fix the index accessing of ids of chroma get (#14434)

### `llama-index-vector-stores-deeplake` [0.1.4]

Section titled “llama-index-vector-stores-deeplake [0.1.4]”

  * Implemented delete_nodes() and clear() in deeplake vector store (#14457)
  * Implemented get_nodes() in deeplake vector store (#14388)

### `llama-index-vector-stores-elasticsearch` [0.2.1]

Section titled “llama-index-vector-stores-elasticsearch [0.2.1]”

  * Add support for dynamic metadata fields in Elasticsearch index creation (#14431)

### `llama-index-vector-stores-kdbai` [0.1.7]

Section titled “llama-index-vector-stores-kdbai [0.1.7]”

  * Kdbai version compatible (#14402)

## [2024-06-24]

Section titled “[2024-06-24]”

### `llama-index-core` [0.10.50]

Section titled “llama-index-core [0.10.50]”

  * added dead simple `FnAgentWorker` for custom agents (#14329)
  * Pass the kwargs on when build_index_from_nodes (#14341)
  * make async utils a bit more robust to nested async (#14356)

### `llama-index-llms-upstage` [0.1.3]

Section titled “llama-index-llms-upstage [0.1.3]”

  * every llm is a chat model (#14334)

### `llama-index-packs-rag-evaluator` [0.1.5]

Section titled “llama-index-packs-rag-evaluator [0.1.5]”

  * added possibility to run local embedding model in RAG evaluation packages (#14352)

## [2024-06-23]

Section titled “[2024-06-23]”

### `llama-index-core` [0.10.49]

Section titled “llama-index-core [0.10.49]”

  * Improvements to `llama-cloud` and client dependencies (#14254)

### `llama-index-indices-managed-llama-cloud` [0.2.1]

Section titled “llama-index-indices-managed-llama-cloud [0.2.1]”

  * Improve the interface and client interactions in `LlamaCloudIndex` (#14254)

### `llama-index-llms-bedrock-converse` [0.1.3]

Section titled “llama-index-llms-bedrock-converse [0.1.3]”

  * add claude sonnet 3.5 to bedrock converse (#14306)

### `llama-index-llms-upstage` [0.1.2]

Section titled “llama-index-llms-upstage [0.1.2]”

  * set default context size (#14293)
  * add api_key alias on upstage llm and embeddings (#14233)

### `llama-index-storage-kvstore-azure` [0.1.2]

Section titled “llama-index-storage-kvstore-azure [0.1.2]”

  * Optimized inserts (#14321)

### `llama-index-utils-azure` [0.1.1]

Section titled “llama-index-utils-azure [0.1.1]”

  * azure_table_storage params bug (#14182)

### `llama-index-vector-stores-neo4jvector` [0.1.6]

Section titled “llama-index-vector-stores-neo4jvector [0.1.6]”

  * Add neo4j client method (#14314)

## [2024-06-21]

Section titled “[2024-06-21]”

### `llama-index-core` [0.10.48]

Section titled “llama-index-core [0.10.48]”

  * Improve efficiency of average precision (#14260)
  * add crewai + llamaindex cookbook (#14266)
  * Add mimetype field to TextNode (#14279)
  * Improve IBM watsonx.ai docs (#14271)
  * Updated frontpage of docs, added agents guide, and more (#14089)

### `llama-index-llms-anthropic` [0.1.14]

Section titled “llama-index-llms-anthropic [0.1.14]”

  * Add support for claude 3.5 (#14277)

### `llama-index-llms-bedrock-converse` [0.1.4]

Section titled “llama-index-llms-bedrock-converse [0.1.4]”

  * Implement Bedrock Converse API for function calling (#14055)

## [2024-06-19]

Section titled “[2024-06-19]”

### `llama-index-core` [0.10.47]

Section titled “llama-index-core [0.10.47]”

  * added average precision as a retrieval metric (#14189)
  * added `.show_jupyter_graph()` method visualizing default simple graph_store in jupyter notebooks (#14104)
  * corrected the behaviour of nltk file lookup (#14040)
  * Added helper args to generate_qa_pairs (#14054)
  * Add new chunking semantic chunking method: double-pass merging (#13629)
  * enable stepwise execution of query pipelines (#14117)
  * Replace tenacity upper limit by only rejecting 8.4.0 (#14218)
  * propagate error_on_no_tool_call kwarg in `llm.predict_and_call()` (#14253)
  * in query pipeline, avoid casting nodes as strings and use `get_content()` instead (#14242)
  * Fix NLSQLTableQueryEngine response metadata (#14169)
  * do not overwrite relations in default simple property graph (#14244)

### `llama-index-embeddings-ipex-llm` [0.1.5]

Section titled “llama-index-embeddings-ipex-llm [0.1.5]”

  * Enable selecting Intel GPU for ipex embedding integrations (#14214)

### `llama-index-embeddings-mixedbreadai` [0.1.0]

Section titled “llama-index-embeddings-mixedbreadai [0.1.0]”

  * add mixedbread ai integration (#14161)

### `llama-index-graph-stores-neo4j` [0.2.5]

Section titled “llama-index-graph-stores-neo4j [0.2.5]”

  * Add default node property to neo4j upsert relations (#14095)

### `llama-index-indices-managed-postgresml` [0.3.0]

Section titled “llama-index-indices-managed-postgresml [0.3.0]”

  * Added re-ranking into the PostgresML Managed Index (#14134)

### `llama-index-llms-ai21` [0.3.0]

Section titled “llama-index-llms-ai21 [0.3.0]”

  * use async AI21 client for async methods (#14193)

### `llama-index-llms-bedrock-converse` [0.1.2]

Section titled “llama-index-llms-bedrock-converse [0.1.2]”

  * Added (fake) async calls to avoid errors (#14241)

### `llama-index-llms-deepinfra` [0.1.3]

Section titled “llama-index-llms-deepinfra [0.1.3]”

  * Add function calling to deep infra llm (#14127)

### `llama-index-llms-ipex-llm` [0.1.8]

Section titled “llama-index-llms-ipex-llm [0.1.8]”

  * Enable selecting Intel GPU for ipex embedding integrations (#14214)

### `llama-index-llms-oci-genai` [0.1.1]

Section titled “llama-index-llms-oci-genai [0.1.1]”

  * add command r support oci genai (#14080)

### `llama-index-llms-premai` [0.1.7]

Section titled “llama-index-llms-premai [0.1.7]”

  * Prem AI Templates Llama Index support (#14105)

### `llama-index-llms-you` [0.1.0]

Section titled “llama-index-llms-you [0.1.0]”

  * Integrate You.com conversational APIs (#14207)

### `llama-index-readers-mongodb` [0.1.8]

Section titled “llama-index-readers-mongodb [0.1.8]”

  * Add metadata field “collection_name” to SimpleMongoReader (#14245)

### `llama-index-readers-pdf-marker` [0.1.0]

Section titled “llama-index-readers-pdf-marker [0.1.0]”

  * add marker-pdf reader (#14099)

### `llama-index-readers-upstage` [0.1.0]

Section titled “llama-index-readers-upstage [0.1.0]”

  * Added upstage as a reader (#13415)

### `llama-index-postprocessor-mixedbreadai-rerank` [0.1.0]

Section titled “llama-index-postprocessor-mixedbreadai-rerank [0.1.0]”

  * add mixedbread ai integration (#14161)

### `llama-index-vector-stores-lancedb` [0.1.6]

Section titled “llama-index-vector-stores-lancedb [0.1.6]”

  * LanceDB: code cleanup, minor updates (#14077)

### `llama-index-vector-stores-opensearch` [0.1.12]

Section titled “llama-index-vector-stores-opensearch [0.1.12]”

  * add option to customize default OpenSearch Client and Engine (#14249)

## [2024-06-17]

Section titled “[2024-06-17]”

### `llama-index-core`[0.10.46]

Section titled “llama-index-core[0.10.46]”

  * Fix Pin tenacity and numpy in core (#14203)
  * Add precision and recall metrics (#14170)
  * Enable Function calling and agent runner for Vertex AI (#14088)
  * Fix for batch_gather (#14162)

### `llama-index-utils-huggingface` [0.1.1]

Section titled “llama-index-utils-huggingface [0.1.1]”

  * Remove sentence-transformers dependency from HuggingFace utils package (#14204)

### `llama-index-finetuning` [0.1.8]

Section titled “llama-index-finetuning [0.1.8]”

  * Add MistralAI Finetuning API support (#14101)

### `llama-index-llms-mistralai` [0.1.16]

Section titled “llama-index-llms-mistralai [0.1.16]”

  * Update MistralAI (#14199)

### `llama-index-llms-bedrock-converse` [0.1.0]

Section titled “llama-index-llms-bedrock-converse [0.1.0]”

  * fix: 🐛 Fix Bedrock Converse’ pyproject.toml for the PyPI release (#14197)

### `llama-index-utils-azure` [0.1.1]

Section titled “llama-index-utils-azure [0.1.1]”

  * Use typical include llama_index/ (#14196)
  * Feature/azure_table_storage (#14182)

### `llama-index-embeddings-nvidia` [0.1.4]

Section titled “llama-index-embeddings-nvidia [0.1.4]”

  * add support for nvidia/nv-embed-v1 (<https://huggingface.co/nvidia/NV-Embed-v1>) (#14194)

### `llama-index-retrievers-you` [0.1.3]

Section titled “llama-index-retrievers-you [0.1.3]”

  * add news retriever (#13934)

### `llama-index-storage-kvstore-azure` [0.1.1]

Section titled “llama-index-storage-kvstore-azure [0.1.1]”

  * Fixes a bug where there is a missing await. (#14177)

### `llama-index-embeddings-nomic` [0.4.0post1]

Section titled “llama-index-embeddings-nomic [0.4.0post1]”

  * Restore Nomic Embed einops dependency (#14176)

### `llama-index-retrievers-bm25` [0.1.4]

Section titled “llama-index-retrievers-bm25 [0.1.4]”

  * Changing BM25Retriever _retrieve to use numpy methods (#14015)

### `llama-index-llms-gemini` [0.1.11]

Section titled “llama-index-llms-gemini [0.1.11]”

  * Add missing @llm_chat_callback() to Gemini.stream_chat (#14166)

### `llama-index-llms-vertex` [0.2.0]

Section titled “llama-index-llms-vertex [0.2.0]”

  * Enable Function calling and agent runner for Vertex AI (#14088)

### `llama-index-vector-stores-opensearch` [0.1.11]

Section titled “llama-index-vector-stores-opensearch [0.1.11]”

  * feat: support VectorStoreQueryMode.TEXT_SEARCH on OpenSearch VectorStore (#14153)

## [2024-06-14]

Section titled “[2024-06-14]”

### `llama-index-core` [0.10.45]

Section titled “llama-index-core [0.10.45]”

  * Fix parsing sql query.py (#14109)
  * Implement NDCG metric (#14100)
  * Fixed System Prompts for Structured Generation (#14026)
  * Split HuggingFace embeddings in HuggingFace API and TextGenerationInference packages (#14013)
  * Add PandasExcelReader class for parsing excel files (#13991)
  * feat: add spans to ingestion pipeline (#14062)

### `llama-index-vector-stores-qdrant` [0.2.10]

Section titled “llama-index-vector-stores-qdrant [0.2.10]”

  * Fix Qdrant nodes (#14149)

### `llama-index-readers-mongodb` [0.1.7]

Section titled “llama-index-readers-mongodb [0.1.7]”

  * Fixes TypeError: sequence item : expected str instance, int found

### `llama-index-indices-managed-vertexai` [0.0.1]

Section titled “llama-index-indices-managed-vertexai [0.0.1]”

  * feat: Add Managed Index for LlamaIndex on Vertex AI for RAG (#13626)

### `llama-index-llms-oci-genai` [0.1.1]

Section titled “llama-index-llms-oci-genai [0.1.1]”

  * Feature/add command r support oci genai (#14080)

### `llama-index-vector-stores-milvus` [0.1.20]

Section titled “llama-index-vector-stores-milvus [0.1.20]”

  * MilvusVectorStore: always include text_key in output_fields (#14076)

### `llama-index-packs-mixture-of-agents` [0.1.0]

Section titled “llama-index-packs-mixture-of-agents [0.1.0]”

  * Add Mixture Of Agents paper implementation (#14112)

### `llama-index-llms-text-generation-inference` [0.1.0]

Section titled “llama-index-llms-text-generation-inference [0.1.0]”

  * Split HuggingFace embeddings in HuggingFace API and TextGenerationInference packages (#14013)

### `llama-index-llms-huggingface-api` [0.1.0]

Section titled “llama-index-llms-huggingface-api [0.1.0]”

  * Split HuggingFace embeddings in HuggingFace API and TextGenerationInference packages (#14013)

### `llama-index-embeddings-huggingface-api` [0.1.0]

Section titled “llama-index-embeddings-huggingface-api [0.1.0]”

  * Split HuggingFace embeddings in HuggingFace API and TextGenerationInference packages (#14013)

### `llama-index-utils-huggingface` [0.1.0]

Section titled “llama-index-utils-huggingface [0.1.0]”

  * Split HuggingFace embeddings in HuggingFace API and TextGenerationInference packages (#14013)

### `llama-index-llms-watsonx` [0.1.8]

Section titled “llama-index-llms-watsonx [0.1.8]”

  * Feat: IBM watsonx.ai llm and embeddings integration (#13600)

### `llama-index-llms-ibm` [0.1.0]

Section titled “llama-index-llms-ibm [0.1.0]”

  * Feat: IBM watsonx.ai llm and embeddings integration (#13600)

### `llama-index-embeddings-ibm` [0.1.0]

Section titled “llama-index-embeddings-ibm [0.1.0]”

  * Feat: IBM watsonx.ai llm and embeddings integration (#13600)

### `llama-index-vector-stores-milvus` [0.1.19]

Section titled “llama-index-vector-stores-milvus [0.1.19]”

  * Fix to milvus filter enum parsing (#14111)

### `llama-index-llms-anthropic` [0.1.13]

Section titled “llama-index-llms-anthropic [0.1.13]”

  * fix anthropic llm calls (#14108)

### `llama-index-storage-index-store-postgres` [0.1.4]

Section titled “llama-index-storage-index-store-postgres [0.1.4]”

  * Wrong mongo name was used instead of Postgres (#14107)

### `llama-index-embeddings-bedrock` [0.2.1]

Section titled “llama-index-embeddings-bedrock [0.2.1]”

  * Remove unnecessary excluded from fields in Bedrock embedding (#14085)

### `llama-index-finetuning` [0.1.7]

Section titled “llama-index-finetuning [0.1.7]”

  * Feature/added trust remote code (#14102)

### `llama-index-readers-file` [0.1.25]

Section titled “llama-index-readers-file [0.1.25]”

  * nit: fix for pandas excel reader (#14086)

### `llama-index-llms-anthropic` [0.1.12]

Section titled “llama-index-llms-anthropic [0.1.12]”

  * Update anthropic dependency to 0.26.2 minimum version (#14091)

### `llama-index-llms-llama-cpp` [0.1.4]

Section titled “llama-index-llms-llama-cpp [0.1.4]”

  * Add support for Llama 3 Instruct prompt format (#14072)

### `llama-index-llms-bedrock-converse` [0.1.8]

Section titled “llama-index-llms-bedrock-converse [0.1.8]”

  * Implement Bedrock Converse API for function calling (#14055)

### `llama-index-vector-stores-postgres` [0.1.11]

Section titled “llama-index-vector-stores-postgres [0.1.11]”

  * fix/postgres-metadata-in-filter-single-elem (#14035)

### `llama-index-readers-file` [0.1.24]

Section titled “llama-index-readers-file [0.1.24]”

  * Add PandasExcelReader class for parsing excel files (#13991)

### `llama-index-embeddings-ipex-llm` [0.1.4]

Section titled “llama-index-embeddings-ipex-llm [0.1.4]”

  * Update dependency of llama-index-embeddings-ipex-llm

### `llama-index-embeddings-gemini` [0.1.8]

Section titled “llama-index-embeddings-gemini [0.1.8]”

  * Add api key as field in Gemini Embedding (#14061)

### `llama-index-vector-stores-milvus` [0.1.18]

Section titled “llama-index-vector-stores-milvus [0.1.18]”

  * Expand milvus vector store filter options (#13961)

## [2024-06-10]

Section titled “[2024-06-10]”

### `llama-index-core` [0.10.44]

Section titled “llama-index-core [0.10.44]”

  * Add WEBP and GIF to supported image types for SimpleDirectoryReader (#14038)
  * refactor: add spans to abstractmethods via mixin (#14003)
  * Adding streaming support for SQLAutoVectorQueryEngine (#13947)
  * add option to specify embed_model to NLSQLTableQueryEngine (#14006)
  * add spans for multimodal LLMs (#13966)
  * change to compact in auto prev next (#13940)
  * feat: add exception events for streaming errors (#13917)
  * feat: add spans for tools (#13916)

### `llama-index-embeddings-azure-openai` [0.1.10]

Section titled “llama-index-embeddings-azure-openai [0.1.10]”

  * Fix error when using azure_ad without setting the API key (#13970)

### `llama-index-embeddings-jinaai` [0.2.0]

Section titled “llama-index-embeddings-jinaai [0.2.0]”

  * add Jina Embeddings MultiModal (#13861)

### `llama-index-embeddings-nomic` [0.3.0]

Section titled “llama-index-embeddings-nomic [0.3.0]”

  * Add Nomic multi modal embeddings (#13920)

### `llama-index-graph-stores-neo4j` [0.2.3]

Section titled “llama-index-graph-stores-neo4j [0.2.3]”

  * ensure cypher returns list before iterating (#13938)

### `llama-index-llms-ai21` [0.2.0]

Section titled “llama-index-llms-ai21 [0.2.0]”

  * Add AI21 Labs Jamba-Instruct Support (#14030)

### `llama-index-llms-deepinfra` [0.1.2]

Section titled “llama-index-llms-deepinfra [0.1.2]”

  * fix(deepinfrallm): default max_tokens (#13998)

### `llama-index-llms-vllm` [0.1.8]

Section titled “llama-index-llms-vllm [0.1.8]”

  * correct `__del__()` Vllm (#14053)

### `llama-index-packs-zenguard` [0.1.0]

Section titled “llama-index-packs-zenguard [0.1.0]”

  * Add ZenGuard llamapack (#13959)

### `llama-index-readers-google` [0.2.7]

Section titled “llama-index-readers-google [0.2.7]”

  * fix how class attributes are set in google drive reader (#14022)
  * Add Google Maps Text Search Reader (#13884)

### `llama-index-readers-jira` [0.1.4]

Section titled “llama-index-readers-jira [0.1.4]”

  * Jira personal access token with hosted instances (#13890)

### `llama-index-readers-mongodb` [0.1.6]

Section titled “llama-index-readers-mongodb [0.1.6]”

  * set document ids when loading (#14000)

### `llama-index-retrievers-duckdb-retriever` [0.1.0]

Section titled “llama-index-retrievers-duckdb-retriever [0.1.0]”

  * Add DuckDBRetriever (#13929)

### `llama-index-vector-stores-chroma` [0.1.9]

Section titled “llama-index-vector-stores-chroma [0.1.9]”

  * Add inclusion filter to chromadb (#14010)

### `llama-index-vector-stores-lancedb` [0.1.5]

Section titled “llama-index-vector-stores-lancedb [0.1.5]”

  * Fix LanceDBVectorStore `add()` logic (#13993)

### `llama-index-vector-stores-milvus` [0.1.17]

Section titled “llama-index-vector-stores-milvus [0.1.17]”

  * Support all filter operators for Milvus vector store (#13745)

### `llama-index-vector-stores-postgres` [0.1.10]

Section titled “llama-index-vector-stores-postgres [0.1.10]”

  * Broaden SQLAlchemy support in llama-index-vector-stores-postgres to 1.4+ (#13936)

### `llama-index-vector-stores-qdrant` [0.2.9]

Section titled “llama-index-vector-stores-qdrant [0.2.9]”

  * Qdrant: Create payload index for `doc_id` (#14001)

## [2024-06-02]

Section titled “[2024-06-02]”

### `llama-index-core` [0.10.43]

Section titled “llama-index-core [0.10.43]”

  * use default UUIDs when possible for property graph index vector stores (#13886)
  * avoid empty or duplicate inserts in property graph index (#13891)
  * Fix cur depth for `get_rel_map` in simple property graph store (#13888)
  * (bandaid) disable instrumentation from logging generators (#13901)
  * Add backwards compatibility to Dispatcher.get_dispatch_event() method (#13895)
  * Fix: Incorrect naming of acreate_plan in StructuredPlannerAgent (#13879)

### `llama-index-graph-stores-neo4j` [0.2.2]

Section titled “llama-index-graph-stores-neo4j [0.2.2]”

  * Handle cases where type is missing (neo4j property graph) (#13875)
  * Rename `Neo4jPGStore` to `Neo4jPropertyGraphStore` (with backward compat) (#13891)

### `llama-index-llms-openai` [0.1.22]

Section titled “llama-index-llms-openai [0.1.22]”

  * Improve the retry mechanism of OpenAI (#13878)

### `llama-index-readers-web` [0.1.18]

Section titled “llama-index-readers-web [0.1.18]”

  * AsyncWebPageReader: made it actually async; it was exhibiting blocking behavior (#13897)

### `llama-index-vector-stores-opensearch` [0.1.10]

Section titled “llama-index-vector-stores-opensearch [0.1.10]”

  * Fix/OpenSearch filter logic (#13804)

## [2024-05-31]

Section titled “[2024-05-31]”

### `llama-index-core` [0.10.42]

Section titled “llama-index-core [0.10.42]”

  * Allow proper setting of the vector store in property graph index (#13816)
  * fix imports in langchain bridge (#13871)

### `llama-index-graph-stores-nebula` [0.2.0]

Section titled “llama-index-graph-stores-nebula [0.2.0]”

  * NebulaGraph support for PropertyGraphStore (#13816)

### `llama-index-llms-langchain` [0.1.5]

Section titled “llama-index-llms-langchain [0.1.5]”

  * fix fireworks imports in langchain llm (#13871)

### `llama-index-llms-openllm` [0.1.5]

Section titled “llama-index-llms-openllm [0.1.5]”

  * feat(openllm): 0.5 sdk integrations update (#13848)

### `llama-index-llms-premai` [0.1.5]

Section titled “llama-index-llms-premai [0.1.5]”

  * Update SDK compatibility (#13836)

### `llama-index-readers-google` [0.2.6]

Section titled “llama-index-readers-google [0.2.6]”

  * Fixed a bug with tokens causing an infinite loop in GoogleDriveReader (#13863)

## [2024-05-30]

Section titled “[2024-05-30]”

### `llama-index-core` [0.10.41]

Section titled “llama-index-core [0.10.41]”

  * pass embeddings from index to property graph retriever (#13843)
  * protect instrumentation event/span handlers from each other (#13823)
  * add missing events for completion streaming (#13824)
  * missing callback_manager.on_event_end when there is exception (#13825)

### `llama-index-llms-gemini` [0.1.10]

Section titled “llama-index-llms-gemini [0.1.10]”

  * use `model` kwarg for model name for gemini (#13791)

### `llama-index-llms-mistralai` [0.1.15]

Section titled “llama-index-llms-mistralai [0.1.15]”

  * Add mistral code model (#13807)
  * update mistral codestral with fill in middle endpoint (#13810)

### `llama-index-llms-openllm` [0.1.5]

Section titled “llama-index-llms-openllm [0.1.5]”

  * 0.5 integrations update (#13848)

### `llama-index-llms-vertex` [0.1.8]

Section titled “llama-index-llms-vertex [0.1.8]”

  * Safety setting for Pydantic Error for Vertex Integration (#13817)

### `llama-index-readers-smart-pdf-loader` [0.1.5]

Section titled “llama-index-readers-smart-pdf-loader [0.1.5]”

  * handle path objects in smart pdf reader (#13847)

## [2024-05-28]

Section titled “[2024-05-28]”

### `llama-index-core` [0.10.40]

Section titled “llama-index-core [0.10.40]”

  * Added `PropertyGraphIndex` and other supporting abstractions. See the [full guide](https://docs.llamaindex.ai/en/latest/module_guides/indexing/lpg_index_guide/) for more details (#13747)
  * Updated `AutoPrevNextNodePostprocessor` to allow passing in response mode and LLM (#13771)
  * fix type handling with return direct (#13776)
  * Correct the method name to `_aget_retrieved_ids_and_texts` in retrievval evaluator (#13765)
  * fix: QueryTransformComponent incorrect call `self._query_transform` (#13756)
  * implement more filters for `SimpleVectorStoreIndex` (#13365)

### `llama-index-embeddings-bedrock` [0.2.0]

Section titled “llama-index-embeddings-bedrock [0.2.0]”

  * Added support for Bedrock Titan Embeddings v2 (#13580)

### `llama-index-embeddings-oci-genai` [0.1.0]

Section titled “llama-index-embeddings-oci-genai [0.1.0]”

  * add Oracle Cloud Infrastructure (OCI) Generative AI (#13631)

### `llama-index-embeddings-huggingface` [0.2.1]

Section titled “llama-index-embeddings-huggingface [0.2.1]”

  * Expose “safe_serialization” parameter from AutoModel (#11939)

### `llama-index-graph-stores-neo4j` [0.2.0]

Section titled “llama-index-graph-stores-neo4j [0.2.0]”

  * Added `Neo4jPGStore` for property graph support (#13747)

### `llama-index-indices-managed-dashscope` [0.1.1]

Section titled “llama-index-indices-managed-dashscope [0.1.1]”

  * Added dashscope managed index (#13378)

### `llama-index-llms-oci-genai` [0.1.0]

Section titled “llama-index-llms-oci-genai [0.1.0]”

  * add Oracle Cloud Infrastructure (OCI) Generative AI (#13631)

### `llama-index-readers-feishu-wiki` [0.1.1]

Section titled “llama-index-readers-feishu-wiki [0.1.1]”

  * fix undefined variable (#13768)

### `llama-index-packs-secgpt` [0.1.0]

Section titled “llama-index-packs-secgpt [0.1.0]”

  * SecGPT - LlamaIndex Integration #13127

### `llama-index-vector-stores-hologres` [0.1.0]

Section titled “llama-index-vector-stores-hologres [0.1.0]”

  * Add Hologres vector db (#13619)

### `llama-index-vector-stores-milvus` [0.1.16]

Section titled “llama-index-vector-stores-milvus [0.1.16]”

  * Remove FlagEmbedding as Milvus’s dependency (#13767) Unify the collection construction regardless of the value of enable_sparse (#13773)

### `llama-index-vector-stores-opensearch` [0.1.9]

Section titled “llama-index-vector-stores-opensearch [0.1.9]”

  * refactor to put helper methods inside class definition (#13749)

## [2024-05-24]

Section titled “[2024-05-24]”

### `llama-index-core` [0.10.39]

Section titled “llama-index-core [0.10.39]”

  * Add VectorMemory and SimpleComposableMemory (#13352)
  * Improve MarkdownReader to ignore headers in code blocks (#13694)
  * proper async element node parsers (#13698)
  * return only the message content in function calling worker (#13677)
  * nit: fix multimodal query engine to use metadata (#13712)
  * Add notebook with workaround for lengthy tool descriptions and QueryPlanTool (#13701)

### `llama-index-embeddings-ipex-llm` [0.1.2]

Section titled “llama-index-embeddings-ipex-llm [0.1.2]”

  * Improve device selection (#13644)

### `llama-index-indices-managed-postgresml` [0.1.3]

Section titled “llama-index-indices-managed-postgresml [0.1.3]”

  * Add the PostgresML Managed Index (#13623)

### `llama-index-indices-managed-vectara` [0.1.4]

Section titled “llama-index-indices-managed-vectara [0.1.4]”

  * Added chat engine, streaming, factual consistency score, and more (#13639)

### `llama-index-llms-deepinfra` [0.0.1]

Section titled “llama-index-llms-deepinfra [0.0.1]”

  * Add Integration for DeepInfra LLM Models (#13652)

### `llama-index-llm-ipex-llm` [0.1.3]

Section titled “llama-index-llm-ipex-llm [0.1.3]”

  * add GPU support for llama-index-llm-ipex-llm (#13691)

### `llama-index-llms-lmstudio` [0.1.0]

Section titled “llama-index-llms-lmstudio [0.1.0]”

  * lmstudio integration (#13557)

### `llama-index-llms-ollama` [0.1.5]

Section titled “llama-index-llms-ollama [0.1.5]”

  * Use aiter_lines function to iterate over lines in ollama integration (#13699)

### `llama-index-llms-vertex` [0.1.6]

Section titled “llama-index-llms-vertex [0.1.6]”

  * Added safety_settings parameter for gemini (#13568)

### `llama-index-postprocessor-voyageai-rerank` [0.1.3]

Section titled “llama-index-postprocessor-voyageai-rerank [0.1.3]”

  * VoyageAI reranking bug fix (#13622)

### `llama-index-retrievers-mongodb-atlas-bm25-retriever` [0.1.4]

Section titled “llama-index-retrievers-mongodb-atlas-bm25-retriever [0.1.4]”

  * Add missing return (#13720)

### `llama-index-readers-web` [0.1.17]

Section titled “llama-index-readers-web [0.1.17]”

  * Add Scrapfly Web Loader (#13654)

### `llama-index-vector-stores-postgres` [0.1.9]

Section titled “llama-index-vector-stores-postgres [0.1.9]”

  * fix bug with delete and special chars (#13651)

### `llama-index-vector-stores-supabase` [0.1.5]

Section titled “llama-index-vector-stores-supabase [0.1.5]”

  * Try-catch in case the ._client attribute is not present (#13681)

## [2024-05-21]

Section titled “[2024-05-21]”

### `llama-index-core` [0.10.38]

Section titled “llama-index-core [0.10.38]”

  * Enabling streaming in BaseSQLTableQueryEngine (#13599)
  * Fix nonetype errors in relational node parsers (#13615)
  * feat(instrumentation): new spans for ALL llms (#13565)
  * Properly Limit the number of generated questions (#13596)
  * Pass ‘exclude_llm_metadata_keys’ and ‘exclude_embed_metadata_keys’ in element Node Parsers (#13567)
  * Add batch mode to QueryPipeline (#13203)
  * Improve SentenceEmbeddingOptimizer to respect Settings.embed_model (#13514)
  * ReAct output parser robustness changes (#13459)
  * fix for pydantic tool calling with a single argument (#13522)
  * Avoid unexpected error when stream chat doesn’t yield (#13422)

### `llama-index-embeddings-nomic` [0.2.0]

Section titled “llama-index-embeddings-nomic [0.2.0]”

  * Implement local Nomic Embed with the inference_mode parameter (#13607)

### `llama-index-embeddings-nvidia` [0.1.3]

Section titled “llama-index-embeddings-nvidia [0.1.3]”

  * Deprecate `mode()` in favor of `__init__(base_url=...)` (#13572)
  * add snowflake/arctic-embed-l support (#13555)

### `llama-index-embeddings-openai` [0.1.10]

Section titled “llama-index-embeddings-openai [0.1.10]”

  * update how retries get triggered for openai (#13608)

### `llama-index-embeddings-upstage` [0.1.0]

Section titled “llama-index-embeddings-upstage [0.1.0]”

  * Integrations: upstage LLM and Embeddings (#13193)

### `llama-index-llms-gemini` [0.1.8]

Section titled “llama-index-llms-gemini [0.1.8]”

  * feat: add gemini new models to multimodal LLM and regular (#13539)

### `llama-index-llms-groq` [0.1.4]

Section titled “llama-index-llms-groq [0.1.4]”

  * fix: enable tool use (#13566)

### `llama-index-llms-lmstudio` [0.1.0]

Section titled “llama-index-llms-lmstudio [0.1.0]”

  * Add support for lmstudio integration (#13557)

### `llama-index-llms-nvidia` [0.1.3]

Section titled “llama-index-llms-nvidia [0.1.3]”

  * Deprecate `mode()` in favor of `__init__(base_url=...)` (#13572)

### `llama-index-llms-openai` [0.1.20]

Section titled “llama-index-llms-openai [0.1.20]”

  * update how retries get triggered for openai (#13608)

### `llama-index-llms-unify` [0.1.0]

Section titled “llama-index-llms-unify [0.1.0]”

  * Add Unify LLM Support (#12921)

### `llama-index-llms-upstage` [0.1.0]

Section titled “llama-index-llms-upstage [0.1.0]”

  * Integrations: upstage LLM and Embeddings (#13193)

### `llama-index-llms-vertex` [0.1.6]

Section titled “llama-index-llms-vertex [0.1.6]”

  * Adding Support for MedLM Models (#11911)

### `llama_index.postprocessor.dashscope_rerank` [0.1.0]

Section titled “llama_index.postprocessor.dashscope_rerank [0.1.0]”

  * Add dashscope rerank for postprocessor (#13353)

### `llama-index-postprocessor-nvidia-rerank` [0.1.2]

Section titled “llama-index-postprocessor-nvidia-rerank [0.1.2]”

  * Deprecate `mode()` in favor of `__init__(base_url=...)` (#13572)

### `llama-index-readers-mongodb` [0.1.5]

Section titled “llama-index-readers-mongodb [0.1.5]”

  * SimpleMongoReader should allow optional fields in metadata (#13575)

### `llama-index-readers-papers` [0.1.5]

Section titled “llama-index-readers-papers [0.1.5]”

  * fix: (ArxivReader) set exclude_hidden to False when reading data from hidden directory (#13578)

### `llama-index-readers-sec-filings` [0.1.5]

Section titled “llama-index-readers-sec-filings [0.1.5]”

  * fix: sec_filings header when making requests to sec.gov #13548

### `llama-index-readers-web` [0.1.16]

Section titled “llama-index-readers-web [0.1.16]”

  * Added firecrawl search mode (#13560)
  * Updated Browserbase web reader (#13535)

### `llama-index-tools-cassandra` [0.1.0]

Section titled “llama-index-tools-cassandra [0.1.0]”

  * added Cassandra database tool spec for agents (#13423)

### `llama-index-vector-stores-azureaisearch` [0.1.7]

Section titled “llama-index-vector-stores-azureaisearch [0.1.7]”

  * Allow querying AzureAISearch without non-null metadata field (#13531)

### `llama-index-vector-stores-elasticsearch` [0.2.0]

Section titled “llama-index-vector-stores-elasticsearch [0.2.0]”

  * Integrate VectorStore from Elasticsearch client (#13291)

### `llama-index-vector-stores-milvus` [0.1.14]

Section titled “llama-index-vector-stores-milvus [0.1.14]”

  * Fix the filter expression construction of Milvus vector store (#13591)

### `llama-index-vector-stores-supabase` [0.1.4]

Section titled “llama-index-vector-stores-supabase [0.1.4]”

  * Disconnect when deleted (#13611)

### `llama-index-vector-stores-wordlift` [0.1.0]

Section titled “llama-index-vector-stores-wordlift [0.1.0]”

  * Added the WordLift Vector Store (#13028)

## [2024-05-14]

Section titled “[2024-05-14]”

### `llama-index-core` [0.10.37]

Section titled “llama-index-core [0.10.37]”

  * Add image_documents at call time for `MultiModalLLMCompletionProgram` (#13467)
  * fix RuntimeError by switching to asyncio from threading (#13486)
  * Add support for prompt kwarg (#13405)
  * VectorStore -> BasePydanticVectorStore (#13439)
  * fix: user_message does not exist bug (#13432)
  * import missing response type (#13382)
  * add `CallbackManager` to `MultiModalLLM` (#13400)

### `llama-index-llms-bedrock` [0.1.8]

Section titled “llama-index-llms-bedrock [0.1.8]”

  * Remove “Truncate” parameter from Bedrock Cohere invoke model request (#13442)

### `llama-index-readers-web` [0.1.14]

Section titled “llama-index-readers-web [0.1.14]”

  * Trafilatura kwargs and progress bar for trafilatura web reader (#13454)

### `llama-index-vector-stores-postgres` [0.1.8]

Section titled “llama-index-vector-stores-postgres [0.1.8]”

  * Fix #9522 - SQLAlchemy warning when using hybrid search (#13476)

### `llama-index-vector-stores-lantern` [0.1.4]

Section titled “llama-index-vector-stores-lantern [0.1.4]”

  * Fix #9522 - SQLAlchemy warning when using hybrid search (#13476)

### `llama-index-callbacks-uptrain` [0.2.0]

Section titled “llama-index-callbacks-uptrain [0.2.0]”

  * update UpTrain Callback Handler to support new Upgratin eval schema (#13479)

### `llama-index-vector-stores-zep` [0.1.3]

Section titled “llama-index-vector-stores-zep [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-vearch` [0.1.1]

Section titled “llama-index-vector-stores-vearch [0.1.1]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-upstash` [0.1.4]

Section titled “llama-index-vector-stores-upstash [0.1.4]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-typesense` [0.1.3]

Section titled “llama-index-vector-stores-typesense [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-timescalerevector` [0.1.3]

Section titled “llama-index-vector-stores-timescalerevector [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-tencentvectordb` [0.1.4]

Section titled “llama-index-vector-stores-tencentvectordb [0.1.4]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-tair` [0.1.3]

Section titled “llama-index-vector-stores-tair [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-singlestoredb` [0.1.3]

Section titled “llama-index-vector-stores-singlestoredb [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-rocksetdb` [0.1.3]

Section titled “llama-index-vector-stores-rocksetdb [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-neptune` [0.1.1]

Section titled “llama-index-vector-stores-neptune [0.1.1]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-neo4jvector` [0.1.5]

Section titled “llama-index-vector-stores-neo4jvector [0.1.5]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-myscale` [0.1.3]

Section titled “llama-index-vector-stores-myscale [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-metal` [0.1.3]

Section titled “llama-index-vector-stores-metal [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-jaguar` [0.1.3]

Section titled “llama-index-vector-stores-jaguar [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-epsilla` [0.1.3]

Section titled “llama-index-vector-stores-epsilla [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-dynamodb` [0.1.3]

Section titled “llama-index-vector-stores-dynamodb [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-dashvector` [0.1.3]

Section titled “llama-index-vector-stores-dashvector [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-chatgpt-plugin` [0.1.3]

Section titled “llama-index-vector-stores-chatgpt-plugin [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-baiduvectordb` [0.1.1]

Section titled “llama-index-vector-stores-baiduvectordb [0.1.1]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-bagel` [0.1.3]

Section titled “llama-index-vector-stores-bagel [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-awsdocdb` [0.1.5]

Section titled “llama-index-vector-stores-awsdocdb [0.1.5]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-awadb` [0.1.3]

Section titled “llama-index-vector-stores-awadb [0.1.3]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-vector-stores-alibabacloud-opensearch` [0.1.1]

Section titled “llama-index-vector-stores-alibabacloud-opensearch [0.1.1]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-readers-wordlift` [0.1.4]

Section titled “llama-index-readers-wordlift [0.1.4]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-readers-guru` [0.1.4]

Section titled “llama-index-readers-guru [0.1.4]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-readers-pebblo` [0.1.1]

Section titled “llama-index-readers-pebblo [0.1.1]”

  * VectorStore -> BasePydanticVectorStore (#13439)

### `llama-index-postprocessor-voyageai-rerank` [0.1.2]

Section titled “llama-index-postprocessor-voyageai-rerank [0.1.2]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-sbert-rerank` [0.1.4]

Section titled “llama-index-postprocessor-sbert-rerank [0.1.4]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-rankllm-rerank` [0.1.3]

Section titled “llama-index-postprocessor-rankllm-rerank [0.1.3]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-rankgpt-rerank` [0.1.4]

Section titled “llama-index-postprocessor-rankgpt-rerank [0.1.4]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-openvino-rerank` [0.1.3]

Section titled “llama-index-postprocessor-openvino-rerank [0.1.3]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-nvidia-rerank` [0.1.1]

Section titled “llama-index-postprocessor-nvidia-rerank [0.1.1]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-jinaai-rerank` [0.1.3]

Section titled “llama-index-postprocessor-jinaai-rerank [0.1.3]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-flag-embedding-rerank` [0.1.3]

Section titled “llama-index-postprocessor-flag-embedding-rerank [0.1.3]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-colbert-rerank` [0.1.2]

Section titled “llama-index-postprocessor-colbert-rerank [0.1.2]”

  * bump rerank versions (#13465)

### `llama-index-postprocessor-cohere-rerank` [0.1.6]

Section titled “llama-index-postprocessor-cohere-rerank [0.1.6]”

  * bump rerank versions (#13465)

### `llama-index-multi-modal-llms-openai` [0.1.6]

Section titled “llama-index-multi-modal-llms-openai [0.1.6]”

  * gpt-4o support (#13463)

### `llama-index-llms-openai` [0.1.19]

Section titled “llama-index-llms-openai [0.1.19]”

  * gpt-4o support (#13463)

### `llama-index-packs-rag-fusion-query-pipeline` [0.1.4]

Section titled “llama-index-packs-rag-fusion-query-pipeline [0.1.4]”

  * fix the RAG fusion pipeline (#13413)

### `llama-index-agent-openai` [0.2.5]

Section titled “llama-index-agent-openai [0.2.5]”

  * fix: update OpenAIAssistantAgent to use attachments (#13341)

### `llama-index-embeddings-deepinfra` [0.1.0]

Section titled “llama-index-embeddings-deepinfra [0.1.0]”

  * new embeddings integration (#13323)

### `llama-index-llms-mlx` [0.1.0]

Section titled “llama-index-llms-mlx [0.1.0]”

  * new llm integration (#13231)

### `llama-index-vector-stores-milvus` [0.1.12]

Section titled “llama-index-vector-stores-milvus [0.1.12]”

  * fix: Corrected connection parameters in connections.connect() (#13448)

### `llama-index-vector-stores-azureaisearch` [0.1.6]

Section titled “llama-index-vector-stores-azureaisearch [0.1.6]”

  * fix AzureAiSearchVectorStore metadata f-string (#13435)

### `llama-index-vector-stores-mongodb` [0.1.5]

Section titled “llama-index-vector-stores-mongodb [0.1.5]”

  * adds Unit and Integration tests for MongoDBAtlasVectorSearch (#12854)

### `llama-index-llms-huggingface` [0.2.0]

Section titled “llama-index-llms-huggingface [0.2.0]”

  * update llama-index-llms-huggingface dependency (#13420)

### `llama-index-vector-store-relyt` [0.1.0]

Section titled “llama-index-vector-store-relyt [0.1.0]”

  * new vector store integration

### `llama-index-storage-kvstore-redis` [0.1.5]

Section titled “llama-index-storage-kvstore-redis [0.1.5]”

  * Implement async methods in RedisKVStore (#12943)

### `llama-index-packs-cohere-citation-chat` [0.1.5]

Section titled “llama-index-packs-cohere-citation-chat [0.1.5]”

  * pin llama-index-llms-cohere dependency (#13417)

### `llama-index-llms-cohere` [0.2.0]

Section titled “llama-index-llms-cohere [0.2.0]”

  * pin cohere dependency (#13417)

### `llama-index-tools-azure-code-interpreter` [0.1.1]

Section titled “llama-index-tools-azure-code-interpreter [0.1.1]”

  * fix indexing issue and runtime error message (#13414)

### `llama-index-postprocessor-cohere-rerank` [0.1.5]

Section titled “llama-index-postprocessor-cohere-rerank [0.1.5]”

  * fix Cohere Rerank bug (#13410)

### `llama-index-indices-managed-llama-cloud` [0.1.7]

Section titled “llama-index-indices-managed-llama-cloud [0.1.7]”

  * fix retriever integration (#13409)

### `llama-index-tools-azure-code-interpreter` [0.1.0]

Section titled “llama-index-tools-azure-code-interpreter [0.1.0]”

  * new tool

### `llama-index-readers-google` [0.2.5]

Section titled “llama-index-readers-google [0.2.5]”

  * fix missing authorized_user_info check on GoogleDriveReader (#13394)

### `llama-index-storage-kvstore-firestore` [0.2.1]

Section titled “llama-index-storage-kvstore-firestore [0.2.1]”

  * await Firestore’s AsyncDocumentReference (#13386)

### `llama-index-llms-nvidia` [0.1.2]

Section titled “llama-index-llms-nvidia [0.1.2]”

  * add dynamic model listing support (#13398)

## [2024-05-09]

Section titled “[2024-05-09]”

### `llama-index-core` [0.10.36]

Section titled “llama-index-core [0.10.36]”

  * add start_char_idx and end_char_idx with MarkdownElementParser (#13377)
  * use handlers from global default (#13368)

### `llama-index-readers-pebblo` [0.1.0]

Section titled “llama-index-readers-pebblo [0.1.0]”

  * Initial release (#13128)

### `llama-index-llms-cohere` [0.1.7]

Section titled “llama-index-llms-cohere [0.1.7]”

  * Call Cohere RAG inference with documents argument (#13196)

### `llama-index-vector-scores-kdbai` [0.1.6]

Section titled “llama-index-vector-scores-kdbai [0.1.6]”

  * update add method decode utf-8 (#13194)

### `llama-index-vector-stores-alibabacloud-opensearch` [0.1.0]

Section titled “llama-index-vector-stores-alibabacloud-opensearch [0.1.0]”

  * Initial release (#13286)

### `llama-index-tools-multion` [0.2.0]

Section titled “llama-index-tools-multion [0.2.0]”

  * update tool to use updated api/sdk (#13373)

### `llama-index-vector-sores-weaviate` [1.0.0]

Section titled “llama-index-vector-sores-weaviate [1.0.0]”

  * Update to weaviate client v4 (#13229)

### `llama-index-readers-file` [0.1.22]

Section titled “llama-index-readers-file [0.1.22]”

  * fix bug where PDFReader ignores extra_info (#13369)

### `llama-index-llms-azure-openai` [0.1.8]

Section titled “llama-index-llms-azure-openai [0.1.8]”

  * Add sync httpx client support (#13370)

### `llama-index-llms-openai` [0.1.18]

Section titled “llama-index-llms-openai [0.1.18]”

  * Add sync httpx client support (#13370)
  * Add missing openai model token context (#13337)

### `llama-index-readers-github` [0.1.9]

Section titled “llama-index-readers-github [0.1.9]”

  * Add fail_on_http_error (#13366)

### `llama-index-vector-stores-pinecone` [0.1.7]

Section titled “llama-index-vector-stores-pinecone [0.1.7]”

  * Add attribution tag for pinecone (#13329)

### `llama-index-llms-nvidia` [0.1.1]

Section titled “llama-index-llms-nvidia [0.1.1]”

  * set default max_tokens to 1024 (#13371)

### `llama-index-readers-papers` [0.1.5]

Section titled “llama-index-readers-papers [0.1.5]”

  * Fix hiddent temp directory issue for arxiv reader (#13351)

### `llama-index-embeddings-nvidia` [0.1.1]

Section titled “llama-index-embeddings-nvidia [0.1.1]”

  * fix truncate passing aget_query_embedding and get_text_embedding (#13367)

### `llama-index-llms-anyscare` [0.1.4]

Section titled “llama-index-llms-anyscare [0.1.4]”

  * Add llama-3 models (#13336)

## [2024-05-07]

Section titled “[2024-05-07]”

### `llama-index-agent-introspective` [0.1.0]

Section titled “llama-index-agent-introspective [0.1.0]”

  * Add CRITIC and reflection agent integrations (#13108)

### `llama-index-core` [0.10.35]

Section titled “llama-index-core [0.10.35]”

  * fix `from_defaults()` erasing summary memory buffer history (#13325)
  * use existing async event loop instead of `asyncio.run()` in core (#13309)
  * fix async streaming from query engine in condense question chat engine (#13306)
  * Handle ValueError in extract_table_summaries in element node parsers (#13318)
  * Handle llm properly for QASummaryQueryEngineBuilder and RouterQueryEngine (#13281)
  * expand instrumentation payloads (#13302)
  * Fix Bug in sql join statement missing schema (#13277)

### `llama-index-embeddings-jinaai` [0.1.5]

Section titled “llama-index-embeddings-jinaai [0.1.5]”

  * add encoding_type parameters in JinaEmbedding class (#13172)
  * fix encoding type access in JinaEmbeddings (#13315)

### `llama-index-embeddings-nvidia` [0.1.0]

Section titled “llama-index-embeddings-nvidia [0.1.0]”

  * add nvidia nim embeddings support (#13177)

### `llama-index-llms-mistralai` [0.1.12]

Section titled “llama-index-llms-mistralai [0.1.12]”

  * Fix async issue when streaming with Mistral AI (#13292)

### `llama-index-llms-nvidia` [0.1.0]

Section titled “llama-index-llms-nvidia [0.1.0]”

  * add nvidia nim llm support (#13176)

### `llama-index-postprocessor-nvidia-rerank` [0.1.0]

Section titled “llama-index-postprocessor-nvidia-rerank [0.1.0]”

  * add nvidia nim rerank support (#13178)

### `llama-index-readers-file` [0.1.21]

Section titled “llama-index-readers-file [0.1.21]”

  * Update MarkdownReader to parse text before first header (#13327)

### `llama-index-readers-web` [0.1.13]

Section titled “llama-index-readers-web [0.1.13]”

  * feat: Spider Web Loader (#13200)

### `llama-index-vector-stores-vespa` [0.1.0]

Section titled “llama-index-vector-stores-vespa [0.1.0]”

  * Add VectorStore integration for Vespa (#13213)

### `llama-index-vector-stores-vertexaivectorsearch` [0.1.0]

Section titled “llama-index-vector-stores-vertexaivectorsearch [0.1.0]”

  * Add support for Vertex AI Vector Search as Vector Store (#13186)

## [2024-05-02]

Section titled “[2024-05-02]”

### `llama-index-core` [0.10.34]

Section titled “llama-index-core [0.10.34]”

  * remove error ignoring during chat engine streaming (#13160)
  * add structured planning agent (#13149)
  * update base class for planner agent (#13228)
  * Fix: Error when parse file using SimpleFileNodeParser and file’s extension doesn’t in FILE_NODE_PARSERS (#13156)
  * add matching `source_node.node_id` verification to node parsers (#13109)
  * Retrieval Metrics: Updating HitRate and MRR for Evaluation@K documents retrieved. Also adding RR as a separate metric (#12997)
  * Add chat summary memory buffer (#13155)

### `llama-index-indices-managed-zilliz` [0.1.3]

Section titled “llama-index-indices-managed-zilliz [0.1.3]”

  * ZillizCloudPipelineIndex accepts flexible params to create pipelines (#10134, #10112)

### `llama-index-llms-huggingface` [0.1.7]

Section titled “llama-index-llms-huggingface [0.1.7]”

  * Add tool usage support with text-generation-inference integration from Hugging Face (#12471)

### `llama-index-llms-maritalk` [0.2.0]

Section titled “llama-index-llms-maritalk [0.2.0]”

  * Add streaming for maritalk (#13207)

### `llama-index-llms-mistral-rs` [0.1.0]

Section titled “llama-index-llms-mistral-rs [0.1.0]”

  * Integrate mistral.rs LLM (#13105)

### `llama-index-llms-mymagic` [0.1.7]

Section titled “llama-index-llms-mymagic [0.1.7]”

  * mymagicai api update (#13148)

### `llama-index-llms-nvidia-triton` [0.1.5]

Section titled “llama-index-llms-nvidia-triton [0.1.5]”

  * Streaming Support for Nvidia’s Triton Integration (#13135)

### `llama-index-llms-ollama` [0.1.3]

Section titled “llama-index-llms-ollama [0.1.3]”

  * added async support to ollama llms (#13150)

### `llama-index-readers-microsoft-sharepoint` [0.2.2]

Section titled “llama-index-readers-microsoft-sharepoint [0.2.2]”

  * Exclude access control metadata keys from LLMs and embeddings - SharePoint Reader (#13184)

### `llama-index-readers-web` [0.1.11]

Section titled “llama-index-readers-web [0.1.11]”

  * feat: Browserbase Web Reader (#12877)

### `llama-index-readers-youtube-metadata` [0.1.0]

Section titled “llama-index-readers-youtube-metadata [0.1.0]”

  * Added YouTube Metadata Reader (#12975)

### `llama-index-storage-kvstore-redis` [0.1.4]

Section titled “llama-index-storage-kvstore-redis [0.1.4]”

  * fix redis kvstore key that was in bytes (#13201)

### `llama-index-vector-stores-azureaisearch` [0.1.5]

Section titled “llama-index-vector-stores-azureaisearch [0.1.5]”

  * Respect filter condition for Azure AI Search (#13215)

### `llama-index-vector-stores-chroma` [0.1.7]

Section titled “llama-index-vector-stores-chroma [0.1.7]”

  * small bump for new chroma client version (#13158)

### `llama-index-vector-stores-firestore` [0.1.0]

Section titled “llama-index-vector-stores-firestore [0.1.0]”

  * Adding Firestore Vector Store (#12048)

### `llama-index-vector-stores-kdbai` [0.1.5]

Section titled “llama-index-vector-stores-kdbai [0.1.5]”

  * small fix to returned IDs after `add()` (#12515)

### `llama-index-vector-stores-milvus` [0.1.11]

Section titled “llama-index-vector-stores-milvus [0.1.11]”

  * Add hybrid retrieval mode to MilvusVectorStore (#13122)

### `llama-index-vector-stores-postgres` [0.1.7]

Section titled “llama-index-vector-stores-postgres [0.1.7]”

  * parameterize queries in pgvector store (#13199)

## [2024-04-27]

Section titled “[2024-04-27]”

### `llama-index-core` [0.10.33]

Section titled “llama-index-core [0.10.33]”

  * add agent_worker.as_agent() (#13061)

### `llama-index-embeddings-bedrock` [0.1.5]

Section titled “llama-index-embeddings-bedrock [0.1.5]”

  * Use Bedrock cohere character limit (#13126)

### `llama-index-tools-google` [0.1.5]

Section titled “llama-index-tools-google [0.1.5]”

  * Change default value for attendees to empty list (#13134)

### `llama-index-graph-stores-falkordb` [0.1.4]

Section titled “llama-index-graph-stores-falkordb [0.1.4]”

  * Skip index creation error when index already exists (#13085)

### `llama-index-tools-google` [0.1.4]

Section titled “llama-index-tools-google [0.1.4]”

  * Fix datetime for google calendar create_event api (#13132)

### `llama-index-llms-anthropic` [0.1.11]

Section titled “llama-index-llms-anthropic [0.1.11]”

  * Merge multiple prompts into one (#13131)

### `llama-index-indices-managed-llama-cloud` [0.1.6]

Section titled “llama-index-indices-managed-llama-cloud [0.1.6]”

  * Use MetadataFilters in LlamaCloud Retriever (#13117)

### `llama-index-graph-stores-kuzu` [0.1.3]

Section titled “llama-index-graph-stores-kuzu [0.1.3]”

  * Fix kuzu integration .execute() calls (#13100)

### `llama-index-vector-stores-lantern` [0.1.3]

Section titled “llama-index-vector-stores-lantern [0.1.3]”

  * Maintenance update to keep up to date with lantern builds (#13116)

## [2024-04-25]

Section titled “[2024-04-25]”

### `llama-index-core` [0.10.32]

Section titled “llama-index-core [0.10.32]”

  * Corrected wrong output type for `OutputKeys.from_keys()` (#13086)
  * add run_jobs to aws base embedding (#13096)
  * allow user to customize the keyword extractor prompt template (#13083)
  * (CondenseQuestionChatEngine) Do not condense the question if there’s no conversation history (#13069)
  * QueryPlanTool: Execute tool calls in subsequent (dependent) nodes in the query plan (#13047)
  * Fix for fusion retriever sometime return Nonetype query(s) before similarity search (#13112)

### `llama-index-embeddings-ipex-llm` [0.1.1]

Section titled “llama-index-embeddings-ipex-llm [0.1.1]”

  * Support llama-index-embeddings-ipex-llm for Intel GPUs (#13097)

### `llama-index-packs-raft-dataset` [0.1.4]

Section titled “llama-index-packs-raft-dataset [0.1.4]”

  * Fix bug in raft dataset generator - multiple system prompts (#12751)

### `llama-index-readers-microsoft-sharepoint` [0.2.1]

Section titled “llama-index-readers-microsoft-sharepoint [0.2.1]”

  * Add access control related metadata to SharePoint reader (#13067)

### `llama-index-vector-stores-pinecone` [0.1.6]

Section titled “llama-index-vector-stores-pinecone [0.1.6]”

  * Nested metadata filter support (#13113)

### `llama-index-vector-stores-qdrant` [0.2.8]

Section titled “llama-index-vector-stores-qdrant [0.2.8]”

  * Nested metadata filter support (#13113)

## [2024-04-23]

Section titled “[2024-04-23]”

### `llama-index-core` [0.10.31]

Section titled “llama-index-core [0.10.31]”

  * fix async streaming response from query engine (#12953)
  * enforce uuid in element node parsers (#12951)
  * add function calling LLM program (#12980)
  * make the PydanticSingleSelector work with async api (#12964)
  * fix query pipeline’s arun_with_intermediates (#13002)

### `llama-index-agent-coa` [0.1.0]

Section titled “llama-index-agent-coa [0.1.0]”

  * Add COA Agent integration (#13043)

### `llama-index-agent-lats` [0.1.0]

Section titled “llama-index-agent-lats [0.1.0]”

  * Official LATs agent integration (#13031)

### `llama-index-agent-llm-compiler` [0.1.0]

Section titled “llama-index-agent-llm-compiler [0.1.0]”

  * Add LLMCompiler Agent Integration (#13044)

### `llama-index-llms-anthropic` [0.1.10]

Section titled “llama-index-llms-anthropic [0.1.10]”

  * Add the ability to pass custom headers to Anthropic LLM requests (#12819)

### `llama-index-llms-bedrock` [0.1.7]

Section titled “llama-index-llms-bedrock [0.1.7]”

  * Adding claude 3 opus to BedRock integration (#13033)

### `llama-index-llms-fireworks` [0.1.5]

Section titled “llama-index-llms-fireworks [0.1.5]”

  * Add new Llama 3 and Mixtral 8x22b model into Llama Index for Fireworks (#12970)

### `llama-index-llms-openai` [0.1.16]

Section titled “llama-index-llms-openai [0.1.16]”

  * Fix AsyncOpenAI “RuntimeError: Event loop is closed bug” when instances of AsyncOpenAI are rapidly created & destroyed (#12946)
  * Don’t retry on all OpenAI APIStatusError exceptions - just InternalServerError (#12947)

### `llama-index-llms-watsonx` [0.1.7]

Section titled “llama-index-llms-watsonx [0.1.7]”

  * Updated IBM watsonx foundation models (#12973)

### `llama-index-packs-code-hierarchy` [0.1.6]

Section titled “llama-index-packs-code-hierarchy [0.1.6]”

  * Return the parent node if the query node is not present (#12983)
  * fixed bug when function is defined twice (#12941)

### `llama-index-program-openai` [0.1.6]

Section titled “llama-index-program-openai [0.1.6]”

  * dding support for streaming partial instances of Pydantic output class in OpenAIPydanticProgram (#13021)

### `llama-index-readers-openapi` [0.1.0]

Section titled “llama-index-readers-openapi [0.1.0]”

  * add reader for openapi files (#12998)

### `llama-index-readers-slack` [0.1.4]

Section titled “llama-index-readers-slack [0.1.4]”

  * Avoid infinite loop when not handled exception is raised (#12963)

### `llama-index-readers-web` [0.1.10]

Section titled “llama-index-readers-web [0.1.10]”

  * Improve whole site reader to remove duplicate links (#12977)

### `llama-index-retrievers-bedrock` [0.1.1]

Section titled “llama-index-retrievers-bedrock [0.1.1]”

  * Fix Bedrock KB retriever to use query bundle (#12910)

### `llama-index-vector-stores-awsdocdb` [0.1.0]

Section titled “llama-index-vector-stores-awsdocdb [0.1.0]”

  * Integrating AWS DocumentDB as a vector storage method (#12217)

### `llama-index-vector-stores-databricks` [0.1.2]

Section titled “llama-index-vector-stores-databricks [0.1.2]”

  * Fix databricks vector search metadata (#12999)

### `llama-index-vector-stores-neo4j` [0.1.4]

Section titled “llama-index-vector-stores-neo4j [0.1.4]”

  * Neo4j metadata filtering support (#12923)

### `llama-index-vector-stores-pinecone` [0.1.5]

Section titled “llama-index-vector-stores-pinecone [0.1.5]”

  * Fix error querying PineconeVectorStore using sparse query mode (#12967)

### `llama-index-vector-stores-qdrant` [0.2.5]

Section titled “llama-index-vector-stores-qdrant [0.2.5]”

  * Many fixes for async and checking if collection exists (#12916)

### `llama-index-vector-stores-weaviate` [0.1.5]

Section titled “llama-index-vector-stores-weaviate [0.1.5]”

  * Adds the index deletion functionality to the WeviateVectoreStore (#12993)

## [2024-04-17]

Section titled “[2024-04-17]”

### `llama-index-core` [0.10.30]

Section titled “llama-index-core [0.10.30]”

  * Add intermediate outputs to QueryPipeline (#12683)
  * Fix show progress causing results to be out of order (#12897)
  * add OR filter condition support to simple vector store (#12823)
  * improved custom agent init (#12824)
  * fix pipeline load without docstore (#12808)
  * Use async `_aprocess_actions` in `_arun_step_stream` (#12846)
  * provide the exception to the StreamChatErrorEvent (#12879)
  * fix bug in load and search tool spec (#12902)

### `llama-index-embeddings-azure-opena` [0.1.7]

Section titled “llama-index-embeddings-azure-opena [0.1.7]”

  * Expose azure_ad_token_provider argument to support token expiration (#12818)

### `llama-index-embeddings-cohere` [0.1.8]

Section titled “llama-index-embeddings-cohere [0.1.8]”

  * Add httpx_async_client option (#12896)

### `llama-index-embeddings-ipex-llm` [0.1.0]

Section titled “llama-index-embeddings-ipex-llm [0.1.0]”

  * add ipex-llm embedding integration (#12740)

### `llama-index-embeddings-octoai` [0.1.0]

Section titled “llama-index-embeddings-octoai [0.1.0]”

  * add octoai embeddings (#12857)

### `llama-index-llms-azure-openai` [0.1.6]

Section titled “llama-index-llms-azure-openai [0.1.6]”

  * Expose azure_ad_token_provider argument to support token expiration (#12818)

### `llama-index-llms-ipex-llm` [0.1.2]

Section titled “llama-index-llms-ipex-llm [0.1.2]”

  * add support for loading “low-bit format” model to IpexLLM integration (#12785)

### `llama-index-llms-mistralai` [0.1.11]

Section titled “llama-index-llms-mistralai [0.1.11]”

  * support `open-mixtral-8x22b` (#12894)

### `llama-index-packs-agents-lats` [0.1.0]

Section titled “llama-index-packs-agents-lats [0.1.0]”

  * added LATS agent pack (#12735)

### `llama-index-readers-smart-pdf-loader` [0.1.4]

Section titled “llama-index-readers-smart-pdf-loader [0.1.4]”

  * Use passed in metadata for documents (#12844)

### `llama-index-readers-web` [0.1.9]

Section titled “llama-index-readers-web [0.1.9]”

  * added Firecrawl Web Loader (#12825)

### `llama-index-vector-stores-milvus` [0.1.10]

Section titled “llama-index-vector-stores-milvus [0.1.10]”

  * use batch insertions into Milvus vector store (#12837)

### `llama-index-vector-stores-vearch` [0.1.0]

Section titled “llama-index-vector-stores-vearch [0.1.0]”

  * add vearch to vector stores (#10972)

## [2024-04-13]

Section titled “[2024-04-13]”

### `llama-index-core` [0.10.29]

Section titled “llama-index-core [0.10.29]”

  * **BREAKING** Moved `PandasQueryEngine` and `PandasInstruction` parser to `llama-index-experimental` (#12419) 
    * new install: `pip install -U llama-index-experimental`
    * new import: `from llama_index.experimental.query_engine import PandasQueryEngine`
  * Fixed some core dependencies to make python3.12 work nicely (#12762)
  * update async utils `run_jobs()` to include tqdm description (#12812)
  * Refactor kvdocstore delete methods (#12681)

### `llama-index-llms-bedrock` [0.1.6]

Section titled “llama-index-llms-bedrock [0.1.6]”

  * Support for Mistral Large from Bedrock (#12804)

### `llama-index-llms-openvino` [0.1.0]

Section titled “llama-index-llms-openvino [0.1.0]”

  * Added OpenVino LLMs (#12639)

### `llama-index-llms-predibase` [0.1.4]

Section titled “llama-index-llms-predibase [0.1.4]”

  * Update LlamaIndex-Predibase Integration to latest API (#12736)
  * Enable choice of either Predibase-hosted or HuggingFace-hosted fine-tuned adapters in LlamaIndex-Predibase integration (#12789)

### `llama-index-output-parsers-guardrails` [0.1.3]

Section titled “llama-index-output-parsers-guardrails [0.1.3]”

  * Modernize GuardrailsOutputParser (#12676)

### `llama-index-packs-agents-coa` [0.1.0]

Section titled “llama-index-packs-agents-coa [0.1.0]”

  * Chain-of-Abstraction Agent Pack (#12757)

### `llama-index-packs-code-hierarchy` [0.1.3]

Section titled “llama-index-packs-code-hierarchy [0.1.3]”

  * Fixed issue with chunking multi-byte characters (#12715)

### `llama-index-packs-raft-dataset` [0.1.4]

Section titled “llama-index-packs-raft-dataset [0.1.4]”

  * Fix bug in raft dataset generator - multiple system prompts (#12751)

### `llama-index-postprocessor-openvino-rerank` [0.1.2]

Section titled “llama-index-postprocessor-openvino-rerank [0.1.2]”

  * Add openvino rerank support (#12688)

### `llama-index-readers-file` [0.1.18]

Section titled “llama-index-readers-file [0.1.18]”

  * convert to Path in docx reader if input path str (#12807)
  * make pip check work for optional pdf packages (#12758)

### `llama-index-readers-s3` [0.1.7]

Section titled “llama-index-readers-s3 [0.1.7]”

  * wrong doc id when using default s3 endpoint in S3Reader (#12803)

### `llama-index-retrievers-bedrock` [0.1.0]

Section titled “llama-index-retrievers-bedrock [0.1.0]”

  * Add Amazon Bedrock knowledge base integration as retriever (#12737)

### `llama-index-retrievers-mongodb-atlas-bm25-retriever` [0.1.3]

Section titled “llama-index-retrievers-mongodb-atlas-bm25-retriever [0.1.3]”

  * Add mongodb atlas bm25 retriever (#12519)

### `llama-index-storage-chat-store-redis` [0.1.3]

Section titled “llama-index-storage-chat-store-redis [0.1.3]”

  * fix message serialization in redis chat store (#12802)

### `llama-index-vector-stores-astra-db` [0.1.6]

Section titled “llama-index-vector-stores-astra-db [0.1.6]”

  * Relax dependency version to accept astrapy `1.*` (#12792)

### `llama-index-vector-stores-couchbase` [0.1.0]

Section titled “llama-index-vector-stores-couchbase [0.1.0]”

  * Add support for Couchbase as a Vector Store (#12680)

### `llama-index-vector-stores-elasticsearch` [0.1.7]

Section titled “llama-index-vector-stores-elasticsearch [0.1.7]”

  * Fix elasticsearch hybrid rrf window_size (#12695)

### `llama-index-vector-stores-milvus` [0.1.8]

Section titled “llama-index-vector-stores-milvus [0.1.8]”

  * Added support to retrieve metadata fields from milvus (#12626)

### `llama-index-vector-stores-redis` [0.2.0]

Section titled “llama-index-vector-stores-redis [0.2.0]”

  * Modernize redis vector store, use redisvl (#12386)

### `llama-index-vector-stores-qdrant` [0.2.0]

Section titled “llama-index-vector-stores-qdrant [0.2.0]”

  * refactor: Switch default Qdrant sparse encoder (#12512)

## [2024-04-09]

Section titled “[2024-04-09]”

### `llama-index-core` [0.10.28]

Section titled “llama-index-core [0.10.28]”

  * Support indented code block fences in markdown node parser (#12393)
  * Pass in output parser to guideline evaluator (#12646)
  * Added example of query pipeline + memory (#12654)
  * Add missing node postprocessor in CondensePlusContextChatEngine async mode (#12663)
  * Added `return_direct` option to tools /tool metadata (#12587)
  * Add retry for batch eval runner (#12647)
  * Thread-safe instrumentation (#12638)
  * Coroutine-safe instrumentation Spans #12589
  * Add in-memory loading for non-default filesystems in PDFReader (#12659)
  * Remove redundant tokenizer call in sentence splitter (#12655)
  * Add SynthesizeComponent import to shortcut imports (#12655)
  * Improved truncation in SimpleSummarize (#12655)
  * adding err handling in eval_utils default_parser for correctness (#12624)
  * Add async_postprocess_nodes at RankGPT Postprocessor Nodes (#12620)
  * Fix MarkdownNodeParser ref_doc_id (#12615)

### `llama-index-embeddings-openvino` [0.1.5]

Section titled “llama-index-embeddings-openvino [0.1.5]”

  * Added initial support for openvino embeddings (#12643)

### `llama-index-llms-anthropic` [0.1.9]

Section titled “llama-index-llms-anthropic [0.1.9]”

  * add anthropic tool calling (#12591)

### `llama-index-llms-ipex-llm` [0.1.1]

Section titled “llama-index-llms-ipex-llm [0.1.1]”

  * add ipex-llm integration (#12322)
  * add more data types support to ipex-llm llm integration (#12635)

### `llama-index-llms-openllm` [0.1.4]

Section titled “llama-index-llms-openllm [0.1.4]”

  * Proper PrivateAttr usage in OpenLLM (#12655)

### `llama-index-multi-modal-llms-anthropic` [0.1.4]

Section titled “llama-index-multi-modal-llms-anthropic [0.1.4]”

  * Bumped anthropic dep version (#12655)

### `llama-index-multi-modal-llms-gemini` [0.1.5]

Section titled “llama-index-multi-modal-llms-gemini [0.1.5]”

  * bump generativeai dep (#12645)

### `llama-index-packs-dense-x-retrieval` [0.1.4]

Section titled “llama-index-packs-dense-x-retrieval [0.1.4]”

  * Add streaming support for DenseXRetrievalPack (#12607)

### `llama-index-readers-mongodb` [0.1.4]

Section titled “llama-index-readers-mongodb [0.1.4]”

  * Improve efficiency of MongoDB reader (#12664)

### `llama-index-readers-wikipedia` [0.1.4]

Section titled “llama-index-readers-wikipedia [0.1.4]”

  * Added multilingual support for the Wikipedia reader (#12616)

### `llama-index-storage-index-store-elasticsearch` [0.1.3]

Section titled “llama-index-storage-index-store-elasticsearch [0.1.3]”

  * remove invalid chars from default collection name (#12672)

### `llama-index-vector-stores-milvus` [0.1.8]

Section titled “llama-index-vector-stores-milvus [0.1.8]”

  * Added support to retrieve metadata fields from milvus (#12626)
  * Bug fix - Similarity metric is always IP for MilvusVectorStore (#12611)

## [2024-04-04]

Section titled “[2024-04-04]”

### `llama-index-agent-openai` [0.2.2]

Section titled “llama-index-agent-openai [0.2.2]”

  * Update imports for message thread typing (#12437)

### `llama-index-core` [0.10.27]

Section titled “llama-index-core [0.10.27]”

  * Fix for pydantic query engine outputs being blank (#12469)
  * Add span_id attribute to Events (instrumentation) (#12417)
  * Fix RedisDocstore node retrieval from docs property (#12324)
  * Add node-postprocessors to retriever_tool (#12415)
  * FLAREInstructQueryEngine : delegating retriever api if the query engine supports it (#12503)
  * Make chat message to dict safer (#12526)
  * fix check in batch eval runner for multi-kwargs (#12563)
  * Fixes agent_react_multimodal_step.py bug with partial args (#12566)

### `llama-index-embeddings-clip` [0.1.5]

Section titled “llama-index-embeddings-clip [0.1.5]”

  * Added support to load clip model from local file path (#12577)

### `llama-index-embeddings-cloudflar-workersai` [0.1.0]

Section titled “llama-index-embeddings-cloudflar-workersai [0.1.0]”

  * text embedding integration: Cloudflare Workers AI (#12446)

### `llama-index-embeddings-voyageai` [0.1.4]

Section titled “llama-index-embeddings-voyageai [0.1.4]”

  * Fix pydantic issue in class definition (#12469)

### `llama-index-finetuning` [0.1.5]

Section titled “llama-index-finetuning [0.1.5]”

  * Small typo fix in QA generation prompt (#12470)

### `llama-index-graph-stores-falkordb` [0.1.3]

Section titled “llama-index-graph-stores-falkordb [0.1.3]”

  * Replace redis driver with FalkorDB driver (#12434)

### `llama-index-llms-anthropic` [0.1.8]

Section titled “llama-index-llms-anthropic [0.1.8]”

  * Add ability to pass custom HTTP headers to Anthropic client (#12558)

### `llama-index-llms-cohere` [0.1.6]

Section titled “llama-index-llms-cohere [0.1.6]”

  * Add support for Cohere Command R+ model (#12581)

### `llama-index-llms-databricks` [0.1.0]

Section titled “llama-index-llms-databricks [0.1.0]”

  * Integrations with Databricks LLM API (#12432)

### `llama-index-llms-watsonx` [0.1.6]

Section titled “llama-index-llms-watsonx [0.1.6]”

  * Updated Watsonx foundation models (#12493)
  * Updated base model name on watsonx integration #12491

### `lama-index-postprocessor-rankllm-rerank` [0.1.2]

Section titled “lama-index-postprocessor-rankllm-rerank [0.1.2]”

  * Add RankGPT support inside RankLLM (#12475)

### `llama-index-readers-microsoft-sharepoint` [0.1.7]

Section titled “llama-index-readers-microsoft-sharepoint [0.1.7]”

  * Use recursive strategy by default for SharePoint (#12557)

### `llama-index-readers-web` [0.1.8]

Section titled “llama-index-readers-web [0.1.8]”

  * Readability web page reader fix playwright async api bug (#12520)

### `llama-index-vector-stores-kdbai` [0.1.5]

Section titled “llama-index-vector-stores-kdbai [0.1.5]”

  * small `to_list` fix (#12515)

### `llama-index-vector-stores-neptune` [0.1.0]

Section titled “llama-index-vector-stores-neptune [0.1.0]”

  * Add support for Neptune Analytics as a Vector Store (#12423)

### `llama-index-vector-stores-postgres` [0.1.5]

Section titled “llama-index-vector-stores-postgres [0.1.5]”

  * fix(postgres): numeric metadata filters (#12583)

## [2024-03-31]

Section titled “[2024-03-31]”

### `llama-index-core` [0.10.26]

Section titled “llama-index-core [0.10.26]”

  * pass proper query bundle in QueryFusionRetriever (#12387)
  * Update llama_parse_json_element.py to fix error on lists (#12402)
  * Add node postprocessors to retriever tool (#12415)
  * Fix bug where user specified llm is not respected in fallback logic in element node parsers(#12403)
  * log proper LLM response key for async callback manager events (#12421)
  * Deduplicate the two built-in react system prompts; Also make it read from a Markdown file (#12307)
  * fix bug in BatchEvalRunner for multi-evaluator eval_kwargs_lists (#12418)
  * add the callback manager event for vector store index insert_nodes (#12443)
  * fixes an issue with serializing chat messages into chat stores when they contain pydantic API objects (#12394)
  * fixes an issue with slow memory.get() operation (caused by multiple calls to get_all()) (#12394)
  * fixes an issue where an agent+tool message pair is cut from the memory (#12394)
  * Added `FnNodeMapping` for object index (#12391)
  * Make object mapping optional / hidden for object index (#12391)
  * Make object index easier to create from existing vector db (#12391)
  * When LLM failed to follow the react response template, tell it so #12300

### `llama-index-embeddings-cohere` [0.1.5]

Section titled “llama-index-embeddings-cohere [0.1.5]”

  * Bump cohere version to 5.1.1 (#12279)

### `llama-index-embeddings-itrex` [0.1.0]

Section titled “llama-index-embeddings-itrex [0.1.0]”

  * add Intel Extension for Transformers embedding model (#12410)

### `llama-index-graph-stores-neo4j` [0.1.4]

Section titled “llama-index-graph-stores-neo4j [0.1.4]”

  * make neo4j query insensitive (#12337)

### `llama-index-llms-cohere` [0.1.5]

Section titled “llama-index-llms-cohere [0.1.5]”

  * Bump cohere version to 5.1.1 (#12279)

### `llama-index-llms-ipex-llm` [0.1.0]

Section titled “llama-index-llms-ipex-llm [0.1.0]”

  * add ipex-llm integration (#12322)

### `llama-index-llms-litellm` [0.1.4]

Section titled “llama-index-llms-litellm [0.1.4]”

  * Fix litellm ChatMessage role validation error (#12449)

### `llama-index-llms-openai` [0.1.14]

Section titled “llama-index-llms-openai [0.1.14]”

  * Use `FunctionCallingLLM` base class in OpenAI (#12227)

### `llama-index-packs-self-rag` [0.1.4]

Section titled “llama-index-packs-self-rag [0.1.4]”

  * Fix llama-index-core dep (#12374)

### `llama-index-postprocessor-cohere-rerank` [0.1.4]

Section titled “llama-index-postprocessor-cohere-rerank [0.1.4]”

  * Bump cohere version to 5.1.1 (#12279)

### `llama-index-postprocessor-rankllm-rerank` [0.1.1]

Section titled “llama-index-postprocessor-rankllm-rerank [0.1.1]”

  * Added RankLLM rerank (#12296)
  * RankLLM fixes (#12399)

### `llama-index-readers-papers` [0.1.4]

Section titled “llama-index-readers-papers [0.1.4]”

  * Fixed bug with path names (#12366)

### `llama-index-vector-stores-analyticdb` [0.1.1]

Section titled “llama-index-vector-stores-analyticdb [0.1.1]”

  * Add AnalyticDB VectorStore (#12230)

### `llama-index-vector-stores-kdbai` [0.1.4]

Section titled “llama-index-vector-stores-kdbai [0.1.4]”

  * Fixed typo in imports/readme (#12370)

### `llama-index-vector-stores-qdrant` [0.1.5]

Section titled “llama-index-vector-stores-qdrant [0.1.5]”

  * add `in` filter operator for qdrant (#12376)

## [2024-03-27]

Section titled “[2024-03-27]”

### `llama-index-core` [0.10.25]

Section titled “llama-index-core [0.10.25]”

  * Add score to NodeWithScore in KnowledgeGraphQueryEngine (#12326)
  * Batch eval runner fixes (#12302)

### `llama-index-embeddings-cohere` [0.1.5]

Section titled “llama-index-embeddings-cohere [0.1.5]”

  * Added support for binary / quantized embeddings (#12321)

### `llama-index-llms-mistralai` [0.1.10]

Section titled “llama-index-llms-mistralai [0.1.10]”

  * add support for custom endpoints to MistralAI (#12328)

### `llama-index-storage-kvstore-redis` [0.1.3]

Section titled “llama-index-storage-kvstore-redis [0.1.3]”

  * Fix RedisDocstore node retrieval from docs property (#12324)

## [2024-03-26]

Section titled “[2024-03-26]”

### `llama-index-core` [0.10.24]

Section titled “llama-index-core [0.10.24]”

  * pretty prints in `LlamaDebugHandler` (#12216)
  * stricter interpreter constraints on pandas query engine (#12278)
  * PandasQueryEngine can now execute ‘pd.*’ functions (#12240)
  * delete proper metadata in docstore delete function (#12276)
  * improved openai agent parsing function hook (#12062)
  * add raise_on_error flag for SimpleDirectoryReader (#12263)
  * remove un-caught openai import in core (#12262)
  * Fix download_llama_dataset and download_llama_pack (#12273)
  * Implement EvalQueryEngineTool (#11679)
  * Expand instrumenation Span coverage for AgentRunner (#12249)
  * Adding concept of function calling agent/llm (mistral supported for now) (#12222, )

### `llama-index-embeddings-huggingface` [0.2.0]

Section titled “llama-index-embeddings-huggingface [0.2.0]”

  * Use `sentence-transformers` as a backend (#12277)

### `llama-index-postprocessor-voyageai-rerank` [0.1.0]

Section titled “llama-index-postprocessor-voyageai-rerank [0.1.0]”

  * Added voyageai as a reranker (#12111)

### `llama-index-readers-gcs` [0.1.0]

Section titled “llama-index-readers-gcs [0.1.0]”

  * Added google cloud storage reader (#12259)

### `llama-index-readers-google` [0.2.1]

Section titled “llama-index-readers-google [0.2.1]”

  * Support for different drives (#12146)
  * Remove unnecessary PyDrive dependency from Google Drive Reader (#12257)

### `llama-index-readers-readme` [0.1.0]

Section titled “llama-index-readers-readme [0.1.0]”

  * added readme.com reader (#12246)

### `llama-index-packs-raft` [0.1.3]

Section titled “llama-index-packs-raft [0.1.3]”

  * added pack for RAFT (#12275)

## [2024-03-23]

Section titled “[2024-03-23]”

### `llama-index-core` [0.10.23]

Section titled “llama-index-core [0.10.23]”

  * Added `(a)predict_and_call()` function to base LLM class + openai + mistralai (#12188)
  * fixed bug with `wait()` in async agent streaming (#12187)

### `llama-index-embeddings-alephalpha` [0.1.0]

Section titled “llama-index-embeddings-alephalpha [0.1.0]”

  * Added alephalpha embeddings (#12149)

### `llama-index-llms-alephalpha` [0.1.0]

Section titled “llama-index-llms-alephalpha [0.1.0]”

  * Added alephalpha LLM (#12149)

### `llama-index-llms-openai` [0.1.7]

Section titled “llama-index-llms-openai [0.1.7]”

  * fixed bug with `wait()` in async agent streaming (#12187)

### `llama-index-readers-docugami` [0.1.4]

Section titled “llama-index-readers-docugami [0.1.4]”

  * fixed import errors in docugami reader (#12154)

### `llama-index-readers-file` [0.1.12]

Section titled “llama-index-readers-file [0.1.12]”

  * fix PDFReader for remote fs (#12186)

## [2024-03-21]

Section titled “[2024-03-21]”

### `llama-index-core` [0.10.22]

Section titled “llama-index-core [0.10.22]”

  * Updated docs backend from sphinx to mkdocs, added ALL api reference, some light re-org, better search (#11301)
  * Added async loading to `BaseReader` class (although its fake async for now) (#12156)
  * Fix path implementation for non-local FS in `SimpleDirectoryReader` (#12141)
  * add args/kwargs to spans, payloads for retrieval events, in instrumentation (#12147)
  * [react agent] Upon exception, say so, so that Agent can correct itself (#12137)

### `llama-index-embeddings-together` [0.1.3]

Section titled “llama-index-embeddings-together [0.1.3]”

  * Added rate limit handling (#12127)

### `llama-index-graph-stores-neptune` [0.1.3]

Section titled “llama-index-graph-stores-neptune [0.1.3]”

  * Add Amazon Neptune Support as Graph Store (#12097)

### `llama-index-llms-vllm` [0.1.7]

Section titled “llama-index-llms-vllm [0.1.7]”

  * fix VllmServer to work without CUDA-required vllm core (#12003)

### `llama-index-readers-s3` [0.1.4]

Section titled “llama-index-readers-s3 [0.1.4]”

  * Use S3FS in S3Reader (#12061)

### `llama-index-storage-docstore-postgres` [0.1.3]

Section titled “llama-index-storage-docstore-postgres [0.1.3]”

  * Added proper kvstore dep (#12157)

### `llama-index-storage-index-store-postgres` [0.1.3]

Section titled “llama-index-storage-index-store-postgres [0.1.3]”

  * Added proper kvstore dep (#12157)

### `llama-index-vector-stores-elasticsearch` [0.1.6]

Section titled “llama-index-vector-stores-elasticsearch [0.1.6]”

  * fix unclosed session in es add function #12135

### `llama-index-vector-stores-kdbai` [0.1.3]

Section titled “llama-index-vector-stores-kdbai [0.1.3]”

  * Add support for `KDBAIVectorStore` (#11967)

## [2024-03-20]

Section titled “[2024-03-20]”

### `llama-index-core` [0.10.21]

Section titled “llama-index-core [0.10.21]”

  * Lazy init for async elements StreamingAgentChatResponse (#12116)
  * Fix streaming generators get bug by SynthesisEndEvent (#12092)
  * CLIP embedding more models (#12063)

### `llama-index-packs-raptor` [0.1.3]

Section titled “llama-index-packs-raptor [0.1.3]”

  * Add `num_workers` to summary module (#)

### `llama-index-readers-telegram` [0.1.5]

Section titled “llama-index-readers-telegram [0.1.5]”

  * Fix datetime fields (#12112)
  * Add ability to select time period of posts/messages (#12078)

### `llama-index-embeddings-openai` [0.1.7]

Section titled “llama-index-embeddings-openai [0.1.7]”

  * Add api version/base api as optional for open ai embedding (#12091)

### `llama-index-networks` [0.2.1]

Section titled “llama-index-networks [0.2.1]”

  * Add node postprocessing to network retriever (#12027)
  * Add privacy-safe networks demo (#12027)

### `llama-index-callbacks-langfuse` [0.1.3]

Section titled “llama-index-callbacks-langfuse [0.1.3]”

  * Chore: bumps min version of langfuse dep (#12077)

### `llama-index-embeddings-google` [0.1.4]

Section titled “llama-index-embeddings-google [0.1.4]”

  * Chore: bumps google-generativeai dep (#12085)

### `llama-index-embeddings-gemini` [0.1.5]

Section titled “llama-index-embeddings-gemini [0.1.5]”

  * Chore: bumps google-generativeai dep (#12085)

### `llama-index-llms-gemini` [0.1.6]

Section titled “llama-index-llms-gemini [0.1.6]”

  * Chore: bumps google-generativeai dep (#12085)

### `llama-index-llms-palm` [0.1.4]

Section titled “llama-index-llms-palm [0.1.4]”

  * Chore: bumps google-generativeai dep (#12085)

### `llama-index-multi-modal-llms-google` [0.1.4]

Section titled “llama-index-multi-modal-llms-google [0.1.4]”

  * Chore: bumps google-generativeai dep (#12085)

### `llama-index-vector-stores-google` [0.1.5]

Section titled “llama-index-vector-stores-google [0.1.5]”

  * Chore: bumps google-generativeai dep (#12085)

### `llama-index-storage-kvstore-elasticsearch` [0.1.0]

Section titled “llama-index-storage-kvstore-elasticsearch [0.1.0]”

  * New integration (#12068)

### `llama-index-readers-google` [0.1.7]

Section titled “llama-index-readers-google [0.1.7]”

  * Fix - Google Drive Issue of not loading same name files (#12022)

### `llama-index-vector-stores-upstash` [0.1.3]

Section titled “llama-index-vector-stores-upstash [0.1.3]”

  * Adding Metadata Filtering support for UpstashVectorStore (#12054)

### `llama-index-packs-raptor` [0.1.2]

Section titled “llama-index-packs-raptor [0.1.2]”

  * Fix: prevent RaptorPack infinite recursion (#12008)

### `llama-index-embeddings-huggingface-optimum` [0.1.4]

Section titled “llama-index-embeddings-huggingface-optimum [0.1.4]”

  * Fix(OptimumEmbedding): removing token_type_ids causing ONNX validation issues

### `llama-index-llms-anthropic` [0.1.7]

Section titled “llama-index-llms-anthropic [0.1.7]”

  * Fix: Anthropic LLM merge consecutive messages with same role (#12013)

### `llama-index-packs-diff-private-simple-dataset` [0.1.0]

Section titled “llama-index-packs-diff-private-simple-dataset [0.1.0]”

  * DiffPrivacy ICL Pack - OpenAI Completion LLMs (#11881)

### `llama-index-cli` [0.1.11]

Section titled “llama-index-cli [0.1.11]”

  * Remove llama_hub_url keyword from download_llama_dataset of command (#12038)

## [2024-03-14]

Section titled “[2024-03-14]”

### `llama-index-core` [0.10.20]

Section titled “llama-index-core [0.10.20]”

  * New `instrumentation` module for observability (#11831)
  * Allow passing in LLM for `CitationQueryEngine` (#11914)
  * Updated keyval docstore to allow changing suffix in addition to namespace (#11873)
  * Add (some) async streaming support to query_engine #11949

### `llama-index-embeddings-dashscope` [0.1.3]

Section titled “llama-index-embeddings-dashscope [0.1.3]”

  * Fixed embedding type for query texts (#11901)

### `llama-index-embeddings-premai` [0.1.3]

Section titled “llama-index-embeddings-premai [0.1.3]”

  * Support for premai embeddings (#11954)

### `llama-index-networks` [0.2.0]

Section titled “llama-index-networks [0.2.0]”

  * Added support for network retrievers (#11800)

### `llama-index-llms-anthropic` [0.1.6]

Section titled “llama-index-llms-anthropic [0.1.6]”

  * Added support for haiku (#11916)

### `llama-index-llms-mistralai` [0.1.6]

Section titled “llama-index-llms-mistralai [0.1.6]”

  * Fixed import error for ChatMessage (#11902)

### `llama-index-llms-openai` [0.1.11]

Section titled “llama-index-llms-openai [0.1.11]”

  * added gpt-35-turbo-0125 for AZURE_TURBO_MODELS (#11956)
  * fixed error with nontype in logprobs (#11967)

### `llama-index-llms-premai` [0.1.4]

Section titled “llama-index-llms-premai [0.1.4]”

  * Support for premai llm (#11954)

### `llama-index-llms-solar` [0.1.3]

Section titled “llama-index-llms-solar [0.1.3]”

  * Support for solar as an LLM class (#11710)

### `llama-index-llms-vertex` [0.1.5]

Section titled “llama-index-llms-vertex [0.1.5]”

  * Add support for medlm in vertex (#11911)

### `llama-index-readers-goolge` [0.1.6]

Section titled “llama-index-readers-goolge [0.1.6]”

  * added README files and query string for google drive reader (#11724)

### `llama-index-readers-file` [0.1.11]

Section titled “llama-index-readers-file [0.1.11]”

  * Updated ImageReader to add `plain_text` option to trigger pytesseract (#11913)

### `llama-index-readers-pathway` [0.1.3]

Section titled “llama-index-readers-pathway [0.1.3]”

  * use pure requests to reduce deps, simplify code (#11924)

### `llama-index-retrievers-pathway` [0.1.3]

Section titled “llama-index-retrievers-pathway [0.1.3]”

  * use pure requests to reduce deps, simplify code (#11924)

### `llama-index-storage-docstore-mongodb` [0.1.3]

Section titled “llama-index-storage-docstore-mongodb [0.1.3]”

  * Allow changing suffix for mongodb docstore (#11873)

### `llama-index-vector-stores-databricks` [0.1.1]

Section titled “llama-index-vector-stores-databricks [0.1.1]”

  * Support for databricks vector search as a vector store (#10754)

### `llama-index-vector-stores-opensearch` [0.1.8]

Section titled “llama-index-vector-stores-opensearch [0.1.8]”

  * (re)implement proper delete (#11959)

### `llama-index-vector-stores-postgres` [0.1.4]

Section titled “llama-index-vector-stores-postgres [0.1.4]”

  * Fixes for IN filters and OR text search (#11872, #11927)

## [2024-03-12]

Section titled “[2024-03-12]”

### `llama-index-cli` [0.1.9]

Section titled “llama-index-cli [0.1.9]”

  * Removed chroma as a bundled dep to reduce `llama-index` deps

### `llama-index-core` [0.10.19]

Section titled “llama-index-core [0.10.19]”

  * Introduce retries for rate limits in `OpenAI` llm class (#11867)
  * Added table comments to SQL table schemas in `SQLDatabase` (#11774)
  * Added `LogProb` type to `ChatResponse` object (#11795)
  * Introduced `LabelledSimpleDataset` (#11805)
  * Fixed insert `IndexNode` objects with unserializable objects (#11836)
  * Fixed stream chat type error when writing response to history in `CondenseQuestionChatEngine` (#11856)
  * Improve post-processing for json query engine (#11862)

### `llama-index-embeddings-cohere` [0.1.4]

Section titled “llama-index-embeddings-cohere [0.1.4]”

  * Fixed async kwarg error (#11822)

### `llama-index-embeddings-dashscope` [0.1.2]

Section titled “llama-index-embeddings-dashscope [0.1.2]”

  * Fixed pydantic import (#11765)

### `llama-index-graph-stores-neo4j` [0.1.3]

Section titled “llama-index-graph-stores-neo4j [0.1.3]”

  * Properly close connection after verifying connectivity (#11821)

### `llama-index-llms-cohere` [0.1.3]

Section titled “llama-index-llms-cohere [0.1.3]”

  * Add support for new `command-r` model (#11852)

### `llama-index-llms-huggingface` [0.1.4]

Section titled “llama-index-llms-huggingface [0.1.4]”

  * Fixed streaming decoding with special tokens (#11807)

### `llama-index-llms-mistralai` [0.1.5]

Section titled “llama-index-llms-mistralai [0.1.5]”

  * Added support for latest and open models (#11792)

### `llama-index-tools-finance` [0.1.1]

Section titled “llama-index-tools-finance [0.1.1]”

  * Fixed small bug when passing in the API get for stock news (#11772)

### `llama-index-vector-stores-chroma` [0.1.6]

Section titled “llama-index-vector-stores-chroma [0.1.6]”

  * Slimmed down chroma deps (#11775)

### `llama-index-vector-stores-lancedb` [0.1.3]

Section titled “llama-index-vector-stores-lancedb [0.1.3]”

  * Fixes for deleting (#11825)

### `llama-index-vector-stores-postgres` [0.1.3]

Section titled “llama-index-vector-stores-postgres [0.1.3]”

  * Support for nested metadata filters (#11778)

## [2024-03-07]

Section titled “[2024-03-07]”

### `llama-index-callbacks-deepeval` [0.1.3]

Section titled “llama-index-callbacks-deepeval [0.1.3]”

  * Update import path for callback handler (#11754)

### `llama-index-core` [0.10.18]

Section titled “llama-index-core [0.10.18]”

  * Ensure `LoadAndSearchToolSpec` loads document objects (#11733)
  * Fixed bug for no nodes in `QueryFusionRetriever` (#11759)
  * Allow using different runtime kwargs for different evaluators in `BatchEvalRunner` (#11727)
  * Fixed issues with fsspec + `SimpleDirectoryReader` (#11665)
  * Remove `asyncio.run()` requirement from guideline evaluator (#11719)

### `llama-index-embeddings-voyageai` [0.1.3]

Section titled “llama-index-embeddings-voyageai [0.1.3]”

  * Update voyage embeddings to use proper clients (#11721)

### `llama-index-indices-managed-vectara` [0.1.3]

Section titled “llama-index-indices-managed-vectara [0.1.3]”

  * Fixed issues with vectara query engine in non-summary mode (#11668)

### `llama-index-llms-mymagic` [0.1.5]

Section titled “llama-index-llms-mymagic [0.1.5]”

  * Add `return_output` option for json output with query and response (#11761)

### `llama-index-packs-code-hierarchy` [0.1.0]

Section titled “llama-index-packs-code-hierarchy [0.1.0]”

  * Added support for a `CodeHiearchyAgentPack` that allows for agentic traversal of a codebase (#10671)

### `llama-index-packs-cohere-citation-chat` [0.1.3]

Section titled “llama-index-packs-cohere-citation-chat [0.1.3]”

  * Added a new llama-pack for citations + chat with cohere (#11697)

### `llama-index-vector-stores-milvus` [0.1.6]

Section titled “llama-index-vector-stores-milvus [0.1.6]”

  * Prevent forced `flush()` on document add (#11734)

### `llama-index-vector-stores-opensearch` [0.1.7]

Section titled “llama-index-vector-stores-opensearch [0.1.7]”

  * Small typo in metadata column name (#11751)

### `llama-index-vector-stores-tidbvector` [0.1.0]

Section titled “llama-index-vector-stores-tidbvector [0.1.0]”

  * Initial support for TiDB vector store (#11635)

### `llama-index-vector-stores-weaviate` [0.1.4]

Section titled “llama-index-vector-stores-weaviate [0.1.4]”

  * Small fix for `int` fields in metadata filters (#11742)

## [2024-03-06]

Section titled “[2024-03-06]”

New format! Going to try out reporting changes per package.

### `llama-index-cli` [0.1.8]

Section titled “llama-index-cli [0.1.8]”

  * Update mappings for `upgrade` command (#11699)

### `llama-index-core` [0.10.17]

Section titled “llama-index-core [0.10.17]”

  * add `relative_score` and `dist_based_score` to `QueryFusionRetriever` (#11667)
  * check for `none` in async agent queue (#11669)
  * allow refine template for `BaseSQLTableQueryEngine` (#11378)
  * update mappings for llama-packs (#11699)
  * fixed index error for extracting rel texts in KG index (#11695)
  * return proper response types from synthesizer when no nodes (#11701)
  * Inherit metadata to summaries in DocumentSummaryIndex (#11671)
  * Inherit callback manager in sql query engines (#11662)
  * Fixed bug with agent streaming not being written to chat history (#11675)
  * Fixed a small bug with `none` deltas when streaming a function call with an agent (#11713)

### `llama-index-multi-modal-llms-anthropic` [0.1.2]

Section titled “llama-index-multi-modal-llms-anthropic [0.1.2]”

  * Added support for new multi-modal models `haiku` and `sonnet` (#11656)

### `llama-index-packs-finchat` [0.1.0]

Section titled “llama-index-packs-finchat [0.1.0]”

  * Added a new llama-pack for hierarchical agents + finance chat (#11387)

### `llama-index-readers-file` [0.1.8]

Section titled “llama-index-readers-file [0.1.8]”

  * Added support for checking if NLTK files are already downloaded (#11676)

### `llama-index-readers-json` [0.1.4]

Section titled “llama-index-readers-json [0.1.4]”

  * Use the metadata passed in when creating documents (#11626)

### `llama-index-vector-stores-astra-db` [0.1.4]

Section titled “llama-index-vector-stores-astra-db [0.1.4]”

  * Update wording in warning message (#11702)

### `llama-index-vector-stores-opensearch` [0.1.7]

Section titled “llama-index-vector-stores-opensearch [0.1.7]”

  * Avoid calling `nest_asyncio.apply()` in code to avoid confusing errors for users (#11707)

### `llama-index-vector-stores-qdrant` [0.1.4]

Section titled “llama-index-vector-stores-qdrant [0.1.4]”

  * Catch RPC errors (#11657)

## [0.10.16] - 2024-03-05

Section titled “[0.10.16] - 2024-03-05”

### New Features

Section titled “New Features”

  * Anthropic support for new models (#11623, #11612)
  * Easier creation of chat prompts (#11583)
  * Added a raptor retriever llama-pack (#11527)
  * Improve batch cohere embeddings through bedrock (#11572)
  * Added support for vertex AI embeddings (#11561)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Ensure order in async embeddings generation (#11562)
  * Fixed empty metadata for csv reader (#11563)
  * Serializable fix for composable retrievers (#11617)
  * Fixed milvus metadata filter support (#11566)
  * FIxed pydantic import in clickhouse vector store (#11631)
  * Fixed system prompts for gemini/vertext-gemini (#11511)

## [0.10.15] - 2024-03-01

Section titled “[0.10.15] - 2024-03-01”

### New Features

Section titled “New Features”

  * Added FeishuWikiReader (#11491)
  * Added videodb retriever integration (#11463)
  * Added async to opensearch vector store (#11513)
  * New LangFuse one-click callback handler (#11324)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed deadlock issue with async chat streaming (#11548)
  * Improved hidden file check in SimpleDirectoryReader (#11496)
  * Fixed null values in document metadata when using SimpleDirectoryReader (#11501)
  * Fix for sqlite utils in jsonalyze query engine (#11519)
  * Added base url and timeout to ollama multimodal LLM (#11526)
  * Updated duplicate handling in query fusion retriever (#11542)
  * Fixed bug in kg indexx struct updating (#11475)

## [0.10.14] - 2024-02-28

Section titled “[0.10.14] - 2024-02-28”

### New Features

Section titled “New Features”

  * Released llama-index-networks (#11413)
  * Jina reranker (#11291)
  * Added DuckDuckGo agent search tool (#11386)
  * helper functions for chatml (#10272)
  * added brave search tool for agents (#11468)
  * Added Friendli LLM integration (#11384)
  * metadata only queries for chromadb (#11328)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed inheriting llm callback in synthesizers (#11404)
  * Catch delete error in milvus (#11315)
  * Fixed pinecone kwargs issue (#11422)
  * Supabase metadata filtering fix (#11428)
  * api base fix in gemini embeddings (#11393)
  * fix elasticsearch vector store await (#11438)
  * vllm server cuda fix (#11442)
  * fix for passing LLM to context chat engine (#11444)
  * set input types for cohere embeddings (#11288)
  * default value for azure ad token (#10377)
  * added back prompt mixin for react agent (#10610)
  * fixed system roles for gemini (#11481)
  * fixed mean agg pooling returning numpy float values (#11458)
  * improved json path parsing for JSONQueryEngine (#9097)

## [0.10.13] - 2024-02-26

Section titled “[0.10.13] - 2024-02-26”

### New Features

Section titled “New Features”

  * Added a llama-pack for KodaRetriever, for on-the-fly alpha tuning (#11311)
  * Added support for `mistral-large` (#11398)
  * Last token pooling mode for huggingface embeddings models like SFR-Embedding-Mistral (#11373)
  * Added fsspec support to SimpleDirectoryReader (#11303)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed an issue with context window + prompt helper (#11379)
  * Moved OpenSearch vector store to BasePydanticVectorStore (#11400)
  * Fixed function calling in fireworks LLM (#11363)
  * Made cohere embedding types more automatic (#11288)
  * Improve function calling in react agent (#11280)
  * Fixed MockLLM imports (#11376)

## [0.10.12] - 2024-02-22

Section titled “[0.10.12] - 2024-02-22”

### New Features

Section titled “New Features”

  * Added `llama-index-postprocessor-colbert-rerank` package (#11057)
  * `MyMagicAI` LLM (#11263)
  * `MariaTalk` LLM (#10925)
  * Add retries to github reader (#10980)
  * Added FireworksAI embedding and LLM modules (#10959)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed string formatting in weaviate (#11294)
  * Fixed off-by-one error in semantic splitter (#11295)
  * Fixed `download_llama_pack` for multiple files (#11272)
  * Removed `BUILD` files from packages (#11267)
  * Loosened python version reqs for all packages (#11267)
  * Fixed args issue with chromadb (#11104)

## [0.10.11] - 2024-02-21

Section titled “[0.10.11] - 2024-02-21”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed multi-modal LLM for async acomplete (#11064)
  * Fixed issue with llamaindex-cli imports (#11068)

## [0.10.10] - 2024-02-20

Section titled “[0.10.10] - 2024-02-20”

I’m still a bit wonky with our publishing process — apologies. This is just a
version bump to ensure the changes that were supposed to happen in 0.10.9
actually did get published. (AF)

## [0.10.9] - 2024-02-20

Section titled “[0.10.9] - 2024-02-20”

  * add llama-index-cli dependency

## [0.10.7] - 2024-02-19

Section titled “[0.10.7] - 2024-02-19”

### New Features

Section titled “New Features”

  * Added Self-Discover llamapack (#10951)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed linting in CICD (#10945)
  * Fixed using remote graph stores (#10971)
  * Added missing LLM kwarg in NoText response synthesizer (#10971)
  * Fixed openai import in rankgpt (#10971)
  * Fixed resolving model name to string in openai embeddings (#10971)
  * Off by one error in sentence window node parser (#10971)

## [0.10.6] - 2024-02-17

Section titled “[0.10.6] - 2024-02-17”

First, apologies for missing the changelog the last few versions. Trying to
figure out the best process with 400+ packages.

At some point, each package will have a dedicated changelog.

But for now, onto the “master” changelog.

### New Features

Section titled “New Features”

  * Added `NomicHFEmbedding` (#10762)
  * Added `MinioReader` (#10744)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Various fixes for clickhouse vector store (#10799)
  * Fix index name in neo4j vector store (#10749)
  * Fixes to sagemaker embeddings (#10778)
  * Fixed performance issues when splitting nodes (#10766)
  * Fix non-float values in reranker + b25 (#10930)
  * OpenAI-agent should be a dep of openai program (#10930)
  * Add missing shortcut imports for query pipeline components (#10930)
  * Fix NLTK and tiktoken not being bundled properly with core (#10930)
  * Add back `llama_index.core.__version__` (#10930)

## [0.10.3] - 2024-02-13

Section titled “[0.10.3] - 2024-02-13”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed passing in LLM to `as_chat_engine` (#10605)
  * Fixed system prompt formatting for anthropic (#10603)
  * Fixed elasticsearch vector store error on `__version__` (#10656)
  * Fixed import on openai pydantic program (#10657)
  * Added client back to opensearch vector store exports (#10660)
  * Fixed bug in SimpleDirectoryReader not using file loaders properly (#10655)
  * Added lazy LLM initialization to RankGPT (#10648)
  * Fixed bedrock embedding `from_credentials` passing ing the model name (#10640)
  * Added back recent changes to TelegramReader (#10625)

## [0.10.0, 0.10.1] - 2024-02-12

Section titled “[0.10.0, 0.10.1] - 2024-02-12”

### Breaking Changes

Section titled “Breaking Changes”

  * Several changes are introduced. See the [full blog post](https://blog.llamaindex.ai/llamaindex-v0-10-838e735948f8) for complete details.

## [0.9.48] - 2024-02-12

Section titled “[0.9.48] - 2024-02-12”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Add back deprecated API for BedrockEmbdding (#10581)

## [0.9.47] - 2024-02-11

Section titled “[0.9.47] - 2024-02-11”

Last patch before v0.10!

### New Features

Section titled “New Features”

  * add conditional links to query pipeline (#10520)
  * refactor conditional links + add to cookbook (#10544)
  * agent + query pipeline cleanups (#10563)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Add sleep to fix lag in chat stream (#10339)
  * OllamaMultiModal kwargs (#10541)
  * Update Ingestion Pipeline to handle empty documents (#10543)
  * Fixing minor spelling error (#10516)
  * fix elasticsearch async check (#10549)
  * Docs/update slack demo colab (#10534)
  * Adding the possibility to use the IN operator for PGVectorStore (#10547)
  * fix agent reset (#10562)
  * Fix MD duplicated Node id from multiple docs (#10564)

## [0.9.46] - 2024-02-08

Section titled “[0.9.46] - 2024-02-08”

### New Features

Section titled “New Features”

  * Update pooling strategy for embedding models (#10536)
  * Add Multimodal Video RAG example (#10530)
  * Add SECURITY.md (#10531)
  * Move agent module guide up one-level (#10519)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Deeplake fixes (#10529)
  * Add Cohere section for llamaindex (#10523)
  * Fix md element (#10510)

## [0.9.45.post1] - 2024-02-07

Section titled “[0.9.45.post1] - 2024-02-07”

### New Features

Section titled “New Features”

  * Upgraded deeplake vector database to use BasePydanticVectorStore (#10504)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix MD parser for inconsistency tables (#10488)
  * Fix ImportError for pypdf in MetadataExtractionSEC.ipynb (#10491)

## [0.9.45] - 2024-02-07

Section titled “[0.9.45] - 2024-02-07”

### New Features

Section titled “New Features”

  * Refactor: add AgentRunner.from_llm method (#10452)
  * Support custom prompt formatting for non-chat LLMS (#10466)
  * Bump cryptography from 41.0.7 to 42.0.0 (#10467)
  * Add persist and load method for Colbert Index (#10477)
  * Allow custom agent to take in user inputs (#10450)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * remove exporter from arize-phoenix global callback handler (#10465)
  * Fixing Dashscope qwen llm bug (#10471)
  * Fix: calling AWS Bedrock models (#10443)
  * Update Azure AI Search (fka Azure Cognitive Search) vector store integration to latest client SDK 11.4.0 stable + updating jupyter notebook sample (#10416)
  * fix some imports (#10485)

## [0.9.44] - 2024-02-05

Section titled “[0.9.44] - 2024-02-05”

### New Features

Section titled “New Features”

  * ollama vision cookbook (#10438)
  * Support Gemini “transport” configuration (#10457)
  * Add Upstash Vector (#10451)

## [0.9.43] - 2024-02-03

Section titled “[0.9.43] - 2024-02-03”

### New Features

Section titled “New Features”

  * Add multi-modal ollama (#10434)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * update base class for astradb (#10435)

## [0.9.42.post1] - 2024-02-02

Section titled “[0.9.42.post1] - 2024-02-02”

### New Features

Section titled “New Features”

  * Add Async support for Base nodes parser (#10418)

## [0.9.42] - 2024-02-02

Section titled “[0.9.42] - 2024-02-02”

### New Features

Section titled “New Features”

  * Add support for `gpt-3.5-turbo-0125` (#10412)
  * Added `create-llama` support to rag cli (#10405)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed minor bugs in lance-db vector store (#10404)
  * Fixed streaming bug in ollama (#10407)

## [0.9.41] - 2024-02-01

Section titled “[0.9.41] - 2024-02-01”

### New Features

Section titled “New Features”

  * Nomic Embedding (#10388)
  * Dashvector support sparse vector (#10386)
  * Table QA with MarkDownParser and Benchmarking (#10382)
  * Simple web page reader (#10395)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * fix full node content in KeywordExtractor (#10398)

## [0.9.40] - 2024-01-30

Section titled “[0.9.40] - 2024-01-30”

### New Features

Section titled “New Features”

  * Improve and fix bugs for MarkdownElementNodeParser (#10340)
  * Fixed and improve Perplexity support for new models (#10319)
  * Ensure system_prompt is passed to Perplexity LLM (#10326)
  * Extended BaseRetrievalEvaluator to include an optional PostProcessor (#10321)

## [0.9.39] - 2024-01-26

Section titled “[0.9.39] - 2024-01-26”

### New Features

Section titled “New Features”

  * Support for new GPT Turbo Models (#10291)
  * Support Multiple docs for Sentence Transformer Fine tuning(#10297)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Marvin imports fixed (#9864)

## [0.9.38] - 2024-01-25

Section titled “[0.9.38] - 2024-01-25”

### New Features

Section titled “New Features”

  * Support for new OpenAI v3 embedding models (#10279)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Extra checks on sparse embeddings for qdrant (#10275)

## [0.9.37] - 2024-01-24

Section titled “[0.9.37] - 2024-01-24”

### New Features

Section titled “New Features”

  * Added a RAG CLI utility (#10193)
  * Added a textai vector store (#10240)
  * Added a Postgresql based docstore and index store (#10233)
  * specify tool spec in tool specs (#10263)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed serialization error in ollama chat (#10230)
  * Added missing fields to `SentenceTransformerRerank` (#10225)
  * Fixed title extraction (#10209, #10226)
  * nit: make chainable output parser more exposed in library/docs (#10262)
  * :bug: summary index not carrying over excluded metadata keys (#10259)

## [0.9.36] - 2024-01-23

Section titled “[0.9.36] - 2024-01-23”

### New Features

Section titled “New Features”

  * Added support for `SageMakerEmbedding` (#10207)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix duplicated `file_id` on openai assistant (#10223)
  * Fix circular dependencies for programs (#10222)
  * Run `TitleExtractor` on groups of nodes from the same parent document (#10209)
  * Improve vectara auto-retrieval (#10195)

## [0.9.35] - 2024-01-22

Section titled “[0.9.35] - 2024-01-22”

### New Features

Section titled “New Features”

  * `beautifulsoup4` dependency to new optional extra `html` (#10156)
  * make `BaseNode.hash` an `@property` (#10163)
  * Neutrino (#10150)
  * feat: JSONalyze Query Engine (#10067)
  * [wip] add custom hybrid retriever notebook (#10164)
  * add from_collection method to ChromaVectorStore class (#10167)
  * CLI experiment v0: ask (#10168)
  * make react agent prompts more editable (#10154)
  * Add agent query pipeline (#10180)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Update supabase vecs metadata filter function to support multiple fields (#10133)
  * Bugfix/code improvement for LanceDB integration (#10144)
  * `beautifulsoup4` optional dependency (#10156)
  * Fix qdrant aquery hybrid search (#10159)
  * make hash a @property (#10163)
  * fix: bug on poetry install of llama-index[postgres] (#10171)
  * [doc] update jaguar vector store documentation (#10179)
  * Remove use of not-launched finish_message (#10188)
  * Updates to Lantern vector stores docs (#10192)
  * fix typo in multi_document_agents.ipynb (#10196)

## [0.9.34] - 2024-01-19

Section titled “[0.9.34] - 2024-01-19”

### New Features

Section titled “New Features”

  * Added SageMakerEndpointLLM (#10140)
  * Added support for Qdrant filters (#10136)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Update bedrock utils for Claude 2:1 (#10139)
  * BugFix: deadlocks using multiprocessing (#10125)

## [0.9.33] - 2024-01-17

Section titled “[0.9.33] - 2024-01-17”

### New Features

Section titled “New Features”

  * Added RankGPT as a postprocessor (#10054)
  * Ensure backwards compatibility with new Pinecone client version bifucation (#9995)
  * Recursive retriever all the things (#10019)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * BugFix: When using markdown element parser on a table containing comma (#9926)
  * extend auto-retrieval notebook (#10065)
  * Updated the Attribute name in llm_generators (#10070)
  * jaguar vector store add text_tag to add_kwargs in add() (#10057)

## [0.9.32] - 2024-01-16

Section titled “[0.9.32] - 2024-01-16”

### New Features

Section titled “New Features”

  * added query-time row retrieval + fix nits with query pipeline over structured data (#10061)
  * ReActive Agents w/ Context + updated stale link (#10058)

## [0.9.31] - 2024-01-15

Section titled “[0.9.31] - 2024-01-15”

### New Features

Section titled “New Features”

  * Added selectors and routers to query pipeline (#9979)
  * Added sparse-only search to qdrant vector store (#10041)
  * Added Tonic evaluators (#10000)
  * Adding async support to firestore docstore (#9983)
  * Implement mongodb docstore `put_all` method (#10014)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Properly truncate sql results based on `max_string_length` (#10015)
  * Fixed `node.resolve_image()` for base64 strings (#10026)
  * Fixed cohere system prompt role (#10020)
  * Remove redundant token counting operation in SentenceSplitter (#10053)

## [0.9.30] - 2024-01-11

Section titled “[0.9.30] - 2024-01-11”

### New Features

Section titled “New Features”

  * Implements a Node Parser using embeddings for Semantic Splitting (#9988)
  * Add Anyscale Embedding model support (#9470)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * nit: fix pandas get prompt (#10001)
  * Fix: Token counting bug (#9912)
  * Bump jinja2 from 3.1.2 to 3.1.3 (#9997)
  * Fix corner case for qdrant hybrid search (#9993)
  * Bugfix: sphinx generation errors (#9944)
  * Fix: `language` used before assignment in `CodeSplitter` (#9987)
  * fix inconsistent name “text_parser” in section “Use a Text Splitter… (#9980)
  * :bug: fixing batch size (#9982)
  * add auto-async execution to query pipelines (#9967)
  * :bug: fixing init (#9977)
  * Parallel Loading with SimpleDirectoryReader (#9965)
  * do not force delete an index in milvus (#9974)

## [0.9.29] - 2024-01-10

Section titled “[0.9.29] - 2024-01-10”

### New Features

Section titled “New Features”

  * Added support for together.ai models (#9962)
  * Added support for batch redis/firestore kvstores, async firestore kvstore (#9827)
  * Parallelize `IngestionPipeline.run()` (#9920)
  * Added new query pipeline components: function, argpack, kwargpack (#9952)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Updated optional langchain imports to avoid warnings (#9964)
  * Raise an error if empty nodes are embedded (#9953)

## [0.9.28] - 2024-01-09

Section titled “[0.9.28] - 2024-01-09”

### New Features

Section titled “New Features”

  * Added support for Nvidia TenorRT LLM (#9842)
  * Allow `tool_choice` to be set during agent construction (#9924)
  * Added streaming support for `QueryPipeline` (#9919)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Set consistent doc-ids for llama-index readers (#9923, #9916)
  * Remove unneeded model inputs for HuggingFaceEmbedding (#9922)
  * Propagate `tool_choice` flag to downstream APIs (#9901)
  * Add `chat_store_key` to chat memory `from_defaults()` (#9928)

## [0.9.27] - 2024-01-08

Section titled “[0.9.27] - 2024-01-08”

### New Features

Section titled “New Features”

  * add query pipeline (#9908)
  * Feature: Azure Multi Modal (fixes: #9471) (#9843)
  * add postgres docker (#9906)
  * Vectara auto_retriever (#9865)
  * Redis Chat Store support (#9880)
  * move more classes to core (#9871)

### Bug Fixes / Nits / Smaller Features

Section titled “Bug Fixes / Nits / Smaller Features”

  * Propagate `tool_choice` flag to downstream APIs (#9901)
  * filter out negative indexes from faiss query (#9907)
  * added NE filter for qdrant payloads (#9897)
  * Fix incorrect id assignment in MyScale query result (#9900)
  * Qdrant Text Match Filter (#9895)
  * Fusion top k for hybrid search (#9894)
  * Fix (#9867) sync_to_async to avoid blocking during asynchronous calls (#9869)
  * A single node passed into compute_scores returns as a float (#9866)
  * Remove extra linting steps (#9878)
  * add vectara links (#9886)

## [0.9.26] - 2024-01-05

Section titled “[0.9.26] - 2024-01-05”

### New Features

Section titled “New Features”

  * Added a `BaseChatStore` and `SimpleChatStore` abstraction for dedicated chat memory storage (#9863)
  * Enable custom `tree_sitter` parser to be passed into `CodeSplitter` (#9845)
  * Created a `BaseAutoRetriever` base class, to allow other retrievers to extend to auto modes (#9846)
  * Added support for Nvidia Triton LLM (#9488)
  * Added `DeepEval` one-click observability (#9801)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Updated the guidance integration to work with the latest version (#9830)
  * Made text storage optional for doctores/ingestion pipeline (#9847)
  * Added missing `sphinx-automodapi` dependency for docs (#9852)
  * Return actual node ids in weaviate query results (#9854)
  * Added prompt formatting to LangChainLLM (#9844)

## [0.9.25] - 2024-01-03

Section titled “[0.9.25] - 2024-01-03”

### New Features

Section titled “New Features”

  * Added concurrancy limits for dataset generation (#9779)
  * New `deepeval` one-click observability handler (#9801)
  * Added jaguar vector store (#9754)
  * Add beta multimodal ReAct agent (#9807)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Changed default batch size for OpenAI embeddings to 100 (#9805)
  * Use batch size properly for qdrant upserts (#9814)
  * `_verify_source_safety` uses AST, not regexes, for proper safety checks (#9789)
  * use provided LLM in element node parsers (#9776)
  * updated legacy vectordb loading function to be more robust (#9773)
  * Use provided http client in AzureOpenAI (#9772)

## [0.9.24] - 2023-12-30

Section titled “[0.9.24] - 2023-12-30”

### New Features

Section titled “New Features”

  * Add reranker for BEIR evaluation (#9743)
  * Add Pathway integration. (#9719)
  * custom agents implementation + notebook (#9746)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * fix beam search for vllm: add missing parameter (#9741)
  * Fix alpha for hrbrid search (#9742)
  * fix token counter (#9744)
  * BM25 tokenizer lowercase (#9745)

## [0.9.23] - 2023-12-28

Section titled “[0.9.23] - 2023-12-28”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * docs: fixes qdrant_hybrid.ipynb typos (#9729)
  * make llm completion program more general (#9731)
  * Refactor MM Vector store and Index for empty collection (#9717)
  * Adding IF statement to check for Schema using “Select” (#9712)
  * allow skipping module loading in `download_module` and `download_llama_pack` (#9734)

## [0.9.22] - 2023-12-26

Section titled “[0.9.22] - 2023-12-26”

### New Features

Section titled “New Features”

  * Added `.iter_data()` method to `SimpleDirectoryReader` (#9658)
  * Added async support to `Ollama` LLM (#9689)
  * Expanding pinecone filter support for `in` and `not in` (#9683)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Improve BM25Retriever performance (#9675)
  * Improved qdrant hybrid search error handling (#9707)
  * Fixed `None` handling in `ChromaVectorStore` (#9697)
  * Fixed postgres schema creation if not existing (#9712)

## [0.9.21] - 2023-12-23

Section titled “[0.9.21] - 2023-12-23”

### New Features

Section titled “New Features”

  * Added zilliz cloud as a managed index (#9605)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Bedrock client and LLM fixes (#9671, #9646)

## [0.9.20] - 2023-12-21

Section titled “[0.9.20] - 2023-12-21”

### New Features

Section titled “New Features”

  * Added `insert_batch_size` to limit number of embeddings held in memory when creating an index, defaults to 2048 (#9630)
  * Improve auto-retrieval (#9647)
  * Configurable Node ID Generating Function (#9574)
  * Introduced action input parser (#9575)
  * qdrant sparse vector support (#9644)
  * Introduced upserts and delete in ingestion pipeline (#9643)
  * Add Zilliz Cloud Pipeline as a Managed Index (#9605)
  * Add support for Google Gemini models via VertexAI (#9624)
  * support allowing additional metadata filters on autoretriever (#9662)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix pip install commands in LM Format Enforcer notebooks (#9648)
  * Fixing some more links and documentations (#9633)
  * some bedrock nits and fixes (#9646)

## [0.9.19] - 2023-12-20

Section titled “[0.9.19] - 2023-12-20”

### New Features

Section titled “New Features”

  * new llama datasets `LabelledEvaluatorDataset` & `LabelledPairwiseEvaluatorDataset` (#9531)

## [0.9.18] - 2023-12-20

Section titled “[0.9.18] - 2023-12-20”

### New Features

Section titled “New Features”

  * multi-doc auto-retrieval guide (#9631)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * fix(vllm): make Vllm’s ‘complete’ method behave the same as other LLM class (#9634)
  * FIx Doc links and other documentation issue (#9632)

## [0.9.17] - 2023-12-19

Section titled “[0.9.17] - 2023-12-19”

### New Features

Section titled “New Features”

  * [example] adding user feedback (#9601)
  * FEATURE: Cohere ReRank Relevancy Metric for Retrieval Eval (#9495)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix Gemini Chat Mode (#9599)
  * Fixed `types-protobuf` from being a primary dependency (#9595)
  * Adding an optional auth token to the TextEmbeddingInference class (#9606)
  * fix: out of index get latest tool call (#9608)
  * fix(azure_openai.py): add missing return to subclass override (#9598)
  * fix mix up b/w ‘formatted’ and ‘format’ params for ollama api call (#9594)

## [0.9.16] - 2023-12-18

Section titled “[0.9.16] - 2023-12-18”

### New Features

Section titled “New Features”

  * agent refactor: step-wise execution (#9584)
  * Add OpenRouter, with Mixtral demo (#9464)
  * Add hybrid search to neo4j vector store (#9530)
  * Add support for auth service accounts for Google Semantic Retriever (#9545)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed missing `default=None` for `LLM.system_prompt` (#9504)
  * Fix #9580 : Incorporate metadata properly (#9582)
  * Integrations: Gradient[Embeddings,LLM] - sdk-upgrade (#9528)
  * Add mixtral 8x7b model to anyscale available models (#9573)
  * Gemini Model Checks (#9563)
  * Update OpenAI fine-tuning with latest changes (#9564)
  * fix/Reintroduce `WHERE` filter to the Sparse Query for PgVectorStore (#9529)
  * Update Ollama API to ollama v0.1.16 (#9558)
  * ollama: strip invalid `formatted` option (#9555)
  * add a device in optimum push #9541 (#9554)
  * Title vs content difference for Gemini Embedding (#9547)
  * fix pydantic fields to float (#9542)

## [0.9.15] - 2023-12-13

Section titled “[0.9.15] - 2023-12-13”

### New Features

Section titled “New Features”

  * Added full support for Google Gemini text+vision models (#9452)
  * Added new Google Semantic Retriever (#9440)
  * added `from_existing()` method + async support to OpenAI assistants (#9367)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed huggingface LLM system prompt and messages to prompt (#9463)
  * Fixed ollama additional kwargs usage (#9455)

## [0.9.14] - 2023-12-11

Section titled “[0.9.14] - 2023-12-11”

### New Features

Section titled “New Features”

  * Add MistralAI LLM (#9444)
  * Add MistralAI Embeddings (#9441)
  * Add `Ollama` Embedding class (#9341)
  * Add `FlagEmbeddingReranker` for reranking (#9285)
  * feat: PgVectorStore support advanced metadata filtering (#9377)
  * Added `sql_only` parameter to SQL query engines to avoid executing SQL (#9422)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Feat/PgVector Support custom hnsw.ef_search and ivfflat.probes (#9420)
  * fix F1 score definition, update copyright year (#9424)
  * Change more than one image input for Replicate Multi-modal models from error to warning (#9360)
  * Removed GPT-Licensed `aiostream` dependency (#9403)
  * Fix result of BedrockEmbedding with Cohere model (#9396)
  * Only capture valid tool names in react agent (#9412)
  * Fixed `top_k` being multiplied by 10 in azure cosmos (#9438)
  * Fixed hybrid search for OpenSearch (#9430)

### Breaking Changes

Section titled “Breaking Changes”

  * Updated the base `LLM` interface to match `LLMPredictor` (#9388)
  * Deprecated `LLMPredictor` (#9388)

## [0.9.13] - 2023-12-06

Section titled “[0.9.13] - 2023-12-06”

### New Features

Section titled “New Features”

  * Added batch prediction support for `LabelledRagDataset` (#9332)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed save and load for faiss vector store (#9330)

## [0.9.12] - 2023-12-05

Section titled “[0.9.12] - 2023-12-05”

### New Features

Section titled “New Features”

  * Added an option `reuse_client` to openai/azure to help with async timeouts. Set to `False` to see improvements (#9301)
  * Added support for `vLLM` llm (#9257)
  * Add support for python 3.12 (#9304)
  * Support for `claude-2.1` model name (#9275)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix embedding format for bedrock cohere embeddings (#9265)
  * Use `delete_kwargs` for filtering in weaviate vector store (#9300)
  * Fixed automatic qdrant client construction (#9267)

## [0.9.11] - 2023-12-03

Section titled “[0.9.11] - 2023-12-03”

### New Features

Section titled “New Features”

  * Make `reference_contexts` optional in `LabelledRagDataset` (#9266)
  * Re-organize `download` module (#9253)
  * Added document management to ingestion pipeline (#9135)
  * Add docs for `LabelledRagDataset` (#9228)
  * Add submission template notebook and other doc updates for `LabelledRagDataset` (#9273)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Convert numpy to list for `InstructorEmbedding` (#9255)

## [0.9.10] - 2023-11-30

Section titled “[0.9.10] - 2023-11-30”

### New Features

Section titled “New Features”

  * Advanced Metadata filter for vector stores (#9216)
  * Amazon Bedrock Embeddings New models (#9222)
  * Added PromptLayer callback integration (#9190)
  * Reuse file ids for `OpenAIAssistant` (#9125)

### Breaking Changes / Deprecations

Section titled “Breaking Changes / Deprecations”

  * Deprecate ExactMatchFilter (#9216)

## [0.9.9] - 2023-11-29

Section titled “[0.9.9] - 2023-11-29”

### New Features

Section titled “New Features”

  * Add new abstractions for `LlamaDataset`’s (#9165)
  * Add metadata filtering and MMR mode support for `AstraDBVectorStore` (#9193)
  * Allowing newest `scikit-learn` versions (#9213)

### Breaking Changes / Deprecations

Section titled “Breaking Changes / Deprecations”

  * Added `LocalAI` demo and began deprecation cycle (#9151)
  * Deprecate `QueryResponseDataset` and `DatasetGenerator` of `evaluation` module (#9165)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix bug in `download_utils.py` with pointing to wrong repo (#9215)
  * Use `azure_deployment` kwarg in `AzureOpenAILLM` (#9174)
  * Fix similarity score return for `AstraDBVectorStore` Integration (#9193)

## [0.9.8] - 2023-11-26

Section titled “[0.9.8] - 2023-11-26”

### New Features

Section titled “New Features”

  * Add `persist` and `persist_from_dir` methods to `ObjectIndex` that are able to support it (#9064)
  * Added async metadata extraction + pipeline support (#9121)
  * Added back support for start/end char idx in nodes (#9143)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix for some kwargs not being set properly in global service context (#9137)
  * Small fix for `memory.get()` when system/prefix messages are large (#9149)
  * Minor fixes for global service context (#9137)

## [0.9.7] - 2023-11-24

Section titled “[0.9.7] - 2023-11-24”

### New Features

Section titled “New Features”

  * Add support for `PGVectoRsStore` (#9087)
  * Enforcing `requests>=2.31` for security, while unpinning `urllib3` (#9108)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Increased default memory token limit for context chat engine (#9123)
  * Added system prompt to `CondensePlusContextChatEngine` that gets prepended to the `context_prompt` (#9123)
  * Fixed bug in `CondensePlusContextChatEngine` not using chat history properly (#9129)

## [0.9.6] - 2023-11-22

Section titled “[0.9.6] - 2023-11-22”

### New Features

Section titled “New Features”

  * Added `default_headers` argument to openai LLMs (#9090)
  * Added support for `download_llama_pack()` and LlamaPack integrations
  * Added support for `llamaindex-cli` command line tool

### Bug Fixed / Nits

Section titled “Bug Fixed / Nits”

  * store normalize as bool for huggingface embedding (#9089)

## [0.9.5] - 2023-11-21

Section titled “[0.9.5] - 2023-11-21”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed bug with AzureOpenAI logic for inferring if stream chunk is a tool call (#9018)

### New Features

Section titled “New Features”

  * `FastEmbed` embeddings provider (#9043)
  * More precise testing of `OpenAILike` (#9026)
  * Added callback manager to each retriever (#8871)
  * Ability to bypass `max_tokens` inference with `OpenAILike` (#9032)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed bug in formatting chat prompt templates when estimating chunk sizes (#9025)
  * Sandboxed Pandas execution, remediate CVE-2023-39662 (#8890)
  * Restored `mypy` for Python 3.8 (#9031)
  * Loosened `dataclasses-json` version range, and removes unnecessary `jinja2` extra from `pandas` (#9042)

## [0.9.4] - 2023-11-19

Section titled “[0.9.4] - 2023-11-19”

### New Features

Section titled “New Features”

  * Added `CondensePlusContextChatEngine` (#8949)

### Smaller Features / Bug Fixes / Nits

Section titled “Smaller Features / Bug Fixes / Nits”

  * Fixed bug with `OpenAIAgent` inserting errors into chat history (#9000)
  * Fixed various bugs with LiteLLM and the new OpenAI client (#9003)
  * Added context window attribute to perplexity llm (#9012)
  * Add `node_parser` attribute back to service context (#9013)
  * Refactor MM retriever classes (#8998)
  * Fix TextNode instantiation on SupabaseVectorIndexDemo (#8994)

## [0.9.3] - 2023-11-17

Section titled “[0.9.3] - 2023-11-17”

### New Features

Section titled “New Features”

  * Add perplexity LLM integration (#8734)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix token counting for new openai client (#8981)
  * Fix small pydantic bug in postgres vector db (#8962)
  * Fixed `chunk_overlap` and `doc_id` bugs in `HierarchicalNodeParser` (#8983)

## [0.9.2] - 2023-11-16

Section titled “[0.9.2] - 2023-11-16”

### New Features

Section titled “New Features”

  * Added new notebook guide for Multi-Modal Rag Evaluation (#8945)
  * Added `MultiModalRelevancyEvaluator`, and `MultiModalFaithfulnessEvaluator` (#8945)

## [0.9.1] - 2023-11-15

Section titled “[0.9.1] - 2023-11-15”

### New Features

Section titled “New Features”

  * Added Cohere Reranker fine-tuning (#8859)
  * Support for custom httpx client in `AzureOpenAI` LLM (#8920)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed issue with `set_global_service_context` not propagating settings (#8940)
  * Fixed issue with building index with Google Palm embeddings (#8936)
  * Fixed small issue with parsing ImageDocuments/Nodes that have no text (#8938)
  * Fixed issue with large data inserts in Astra DB (#8937)
  * Optimize `QueryEngineTool` for agents (#8933)

## [0.9.0] - 2023-11-15

Section titled “[0.9.0] - 2023-11-15”

### New Features / Breaking Changes / Deprecations

Section titled “New Features / Breaking Changes / Deprecations”

  * New `IngestionPipeline` concept for ingesting and transforming data
  * Data ingestion and transforms are now automatically cached
  * Updated interface for node parsing/text splitting/metadata extraction modules
  * Changes to the default tokenizer, as well as customizing the tokenizer
  * Packaging/Installation changes with PyPi (reduced bloat, new install options)
  * More predictable and consistent import paths
  * Plus, in beta: MultiModal RAG Modules for handling text and images!
  * Find more details at: `https://medium.com/@llama_index/719f03282945`

## [0.8.69.post1] - 2023-11-13

Section titled “[0.8.69.post1] - 2023-11-13”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Increase max weaivate delete size to max of 10,000 (#8887)
  * Final pickling remnant fix (#8902)

## [0.8.69] - 2023-11-13

Section titled “[0.8.69] - 2023-11-13”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed bug in loading pickled objects (#8880)
  * Fix `custom_path` vs `custom_dir` in `download_loader` (#8865)

## [0.8.68] - 2023-11-11

Section titled “[0.8.68] - 2023-11-11”

### New Features

Section titled “New Features”

  * openai assistant agent + advanced retrieval cookbook (#8863)
  * add retrieval API benchmark (#8850)
  * Add JinaEmbedding class (#8704)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Improved default timeouts/retries for OpenAI (#8819)
  * Add back key validation for OpenAI (#8819)
  * Disable automatic LLM/Embedding model downloads, give informative error (#8819)
  * fix openai assistant tool creation + retrieval notebook (#8862)
  * Quick fix Replicate MultiModal example (#8861)
  * fix: paths treated as hidden (#8860)
  * fix Replicate multi-modal LLM + notebook (#8854)
  * Feature/citation metadata (#8722)
  * Fix ImageNode type from NodeWithScore for SimpleMultiModalQueryEngine (#8844)

## [0.8.67] - 2023-11-10

Section titled “[0.8.67] - 2023-11-10”

### New Features

Section titled “New Features”

  * Advanced Multi Modal Retrieval Example and docs (#8822, #8823)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix retriever node postprocessors for `CitationQueryEngine` (#8818)
  * Fix `cannot pickle 'builtins.CoreBPE' object` in most scenarios (#8835)

## [0.8.66] - 2023-11-09

Section titled “[0.8.66] - 2023-11-09”

### New Features

Section titled “New Features”

  * Support parallel function calling with new OpenAI client in `OpenAIPydanticProgram` (#8793)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix bug in pydantic programs with new OpenAI client (#8793)
  * Fixed bug with un-listable fsspec objects (#8795)

## [0.8.65] - 2023-11-08

Section titled “[0.8.65] - 2023-11-08”

### New Features

Section titled “New Features”

  * `OpenAIAgent` parallel function calling (#8738)

### New Features

Section titled “New Features”

  * Properly supporting Hugging Face recommended model (#8784)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed missing import for `embeddings.__all__` (#8779)

### Breaking Changes / Deprecations

Section titled “Breaking Changes / Deprecations”

  * Use `tool_choice` over `function_call` and `tool` over `functions` in `OpenAI(LLM)` (#8738)
  * Deprecate `to_openai_function` in favor of `to_openai_tool` (#8738)

## [0.8.64] - 2023-11-06

Section titled “[0.8.64] - 2023-11-06”

### New Features

Section titled “New Features”

  * `OpenAIAgent` parallel function calling (#8738)
  * Add AI assistant agent (#8735)
  * OpenAI GPT4v Abstraction (#8719)
  * Add support for `Lantern` VectorStore (#8714)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix returning zero nodes in elastic search vector store (#8746)
  * Add try/except for `SimpleDirectoryReader` loop to avoid crashing on a single document (#8744)
  * Fix for `deployment_name` in async embeddings (#8748)

## [0.8.63] - 2023-11-05

Section titled “[0.8.63] - 2023-11-05”

### New Features

Section titled “New Features”

  * added native sync and async client support for the lasted `openai` client package (#8712)
  * added support for `AzureOpenAIEmbedding` (#8712)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed errors about “no host supplied” with `download_loader` (#8723)

### Breaking Changes

Section titled “Breaking Changes”

  * `OpenAIEmbedding` no longer supports azure, moved into the `AzureOpenAIEmbedding` class (#8712)

## [0.8.62.post1] - 2023-11-05

Section titled “[0.8.62.post1] - 2023-11-05”

### Breaking Changes

Section titled “Breaking Changes”

  * add new devday models (#8713)
  * moved `max_docs` parameter from constructor to `lazy_load_data()` for `SimpleMongoReader` (#8686)

## [0.8.61] - 2023-11-05

Section titled “[0.8.61] - 2023-11-05”

### New Features

Section titled “New Features”

  * [experimental] Hyperparameter tuner (#8687)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix typo error in CohereAIModelName class: cohere light models was missing v3 (#8684)
  * Update deeplake.py (#8683)

## [0.8.60] - 2023-11-04

Section titled “[0.8.60] - 2023-11-04”

### New Features

Section titled “New Features”

  * prompt optimization guide (#8659)
  * VoyageEmbedding (#8634)
  * Multilingual support for `YoutubeTranscriptReader` (#8673)
  * emotion prompt guide (#8674)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Adds mistral 7b instruct v0.1 to available anyscale models (#8652)
  * Make pgvector’s setup (extension, schema, and table creation) optional (#8656)
  * Allow init of stores_text variable for Pinecone vector store (#8633)
  * fix: azure ad support (#8667)
  * Fix nltk bug in multi-threaded environments (#8668)
  * Fix google colab link in cohereai notebook (#8677)
  * passing max_tokens to the `Cohere` llm (#8672)

## [0.8.59] - 2023-11-02

Section titled “[0.8.59] - 2023-11-02”

  * Deepmemory support (#8625)
  * Add CohereAI embeddings (#8650)
  * Add Azure AD (Microsoft Entra ID) support (#8667)

## [0.8.58] - 2023-11-02

Section titled “[0.8.58] - 2023-11-02”

### New Features

Section titled “New Features”

  * Add `lm-format-enforcer` integration for structured output (#8601)
  * Google Vertex Support (#8626)

## [0.8.57] - 2023-10-31

Section titled “[0.8.57] - 2023-10-31”

### New Features

Section titled “New Features”

  * Add `VoyageAIEmbedding` integration (#8634)
  * Add fine-tuning evaluator notebooks (#8596)
  * Add `SingleStoreDB` integration (#7991)
  * Add support for ChromaDB PersistentClient (#8582)
  * Add DataStax Astra DB support (#8609)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Update dataType in Weaviate (#8608)
  * In Knowledge Graph Index with hybrid retriever_mode, 
    * return the nodes found by keyword search when ‘No Relationship found’
  * Fix exceed context length error in chat engines (#8530)
  * Retrieve actual content of all the triplets from KG (#8579)
  * Return the nodes found by Keywords when no relationship is found by embeddings in hybrid retriever_mode in `KnowledgeGraphIndex` (#8575)
  * Optimize content of retriever tool and minor bug fix (#8588)

## [0.8.56] - 2023-10-30

Section titled “[0.8.56] - 2023-10-30”

### New Features

Section titled “New Features”

  * Add Amazon `BedrockEmbedding` (#8550)
  * Moves `HuggingFaceEmbedding` to center on `Pooling` enum for pooling (#8467)
  * Add IBM WatsonX LLM support (#8587)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * [Bug] Patch Clarifai classes (#8529)
  * fix retries for bedrock llm (#8528)
  * Fix : VectorStore’s QueryResult always returns saved Node as TextNode (#8521)
  * Added default file_metadata to get basic metadata that many postprocessors use, for SimpleDirectoryReader (#8486)
  * Handle metadata with None values in chromadb (#8584)

## [0.8.55] - 2023-10-29

Section titled “[0.8.55] - 2023-10-29”

### New Features

Section titled “New Features”

  * allow prompts to take in functions with `function_mappings` (#8548)
  * add advanced prompt + “prompt engineering for RAG” notebook (#8555)
  * Leverage Replicate API for serving LLaVa modal (#8539)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Update pull request template with google colab support inclusion (#8525)

## [0.8.54] - 2023-10-28

Section titled “[0.8.54] - 2023-10-28”

### New Features

Section titled “New Features”

  * notebook showing how to fine-tune llama2 on structured outputs (#8540) 
    * added GradientAIFineTuningHandler
    * added pydantic_program_mode to ServiceContext
  * Initialize MultiModal Retrieval using LlamaIndex (#8507)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Add missing import to `ChatEngine` usage pattern `.md` doc (#8518)
  * :bug: fixed async add (#8531)
  * fix: add the needed CondenseQuestionChatEngine import in the usage_pa… (#8518)
  * Add import LongLLMLinguaPostprocessor for LongLLMLingua.ipynb (#8519)

## [0.8.53] - 2023-10-27

Section titled “[0.8.53] - 2023-10-27”

### New Features

Section titled “New Features”

  * Docs refactor (#8500) An overhaul of the docs organization. Major changes 
    * Added a big new “understanding” section
    * Added a big new “optimizing” section
    * Overhauled Getting Started content
    * Categorized and moved module guides to a single section

## [0.8.52] - 2023-10-26

Section titled “[0.8.52] - 2023-10-26”

### New Features

Section titled “New Features”

  * Add longllmlingua (#8485)
  * Add google colab support for notebooks (#7560)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Adapt Cassandra VectorStore constructor DB connection through cassio.init (#8255)
  * Allow configuration of service context and storage context in managed index (#8487)

## [0.8.51.post1] - 2023-10-25

Section titled “[0.8.51.post1] - 2023-10-25”

### New Features

Section titled “New Features”

  * Add Llava MultiModal QA examples for Tesla 10k RAG (#8271)
  * fix bug streaming on react chat agent not working as expected (#8459)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * patch: add selected result to response metadata for router query engines, fix bug (#8483)
  * add Jina AI embeddings notebook + huggingface embedding fix (#8478)
  * add `is_chat_model` to replicate (#8469)
  * Brought back `toml-sort` to `pre-commit` (#8267)
  * Added `LocationConstraint` for local `test_s3_kvstore` (#8263)

## [0.8.50] - 2023-10-24

Section titled “[0.8.50] - 2023-10-24”

### New Features

Section titled “New Features”

  * Expose prompts in different modules (query engines, synthesizers, and more) (#8275)

## [0.8.49] - 2023-10-23

Section titled “[0.8.49] - 2023-10-23”

### New Features

Section titled “New Features”

  * New LLM integrations 
    * Support for Hugging Face Inference API’s `conversational`, `text_generation`, and `feature_extraction` endpoints via `huggingface_hub[inference]` (#8098)
    * Add Amazon Bedrock LLMs (#8223)
    * Add AI21 Labs LLMs (#8233)
    * Add OpenAILike LLM class for OpenAI-compatible api servers (#7973)
  * New / updated vector store integrations 
    * Add DashVector (#7772)
    * Add Tencent VectorDB (#8173)
    * Add option for custom Postgres schema on PGVectorStore instead of only allowing public schema (#8080)
  * Add Gradient fine tuning engine (#8208)
  * docs(FAQ): frequently asked questions (#8249)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix inconsistencies with `ReActAgent.stream_chat` (#8147)
  * Deprecate some functions for GuardrailsOutputParser (#8016)
  * Simplify dependencies (#8236)
  * Bug fixes for LiteLLM (#7885)
  * Update for Predibase LLM (#8211)

## [0.8.48] - 2023-10-20

Section titled “[0.8.48] - 2023-10-20”

### New Features

Section titled “New Features”

  * Add `DELETE` for MyScale vector store (#8159)
  * Add SQL Retriever (#8197)
  * add semantic kernel document format (#8226)
  * Improve MyScale Hybrid Search and Add `DELETE` for MyScale vector store (#8159)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed additional kwargs in ReActAgent.from_tools() (#8206)
  * Fixed missing spaces in prompt templates (#8190)
  * Remove auto-download of llama2-13B on exception (#8225)

## [0.8.47] - 2023-10-19

Section titled “[0.8.47] - 2023-10-19”

### New Features

Section titled “New Features”

  * add response synthesis to text-to-SQL (#8196)
  * Added support for `LLMRailsEmbedding` (#8169)
  * Inferring MPS device with PyTorch (#8195)
  * Consolidated query/text prepending (#8189)

## [0.8.46] - 2023-10-18

Section titled “[0.8.46] - 2023-10-18”

### New Features

Section titled “New Features”

  * Add fine-tuning router support + embedding selector (#8174)
  * add more document converters (#8156)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Add normalization to huggingface embeddings (#8145)
  * Improve MyScale Hybrid Search (#8159)
  * Fixed duplicate `FORMAT_STR` being inside prompt (#8171)
  * Added: support for output_kwargs={‘max_colwidth’: xx} for PandasQueryEngine (#8110)
  * Minor fix in the description for an argument in cohere llm (#8163)
  * Fix Firestore client info (#8166)

## [0.8.45] - 2023-10-13

Section titled “[0.8.45] - 2023-10-13”

### New Features

Section titled “New Features”

  * Added support for fine-tuning cross encoders (#7705)
  * Added `QueryFusionRetriever` for merging multiple retrievers + query augmentation (#8100)
  * Added `nb-clean` to `pre-commit` to minimize PR diffs (#8108)
  * Support for `TextEmbeddingInference` embeddings (#8122)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Improved the `BM25Retriever` interface to accept `BaseNode` objects (#8096)
  * Fixed bug with `BM25Retriever` tokenizer not working as expected (#8096)
  * Brought mypy to pass in Python 3.8 (#8107)
  * `ReActAgent` adding missing `super().__init__` call (#8125)

## [0.8.44] - 2023-10-12

Section titled “[0.8.44] - 2023-10-12”

### New Features

Section titled “New Features”

  * add pgvector sql query engine (#8087)
  * Added HoneyHive one-click observability (#7944)
  * Add support for both SQLAlchemy V1 and V2 (#8060)

## [0.8.43.post1] - 2023-10-11

Section titled “[0.8.43.post1] - 2023-10-11”

### New Features

Section titled “New Features”

  * Moves `codespell` to `pre-commit` (#8040)
  * Added `prettier` for autoformatting extensions besides `.py` (#8072)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed forgotten f-str in `HuggingFaceLLM` (#8075)
  * Relaxed numpy/panadas reqs

## [0.8.43] - 2023-10-10

Section titled “[0.8.43] - 2023-10-10”

### New Features

Section titled “New Features”

  * Added support for `GradientEmbedding` embed models (#8050)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * added `messages_to_prompt` kwarg to `HuggingFaceLLM` (#8054)
  * improved selection and sql parsing for open-source models (#8054)
  * fixed bug when agents hallucinate too many kwargs for a tool (#8054)
  * improved prompts and debugging for selection+question generation (#8056)

## [0.8.42] - 2023-10-10

Section titled “[0.8.42] - 2023-10-10”

### New Features

Section titled “New Features”

  * `LocalAI` more intuitive module-level var names (#8028)
  * Enable `codespell` for markdown docs (#7972)
  * add unstructured table element node parser (#8036)
  * Add: Async upserting for Qdrant vector store (#7968)
  * Add cohere llm (#8023)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Parse multi-line outputs in react agent answers (#8029)
  * Add properly named kwargs to keyword `as_retriever` calls (#8011)
  * Updating Reference to RAGAS LlamaIndex Integration (#8035)
  * Vectara bugfix (#8032)
  * Fix: ChromaVectorStore can attempt to add in excess of chromadb batch… (#8019)
  * Fix get_content method in Mbox reader (#8012)
  * Apply kwarg filters in WeaviateVectorStore (#8017)
  * Avoid ZeroDivisionError (#8027)
  * `LocalAI` intuitive module-level var names (#8028)
  * zep/fix: imports & typing (#8030)
  * refactor: use `str.join` (#8020)
  * use proper metadata str for node parsing (#7987)

## [0.8.41] - 2023-10-07

Section titled “[0.8.41] - 2023-10-07”

### New Features

Section titled “New Features”

  * You.com retriever (#8024)
  * Pull fields from mongodb into metadata with `metadata_names` argument (#8001)
  * Simplified `LocalAI.__init__` preserving the same behaviors (#7982)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Use longest metadata string for metadata aware text splitting (#7987)
  * Handle lists of strings in mongodb reader (#8002)
  * Removes `OpenAI.class_type` as it was dead code (#7983)
  * Fixing `HuggingFaceLLM.device_map` type hint (#7989)

## [0.8.40] - 2023-10-05

Section titled “[0.8.40] - 2023-10-05”

### New Features

Section titled “New Features”

  * Added support for `Clarifai` LLM (#7967)
  * Add support for function fine-tuning (#7971)

### Breaking Changes

Section titled “Breaking Changes”

  * Update document summary index (#7815) 
    * change default retrieval mode to embedding
    * embed summaries into vector store by default at indexing time (instead of calculating embedding on the fly)
    * support configuring top k in llm retriever

## [0.8.39] - 2023-10-03

Section titled “[0.8.39] - 2023-10-03”

### New Features

Section titled “New Features”

  * Added support for pydantic object outputs with query engines (#7893)
  * `ClarifaiEmbedding` class added for embedding support (#7940)
  * Markdown node parser, flat file reader and simple file node parser (#7863)
  * Added support for mongdb atlas `$vectorSearch` (#7866)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Adds support for using message metadata in discord reader (#7906)
  * Fix `LocalAI` chat capability without `max_tokens` (#7942)
  * Added `codespell` for automated checking (#7941)
  * `ruff` modernization and autofixes (#7889)
  * Implement own SQLDatabase class (#7929)
  * Update LlamaCPP context_params property (#7945)
  * fix duplicate embedding (#7949)
  * Adds `codespell` tool for enforcing good spelling (#7941)
  * Supporting `mypy` local usage with `venv` (#7952)
  * Vectara - minor update (#7954)
  * Avoiding `pydantic` reinstalls in CI (#7956)
  * move tree_sitter_languages into data_requirements.txt (#7955)
  * Add `cache_okay` param to `PGVectorStore` to help suppress TSVector warnings (#7950)

## [0.8.38] - 2023-10-02

Section titled “[0.8.38] - 2023-10-02”

### New Features

Section titled “New Features”

  * Updated `KeywordNodePostprocessor` to use spacy to support more languages (#7894)
  * `LocalAI` supporting global or per-query `/chat/completions` vs `/completions` (#7921)
  * Added notebook on using REBEL + Wikipedia filtering for knowledge graphs (#7919)
  * Added support for `ElasticsearchEmbedding` (#7914)

## [0.8.37] - 2023-09-30

Section titled “[0.8.37] - 2023-09-30”

### New Features

Section titled “New Features”

  * Supporting `LocalAI` LLMs (#7913)
  * Validations protecting against misconfigured chunk sizes (#7917)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Simplify NL SQL response to SQL parsing, with expanded NL SQL prompt (#7868)
  * Improve vector store retrieval speed for vectordb integrations (#7876)
  * Added replacing {{ and }}, and fixed JSON parsing recursion (#7888)
  * Nice-ified JSON decoding error (#7891)
  * Nice-ified SQL error from LLM not providing SQL (#7900)
  * Nice-ified `ImportError` for `HuggingFaceLLM` (#7904)
  * eval fixes: fix dataset response generation, add score to evaluators (#7915)

## [0.8.36] - 2023-09-27

Section titled “[0.8.36] - 2023-09-27”

### New Features

Section titled “New Features”

  * add “build RAG from scratch notebook” - OSS/local (#7864)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix elasticsearch hybrid scoring (#7852)
  * Replace `get_color_mapping` and `print_text` Langchain dependency with internal implementation (#7845)
  * Fix async streaming with azure (#7856)
  * Avoid `NotImplementedError()` in sub question generator (#7855)
  * Patch predibase initialization (#7859)
  * Bumped min langchain version and changed prompt imports from langchain (#7862)

## [0.8.35] - 2023-09-27

Section titled “[0.8.35] - 2023-09-27”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix dropping textnodes in recursive retriever (#7840)
  * share callback_manager between agent and its llm when callback_manager is None (#7844)
  * fix pandas query engine (#7847)

## [0.8.34] - 2023-09-26

Section titled “[0.8.34] - 2023-09-26”

### New Features

Section titled “New Features”

  * Added `Konko` LLM support (#7775)
  * Add before/after context sentence (#7821)
  * EverlyAI integration with LlamaIndex through OpenAI library (#7820)
  * add Arize Phoenix tracer to global handlers (#7835)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Normalize scores returned from ElasticSearch vector store (#7792)
  * Fixed `refresh_ref_docs()` bug with order of operations (#7664)
  * Delay postgresql connection for `PGVectorStore` until actually needed (#7793)
  * Fix KeyError in delete method of `SimpleVectorStore` related to metadata filters (#7829)
  * Fix KeyError in delete method of `SimpleVectorStore` related to metadata filters (#7831)
  * Addressing PyYAML import error (#7784)
  * ElasticsearchStore: Update User-Agent + Add example docker compose (#7832)
  * `StorageContext.persist` supporting `Path` (#7783)
  * Update ollama.py (#7839)
  * fix bug for self._session_pool (#7834)

## [0.8.33] - 2023-09-25

Section titled “[0.8.33] - 2023-09-25”

### New Features

Section titled “New Features”

  * add pairwise evaluator + benchmark auto-merging retriever (#7810)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Minor cleanup in embedding class (#7813)
  * Misc updates to `OpenAIEmbedding` (#7811)

## [0.8.32] - 2023-09-24

Section titled “[0.8.32] - 2023-09-24”

### New Features

Section titled “New Features”

  * Added native support for `HuggingFaceEmbedding`, `InstructorEmbedding`, and `OptimumEmbedding` (#7795)
  * Added metadata filtering and hybrid search to MyScale vector store (#7780)
  * Allowing custom text field name for Milvus (#7790)
  * Add support for `vector_store_query_mode` to `VectorIndexAutoRetriever` (#7797)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Update `LanceDBVectorStore` to handle score and distance (#7754)
  * Pass LLM to `memory_cls` in `CondenseQuestionChatEngine` (#7785)

## [0.8.31] - 2023-09-22

Section titled “[0.8.31] - 2023-09-22”

### New Features

Section titled “New Features”

  * add pydantic metadata extractor (#7778)
  * Allow users to set the embedding dimensions in azure cognitive vector store (#7734)
  * Add semantic similarity evaluator (#7770)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * 📝docs: Update Chatbot Tutorial and Notebook (#7767)
  * Fixed response synthesizers with empty nodes (#7773)
  * Fix `NotImplementedError` in auto vector retriever (#7764)
  * Multiple kwargs values in “KnowledgeGraphQueryEngine” bug-fix (#7763)
  * Allow setting azure cognitive search dimensionality (#7734)
  * Pass service context to index for dataset generator (#7748)
  * Fix output parsers for selector templates (#7774)
  * Update Chatbot_SEC.ipynb (#7711)
  * linter/typechecker-friendly improvements to cassandra test (#7771)
  * Expose debug option of `PgVectorStore` (#7776)
  * llms/openai: fix Azure OpenAI by considering `prompt_filter_results` field (#7755)

## [0.8.30] - 2023-09-21

Section titled “[0.8.30] - 2023-09-21”

### New Features

Section titled “New Features”

  * Add support for `gpt-3.5-turbo-instruct` (#7729)
  * Add support for `TimescaleVectorStore` (#7727)
  * Added `LongContextReorder` for lost-in-the-middle issues (#7719)
  * Add retrieval evals (#7738)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Added node post-processors to async context chat engine (#7731)
  * Added unique index name for postgres tsv column (#7741)

## [0.8.29.post1] - 2023-09-18

Section titled “[0.8.29.post1] - 2023-09-18”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix langchain import error for embeddings (#7714)

## [0.8.29] - 2023-09-18

Section titled “[0.8.29] - 2023-09-18”

### New Features

Section titled “New Features”

  * Added metadata filtering to the base simple vector store (#7564)
  * add low-level router guide (#7708)
  * Add CustomQueryEngine class (#7703)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix context window metadata in lite-llm (#7696)

## [0.8.28] - 2023-09-16

Section titled “[0.8.28] - 2023-09-16”

### New Features

Section titled “New Features”

  * Add CorrectnessEvaluator (#7661)
  * Added support for `Ollama` LLMs (#7635)
  * Added `HWPReader` (#7672)
  * Simplified portkey LLM interface (#7669)
  * Added async operation support to `ElasticsearchStore` vector store (#7613)
  * Added support for `LiteLLM` (#7600)
  * Added batch evaluation runner (#7692)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Avoid `NotImplementedError` for async langchain embeddings (#7668)
  * Imrpoved reliability of LLM selectors (#7678)
  * Fixed `query_wrapper_prompt` and `system_prompt` for output parsers and completion models (#7678)
  * Fixed node attribute inheritance in citation query engine (#7675)

### Breaking Changes

Section titled “Breaking Changes”

  * Refactor and update `BaseEvaluator` interface to be more consistent (#7661) 
    * Use `evaluate` function for generic input
    * Use `evaluate_response` function with `Response` objects from llama index query engine
  * Update existing evaluators with more explicit naming 
    * `ResponseEvaluator` -> `FaithfulnessEvaluator`
    * `QueryResponseEvaluator` -> `RelevancyEvaluator`
    * old names are kept as class aliases for backwards compatibility

## [0.8.27] - 2023-09-14

Section titled “[0.8.27] - 2023-09-14”

### New Features

Section titled “New Features”

  * add low-level tutorial section (#7673)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * default delta should be a dict (#7665)
  * better query wrapper logic on LLMPredictor (#7667)

## [0.8.26] - 2023-09-12

Section titled “[0.8.26] - 2023-09-12”

### New Features

Section titled “New Features”

  * add non-linear embedding adapter (#7658)
  * Add “finetune + RAG” evaluation to knowledge fine-tuning notebook (#7643)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed chunk-overlap for sentence splitter (#7590)

## [0.8.25] - 2023-09-12

Section titled “[0.8.25] - 2023-09-12”

### New Features

Section titled “New Features”

  * Added `AGENT_STEP` callback event type (#7652)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Allowed `simple` mode to work with `as_chat_engine()` (#7637)
  * Fixed index error in azure streaming (#7646)
  * Removed `pdb` from llama-cpp (#7651)

## [0.8.24] - 2023-09-11

Section titled “[0.8.24] - 2023-09-11”

## New Features

Section titled “New Features”

  * guide: fine-tuning to memorize knowledge (#7626)
  * added ability to customize prompt template for eval modules (#7626)

### Bug Fixes

Section titled “Bug Fixes”

  * Properly detect `llama-cpp-python` version for loading the default GGML or GGUF `llama2-chat-13b` model (#7616)
  * Pass in `summary_template` properly with `RetrieverQueryEngine.from_args()` (#7621)
  * Fix span types in wandb callback (#7631)

## [0.8.23] - 2023-09-09

Section titled “[0.8.23] - 2023-09-09”

### Bug Fixes

Section titled “Bug Fixes”

  * Make sure context and system prompt is included in prompt for first chat for llama2 (#7597)
  * Avoid negative chunk size error in refine process (#7607)
  * Fix relationships for small documents in hierarchical node parser (#7611)
  * Update Anyscale Endpoints integration with full streaming and async support (#7602)
  * Better support of passing credentials as LLM constructor args in `OpenAI`, `AzureOpenAI`, and `Anyscale` (#7602)

### Breaking Changes

Section titled “Breaking Changes”

  * Update milvus vector store to support filters and dynamic schemas (#7286) 
    * See the [updated notebook](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo.html) for usage
  * Added NLTK to core dependencies to support the default sentence splitter (#7606)

## [0.8.22] - 2023-09-07

Section titled “[0.8.22] - 2023-09-07”

### New Features

Section titled “New Features”

  * Added support for ElasticSearch Vector Store (#7543)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed small `_index` bug in `ElasticSearchReader` (#7570)
  * Fixed bug with prompt helper settings in global service contexts (#7576)
  * Remove newlines from openai embeddings again (#7588)
  * Fixed small bug with setting `query_wrapper_prompt` in the service context (#7585)

### Breaking/Deprecated API Changes

Section titled “Breaking/Deprecated API Changes”

  * Clean up vector store interface to use `BaseNode` instead of `NodeWithEmbedding`
    * For majority of users, this is a no-op change
    * For users directly operating with the `VectorStore` abstraction and manually constructing `NodeWithEmbedding` objects, this is a minor breaking change. Use `TextNode` with `embedding` set directly, instead of `NodeWithEmbedding`.

## [0.8.21] - 2023-09-06

Section titled “[0.8.21] - 2023-09-06”

### New Features

Section titled “New Features”

  * add embedding adapter fine-tuning engine + guide (#7565)
  * Added support for Azure Cognitive Search vector store (#7469)
  * Support delete in supabase (#6951)
  * Added support for Espilla vector store (#7539)
  * Added support for AnyScale LLM (#7497)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Default to user-configurable top-k in `VectorIndexAutoRetriever` (#7556)
  * Catch validation errors for structured responses (#7523)
  * Fix streaming refine template (#7561)

## [0.8.20] - 2023-09-04

Section titled “[0.8.20] - 2023-09-04”

### New Features

Section titled “New Features”

  * Added Portkey LLM integration (#7508)
  * Support postgres/pgvector hybrid search (#7501)
  * upgrade recursive retriever node reference notebook (#7537)

## [0.8.19] - 2023-09-03

Section titled “[0.8.19] - 2023-09-03”

### New Features

Section titled “New Features”

  * replace list index with summary index (#7478)
  * rename list index to summary index part 2 (#7531)

## [0.8.18] - 2023-09-03

Section titled “[0.8.18] - 2023-09-03”

### New Features

Section titled “New Features”

  * add agent finetuning guide (#7526)

## [0.8.17] - 2023-09-02

Section titled “[0.8.17] - 2023-09-02”

### New Features

Section titled “New Features”

  * Make (some) loaders serializable (#7498)
  * add node references to recursive retrieval (#7522)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Raise informative error when metadata is too large during splitting (#7513)
  * Allow langchain splitter in simple node parser (#7517)

## [0.8.16] - 2023-09-01

Section titled “[0.8.16] - 2023-09-01”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * fix link to Marvin notebook in docs (#7504)
  * Ensure metadata is not `None` in `SimpleWebPageReader` (#7499)
  * Fixed KGIndex visualization (#7493)
  * Improved empty response in KG Index (#7493)

## [0.8.15] - 2023-08-31

Section titled “[0.8.15] - 2023-08-31”

### New Features

Section titled “New Features”

  * Added support for `MarvinEntityExtractor` metadata extractor (#7438)
  * Added a url_metadata callback to SimpleWebPageReader (#7445)
  * Expanded callback logging events (#7472)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Only convert newlines to spaces for text 001 embedding models in OpenAI (#7484)
  * Fix `KnowledgeGraphRagRetriever` for non-nebula indexes (#7488)
  * Support defined embedding dimension in `PGVectorStore` (#7491)
  * Greatly improved similarity calculation speed for the base vector store (#7494)

## [0.8.14] - 2023-08-30

Section titled “[0.8.14] - 2023-08-30”

### New Features

Section titled “New Features”

  * feat: non-kg heterogeneous graph support in Graph RAG (#7459)
  * rag guide (#7480)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Improve openai fine-tuned model parsing (#7474)
  * doing some code de-duplication (#7468)
  * support both str and templates for query_wrapper_prompt in HF LLMs (#7473)

## [0.8.13] - 2023-08-29

Section titled “[0.8.13] - 2023-08-29”

### New Features

Section titled “New Features”

  * Add embedding finetuning (#7452)
  * Added support for RunGPT LLM (#7401)
  * Integration guide and notebook with DeepEval (#7425)
  * Added `VectorIndex` and `VectaraRetriever` as a managed index (#7440)
  * Added support for `to_tool_list` to detect and use async functions (#7282)

## [0.8.12] - 2023-08-28

Section titled “[0.8.12] - 2023-08-28”

### New Features

Section titled “New Features”

  * add openai finetuning class (#7442)
  * Service Context to/from dict (#7395)
  * add finetuning guide (#7429)

### Smaller Features / Nits / Bug Fixes

Section titled “Smaller Features / Nits / Bug Fixes”

  * Add example how to run FalkorDB docker (#7441)
  * Update root.md to use get_response_synthesizer expected type. (#7437)
  * Bugfix MonsterAPI Pydantic version v2/v1 support. Doc Update (#7432)

## [0.8.11.post3] - 2023-08-27

Section titled “[0.8.11.post3] - 2023-08-27”

### New Features

Section titled “New Features”

  * AutoMergingRetriever (#7420)

## [0.8.10.post1] - 2023-08-25

Section titled “[0.8.10.post1] - 2023-08-25”

### New Features

Section titled “New Features”

  * Added support for `MonsterLLM` using MonsterAPI (#7343)
  * Support comments fields in NebulaGraphStore and int type VID (#7402)
  * Added configurable endpoint for DynamoDB (#6777)
  * Add structured answer filtering for Refine response synthesizer (#7317)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Use `utf-8` for json file reader (#7390)
  * Fix entity extractor initialization (#7407)

## [0.8.9] - 2023-08-24

Section titled “[0.8.9] - 2023-08-24”

### New Features

Section titled “New Features”

  * Added support for FalkorDB/RedisGraph graph store (#7346)
  * Added directed sub-graph RAG (#7378)
  * Added support for `BM25Retriever` (#7342)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Added `max_tokens` to `Xinference` LLM (#7372)
  * Support cache dir creation in multithreaded apps (#7365)
  * Ensure temperature is a float for openai (#7382)
  * Remove duplicate subjects in knowledge graph retriever (#7378)
  * Added support for both pydantic v1 and v2 to allow other apps to move forward (#7394)

### Breaking/Deprecated API Changes

Section titled “Breaking/Deprecated API Changes”

  * Refactor prompt template (#7319) 
    * Use `BasePromptTemplate` for generic typing
    * Use `PromptTemplate`, `ChatPromptTemplate`, `SelectorPromptTemplate` as core implementations
    * Use `LangchainPromptTemplate` for compatibility with Langchain prompt templates
    * Fully replace specific prompt classes (e.g. `SummaryPrompt`) with generic `BasePromptTemplate` for typing in codebase.
    * Keep `Prompt` as an alias for `PromptTemplate` for backwards compatibility.
    * BREAKING CHANGE: remove support for `Prompt.from_langchain_prompt`, please use `template=LangchainPromptTemplate(lc_template)` instead.

## [0.8.8] - 2023-08-23

Section titled “[0.8.8] - 2023-08-23”

### New Features

Section titled “New Features”

  * `OpenAIFineTuningHandler` for collecting LLM inputs/outputs for OpenAI fine tuning (#7367)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Add support for `claude-instant-1.2` (#7369)

## [0.8.7] - 2023-08-22

Section titled “[0.8.7] - 2023-08-22”

### New Features

Section titled “New Features”

  * Support fine-tuned OpenAI models (#7364)
  * Added support for Cassandra vector store (#6784)
  * Support pydantic fields in tool functions (#7348)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix infinite looping with forced function call in `OpenAIAgent` (#7363)

## [0.8.6] - 2023-08-22

Section titled “[0.8.6] - 2023-08-22”

### New Features

Section titled “New Features”

  * auto vs. recursive retriever notebook (#7353)
  * Reader and Vector Store for BagelDB with example notebooks (#7311)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Use service context for intermediate index in retry source query engine (#7341)
  * temp fix for prompt helper + chat models (#7350)
  * Properly skip unit-tests when packages not installed (#7351)

## [0.8.5.post2] - 2023-08-20

Section titled “[0.8.5.post2] - 2023-08-20”

### New Features

Section titled “New Features”

  * Added FireStore docstore/index store support (#7305)
  * add recursive agent notebook (#7330)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix Azure pydantic error (#7329)
  * fix callback trace ids (make them a context var) (#7331)

## [0.8.5.post1] - 2023-08-18

Section titled “[0.8.5.post1] - 2023-08-18”

### New Features

Section titled “New Features”

  * Awadb Vector Store (#7291)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix bug in OpenAI llm temperature type

## [0.8.5] - 2023-08-18

Section titled “[0.8.5] - 2023-08-18”

### New Features

Section titled “New Features”

  * Expose a system prompt/query wrapper prompt in the service context for open-source LLMs (#6647)
  * Changed default MyScale index format to `MSTG` (#7288)
  * Added tracing to chat engines/agents (#7304)
  * move LLM and embeddings to pydantic (#7289)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix sentence splitter bug (#7303)
  * Fix sentence splitter infinite loop (#7295)

## [0.8.4] - 2023-08-17

Section titled “[0.8.4] - 2023-08-17”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Improve SQL Query parsing (#7283)
  * Fix loading embed_model from global service context (#7284)
  * Limit langchain version until we migrate to pydantic v2 (#7297)

## [0.8.3] - 2023-08-16

Section titled “[0.8.3] - 2023-08-16”

### New Features

Section titled “New Features”

  * Added Knowledge Graph RAG Retriever (#7204)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * accept `api_key` kwarg in OpenAI LLM class constructor (#7263)
  * Fix to create separate queue instances for separate instances of `StreamingAgentChatResponse` (#7264)

## [0.8.2.post1] - 2023-08-14

Section titled “[0.8.2.post1] - 2023-08-14”

### New Features

Section titled “New Features”

  * Added support for Rockset as a vector store (#7111)

### Bug Fixes

Section titled “Bug Fixes”

  * Fixed bug in service context definition that could disable LLM (#7261)

## [0.8.2] - 2023-08-14

Section titled “[0.8.2] - 2023-08-14”

### New Features

Section titled “New Features”

  * Enable the LLM or embedding model to be disabled by setting to `None` in the service context (#7255)
  * Resolve nearly any huggingface embedding model using the `embed_model="local:<model_name>"` syntax (#7255)
  * Async tool-calling support (#7239)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Updated supabase kwargs for add and query (#7103)
  * Small tweak to default prompts to allow for more general purpose queries (#7254)
  * Make callback manager optional for `CustomLLM` \+ docs update (#7257)

## [0.8.1] - 2023-08-13

Section titled “[0.8.1] - 2023-08-13”

### New Features

Section titled “New Features”

  * feat: add node_postprocessors to ContextChatEngine (#7232)
  * add ensemble query engine tutorial (#7247)

### Smaller Features

Section titled “Smaller Features”

  * Allow EMPTY keys for Fastchat/local OpenAI API endpoints (#7224)

## [0.8.0] - 2023-08-11

Section titled “[0.8.0] - 2023-08-11”

### New Features

Section titled “New Features”

  * Added “LLAMA_INDEX_CACHE_DIR” to control cached files (#7233)
  * Default to pydantic selectors when possible (#7154, #7223)
  * Remove the need for langchain wrappers on `embed_model` in the service context (#7157)
  * Metadata extractors take an `LLM` object now, in addition to `LLMPredictor` (#7202)
  * Added local mode + fallback to llama.cpp + llama2 (#7200)
  * Added local fallback for embeddings to `BAAI/bge-small-en` (#7200)
  * Added `SentenceWindowNodeParser` \+ `MetadataReplacementPostProcessor` (#7211)

### Breaking Changes

Section titled “Breaking Changes”

  * Change default LLM to gpt-3.5-turbo from text-davinci-003 (#7223)
  * Change prompts for compact/refine/tree_summarize to work better with gpt-3.5-turbo (#7150, #7179, #7223)
  * Increase default LLM temperature to 0.1 (#7180)

## [0.7.24.post1] - 2023-08-11

Section titled “[0.7.24.post1] - 2023-08-11”

### Other Changes

Section titled “Other Changes”

  * Reverted #7223 changes to defaults (#7235)

## [0.7.24] - 2023-08-10

Section titled “[0.7.24] - 2023-08-10”

### New Features

Section titled “New Features”

  * Default to pydantic selectors when possible (#7154, #7223)
  * Remove the need for langchain wrappers on `embed_model` in the service context (#7157)
  * Metadata extractors take an `LLM` object now, in addition to `LLMPredictor` (#7202)
  * Added local mode + fallback to llama.cpp + llama2 (#7200)
  * Added local fallback for embeddings to `BAAI/bge-small-en` (#7200)
  * Added `SentenceWindowNodeParser` \+ `MetadataReplacementPostProcessor` (#7211)

### Breaking Changes

Section titled “Breaking Changes”

  * Change default LLM to gpt-3.5-turbo from text-davinci-003 (#7223)
  * Change prompts for compact/refine/tree_summarize to work better with gpt-3.5-turbo (#7150, #7179, #7223)
  * Increase default LLM temperature to 0.1 (#7180)

### Other Changes

Section titled “Other Changes”

  * docs: Improvements to Mendable Search (#7220)
  * Refactor openai agent (#7077)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Use `1 - cosine_distance` for pgvector/postgres vector db (#7217)
  * fix metadata formatting and extraction (#7216)
  * fix(readers): Fix non-ASCII JSON Reader bug (#7086)
  * Chore: change PgVectorStore variable name from `sim` to `distance` for clarity (#7226)

## [0.7.23] - 2023-08-10

Section titled “[0.7.23] - 2023-08-10”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed metadata formatting with custom tempalates and inheritance (#7216)

## [0.7.23] - 2023-08-10

Section titled “[0.7.23] - 2023-08-10”

### New Features

Section titled “New Features”

  * Add “one click observability” page to docs (#7183)
  * Added Xorbits inference for local deployments (#7151)
  * Added Zep vector store integration (#7203)
  * feat/zep vectorstore (#7203)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Update the default `EntityExtractor` model (#7209)
  * Make `ChatMemoryBuffer` pickleable (#7205)
  * Refactored `BaseOpenAIAgent` (#7077)

## [0.7.22] - 2023-08-08

Section titled “[0.7.22] - 2023-08-08”

### New Features

Section titled “New Features”

  * add ensemble retriever notebook (#7190)
  * DOCS: added local llama2 notebook (#7146)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix for `AttributeError: 'OpenAIAgent' object has no attribute 'callback_manager'` by calling super constructor within `BaseOpenAIAgent`
  * Remove backticks from nebula queries (#7192)

## [0.7.21] - 2023-08-07

Section titled “[0.7.21] - 2023-08-07”

### New Features

Section titled “New Features”

  * Added an `EntityExtractor` for metadata extraction (#7163)

## [0.7.20] - 2023-08-06

Section titled “[0.7.20] - 2023-08-06”

### New Features

Section titled “New Features”

  * add router module docs (#7171)
  * add retriever router (#7166)

### New Features

Section titled “New Features”

  * Added a `RouterRetriever` for routing queries to specific retrievers (#7166)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix for issue where having multiple concurrent streamed responses from `OpenAIAgent` would result in interleaving of tokens across each response stream. (#7164)
  * fix llms callbacks issue (args[0] error) (#7165)

## [0.7.19] - 2023-08-04

Section titled “[0.7.19] - 2023-08-04”

### New Features

Section titled “New Features”

  * Added metadata filtering to weaviate (#7130)
  * Added token counting (and all callbacks) to agents and streaming (#7122)

## [0.7.18] - 2023-08-03

Section titled “[0.7.18] - 2023-08-03”

### New Features

Section titled “New Features”

  * Added `to/from_string` and `to/from_dict` methods to memory objects (#7128)
  * Include columns comments from db tables in table info for SQL queries (#7124)
  * Add Neo4j support (#7122)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Added `Azure AD` validation support to the `AzureOpenAI` class (#7127)
  * add `flush=True` when printing agent/chat engine response stream (#7129)
  * Added `Azure AD` support to the `AzureOpenAI` class (#7127)
  * Update LLM question generator prompt to mention JSON markdown (#7105)
  * Fixed `astream_chat` in chat engines (#7139)

## [0.7.17] - 2023-08-02

Section titled “[0.7.17] - 2023-08-02”

### New Features

Section titled “New Features”

  * Update `ReActAgent` to support memory modules (minor breaking change since the constructor takes `memory` instead of `chat_history`, but the main `from_tools` method remains backward compatible.) (#7116)
  * Update `ReActAgent` to support streaming (#7119)
  * Added Neo4j graph store and query engine integrations (#7122)
  * add object streaming (#7117)

## [0.7.16] - 2023-07-30

Section titled “[0.7.16] - 2023-07-30”

### New Features

Section titled “New Features”

  * Chat source nodes (#7078)

## [0.7.15] - 2023-07-29

Section titled “[0.7.15] - 2023-07-29”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * anthropic api key customization (#7082)
  * Fix broken link to API reference in Contributor Docs (#7080)
  * Update vector store docs (#7076)
  * Update comment (#7073)

## [0.7.14] - 2023-07-28

Section titled “[0.7.14] - 2023-07-28”

### New Features

Section titled “New Features”

  * Added HotpotQADistractor benchmark evaluator (#7034)
  * Add metadata filter and delete support for LanceDB (#7048)
  * Use MetadataFilters in opensearch (#7005)
  * Added support for `KuzuGraphStore` (#6970)
  * Added `kg_triplet_extract_fn` to customize how KGs are built (#7068)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix string formatting in context chat engine (#7050)
  * Fixed tracing for async events (#7052)
  * Less strict triplet extraction for KGs (#7059)
  * Add configurable limit to KG data retrieved (#7059)
  * Nebula connection improvements (#7059)
  * Bug fix in building source nodes for agent response (#7067)

## [0.7.13] - 2023-07-26

Section titled “[0.7.13] - 2023-07-26”

### New Features

Section titled “New Features”

  * Support function calling api for AzureOpenAI (#7041)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * tune prompt to get rid of KeyError in SubQ engine (#7039)
  * Fix validation of Azure OpenAI keys (#7042)

## [0.7.12] - 2023-07-25

Section titled “[0.7.12] - 2023-07-25”

### New Features

Section titled “New Features”

  * Added `kwargs` to `ComposableGraph` for the underlying query engines (#6990)
  * Validate openai key on init (#6940)
  * Added async embeddings and async RetrieverQueryEngine (#6587)
  * Added async `aquery` and `async_add` to PGVectorStore (#7031)
  * Added `.source_nodes` attribute to chat engine and agent responses (#7029)
  * Added `OpenInferenceCallback` for storing generation data in OpenInference format (#6998)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix achat memory initialization for data agents (#7000)
  * Add `print_response_stream()` to agengt/chat engine response class (#7018)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix achat memory initialization for data agents (#7000)
  * Add `print_response_stream()` to agengt/chat engine response class (#7018)

## [v0.7.11.post1] - 2023-07-20

Section titled “[v0.7.11.post1] - 2023-07-20”

### New Features

Section titled “New Features”

  * Default to pydantic question generation when possible for sub-question query engine (#6979)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix returned order of messages in large chat memory (#6979)

## [v0.7.11] - 2023-07-19

Section titled “[v0.7.11] - 2023-07-19”

### New Features

Section titled “New Features”

  * Added a `SentenceTransformerRerank` node post-processor for fast local re-ranking (#6934)
  * Add numpy support for evaluating queries in pandas query engine (#6935)
  * Add metadata filtering support for Postgres Vector Storage integration (#6968)
  * Proper llama2 support for agents and query engines (#6969)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Added `model_name` to LLMMetadata (#6911)
  * Fallback to retriever service context in query engines (#6911)
  * Fixed `as_chat_engine()` ValueError with extra kwargs (#6971

## [v0.7.10.post1] - 2023-07-18

Section titled “[v0.7.10.post1] - 2023-07-18”

### New Features

Section titled “New Features”

  * Add support for Replicate LLM (vicuna & llama 2!)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * fix streaming for condense chat engine (#6958)

## [v0.7.10] - 2023-07-17

Section titled “[v0.7.10] - 2023-07-17”

### New Features

Section titled “New Features”

  * Add support for chroma v0.4.0 (#6937)
  * Log embedding vectors to callback manager (#6962)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * add more robust embedding timeouts (#6779)
  * improved connection session management on postgres vector store (#6843)

## [v0.7.9] - 2023-07-15

Section titled “[v0.7.9] - 2023-07-15”

### New Features

Section titled “New Features”

  * specify `embed_model="local"` to use default local embbeddings in the service context (#6806)
  * Add async `acall` endpoint to `BasePydanticProgram` (defaults to sync version). Implement for `OpenAIPydanticProgram`

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * fix null metadata for searching existing vector dbs (#6912)
  * add module guide docs for `SimpleDirectoryReader` (#6916)
  * make sure `CondenseQuestionChatEngine` streaming chat endpoints work even if not explicitly setting `streaming=True` in the underlying query engine.

## [v0.7.8] - 2023-07-13

Section titled “[v0.7.8] - 2023-07-13”

### New Features

Section titled “New Features”

  * Added embedding speed benchmark (#6876)
  * Added BEIR retrieval benchmark (#6825)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * remove toctrees from deprecated_terms (#6895)
  * Relax typing dependencies (#6879)
  * docs: modification to evaluation notebook (#6840)
  * raise error if the model does not support functions (#6896)
  * fix(bench embeddings): bug not taking into account string length (#6899)x

## [v0.7.7] - 2023-07-13

Section titled “[v0.7.7] - 2023-07-13”

### New Features

Section titled “New Features”

  * Improved milvus consistency support and output fields support (#6452)
  * Added support for knowledge graph querying w/ cypyer+nebula (#6642)
  * Added `Document.example()` to create documents for fast prototyping (#6739)
  * Replace react chat engine to use native reactive agent (#6870)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * chore: added a help message to makefile (#6861)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed support for using SQLTableSchema context_str attribute (#6891)

## [v0.7.6] - 2023-07-12

Section titled “[v0.7.6] - 2023-07-12”

### New Features

Section titled “New Features”

  * Added sources to agent/chat engine responses (#6854)
  * Added basic chat buffer memory to agents / chat engines (#6857)
  * Adding load and search tool (#6871)
  * Add simple agent benchmark (#6869)
  * add agent docs (#6866)
  * add react agent (#6865)

### Breaking/Deprecated API Changes

Section titled “Breaking/Deprecated API Changes”

  * Replace react chat engine with native react agent (#6870)
  * Set default chat mode to “best”: use openai agent when possible, otherwise use react agent (#6870)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fixed support for legacy vector store metadata (#6867)
  * fix chroma notebook in docs (#6872)
  * update LC embeddings docs (#6868)

## [v0.7.5] - 2023-07-11

Section titled “[v0.7.5] - 2023-07-11”

### New Features

Section titled “New Features”

  * Add `Anthropic` LLM implementation (#6855)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix indexing error in `SentenceEmbeddingOptimizer` (#6850)
  * fix doc for custom embedding model (#6851)
  * fix(silent error): Add validation to `SimpleDirectoryReader` (#6819)
  * Fix link in docs (#6833)
  * Fixes Azure gpt-35-turbo model not recognized (#6828)
  * Update Chatbot_SEC.ipynb (#6808)
  * Rename leftover original name to LlamaIndex (#6792)
  * patch nested traces of the same type (#6791)

## [v0.7.4] - 2023-07-08

Section titled “[v0.7.4] - 2023-07-08”

### New Features

Section titled “New Features”

  * `MetadataExtractor` \- Documnent Metadata Augmentation via LLM-based feature extractors (#6764)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * fixed passing in query bundle to node postprocessors (#6780)
  * fixed error in callback manager with nested traces (#6791)

## [v0.7.3] - 2023-07-07

Section titled “[v0.7.3] - 2023-07-07”

### New Features

Section titled “New Features”

  * Sub question query engine returns source nodes of sub questions in the callback manager (#6745)
  * trulens integration (#6741)
  * Add sources to subquestion engine (#6745)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Added/Fixed streaming support to simple and condense chat engines (#6717)
  * fixed `response_mode="no_text"` response synthesizer (#6755)
  * fixed error setting `num_output` and `context_window` in service context (#6766)
  * Fix missing as_query_engine() in tutorial (#6747)
  * Fixed variable sql_query_engine in the notebook (#6778)
  * fix required function fields (#6761)
  * Remove usage of stop token in Prompt, SQL gen (#6782)

## [v0.7.2] - 2023-07-06

Section titled “[v0.7.2] - 2023-07-06”

### New Features

Section titled “New Features”

  * Support Azure OpenAI (#6718)
  * Support prefix messages (e.g. system prompt) in chat engine and OpenAI agent (#6723)
  * Added `CBEventType.SUB_QUESTIONS` event type for tracking sub question queries/responses (#6716)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix HF LLM output error (#6737)
  * Add system message support for langchain message templates (#6743)
  * Fixed applying node-postprocessors (#6749)
  * Add missing `CustomLLM` import under `llama_index.llms` (#6752)
  * fix(typo): `get_transformer_tokenizer_fn` (#6729)
  * feat(formatting): `black[jupyter]` (#6732)
  * fix(test): `test_optimizer_chinese` (#6730)

## [v0.7.1] - 2023-07-05

Section titled “[v0.7.1] - 2023-07-05”

### New Features

Section titled “New Features”

  * Streaming support for OpenAI agents (#6694)
  * add recursive retriever + notebook example (#6682)

## [v0.7.0] - 2023-07-04

Section titled “[v0.7.0] - 2023-07-04”

### New Features

Section titled “New Features”

  * Index creation progress bars (#6583)

### Bug Fixes/ Nits

Section titled “Bug Fixes/ Nits”

  * Improved chat refine template (#6645)

### Breaking/Deprecated API Changes

Section titled “Breaking/Deprecated API Changes”

  * Change `BaseOpenAIAgent` to use `llama_index.llms.OpenAI`. Adjust `chat_history` to use `List[ChatMessage]]` as type.
  * Remove (previously deprecated) `llama_index.langchain_helpers.chain_wrapper` module.
  * Remove (previously deprecated) `llama_index.token_counter.token_counter` module. See [migration guide](/how_to/callbacks/token_counting_migration.html) for more details on new callback based token counting.
  * Remove `ChatGPTLLMPredictor` and `HuggingFaceLLMPredictor`. See [migration guide](/how_to/customization/llms_migration_guide.html) for more details on replacements.
  * Remove support for setting `cache` via `LLMPredictor` constructor.
  * Update `BaseChatEngine` interface: 
    * adjust `chat_history` to use `List[ChatMessage]]` as type
    * expose `chat_history` state as a property
    * support overriding `chat_history` in `chat` and `achat` endpoints
  * Remove deprecated arguments for `PromptHelper`: `max_input_size`, `embedding_limit`, `max_chunk_overlap`
  * Update all notebooks to use native openai integration (#6696)

## [v0.6.38] - 2023-07-02

Section titled “[v0.6.38] - 2023-07-02”

### New Features

Section titled “New Features”

  * add optional tqdm progress during index creation (#6583)
  * Added async support for “compact” and “refine” response modes (#6590)
  * [feature]add transformer tokenize functionalities for optimizer (chinese) (#6659)
  * Add simple benchmark for vector store (#6670)
  * Introduce `llama_index.llms` module, with new `LLM` interface, and `OpenAI`, `HuggingFaceLLM`, `LangChainLLM` implementations. (#6615)
  * Evaporate pydantic program (#6666)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Improve metadata/node storage and retrieval for RedisVectorStore (#6678)
  * Fixed node vs. document filtering in vector stores (#6677)
  * add context retrieval agent notebook link to docs (#6660)
  * Allow null values for the ‘image’ property in the ImageNode class and se… (#6661)
  * Fix broken links in docs (#6669)
  * update milvus to store node content (#6667)

## [v0.6.37] - 2023-06-30

Section titled “[v0.6.37] - 2023-06-30”

### New Features

Section titled “New Features”

  * add context augmented openai agent (#6655)

## [v0.6.36] - 2023-06-29

Section titled “[v0.6.36] - 2023-06-29”

### New Features

Section titled “New Features”

  * Redis support for index stores and docstores (#6575)
  * DuckDB + SQL query engine notebook (#6628)
  * add notebook showcasing deplot data loader (#6638)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * More robust JSON parsing from LLM for `SelectionOutputParser` (#6610)
  * bring our loaders back in line with llama-hub (#6630)
  * Remove usage of SQLStructStoreIndex in notebooks (#6585)
  * MD reader: remove html tags and leave linebreaks alone (#6618)
  * bump min langchain version to latest version (#6632)
  * Fix metadata column name in postgres vector store (#6622)
  * Postgres metadata fixes (#6626, #6634)
  * fixed links to dataloaders in contribution.md (#6636)
  * fix: typo in docs in creating custom_llm huggingface example (#6639)
  * Updated SelectionOutputParser to handle JSON objects and arrays (#6610)
  * Fixed docstring argument typo (#6652)

## [v0.6.35] - 2023-06-28

Section titled “[v0.6.35] - 2023-06-28”

  * refactor structured output + pydantic programs (#6604)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix serialization for OpenSearch vector stores (#6612)
  * patch docs relationships (#6606)
  * Bug fix for ignoring directories while parsing git repo (#4196)
  * updated Chroma notebook (#6572)
  * Backport old node name (#6614)
  * Add the ability to change chroma implementation (#6601)

## [v0.6.34] - 2023-06-26

Section titled “[v0.6.34] - 2023-06-26”

### Patch Update (v0.6.34.post1)

Section titled “Patch Update (v0.6.34.post1)”

  * Patch imports for Document obj for backwards compatibility (#6597)

### New Features

Section titled “New Features”

  * New `TextNode`/`Document` object classes based on pydantic (#6586)
  * `TextNode`/`Document` objects support metadata customization (metadata templates, exclude metadata from LLM or embeddings) (#6586)
  * Nodes no longer require flat metadata dictionaries, unless the vector store you use requires it (#6586)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * use `NLTK_DATA` env var to control NLTK download location (#6579)
  * [discord] save author as metadata in group_conversations.py (#6592)
  * bs4 -> beautifulsoup4 in requirements (#6582)
  * negate euclidean distance (#6564)
  * add df output parser notebook link to docs (#6581)

### Breaking/Deprecated API Changes

Section titled “Breaking/Deprecated API Changes”

  * `Node` has been renamed to `TextNode` and is imported from `llama_index.schema` (#6586)
  * `TextNode` and `Document` must be instantiated with kwargs: `Document(text=text)` (#6586)
  * `TextNode` (fka `Node`) has a `id_` or `node_id` property, rather than `doc_id` (#6586)
  * `TextNode` and `Document` have a metadata property, which replaces the extra_info property (#6586)
  * `TextNode` no longer has a `node_info` property (start/end indexes are accessed directly with `start/end_char_idx` attributes) (#6586)

## [v0.6.33] - 2023-06-25

Section titled “[v0.6.33] - 2023-06-25”

### New Features

Section titled “New Features”

  * Add typesense vector store (#6561)
  * add df output parser (#6576)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Track langchain dependency via bridge module. (#6573)

## [v0.6.32] - 2023-06-23

Section titled “[v0.6.32] - 2023-06-23”

### New Features

Section titled “New Features”

  * add object index (#6548)
  * add SQL Schema Node Mapping + SQLTableRetrieverQueryEngine + obj index fixes (#6569)
  * sql refactor (NLSQLTableQueryEngine) (#6529)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Update vector_stores.md (#6562)
  * Minor `BaseResponseBuilder` interface cleanup (#6557)
  * Refactor TreeSummarize (#6550)

## [v0.6.31] - 2023-06-22

Section titled “[v0.6.31] - 2023-06-22”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * properly convert weaviate distance to score (#6545)
  * refactor tree summarize and fix bug to not truncate context (#6550)
  * fix custom KG retrieval notebook nits (#6551)

## [v0.6.30] - 2023-06-21

Section titled “[v0.6.30] - 2023-06-21”

### New Features

Section titled “New Features”

  * multi-selector support in router query engine (#6518)
  * pydantic selector support in router query engine using OpenAI function calling API (#6518)
  * streaming response support in `CondenseQuestionChatEngine` and `SimpleChatEngine` (#6524)
  * metadata filtering support in `QdrantVectorStore` (#6476)
  * add `PGVectorStore` to support postgres with pgvector (#6190)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * better error handling in the mbox reader (#6248)
  * Fix blank similarity score when using weaviate (#6512)
  * fix for sorted nodes in `PrevNextNodePostprocessor` (#6048)

### Breaking/Deprecated API Changes

Section titled “Breaking/Deprecated API Changes”

  * Refactor PandasQueryEngine to take in df directly, deprecate PandasIndex (#6527)

## [v0.6.29] - 2023-06-20

Section titled “[v0.6.29] - 2023-06-20”

### New Features

Section titled “New Features”

  * query planning tool with OpenAI Function API (#6520)
  * docs: example of kg+vector index (#6497)
  * Set context window sizes for Cohere and AI21(J2 model) (#6485)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * add default input size for Cohere and AI21 (#6485)
  * docs: replace comma with colon in dict object (#6439)
  * extra space in prompt and error message update (#6443)
  * [Issue 6417] Fix prompt_templates docs page (#6499)
  * Rip out monkey patch and update model to context window mapping (#6490)

## [v0.6.28] - 2023-06-19

Section titled “[v0.6.28] - 2023-06-19”

### New Features

Section titled “New Features”

  * New OpenAI Agent + Query Engine Cookbook (#6496)
  * allow recursive data extraction (pydantic program) (#6503)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * update mongo interface (#6501)
  * fixes that we forgot to include for openai pydantic program (#6503) (#6504)
  * Fix github pics in Airbyte notebook (#6493)

## [v0.6.27] - 2023-06-16

Section titled “[v0.6.27] - 2023-06-16”

### New Features

Section titled “New Features”

  * Add node doc_id filtering to weaviate (#6467)
  * New `TokenCountingCallback` to customize and track embedding, prompt, and completion token usage (#6440)
  * OpenAI Retrieval Function Agent (#6491)

### Breaking/Deprecated API Changes

Section titled “Breaking/Deprecated API Changes”

  * Deprecated current token tracking (llm predictor and embed model will no longer track tokens in the future, please use the `TokenCountingCallback` (#6440)
  * Add maximal marginal relevance to the Simple Vector Store, which can be enabled as a query mode (#6446)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * `as_chat_engine` properly inherits the current service context (#6470)
  * Use namespace when deleting from pinecone (#6475)
  * Fix paths when using fsspec on windows (#3778)
  * Fix for using custom file readers in `SimpleDirectoryReader` (#6477)
  * Edit MMR Notebook (#6486)
  * FLARE fixes (#6484)

## [v0.6.26] - 2023-06-14

Section titled “[v0.6.26] - 2023-06-14”

### New Features

Section titled “New Features”

  * Add OpenAIAgent and tutorial notebook for “build your own agent” (#6461)
  * Add OpenAIPydanticProgram (#6462)

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Fix citation engine import (#6456)

## [v0.6.25] - 2023-06-13

Section titled “[v0.6.25] - 2023-06-13”

### New Features

Section titled “New Features”

  * Added FLARE query engine (#6419).

## [v0.6.24] - 2023-06-12

Section titled “[v0.6.24] - 2023-06-12”

### New Features

Section titled “New Features”

  * Added better support for vector store with existing data (e.g. allow configurable text key) for Pinecone and Weaviate. (#6393)
  * Support batched upsert for Pineone (#6393)
  * Added initial [guidance](https://github.com/microsoft/guidance/) integration. Added `GuidancePydanticProgram` for generic structured output generation and `GuidanceQuestionGenerator` for generating sub-questions in `SubQuestionQueryEngine` (#6246).

## [v0.6.23] - 2023-06-11

Section titled “[v0.6.23] - 2023-06-11”

### Bug Fixes / Nits

Section titled “Bug Fixes / Nits”

  * Remove hardcoded chunk size for citation query engine (#6408)
  * Mongo demo improvements (#6406)
  * Fix notebook (#6418)
  * Cleanup RetryQuery notebook (#6381)

## [v0.6.22] - 2023-06-10

Section titled “[v0.6.22] - 2023-06-10”

### New Features

Section titled “New Features”

  * Added `SQLJoinQueryEngine` (generalization of `SQLAutoVectorQueryEngine`) (#6265)
  * Added support for graph stores under the hood, and initial support for Nebula KG. More docs coming soon! (#2581)
  * Added guideline evaluator to allow llm to provide feedback based on user guidelines (#4664)
  * Added support for MongoDB Vector stores to enable Atlas knnbeta search (#6379)
  * Added new CitationQueryEngine for inline citations of sources in response text (#6239)

### Bug Fixes

Section titled “Bug Fixes”

  * Fixed bug with `delete_ref_doc` not removing all metadata from the docstore (#6192)
  * FIxed bug with loading existing QDrantVectorStore (#6230)

### Miscellaneous

Section titled “Miscellaneous”

  * Added changelog officially to github repo (#6191)

## [v0.6.21] - 2023-06-06

Section titled “[v0.6.21] - 2023-06-06”

### New Features

Section titled “New Features”

  * SimpleDirectoryReader has new `filename_as_id` flag to automatically set the doc_id (useful for `refresh_ref_docs()`)
  * DocArray vector store integration
  * Tair vector store integration
  * Weights and Biases callback handler for tracing and versioning indexes
  * Can initialize indexes directly from a vector store: `index = VectorStoreIndex.from_vector_store(vector_store=vector_store)`

### Bug Fixes

Section titled “Bug Fixes”

  * Fixed multimodal notebook
  * Updated/fixed the SQL tutorial in the docs

### Miscellaneous

Section titled “Miscellaneous”

  * Minor docs updates
  * Added github pull-requset templates
  * Added github issue-forms

## [v0.6.20] - 2023-06-04

Section titled “[v0.6.20] - 2023-06-04”

### New Features

Section titled “New Features”

  * Added new JSONQueryEngine that uses JSON schema to deliver more accurate JSON query answers
  * Metadata support for redis vector-store
  * Added Supabase vector store integration

### Bug Fixes

Section titled “Bug Fixes”

  * Fixed typo in text-to-sql prompt

### Breaking/Deprecated API Changes

Section titled “Breaking/Deprecated API Changes”

  * Removed GPT prefix from indexes (old imports/names are still supported though)

### Miscellaneous

Section titled “Miscellaneous”

  * Major docs updates, brought important modules to the top level

## [v0.6.19] - 2023-06-02

Section titled “[v0.6.19] - 2023-06-02”

### New Features

Section titled “New Features”

  * Added agent tool abstraction for llama-hub data loaders

### Miscellaneous

Section titled “Miscellaneous”

  * Minor doc updates

## [v0.6.18] - 2023-06-02

Section titled “[v0.6.18] - 2023-06-02”

### Miscellaneous

Section titled “Miscellaneous”

  * Added `Discover LlamaIndex` video series to the tutorials docs section
  * Minor docs updates

[ Previous  
Llama Packs 🦙📦 ](/python/framework/community/llama_packs/) [ Next  
AI21  ](/python/examples/llm/ai21/)

