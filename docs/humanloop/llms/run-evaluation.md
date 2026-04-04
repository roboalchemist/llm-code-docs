# Source: https://humanloop.com/docs/sdk/run-evaluation.md

# Run Evaluation

> Getting up and running with Humanloop is quick and easy. This guide will explain how to set up evaluations on Humanloop and use them to iteratively improve your applications.


The `evaluations.run()` function is a convenience function that allows you to trigger evaluations from code. It will create the evaluation, fetch the dataset, generate all the Logs and then run the evaluators on each log.

It supports evaluating arbitrary functions, Prompts stored on Humanloop, and Prompts defined in code.

## Parameters

You can see the source code for the `evaluations.run()` function in [Python](https://github.com/humanloop/humanloop-python/blob/master/src/humanloop/evals/run.py#L106) and [TypeScript](https://github.com/humanloop/humanloop-node/blob/master/src/evals/run.ts#L211).

<ParamField path="name" type="string" required={true}>
Name of the evaluation to help identify it
</ParamField>

<ParamField path="file" type="object" required={true}>
Configuration for what is being evaluated. The evaluation will be stored on this File.

<Accordion title='file'>
<ParamField path="path" type="string" required={true}>
Path to the evaluated File (a [Prompt](/docs/explanation/prompts), [Flow](/docs/explanation/flows), [Tool](/docs/explanation/tools), [Evaluator](/docs/explanation/evaluators) etc.) on Humanloop. If the File does not exist on Humanloop, it will be created.

Example: `My Agent` will create a `flow` file on Humanloop.
</ParamField>

<ParamField path="type" type="enum">
`flow` (default), `prompt`, `tool`, `evaluator`

If the File does not exist on Humanloop, it will be created with this File type.
</ParamField>

<ParamField path="version" type="object">
Pass in the details of the version of the File you want to evaluate.

For example, for a Flow you might pass in identifiers:

```json
{
  "git_hash": "1234567890",
  "identifier": "rag-with-pinecone"
}
```

Or for a Prompt you can pass in Prompt details and it will be called.

```json
{
  "model": "gpt-4",
  "template": [
    {
      "role": "user",
      "content": "You are a helpful assistant on the topic of {{topic}}."
    }
  ]
}
```

</ParamField>

<ParamField path="callable" type="function">
Function to evaluate (optional if the File is runnable on Humanloop like a Prompt).
It will be called using your Dataset `callable(**datapoint.inputs, messages=datapoint.messages)`. It should return a single string output.
</ParamField>

</Accordion>
</ParamField>

<ParamField path="evaluators" type="array" required={true}>
List of evaluators to judge the generated output
<Accordion title='evaluator'>

<ParamField path="path" type="string" required={true}>
Path to evaluator on Humanloop
</ParamField>
<ParamField path="args_type" type="string">
The type of arguments the Evaluator expects - only required for local Evaluators
</ParamField>
<ParamField path="return_type" type="string">
The type of return value the Evaluator produces - only required for local Evaluators
</ParamField>
<ParamField path="callable" type="function">
Function to evaluate (optional if the Evaluator is runnable on Humanloop).
It will be called using the generated output as follows: `callable(output)`.
It should return a single string output.
</ParamField>
<ParamField path="custom_logger" type="function">
Optional function that logs the output judgment from your Evaluator to Humanloop. If provided, it will be called as:
`judgment = callable(log_dict); log = custom_logger(client, judgment)`. Inside the custom_logger, you can use the Humanloop `client` to log the judgment to Humanloop.
If not provided your function must return a single string and by default the code will be used to inform the version of the external Evaluator on Humanloop.
</ParamField>
<ParamField path="threshold" type="number">
The threshold to check the evaluator result against
</ParamField>

</Accordion>
</ParamField>
<ParamField path="dataset" type="object" required={true}>
Dataset to evaluate against
<Accordion title='dataset'>
<ParamField path="path" type="string" required={true}>
Path to existing dataset on Humanloop. If the Dataset does not exist on Humanloop, it will be created.
</ParamField>
<ParamField path="datapoints" type="array">
The datapoints to map your function over to produce the outputs required by the evaluation. Optional - if not provided, the evaluation will be run over the datapoints stored on Humanloop.
</ParamField>
</Accordion>
</ParamField>

## Return Type

Returns an `EvaluationStats` object containing:

- run_stats: Array of statistics for each run
- progress: Summary of evaluation progress
- report: Detailed evaluation report
- status: Current status of evaluation

# Examples

## 1. Evaluating an Arbitrary Flow Function

To evaluate an arbitrary workflow you can pass in the `callable` parameter to the `file` object.

<CodeBlocks>

```python
def my_flow_function(messages):
    # Your custom logic here
    return "Response based on messages"

evaluation = humanloop.evaluations.run(
    name="Custom Flow Evaluation",
    type="flow",
    file={
        "path": "Custom/Flow",
        "callable": my_flow_function
    },
    evaluators=[
        {"path": "Example Evaluators/AI/Semantic similarity"},
        {"path": "Example Evaluators/Code/Latency"}
    ],
    dataset={
        "path": "Test/Dataset",
        "datapoints": [
            {
                "messages": [
                    {"role": "user", "content": "Test question 1"}
                ]
            }
        ]
    }
)
```

```typescript
const myFlowFunction = (messages: Message[]): string => {
  // Your custom logic here
  return "Response based on messages";
};

const evaluation = await humanloop.evaluations.run({
  name: "Custom Flow Evaluation",
  file: {
    path: "Custom/Flow",
    type: "flow",
    callable: myFlowFunction,
  },
  evaluators: [
    { path: "Example Evaluators/AI/Semantic similarity" },
    { path: "Example Evaluators/Code/Latency" },
  ],
  dataset: {
    path: "Test/Dataset",
    datapoints: [
      {
        messages: [{ role: "user", content: "Test question 1" }],
      },
    ],
  },
});
```

</CodeBlocks>

## 2. Evaluating a Prompt on Humanloop

To evaluate a Prompt stored on Humanloop you simply supply a `path` to the Prompt and a list of Evaluators.
<CodeBlocks>

```python
evaluation = humanloop.evaluations.run(
    name="Existing Prompt Evaluation",
    file={
        "path": "Existing/Prompt",
    },
    evaluators=[
        {"path": "Example Evaluators/AI/Semantic similarity"},
        {"path": "Example Evaluators/Code/Cost"}
    ],
    dataset={
        "path": "Existing/Dataset"
    }
)
```

```typescript
const evaluation = await humanloop.evaluations.run({
  name: "Existing Prompt Evaluation",
  file: {
    path: "Existing/Prompt",
  },
  evaluators: [
    { path: "Example Evaluators/AI/Semantic similarity" },
    { path: "Example Evaluators/Code/Cost" },
  ],
  dataset: {
    path: "Existing/Dataset",
  },
});
```

</CodeBlocks>

## 3. Evaluating a Prompt in Code

To evaluate a Prompt defined in code you can pass in the `model`, `template` and other Prompt parameters to the `file`'s `version` object.

<CodeBlocks>

```python
evaluation = humanloop.evaluations.run(
    name="Code Prompt Evaluation",
    file={
        "path": "Code/Prompt",
        "version": {
            "model": "gpt-4",
            "template": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant on the topic of {{topic}}."
                }
            ]
        },
    },
    evaluators=[
        {"path": "Example Evaluators/AI/Semantic similarity"},
        {"path": "Example Evaluators/Code/Latency"}
    ],
    dataset={
        "datapoints": [
            {
                "inputs": { "topic": "machine learning" },
                "messages": [ {"role": "user", "content": "What is machine learning?"} ],
                "target": { "output": "Machine learning is a subset of artificial intelligence..." }
            }
        ]
    }
)
```

```typescript
const evaluation = await humanloop.evaluations.run({
  name: "Code Prompt Evaluation",
  file: {
    path: "Code/Prompt",
    model: "gpt-4",
    template: [
      {
        role: "system",
        content: "You are a helpful assistant on the topic of {{topic}}.",
      },
    ],
  },
  evaluators: [
    { path: "Example Evaluators/AI/Semantic similarity" },
    { path: "Example Evaluators/Code/Latency" },
  ],
  dataset: {
    datapoints: [
      {
        inputs: { topic: "machine learning" },
        messages: [{ role: "user", content: "What is machine learning?" }],
        target: {
          output: "Machine learning is a subset of artificial intelligence...",
        },
      },
    ],
  },
});
```

</CodeBlocks>

Each example demonstrates a different way to use the `evaluation.run` function. The function returns evaluation statistics that can be used to understand the performance of your LLM application according to the specified evaluators.

You can view the results of your evaluation in the Humanloop UI by navigating to the specified file path, or by checking the evaluation stats programmatically using the returned object's `report` field.
