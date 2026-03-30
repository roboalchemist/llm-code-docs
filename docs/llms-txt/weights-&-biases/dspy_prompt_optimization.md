# Source: https://docs.wandb.ai/weave/cookbooks/dspy_prompt_optimization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# DSPy Prompt Optimization

> Learn how to use dspy prompt optimization with W&B Weave

<Note>
  This is an interactive notebook. You can run it locally or use the links below:

  * [Open in Google Colab](https://colab.research.google.com/github/wandb/docs/blob/main/weave/cookbooks/source/dspy_prompt_optimization.ipynb)
  * [View source on GitHub](https://github.com/wandb/docs/blob/main/weave/cookbooks/source/dspy_prompt_optimization.ipynb)
</Note>

# Optimizing LLM Workflows Using DSPy and Weave

The [BIG-bench (Beyond the Imitation Game Benchmark)](https://github.com/google/BIG-bench) is a collaborative benchmark intended to probe large language models and extrapolate their future capabilities consisting of more than 200 tasks. The [BIG-Bench Hard (BBH)](https://github.com/suzgunmirac/BIG-Bench-Hard) is a suite of 23 most challenging BIG-Bench tasks that can be quite difficult to be solved using the current generation of language models.

This tutorial demonstrates how we can improve the performance of our LLM workflow implemented  on the **causal judgement task** from the BIG-bench Hard benchmark and evaluate our prompting strategies. We will use [DSPy](https://dspy.ai) for implementing our LLM workflow and optimizing our prompting strategy. We will also use [Weave](/weave) to track our LLM workflow and evaluate our prompting strategies.

## Installing the Dependencies

We need the following libraries for this tutorial:

* [DSPy](https://dspy.ai) for building the LLM workflow and optimizing it.
* [Weave](/weave) to track our LLM workflow and evaluate our prompting strategies.
* [datasets](https://huggingface.co/docs/datasets/index) to access the Big-Bench Hard dataset from HuggingFace Hub.

```python lines theme={null}
!pip install -qU dspy-ai weave datasets
```

Since we'll be using [OpenAI API](https://openai.com/index/openai-api/) as the LLM Vendor, we will also need an OpenAI API key. You can [sign up](https://platform.openai.com/signup) on the OpenAI platform to get your own API key.

```python lines theme={null}
import os
from getpass import getpass

api_key = getpass("Enter you OpenAI API key: ")
os.environ["OPENAI_API_KEY"] = api_key
```

## Enable Tracking using Weave

Weave is currently integrated with DSPy, and including [`weave.init`](/weave/reference/python-sdk/trace/weave_client#method-init) at the start of our code lets us automatically trace our DSPy functions which can be explored in the Weave UI. Check out the [Weave integration docs for DSPy](/weave/guides/integrations/dspy) to learn more.

```python lines theme={null}
import weave

weave.init(project_name="dspy-bigbench-hard")
```

In this tutorial, we use a metadata class inherited from [`weave.Object`](/weave/reference/python-sdk#class-object) to manage our metadata.

```python lines theme={null}
class Metadata(weave.Object):
    dataset_address: str = "maveriq/bigbenchhard"
    big_bench_hard_task: str = "causal_judgement"
    num_train_examples: int = 50
    openai_model: str = "gpt-3.5-turbo"
    openai_max_tokens: int = 2048
    max_bootstrapped_demos: int = 8
    max_labeled_demos: int = 8

metadata = Metadata()
```

<Tip>
  **Object Versioning**: The `Metadata` objects are automatically versioned and traced when functions consuming them are traced
</Tip>

## Load the BIG-Bench Hard Dataset

We will load this dataset from HuggingFace Hub, split into training and validation sets, and [publish](/weave/guides/core-types/datasets) them on Weave, this will let us version the datasets, and also use [`weave.Evaluation`](/weave/guides/core-types/evaluations) to evaluate our prompting strategy.

```python lines theme={null}
import dspy
from datasets import load_dataset

@weave.op()
def get_dataset(metadata: Metadata):
    # load the BIG-Bench Hard dataset corresponding to the task from Huggingface Hug
    dataset = load_dataset(metadata.dataset_address, metadata.big_bench_hard_task)[
        "train"
    ]

    # create the training and validation datasets
    rows = [{"question": data["input"], "answer": data["target"]} for data in dataset]
    train_rows = rows[0 : metadata.num_train_examples]
    val_rows = rows[metadata.num_train_examples :]

    # create the training and validation examples consisting of `dspy.Example` objects
    dspy_train_examples = [
        dspy.Example(row).with_inputs("question") for row in train_rows
    ]
    dspy_val_examples = [dspy.Example(row).with_inputs("question") for row in val_rows]

    # publish the datasets to the Weave, this would let us version the data and use for evaluation
    weave.publish(
        weave.Dataset(
            name=f"bigbenchhard_{metadata.big_bench_hard_task}_train", rows=train_rows
        )
    )
    weave.publish(
        weave.Dataset(
            name=f"bigbenchhard_{metadata.big_bench_hard_task}_val", rows=val_rows
        )
    )

    return dspy_train_examples, dspy_val_examples

dspy_train_examples, dspy_val_examples = get_dataset(metadata)
```

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/aRvhhwVWqlxBzke5/media/dspy_optimization/1.png?fit=max&auto=format&n=aRvhhwVWqlxBzke5&q=85&s=d082875b9287c19fe59961b983bfffdc" alt="DSPy dataset loading interface with dataset preparation steps and data structure" width="3024" height="1188" data-path="media/dspy_optimization/1.png" />
</Frame>

## The DSPy Program

[DSPy](https://dspy.ai) is a framework that pushes building new LM pipelines away from manipulating free-form strings and closer to programming (composing modular operators to build text transformation graphs) where a compiler automatically generates optimized LM invocation strategies and prompts from a program.

We will use the [`dspy.OpenAI`](https://dspy.ai/learn/programming/language_models/#__tabbed_1_1) abstraction to make LLM calls to [GPT3.5 Turbo](https://platform.openai.com/docs/models/gpt-3.5-turbo).

```python lines theme={null}
system_prompt = """
You are an expert in the field of causal reasoning. You are to analyze the a given question carefully and answer in `Yes` or `No`.
You should also provide a detailed explanation justifying your answer.
"""

llm = dspy.OpenAI(model="gpt-3.5-turbo", system_prompt=system_prompt)
dspy.settings.configure(lm=llm)
```

### Writing the causal reasoning signature

A [signature](https://dspy.ai/learn/programming/signatures) is a declarative specification of input/output behavior of a [DSPy module](https://dspy.ai/learn/programming/modules) which are task-adaptive components—akin to neural network layers—that abstract any particular text transformation.

```python lines theme={null}
from pydantic import BaseModel, Field

class Input(BaseModel):
    query: str = Field(description="The question to be answered")

class Output(BaseModel):
    answer: str = Field(description="The answer for the question")
    confidence: float = Field(
        ge=0, le=1, description="The confidence score for the answer"
    )
    explanation: str = Field(description="The explanation for the answer")

class QuestionAnswerSignature(dspy.Signature):
    input: Input = dspy.InputField()
    output: Output = dspy.OutputField()

class CausalReasoningModule(dspy.Module):
    def __init__(self):
        self.prog = dspy.TypedPredictor(QuestionAnswerSignature)

    @weave.op()
    def forward(self, question) -> dict:
        return self.prog(input=Input(query=question)).output.dict()
```

Let's test our LLM workflow, i.e., the `CausalReasoningModule` on an example from the causal reasoning subset of Big-Bench Hard.

```python lines theme={null}
import rich

baseline_module = CausalReasoningModule()

prediction = baseline_module(dspy_train_examples[0]["question"])
rich.print(prediction)
```

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/aRvhhwVWqlxBzke5/media/dspy_optimization/2.png?fit=max&auto=format&n=aRvhhwVWqlxBzke5&q=85&s=85e97c14054851da3d86399d4c53ae10" alt="Baseline DSPy program evaluation results with performance metrics and output examples" width="3018" height="1894" data-path="media/dspy_optimization/2.png" />

  ## Evaluating our DSPy Program
</Frame>

Now that we have a baseline prompting strategy, let's evaluate it on our validation set using [`weave.Evaluation`](/weave/guides/core-types/evaluations) on a simple metric that matches the predicted answer with the ground truth. Weave will take each example, pass it through your application and score the output on multiple custom scoring functions. By doing this, you'll have a view of the performance of your application, and a rich UI to drill into individual outputs and scores.

First, we need to create a simple weave evaluation scoring function that tells whether the answer from the baseline module's output is the same as the ground truth answer or not. Scoring functions need to have a `model_output` keyword argument, but the other arguments are user defined and are taken from the dataset examples. It will only take the necessary keys by using a dictionary key based on the argument name.

```python lines theme={null}
@weave.op()
def weave_evaluation_scorer(answer: str, output: Output) -> dict:
    return {"match": int(answer.lower() == output["answer"].lower())}
```

Next, we can simply define the evaluation and run it.

```python lines theme={null}
validation_dataset = weave.ref(
    f"bigbenchhard_{metadata.big_bench_hard_task}_val:v0"
).get()

evaluation = weave.Evaluation(
    name="baseline_causal_reasoning_module",
    dataset=validation_dataset,
    scorers=[weave_evaluation_scorer],
)

await evaluation.evaluate(baseline_module.forward)
```

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/aRvhhwVWqlxBzke5/media/dspy_optimization/3.png?fit=max&auto=format&n=aRvhhwVWqlxBzke5&q=85&s=8f514d3eeaa439ccb874f8a02f16f6a6" alt="Weave evaluation dashboard with DSPy program performance metrics, traces, and comparison results" width="3024" height="1892" data-path="media/dspy_optimization/3.png" />
</Frame>

<Note>
  If you're running from a python script, you can use the following code to run the evaluation:

  ```python lines theme={null}
  import asyncio
  asyncio.run(evaluation.evaluate(baseline_module.forward))
  ```
</Note>

<Warning>
  Running the evaluation causal reasoning dataset will cost approximately \$0.24 in OpenAI credits.
</Warning>

## Optimizing our DSPy Program

Now, that we have a baseline DSPy program, let us try to improve its performance for causal reasoning using the [BootstrapFewShot](https://dspy.ai/api/optimizers/BootstrapFewShot/) teleprompter, which can tune the parameters of a DSPy program to maximize the specified metrics.

```python lines theme={null}
from dspy.teleprompt import BootstrapFewShot

@weave.op()
def get_optimized_program(model: dspy.Module, metadata: Metadata) -> dspy.Module:
    @weave.op()
    def dspy_evaluation_metric(true, prediction, trace=None):
        return prediction["answer"].lower() == true.answer.lower()

    teleprompter = BootstrapFewShot(
        metric=dspy_evaluation_metric,
        max_bootstrapped_demos=metadata.max_bootstrapped_demos,
        max_labeled_demos=metadata.max_labeled_demos,
    )
    return teleprompter.compile(model, trainset=dspy_train_examples)

optimized_module = get_optimized_program(baseline_module, metadata)
```

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/aRvhhwVWqlxBzke5/media/dspy_optimization/4.png?fit=max&auto=format&n=aRvhhwVWqlxBzke5&q=85&s=97b6324c43e6a1ed6bb7e54b71c0a94a" alt="DSPy program optimization process interface with teleprompter configuration and optimization progress" width="3024" height="1896" data-path="media/dspy_optimization/4.png" />
</Frame>

<Warning>
  Running the evaluation causal reasoning dataset will cost approximately \$0.04 in OpenAI credits.
</Warning>

Now that we have our optimized program (the optimized prompting strategy), let's evaluate it once again on our validation set and compare it with our baseline DSPy program.

```python lines theme={null}
evaluation = weave.Evaluation(
    name="optimized_causal_reasoning_module",
    dataset=validation_dataset,
    scorers=[weave_evaluation_scorer],
)

await evaluation.evaluate(optimized_module.forward)
```

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/aRvhhwVWqlxBzke5/media/dspy_optimization/5.png?fit=max&auto=format&n=aRvhhwVWqlxBzke5&q=85&s=fc3d2aeb7dc78ba8a2f9bcc626cf9906" alt="Optimized DSPy program evaluation results with improved performance metrics and output quality" width="3024" height="1892" data-path="media/dspy_optimization/5.png" />
</Frame>

When coomparing the evalution of the baseline program with the optimized one shows that the optimized program answers the causal reasoning questions with siginificantly more accuracy.

## Conclusion

In this tutorial, we learned how to use DSPy for prompt optimization alongside using Weave for tracking and evaluation to compare the original and optimized programs.
