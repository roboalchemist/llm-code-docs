# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-rag-applications.md

# Evaluate and Optimize RAG Applications

> How to use Galileo Evaluate with RAG applications

Galileo Evaluate enables you to evaluate and optimize your Retrieval-Augmented Generation (RAG) application with out-of-the-box Tracing and Analytics.

## Getting Started

The first step in evaluating your application is creating an evaluation run. To do this, run your evaluation set (e.g. a set of inputs that mimic the inputs you expect to get from users) through your RAG system and create a prompt run.

Follow [these instructions](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/custom-chain#logging-rag-workflows) to integrate `promptquality` into your RAG workflows and create Evaluation Runs on Galileo.

<Info>If you're using LangChain, we recommend you use the Galileo Langchain callback instead. See [these instructions](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/langchain) for more details.</Info>

#### Keeping track of what changed in your experiment

As you start experimenting, you're going to want to keep track of what you're attempting with each experiment. To do so, use Prompt Tags. Prompt Tags are tags you can add to the run (e.g. "embedding\_model" = "voyage-2", "embedding\_model" = "text-embedding-ada-002").

Prompt Tags will help you remember what you tried with each experiment. Read more about [how to add Prompt Tags here](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/add-tags-and-metadata-to-prompt-runs).

## Tracing your Retrieval System

Once you log your evaluation runs, you can go to the Galileo Console to analyze your workflow executions. For each execution, you'll be able to see what the input into the workflow was and what the final response was, as well as any intermediate results.

![Tracing your Retrieval System](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/rag.png)

Clicking on any row will open the Expanded View for that node. The Retriever Node will show you all the chunks that your retriever returned. Once you start debugging your executions, this will allow you to trace poor-quality responses back to the step that went wrong.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/ev-op-2.png)

## Evaluating and Optimizing the performance of your RAG application

Galileo has out-of-the-box [Guardrail Metrics](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) to help you assess and evaluate the quality of your application. In addition, Galileo supports user-defined [custom metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics). When logging your evaluation run, make sure to include the metrics you want computed for your run.

For RAG applications, we recommend using the following:

#### Context Adherence

*Context Adherence* (fka Groundedness) measures whether your model's response was purely based on the context provided, i.e. the response didn't state any facts not contained in the context provided. For RAG users, *Context Adherence* is a measurement of hallucinations.

If a response is *grounded* in the context (i.e. it has a value of 1 or close to 1), it only contains information given in the context. If a response is *not grounded* (i.e. it has a value of 0 or close to 0), it's likely to contain facts not included in the context provided to the model.

To fix low *Context Adherence* values, we recommend (1) ensuring your context DB has all the necessary info to answer the question, and (2) adjusting the prompt to tell the model to stick to the information it's given in the context.

*Note:* This metric has two options: [Context Adherence Basic](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna) and [Context Adherence Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus).

#### Context Relevance

*Context Relevance* measures if the context has enough information to answer the user query.

High Context Relevance values indicate strong confidence that there is enough context to answer the question. Low Context Relevance values are a sign that you need to increase your Top K, modify your retrieval strategy, or use better embeddings.

#### Completeness

If *Context Adherence* is your precision metric for RAG, *Completeness* is your recall. In other words, it tries to answer the question: "Out of all the information in the context that's pertinent to the question, how much was covered in the answer?"

Low Completeness values indicate there's relevant information to the question included in your context that was not included in the model's response.

*Note:* This metric has two options: [Completeness Basic](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-luna) and [Completeness Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus).

#### Chunk Attribution

Chunk Attribution is a chunk-level metric that denotes whether a chunk was or wasn't used by the model in generating the response. Attribution helps you more quickly identify why the model said what it did, without needing to read over the whole context.

Additionally, Attribution helps you optimize your retrieval strategy.

*Note:* This metric has two options: [Chunk Attribution Basic](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna) and [Chunk Attribution Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-plus).

#### Chunk Utilization

Chunk Utilization measures how much of the text included in your chunk was used by the model to generate a response. Chunk Utilization helps you optimize your chunking strategy.

*Note:* This metric has two options: [Chunk Utilization Basic](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna) and [Chunk Utilization Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization/chunk-utilization-plus).

#### Non-RAG specific Metrics

Other metrics such as [*Uncertainty*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/uncertainty) and [*Correctness*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/correctness) might be useful as well. If these don't cover all your needs, you can always write custom metrics.

## Iterative Experimentation

Now that you've identified something wrong with your RAG application, try to change your retriever logic, prompt template, or model settings and re-run your evaluation under the same project. Your project view will allow you to quickly compare evaluation runs and see which [configuration](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-rag-applications#keeping-track-of-what-changed-in-your-experiment) of your system worked best.
