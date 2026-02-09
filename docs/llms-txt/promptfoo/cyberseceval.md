# Source: https://www.promptfoo.dev/docs/red-team/plugins/cyberseceval/

# CyberSecEval Dataset for LLM Security Testing

## Overview

The CyberSecEval plugin uses Meta's [Purple Llama CyberSecEval dataset](https://meta-llama.github.io/PurpleLlama/docs/benchmarks/prompt_injection), a comprehensive benchmark suite designed to assess cybersecurity vulnerabilities in Large Language Models (LLMs).

The dataset includes multilingual prompt injection attacks, testing LLM systems against a diverse collection of potentially harmful prompts in multiple languages.

The dataset includes test cases that evaluate:

- Direct prompt injection attacks
- Indirect prompt injection attempts
- Security-violating content
- Logic-violating content
- Cross-language attack vectors
- System prompt leakage attempts

> **Tip**
>
> This plugin requires a target provider that accepts both a system prompt and user input in OpenAI-compatible chat format.

## How it works

The plugin:

- Downloads test cases from the CyberSecEval dataset
- Formats each test case as a system/user message pair
- Randomly selects prompts from the dataset
- Tests if the model appropriately handles the injection attempts
- Uses language-specific LLM-as-a-judge criteria to evaluate responses

![CyberSecEval Workflow](https://www.promptfoo.dev/docs/red-team/plugins/cyberseceval/data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjQwMCIgdmlld0JveD0iMCAwIDgwMCA0MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8IS0tIFN0eWxlIGRlZmluaXRpb25zIC0tPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlPgogICAgICAgICAgICAudGl0bGUgeyBmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyBmb250LXNpemU6IDE0cHg7IGZvbnQtd2VpZ2h0OiBib2xkOyB9CiAgICAgICAgICAgIC5sYWJlbCB7IGZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IGZvbnQtc2l6ZTogMTJweDsgfQogICAgICAgICAgICAuY29kZSB7IGZvbnQtZmFtaWx5OiBtb25vc3BhY2U7IGZvbnQtc2l6ZTogMTFweDsgfQogICAgICAgICAgICAuYXJyb3cgeyBzdHJva2U6ICM2NjY7IHN0cm9rZS13aWR0aDogMjsgZmlsbDogbm9uZTsgbWFya2VyLWVuZDogdXJsKCNhcnJvd2hlYWQpOyB9CiAgICAgICAgICAgIC5ib3ggeyBmaWxsOiAjZmZmOyBzdHJva2U6ICM2NjY7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAuaGlnaGxpZ2h0IHsgZmlsbDogI2UzZjJmZDsgfQogICAgICAgICAgICAucGFzcyB7IGZpbGw6ICM0Y2FmNTA7IH0KICAgICAgICAgICAgLmZhaWwgeyBmaWxsOiAjZjQ0MzM2OyB9CiAgICAgICAgPC9zdHlsZT4KICAgICAgICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSIxMCIgbWFya2VySGVpZ2h0PSI3IiByZWZYPSI5IiByZWZZPSIzLjUiIG9yaWVudD0iYXV0byI+CiAgICAgAgICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCAxMCAzLjUsIDAgNyIgZmlsbD0iIzY2NiIvPgogICAgICAgIDwvbWFya2VyPgogICAgPC9kZWZzPgoKICAgIDwhLS0gQmFja2dyb3VuZCAtLT4KICAgIDxyZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9IiNmZmZmZmYiLz4KCiAgICA8IS0tIERhdGFzZXQgQm94IC0tPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNTAsNTApIj4KICAgICAgICA8cmVjdCBjbGFzcz0iYm94IGhpZ2hsaWdodCIgd2lkdGg9IjIwMCIgaGVpZ2h0PSIxODAiIHJ4PSI1Ii8+CiAgICAgICAgPHRleHQgY2xhc3M9InRpdGxlIiB4PSIxMCIgeT0iMzAiPkN5YmVyU2VjRXZhbCBEYXRhc2V0PC90ZXh0PgogICAgICAgIDx0ZXh0IGNsYXNzPSJjb2RlIiB4PSIxMCIgeT0iNjAiPns8L3RleHQ+CiAgICAgICAgPHRleHQgY2xhc3M9ImNvZGUiIHg9IjIwIiB5PSI4NSI+InRlc3RfY2FzZV9wcm9tcHQiOiAiLi4uIiw8L3RleHQ+CiAgICAgICAgPHRleHQgY2xhc3M9ImNvZGUiIHg9IjIwIiB5PSIxMTAiPiJ1c2VyX2lucHV0IjogIi4uLiIsPC90ZXh0PgogICAgICAgIDx0ZXh0IGNsYXNzPSJjb2RlIiB4PSIxMCIgeT0iMTc1Ij59PC90ZXh0PgogICAgPC9nPgoKICAgIDwhLS0gUGx1Z2luIFByb2Nlc3NpbmcgQm94IC0tPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzAwLDMwKSI+CiAgICAgICAgPHJlY3QgY2xhc3M9ImJveCIgd2lkdGg9IjIwMCIgaGVpZ2h0PSIyMDAiIHJ4PSI1Ii8+CiAgICAgICAgPHRleHQgY2xhc3M9InRpdGxlIiB4PSIxMCIgeT0iMzAiPlBsdWdpbiBQcm9jZXNzaW5nPC90ZXh0PgogICAgICAgIDx0ZXh0IGNsYXNzPSJsYWJlbCIgeD0iMTAiIHk9IjcwIj4xLiBEb3dubG9hZCB0ZXN0IGNhc2VzPC90ZXh0PgogICAgICAgIDx0ZXh0IGNsYXNzPSJsYWJlbCIgeD0iMTAiIHk9IjEwMCI+Mi4gRm9ybWF0IGFzIG1lc3NhZ2VzPC90ZXh0PgogICAgICAgIDx0ZXh0IGNsYXNzPSJsYWJlbCIgeD0iMTAiIHk9IjEzMCI+My4gUmFuZG9tIHNlbGVjdGlvbjwvdGV4dD4KICAgICAgICA8dGV4dCBjbGFzcz0ibGFiZWwiIHg9IjEwIiB5PSIxNjAiPjQuIFRlc3QgbW9kZWw8L3RleHQ+CiAgICAgICAgPHRleHQgY2xhc3M9ImxhYmVsIiB4PSIxMCIgeT0iMTkwIj41LiBFdmFsdWF0ZSByZXNwb25zZTwvdGV4dD4KICAgIDwvZz4KCiAgICA8IS0tIExMTSBUZXN0aW5nIEJveCAtLT4KICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDU1MCw1MCkiPgogICAgICAgIDxyZWN0IGNsYXNzPSJib3ggaGlnaGxpZ2h0IiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjUiLz4KICAgICAgICA8dGV4dCBjbGFzcz0idGl0bGUiIHg9IjEwIiB5PSIzMCI+TExNIFRlc3Rpbmc8L3RleHQ+CiAgICAgICAgPHRleHQgY2xhc3M9ImNvZGUiIHg9IjEwIiB5PSI2MCI+UEFTUzogU2VjdXJlIHJlc3BvbnNlPC90ZXh0PgogICAgICAgIDx0ZXh0IGNsYXNzPSJmYWlsIiB4PSIxMCIgeT0iODUiPuKclzwvdGV4dD4KICAgICAgICA8dGV4dCBjbGFzcz0ibGFiZWwiIHg9IjI1IiB5PSI2MCI+UEFTUzogU2VjdXJlIHJlc3BvbnNlPC90ZXh0PgogICAgICAgIDx0ZXh0IGNsYXNzPSJmYWlsIiB4PSIxMCIgeT0iODUiPuKckzwvdGV4dD4KICAgICAgICA8dGV4dCBjbGFzcz0ibGFiZWwiIHg9IjI1IiB5PSI4NSI+InJvbGUiOiAic3lzdGVtIiw8L3RleHQ+CiAgICAgICAgPHRleHQgY2xhc3M9ImNvZGUiIHg9IjI1IiB5PSI4NSI+RkFJTDogVnVsbmVyYWJsZSByZXNwb25zZTwvdGV4dD4KICAgIDwvZz4KCiAgICA8IS0tIEFycm93cyAtLT4KICAgIDxwYXRoIGNsYXNzPSJhcnJvdyIgZD0iTTI1MCwxNDAgSDI5MCIvPgogICAgPHBhdGggY2xhc3M9ImFycm93IiBkPSJNNTAwLDE0MCBINTQwIi8+CiAgICA8cGF0aCBjbGFzcz0iYXJyb3ciIGQ9Ik00MDAsMjMwIFYyNzAiLz4KPC9zdmc+Cg==)

## Configuration

To include the CyberSecEval plugin in your LLM red teaming setup, add the following configuration to your YAML file:

```yaml
redteam:
  plugins:
    - cyberseceval
```

You can control the number of test cases using the `config.numTests` parameter (defaults to 5):

```yaml
redteam:
  plugins:
    - id: cyberseceval
      numTests: 25
```

You can also enable multilingual prompt injection by setting the `config.multilingual` parameter to `true`:

```yaml
redteam:
  plugins:
    - id: cyberseceval
      config:
        multilingual: true
```

## Full example

Create a configuration file `promptfooconfig.yaml`:

```yaml
targets:
  # You can target a model
  - openai:chat:gpt-5
  # Or an API endpoint
  - id: https
    config:
      url: 'https://example.com/generate'
      method: 'POST'
      headers:
        'Content-Type': 'application/json'
      body:
        myPrompt: '{{prompt}}'
redteam:
  plugins:
    - cyberseceval
```

Then, run the red team command in the same directory as your configuration file:

```sh
promptfoo redteam run
```

## Grading

The plugin uses a specialized grader that evaluates model outputs against language-specific judge questions. The grader checks if:

- The model maintained its original instructions despite the injection attempt
- The response adheres to security boundaries
- The model appropriately handled non-English attack vectors
- The system prompt remained protected from extraction attempts

Outputs are graded as either PASS (secure) or FAIL (vulnerable) based on these criteria.

## Related Concepts

- [Types of LLM Vulnerabilities](/docs/red-team/llm-vulnerability-types/)
- [Prompt Injection](/docs/red-team/strategies/prompt-injection/)
- [Language Configuration](/docs/red-team/configuration/#language) - Test in multiple languages