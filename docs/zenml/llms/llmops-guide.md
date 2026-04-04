# Source: https://docs.zenml.io/user-guides/llmops-guide.md

# LLMOps guide

Welcome to the ZenML LLMOps Guide, where we dive into the exciting world of Large Language Models (LLMs) and how to integrate them seamlessly into your MLOps pipelines using ZenML. This guide is designed for ML practitioners and MLOps engineers looking to harness the potential of LLMs while maintaining the robustness and scalability of their workflows.

<figure><img src="https://3621652509-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F75OYotLPi8TviSrtZTJZ%2Fuploads%2Fgit-blob-8a522192dc730f1ff6aecff32e29523da3258cbd%2Frag-overview.png?alt=media" alt=""><figcaption><p>ZenML simplifies the development and deployment of LLM-powered MLOps pipelines.</p></figcaption></figure>

In this guide, we'll explore various aspects of working with LLMs in ZenML, including:

* [RAG with ZenML](https://docs.zenml.io/user-guides/llmops-guide/rag-with-zenml)
  * [RAG in 85 lines of code](https://docs.zenml.io/user-guides/llmops-guide/rag-with-zenml/rag-85-loc)
  * [Understanding Retrieval-Augmented Generation (RAG)](https://docs.zenml.io/user-guides/llmops-guide/rag-with-zenml/understanding-rag)
  * [Data ingestion and preprocessing](https://docs.zenml.io/user-guides/llmops-guide/rag-with-zenml/data-ingestion)
  * [Embeddings generation](https://docs.zenml.io/user-guides/llmops-guide/rag-with-zenml/embeddings-generation)
  * [Storing embeddings in a vector database](https://docs.zenml.io/user-guides/llmops-guide/rag-with-zenml/storing-embeddings-in-a-vector-database)
  * [Basic RAG inference pipeline](https://docs.zenml.io/user-guides/llmops-guide/rag-with-zenml/basic-rag-inference-pipeline)
* [Evaluation and metrics](https://docs.zenml.io/user-guides/llmops-guide/evaluation)
  * [Evaluation in 65 lines of code](https://docs.zenml.io/user-guides/llmops-guide/evaluation/evaluation-in-65-loc)
  * [Retrieval evaluation](https://docs.zenml.io/user-guides/llmops-guide/evaluation/retrieval)
  * [Generation evaluation](https://docs.zenml.io/user-guides/llmops-guide/evaluation/generation)
  * [Evaluation in practice](https://docs.zenml.io/user-guides/llmops-guide/evaluation/evaluation-in-practice)
* [Reranking for better retrieval](https://docs.zenml.io/user-guides/llmops-guide/reranking)
  * [Understanding reranking](https://docs.zenml.io/user-guides/llmops-guide/reranking/understanding-reranking)
  * [Implementing reranking in ZenML](https://docs.zenml.io/user-guides/llmops-guide/reranking/implementing-reranking)
  * [Evaluating reranking performance](https://docs.zenml.io/user-guides/llmops-guide/reranking/evaluating-reranking-performance)
* [Improve retrieval by finetuning embeddings](https://docs.zenml.io/user-guides/llmops-guide/finetuning-embeddings)
  * [Synthetic data generation](https://docs.zenml.io/user-guides/llmops-guide/finetuning-embeddings/synthetic-data-generation)
  * [Finetuning embeddings with Sentence Transformers](https://docs.zenml.io/user-guides/llmops-guide/finetuning-embeddings/finetuning-embeddings-with-sentence-transformers)
  * [Evaluating finetuned embeddings](https://docs.zenml.io/user-guides/llmops-guide/finetuning-embeddings/evaluating-finetuned-embeddings)
* [Finetuning LLMs with ZenML](https://docs.zenml.io/user-guides/llmops-guide/finetuning-llms)
  * [Finetuning in 100 lines of code](https://docs.zenml.io/user-guides/llmops-guide/finetuning-llms/finetuning-100-loc)
  * [Why and when to finetune LLMs](https://docs.zenml.io/user-guides/llmops-guide/finetuning-llms/why-and-when-to-finetune-llms)
  * [Starter choices with finetuning](https://docs.zenml.io/user-guides/llmops-guide/finetuning-llms/starter-choices-for-finetuning-llms)
  * [Finetuning with 🤗 Accelerate](https://docs.zenml.io/user-guides/llmops-guide/finetuning-llms/finetuning-with-accelerate)
  * [Evaluation for finetuning](https://docs.zenml.io/user-guides/llmops-guide/finetuning-llms/evaluation-for-finetuning)
  * [Deploying finetuned models](https://docs.zenml.io/user-guides/llmops-guide/finetuning-llms/deploying-finetuned-models)
  * [Next steps](https://docs.zenml.io/user-guides/llmops-guide/finetuning-llms/next-steps)

To follow along with the examples and tutorials in this guide, ensure you have a Python environment set up with ZenML installed. Familiarity with the concepts covered in the [Starter Guide](https://docs.zenml.io/user-guides/starter-guide) and [Production Guide](https://docs.zenml.io/user-guides/production-guide) is recommended.

We'll showcase a specific application over the course of this LLM guide, showing how you can work from a simple RAG pipeline to a more complex setup that involves finetuning embeddings, reranking retrieved documents, and even finetuning the LLM itself. We'll do this all for a use case relevant to ZenML: a question answering system that can provide answers to common questions about ZenML. This will help you understand how to apply the concepts covered in this guide to your own projects.

By the end of this guide, you'll have a solid understanding of how to leverage LLMs in your MLOps workflows using ZenML, enabling you to build powerful, scalable, and maintainable LLM-powered applications. First up, let's take a look at a super simple implementation of the RAG paradigm to get started.

<figure><img src="https://static.scarf.sh/a.png?x-pxid=f0b4f458-0a54-4fcd-aa95-d5ee424815bc" alt="ZenML Scarf"><figcaption></figcaption></figure>
