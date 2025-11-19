# Source: https://docs.baseten.co/inference/structured-output.md

# Structured output (JSON mode)

> Enforce an output schema on LLM inference

<Note>
  Structured outputs requires an LLM deployed using the [TensorRT-LLM Engine Builder](/development/model/performance/engine-builder-overview).

  If you want to try this structured output example code for yourself, deploy [this implementation of Llama 3.1 8B](/examples/tensorrt-llm).
</Note>

To generate structured outputs:

1. Define an object schema with [Pydantic](https://docs.pydantic.dev/latest/).
2. Pass the schema to the LLM with the `response_format` argument.
3. Receive output that is guaranteed to match the provided schema, including types and validations like `max_length`.

Using structured output, you should observe approximately equivalent tokens per second output speed to an ordinary call to the model after an initial delay for schema processing. If you're interested in the mechanisms behind structured output, check out this [engineering deep dive on our blog](https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms).

## Schema generation with Pydantic

[Pydantic](https://docs.pydantic.dev/latest/) is an industry standard Python library for data validation. With Pydantic, we'll build precise schemas for LLM output to match.

For example, here's a schema for a basic `Person` object.

```python  theme={"system"}
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Person(BaseModel):
    first_name: str = Field(..., description="The person's first name", max_length=50)
    last_name: str = Field(..., description="The person's last name", max_length=50)
    age: int = Field(..., description="The person's age, must be a non-negative integer")
    email: str = Field(..., description="The person's email address")
```

Structured output supports multiple data types, required and optional fields, and additional validations like `max_length`.

## Add response format to LLM call

<Warning>
  The first time that you pass a given schema for the model, it can take a
  minute for the schema to be processed and cached. Subsequent calls with the
  same schema will run at normal speeds.
</Warning>

Once your object is defined, you can add it as a parameter to your LLM call with the `response_format` field:

```python  theme={"system"}
import json
import requests


payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        { "role": "user", "content": "Make up a new person!"},
    ],
    "max_tokens": 512,
    "response_format": {  # Add this parameter to use structured outputs
        "type": "json_schema",
        "json_schema": {"schema": Person.model_json_schema()},
    },
}

MODEL_ID = ""
BASETEN_API_KEY = ""

resp = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload,
)

json.loads(resp.text)
```

The response may have an end of sequence token, which will need to be removed before the JSON can be parsed.

## Parsing LLM output

From the LLM, we expect output in the following format:

```json  theme={"system"}
{
  "first_name": "Astrid",
  "last_name": "Nyxoria",
  "age": 28,
  "email": "astrid.nyxoria@starlightmail.com"
}
```

This example output is valid, which can be double-checked with:

```python  theme={"system"}
Person.parse_raw(resp.text)
```
