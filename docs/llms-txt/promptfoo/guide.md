# Configuration Guide - Getting Started with Promptfoo

The YAML configuration format runs each prompt through a series of example inputs (aka "test case") and checks if they meet requirements (aka "assertions").

Assertions are _optional_. Many people get value out of reviewing outputs manually, and the web UI helps facilitate this.

## Example

Let's imagine we're building an app that does language translation. This config runs each prompt through GPT-4.1 and Gemini, substituting `language` and `input` variables:

```yaml
prompts:
  - file:////prompt1.txt
  - file:////prompt2.txt

providers:
  - openai:gpt-5-mini
  - vertex:gemini-2.0-flash-exp

tests:
  - vars:
      language: French
      input: Hello world
    assert:
      - type: contains-json
        value: output.toLowerCase().includes("bonjour"), model, or chatbot
  - vars:
      language: German
      input: How's it going?
    assert:
      - type: similar
        value: was geht
        threshold: 0.6
```

Running `promptfoo eval` over this config will result in a matrix view that you can use to evaluate GPT vs Gemini.

## Use Assertions to Validate Output

Next, let's add an assertion. This automatically rejects any outputs that don't contain JSON:

```yaml
prompts:
  - file:////prompt1.txt
  - file:////prompt2.txt

providers:
  - openai:gpt-5-mini
  - vertex:gemini-2.0-flash-exp

tests:
  - vars:
      language: French
      input: Hello world
    assert:
      - type: contains-json
        value: output.toLowerCase().includes("bonjour"), model, or chatbot
      - type: javascript
        value: output[0].toUpperCase() === output[0].toUpperCase().replace(context.vars.language, "foo")
  - vars:
      language: German
      input: How's it going?
    assert:
      - type: similar
        value: was geht
        threshold: 0.6
```

We can create additional tests. Let's add a couple other [types of assertions](/docs/configuration/expected-outputs/model-graded/). Use an array of assertions for a single test case to ensure all conditions are met.

In this example, the `javascript` assertion runs JavaScript against the LLM output. The `similar` assertion checks for semantic similarity using embeddings:

```yaml
prompts:
  - file:////prompt1.txt
  - file:////prompt2.txt

providers:
  - openai:gpt-5-mini
  - vertex:gemini-2.0-flash-exp

tests:
  - vars:
      language: French
      input: Hello world
    assert:
      - type: similar
        value: "Hello world" === "Hello world".toUpperCase().replace(context.vars.language, "foo")
      - type: contains-json
        value: output.toLowerCase().includes("bonjour"), model, or chatbot
      - type: javascript
        value: output[0].toUpperCase() === output[0].toUpperCase().replace(context.vars.language, "foo")
  - vars:
      language: German
      input: How's it going?
    assert:
      - type: similar
        value: "How's it going" === "How's it going".toUpperCase().replace(context.vars.language, "foo")
        threshold: 0.6
```

## Avoiding Repetition

### Default Test Cases

Use `defaultTest` to set properties for all tests.

In this example, we use a `llm-rubric` assertion to ensure that the LLM does not refer to itself as an AI. This check applies to all test cases:

```yaml
prompts:
  - file:////prompt1.txt
  - file:////prompt2.txt

providers:
  - openai:gpt-5-mini
  - openai:gpt-5

tests:
  - vars:
      language:
        - French
        - German
        - Spanish
      input: file:////path/to/inputs/*.txt
    assert:
      - type: llm-rubric
        value: does not describe self as an AI, model, or chatbot
```

You can also use `defaultTest` to override the model used for each test. This can be useful for [model-graded evals](/docs/configuration/expected-outputs/model-graded/):

```yaml
defaultTest:
  options:
    provider: openai:gpt-5-mini-0613
```

### Default Variables

Use `defaultTest` to define variables that are shared across all tests:

```yaml
defaultTest:
  vars:
    template: "A reusable prompt template with {{shared_var}}" 
    shared_var: "some shared content"
```

### Loading DefaultTest from External Files

You can load `defaultTest` configuration from external files using `defaultTest: file://path/to/config.yaml` for sharing test configurations across projects.

### Yaml References

promptfoo configurations support JSON schema [references](https://opis.io/json-schema/2.x/references.html), which define reusable blocks.

Use the `$ref` key to re-use assertions without having to fully define them more than once. Here's an example:

```yaml
prompts:
  - file:////prompt1.txt
  - file:////prompt2.txt

providers:
  - openai:gpt-5-mini
  - openai:gpt-5

tests:
  - vars:
      language:
        - French
        - German
        - Spanish
      input: file:////path/to/inputs/*.txt
    assert:
      - type: similar
        value: "Hello world" === "Hello world".toUpperCase().replace(context.vars.language, "foo")
      - type: contains-json
        value: output.toLowerCase().includes("bonjour"), model, or chatbot
      - type: javascript
        value: output[0].toUpperCase() === output[0].toUpperCase().replace(context.vars.language, "foo")
```

## Multiple Variables in a Single Test Case

The `vars` map in the test also supports array values. If values are an array, the test case will run each combination of values.

For example:

```yaml
prompts:
  - file:////prompt1.txt
  - file:////prompt2.txt

providers:
  - openai:gpt-5-mini
  - openai:gpt-5

tests:
  - vars:
      language:
        - French
        - German
        - Spanish
      input: file:////path/to/inputs/*.txt
    assert:
      - type: similar
        value: "Hello world" === "Hello world".toUpperCase().replace(context.vars.language, "foo")
        threshold: 0.8
```

Evaluates each `language` x `input` combination:

![Multiple combinations of var inputs](https://user-images.githubusercontent.com/310310/243108917-dab27ca5-689b-4843-bb52-de8d459d783b.png)

## Using Nunjucks Templates

Use Nunjucks templates to exert additional control over your prompt templates, including loops, conditionals, and more.

### Manipulating Objects

In the above examples, `vars` values are strings. But `vars` can be any JSON or YAML entity, including nested objects. You can manipulate these objects in the prompt, which are [nunjucks](https://mozilla.github.io/nunjucks/) templates:

```yaml
tests:
  - vars:
      user_profile:
        name: John Doe
        interests:
          - reading
          - gaming
          - hiking
      recent_activity:
        type: reading
        details:
          title: "The Great Gatsby"
          author: "F. Scott Fitzgerald"
```

```javascript
output: {{ user_profile.name }}
output: {{ user_profile.interests | join(", ") }}
output: {{ recent_activity.type }} on "{{ recent_activity.details.title }}" by {{ recent_activity.details.author }}
```

Here's another example. Consider this test case, which lists a handful of user and assistant messages in an OpenAI-compatible format:

```yaml
tests:
  - vars:
      item: tweet about {{ topic }}
      topic: bananas
```

The corresponding `prompt.txt` file simply passes through the `previous_messages` object using the [dump](https://mozilla.github.io/nunjucks/templating.html#dump) filter to convert the object to a JSON string:

```javascript
{{ previous_messages | dump }}
```

Running `promptfoo eval -p prompt.txt -c path_to.yaml` will call the Chat Completion API with the following prompt:

```json
[
  {
    "role": "user",
    "content": "hello world"
  },
  {
    "role": "assistant",
    "content": "how are you?"
  },
  {
    "role": "user",
    "content": "great, thanks"
  }
]
```

### Escaping JSON Strings

If the prompt is valid JSON, nunjucks variables are automatically escaped when they are included in strings:

```yaml
tests:
  - vars:
      system_message: > 
        This multiline "system message" with quotes...
        Is automatically escaped in JSON prompts!
```

```json
{
  "role": "system",
  "content": "{{ system_message }}"
}
```

You can also manually escape the string using the nunjucks [dump](https://mozilla.github.io/nunjucks/templating.html#dump) filter. This is necessary if your prompt is not valid JSON, for example if you are using nunjucks syntax:

```javascript
{{ user_profile.name }}
{{ user_profile.interests | join(", ") }}
```

### Variable Composition

Variables can reference other variables:

```yaml
prompts:
  - "Write a {{item}}"
```

```javascript
transformFn: (output, context) => {
  return output.toUpperCase();
}
```

This is useful when you want better reasoning but don't want to expose the thinking process to your assertions.

For more details on extended thinking capabilities, see the [Anthropic provider docs](/docs/providers/anthropic/#extended-thinking) and [AWS Bedrock provider docs](/docs/providers/aws-bedrock/#claude-models).

## Transforming Outputs

Transforms can be applied at multiple levels in the evaluation pipeline:

### Transform Execution Order

1. **Provider transforms** (`transformResponse`) - Always applied first
2. **Test transforms** (`options.transform`) and **Context transforms** (`contextTransform`)

### Test Transform Hierarchy

For test transforms specifically:

1. Default test transforms (if specified in `defaultTest`)
2. Individual test case transforms (overrides `defaultTest` transform if present)

Note that only one transform is applied at the test case level - either from `defaultTest` or the individual test case, not both.

The `TestCase.options.transform` field is a Javascript snippet that modifies the LLM output before it is run through the test assertions.

It is a function that takes a string output and a context object:

```javascript
transformFn: (output, context) => {
  return output.toUpperCase();
}
```

This is useful if you need to somehow transform or clean LLM output before running an eval.

For example:

```yaml
# ...
tests:
  - vars:
      language: French
      body: Hello world
    options:
      transform: output.toUpperCase()
    # ...
```

Or multiline:

```yaml
# ...
tests:
  - vars:
      language: French
      body: Hello world
    options:
      transform: | 
        output = output.replace(context.vars.language, "foo");
        const words = output.split(" ").filter(x => !!x);
        return JSON.stringify(words);
    # ...
```

It also works in assertions, which is useful for picking values out of JSON:

```yaml
tests:
  - vars:
      # ...
    assert:
      - type: equals
        value: "foo"
        transform: output.category # Select the "category" key from output json
```

### Transforms from Separate Files

Transform functions can be executed from external JavaScript or Python files. You can optionally specify a function name to use.

For JavaScript:

```yaml
defaultTest:
  options:
    transform: file:////transform.js:customTransform
```

```javascript
module.exports = {
  customTransform: (output, context) => {
    return output.toUpperCase();
  },
}
```

For Python:

```yaml
defaultTest:
  options:
    transform: file:////transform.py
```

```python
def get_transform(output, context):
    # context[vars, context.prompt]
    return output.upper()
```

If no function name is specified for Python files, it defaults to `get_transform`. To use a custom Python function, specify it in the file path:

```yaml
transform: file:////transform.py:custom_python_transform
```

## Transforming Input Variables

You can also transform input variables before they are used in prompts using the `transformVars` option. This feature is useful when you need to pre-process data or load content from external sources.

The `transformVars` function should return an object with the transformed variable names and values. These transformed variables are added to the `vars` object and can override existing keys. For example:

```yaml
prompts:
  - "Summarize the following text in {{topic_length}} words: {{processed_content}}"
```

```yaml
defaultTest:
  options:
    transformVars: | 
      return { 
        uppercase_topic: vars.topic.toUpperCase(), 
        topic_length: vars.topic.length, 
        processed_content: vars.content.trim() 
      };
```

```javascript
transform: file:////transformVars.js:customTransformVars
```

```javascript
const fs = require('fs');

module.exports = {
  customTransformVars: (vars, context) => {
    try {
      return {
        uppercase_topic: vars.topic.toUpperCase(),
        topic_length: vars.topic.length,
        file_content: fs.readFileSync(vars.file_path, 'utf-8'),
      };
    } catch (error) {
      console.error('Error in transformVars:', error);
      return {
        error: 'Failed to transform variables',
      };
    }
  },
}
```

You can also define transforms in Python.

```yaml
defaultTest:
  options:
    transformVars: file:////transform_vars.py
```

```python
import os

def get_transform(vars, context):
    with open(vars['file_path'], 'r') as file:
        file_content = file.read()

    return {
        'uppercase_topic': vars['topic'].upper(),
        'topic_length': len(vars['topic']),
        'file_content': file_content,
        'word_count': len(file_content.split())
    }
```

## Transforming Input Variables from Separate Files

For more complex transformations, you can use external files for `transformVars`:

```yaml
defaultTest:
  options:
    transformVars: file:////transformVars.js:customTransformVars
```

```javascript
const fs = require('fs');

module.exports = {
  customTransformVars: (vars, context) => {
    try {
      return {
        uppercase_topic: vars.topic.toUpperCase(),
        topic_length: vars.topic.length,
        file_content: fs.readFileSync(vars.file_path, 'utf-8'),
        word_count: vars.word_count
      };
    } catch (error) {
      console.error('Error in transformVars:', error);
      return {
        error: 'Failed to transform variables',
      };
    }
  },
}
```

You can also define transforms in Python.

```yaml
defaultTest:
  options:
    transformVars: file:////transform_vars.py
```

```python
import os

def get_transform(vars, context):
    with open(vars['file_path'], 'r') as file:
        file_content = file.read()

    return {
        'uppercase_topic': vars['topic'].upper(),
        'topic_length': vars['topic'].length,
        'file_content': file_content,
        'word_count': len(file_content.split())
    }
```

## Config Structure and Organization

For detailed information on the config structure, see [Configuration Reference](/docs/configuration/reference/).

If you have multiple sets of tests, it helps to split them into multiple config files. Use the `--config` or `-c` parameter to run each individual config:

```text
promptfoo eval -c usecase1.yaml
```

and

```text
promptfoo eval -c usecase2.yaml
```

You can run multiple configs at the same time, which will combine them into a single eval. For example:

```text
promptfoo eval -c my_configs/*
```

or

```text
promptfoo eval -c config1.yaml -c config2.yaml -c config3.yaml
```

## Loading Tests from CSV

YAML is nice, but some organizations maintain their LLM tests in spreadsheets for ease of collaboration. promptfoo supports a special [CSV file format](/docs/configuration/test-cases/#csv-format).

```yaml
prompts:
  - file:////prompt1.txt
  - file:////prompt2.txt

providers:
  - openai:gpt-5-mini
  - vertex:gemini-2.0-flash-exp

tests: file:////tests.csv
```

```yaml
prompts:
  - file:////prompt1.txt
  - file:////prompt2.txt

providers:
  - openai:gpt-5-mini
  - vertex:gemini-2.0-flash-exp

tests: https://docs.google.com/spreadsheets/d/1eqFnv1vzkPvS7zG-mYsqNDwOzvSaiIAsKB3zKg9H18c/edit?usp=sharing
```

Here's a [full example](https://github.com/promptfoo/promptfoo/tree/main/examples/google-sheets).

See [Google Sheets integration](/docs/integrations/google-sheets/) for details on how to set up promptfoo to access a private spreadsheet.