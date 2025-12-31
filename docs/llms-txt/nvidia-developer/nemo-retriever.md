# Source: https://developer.nvidia.com/nemo-retriever.md

1. [Topics](https://developer.nvidia.com/topics/)

[AI](https://developer.nvidia.com/topics/ai)
2. [Generative AI](https://developer.nvidia.com/generative-ai)

NVIDIA NeMo Retriever

# NVIDIA NeMo Retriever

NVIDIA NeMo™ Retriever is a collection of industry-leading [Nemotron RAG](https://huggingface.co/collections/nvidia/nemotron-rag-68f01e412f2dc5a5db5f30ed) models delivering 50% better accuracy, 15x faster multimodal PDF extraction, and 35x better storage efficiency, enabling enterprises to build retrieval-augmented generation (RAG) pipelines that provide real-time business insights. NeMo Retriever, part of the [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) software suite for managing the AI agent lifecycle, ensures data privacy and seamlessly connects to proprietary data wherever it resides, empowering secure, enterprise-grade retrieval. NeMo Retriever serves as a core component for [NVIDIA AI-Q](https://build.nvidia.com/nvidia/aiq)—a blueprint for building intelligent AI agents—and the [NVIDIA RAG blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline), enabling access to knowledge from enterprise AI data platforms. It provides a reliable foundation for scalable, production-ready retrieval pipelines supporting advanced AI applications.  
  
[NeMo Retriever microservices](https://developer.nvidia.com/blog/nvidia-nemo-retriever-delivers-accurate-multimodal-pdf-data-extraction-15x-faster/) set a new standard for enterprise RAG applications, leading the industry with first-place performance across three top visual document retrieval leaderboards (ViDoRe V1, ViDoRe V2, MTEB, and MMTEB VisualDocumentRetrieval).

[Access Code](https://huggingface.co/collections/nvidia/nemotron-rag-68f01e412f2dc5a5db5f30ed &quot;Try Now&quot;)[Forum  
](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nemo/715 &quot;Forum&quot;)

* * *

## Documentation

Build world-class information retrieval pipelines and [AI query engines](https://blogs.nvidia.com/blog/ai-query-engines-agentic-ai/) with scalable data extraction and high-accuracy embedding and reranking.

### Ingestion  

Rapidly ingest massive volumes of data and extract text, graphs, charts, and tables at the same time for highly accurate retrieval.

- 
[Documentation](https://docs.nvidia.com/nemo/retriever/extraction/overview/)
- 
[Experience the RAG Blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline)
- 
[Try NIM Microservices for Retrieval](https://build.nvidia.com/explore/retrieval)

### Embedding  

Boost text question-and-answer retrieval performance, providing high-quality embeddings for many downstream natural language processing (NLP) tasks.

- 
[Documentation](https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/overview.html)
- 
[Read the Blog](https://developer.nvidia.com/blog/develop-multilingual-and-cross-lingual-information-retrieval-systems-with-efficient-data-storage/)
- 
[Try NIM Microservices for Retrieval](https://build.nvidia.com/explore/retrieval)

### Reranking  

Enhance retrieval performance further with a fine-tuned reranking model, finding the most relevant passages to provide as context when querying a large language model (LLM).

- 
[Documentation](https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/overview.html)
- 
[Read the Blog](https://developer.nvidia.com/blog/how-using-a-reranking-microservice-can-improve-accuracy-and-costs-of-information-retrieval/)
- 
[Try NIM Microservices for Retrieval](https://build.nvidia.com/explore/retrieval)

* * *

## How NVIDIA NeMo Retriever Works

NeMo Retriever provides components for building data extraction and information retrieval pipelines. The pipeline extracts structured and unstructured data (ex. text, charts, tables), converts it to text, and filters out duplicates. A NeMo Retriever [embedding NIM](https://build.nvidia.com/explore/retrieval) converts the chunks into embeddings and stores them in a vector database, accelerated by [NVIDIA cuVS](https://developer.nvidia.com/cuvs), for enhanced performance and speed of indexing and search.   
  
When a query is submitted, the system retrieves relevant information using vector similarity search, and then a NeMo Retriever [reranking NIM](https://build.nvidia.com/explore/retrieval) reranks the results for accuracy. With the most pertinent information, an LLM NIM generates a response that’s informed, accurate, and contextually relevant. You can use various LLM NIM microservices from the NVIDIA [API catalog](http://build.nvidia.com) to enable additional capabilities, such as synthetic data generation.

![A diagram showing how NVIDIA NeMo Retriever works from data ingestion to information retrieval.](https://developer.download.nvidia.com/images/nemo-retriever/llm-nemo-retriever-diagram-1920-1416.jpg)
_NVIDIA NeMo Retriever collection of NIM microservices are used to build optimized ingestion and retrieval pipelines for highly accurate information retrieval at scale._

* * *

## Introductory Resources  

Learn more about building efficient information-retrieval pipelines with NeMo Retriever.

### Introductory Blog  

Understand the function of embedding and reranking models in information retrieval pipelines, top considerations, and more.

[Read Blog](https://developer.nvidia.com/blog/translate-your-enterprise-data-into-actionable-insights-with-nvidia-nemo-retriever/)

### Introductory Webinar  

Improve the accuracy and scalability of text retrieval for production-ready generative AI pipelines and deploy at scale.

[Watch Now](https://info.nvidia.com/World-Class-Text-Retrieval-Accuracy-Generative-AI.html?ondemandrgt=yes#)

### AI Blueprint for RAG  

Learn best practices for connecting AI apps to enterprise data using industry-leading embedding and reranking models.

[Try the   
Blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline)

### Introductory GTC Session

Learn about the latest models, tools, and techniques for creating agentic and RAG pipelines for multimodal data ingestion, extraction, and retrieval.

[Watch Session](https://www.nvidia.com/en-us/on-demand/session/gtc25-s72205/)

* * *

## World-Class Information-Retrieval Performance

NeMo Retriever microservices accelerate multimodal document extraction and real-time retrieval with lower RAG costs and higher accuracy. They support reliable, multilingual, and cross-lingual retrieval, and optimize storage, performance, and adaptability for data platforms – enabling efficient vector database expansion.

### 50% Fewer Incorrect Answers

NeMo Retriever Multimodal Extraction Recall@5 Accuracy

![A graph showing NeMo Retriever has achieved 2X throughput for fast info retrieval](https://developer.download.nvidia.com/images/nemo-retriever/nemo-retriever-llama-chart-1.svg)

Evaluated on publicly available dataset of PDFs consisting of text, charts, tables, and infographics. NeMo Retriever Extraction On: nemoretriever-page-elements-v2, nemoretriever-table-structure-v1, nemoretriever-graphic-elements-v1, paddle-ocr  
compared with NeMo Retriever Off: open-source alternative: HW - 1xH100   

 

### 3X Higher Embedding Throughput  

NeMo Retriever Llama 3.2 Multilingual Text Embedding

![A graph showing NeMo Retriever has achieved high accuracy with 30% fewer incorrect answers](https://developer.download.nvidia.com/images/nemo-retriever/nemo-retriever-llama-chart-2.svg)

This test was conducted with the following requirements: 1xH100 SXM; passage token length: 512, batch size: 64, concurrent client requests: 5; OSS Alternative: FP16 compared to the NeMo Retriever lama-3.2-nv-embedqa-1b-v2, NIM: FP8

 

### 15X Higher Multimodal Data Extraction Throughput

NeMo Retriever Extraction NIM Microservices

![A graph showing NeMo Retriever embedding model is a leader on the Massive Text Embedding Benchmark (MTEB) leaderboard](https://developer.download.nvidia.com/images/nemo-retriever/nemo-retriever-extraction-chart-3.svg)

Pages per second, evaluated on publicly available dataset of PDFs consisting of text, charts, and tables, with NeMo Retriever extraction NIM microservices: nv-yolox-structured-image-v1, nemoretriever-page-elements-v1, nemoretriever-graphic-elements-v1, nemoretriever-table-structure-v1, PaddleOCR, nv-llama3.2-embedqa-1b-v2 compared to an open-source alternative; HW - 1xH100

 

### 35x Improved Data Storage Efficiency  

Multilingual, Long-Context, Text Embedding NIM Microservice

![A graph showing NeMo Retriever embedding model, llama-3.2-nv-embedqa-1b-v2.](https://developer.download.nvidia.com/images/nemo-retriever/data-storage-efficiency(1).svg)

Tested with the latest NeMo Retriever embedding model, llama-3.2-nv-embedqa-1b-v2, this shows the impact on vector storage volume with long-context support, dynamic embeddings, and efficient storage for high-performance, scalable data processing. In the chart above, DIM=dimensions. 

 

* * *

## Ways to Get Started With NVIDIA NeMo Retriever

Use the right tools and technologies to build and deploy generative AI applications that require secure and accurate information retrieval to generate real-time business insights for organizations across every industry. 

 ![Decorative icon](https://developer.download.nvidia.com/images/isaac/m48-digital-deep-learning-institute-talks-training.svg)
### Access

Download our open models from Hugging Face.

[Access Code](https://huggingface.co/collections/nvidia/nemotron-rag-68f01e412f2dc5a5db5f30ed)

 ![Decorative](https://developer.download.nvidia.com/images/omniverse/m48-nim.svg)
### Download

Experience NeMo Retriever NIM microservices through a UI-based portal for exploring and prototyping with NVIDIA-managed endpoints, available for free through NVIDIA’s API catalog and deployed anywhere.

[Download NeMo Retriever Microservices](https://build.nvidia.com/explore/retrieval)

 ![Decorative icon representing source code](https://developer.download.nvidia.com/images/icons/m48-workflow-complex-256px-blk.png)
### Try

Jump-start building your AI solutions with [NVIDIA Blueprints](https://www.nvidia.com/en-us/ai-data-science/ai-workflows/), customizable reference applications, available on the NVIDIA API catalog.

[Try the Blueprint](https://build.nvidia.com/nim/agent-blueprints)

* * *

## Starter Kits

Start building information retrieval pipelines and generative AI applications for multimodal data ingestion, embedding, reranking, retrieval-augmented generation, and agentic workflows by accessing [NVIDIA Blueprints](https://www.nvidia.com/en-us/ai-data-science/ai-workflows/), tutorials, notebooks, blogs, forums, reference code, comprehensive documentation, and more.

### AI Agent for Enterprise Research

Develop AI agents that continuously process and synthesize multimodal enterprise data, reason, plan, and refine to generate comprehensive reports.

- 
[Read Blueprint Model Card](https://build.nvidia.com/nvidia/aiq)
- 
[Read Technical Blog](https://developer.nvidia.com/blog/chat-with-your-enterprise-data-through-open-source-ai-q-nvidia-blueprint/)
- 
[Try Blueprint](https://brev.nvidia.com/launchable/deploy/now?launchableID=env-2y9mLGTtOuAHzLbXu3xUY5HLckY)

### Enterprise RAG  

Connect secure, scalable, reliable AI applications to your company’s internal enterprise data using industry-leading embedding and reranking models for information retrieval at scale.

- 
[Read Blueprint Model Card  
](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline)
- 
[Read Technical Blog](https://developer.nvidia.com/blog/build-a-rag-agent-with-nvidia-nemotron/)

### Streaming Data to RAG

Unlock dynamic, context-aware insights from streaming sources like radio signals and other sensor data.

- 
[Read Blueprint Model Card](https://build.nvidia.com/nvidia/streaming-data-to-rag)
- 
[Try NeMo Retriever Microservices](https://build.nvidia.com/explore/retrieval)

### Evaluating and Customizing RAG Pipelines

Evaluate pretrained embedding models on data and queries similar to your users’ needs using NVIDIA NeMo microservices to optimize RAG performance.

- 
[Learn About NeMo Curator](/nemo-curator)
- 
[Learn About NeMo Evaluator](/nemo-evaluator)
- 
[Read Technical Blog](https://developer.nvidia.com/blog/evaluating-and-enhancing-rag-pipeline-performance-using-synthetic-data/)

* * *

## NVIDIA NeMo Retriever Learning Library  

* * *

## More Resources

 ![Decorative image representing forums](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore the Community  

 ![](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Accelerate Your Startup  

* * *

## Ethical AI

NVIDIA’s platforms and application frameworks enable developers to build a wide array of AI applications. Consider potential algorithmic bias when choosing or creating the models being deployed. Work with the model’s developer to ensure that it meets the requirements for the relevant industry and use case; that the necessary instruction and documentation are provided to understand error rates, confidence intervals, and results; and that the model is being used under the conditions and in the manner intended.

## Get Started With NeMo Retriever Today.

[Try Now](https://build.nvidia.com/explore/retrieval &quot;Try Now&quot;)


