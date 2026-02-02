# LLM Rubric

`llm-rubric` is promptfoo's general-purpose grader for "LLM as a judge" evaluation.

It is similar to OpenAI's [model-graded-closedqa](/docs/configuration/expected-outputs/) prompt, but can be more effective and robust in certain cases.

## How to use it

To use the `llm-rubric` assertion type, add it to your test configuration like this:

```yaml
assert:
  - type: llm-rubric
    value: Is not apologetic and provides a clear, concise answer
```

This assertion will use a language model to grade the output based on the specified rubric.

## How it works

Under the hood, `llm-rubric` uses a model to evaluate the output based on the criteria you provide. By default, it uses different models depending on which API keys are available:

- **OpenAI API key**: `gpt-5`
- **Anthropic API key**: `claude-sonnet-4-5-20250929`
- **Google AI Studio API key**: `gemini-2.5-pro` (GEMINI_API_KEY, GOOGLE_API_KEY, or PALM_API_KEY)
- **Google Vertex credentials**: `gemini-2.5-pro` (service account credentials)
- **Mistral API key**: `mistral-large-latest`
- **GitHub token**: `openai/gpt-5`
- **Azure credentials**: Your configured Azure GPT deployment

You can override this by setting the `provider` option (see below).

It asks the model to output a JSON object that looks like this:

```json
{
  "reason": "<Analysis of the rubric and the output>",
  "score": 0.5, // 0.0-1.0
  "pass": true // true or false
}
```

Use your knowledge of this structure to give special instructions in your rubric, for example:

```yaml
assert:
  - type: llm-rubric
    value: | 
      Evaluate the output based on how funny it is. Grade it on a scale of 0.0 to 1.0, where:
      Score of 0.1: Only a slight smile.
      Score of 0.5: Laughing out loud.
      Score of 1.0: Rolling on the floor laughing.
      Anything funny enough to be on SNL should pass,
```

## Using variables in the rubric

You can incorporate test variables into your LLM rubric. This is particularly useful for detecting hallucinations or ensuring the output addresses specific aspects of the input. Here's an example:

```yaml
providers:
  - openai:gpt-5-mini

prompts:
  - file://prompt1.txt
  - file://prompt2.txt

defaultTest:
  assert:
    - type: llm-rubric
      value: Provides a direct answer to the question: "{{question}}" without unnecessary elaboration

tests:
  - vars:
      question: What is the capital of France?
  - vars:
      question: How many planets are in our solar system?
```

## Overriding the LLM grader

By default, `llm-rubric` uses `gpt-5` for grading. You can override this in several ways:

1. Using the `--grader` CLI option:

    ```sh
    promptfoo eval --grader openai:gpt-5-mini
    ```

2. Using `test.options` or `defaultTest.options`:

    ```yaml
    defaultTest:
      options:
        provider: openai:gpt-5-mini
      assert:
        - type: llm-rubric
          value:
            Provides a direct answer to the question: "{{question}}" without unnecessary elaboration
    tests:
      - vars:
          question: What is the capital of France?
      - vars:
          question: How many planets are in our solar system?
    ```

3. Using `assertion.provider`:

    ```yaml
    tests:
      - description: Evaluate output using LLM
        assert:
          - type: llm-rubric
            value:
              Provides a direct answer to the question: "{{question}}" without unnecessary elaboration
              provider: openai:gpt-5-mini
    ```

## Customizing the rubric prompt

For more control over the `llm-rubric` evaluation, you can set a custom prompt using the `rubricPrompt` property:

```yaml
defaultTest:
  options:
    rubricPrompt: |
      [
        {
          "role": "system",
          "content": "Evaluate the following output based on these criteria:\n1. Clarity of explanation\n2. Accuracy of information\n3. Relevance to the topic\n\nProvide a score out of 10 for each criterion and an overall assessment."
        },
        {
          "role": "user",
          "content": "Output to evaluate: {{output}}\n\nRubric: {{rubric}}"
        }
      ]
```

## Non-English Evaluation

To get evaluation output in languages other than English, you can use different approaches:

### Option 1: rubricPrompt Override (Recommended)

For reliable multilingual output with compatible assertion types:

```yaml
defaultTest:
  options:
    rubricPrompt: |
      [
        {
          "role": "system",
          // German: "You evaluate outputs based on criteria. Respond with JSON: {\\"reason\\": \\"string\\", \\"pass\\": boolean, \\"score\\": number}. ALL responses in German."
          "content": "Du bewertest Ausgaben nach Kriterien. Antworte mit JSON: {\\"reason\\": \\"string\\", \\"pass\\": boolean, \\"score\\": number}. ALLE Antworten auf Deutsch."
        },
        {
          "role": "user",
          // German: "Output: {{ output }}\nCriterion: {{ rubric }}"
          "content": "Ausgabe: {{ output }}\nKriterium: {{ rubric }}"
        }
      ]
```

### Option 2: Language Instructions in Rubric

```yaml
assert:
  - type: llm-rubric
    value: "Responds politely and helpfully. Provide your evaluation reason in German."
```

### Option 3: Full Native Language Rubric

```yaml
# German
assert:
  - type: llm-rubric
    value: "Responds politely and helpfully. Provide reasoning in German."
    rubricPrompt: |
      [
        {
          "role": "system",
          // German: "You compare factual accuracy. Respond with JSON: {\\"category\\": \\"A/B/C/D/E\\", \\"reason\\": \\"string\\"}. A=subset, B=superset, C=identical, D=contradiction, E=irrelevant. ALL responses in German."
          "content": "Du vergleichst Faktentreue. Antworte mit JSON: {\\"category\\": \\"A/B/C/D/E\\", \\"reason\\": \\"string\\"}. A=Teilmenge, B=Obermenge, C=identisch, D=Widerspruch, E=irrelevant. ALLE Antworten auf Deutsch."
        },
        {
          "role": "user",
          // German: "Expert answer: {{ rubric }}\nSubmitted answer: {{ output }}"
          "content": "Expertenantwort: {{ rubric }}\nEingereichte Antwort: {{ output }}"
        }
      ]
```