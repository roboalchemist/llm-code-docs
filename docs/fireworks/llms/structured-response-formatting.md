# Source: https://docs.fireworks.ai/structured-responses/structured-response-formatting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Structured Outputs

> Enforce output formats using JSON schemas or custom grammars

Structured outputs ensure model responses conform to your specified format, making them easy to parse and integrate into your application. Fireworks supports two methods: **JSON mode** (using JSON schemas) and **Grammar mode** (using custom BNF grammars).

<Info>
  New to structured outputs? Check out the [Serverless Quickstart](/getting-started/quickstart#structured-outputs) for a quick introduction.
</Info>

## Quick Start

Force model output to conform to a [JSON schema](https://json-schema.org/):

```python  theme={null}
import os
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

# Define your schema
class Result(BaseModel):
    winner: str

# Make the request
response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "Result",
            "schema": Result.model_json_schema()
        }
    },
    messages=[{
        "role": "user",
        "content": "Who won the US presidential election in 2012? Reply in JSON format."
    }]
)

print(response.choices[0].message.content)
# Output: {"winner": "Barack Obama"}
```

<Tip>
  Include the schema in **both** your prompt and the `response_format` for best results. The model doesn't automatically "see" the schema—it's enforced during generation.
</Tip>

## Response Format Options

Fireworks supports two JSON mode variants:

* **`json_object`** – Force any valid JSON output (no specific schema)
* **`json_schema`** – Enforce a specific JSON schema (recommended)

<Warning>
  Always instruct the model to produce JSON in your prompt. Without this, the model may generate whitespace indefinitely until hitting token limits.
</Warning>

<AccordionGroup>
  <Accordion title="Using arbitrary JSON mode">
    To force JSON output without a specific schema:

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        response_format={"type": "json_object"},
        messages=[{
            "role": "user",
            "content": "List the top 3 programming languages in JSON format."
        }]
    )
    ```

    This is similar to [OpenAI's JSON mode](https://platform.openai.com/docs/guides/text-generation/json-mode).
  </Accordion>

  <Accordion title="Important notes and limitations">
    **Token limits:** If `finish_reason="length"`, the response may be truncated and invalid JSON. Increase `max_tokens` if needed.

    **Completions API:** JSON mode works with both Chat Completions and Completions APIs.

    **Function calling:** When using [Tool Calling](/guides/function-calling), JSON mode is enabled automatically—these guidelines don't apply.
  </Accordion>
</AccordionGroup>

## JSON Schema Support

Fireworks supports most [JSON schema specification](https://json-schema.org/specification) constructs:

**Supported:**

* Types: `string`, `number`, `integer`, `boolean`, `object`, `array`, `null`
* Object constraints: `properties`, `required`
* Array constraints: `items`
* Nested schemas: `anyOf`, `$ref`

**Not yet supported:**

* `oneOf` composition
* Length/size constraints (`minLength`, `maxLength`, `minItems`, `maxItems`)
* Regular expressions (`pattern`)

<Tip>
  Fireworks automatically prevents hallucinated fields by treating schemas with `properties` as if `"unevaluatedProperties": false` is set.
</Tip>

<Accordion title="Advanced: Reasoning Model JSON Mode">
  Some models support generating structured JSON outputs with visible reasoning. In this mode, the model's response includes a `<think>...</think>` section showing its reasoning process, followed by the JSON output.

  #### Example Usage

  ```python  theme={null}
  import os
  import re
  from openai import OpenAI
  from pydantic import BaseModel

  client = OpenAI(
      api_key=os.environ.get("FIREWORKS_API_KEY"),
      base_url="https://api.fireworks.ai/inference/v1"
  )

  # Define the output schema
  class QAResult(BaseModel):
      question: str
      answer: str

  # Make the request
  response = client.chat.completions.create(
      model="accounts/fireworks/models/deepseek-v3p1",
      messages=[{"role": "user", "content": "Who wrote 'Pride and Prejudice'?"}],
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "QAResult",
              "schema": QAResult.model_json_schema()
          }
      },
      max_tokens=1000
  )

  # Extract the response content
  response_content = response.choices[0].message.content

  # Extract reasoning (if present)
  reasoning_match = re.search(r"<think>(.*?)</think>", response_content, re.DOTALL)
  reasoning = reasoning_match.group(1).strip() if reasoning_match else None

  # Extract JSON
  json_match = re.search(r"</think>\s*(\{.*\})", response_content, re.DOTALL) if reasoning else re.search(r"(\{.*\})", response_content, re.DOTALL)
  json_str = json_match.group(1).strip() if json_match else "{}"

  # Parse into Pydantic model
  qa_result = QAResult.model_validate_json(json_str)

  if reasoning:
      print("Reasoning:", reasoning)
  print("Result:", qa_result.model_dump_json(indent=2))
  ```

  #### Use Cases

  Reasoning mode is useful for:

  * **Debugging**: Understanding why the model generated specific outputs
  * **Auditing**: Documenting the decision-making process
  * **Complex tasks**: Scenarios where the reasoning is as valuable as the final answer

  #### Additional Examples

  <CardGroup cols={2}>
    <Card title="Computer Specs with Reasoning" icon="square-1" href="https://colab.research.google.com/drive/1zBK1nDITDNOx7oRWxh19C5_sNSh64PKM?usp=sharing">
      Generate structured PC specifications with reasoning
    </Card>

    <Card title="Healthcare Records with Reasoning" icon="square-2" href="https://colab.research.google.com/drive/1njzOgHWgguSuA732RYROJDiCua3hGO_R?usp=sharing">
      Structure patient records with AI-generated reasoning
    </Card>
  </CardGroup>
</Accordion>

## Grammar Mode

For advanced use cases where JSON isn't sufficient, use [Grammar mode](/structured-responses/structured-output-grammar-based) to constrain outputs using custom BNF grammars. Grammar mode is ideal for:

* **Classification tasks** – Limit output to a predefined list of options
* **Language-specific output** – Force output in specific languages or character sets
* **Custom formats** – Define arbitrary output structures beyond JSON

[Learn more about Grammar mode →](/structured-responses/structured-output-grammar-based)

## Related features

Check out [Tool Calling](/guides/function-calling) for multi-turn capabilities and routing across multiple schemas.
