# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/log-pre-generated-responses-in-python.md

# Log Pre-generated Responses in Python

> If you already have a dataset of requests and application responses, and you want to log and evaluate these on Galileo without re-generating the responses, you can do so via our worflows.

First, log in to Galileo:

```py
import promptquality as pq

pq.login()
```

Now you can take your previously generated data and log it to Galileo.

```py
from promptquality import EvaluateRun

metrics = [pq.Scorers.context_adherence_plus, pq.Scorers.prompt_injection]

evaluate_run = EvaluateRun(run_name="my_run", project_name="my_project", scorers=metrics)
```

```py
# Your previously generated requests & responses
data = [
    {
        'request': 'What\'s the capital of United States?',
        'response': 'Washington D.C.',
        'context': 'Washington D.C. is the capital of United States'
    },
    {
        'request': 'What\'s the capital of France?',
        'response': 'Paris',
        'context': 'Paris is the capital of France'
    }
]

metrics = [pq.Scorers.context_adherence_plus, pq.Scorers.prompt_injection]

evaluate_run = EvaluateRun(run_name="my_run", project_name="my_project", scorers=metrics)

for row in data:
    template = "Given the following context answer the question. \n Context: {context} \n Question: {question}"
    wf = evaluate_run.add_workflow(input=row["request"], output=row["response"])
    wf.add_llm(
        input=template.format(context=row['context'], question=row["request"]),
        output=row["response"],
        model=pq.Models.chat_gpt,
    )
```

Finally, log your Evaluate run to Galileo:

```py
evaluate_run.finish()
```

Once complete, this step will display the link to access the run from your Galileo Console.

## Logging as a RAG workflow

To log the above dataset as a RAG workflow, you can modify the code snippet as follows:

```py
for row in data:
    template = "Given the following context answer the question. \n Context: {context} \n Question: {question}"
    wf = evaluate_run.add_workflow(input=row["request"], output=row["response"])
    # Add the retriever step with the context retrieved.
    wf.add_retriever(
        input=row["request"],
        documents=[row['context']],
    )
    wf.add_llm(
        input=template.format(context=row['context'], question=row["request"]),
        output=row["response"],
        model=pq.Models.chat_gpt,
    )
```
