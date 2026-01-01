# Source: https://braintrust.dev/docs/integrations/sdk-integrations/instructor.md

# Instructor

[Instructor](https://github.com/jxnl/instructor) is a Python library for generating structured outputs from LLMs using Pydantic models. Braintrust integrates with Instructor to trace structured output generation.

## Setup

Install Instructor alongside the Braintrust SDK and OpenAI client:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install braintrust instructor openai
  ```
</CodeGroup>

## Trace with Instructor

When using Instructor with Braintrust, wrap the OpenAI client with `wrap_openai` **before** patching with Instructor. This ensures Braintrust captures the low-level metrics and headers from OpenAI.

```python title="trace-instructor.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import instructor
from braintrust import init_logger, wrap_openai
from openai import OpenAI
from pydantic import BaseModel

# Initialize Braintrust
logger = init_logger(project="Your project name")

# Define your response model
class MyResponseModel(BaseModel):
    name: str
    age: int

# Wrap OpenAI client with Braintrust FIRST, then patch with Instructor
client = instructor.patch(wrap_openai(OpenAI()))

# Use as normal - all calls are traced
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Extract: John is 30 years old"}],
    response_model=MyResponseModel,
)
```

<Note>
  The order matters: `instructor.patch(wrap_openai(OpenAI()))` ensures Braintrust captures complete metrics.
</Note>

## Resources

* [Instructor documentation](https://github.com/jxnl/instructor)
* [Braintrust OpenAI integration](/integrations/ai-providers/openai)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt