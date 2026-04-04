# Source: https://www.promptfoo.dev/docs/configuration/parameters/

# Prompts, tests, and outputs

Configure how promptfoo evaluates your LLM applications.

## Detailed Documentation

For comprehensive guides, see the dedicated pages:

- **[Prompts](/docs/configuration/prompts/)** - Configure what you send to LLMs
- **[Test Cases](/docs/configuration/test-cases/)** - Set up evaluation scenarios
- **[Output Formats](/docs/configuration/outputs/)** - Save and analyze results

## Quick Start

```yaml
# Define your prompts
prompts:
  - 'Translate to {{language}}: {{text}}'

# Configure test cases
tests:
  - vars:
      language: French
      text: Hello world
    assert:
      - type: contains
        value: Bonjour

# Run evaluation
# promptfoo eval
```

## Core Concepts

### 📝 [Prompts](/docs/configuration/prompts/)

Define what you send to your LLMs - from simple strings to complex conversations.

#### Common patterns

**Text prompts**

```yaml
prompts:
  - 'Summarize this: {{content}}'
  - file://prompts/customer_service.txt
```

**Chat conversations**

```yaml
prompts:
  - file://prompts/chat.json
```

**Dynamic prompts**

```yaml
prompts:
  - file://generate_prompt.js
  - file://create_prompt.py
```

[Learn more about prompts →](/docs/configuration/prompts/)

### 🔮 [Test Cases](/docs/configuration/test-cases/)

Configure evaluation scenarios with variables and assertions.

#### Common patterns

**Inline tests**

```yaml
tests:
  - vars:
      question: "What's 2+2?"
    assert:
      - type: equals
        value: '4'
```

**CSV test data**

```yaml
tests: file://test_cases.csv
```

**HuggingFace datasets**

```yaml
tests: huggingface://datasets/rajpurkar/squad
```

**Dynamic generation**

```yaml
tests: file://generate_tests.js
```

[Learn more about test cases →](/docs/configuration/test-cases/)

### 📊 [Output Formats](/docs/configuration/outputs/)

Save and analyze your evaluation results.

#### Available formats

```bash
# Visual report
promptfoo eval --output results.html

# Data analysis
promptfoo eval --output results.json

# Spreadsheet
promptfoo eval --output results.csv
```

[Learn more about outputs →](/docs/configuration/outputs/)

## Complete Example

Here's a real-world example that combines multiple features:

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: Customer service chatbot evaluation

prompts:
  # Simple text prompt
  - 'You are a helpful customer service agent. {{query}}'

  # Chat conversation format
  - file://prompts/chat_conversation.json

  # Dynamic prompt with logic
  - file://prompts/generate_prompt.js

providers:
  - openai:gpt-5-mini
  - anthropic:claude-3-haiku

tests:
  # Inline test cases
  - vars:
      query: 'I need to return a product'
    assert:
      - type: contains
        value: 'return policy'
      - type: llm-rubric
        value: 'Response is helpful and professional'

  # Load more tests from CSV
  - file://test_scenarios.csv

# Save results
outputPath: evaluations/customer_service_results.html
```

## Quick Reference

### Supported File Formats

| Format | Prompts | Tests | Use Case |
| --- | --- | --- | --- |
| `.txt` | ✅ | ❌ | Simple text prompts |
| `.json` | ✅ | ✅ | Chat conversations, structured data |
| `.yaml` | ✅ | ✅ | Complex configurations |
| `.csv` | ✅ | ✅ | Bulk data, multiple variants |
| `.js`/`.ts` | ✅ | ✅ | Dynamic generation with logic |
| `.py` | ✅ | ✅ | Python-based generation |
| `.md` | ✅ | ❌ | Markdown-formatted prompts |
| `.j2` | ✅ | ❌ | Jinja2 templates |
| HuggingFace datasets | ❌ | ✅ | Import from existing datasets |

### Variable Syntax

Variables use [Nunjucks](https://mozilla.github.io/nunjucks/) templating:

```yaml
# Basic substitution
prompt: 'Hello {{name}}'

# Filters
prompt: 'URGENT: {{message | upper}}'

# Conditionals
prompt: '{% if premium %}Premium support: {% endif %}{{query}}'
```

### File References

All file paths are relative to the config file:

```yaml
# Single file
prompts:
  - file://prompts/main.txt

# Multiple files with glob
tests:
  - file://tests/*.yaml

# Specific function
prompts:
  - file://generate.js:createPrompt
```

Wildcards like `path/to/prompts/**/*.py:func_name` are also supported.

## Next Steps

- **[Prompts](/docs/configuration/prompts/)** - Deep dive into prompt configuration
- **[Test Cases](/docs/configuration/test-cases/)** - Learn about test scenarios and assertions
- **[HuggingFace Datasets](/docs/configuration/huggingface-datasets/)** - Import test cases from existing datasets
- **[Output Formats](/docs/configuration/outputs/)** - Understand evaluation results
- **[Expected Outputs](/docs/configuration/expected-outputs/)** - Configure assertions
- **[Configuration Reference](/docs/configuration/reference/)** - All configuration options