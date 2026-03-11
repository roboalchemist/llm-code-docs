# Source: https://docs.anyscale.com/llm/serving/structured-output.md

# Configure structured output for LLMs

[View Markdown](/llm/serving/structured-output.md)

# Configure structured output for LLMs

Learn how to deploy models with structured output patterns, including JSON schemas, guided choices, regular expressions, and grammar-based constraints.

note

Starting in `ray>=2.49.0`, Ray Serve LLM directly integrates vLLM APIs for structured output. See their [structured output documentation](https://docs.vllm.ai/en/stable/features/structured_outputs/) for more details.

caution

Starting with `ray>=2.50.2`, vLLM has started to deprecate the `guided_*` parameters in favor of the unified `structured_outputs` format.

If you're still using the following deprecated API fields, update your code to use `structured_outputs` as demonstrated in this document:

* `guided_json` → `{"structured_outputs": {"json": ...}}`
* `guided_regex` → `{"structured_outputs": {"regex": ...}}`
* `guided_choice` → `{"structured_outputs": {"choice": ...}}`
* `guided_grammar` → `{"structured_outputs": {"grammar": ...}}`
* `guided_whitespace_pattern` → `{"structured_outputs": {"whitespace_pattern": ...}}`
* `structural_tag` → `{"structured_outputs": {"structural_tag": ...}}`
* `guided_decoding_backend` → Remove this field from your request :::

## Understand structured output[​](#understand-structured-output "Direct link to Understand structured output")

Unstructured LLM outputs can be difficult to extract and process reliably. Structured outputs let you enforce a specific format, such as JSON, removing ambiguity and making it easier to integrate responses into downstream systems.

Use structured output when your application requires predictable fields or values.

Compared to unstructured text, structured output:

* Follows a fixed schema (for example, JSON, regular expressions, choices) instead of freeform language.
* Minimizes post-processing; responses are machine-readable by design.
* Ensures consistency between responses.

## Review supported output formats[​](#review-supported-output-formats "Direct link to Review supported output formats")

Since Ray Serve LLM uses vLLM as the inference engine, you can guide models to produce structured outputs using vLLM's built-in output formats.

| Format                  | Description                                                | Use case example                                                                 |
| ----------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **JSON output**         | Returns structured outputs using a JSON schema.            | Schema consistency, configuration generation, API responses.                     |
| **Choices**             | Restricts output to a predefined list of values.           | Classification tasks, form field selection.                                      |
| **Regular expressions** | Validates output format using regular expression patterns. | Dates, phone numbers, formatted strings, IDs.                                    |
| **Grammar**             | Defines rules using EBNF grammar.                          | SQL queries, code snippets, templates, custom DSLs.                              |
| **Structural tags**     | Applies schema constraints to parts of the response.       | Structured function calls, markup-like outputs, tool use, XML-style integration. |

caution

Not all models support every output format. To verify which structured formats your model supports, see the [vLLM compatibility matrix](https://docs.vllm.ai/en/stable/features/reasoning_outputs/#supported-models).

## Enforce JSON format[​](#enforce-json-format "Direct link to Enforce JSON format")

JSON outputs are especially useful when you build applications that require consistent, machine-readable outputs, such as configuration generation, API responses, or data extraction pipelines.

### Follow a specific schema[​](#json-schema-type "Direct link to Follow a specific schema")

warning

**Deprecation notice:** Starting with `ray>=2.50.2`, Ray Serve LLM is phasing out support for `extra_body={"guided_json": schema}`. You should use `response_format={"type": "json_schema", ...}` as shown in this section.

You can enforce a specific schema by setting the `response_format` parameter of your request with type `"json_schema"`:

1. Define your JSON schema.

2. In your client request, define a `response_format` parameter:

   <!-- -->

   * Set `type` to `"json_schema"`
   * Set `json_schema` to a dictionary with keys `name` and `schema`
   * Set `schema` to your JSON schema

The following example uses a [Pydantic model](https://docs.pydantic.dev/) to define the JSON schema:

```
from openai import OpenAI
from pydantic import BaseModel
from enum import Enum

client = OpenAI(...)

# (Optional) Use a Pydantic model to handle schema definition or validation.
class CarType(str, Enum):
    sedan = "sedan"
    suv = "SUV"
    truck = "Truck"
    coupe = "Coupe"

class CarDescription(BaseModel):
    brand: str
    model: str
    car_type: CarType

# 1. Define your schema.
json_schema = CarDescription.model_json_schema()

# 2. Send a request.
response = client.chat.completions.create(
    ...
    messages=[
        {
            "role": "user",
            "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's",
        }
    ],
    # 3. Set `response_format` of type `json_schema`
    response_format= {
        "type": "json_schema",
        # 4. Provide `name` and `schema` (both required).
        "json_schema": {
            "name": "car-description", # Arbitrary.
            "schema": json_schema # Your JSON schema.
        },
    }
)
```

Output:

```
{
  "brand": "Lexus",
  "model": "IS F",
  "car_type": "SUV"
}
```

tip

Using Pydantic is purely optional but strongly recommended. The key requirement is having a valid JSON schema.

### Freeform schema[​](#json-object-type "Direct link to Freeform schema")

You can generate freeform JSON without enforcing any specific schema by setting the `response_format` parameter of your request with type `"json_object"`.

```
from openai import OpenAI

client = OpenAI(...)

response = client.chat.completions.create(
    ...
    messages=[
        {
            "role": "user",
            "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's",
        }
    ]
    # Set the type of `response_format` to `json_object`.
    response_format={"type": "json_object"},
)
```

Output:

```
{
  "brand": "Ford",
  "model": "Mustang",
  "type": "Muscle Car"
}
```

### Troubleshoot JSON outputs[​](#troubleshoot-json-outputs "Direct link to Troubleshoot JSON outputs")

Even in structured output mode, LLMs may occasionally produce invalid JSON due to minor formatting errors.

The mistakes are often simple. Tools such as [`json_repair`](https://github.com/mangiucugna/json_repair) can often fix minor issues without losing content.

**Annotate errors:** Include error fields in JSON (for example, `"error": "description"`) for troubleshooting.

**System prompts:** To reduce errors with the [JSON Object type method](#json-object-type), include a format hint in the prompt:

```
{"role": "system", "content": "You are a helpful assistant. Always reply in this JSON format: {\"color\": string}"}
```

## Enforce list of choices[​](#enforce-list-of-choices "Direct link to Enforce list of choices")

warning

**Deprecation notice:** Starting with `ray>=2.50.2`, Ray Serve LLM is phasing out support for `extra_body={"guided_json": schema}`. You should use `extra_body={"structured_outputs": {"choice": ...}}` as shown in this section.

Set the `structured_outputs` parameter of the vLLM engine to `choice` mode to restrict the model's output to a set of predefined choices during generation.<br /><!-- -->This is especially useful for classification tasks, form field selection, or any situation where the response must match one of a few allowed values.

To implement guided choices:

1. Define your list of valid options.
2. Pass it to the vLLM engine using `extra_body={ "structured_outputs": { "choice": [...]} }` in your OpenAI client call.

```
from openai import OpenAI

client = OpenAI(...)

# 1. Define the valid choices.
choices = ["Purple", "Cyan", "Magenta"]

# 2. Make a call with the choices.
response = client.chat.completions.create(
    ...
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Always reply with one of the choices provided"},
        {"role": "user", "content": "Pick a color"}
    ],
    # 3. Pass it to the `guided_choice` field as an `extra_body`
    extra_body={
        "structured_outputs": { "choice": choices}
    }
)
```

Output:

```
Purple
```

The output follows the required choices. Without guidance, the model might default to more common options such as red, green, or blue.

## Enforce with regular expressions[​](#enforce-with-regular-expressions "Direct link to Enforce with regular expressions")

warning

**Deprecation notice:** Starting with `ray>=2.50.2`, Ray Serve LLM is phasing out support for `extra_body={"guided_json": schema}`. You should use `extra_body={"structured_outputs": {"regex": ...}}` as shown in this section.

note

Verify compatibility in the [vLLM compatibility matrix](https://docs.vllm.ai/en/stable/features/reasoning_outputs/#supported-models).

Set the `structured_outputs` parameter of the vLLM engine to `regex` mode to constrain the model's output to match a specific pattern during generation.

This is especially useful for structured outputs such as dates, phone numbers, formatted strings, IDs, or any pattern that needs to follow a strict format.

Because `structured_outputs` isn't part of the OpenAI API, you must pass it as an `extra_body` parameter so the vLLM engine can intercept and enforce it.

To implement regular expression constraints:

1. Define your regular expression pattern.
2. Pass it to the server using `extra_body={"structured_outputs": {"regex": ...}}` in your OpenAI client call.
3. To reduce errors, add an explicit "stop" extra parameter and make sure the regular expression pattern ends with it.

```
from openai import OpenAI

client = OpenAI(...)

# 1. Define a regular expression pattern for an email format.
email_pattern = r"^customprefix\.[a-zA-Z]+@[a-zA-Z]+\.com\n$" 

# 2. Make a call with the regex pattern.
response = client.chat.completions.create(
    ...
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Always reply following the pattern provided"},
        {"role": "user", "content": "Generate an example email address for Alan Turing, who works in Enigma. End your answer with a new line"}
    ],
    # 3. Pass it to the `structured_outputs` field as an `extra_body`.
    # For more reliability, add a `stop` parameter and include it at the end of your pattern.
    extra_body={
        "structured_outputs": {"regex": email_pattern},
        "stop": ["\n"]
    }
)
```

Output:

```
customprefix.alanturing@enigma.com
```

The output follows the required pattern, starting with `"customprefix.[...]"`. The prompt alone can't convey this constraint.

## Configure grammar constraints (advanced)[​](#configure-grammar-constraints-advanced "Direct link to Configure grammar constraints (advanced)")

warning

**Deprecation notice:** Starting with `ray>=2.50.2`, Ray Serve LLM is phasing out support for `extra_body={"guided_json": schema}`. You should use `extra_body={"structured_outputs": {"grammar": ...}}` as shown in this section.

Set the `structured_outputs` parameter of the vLLM engine to `grammar` mode to constrain the model's output to a custom formal grammar using a grammar-based decoder during generation.

This is especially useful for generating SQL queries, code snippets, templates, custom DSLs, or any pattern that needs to follow a strict format.

Because `structured_outputs` isn't part of the OpenAI API, you must pass it as an `extra_body` parameter so the vLLM engine can intercept and enforce it.

To implement grammar constraints:

1. Define your context-free [EBNF grammar](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form).
2. Pass it to the server using `extra_body={"structured_outputs": {"grammar": ...}}` in your OpenAI client call.

```
from openai import OpenAI

client = OpenAI(...)

# 1. Define the grammar.
simplified_sql_grammar = """
start: "SELECT " columns " from " table ";"

columns: column (", " column)?
column: "username" | "email" | "*"

table: "users"
"""

# 2. Make a call with the grammar.
response = client.chat.completions.create(
    ...
    messages=[
        {"role": "system", "content": "Respond with a SQL query using the grammar."},
        {"role": "user", "content": "Generate an SQL query to show the 'username' and 'email' from the 'users' table.",
        }
    ],
    # 3. Pass it to the `structured_outputs` field as an `extra_body`
    extra_body={
        "structured_outputs": {"grammar": simplified_sql_grammar}
    }
)
```

Output:

```
SELECT username, email from users;
```

The output adheres to the grammar by using uppercase `"SELECT"` and lowercase `"from"`. Without grammar constraints, the model would likely use `"FROM"` in all caps.

## Configure structural tag formatting (advanced)[​](#configure-structural-tag-formatting-advanced "Direct link to Configure structural tag formatting (advanced)")

warning

**Deprecation notice:** Starting with `ray>=2.50.2`, Ray Serve LLM is phasing out support for `extra_body={"guided_json": schema}`. You should use `extra_body={"structured_outputs": {"structural_tag": ...}}` as shown in this section.

If you want to constrain the model's output to a custom structural tag formatting, use `structural_tag`, a vLLM-specific feature that uses a grammar-based decoder during generation.

In this mode, the LLM can generate freely, but must follow specific structural rules whenever it encounters a trigger token. You define each structure by a start tag, end tag, and schema that constrains the content between them.

This is especially useful for structured function calls, markup-style outputs, tool use, XML-style integration, or any similar pattern.

Because `structural_tag` isn't part of the OpenAI API, you must pass it as an `extra_body` parameter so the vLLM engine can intercept and enforce it.

To implement structural tag formatting, do the following:

1. Add clear formatting instructions in your system prompt to ensure your model hits the triggers when you want it.
2. Define structure rules with tags (triggers) and their schema.
3. Pass them to the server using `extra_body={"structured_outputs": {"structural_tag": ...}}` in your OpenAI client call.

```
#structural_tag.py
import json
from openai import OpenAI

client = OpenAI(...)

# 1. Describe the overall structural constraint in a system prompt.
system_prompt = """
You are a helpful assistant.

You can answer user questions and optionally call a function if needed. If calling a function, use the format:
<function=function_name>{"arg1": value1, ...}</function>

Example:
<function=get_weather>{"city": "San Francisco"}</function>

Task:
Start by writing a short description (two sentences max) of the requested city.
Then output a form that uses the tags below, one tag per line.
Finish by writing a short conclusion (two sentences max) on the main touristic things to do there.

Required tag blocks
<city-name>{"value": string}</city-name>
<state>{"value": string}</state>
<main-borough>{"value": string}</main-borough>
<baseball-teams>{"value": [string]}</baseball-teams>
<weather>{"value": string}</weather>
"""

# 2. Define the structural rules to follow (one per field).
structures = [
    {  # <city-name>{"value": "Boston"}
        "begin": "<city-name>",
        "schema": {
            "type": "object",
            "properties": {"value": {"type": "string"}},
            "required": ["value"],
        },
        "end": "</city-name>",
    },
    {  # <state>{"value": "MA"}
        "begin": "<state>",
        "schema": {
            "type": "object",
            "properties": {"value": {"type": "string"}},
            "required": ["value"],
        },
        "end": "</state>",
    },
    {  # <main-borough>{"value": "Charlestown"}
        "begin": "<main-borough>",
        "schema": {
            "type": "object",
            "properties": {"value": {"type": "string"}},
            "required": ["value"],
        },
        "end": "</main-borough>",
    },
    {  # <baseball-teams>{"value": ["Red Sox"]}
        "begin": "<baseball-teams>",
        "schema": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": ["value"],
        },
        "end": "</baseball-teams>",
    },
    {  # <weather>{"value": <function=get_weather>...</function>}
        "begin": "<weather>",
        "schema": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "pattern": r"^<function=get_weather>\{.*\}</function>$"
                }
            },
            "required": ["value"],
        },
        "end": "</weather>",
    },
    {  # <function=get_weather>{"city": "San Francisco"}
        "begin": "<function=get_weather>",
        "schema": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"]
        },
        "end": "</function>"
    }
]

# 3. Define the triggers: whenever the model types "<city-name" etc.
triggers = ["<city-name", "<state", "<main-borough", "<baseball-teams", "<weather", "<function="]


# 4. Create the structural tag configuration.
structural_tag_config = {
    "type": "structural_tag",
    "structures": structures,
    "triggers": triggers,
}

# 5. Make a call with the structural tag configuration.
response = client.chat.completions.create(
    ...
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "Tell me about a city in the east coast of the U.S"
        },
    ],
    # Pass the structural tag config as a JSON string in extra_body.
    extra_body={
        "structured_outputs": {
            "structural_tag": json.dumps(structural_tag_config)
        }
    }
)
```

Output:

```
Let's start with a description of the city you're interested in. For this example, we'll consider New York City, which is a vibrant metropolis located on the east coast of the United States.

<city-name>{"value": "New York City"}</city-name>
<state>{"value": "New York"}</state>
<main-borough>{"value": "Manhattan"}</main-borough>
<baseball-teams>{"value": ["New York Yankees", "New York Mets"]}</baseball-teams>
<weather>{"value": "<function=get_weather>{\"city\": \"New York City\"}</function>"}</weather>

New York City, located in the state of New York, is a bustling city known for its iconic landmarks such as the Statue of Liberty, Central Park, and Times Square. It's also home to two major baseball teams: the New York Yankees and the New York Mets. The weather in New York City can vary greatly depending on the season, so it's always a good idea to check the forecast before visiting.

Conclusion:
New York City offers an incredible array of attractions including Broadway shows, museums such as the Metropolitan Museum of Art and the American Museum of Natural History, and world-class dining experiences. Baseball fans won't want to miss visiting Yankee Stadium or watching a game at Citi Field. Whether you prefer exploring the city's diverse neighborhoods or relaxing in Central Park, New York City has something for everyone.
```

The model follows nested tag patterns correctly.

## Apply best practices[​](#apply-best-practices "Direct link to Apply best practices")

### Validate responses[​](#validate-responses "Direct link to Validate responses")

Make sure to validate your model's outputs against your expected format and handle errors gracefully.

```
response = client.chat.completions.create(...)
output = response.choices[0].message.content

try:
    # Validate JSON schema.
    parsed = ColorSchema.model_validate_json(output)
except ValidationError as e:
    print("Validation failed:", e)
```

### Enable streaming for responsiveness[​](#enable-streaming-for-responsiveness "Direct link to Enable streaming for responsiveness")

Enable `stream=True` in your client call to reduce latency, especially with larger responses.

```
from openai import OpenAI

client = OpenAI(...)

response = client.chat.completions.create(
    ...
    # Enable streaming mode.
    stream=True
)

# Stream chunk by chunk.
for chunk in response:
    data = chunk.choices[0].delta.content
    if data:
        print(data, end="", flush=True)
```

caution

Streaming mode can lead to incomplete or malformed outputs if system or application errors occur. Make sure to implement proper error handling and fallbacks.

### Reduce format drift with deterministic sampling[​](#reduce-format-drift-with-deterministic-sampling "Direct link to Reduce format drift with deterministic sampling")

For structured outputs, use low temperature settings to encourage deterministic behavior and reduce *format drift*.

### Handle reasoning models[​](#handle-reasoning-models "Direct link to Handle reasoning models")

Reasoning models generate internal "thoughts" before producing the final structured output. The guided decoding backend waits until the end of the reasoning segment (for example, a closing `</think>` tag) before enforcing the structured output.

First, pick an [appropriate reasoning parser](https://docs.vllm.ai/en/stable/features/reasoning_outputs/#supported-models) for your model:

```
applications:
- name: my-structured-output-app
  ...
  args:
    llm_configs:
      - model_loading_config:
          model_id: my-qwq-32B
          model_source: Qwen/QwQ-32B
        ...
        engine_kwargs:
          ...
          reasoning_parser: deepseek-r1 # <-- for QwQ models
```

If you set an appropriate reasoning parser, the response places the thinking process in the `reasoning_content` field and the structured output in `content`:

```
ChatCompletionMessage(
    role='assistant',
    reasoning_content="Okay, let me think this through step by step. First, Lexus is a brand that...",
    content='{"brand": "Lexus", "model": "IS F", "car_type": "SUV"}', 
)
```

Without a reasoning parser, the reasoning text may spill into `content`, often wrapped in `<think>...</think>`, which can break your structured output parsing.

For details on how to configure a reasoning parser, see [Deploy a reasoning LLM: Parse reasoning outputs](https://docs.ray.io/en/latest/serve/tutorials/deployment-serve-llm/reasoning-llm/README.html#parse-reasoning-outputs).

## Summary[​](#summary "Direct link to Summary")

In this guide, you learned how to enforce structured formats in model outputs using JSON schemas, choice constraints, regular expressions, grammar constraints, and structural tags. You also learned performance tips on troubleshooting, optimization, streaming, and handling reasoning outputs.

To explore related patterns such as function calling or tool use, see [LLMs and agentic AI on Anyscale](/llm.md).
