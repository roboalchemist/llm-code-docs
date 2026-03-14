# Source: https://quarkus.io/ai-blueprints

Title: AI Blueprints

URL Source: https://quarkus.io/ai-blueprints

Markdown Content:
### AI blueprints offer conceptual, infrastructure-agnostic reference architectures for developing enterprise-grade AI solutions in Java.

![Image 1: AI blueprints icon](https://quarkus.io/assets/images/icons/icon-ai-blueprints.svg)![Image 2: AI blueprints icon](https://quarkus.io/assets/images/icons/icon-ai-blueprints-dark.svg)

Enterprise AI Blueprints for Java with Quarkus & LangChain4j
------------------------------------------------------------

The following three blueprints are conceptual, infrastructure-agnostic reference architectures. Each stands on its own and shows how to structure a Java solution with Quarkus (runtime, APIs, orchestration) and LangChain4j (LLM access, embeddings, tools, chains).

Quarkus provides the foundation for building secure, cloud-native, and AI-infused applications. Quarkus applications integrate with external model runtimes through LangChain4j, which offers rich abstractions for connecting to LLM providers, managing embeddings, defining tools, and orchestrating agentic workflows. This keeps AI where it belongs, as a capability embedded in enterprise applications, while Quarkus ensures performance, scalability, and operational reliability.

These blueprints demonstrate practical patterns and best practices for developing enterprise-grade AI solutions using a combination of these technologies. They aim to simplify the process of using AI in Java applications and guiding software architects along the way. Whether you're building intelligent chatbots, recommendation engines, or sophisticated data analysis tools, these blueprints provide a solid starting point for your next AI project. Explore each blueprint to discover how Quarkus and LangChain4j can enrich your Java applications with advanced AI capabilities.

### Frozen RAG (Retrieval-Augmented Generation)

Improve LLM accuracy with RAG, leveraging enterprise data. Quarkus handles RAG's entire process, including data ingestion, query execution, embedding, context retrieval, and LLM communication.

[Learn the basics of Frozen RAG](https://quarkus.io/ai-frozen-rag)

### Contextual RAG (Multi-Sources, Rerank, Injection)

Advanced Contextual RAG improves frozen RAG by adding multi-source retrieval, reranking, and content injection. This makes it ideal for complex enterprise scenarios, ensuring accuracy, relevance, and explainability across distributed information. It enables dynamic information handling, complex queries, and clear lineage for auditable, high-stakes decisions.

[Learn about Contextual RAG](https://quarkus.io/ai-contextual-rag)

### Chain-of-Thought (CoT) Reasoning

Chain-of-Thought (CoT) guides LLMs through explicit intermediate steps to solve complex problems. This systematic approach breaks tasks into manageable sub-problems for sequential processing and solution building. CoT enhances LLM accuracy, enabling understanding and debugging, especially for multi-step reasoning in mathematical problem-solving, code generation, and logical inference.

[Learn about Chain-of-Thought Reasoning](https://quarkus.io/ai-chain-of-thought)
