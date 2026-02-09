# Source: https://www.promptfoo.dev/docs/configuration/prompts/

# Prompt Configuration

Define what you send to your LLMs - from simple strings to complex multi-turn conversations.

## Text Prompts

The simplest way to define prompts is with plain text:

```yaml
prompts:
  - "Translate the following text to French: {{text}}"
  - "Summarize this article: {{article}}"
```

### Multiline Prompts

Use YAML's multiline syntax for longer prompts:

```yaml
prompts:
  - |
    You are a helpful assistant.
    Please answer the following question:
    {{question}}
    Provide a detailed explanation.
```

### Variables and Templates

Prompts use [Nunjucks](https://mozilla.github.io/nunjucks/) templating:

```yaml
prompts:
  - file:////prompts/customer_service.txt
  - file:////prompts/technical_support.txt
```

#### Supported File Formats

##### Text Files (.txt)

Simple text prompts with variable substitution.

##### Markdown Files (.md)

```yaml
# System Instructions
You are an AI assistant for {{company}}.

Customer query: {{query}}
Please provide a helpful and professional response.
```

##### Jinja2 Templates (.j2)

```jinja
You are assisting with {{ topic }}.

{% if advanced_mode %}
Provide technical details and code examples.
{% else %}
Keep explanations simple and clear.
{% endif %}
```

##### Multiple Prompts in One File

Separate multiple prompts with `---`:

```text
Translate to French: {{text}}
---
Translate to Spanish: {{text}}
---
Translate to German: {{text}}
```

##### Using Globs

Load multiple files with glob patterns:

```yaml
prompts:
  - file:////prompts/*.txt
  - file:////scenarios/**/*.json
```

Wildcards like `path/to/prompts/**/*.py:func_name` are also supported.

## Chat Format (JSON)

For conversation-style interactions, use JSON format:

```yaml
prompts:
  - file:////chat_prompt.json
```

```json
[
  {
    "role": "system",
    "content": "You are a helpful coding assistant."
  },
  {
    "role": "user",
    "content": "Write a function to {{task}}"
  }
]
```

### Multi-Turn Conversations

```json
[
  {
    "role": "system",
    "content": "You are a tutoring assistant."
  },
  {
    "role": "user",
    "content": "What is recursion?"
  },
  {
    "role": "assistant",
    "content": "Recursion is a programming technique where a function calls itself."
  },
  {
    "role": "user",
    "content": "Can you show me an example in {{language}}?"
  }
]
```

## Dynamic Prompts (Functions)

Use JavaScript or Python to generate prompts with custom logic:

### JavaScript Functions

```yaml
prompts:
  - file:////generate_prompt.js
```

```javascript
module.exports = async function ({ vars, provider }) {
  // Access variables and provider info
  const topic = vars.topic;
  const complexity = vars.complexity || 'medium';

  // Build prompt based on logic
  if (complexity === 'simple') {
    return `Explain ${topic} in simple terms.`
  } else {
    return `Provide a detailed explanation of ${topic} with examples.`
  }
};
```

### Python Functions

```yaml
prompts:
  - file:////generate_prompt.py:create_prompt
```

```python
def create_prompt(context):
    vars = context['vars']
    provider = context['provider']

    # Dynamic prompt generation
    if vars.get('technical_audience'):
        return f"Provide a technical analysis of {vars['topic']}"
    else:
        return f"Explain {vars['topic']} for beginners"
```

### Function with Configuration

Return both prompt and provider configuration:

```javascript
module.exports = async function ({ vars }) {
  const complexity = vars.complexity || 'medium';

  return {
    prompt: `Analyze ${vars.topic}`,
    config: {
      temperature: complexity === 'creative' ? 0.9 : 0.3,
      max_tokens: complexity === 'detailed' ? 1000 : 200,
    }
  };
};
```

## Executable Scripts

Run any script or binary to generate prompts dynamically. This lets you use your existing tooling and any programming language.

Your script receives test context as JSON in the first argument and outputs the prompt to stdout.

### Usage

Explicitly mark as executable:

```yaml
prompts:
  - exec:./generate-prompt.sh
  - exec:/usr/bin/my-prompt-tool
```

Or just reference the script directly (auto-detected for `.sh`, `.bash`, `.rb`, `.pl`, and other common script extensions):

```yaml
prompts:
  - ./generate-prompt.sh
  - ./prompt_builder.rb
```

**Note**: Python files (`.py`) are processed as Python prompt templates, not executables. To run a Python script as an executable prompt, use the `exec:` prefix: `exec:./generator.sh`

Pass configuration if needed:

```yaml
prompts:
  - label: "Technical Prompt"
    raw: exec:./generator.sh
    config:
      style: technical
      verbose: true
```

### Examples

#### Shell script that reads from a database:

```bash
#!/bin/bash
CONTEXT=$1
USER_ID=$(echo "$CONTEXT" | jq -r '.vars.user_id')
# Fetch user history from database
HISTORY=$(psql -h localhost -U myapp -t -v user_id=$USER_ID -c "\nSELECT prompt_context FROM users WHERE id = :user_id")
echo "Based on your previous interactions: $HISTORY"
How can I help you today?"
```

#### Ruby script:

```ruby
#!/usr/bin/env ruby
require 'json'
require 'digest'
context = JSON.parse(ARGV[0])
user_id = context['vars']['user_id']
# Call LLM API here...
puts "\nUser query: #{context['vars']['query']}"
```

### Security Considerations

**Warning**: Executable scripts run with full permissions of the promptfoo process. Be mindful of:

- **User Input**: Scripts receive user-controlled `vars` as JSON. Always validate and sanitize inputs before using them in commands.
- **Untrusted Scripts**: Only run scripts from trusted sources. Scripts can access files, make network calls, and execute commands.
- **Environment Access**: Scripts can access environment variables, including API keys.
- **Timeout**: Configure a timeout via `config.timeout` (default: 60 seconds) to prevent hanging scripts.

### When to Use

This approach works well when you're already using scripts for prompt generation, need to query external systems (databases, APIs), or want to reuse code written in languages other than JavaScript or Python.

Scripts can be written in any language - Bash, Go, Rust, or even compiled binaries - as long as it reads JSON from argv and prints to stdout.

Note that there are dedicated handlers for Python and Javascript (see above).

## Model-Specific Prompts

Different prompts for different providers:

```yaml
prompts:
  - id: file://prompts/gpt_prompt.json
    label: gpt_prompt
  - id: file://prompts/claude_prompt.txt
    label: claude_prompt

providers:
  - id: openai:gpt-4
    prompts: [gpt_prompt]
  - id: anthropic:claude-3
    prompts: [claude_prompt]
```

Prompt filters match labels exactly, support group prefixes (e.g. `group` matches `group:...`), and allow wildcard prefixes like `group:*`.

The `prompts` field also works when providers are defined in external files (`file://provider.yaml`).

## CSV Prompts

Define multiple prompts in CSV format:

```yaml
prompts:
  - file://prompts.csv
```

```csv
prompt,label
"Translate to French: {{text}}","French Translation"
"Translate to Spanish: {{text}}","Spanish Translation"
"Translate to German: {{text}}","German Translation"
```

## External Prompt Management Systems

Promptfoo integrates with external prompt management platforms, allowing you to centralize and version control your prompts:

### Langfuse

[Langfuse](/docs/integrations/langfuse/) is an open-source LLM engineering platform with collaborative prompt management:

```yaml
prompts:
  - langfuse://my-prompt:3:text
  - langfuse://chat-prompt:1:chat

  - langfuse://my-prompt@production
  - langfuse://chat-prompt@staging:chat
  - langfuse://email-template@latest:text

  - langfuse://my-prompt:production # String detected as label
  - langfuse://chat-prompt:staging:chat # String detected as label
```

### Portkey

[Portkey](/docs/integrations/portkey/) provides AI observability with prompt management capabilities:

```yaml
prompts:
  - portkey://pp-customer-support-v2
  - portkey://pp-email-generator-prod
```

### Helicone

[Helicone](/docs/integrations/helicone/) offers prompt management alongside observability features:

```yaml
prompts:
  - helicone://greeting-prompt:1.0
  - helicone://support-chat:2.5
```

Variables from your test cases are automatically passed to these external prompts.

## Advanced Features

### Custom Nunjucks Filters

Create custom filters for prompt processing:

```javascript
module.exports = function (str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
};
```

```yaml
nunjucksFilters:
  uppercaseFirst: ./uppercase_first.js

prompts:
  - "Dear {{ name | uppercaseFirst }} {query}"
```

### Prompt Labels and IDs

Organize prompts with labels:

```yaml
prompts:
  - id: file://customer_prompt.txt
    label: "Customer Service"
  - id: file://technical_prompt.txt
    label: "Technical Support"
```

### Default Prompt

If no prompts are specified, promptfoo uses `{{prompt}}` as a passthrough.

## Best Practices

1. **Start Simple**: Use inline text for basic use cases
2. **Organize Complex Prompts**: Move longer prompts to files
3. **Use Version Control**: Track prompt files in Git
4. **Leverage Templates**: Use variables for reusable prompts
5. **Test Variations**: Create multiple versions to compare performance

## Common Patterns

### System + User Message

```json
[
  {
    "role": "system",
    "content": "You are {{role}}"
  },
  {
    "role": "user",
    "content": "{{query}}"
  }
]
```

### Few-Shot Examples

```yaml
prompts:
  - |
    Classify the sentiment:
    Text: "I love this!"
    Text: "This is terrible"
    Text: "{text}"
```

### Chain of Thought

```yaml
prompts:
  - |
    Question: {{question}}
    Let's think step by step:
    1. First, identify what we know
    2. Then, determine what we need to find
    3. Finally, solve the problem
    Answer:
```

## Viewing Final Prompts

To see the final rendered prompts:

1. Run `promptfoo view`
2. Enable **Table Settings** > **Show full prompt in output cell**

This shows exactly what was sent to each provider after variable substitution.