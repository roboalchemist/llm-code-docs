# [Anchor](https://qdrant.tech/benchmarks/benchmarks-intro/\#benchmarking-vector-databases) Benchmarking Vector Databases

At Qdrant, performance is the top-most priority. We always make sure that we use system resources efficiently so you get the **fastest and most accurate results at the cheapest cloud costs**. So all of our decisions from [choosing Rust](https://qdrant.tech/articles/why-rust/), [io optimisations](https://qdrant.tech/articles/io_uring/), [serverless support](https://qdrant.tech/articles/serverless/), [binary quantization](https://qdrant.tech/articles/binary-quantization/), to our [fastembed library](https://qdrant.tech/articles/fastembed/) are all based on our principle. In this article, we will compare how Qdrant performs against the other vector search engines.

Here are the principles we followed while designing these benchmarks:

- We do comparative benchmarks, which means we focus on **relative numbers** rather than absolute numbers.
- We use affordable hardware, so that you can reproduce the results easily.
- We run benchmarks on the same exact machines to avoid any possible hardware bias.
- All the benchmarks are [open-sourced](https://github.com/qdrant/vector-db-benchmark), so you can contribute and improve them.

Scenarios we tested

1. Upload & Search benchmark on single node [Benchmark](https://qdrant.tech/benchmarks/single-node-speed-benchmark/)
2. Filtered search benchmark - [Benchmark](https://qdrant.tech/benchmarks/#filtered-search-benchmark)
3. Memory consumption benchmark - Coming soon
4. Cluster mode benchmark - Coming soon

Some of our experiment design decisions are described in the [F.A.Q Section](https://qdrant.tech/benchmarks/#benchmarks-faq).
Reach out to us on our [Discord channel](https://qdrant.to/discord) if you want to discuss anything related Qdrant or these benchmarks.

Share this article

[x](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmarks-intro%2F&text=How%20vector%20search%20should%20be%20benchmarked? "x")[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmarks-intro%2F "LinkedIn")

Up!

<|page-129-lllmstxt|>
## rag-and-genai
- [Articles](https://qdrant.tech/articles/)
- RAG & GenAI

#### RAG & GenAI

Leverage Qdrant for Retrieval-Augmented Generation (RAG) and build AI Agents

[![Preview](https://qdrant.tech/articles_data/agentic-rag/preview/preview.jpg)\\
**What is Agentic RAG? Building Agents with Qdrant** \\
Agents are a new paradigm in AI, and they are changing how we build RAG systems. Learn how to build agents with Qdrant and which framework to choose.\\
\\
Kacper Łukawski\\
\\
November 22, 2024](https://qdrant.tech/articles/agentic-rag/)[![Preview](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/preview/preview.jpg)\\
**Optimizing RAG Through an Evaluation-Based Methodology** \\
Learn how Qdrant-powered RAG applications can be tested and iteratively improved using LLM evaluation tools like Quotient.\\
\\
Atita Arora\\
\\
June 12, 2024](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/)[![Preview](https://qdrant.tech/articles_data/semantic-cache-ai-data-retrieval/preview/preview.jpg)\\
**Semantic Cache: Accelerating AI with Lightning-Fast Data Retrieval** \\
Semantic cache is reshaping AI applications by enabling rapid data retrieval. Discover how its implementation benefits your RAG setup.\\
\\
Daniel Romero, David Myriel\\
\\
May 07, 2024](https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/)[![Preview](https://qdrant.tech/articles_data/what-is-rag-in-ai/preview/preview.jpg)\\
**What is RAG: Understanding Retrieval-Augmented Generation** \\
Explore how RAG enables LLMs to retrieve and utilize relevant external data when generating responses, rather than being limited to their original training data alone.\\
\\
Sabrina Aquino\\
\\
March 19, 2024](https://qdrant.tech/articles/what-is-rag-in-ai/)[![Preview](https://qdrant.tech/articles_data/rag-is-dead/preview/preview.jpg)\\
**Is RAG Dead? The Role of Vector Databases in Vector Search \| Qdrant** \\
Uncover the necessity of vector databases for RAG and learn how Qdrant's vector database empowers enterprise AI with unmatched accuracy and cost-effectiveness.\\
\\
David Myriel\\
\\
February 27, 2024](https://qdrant.tech/articles/rag-is-dead/)

×

[Powered by](https://qdrant.tech/)

<|page-130-lllmstxt|>
## security
- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Security