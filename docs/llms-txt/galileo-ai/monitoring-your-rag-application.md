# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/monitoring-your-rag-application.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Your Rag Application

> Galileo Observe allows you to monitor your Retrieval-Augmented Generation (RAG) application with out-of-the-box Tracing and Analytics.

## Getting Started

The first step is to integrate Galileo Observe into your application code. If you're using Langchain, follow the [integration instructions here](/galileo/gen-ai-studio-products/galileo-observe/getting-started#langchain). If you're not using Langchain, or you're using a different kind of orchestration service, follow [these instructions](/galileo/gen-ai-studio-products/galileo-observe/getting-started#python-logger) on how to log your run. For any RAG or multi-step application, make sure to log your retriever node as well as your LLM node.

## Tracing your Retrieval System

Once you start logging your data to Galileo Observe, you can go to the Galileo Console to analyze your workflow executions. For each execution, you'll be able to see what the original input and the final output of the workflow were, as well as all the steps that were taken in between.

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-table.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=a3b473a23ae0854fce061736a2be152f" alt="" data-og-width="1312" width="1312" data-og-height="1033" height="1033" data-path="images/observe-monitoring-app-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-table.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=c4f199a34a34321e4e0e3a4c3ecae7f6 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-table.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=966b22955ba2c2e3b34e5558af140558 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-table.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=55c52628e9dd1d6fbe810f7ededa8252 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-table.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=09f1bfb6bcb027d1ce0291f04b4a6d74 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-table.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=778e02e8f07134a121cb5b9a2a06be22 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-table.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=68316f5622da9ef1cc1a80b4dd50d447 2500w" />

Clicking on any row will open the Expanded View for that node. The Retriever Node will show you all the chunks that your retriever returned. Once you start debugging your executions, this will allow you to trace poor-quality responses back to the step that went wrong.

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-expanded-view.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=9f4934ec244867d487b3f2be29f29cfa" alt="" data-og-width="1215" width="1215" data-og-height="989" height="989" data-path="images/observe-monitoring-app-expanded-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-expanded-view.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1101e5f7a593d5e91db6fb34f235bb0a 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-expanded-view.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=155b3e7b46b844b1915b2ec6c47e7d5d 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-expanded-view.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=f89150ed9931d570fca71dc74ec24f52 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-expanded-view.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=338aff64a5bca2ecc45180887da433b0 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-expanded-view.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=012694382a03fce9cfe59951640b39f9 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-monitoring-app-expanded-view.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=eaa804580c8d6a070b730099669c66bb 2500w" />

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
