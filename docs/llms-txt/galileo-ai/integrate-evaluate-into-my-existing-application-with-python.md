# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/quickstart/integrate-evaluate-into-my-existing-application-with-python.md

# Integrate Evaluate Into My Existing Application With Python

> Learn how to integrate Galileo Evaluate into your Python applications, featuring step-by-step guidance and code samples for streamlined integration.

If you already have a prototype or an application you're looking to run experiments and evaluations over, Galileo Evaluate allows you to hook into it and log the inputs, outputs, and any intermediate steps to Galileo for further analysis.

In this QuickStart, we'll show you how to:

* Integrate with your workflows

* Integrate with your Langchain apps

Let's dive in!

### Logging Workflows

If you're looking to log your workflows, we provide an interface for uploading your executions.

<Tabs>
  <Tab title="Python">
    ```py
    import promptquality as pq

    pq.login()
    ```

    ```py
    from promptquality import EvaluateRun

    metrics = [pq.Scorers.context_adherence_plus, pq.Scorers.prompt_injection]

    evaluate_run = EvaluateRun(run_name="my_run", project_name="my_project", scorers=metrics)
    ```

    ```py
    # Define your inputs.
    eval_set = [
        "What are hallucinations?",
        "What are intrinsic hallucinations?",
        "What are extrinsic hallucinations?"
    ]
    # Define your run.
    evaluate_run = EvaluateRun(run_name="my_run", project_name="my_project", scorers=metrics)
    # Run the evaluation set on your app and log the results.
    for input in eval_set:
        output = llm.call(input) # Pseudo-code, replace with your LLM call.
        evaluate_run.add_single_step_workflow(input=input, output=output, model=<my_model_name>)
    ```

    Finally, log your Evaluate run to Galileo:

    ```py
    evaluate_run.finish()
    ```

    Please check out this page [here](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/custom-chain) for more information on logging experiments with our Python logger.
  </Tab>

  <Tab title="TypeScript">
    1. Initialize client and create or select your project

    ```TypeScript
    import { GalileoEvaluateWorkflow } from "@rungalileo/galileo";

    // Initialize and create project
    const evaluateWorkflow = new GalileoEvaluateWorkflow("Evaluate Project"); // Project Name
    await evaluateWorkflow.init();
    ```

    2. Log your workflows

    ```TypeScript
    // Evaluate dataset
    const evaluateSet = [
      "What are hallucinations?",
      "What are intrinsic hallucinations?",
      "What are extrinsic hallucinations?"
    ]

    // Add workflows
    const myLlmApp = (input) => {
        const template = "Given the following context answer the question. \n Context: {context} \n Question: {question}"

        // Add workflow
        evaluateWorkflow.addWorkflow({ input });

        // Get context from Retriever
        // Pseudo-code, replace with your Retriever call
        const retrieverCall = () => 'You're an AI assistant helping a user with hallucinations.';
        const context = retrieverCall()

        // Log Retriever Step
        evaluateWorkflow.addRetrieverStep({
            input: template,
            output: context
        })

        // Get response from your LLM
        // Pseudo-code, replace with your LLM call
        const prompt = template.replace('{context}', context).replace('{question}', input)
        const llmCall = (_prompt) => 'An LLM response…';
        const llmResponse = llmCall(prompt);

        // Log LLM step
        evaluateWorkflow.addLlmStep({
            durationNs: parseInt((Math.random() * 3) * 1000000000),
            input: prompt,
            output: llmResponse,
        })

        // Conclude workflow
        evaluateWorkflow.concludeWorkflow(llmResponse);
    }

    evaluateSet.forEach((input) => myLlmApp(input));
    ```

    3. Log your Evaluate run to Galileo

    ```TypeScript
    // Configure run and upload workflows to Galileo
    // Optional: Set run name, tags, registered scorers, and customized scorers
    // Note: If no run name is provided a timestamp will be used
    await evaluateWorkflow.uploadWorkflows(
        {
            adherence_nli: true,
            chunk_attribution_utilization_nli: true,
            completeness_nli: true,
            context_relevance: true,
            factuality: true,
            instruction_adherence: true,
            ground_truth_adherence: true,
            pii: true,
            prompt_injection: true,
            prompt_perplexity: true,
            sexist: true,
            tone: true,
            toxicity: true,
        }
    );
    ```
  </Tab>
</Tabs>

### Langchain

Galileo supports the logging of chains from `langchain`. To log these chains, we require using the callback from our Python client [`promptquality`](https://docs.rungalileo.io/galileo/python-clients/index).

Before creating a run, you'll want to make sure you have an evaluation set (a set of questions / sample inputs you want to run through your prototype for evaluation). Your evaluation set should be consistent across runs.

First, we are going to construct a simple RAG chain with Galileo's documentations stored in a vectorDB using Langchain:

```py
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.document import Document

# Load text from webpage
loader = WebBaseLoader("https://www.rungalileo.io/blog/deep-dive-into-llm-hallucinations-across-generative-tasks")
data = loader.load()

# Split text into documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(data)

# Add text to vector db
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=splits, embedding=embedding)

# Create a retriever
retriever = vectordb.as_retriever()

def format_docs(docs: List[Document]) -> str:
    return "\n\n".join([d.page_content for d in docs])

template = """Answer the question based only on the following context:

    {context}

    Question: {question}
    """
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI()

chain = {"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | model | StrOutputParser()
```

Next, you can log in with Galileo:

```py
import promptquality as pq
pq.login({YOUR_GALILEO_URL})
```

After that, you can set up the `GalileoPromptCallback`:

```py
from promptquality import Scorers
scorers = [Scorers.context_adherence_basic,
           Scorers.completeness_basic,
           Scorers.pii,
           ...]
#This is the list of metrics you want to evaluate your run over.

galileo_handler = pq.GalileoPromptCallback(
    project_name="quickstart_project", scorers=scorers,
)
#Each "run" will appear under this project. Choose a name that'll help you identify what you're evaluating
```

Finally, you can run the chain experiments across multiple intputs with Galileo Callback:

```py
inputs = [
    "What are hallucinations?",
    "What are intrinsic hallucinations?",
    "What are extrinsic hallucinations?"
]
chain.batch(inputs, config=dict(callbacks=[galileo_handler]))

# publish the results of your run
galileo_handler.finish()
```

<Info>For more detailed information on Galileo's Langchain integration, check out instructions [here](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/langchain).</Info>
