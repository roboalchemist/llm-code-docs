# Source: https://developer.nvidia.com/cuvs.md

1. [AI](https://developer.nvidia.com/topics/ai)
2. [Generative AI](https://developer.nvidia.com/generative-ai)

cuVS  

# NVIDIA cuVS  

NVIDIA cuVS is an open-source library for GPU-accelerated vector search and data clustering that enables faster vector searches and index builds.

It supports scalable data analysis, enhances semantic search efficiency, and helps developers accelerate existing systems or compose new ones from the ground up. Integrated with key libraries and databases, cuVS also manages complex code updates as new NVIDIA architectures and NVIDIA® CUDA® versions are released, ensuring peak performance and seamless scalability.

[Download Now](https://github.com/rapidsai/cuvs &quot;Try Now&quot;)[Integrations](https://docs.rapids.ai/api/cuvs/nightly/integrations/ &quot;Request License&quot;)[Documentation](https://docs.nvidia.com/cuvs/index.html#product-documentationBYzNyK3Q &quot;Request License&quot;)

## How NVIDIA cuVS Works

NVIDIA cuVS is designed to accelerate and optimize vector index builds and vector search for existing [databases](https://www.nvidia.com/en-us/glossary/vector-database/) and vector search libraries. It enables developers to enhance data mining and semantic search workloads, such as recommender systems and [retrieval-augmented generation](/topics/ai/retrieval-augmented-generation) (RAG). Built on top of the [NVIDIA CUDA software stack](https://docs.rapids.ai/api/cuvs/nightly/#cuvs-technology-stack), it contains many building blocks for composing vector search systems and exposes easy-to-use APIs for C, C++, Rust, Java, Python, and Go.

 ![NVIDIA cuVS accelerates and optimizes vector index builds and vector search](https://developer.download.nvidia.com/images/how-nvidia-cu-vs-works.svg)

### Introductory Blog

Get an intro into accelerating vector search with cuVS, popular applications, and performance comparison of GPU-accelerated vector search indexes vs. CPU.

[Read the Blog](/blog/accelerating-vector-search-using-gpu-powered-indexes-with-rapids-raft/ &quot;Get Started&quot;)

### Getting Started Guide

Understand the differences between vector search indexes and fully-fledged vector databases.

[Get the Primer](https://docs.rapids.ai/api/cuvs/nightly/getting_started/ &quot;Get Started&quot;)

### Notebooks

Build [IVF-PQ](https://github.com/rapidsai/cuvs/blob/branch-25.02/notebooks/tutorial_ivf_pq.ipynb) index and use it to search approximate nearest neighbors (ANN) or learn how to run approximate nearest neighbor search using [cuVS IVF-Flat](https://github.com/rapidsai/cuvs/blob/branch-25.02/notebooks/ivf_flat_example.ipynb) algorithm.

[Get Started on GitHub](https://github.com/rapidsai/cuvs/tree/branch-25.02/notebooks &quot;Get Started&quot;)

### Examples

Get access to drop-in samples to build a new application with cuVS, or use it in an existing project. See cuVS [installation docs](https://docs.rapids.ai/api/cuvs/stable/build.html#cuda-gpu-requirements).

[Check Out on GitHub](https://github.com/rapidsai/cuvs/tree/branch-24.12/examples &quot;Get Started&quot;)

* * *

## Key Features

### GPU-Accelerated Indexing Algorithms

Optimized GPU indexing enables high-quality index builds and low-latency search. cuVS delivers advanced algorithms for indexing vector embeddings, including exact, tree-based, and graph-based indexes.  

- 

### **Real-Time Updates for Large Language Models (LLMs)**

cuVS enables real-time updates to search indexes by dynamically integrating new embeddings and data without rebuilding the entire index. By integrating cuVS with LLMs, search results remain fresh and relevant.

- 

### **High-Efficiency Indexing**

GPU indexing lowers cost compared to CPU-only workflows while maintaining quality at scale. Additionally, the ability to build large indexes out-of-core enables more flexible GPU selection and ultimately lower costs per gigabyte.

- 

### 
**### Scalable Index Building**

For real-time applications and large-scale deployments, cuVS enables both scale-up and scale-out for index creation and search at a fraction of the time it takes on a CPU without compromising quality.

### GPU-Accelerated Search Algorithms

cuVS transforms vector search by integrating optimized CUDA-based algorithms for approximate nearest neighbors and clustering, ideal for large-scale, time-sensitive workloads.  

- 

### 
**### Real-Time Updates for Large Language Models (LLMs)**

cuVS enables real-time updates to search indexes by dynamically integrating new embeddings and data without rebuilding the entire index. By integrating cuVS with LLMs, search results remain fresh and relevant.

- 

### 
**### Low-Latency Performance**

cuVS provides ultra-fast response times for applications such as semantic search, where speed and accuracy are critical. Furthermore, support for binary, 8-, 16-, and 32-bit types means memory use is optimized for high-throughput applications.

- 

### 
**### High-Throughput Processing**

GPUs handle hundreds of thousands of queries per second, making cuVS perfect for demanding use cases like machine learning, data mining, and real-time analytics.

## Get Started

Select the right path to get started using cuVS. Integrate it into your existing vector search systems, pipelines, or applications and accelerate your semantic search for data mining use cases in production.  

![Evaluate with cuVS Bench](https://developer.download.nvidia.com/icons/containerized-model.svg)

### Evaluate  

Start using cuVS as a benchmarking tool designed for reproducible comparisons of ANN search implementations, especially between GPU and CPU, by optimizing index configurations and analyzing performance across different hardware environments.

[Start Evaluating With cuVS Bench](https://docs.rapids.ai/api/cuvs/nightly/cuvs_bench/)

![Download Library (GitHub)](https://developer.download.nvidia.com/icons/m48-speech-recognition.svg)

### Develop  

NVIDIA cuVS is available on GitHub with end-to-end examples and an automated tuning guide. Access the source code to get started.

[Download Library (GitHub)](https://github.com/rapidsai/cuvs)

![Launch Through Integrations](https://developer.download.nvidia.com/icons/m48-digital-deep-learning-institute-talks-training.svg)

### Launch  

cuVS can be used as a standalone library or deployed through a number of SDK and vector database integrations like FAISS, Milvus, Lucene, Kinetica, and more.

[Launch Through Integrations](https://docs.rapids.ai/api/cuvs/nightly/integrations/)

* * *

## Performance—World&#39;s Fastest Vector Search

NVIDIA cuVS exploits the parallel architecture of NVIDIA GPUs, allowing for easy deployment of popular and performance-critical algorithms. GPU-acceleration of vector similarity search [sets benchmark records](https://github.com/harsha-simhadri/big-ann-benchmarks/blob/main/neurips21/t3/LEADERBOARDS.md#public-dataset-leaderboards-and-winners) for large-scale, high-performance solutions.

### 21x Faster Indexing  

Lower is Better.

 ![A chart showing 21X faster indexing on GPU vs CPU in the cloud](https://developer.download.nvidia.com/images/cuvs/index-build-performance-3691350.svg)

_Time to build an index on GPU (8x A10g) vs CPU (Intel Ice Lake) in the cloud (AWS), reducing from hours to minutes._

### 12.5x Lower Cost  

Lower is Better.

 ![A chart showing 12.5X lower cost indexing on GPU vs CPU in the cloud](https://developer.download.nvidia.com/images/cuvs/index-build-cost-3691350.svg)

_Cost to build an index on the GPU (8x A10g) vs CPU (Intel Ice Lake) in the cloud (AWS)._

### 29x Higher Throughput  

Higher is Better.

 ![A chart showing 34X higher throughput on GPU vs CPU](https://developer.download.nvidia.com/images/cuvs/search-throughput-3691350.svg)

_Number of vectors that can be queried per second on a GPU (H100) vs CPU (Intel Xeon Platinum 8470Q) when submitted 10,000 at a time._

### 11x Lower Latency  

Lower is Better.

 ![A chart showing 11X lower latency on GPU vs CPU](https://developer.download.nvidia.com/images/cuvs/search-latency-3691350.svg)

_Average time to process each query on a GPU (H100) vs CPU (Intel Xeon Platinum 8470Q) when submitted one at a time._

* * *

## Starter Kits for NVIDIA cuVS

Start accelerating your libraries, databases, and applications with cuVS by accessing tutorials, notebooks, forums, release notes, and comprehensive documentation.

### For Library Development  

cuVS provides easy-to-use Python APIs, which enable straightforward integration into libraries for data mining and analysis. cuVS is also integrated into the popular FAISS library for CPU and GPU interoperability.

- 

[Explore Example Python Notebooks](https://github.com/rapidsai/cuvs/tree/branch-24.12/notebooks)

- 

[Read the Getting Started Guide](https://docs.rapids.ai/api/cuvs/nightly/getting_started/)

- 

[Read API Documentation](https://docs.rapids.ai/api/cuvs/nightly/api_docs/)

### For Database Development  

cuVS building blocks are built in C++ and wrapped in popular languages like C, Python, Rust, Java, and Go, making them easy to integrate into existing databases and vector indexing tools.

- 

[Explore Example Projects and Code](https://github.com/rapidsai/cuvs/tree/branch-24.12/examples)

- 

[Read the Getting Started Guide](https://docs.rapids.ai/api/cuvs/nightly/getting_started/)

- 

[Try the Reproducible Benchmarking Tool](https://docs.rapids.ai/api/cuvs/nightly/cuvs_bench/)

### For Application Development  

cuVS can be used directly or through several database and library integrations to supercharge your applications and workflows with GPU acceleration.

- 

[Try the NVIDIA AI Blueprint for RAG](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline)

- 

[Read the Getting Started Guide](https://docs.rapids.ai/api/cuvs/nightly/getting_started/)

- 

[Explore Library and Database Integrations](https://docs.rapids.ai/api/cuvs/nightly/integrations/)

- 

[Learn About Vector Databases vs. Databases](https://docs.rapids.ai/api/cuvs/nightly/vector_databases_vs_vector_search/)

* * *

## Learning Library

* * *

## Ecosystem

[
 ![NVIDIA cuVS Ecosystem Partner - Datastax](https://developer.download.nvidia.com/images/cuvs/logo-datastax.svg)
](https://www.datastax.com/blog/datastax-ai-paas-integrated-with-nvidia-nemo-retriever)

[
 ![NVIDIA cuVS Ecosystem Partner - Elastic](https://developer.download.nvidia.com/images/cuvs/logo-elastic.svg)
](https://www.nvidia.com/gtc/session-catalog/?tab.catalogallsessionstab=16566177511100015Kus&amp;search=lucene#/session/1725488451726001Mz27)

[
 ![NVIDIA cuVS Ecosystem Partner -](https://developer.download.nvidia.com/images/cuvs/logo-faiss.svg)
](https://docs.rapids.ai/api/cuvs/nightly/integrations/faiss/)

[
 ![NVIDIA cuVS Ecosystem Partner - Kinetica](https://developer.download.nvidia.com/images/cuvs/logo-kinetica.svg)
](https://docs.rapids.ai/api/cuvs/nightly/integrations/kinetica/)

[
 ![NVIDIA cuVS Ecosystem Partner - Lucene](https://developer.download.nvidia.com/images/cuvs/logo-apache-lucene.svg)
](https://docs.rapids.ai/api/cuvs/nightly/integrations/lucene/)

[
 ![NVIDIA cuVS Ecosystem Partner - Milvus](https://developer.download.nvidia.com/images/cuvs/logo-milvus.svg)
](https://docs.rapids.ai/api/cuvs/nightly/integrations/milvus/)

[
 ![NVIDIA cuVS Ecosystem Partner - OpenSearch](https://developer.download.nvidia.com/images/cuvs/logo-open-search.svg)
](https://opensearch.org/blog/GPU-Accelerated-Vector-Search-OpenSearch-New-Frontier/)

[
 ![NVIDIA cuVS Ecosystem Partner - Solr](https://developer.download.nvidia.com/images/cuvs/logo-solr.svg)
](https://www.nvidia.com/gtc/session-catalog/?tab.catalogallsessionstab=16566177511100015Kus&amp;search=lucene#/session/1725488451726001Mz27)

[
 ![NVIDIA cuVS Ecosystem Partner - Weaviate](https://developer.download.nvidia.com/images/cuvs/logo-weaviate.svg)
](https://www.nvidia.com/gtc/session-catalog/?tab.catalogallsessionstab=16566177511100015Kus&amp;search=weaviate#/session/1725741930792001U8IR)

* * *

## More Resources

 ![NVIDIA Developer Newsletter](https://developer.download.nvidia.com/icons/m48-email-settings.svg)

### Sign Up for Developer Newsletter  

 ![NVIDIA Training and Certification](https://developer.download.nvidia.com/icons/m48-certification-ribbon-2.svg)

### Get Training and Certification  

 ![NVIDIA Developer Program](https://developer.download.nvidia.com/images/cuvs/developer-1.svg)

### Join the NVIDIA Developer Program  

### Get Started With NVIDIA cuVS Today

[Download Now](https://github.com/rapidsai/cuvs)


