# Prompt Guide
Source: https://docs.perplexity.ai/docs/agent-api/prompt-guide



## Instructions

You can use the `instructions` parameter to provide instructions related to style, tone, and language of the response.

<Warning>
  The real-time search component of our models does not attend to the system prompt.
</Warning>

**Example of a system prompt**

```
You are a helpful AI assistant.

Rules:
1. Provide only the final answer. It is important that you do not include any explanation on the steps below.
2. Do not show the intermediate steps information.

Steps:
1. Decide if the answer should be a brief sentence or a list of suggestions.
2. If it is a list of suggestions, first, write a brief and natural introduction based on the original query.
3. Followed by a list of suggestions, each suggestion should be split by two newlines.
```

## Input

You should use the `input` parameter to pass in the actual query for which you need an answer. The input will be used to kick off a real-time web search to make sure the answer has the latest and the most relevant information needed.

**Example of a user prompt**

```
What are the best sushi restaurants in the world currently?
```

## API Example

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    preset="pro-search",
    input="What are the best sushi restaurants in the world currently?",
    instructions="You are a helpful AI assistant. Provide concise, well-researched answers."
)

print(response.output_text)
```
