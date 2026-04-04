# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Defining Rules

> Explore supported metrics and operators in Galileo Protect to configure precise rulesets and enhance AI application monitoring and decision-making.

A condition or rule you never want your application to break. It's composed of three ingredients:

* A metric

* An operator

* A target value

Your Rules should evaluate to False for the base case, and to True for unwanted scenarios.

In the example above, the "*input/output shall never contain PII*" is encoded into a Rule like below:

<CodeGroup>
  ```py Python theme={null}
  gp.Rule(
      metric=gp.RuleMetrics.pii,
      operator=gp.RuleOperator.contains,
      target_value="ssn"
  )
  ```

  ```json REST API theme={null}
  {
      "metric": "pii",
      "operator": "contains",
      "target_value": "ssn",
  },
  ```
</CodeGroup>

### Metrics and Operators supported

We support several metrics within Protect rules. Because each metric can have different output values (e.g. float metrics, categorical, etc.), the Operators and Target values differ by metric. Below is a list of all supported metric and their available configurations:

* [Prompt Injection](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators#prompt-injection)

* [Context Adherence](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators#context-adherence)

* [PII](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators#pii)

* [Tone](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators#tone)

* [Toxicity](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators#toxicity)

* [Sexism](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators#sexism)

* [Registered Scorers](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators#registered-scorers)

## Prompt Injection

Used to detect and stop prompt injections in the input (Read more about [Prompt Injection](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/prompt-injection)).

**Metric Constants:**

* `gp.RuleMetrics.prompt_injection`

**Payload Field:** `input`

**Potential Categories:**

* impersonation

* obfuscation

* simple\_instruction

* few\_shot

* new\_context

**Operators and Target Value Supported:**

| Operator                                | Target Value                                                  |
| --------------------------------------- | ------------------------------------------------------------- |
| Any (`gp.RuleOperator.any`)             | A list of categories (e.g. \["obfuscation", "impersonation"]) |
| All (`gp.RuleOperator.all`)             | A list of categories (e.g. \["obfuscation", "impersonation"]) |
| Contains (`gp.RuleOperator.contains`)   | A single category (e.g. "impersonation")                      |
| Equal (`gp.RuleOperator.eq`)            | A single category (e.g. "impersonation")                      |
| Not equal (`gp.RuleOperator.neq`)       | A single category (e.g. "impersonation")                      |
| Empty (`gp.RuleOperator.empty`)         | -                                                             |
| Not Empty (`gp.RuleOperator.not_empty`) | -                                                             |

**Example:**

<CodeGroup>
  ```py Python theme={null}
  gp.Rule(
      metric=gp.RuleMetrics.prompt_injection,
      operator=gp.RuleOperator.any,
      target_value=["impersonation", "obfuscation"]
  )
  ```

  ```json REST API theme={null}
  {
      "metric": "prompt_injection",
      "operator": "any",
      "target_value": ["impersonation", "obfuscation"],
  },
  ```
</CodeGroup>

## PII (Personal Identifiable Information)

Used to detect and stop Personal Identifiable Information (PII). When applied on the input, it can be used to stop the user or company PII from being included in API calls to external services. When applied on the output, it can be used to prevent data leakage or PII being shown back to the user. Read more about [PII classes and their definitions](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/private-identifiable-information).

**Metric Constants:**

* `gp.RuleMetrics.pii`for output PII

* `gp.RuleMetrics.input_pii` for input PII

**Payload Field:** `input` (for input PII) or `output` (for output PII)

**Potential Categories:**

* account\_info
* address
* credit\_card\_info
* date\_of\_birth
* email
* name
* network\_info
* password
* phone\_number
* ssn
* username

**Operators and Target Value Supported:**

| Operator                                | Target Value                                    |
| --------------------------------------- | ----------------------------------------------- |
| Any (`gp.RuleOperator.any`)             | A list of categories (e.g. \["ssn", "address"]) |
| All (`gp.RuleOperator.all`)             | A list of categories (e.g. \["ssn", "address"]) |
| Contains (`gp.RuleOperator.contains`)   | A single category (e.g. "ssn")                  |
| Equal (`gp.RuleOperator.eq`)            | A single category (e.g. "ssn")                  |
| Not equal (`gp.RuleOperator.neq`)       | A single category (e.g. "ssn")                  |
| Empty (`gp.RuleOperator.empty`)         | -                                               |
| Not Empty (`gp.RuleOperator.not_empty`) | -                                               |

**Example:**

<CodeGroup>
  ```py Python theme={null}
  gp.Rule(
      metric=gp.RuleMetrics.pii,
      operator=gp.RuleOperator.any,
      target_value=["ssn", "address"]
  )
  ```

  ```json REST API theme={null}
  {
      "metric": "pii",
      "operator": "any",
      "target_value": ["ssn", "address"],
  },
  ```
</CodeGroup>

## Context Adherence

Measures whether your model's response was purely based on the context provided. It can be used to stop hallucinations from reaching your end users. Powered by [Context Adherence Luna](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna).

**Metric Constant:** `gp.RuleMetrics.context_adherence_luna`

**Payload Field:** Both `input` and `output` must be included in the payload

**Potential Values:** 0.00 to 1.00.

Generally, we see 0.1 as a good threshold below which we're confident the response is not adhering to the context.

**Operators Supported:**

* Greater than (`gp.RuleOperator.gt`)

* Less than (`gp.RuleOperator.lt`)

* Greater than or equal (`gp.RuleOperator.gte`)

* Less than or equal (`gp.RuleOperator.lte`)

**Example:**

<CodeGroup>
  ```py Python theme={null}
  gp.Rule(
      metric=gp.RuleMetrics.context_adherence_luna,
      operator=gp.RuleOperator.lt,
      target_value=0.90
  )
  ```

  ```json REST API theme={null}
  {
      "metric": "adherence_nli",
      "operator": "lt",
      "target_value": 0.90,
  },
  ```
</CodeGroup>

## Toxicity

Used to detect and stop toxic or foul language in the input (user query) or output (response shown to the user). Read more about [Toxicity](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/toxicity).

**Metric Constants:**

* `gp.RuleMetrics.toxicity`for output Toxicity

* `gp.RuleMetrics.input_toxicity` for input Toxicity

**Payload Field:** `input` or `output`

**Potential Values:** 0.00 to 1.00 (higher values indicate higher toxicity)

**Operators Supported:**

* Greater than (`gp.RuleOperator.gt`)

* Less than (`gp.RuleOperator.lt`)

* Greater than or equal (`gp.RuleOperator.gte`)

* Less than or equal (`gp.RuleOperator.lte`)

**Example:**

<CodeGroup>
  ```py Python theme={null}
  gp.Rule(
      metric=gp.RuleMetrics.toxicity,
      operator=gp.RuleOperator.gt,
      target_value=0.95
  )
  ```

  ```json REST API theme={null}
  {
      "metric": "toxicity",
      "operator": "gt",
      "target_value": 0.95,
  },
  ```
</CodeGroup>

## Sexism

Detect sexist or biased language. When applied on the input, it can be used to detect sexist remarks in user queries. When applied on the output, it can be used to prevent your application from using an making biased or sexist comments in its responses.

**Metric Constants:**

* `gp.RuleMetrics.sexist`for output Sexism

* `gp.RuleMetrics.input_sexist` for input Sexism

**Payload Field:** `input` or `output`

**Potential Values:** 0.00 to 1.00 (higher values indicate higher toxicity)

**Operators Supported:**

* Greater than (`gp.RuleOperator.gt`)

* Less than (`gp.RuleOperator.lt`)

* Greater than or equal (`gp.RuleOperator.gte`)

* Less than or equal (`gp.RuleOperator.lte`)

**Example:**

<CodeGroup>
  ```json REST API theme={null}
  {
      "metric": "sexist",
      "operator": "gt",
      "target_value": 0.95,
  },
  ```

  ```py Python theme={null}
  gp.Rule(
      metric=gp.RuleMetrics.sexist,
      operator=gp.RuleOperator.gt,
      target_value=0.95
  )
  ```
</CodeGroup>

## Tone

Primary tone detected from the text. When applied on the input, it can be used to detect negative tones in user queries. When applied on the output, it can be used to prevent your application from using an undesired tone in its responses.

**Metric Constants:**

* `gp.RuleMetrics.tone`for output Tone

* `gp.RuleMetrics.input_tone` for input Tone

**Payload Field:** `input` (for input Tone) or `output` (for output Tone)

**Potential Categories:**

* anger

* annoyance

* confusion

* fear

* joy

* love

* sadness

* surprise

* neutral

**Operators and Target Value Supported:**

| Operator                          | Target Value                       |
| --------------------------------- | ---------------------------------- |
| Equal (`gp.RuleOperator.eq`)      | A single category (e.g. "anger")   |
| Not equal (`gp.RuleOperator.neq`) | A single category (e.g. "neutral") |

**Example:**

<CodeGroup>
  ```py Python theme={null}
  gp.Rule(
      metric=gp.RuleMetrics.tone,
      operator=gp.RuleOperator.neq,
      target_value="neutral"
  )
  ```

  ```json REST API theme={null}
  {
      "metric": "tone",
      "operator": "neq",
      "target_value": "neutral",
  },
  ```
</CodeGroup>

## Registered Scorers

If you have a [registered scorer](https://docs.rungalileo.io/galileo/gen-ai-studio-products/galileo-evaluate/how-to/register-custom-metrics#registered-scorers), it can also be used in your Galileo Protect rulesets.

**Example:**

<CodeGroup>
  ```py Python theme={null}
  gp.Rule(
      metric=<registered-metric-name>,
      operator=<operator>,
      target_value=<target>,
  )
  ```

  ```json REST API theme={null}
  {
      "metric": "<registered-metric-name>",
      "operator": "<operator>",
      "target_value": <target>,
  },
  ```
</CodeGroup>

The operators and target values here should match the type of data that the registered scorer is expected to produce.
