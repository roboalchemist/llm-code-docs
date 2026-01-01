# Source: https://docs.together.ai/docs/logprobs.md

# Getting Started with Logprobs

> Learn how to return log probabilities for your output tokens & build better classifiers.

Logprobs, short for log probabilities, are logarithms of probabilities that indicate the likelihood of each token occurring based on the previous tokens in the context. They allow users to gauge a model's confidence in its outputs and explore alternative responses considered by the model and are beneficial for various applications such as classification tasks, retrieval evaluations, and autocomplete suggestions.

One big use case of using logprobs is to assess how confident a model is in its answer. For example, if you were building a classifier to categorize emails into 5 categories, with logprobs, you can get back the category and the confidence of the model in that token. For example, the LLM can categorize an email as "Spam" with 87% confidence. You can then make decisions based on this probability like if it's too low, having a larger LLM classify a specific email.

## Returning logprobs

To return logprobs from our API, simply add `logprobs: 1` to your API call as seen below.

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  import json

  client = Together()

  completion = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "What are the top 3 things to do in New York?",
          }
      ],
      max_tokens=10,
      logprobs=1,
  )

  print(json.dumps(completion.model_dump(), indent=1))
  ```
</CodeGroup>

### Response of returning logprobs

Here's the response you can expect. You'll notice both the tokens and the log probability of every token is shown.

```json  theme={null}
{
  "id": "nrFCEVD-2j9zxn-934d8c409a0f43fd",
  "object": "chat.completion",
  "created": 1745413268,
  "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  "choices": [
    {
      "index": 0,
      "logprobs": {
        "tokens": [
          "New",
          " York",
          " City",
          " is",
          " a",
          " vibrant",
          " and",
          " diverse",
          " destination",
          " with"
        ],
        "token_logprobs": [
          -0.39648438, -2.026558e-6, -0.3515625, -0.609375, -0.023803711,
          -0.53125, -0.03149414, -0.43359375, -0.38085938, -0.74609375
        ],
        "token_ids": [3648, 4356, 4409, 374, 264, 34076, 323, 17226, 9284, 449],
        "top_logprobs": [
          { "New": -0.39648438 },
          { " York": -2.026558e-6 },
          { " City": -0.3515625 },
          { " is": -0.609375 },
          { " a": -0.023803711 },
          { " vibrant": -0.53125 },
          { " and": -0.03149414 },
          { " diverse": -0.43359375 },
          { " destination": -0.38085938 },
          { " with": -0.74609375 }
        ]
      },
      "seed": 15158565520978651000,
      "finish_reason": "length",
      "message": {
        "role": "assistant",
        "content": "New York City is a vibrant and diverse destination with",
        "tool_calls": []
      }
    }
  ],
  "prompt": [],
  "usage": {
    "prompt_tokens": 48,
    "completion_tokens": 10,
    "total_tokens": 58,
    "cached_tokens": 0
  }
}
```

## Converting logprobs to probabilities

Let's take the first token from the previous example: `{ "New": -0.39648438 }`. The "New" token has a logprob of -0.39648438, but this isn't very helpful by itself. However, we can quickly convert it to a probability by taking the exponential of it.

<CodeGroup>
  ```python Python theme={null}
  import math


  def get_probability(logprob: float) -> float:
      return round(math.exp(logprob) * 100, 2)


  print(get_probability(-0.39648438))
  # 67.02%
  ```
</CodeGroup>

This tells us that the model's confidence in starting with "New" was 67%. Let's now look at a practical example where this would be useful.

## A practical example for logprobs: Classification

In this example, we're building an email classifier and we want to know how confident the model is in its answer. We give the LLM 4 categories in the system prompt then pass in an example email.

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  import json

  client = Together()

  completion = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are a helpful email categorizer. Given an email, please classify it as one of the following categories: 'work', 'personal', 'spam', or 'other'. ONLY respond with the category name.",
          },
          {
              "role": "user",
              "content": "I hope this message finds you well. I am writing to request a meeting next week to discuss the progress of Project X. We have reached several key milestones, and I believe it would be beneficial to review our current status and plan the next steps together.Could we schedule a time that works best for you? Please let me know your availability between Tuesday and Thursday next week. Also, lmk if you still wanna grab dinner on Friday!.",
          },
      ],
      logprobs=1,
  )

  print(completion.choices[0].logprobs.top_logprobs)
  ```
</CodeGroup>

The output is the following:

```json  theme={null}
[{'work': -0.012512207}, {'<|eot_id|>': -0.005706787}]
```

This means that the model chose "work" as the answer, which is correct, and the logprob for work was `-0.012512207`. After taking the exponential of this, we get a probability of 98.7%. We're using a small and fast LLM here (llama 3.1 8B) which is great, but using logprobs, we can also tell when the model is unsure of its answer and see if we need to route it to a bigger LLM.

## Conclusion

We were able to use `logprobs` to show how to build a more robust classifier (and a cheaper classifier, using a smaller model for most queries but selectively using bigger models when needed). There are many other use cases for `logprobs` around autocompletion, keyword selection, and moderation.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt