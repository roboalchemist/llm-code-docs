# Source: https://docs.pinecone.io/integrations/trulens.md

# TruLens

> Using TruLens and Pinecone to evaluate grounded LLM applications

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

TruLens is a powerful open source library for evaluating and tracking large language model-based applications. TruLens provides a set of tools for developing and monitoring neural nets, including large language models (LLMs). This includes both tools for evaluation of LLMs and LLM-based applications with TruLens-Eval and deep learning explainability with TruLens-Explain.

To build an effective RAG-style LLM application, it is important to experiment with various configuration choices while setting up your Pinecone vector database, and study their impact on performance metrics. Tracking and evaluation with TruLens enables fast iteration of your application.

<PrimarySecondaryCTA secondaryHref={"#setup-guide"} secondaryLabel={"View setup guide"} />

## Setup guide

[TruLens](https://github.com/truera/trulens) is a powerful open source library for evaluating and tracking large language model-based applications. In this guide, we will show you how to use TruLens to evaluate applications built on top of a high performance Pinecone vector database.

### Why TruLens?

Systematic evaluation is needed to support reliable, non-hallucinatory LLM-based applications. TruLens contains instrumentation and evaluation tools for large language model (LLM)-based applications. For evaluation, TruLens provides a set of feedback functions, analogous to labeling functions, to programmatically score the input, output and intermediate text of an LLM app. Each LLM application request can be scored on its question-answer relevance, context relevance and groundedness. These feedback functions provide evidence that your LLM-application is non-hallucinatory.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/1.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=5e9bed118e6b241799bf579d0f528247" alt="diagram-1" data-og-width="1721" width="1721" data-og-height="598" height="598" data-path="images/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/1.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=08db4c06a2f1f3eab651e2ee2dce9fd8 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/1.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=616758e4f7f4dfb657d98142a287965e 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/1.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9e89e1b1c185dddadc25637f87df30a2 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/1.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3e1471b914e6cffb8d3c629084f01e1f 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/1.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=24f7f161ef9257050fdc062d7c638a5e 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/1.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=32f0d2e3ff4fabe3c7d407a0a3ac4a01 2500w" />

In addition to the above, feedback functions also support the evaluation of ground truth agreement, sentiment, model agreement, language match, toxicity, and a full suite of moderation evaluations, including hate, violence and more. TruLens implements feedback functions as an extensible framework that can evaluate your custom needs as well.

During the development cycle, TruLens supports the iterative development of a wide range of LLM applications by wrapping your application to log cost, latency, key metadata and evaluations of each application run. This allows you to track and identify failure modes, pinpoint their root cause, and measure improvement across experiments.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/2.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=ab375c103797d6ed5cc3e6a4f86b637f" alt="application-screenshot" data-og-width="1494" width="1494" data-og-height="700" height="700" data-path="images/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/2.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=bb1da067913ac5f726dffd8a102357b4 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/2.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=4df448fe4e85641d732fc003fdb0caf6 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/2.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=d795ca7efa2aead62a861f1af8da237d 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/2.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6536021c3b233d53162fee1b82ddb5fa 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/2.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8cb8cd60ab2f524180715c3e75521ed0 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/2.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c7784c2edd556209898448807d4196c8 2500w" />

### Why Pinecone?

Large language models alone have a hallucination problem. Several decades of machine learning research have optimized models, including modern LLMs, for generalization, while actively penalizing memorization. However, many of today's applications require factual, grounded answers. LLMs are also expensive to train, and provided by third party APIs. This means the knowledge of an LLM is fixed. Retrieval-augmented generation (RAG) is a way to reliably ensure models are grounded, with Pinecone as the curated source of real world information, long term memory, application domain knowledge, or whitelisted data.

In the RAG paradigm, rather than just passing a user question directly to a language model, the system retrieves any documents that could be relevant in answering the question from the knowledge base, and then passes those documents (along with the original question) to the language model to generate the final response. The most popular method for RAG involves chaining together LLMs with vector databases, such as the widely used Pinecone vector DB.

In this process, a numerical vector (an embedding) is calculated for all documents, and those vectors are then stored in a database optimized for storing and querying vectors. Incoming queries are vectorized as well, typically using an encoder LLM to convert the query into an embedding. The query embedding is then matched via embedding similarity against the document embeddings in the vector database to retrieve the documents that are relevant to the query.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/3.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3c3b7194183c239a69db1989b77fa15d" alt="diagram-2" data-og-width="1364" width="1364" data-og-height="623" height="623" data-path="images/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/3.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e5434da70f2237fe8735fe18ac1e2291 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/3.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=00cdb8549012faee0dd649322b9d5da1 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/3.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=a2e803adf53599748a030e9f89259891 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/3.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=4c8d0a28e052574131736cde74cf6479 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/3.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3835b02af50749b0200cbd39a2de58d3 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/3.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6ab02341c8579fbf5c6b2a121ef52811 2500w" />

Pinecone makes it easy to build high-performance vector search applications, including retrieval-augmented question answering. Pinecone can easily handle very large scales of hundreds of millions and even billions of vector embeddings. Pinecone's large scale allows it to handle long term memory or a large corpus of rich external and domain-appropriate data so that the LLM component of RAG application can focus on tasks like summarization, inference and planning. This setup is optimal for developing a non-hallucinatory application.\
In addition, Pinecone is fully managed, so it is easy to change configurations and components. Combined with the tracking and evaluation with TruLens, this is a powerful combination that enables fast iteration of your application.

### Using Pinecone and TruLens to improve LLM performance and reduce hallucination

To build an effective RAG-style LLM application, it is important to experiment with various configuration choices while setting up the vector database, and study their impact on performance metrics.

In this example, we explore the downstream impact of some of these configuration choices on response quality, cost and latency with a sample LLM application built with Pinecone as the vector DB. The evaluation and experiment tracking is done with the [TruLens](https://www.trulens.org/) open source library. TruLens offers an extensible set of [feedback functions](https://truera.com/ai-quality-education/generative-ai-and-llms/whats-missing-to-evaluate-foundation-models-at-scale/) to evaluate LLM apps and enables developers to easily track their LLM app experiments.

In each component of this application, different configuration choices can be made that can impact downstream performance. Some of these choices include the following:

**Constructing the Vector DB**

* Data preprocessing and selection
* Chunk Size and Chunk Overlap
* Index distance metric
* Selection of embeddings

**Retrieval**

* Amount of context retrieved (top k)
* Query planning

**LLM**

* Prompting
* Model choice
* Model parameters (size, temperature, frequency penalty, model retries, etc.)

These configuration choices are useful to keep in mind when constructing your app. In general, there is no optimal choice for all use cases. Rather, we recommend that you experiment with and evaluate a variety of configurations to find the optimal selection as you are building your application.

#### Creating the index in Pinecone

Here we'll download a pre-embedded dataset from the `pinecone-datasets` library allowing us to skip the embedding and preprocessing steps.

```Python Python theme={null}
import pinecone_datasets

dataset = pinecone_datasets.load_dataset('wikipedia-simple-text-embedding-ada-002-100K')
dataset.head()
```

After downloading the data, we can initialize our pinecone environment and create our first index. Here, we have our first potentially important choice, by selecting the **distance metric** used for our index.

```Python Python theme={null}
pinecone.create_index(
        name=index_name_v1,
        metric='cosine', # We'll try each distance metric here.
        dimension=1536  # 1536 dim of text-embedding-ada-002.
)
```

Then, we can upsert our documents into the index in batches.

```Python Python theme={null}
for batch in dataset.iter_documents(batch_size=100):
    index.upsert(batch)
```

#### Build the vector store

Now that we've built our index, we can start using LangChain to initialize our vector store.

```Python Python theme={null}
embed = OpenAIEmbeddings(
    model='text-embedding-ada-002',
    openai_api_key=OPENAI_API_KEY
)

from langchain.vectorstores import Pinecone

text_field = "text"

# Switch back to a normal index for LangChain.
index = pinecone.Index(index_name_v1)

vectorstore = Pinecone(
    index, embed.embed_query, text_field
)
```

In RAG, we take the query as a question that is to be answered by an LLM, but the LLM must answer the question based on the information it receives from the `vectorstore`.

#### Initialize our RAG application

To do this, we initialize a `RetrievalQA` as our app:

```Python Python theme={null}
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# completion llm
llm = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)
```

#### TruLens for evaluation and tracking of LLM experiments

Once we've set up our app, we should put together our [feedback functions](https://truera.com/ai-quality-education/generative-ai-and-llms/whats-missing-to-evaluate-foundation-models-at-scale/). As a reminder, feedback functions are an extensible method for evaluating LLMs. Here we'll set up two feedback functions: `qs_relevance` and `qa_relevance`. They're defined as follows:

*QS Relevance: query-statement relevance is the average of relevance (0 to 1) for each context chunk returned by the semantic search.*
*QA Relevance: question-answer relevance is the relevance (again, 0 to 1) of the final answer to the original question.*

```Python Python theme={null}
# Imports main tools for eval
from trulens_eval import TruChain, Feedback, Tru, feedback, Select
import numpy as np
tru = Tru()

# OpenAI as feedback provider
openai = feedback.OpenAI()

# Question/answer relevance between overall question and answer.
qa_relevance = Feedback(openai.relevance).on_input_output()

# Question/statement relevance between question and each context chunk.
qs_relevance = 
Feedback(openai.qs_relevance).
on_input()
# See explanation below 
.on(Select.Record.app.combine_documents_chain._call.args.inputs.input_documents[:].page_content)
.aggregate(np.mean)

```

Our use of selectors here also requires an explanation.

QA Relevance is the simpler of the two. Here, we are using `.on_input_output()` to specify that the feedback function should be applied on both the input and output of the application.

For QS Relevance, we use TruLens selectors to locate the context chunks retrieved by our application. Let's break it down into simple parts:

1. Argument Specification – The `on_input` which appears first is a convenient shorthand and states that the first argument to `qs_relevance` (the question) is to be the main input of the app.

2. Argument Specification – The `on(Select...)` line specifies where the statement argument to the implementation comes from. We want to evaluate the context chunks, which are an intermediate step of the LLM app. This form references the langchain app object call chain, which can be viewed from `tru.run_dashboard()`. This flexibility allows you to apply a feedback function to any intermediate step of your LLM app. Below is an example where TruLens displays how to select each piece of the context.

   <img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/4.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=5822c0cf4ac339a43386120b9c8bdea0" alt="subcomponents" data-og-width="1850" width="1850" data-og-height="336" height="336" data-path="images/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/4.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=1491ad9e2af87a72d4d94eb7dbd1ab59 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/4.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=a3cfbb5990e305c451d5bf3a713d4d2e 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/4.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e3a8b5e552edc5ece5c28d76d88aa264 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/4.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3739a31a93ddd97eafed5fe7d3880551 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/4.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e0b55c3382063504157437bbdb66f8d0 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/4.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8d0811e7ecd13123debafd0ab0eeffac 2500w" />

3. Aggregation specification -- The last line aggregate (`np.mean`) specifies how feedback outputs are to be aggregated. This only applies to cases where the argument specification names more than one value for an input or output.

The result of these lines is that `f_qs_relevance` can be now be run on apps/records and will automatically select the specified components of those apps/records

To finish up, we just wrap our Retrieval QA app with TruLens along with a list of the feedback functions we will use for eval.

```Python Python theme={null}
# wrap with TruLens
truchain = TruChain(qa,
    app_id='Chain1_WikipediaQA',
    feedbacks=[qa_relevance, qs_relevance])

truchain(“Which state is Washington D.C. in?”)
```

After submitting a number of queries to our application, we can track our experiment and evaluations with the TruLens dashboard.

```Python Python theme={null}
tru.run_dashboard()
```

Here is a view of our first experiment:

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/5.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=25f3f2684029f23e72189334db906f49" alt="trulens-dashboard-1" data-og-width="1017" width="1017" data-og-height="143" height="143" data-path="images/5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/5.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=835238582da8592aa840dff87c69d283 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/5.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=20e7c6e981a9657b8e4304ee221725dc 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/5.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8c4423f3be2668ae666485c98c1b5a47 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/5.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9f4eb89c6c00735276f5064000e4ce3c 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/5.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=dc0b96deb57e9ac8c711afe0698669d2 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/5.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e25fde50e8e1c25a4d0d8edb102b6b6a 2500w" />

#### Experiment with distance metrics

Now that we've walked through the process of building our tracked RAG application using cosine as the distance metric, all we have to do for the next two experiments is to rebuild the index with `euclidean` or `dotproduct` as the metric and follow the rest of the steps above as is.

Because we are using OpenAI embeddings, which are normalized to length 1, dot product and cosine distance are equivalent - and Euclidean will also yield the same ranking. See the OpenAI docs for more information. With the same document ranking, we should not expect a difference in response quality, but computation latency may vary across the metrics. Indeed, OpenAI advises that dot product computation may be a bit faster than cosine. We will be able to confirm this expected latency difference with TruLens.

```Python Python theme={null}
index_name_v2 = 'langchain-rag-euclidean'
pinecone.create_index(
        name=index_name_v2,
        metric='euclidean', # metric='dotproduct',
        dimension=1536,  # 1536 dim of text-embedding-ada-002
    )
```

After doing so, we can view our evaluations for all three LLM apps sitting on top of the different indexes. All three apps are struggling with query-statement relevance. In other words, the context retrieved is only somewhat relevant to the original query.

**We can also see that both the Euclidean and dot-product metrics performed at a lower latency than cosine at roughly the same evaluation quality.**

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=cf0234cb8924dc23cf364387f9126881" alt="trulens-dashboard-2" data-og-width="1013" width="1013" data-og-height="523" height="523" data-path="images/6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0d1fd6b71d55bf6984310e89b2ecb5d0 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0320201157b8d94a87114b3cd83590c3 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=1f3790b99f600f60a7bffc26043d85be 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6888d3ded645a16c00f8b050cac5b76f 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=7b309425a15f78d512e6fe6f31136bb0 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=27ce449f1ece420647c93eb824a09809 2500w" />

### Problem: hallucination

Digging deeper into the Query Statement Relevance, we notice one problem in particular with a question about famous dental floss brands. The app responds correctly, but is not backed up by the context retrieved, which does not mention any specific brands.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/7.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9de7098b912d0249ba900299660f921b" alt="trulens-dashboard-feedback-1" data-og-width="586" width="586" data-og-height="415" height="415" data-path="images/7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/7.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=bf334c79229d877737f0e3c185ca4fc1 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/7.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=04cf66c99f0a9eb630dccd679d8e449b 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/7.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=748327f7716489fcb324eab2cef25530 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/7.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=206f5881eccf29d1cd20f237f7c2fb70 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/7.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=da5fe01f0e281b7b8d9a2d24cf6ab2b9 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/7.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=993e9de4e3545808d384fd2939dd5eb7 2500w" />

#### Quickly evaluate app components with LangChain and TruLens

Using a less powerful model is a common way to reduce hallucination for some applications. We'll evaluate ada-001 in our next experiment for this purpose.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/8.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=7dea53e93c7189bb81de5a2d331961a0" alt="trulens-dashboard-3" data-og-width="992" width="992" data-og-height="128" height="128" data-path="images/8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/8.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e49e676788190ab84141fcc7ccf6793d 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/8.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=ad8b8a8f72e58a446be8b40857d82ac6 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/8.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=795c0bbbef65f993640e8cfe866d5580 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/8.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=367b1f5de867b4dcebf896ffda9be192 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/8.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=165d075015baf3a519f38e5cc7d28082 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/8.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f949f8604d0bfa2008304a6a3b893eb2 2500w" />

Changing different components of apps built with frameworks like LangChain is really easy. In this case we just need to call `text-ada-001` from the LangChain LLM store. Adding in easy evaluation with TruLens allows us to quickly iterate through different components to find our optimal app configuration.

```Python Python theme={null}
# completion llm
from langchain.llms import OpenAI

llm = OpenAI(
    model_name='text-ada-001',
    temperature=0
)

from langchain.chains import RetrievalQAWithSourcesChain
qa_with_sources = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# wrap with TruLens
truchain = TruChain(qa_with_sources,
    app_id='Chain4_WikipediaQA',
    feedbacks=[qa_relevance, qs_relevance])
```

**However, this configuration with a less powerful model struggles to return a relevant answer given the context provided.**

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/9.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=73f93e1a26ded0ae6a52c5a9a750884f" alt="trulens-dashboard-4" data-og-width="1022" width="1022" data-og-height="147" height="147" data-path="images/9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/9.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3e4b4149212a2da4004067d610f0afec 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/9.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=cd650d3ae9c67b99aacd1738d22ea742 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/9.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f0a5a73fc8c792fff9d462110328382c 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/9.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9bba67d6abfaa9fbfe752995ace04cfc 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/9.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=607a0defab012a6e6095d0667f358bb1 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/9.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=7783a78d4ffd11c269d2a297f9bc0ecb 2500w" />

For example, when asked “Which year was Hawaii's state song written?”, the app retrieves context that contains the correct answer but fails to respond with that answer, instead simply responding with the name of the song.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/10.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=20bd62ec726af77b872cfd34b3f6370e" alt="trulens-dashboard-feedback-2" data-og-width="648" width="648" data-og-height="430" height="430" data-path="images/10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/10.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=e0ed4a0b3a43bbbf1032717a69543790 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/10.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=b21ca5cfacc36d408d3cb9fd9b341484 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/10.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0908b2ad2fe0fff3f2733917293afdb6 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/10.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=5770a6f19f8856971415daaa5fd12a54 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/10.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=736c2727fa3f5f8c62f6236d8327b166 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/10.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=a17ccd36ca1a0d7792674c18b4c90b33 2500w" />

While our relevance function is not doing a great job here in differentiating which context chunks are relevant, we can manually see that only the one (the 4th chunk) mentions the year the song was written. Narrowing our `top_k`, or the number of context chunks retrieved by the semantic search, may help.

We can do so as follows:

```Python Python theme={null}
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(top_k = 1)
)
```

The way the `top_k` is implemented in LangChain's RetrievalQA is that the documents are still retrieved by semantic search and only the `top_k` are passed to the LLM. Therefore, TruLens also captures all of the context chunks that are being retrieved. In order to calculate an accurate QS Relevance metric that matches what's being passed to the LLM, we only calculate the relevance of the top context chunk retrieved by slicing the `input_documents` passed into the TruLens Select function:

```Python Python theme={null}
qs_relevance = Feedback(openai.qs_relevance).on_input().on(
    Select.Record.app.combine_documents_chain._call.args.inputs.input_documents[:1].page_content
).aggregate(np.mean)
```

Once we've done so, our final application has much improved `qs_relevance`, `qa_relevance` and latency!

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/11.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8d020d3573789f3a84a33ab2454c6017" alt="trulens-dashboard-5" data-og-width="832" width="832" data-og-height="114" height="114" data-path="images/11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/11.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=fa84e46a4c4ca2de65e52a3a4ff7510e 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/11.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=bcb077e2814852755c8052d98a1d2c00 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/11.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=b8518e0ca388d9b1379507f2f5cc8288 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/11.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=4b0f852fb9db98a5b73bba39805b95d2 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/11.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9540196c0ca72a2db5bc3d9f4fd9bd4f 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/11.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=fb17431f19c302f6be5ebe9d5cc67372 2500w" />

With that change, our application is successfully retrieving the one piece of context it needs, and successfully forming an answer from that context.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/12.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=d304b502bf601fb1f4fe24fb05daa325" alt="trulens-dashboard-feedback-3" data-og-width="653" width="653" data-og-height="413" height="413" data-path="images/12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/12.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=ad0f9bd7fcfacd0d8964f94b5dcf9944 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/12.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=fc2e4954cd701b53def3ed93f25a600c 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/12.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=7511483fb00d8a089205ac2654e9719e 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/12.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c03adca2cbba373c46e3b426621e1696 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/12.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=1440bace9aedb35a9d82d962f18e9e2d 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/12.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8f8934d528f22980ca4a4337d3db5d53 2500w" />

Even better, the application now knows what it doesn't know:

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/13.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9752560cdd280531c09feecf1d4492af" alt="trulens-dashboard-feedback-4" data-og-width="494" width="494" data-og-height="217" height="217" data-path="images/13.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/13.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0fc55c8534f61a5e58e505c4dc6ecbf9 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/13.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=14629e78fcadde9f8d782c4e5a0bda3a 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/13.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f6d11230665696a6fe965c6da2333d6e 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/13.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6a9c57780f6a5f0678ce4de25fdee4e3 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/13.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=499aad55bf8c556818dc9cf184f77055 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/13.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=84973891f083f8a33d45090fa0b7c20e 2500w" />

### Summary

In conclusion, we note that exploring the downstream impact of some Pinecone configuration choices on response quality, cost and latency is an important part of the LLM app development process, ensuring that we make the choices that lead to the app performing the best. Overall, TruLens and Pinecone are the perfect combination for building reliable RAG-style applications. Pinecone provides a way to efficiently store and retrieve context used by LLM apps, and TruLens provides a way to track and evaluate each iteration of your application.
