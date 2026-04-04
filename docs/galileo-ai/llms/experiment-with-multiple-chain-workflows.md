# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/experiment-with-multiple-chain-workflows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Experiment with Multiple Workflows

> If you're building a multi-step workflow or chain (e.g. a RAG system, an Agent, or a chain) and want to experiment with multiple combinations of parameters or your versions at once, Chain Sweeps are your friend.

A Chain Sweep allows you to execute, in bulk, multiple chains or workflows iterating over different versions or parameters of your system.

First, you'll need to wrap your workflow or chain in a function. This function should take anything you want to experiment with as an argument (e.g. chunk size, embedding model, top\_k).

Here we create a function `rag_chain_executor` utilizing our workflow logging integration.

```py  theme={null}
import promptquality as pq
from promptquality import EvaluateRun

# Login to Galileo.
pq.login(console_url=os.environ["GALILEO_CONSOLE_URL"])

def rag_chain_executor(chunk_size: int, chunk_overlap: int, model_name: str) -> None:
    # Formulate your input data.
    questions = [...] # Pseudo-code, replace with your evaluation set.

    # Create an evaluate run.
    evaluate_run = EvaluateRun(
        scorers=[Scorers.sexist, Scorers.pii, Scorers.toxicity],
        project_name="<my_project_name>",
    )

    # Log a workflow for each question in your evaluation set.
    for question in questions:
        template = "Given the following context answer the question. \n Context: {context} \n Question: {question}"
        wf = evaluate_run.add_workflow(input=question)
        # Fetch documents from your retriever
        documents = retriever.retrieve(question, chunk_size, chunk_overlap) # Pseudo-code, replace with your evaluation set.
        # Log retriever step to Galileo
        wf.add_retriever(input=question, documents=documents)
        # Get response from your llm.
        prompt = template.format(context="\n".join(documents), question=question)
        llm_response = llm(model_name).call(prompt) # Pseudo-code, replace with your evaluation set.
        # Log llm step to Galileo
        wf.add_llm(input=prompt, output=llm_response, model=model_name)
        # Conclude the workflow and add the final output.
        wf.conclude(output=llm_response)
    evaluate_run.finish()
    return llm_response
```

Alertnatively we can create the function `rag_chain_executor` utilizing a LangChain integration.

```py  theme={null}

import promptquality as pq

# Login to Galileo.
pq.login(console_url=os.environ["GALILEO_CONSOLE_URL"])


from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

documents = [Document(page_content=doc) for doc in source_documents]
questions = [...]

def rag_chain_executor(chunk_size: int, chunk_overlap: int, model_name: str) -> None:
    # Example of a RAG chain that uses the params in the function signature
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(openai_api_key="<OPENAI_API_KEY>")
    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()
    model = ChatOpenAI(openai_api_key="<OPENAI_API_KEY>", model_name=model_name)
    qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)

    # Before running your chain, add the Galileo Prompt Callback on the invoke/run/batch step
    prompt_handler = pq.GalileoPromptCallback(
        scorers=[Scorers.sexist, Scorers.pii, Scorers.toxicity],
        project_name="<my_project_name>",
    )
    for question in questions:
        result = qa.invoke(
            {"question": question, "chat_history": []},
            config=dict(callbacks=[prompt_handler]),
        )
    # Call .finish() on your callback to upload your results to Galileo
    prompt_handler.finish()
```

Finally, call pq.sweep() with your chain's wrapper function and a dict containing all the different params you'd like to run your chain over:

```py  theme={null}

pq.sweep(
    rag_chain_executor,
    {
        "chunk_size": [50, 100, 200],
        "chunk_overlap": [0, 25, 50],
        "model_name": ["gpt-3.5-turbo", "gpt-3.5-turbo-instruct", "gpt-4-0125-preview"],
    },
)
```

See the [PromptQuality Python Library Docs](https://promptquality.docs.rungalileo.io/#promptquality.sweep) for the function docstrings.
