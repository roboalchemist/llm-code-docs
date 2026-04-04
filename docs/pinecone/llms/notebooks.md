# Source: https://docs.pinecone.io/examples/notebooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Notebooks

export const UtilityExampleCard = ({title, text, link}) => {
  return <a href={link} className="example-card group">
            <h2 className="font-bold" style={{
    fontSize: "0.875rem"
  }}>{title}</h2>
            <p style={{
    fontSize: "0.875rem",
    marginTop: "0"
  }}>{text}</p>
        </a>;
};

export const ExampleCard = ({title, text, link, children, arrow, vectors, namespaces}) => {
  return <a href={link} className="example-card group">
            <h2 className="font-semibold text-base">{title}</h2>
            <p>{text}</p>

            {children && <div className="tags">{children}</div>}

            {arrow && <svg xmlns="http://www.w3.org/2000/svg" className="arrow" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M5.30739 20L4 18.6926L16.8249 5.8677H5.05837V4H20V18.9416H18.1323V7.1751L5.30739 20Z" fill="var(--text-secondary)" />
            </svg>}

            {(vectors || namespaces) && <div className="vectors">
                {vectors && <span>{vectors} vectors</span>}
                {namespaces && <span>{namespaces} namespaces</span>}
            </div>}
        </a>;
};

export const Tag = ({text, icon}) => {
  return <span className="card-tag">
            {icon && <img src={icon} className={`w-4 h-4 object-contain ${icon.includes("openai") ? "dark-inverted" : ""}`} />}
            {text}
        </span>;
};

<h2 className="examples-h2">Search</h2>

<div className="card-grid not-prose">
  <ExampleCard title="Semantic search" text="Implement semantic search over a dense index to find records that are similar in meaning to a given query." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/semantic-search.ipynb" arrow>
    <Tag text="Pinecone Integrated Inference" />

    <Tag text="Hugging Face Datasets" icon="/images/examples/huggingface-icon.svg" />

    <Tag text="llama-text-embed-v2" />
  </ExampleCard>

  <ExampleCard title="Lexical search" text="Implement lexical search over a sparse index to find records that most exactly match the words or phrases in a query." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/lexical-search.ipynb" arrow>
    <Tag text="Pinecone Integrated Inference" />

    <Tag text="pinecone-sparse-english-v0" />

    <Tag text="bge-reranker-v2-m3" />
  </ExampleCard>

  <ExampleCard title="Cascading retrieval" text="Implement cascading retrieval (hybrid search with two indexes) to combine the benefits of semantic and lexical search." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/cascading-retrieval.ipynb" arrow>
    <Tag text="Pinecone Integrated Inference" />

    <Tag text="llama-text-embed-v2" />

    <Tag text="pinecone-sparse-english-v0" />

    <Tag text="bge-reranker-v2-m3" />
  </ExampleCard>

  <ExampleCard title="Reranking search results" text="Use Pinecone's reranking feature to enhance the accuracy of search results." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-reranker.ipynb" arrow>
    <Tag text="Pinecone Inference" />

    <Tag text="bge-reranker-v2-m3" icon="https://cdn.sanity.io/images/vr8gru94/production/40b1d05ee1325e6d9e4886af4e76ff06d844faff-188x188.jpg" />
  </ExampleCard>
</div>

<h2 className="examples-h2">Retrieval-augmented generation (RAG)</h2>

<div className="card-grid not-prose">
  <ExampleCard title="RAG with hybrid search and Claude" text="Implement simple retrieval-augmented generation with hybrid search and Anthropic's Claude models" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/learn/generation/traditional-rag/traditional-rag-with-claude-and-hybrid.ipynb" arrow>
    <Tag text="claude-3-5-haiku-latest" />

    <Tag text="llama-text-embed-v2" />

    <Tag text="pinecone-sparse-english-v0" />

    <Tag text="Dense Indexes" />

    <Tag text="Sparse Indexes" />

    <Tag text="Hybrid Search" />
  </ExampleCard>

  <ExampleCard title="Agentic RAG with Claude" text="Build an agentic RAG pipeline that uses tools to retrieve data from web search and Pinecone semantic search, then generates responses using Anthropic's Claude models" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/learn/generation/agentic-rag/agentic-rag-with-claude.ipynb" arrow>
    <Tag text="claude-3-5-haiku-latest" />

    <Tag text="llama-text-embed-v2" />

    <Tag text="Dense Indexes" />

    <Tag text="Tool use" />
  </ExampleCard>

  <ExampleCard title="RAG with LangChain and OpenAI" text="Learn how RAG can be used with Pinecone to reduce hallucinations, by grounding responses using our own release notes" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/langchain-retrieval-augmentation.ipynb" arrow>
    <Tag text="gpt-5" icon="/images/examples/openai-icon.svg" />

    <Tag text="text-embedding-3-small" icon="/images/examples/openai-icon.svg" />

    <Tag text="OpenAI" />

    <Tag text="LangChain" />
  </ExampleCard>

  <ExampleCard title="RAG with cascading retrieval and OpenAI " text="Investigate research papers by implementing cascading retrieval, then pass results to OpenAI to generate answers" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb" arrow>
    <Tag text="gpt-4o-mini" icon="/images/examples/openai-icon.svg" />

    <Tag text="llama-text-embed-v2" />

    <Tag text="pinecone-sparse-english-v0" />

    <Tag text="Dense Indexes" />

    <Tag text="Sparse Indexes" />

    <Tag text="Cascading Retrieval" />
  </ExampleCard>

  <ExampleCard title="Retrieval Agents with Pinecone Assistant, LangChain and LangGraph" text="Create a study guide generator using agentic retrieval and the Pinecone Assistant Context API" link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/langchain-retrieval-agent.ipynb" arrow>
    <Tag text="gpt-4o-mini" icon="/images/examples/openai-icon.svg" />

    <Tag text="gpt-4.1" icon="/images/examples/openai-icon.svg" />

    <Tag text="LangChain" />

    <Tag text="LangGraph" />

    <Tag text="Agentic Retrieval" />

    <Tag text="Structured Generation" />
  </ExampleCard>
</div>

<h2 className="examples-h2">Miscellaneous</h2>

<div className="card-grid not-prose">
  <ExampleCard title="Import from object storage" text="Import records from Parquet files in Amazon S3 bucket into a serverless index." link="https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-import.ipynb" arrow>
    <Tag text="Amazon S3" />
  </ExampleCard>
</div>
