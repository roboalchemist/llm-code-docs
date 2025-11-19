# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/monitoring-your-rag-application.md

# Monitoring Your Rag Application

> Galileo Observe allows you to monitor your Retrieval-Augmented Generation (RAG) application with out-of-the-box Tracing and Analytics.

## Getting Started

The first step is to integrate Galileo Observe into your application code. If you're using Langchain, follow the [integration instructions here](/galileo/gen-ai-studio-products/galileo-observe/getting-started#langchain). If you're not using Langchain, or you're using a different kind of orchestration service, follow [these instructions](/galileo/gen-ai-studio-products/galileo-observe/getting-started#python-logger) on how to log your run. For any RAG or multi-step application, make sure to log your retriever node as well as your LLM node.

## Tracing your Retrieval System

Once you start logging your data to Galileo Observe, you can go to the Galileo Console to analyze your workflow executions. For each execution, you'll be able to see what the original input and the final output of the workflow were, as well as all the steps that were taken in between.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-monitoring-app-table.png)

Clicking on any row will open the Expanded View for that node. The Retriever Node will show you all the chunks that your retriever returned. Once you start debugging your executions, this will allow you to trace poor-quality responses back to the step that went wrong.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-monitoring-app-expanded-view.png)

## Evaluating the performance of your RAG application

Galileo has out-of-the-box [Guardrail Metrics](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) to help you assess and evaluate the quality of your application. In addition, Galileo supports user-defined [custom metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics). When logging your evaluation run, make sure to include the metrics you want computed for your run.

For RAG applications, we recommend using the following:

#### Context Adherence

*Context Adherence* (fka Groundedness) measures whether your model's response was purely based on the context provided, i.e. the response didn't state any facts not contained in the context provided. For RAG users, *Context Adherence* is a measurement of hallucinations.

If a response is *grounded* in the context (i.e. it has a value of 1 or close to 1), it only contains information given in the context. If a response is *not grounded* (i.e. it has a value of 0 or close to 0), it's likely to contain facts not included in the context provided to the model.

To fix low *Context Adherence* values, we recommend (1) ensuring your context DB has all the necessary info to answer the question, and (2) adjusting the prompt to tell the model to stick to the information it's given in the context.

*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.

**Context Relevance**

*Context Relevance* measures if the context has enough information to answer the user query.

High Context Relevance values indicate strong confidence that there is enough context to answer the question. Low Context Relevance values are a sign that you need to increase your Top K, modify your retrieval strategy, or use better embeddings.

**Completeness**

If *Context Adherence* is your precision metric for RAG, *Completeness* is your recall. In other words, it tries to answer the question: "Out of all the information in the context that's pertinent to the question, how much was covered in the answer?"

Low Completeness values indicate there's relevant information to the question included in your context that was not included in the model's response.

**Chunk Attribution**

Chunk Attribution is a chunk-level metric that denotes whether a chunk was or wasn't used by the model in generating the response. Attribution helps you more quickly identify why the model said what it did, without needing to read over the whole context.

Additionally, Attribution helps you optimize your retrieval strategy.

**Chunk Utilization**

Chunk Utilization measures how much of the text included in your chunk was used by the model to generate a response. Chunk Utilization helps you optimize your chunking strategy.

**Non-RAG specific Metrics**

Other metrics such as [*Uncertainty*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/uncertainty) and [*Correctness*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/correctness) might be useful as well. If these don't cover all your needs, you can always write custom metrics.
