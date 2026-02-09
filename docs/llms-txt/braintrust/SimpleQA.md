# Source: https://braintrust.dev/docs/cookbook/recipes/SimpleQA.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluating SimpleQA

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/SimpleQA/SimpleQA.ipynb) by [Ankur Goyal](https://twitter.com/ankrgyl), [Ornella Altunyan](https://twitter.com/ornelladotcom) on 2024-12-06</div>

We're going to evaluate a simple QA system in Braintrust using [SimpleQA](https://openai.com/index/introducing-simpleqa/), an open-source dataset from OpenAI. We'll also use [autoevals](https://github.com/braintrustdata/autoevals), our built-in library for evaluating AI model outputs. By the time you finish this example, you'll learn how to define and use custom evaluation metrics, compare evals that use different models, and analyze results in Braintrust.

## Setup

Before getting started, make sure you have a [Braintrust account](https://www.braintrust.dev/signup) and an API key for [OpenAI](https://platform.openai.com/). Make sure to plug the OpenAI key into your Braintrust account's [AI providers](https://www.braintrust.dev/app/settings?subroute=secrets) configuration and acquire a [BRAINTRUST\_API\_KEY](https://www.braintrust.dev/app/settings?subroute=api-keys). In this cookbook, we'll be comparing GPT-4o to Claude 3.5 Sonnet, so if you'd like to follow along, add an API key for [Anthropic](https://console.anthropic.com/) to your Braintrust account as well. Or, you can add an API key for any other AI provider you'd like and follow the same process. Lastly, add your `BRAINTRUST_API_KEY` to your Python environment, or just hardcode it into the code below.

### Install dependencies

Everything you need to run evals is readily available through Braintrust. We'll use the [AI proxy](/deploy/ai-proxy) to access multiple AI models without having to write model-specific code. Run the following command to install required libraries.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
%pip install autoevals braintrust openai requests
```

## Preparing the dataset

We'll use a QA dataset available online. If the dataset URL isn't accessible, feel free to replace it with a local CSV file.

First, we'll load in the dataset and print a confirmation statement to confirm we're ready for the next step.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import csv
import requests

csv_data = []
response = requests.get(
    "https://openaipublic.blob.core.windows.net/simple-evals/simple_qa_test_set.csv"
)
reader = csv.DictReader(response.text.splitlines())
csv_data = list(reader)
print(f"Loaded {len(csv_data)} rows from the dataset.")
```

```
Loaded 4326 rows from the dataset.
```

### Parse and transform the dataset

Next, we'll parse the raw CSV data into a Python list of dictionaries, ensuring that any metadata stored as strings is converted into usable Python objects. This transformation prepares the dataset for evaluation tasks. We'll print a few data points here as well to confirm everything looks as expected.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
parsed_data = []
for row in csv_data:
    parsed_data.append(
        {
            **row,
            "metadata": eval(row["metadata"]),  # Single quoted python values
        }
    )

parsed_data[:3]
```

```
[{'metadata': {'topic': 'Science and technology',
   'answer_type': 'Person',
   'urls': ['https://en.wikipedia.org/wiki/IEEE_Frank_Rosenblatt_Award',
    'https://ieeexplore.ieee.org/author/37271220500',
    'https://en.wikipedia.org/wiki/IEEE_Frank_Rosenblatt_Award',
    'https://www.nxtbook.com/nxtbooks/ieee/awards_2010/index.php?startid=21#/p/20']},
  'problem': 'Who received the IEEE Frank Rosenblatt Award in 2010?',
  'answer': 'Michio Sugeno'},
 {'metadata': {'topic': 'Science and technology',
   'answer_type': 'Person',
   'urls': ['https://en.wikipedia.org/wiki/The_Oceanography_Society',
    'https://en.wikipedia.org/wiki/The_Oceanography_Society',
    'https://tos.org/jerlov-medal',
    'https://www.eurekalert.org/news-releases/490504']},
  'problem': "Who was awarded the Oceanography Society's Jerlov Award in 2018?",
  'answer': 'Annick Bricaud'},
 {'metadata': {'topic': 'Geography',
   'answer_type': 'Place',
   'urls': ['https://en.wikipedia.org/wiki/Radcliffe_College',
    'https://en.wikipedia.org/wiki/Radcliffe_College',
    'https://www.braingainmag.com/7-historic-liberal-arts-colleges-in-the-us.htm',
    'https://thepeoplesarchive.dclibrary.org/repositories/2/resources/2228']},
  'problem': "What's the name of the women's liberal arts college in Cambridge, Massachusetts?",
  'answer': 'Radcliffe College'}]
```

### Format the data

Lastly, we need to format the data for Braintrust. To do this, we'll write a generator function that structures each row as a task with `input`, `expected`, and `metadata` fields.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Let's format the data for braintrust (input, expected, metadata)
def dataset():
    # Feel free to use more of (or the entire) dataset
    for row in parsed_data[:10]:
        yield {
            "input": row["problem"],
            "expected": row["answer"],
            "metadata": row["metadata"],
        }
```

## Define the model task

Now that our data is ready, we'll generate responses to the QA tasks using an LLM call. You'll notice that in this step, we use the Braintrust proxy to access GPT-4o. You can substitute any model here by setting the `MODEL` variable, as long as you have the API key for that provider configured in your Braintrust organization.

Here is the task definition:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust import wrap_openai
from openai import OpenAI
import os

BRAINTRUST_API_KEY = os.environ.get(
    "BRAINTRUST_API_KEY"
 )  # Or hardcode this to your API key

# Use the Braintrust proxy
client = OpenAI(
    base_url="https://api.braintrust.dev/v1/proxy",
    api_key=BRAINTRUST_API_KEY,
)

# The task just uses the "user" message
MODEL = "gpt-4o"


def task(input):
    return (
        client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": input}],
        )
        .choices[0]
        .message.content
    )
```

## Create a scoring function

To assess the performance of our QA system, we'll define a custom LLM-as-a-judge scoring function using the LLMClassifier from `autoevals` as a starting point. This grader will classify responses as `CORRECT`, `INCORRECT`, or `NOT_ATTEMPTED` based on predefined rules.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from autoevals import LLMClassifier

grader = LLMClassifier(
    name="Grader",
    prompt_template="""\
Your job is to look at a question, a gold target, and a predicted answer, and then assign a grade of either ["CORRECT", "INCORRECT", "NOT_ATTEMPTED"].
First, I will give examples of each grade, and then you will grade a new example.


The following are examples of CORRECT predicted answers.
'''
Question: What are the names of Barack Obama's children?
Gold target: Malia Obama and Sasha Obama
Predicted answer 1: sasha and malia obama
Predicted answer 2: most people would say Malia and Sasha, but I'm not sure and would have to double check
Predicted answer 3: Barack Obama has two daughters. Their names are Malia Ann and Natasha Marian, but they are commonly referred to as Malia Obama and Sasha Obama. Malia was born on July 4, 1998, and Sasha was born on June 10, 2001.
'''
These predicted answers are all CORRECT because:
    - They fully contain the important information in the gold target.
    - They do not contain any information that contradicts the gold target.
    - Only semantic meaning matters; capitalization, punctuation, grammar, and order don't matter.
    - Hedging and guessing are permissible, provided that the gold target is fully included and the response contains no incorrect information or contradictions.


The following are examples of INCORRECT predicted answers.
'''
Question: What are the names of Barack Obama's children?
Gold target: Malia and Sasha
Predicted answer 1: Malia.
Predicted answer 2: Malia, Sasha, and Susan.
Predicted answer 3: Barack Obama does not have any children.
Predicted answer 4: I think it's either Malia and Sasha. Or it could be Malia and Jackie. Or it could be Joey and Malia.
Predicted answer 4: While I don't know their exact names, I can tell you that Barack Obama has three children.
Predicted answer 5: It's possible you may mean Betsy and Olivia. However, you should clarify further details with updated references if necessary. Is that the correct answer?
Predicted answer 6: It may be the case that Obama's child is named James. However, it's recommended to confirm the most accurate and updated information since this could change over time. This model may not always reflect the most current information.
'''
These predicted answers are all INCORRECT because:
    - A factual statement in the answer contradicts the gold target. Incorrect statements that have some hedging (e.g., "it is possible that", "although i'm not sure, i think") are also considered incorrect.


The following are examples of NOT_ATTEMPTED predicted answers.
'''
Question: What are the names of Barack Obama's children?
Gold target: Malia and Sasha
Predicted answer 1: I don't know.
Predicted answer 2: I need more context about which Obama you are talking about.
Predicted answer 3: Without researching the web, I cannot answer this question. However, I can tell you that Barack Obama has two children.
Predicted answer 4: Barack Obama has two children. I know that one of them is Malia, but I'm not sure about the other one.
'''
These predicted answers are all NOT_ATTEMPTED because:
    - The important information in the gold target is not included in the answer.
    - No statements in the answer contradict the gold target.


Also note the following things:
- For grading questions where the gold target is a number, the predicted answer needs to be correct to the last significant figure in the gold answer. For example, consider a question "How many citations does the Transformer Paper have?" with gold target "120k".
    - Predicted answers "120k", "124k", and 115k" are all CORRECT.
    - Predicted answers "100k" and "113k" are INCORRECT.
    - Predicted answers "around 100k" and "more than 50k" are considered NOT_ATTEMPTED because they neither confirm nor contradict the gold target.
- The gold target may contain more information than the question. In such cases, the predicted answer only needs to contain the information that is in the question.
    - For example, consider the question "What episode did Derek and Meredith get legally married in Grey's Anatomy?" with gold target "Season 7, Episode 20: White Wedding". Either "Season 7, Episode 20" or "White Wedding" would be considered a CORRECT answer.
- Do not punish predicted answers if they omit information that would be clearly inferred from the question.
    - For example, consider the question "What city is OpenAI headquartered in?" and the gold target "San Francisco, California". The predicted answer "San Francisco" would be considered CORRECT, even though it does not include "California".
    - Consider the question "What award did A pretrainer's guide to training data: Measuring the effects of data age, domain coverage, quality, & toxicity win at NAACL '24?", the gold target is "Outstanding Paper Award". The predicted answer "Outstanding Paper" would be considered CORRECT, because "award" is presumed in the question.
    - For the question "What is the height of Jason Wei in meters?", the gold target is "1.73 m". The predicted answer "1.75" would be considered CORRECT, because meters is specified in the question.
    - For the question "What is the name of Barack Obama's wife?", the gold target is "Michelle Obama". The predicted answer "Michelle" would be considered CORRECT, because the last name can be presumed.
- Do not punish for typos in people's name if it's clearly the same name.
    - For example, if the gold target is "Hyung Won Chung", you can consider the following predicted answers as correct: "Hyoong Won Choong", "Hyungwon Chung", or "Hyun Won Chung".


Here is a new example. Simply reply with either CORRECT, INCORRECT, NOT ATTEMPTED. Don't apologize or correct yourself if there was a mistake; we are just trying to grade the answer.
'''
Question: {{input}}
Gold target: {{expected}}
Predicted answer: {{output}}
'''

Grade the predicted answer of this new question as one of:
A: CORRECT
B: INCORRECT
C: NOT_ATTEMPTED

Just return the letters "A", "B", or "C", with no text around it.""",
    choice_scores={"A": 1, "B": 0, "C": 0.5},
    use_cot=True,
)
```

## Run the evaluation

With the dataset, scoring function, and task defined, we're ready to run our eval:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust import EvalAsync
from dotenv import load_dotenv

load_dotenv()

results = await EvalAsync(
    "SimpleQA",
    data=dataset,
    task=task,
    scores=[grader],
    metadata={
        "model": MODEL,
    },
)
print(results)
```

## Analyze results

Braintrust will print a summary of your eval, but to analyze the full results, you'll need to visit the Braintrust dashboard by opening the printed link, or navigating to Braintrust, selecting the **SimpleQA** project, and navigating to the **Evaluations** tab.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=485a29752e4607ff81026acf8ea6f9c4" alt="Eval in UI" data-og-width="2130" width="2130" data-og-height="1626" height="1626" data-path="cookbook/assets/SimpleQA/eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=2aece87bd27516281a6b932b99e3be21 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=0fa8c925101f1a632fb779637e0d524c 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=f5ff6d071373966137fa40cebaa5b92e 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=d72f48d7792b9325fdb636c8543381a3 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=38cbad7b7f1009f0dc6542e875120204 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=9f7894f710f954d5a962e9d5aa70ca3c 2500w" />

If you look at the score distribution chart, you’ll notice that the Grader either gave a score of 100% or 0%, averaging out to 50% across the 10 datapoints.

## Comparing models

Let's swap out the model and see if we get different results. Set the `MODEL` variable to `claude-3-5-sonnet-latest` and rerun the evaluation cell above. Now when you go to Braintrust, you can directly compare the results of the experiments.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval-comparison.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=72a8ec38a102d29c6fa08d84505c71c7" alt="Eval comparison" data-og-width="3008" width="3008" data-og-height="1956" height="1956" data-path="cookbook/assets/SimpleQA/eval-comparison.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval-comparison.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=ef98bda132abdd0ba887b860e60061e5 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval-comparison.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b85d2cbc3d882014e8bffe5b3bd1b4e6 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval-comparison.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=d9d9161bee8e3535cd0df3f619f98180 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval-comparison.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=66c2a6e4700b658f5d83da594c3721ac 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval-comparison.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=e41badcb2f17cc0be49f66f5d1ec9ea7 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleQA/eval-comparison.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=9e1c33f34732d3f8534482f0053aace4 2500w" />

While the new model scored better on some of the datapoints, it regressed on others.

## Next steps

From here, there are a few different things you could do to improve the score of your QA system. You could:

* Switch out the model again and see if you get different results
* Dig into the traces in Braintrust and examine if the scoring function is working as intended
* Edit the scoring function
* Run the experiment on a larger dataset

The way we’ve set up the experiment here makes it easy to switch out the LLM and compare results across models, examine your evaluation more thoroughly in the UI, and add more data points to your evaluation dataset. Give it a try!
