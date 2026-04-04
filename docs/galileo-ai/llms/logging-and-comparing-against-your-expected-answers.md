# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/logging-and-comparing-against-your-expected-answers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Logging and Comparing against your Expected Answers

> Expected outputs are a key element for evaluating LLM applications. They provide benchmarks to measure model accuracy, identify errors, and ensure consistent assessments.

By comparing model responses to these predefined targets, you can pinpoint areas of improvement and track performance changes over time.

Including expected outputs in your evaluation process also aids in benchmarking your application, ensuring fair and replicable evaluations.

## Logging Expected Output

There are a few ways to create runs, and each way has a slightly different way of logging your Expected Output:

### PQ.run() or Playground UI

If you're using `pq.run()` or creating runs through the [Playground UI](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart), simply include your expected answers in a column called `output` in your evaluation set.

### Python Logger

If you're logging your runs via [EvaluateRun](https://promptquality.docs.rungalileo.io/#promptquality.EvaluateRun),
you can set the expected output using the `ground_truth` parameter in the workflow creation methods.

To log your runs with Galileo, you'd start with the same typical flow of logging into Galileo:

```py  theme={null}
import promptquality as pq

pq.login()
```

Next you can construct your [EvaluateRun](https://promptquality.docs.rungalileo.io/#promptquality.EvaluateRun) object:

```py  theme={null}
from promptquality import EvaluateRun

metrics = [pq.Scorers.context_adherence_plus, pq.Scorers.prompt_injection]

evaluate_run = EvaluateRun(run_name="my_run", project_name="my_project", scorers=metrics)
```

Now you can integrate this logging into your existing application and include the expected output in your evaluation set.

```py  theme={null}
def my_llm_app(input, ground_truth, evaluate_run):
    context = "You're a helpful AI assistant."
    template = "Given the following context answer the question. \n Context: {context} \n Question: {question}"
    # Add groundtruth to your workflow.
    wf = evaluate_run.add_workflow(input=input, ground_truth=ground_truth)
    # Get response from your llm.
    prompt = template.format(context=context, question=input)
    llm_response = llm.call(prompt) # Pseudo-code, replace with your LLM call.
    # Log llm step to Galileo
    wf.add_llm(input=prompt, output=llm_response, model=<model_name>)
    # Conclude the workflow and add the final output.
    wf.conclude(output=llm_response)
    return llm_response

# Your evaluation dataset.
eval_set = [
    {
        "input": "What are plants?",
        "ground_truth": "Plants are living organisms that typically grow in soil and have roots, stems, and leaves."
    },
    {
        "input": "What is the capital of France?",
        "ground_truth": "Paris"
    }
]
for row in eval_set:
    my_llm_app(row["input"], row["ground_truth"], evaluate_run)
```

### Langchain Callback

If you're using a Langchain Callback, add your expected output by calling `add_expected_outputs` on your callback handler.

```py  theme={null}

my_chain = ... # your langchain chain

galileo_handler = pq.GalileoPromptCallback(
    project_name="my_project", scorers=scorers,
)

inputs = ['What is 2+2?', 'Which city is the Golden Gate Bridge in?']
expected_outputs = ['4', 'San Francisco']

my_chain.batch(inputs, config=dict(callbacks=[galileo_handler]))

# Sets the expected output from each of the inputs.
galileo_handler.add_expected_outputs(expected_outputs)

galileo_handler.finish()
```

### REST Endpoint

If you're logging Evaluation runs via the [REST endpoint](/galileo/clients/log-evaluate-runs-via-rest-apis), set the *target* field in the root node of each workflow.

```py  theme={null}

...
    {
        node_id: "A_UNIQUE_ID",
        node_type: "chain",
        node_name: "Chain",
        node_input: "What is 2+2?",
        node_output: "3",
        chain_root_id: "A_UNIQUE_ID",
        step: 0,
        has_children: true,
        creation_timestamp: 0,
        expected_output: "4"
    },
...
```

<Note>Important note: Set the *expected\_output* on the root node of your workflow. Typically this will be the sole LLM node in your workflow or a "chain" node with other children nodes.</Note>

## Comparing Output and Expected Output

When Expected Output gets logged, it'll appear next to your Output wherever your output is shown.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/galileo/gen-ai-studio-products/galileo-evaluate/how-to/images/exp-output.png" alt="Comparing Output and Expected Output" />

## Metrics

When you add a ground truth, [BLEU and ROUGE-1](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/bleu-and-rouge-1) will automatically be computed and appear on the UI.
BLEU and ROUGE measure syntactical equivalence (i.e. word-by-word similarity) between your Ground Truth and actual responses.

Additionally, [Ground Truth Adherence](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/ground-truth-adherence) can be added as a metric to measure the semantic equivalence
between your Ground Truth and actual responses.
