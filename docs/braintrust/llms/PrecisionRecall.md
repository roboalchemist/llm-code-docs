# Source: https://braintrust.dev/docs/cookbook/recipes/PrecisionRecall.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluating the precision and recall of an emotion classifier

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/PrecisionRecall/PrecisionRecall.ipynb) by [Adrian Barbir](https://www.linkedin.com/in/adrianbarbir/) on 2025-01-17</div>

In this cookbook, we'll explore how to evaluate an LLM classifier in Braintrust using custom scoring functions that measure precision and recall. We'll use the [GoEmotions dataset](https://huggingface.co/datasets/google-research-datasets/go_emotions), which contains Reddit comments labeled with 28 different emotions. This dataset is interesting since each comment can be labeled with multiple emotions; for example, a single message might express both "excitement" and "anger."

We'll build two classifiers-a random baseline and an LLM-based approach using OpenAI's GPT-4o. By comparing their performance using custom scorers, we'll demonstrate how to effectively measure and then improve your LLM's accuracy on complex classification tasks.

## Getting started

To get started, you'll need [Braintrust](https://www.braintrust.dev/signup) and [OpenAI](https://platform.openai.com/) accounts, along with their corresponding API keys. Add your `BRAINTRUST_API_KEY` and `OPENAI_API_KEY` to your environment:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export BRAINTRUST_API_KEY="YOUR_BRAINTRUST_API_KEY"
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

<Callout type="info">
  Best practice is to export your API key as an environment variable. However, to make it easier to follow along with this cookbook, you can also hardcode it into the code below.
</Callout>

Let's start by installing the required Python dependencies:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust openai datasets autoevals pydantic
```

Next, we'll import all of the modules we need and initialize our OpenAI client. We're wrapping the client so that we have access to Braintrust features.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os
import random
from typing import List, Literal, Union, Set

import autoevals
from datasets import load_dataset
import braintrust
import openai
from pydantic import BaseModel, Field, create_model

# Uncomment if you want to hardcode your API keys
# os.environ["BRAINTRUST_API_KEY"] = "YOUR_BRAINTRUST_API_KEY"
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

openai_client = braintrust.wrap_openai(openai.OpenAI())
```

## Type definitions and data models

To ensure that the LLM classifier outputs only emotions predefined by the dataset, we'll leverage OpenAI's structured outputs feature by providing a Pydantic `DynamicModel` representing the classification output.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
EMOTIONS = [
    "admiration",
    "amusement",
    "anger",
    "annoyance",
    "approval",
    "caring",
    "confusion",
    "curiosity",
    "desire",
    "disappointment",
    "disapproval",
    "disgust",
    "embarrassment",
    "excitement",
    "fear",
    "gratitude",
    "grief",
    "joy",
    "love",
    "nervousness",
    "optimism",
    "pride",
    "realization",
    "relief",
    "remorse",
    "sadness",
    "surprise",
    "neutral",
]

EmotionType = Literal[tuple(EMOTIONS)]

EmotionClassification = create_model(
    "EmotionClassification", emotions=(List[EmotionType], ...)
)


def load_data(limit: int = 100):
    ds = load_dataset("google-research-datasets/go_emotions", "raw")
    for i, item in list(enumerate(ds["train"]))[:limit]:
        actual_emotions = [emotion for emotion in EMOTIONS if item.get(emotion, 0) == 1]
        yield {
            "input": item["text"],
            "expected": actual_emotions,
            "metadata": {"subreddit": item["subreddit"], "author": item["author"]},
        }
```

## Creating the classifiers

We'll implement two different approaches to emotion classification:

1. A random classifier that assigns 1-3 emotions randomly from our predefined list. This random baseline helps us verify that our LLM classifier performs meaningfully better than chance predictions.

2. An LLM-based classifier using GPT-4o that uses [structured outputs](https://platform.openai.com/docs/guides/structured-outputs) to ensure valid emotion labels.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def llm_classifier(text: str) -> EmotionClassification:
    prompt = (
        f"Analyze the emotional content in this text and STRICTLY classify it using ONLY the following emotion labels:\n"
        f"{', '.join(EMOTIONS)}\n\n"
        f"IMPORTANT: You must ONLY use emotions from the above list. Do not use any other emotion labels and DO NOT repeat emotions.\n\n"
        f"Text: {text}\n\n"
        f"Respond with a JSON object containing:\n"
        f"- emotions: array of emotions from the provided list only\n"
        f"Remember: Only use emotions from the provided list. If you see an emotion that isn't in the list, map it to the closest matching emotion from the list."
    )

    response = openai_client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format=EmotionClassification,
    )

    result = response.choices[0].message.content
    return EmotionClassification.model_validate_json(result)


def random_classifier(text: str) -> EmotionClassification:
    num_emotions = random.randint(1, 3)
    selected_emotions = random.sample(EMOTIONS, num_emotions)
    return EmotionClassification(
        emotions=selected_emotions,
        confidence=random.random(),
        rationale="Random selection",
    )
```

## Implementing evaluation metrics

Because each comment can express multiple emotions, we're going to use three metrics to assess the performance of our LLM classifier:

`Precision` measures prediction accuracy by calculating the fraction of true positive predictions out of all positive predictions, expressed as (true positives)/(true positives + false positives). If we predict "joy" and "anger" for a comment that only expresses "joy," we have one true positive and one false positive, so the precision is 0.5. Higher precision means fewer false positives.

`Recall` measures the fraction of actual emotions that were correctly identified, expressed as (true positives)/(true positives + false negatives). If a comment expresses "sadness" and "fear," but we only catch "sadness," we have one true positive and one false negative, so the recall is 0.5. Higher recall means fewer missed emotions.

`F1 Score` combines precision and recall into a single metric since improving one can hurt the other. It helps balance being too strict (high precision, low recall) and too lenient (high recall, low precision).

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def emotion_precision(
    output: EmotionClassification, expected: List[EmotionType]
) -> float:
    expected_set = set(expected)
    output_set = set(output.emotions)
    true_positives = len(output_set & expected_set)
    false_positives = len(output_set - expected_set)
    return (
        true_positives / (true_positives + false_positives)
        if (true_positives + false_positives) > 0
        else 1.0
    )


def emotion_recall(output: EmotionClassification, expected: List[EmotionType]) -> float:
    expected_set = set(expected)
    output_set = set(output.emotions)
    true_positives = len(output_set & expected_set)
    false_negatives = len(expected_set - output_set)
    return (
        true_positives / (true_positives + false_negatives)
        if (true_positives + false_negatives) > 0
        else 1.0
    )


def emotion_f1(output: EmotionClassification, expected: List[EmotionType]) -> float:
    prec = emotion_precision(output, expected)
    rec = emotion_recall(output, expected)
    return 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0
```

## Running evaluations

Finally, let's set up our evaluation pipeline using Braintrust:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def run_evaluations(num_samples: int = 100):
    data = list(load_data(limit=num_samples))

    braintrust.Eval(
        "emotion-classification-cookbook-main",
        data=data,  # Return the preloaded data
        task=random_classifier,
        scores=[emotion_precision, emotion_recall, emotion_f1],
        metadata={"classifier_type": "random"},
        experiment_name="random-classifier",
    )

    braintrust.Eval(
        "emotion-classification-cookbook-main",
        data=data,  # Return the preloaded data
        task=llm_classifier,
        scores=[emotion_precision, emotion_recall, emotion_f1],
        metadata={"classifier_type": "llm", "model": "gpt-4o"},
        experiment_name="llm-classifier",
    )


if __name__ == "__main__":
    run_evaluations(num_samples=100)  # Adjust the number of samples as needed
```

## Analyzing the results

Once you run the evaluations, you'll see the results in your Braintrust dashboard. The LLM classifier should significantly outperform the random baseline across all metrics.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/results.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1891bac93f4a79496bfca11a411bf2e7" alt="results.png" data-og-width="2879" width="2879" data-og-height="1460" height="1460" data-path="cookbook/assets/PrecisionRecall/results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/results.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=02d3cf97f683e94a122da77cf986a957 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/results.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=66193d0b129d757aa03dc803bd62d6e8 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/results.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=042079813f85c8b496485ff4fe1fac88 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/results.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5c0143115ad5111c40323f73f53878fb 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/results.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=233228a5df69e4d933102430d099f574 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/results.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=965996e1bcf93fd15673ab6a28d23b68 2500w" />

Key features to examine:

* Compare precision and recall scores between our runs
* Look at specific examples where the LLM fails
* Analyze cases where multiple emotions are present

One of the more common next steps is to answer questions like "What is my model's precision on amusement?" or "What is my model's recall on anger?". Braintrust makes this easy to do with our filtering features in the UI.

Select **Filter**, **Output**, then **contains**, and enter the emotion you want to look at, such as "amusement" or "anger" in the input box. The precision and recall scores will then be specific to the selected class.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/filters.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=c493b07ae5eb0950beb2f1fbe8c2d350" alt="filter.png" data-og-width="2320" width="2320" data-og-height="1318" height="1318" data-path="cookbook/assets/PrecisionRecall/filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/filters.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=462f22494db8c5ed355a3b0a0b788370 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/filters.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=46586e694b63f7ca0d1f4f274b55021a 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/filters.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=c59e7d4fdf39c5a4c63880840548d8a1 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/filters.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=51789d68ef1a8fe5992af711d8f0b7ce 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/filters.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e188e713841698b410ca32a64a36fc79 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PrecisionRecall/filters.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=3c2f79b1dfc9e7bd0caabdcb7cb4dd02 2500w" />

## Next steps

There are several ways to improve this emotion classifier, including:

* Experimenting with different prompts and instructions, or even a series of prompts.
* Adding a `rationale` to the output for each emotion to help us identify the root cause of the classifier's failures and improve the prompts accordingly.
* Trying other models like xAI's [Grok 2](https://x.ai/blog/grok-2) or OpenAI's [o1](https://openai.com/o1/). To learn more about comparing evals across multiple AI models, check out this [cookbook](https://www.braintrust.dev/docs/cookbook/recipes/ModelComparison).
* Adding more sophisticated scoring functions or [LLM-based scoring functions](/evaluate/run-evaluations#score-using-ai) to evaluate something like "anger" recall.
