# Source: https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandOptions.md

# StagehandOptions<!-- -->

Stagehand-specific configuration options.

## Index[**](#Index)

### Properties

* [**apiKey](#apiKey)
* [**cacheDir](#cacheDir)
* [**domSettleTimeout](#domSettleTimeout)
* [**env](#env)
* [**llmClient](#llmClient)
* [**logInferenceToFile](#logInferenceToFile)
* [**model](#model)
* [**projectId](#projectId)
* [**selfHeal](#selfHeal)
* [**systemPrompt](#systemPrompt)
* [**verbose](#verbose)

## Properties<!-- -->[**](#Properties)

### [**](#apiKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L74)optionalapiKey

**apiKey?

<!-- -->

: string

API key - interpreted based on the `env` setting:

* When `env: 'LOCAL'`: LLM provider API key (OpenAI, Anthropic, or Google)
* When `env: 'BROWSERBASE'`: Browserbase API key

For LOCAL env, can also be set via environment variables:

* OpenAI: `OPENAI_API_KEY`
* Anthropic: `ANTHROPIC_API_KEY`
* Google: `GOOGLE_API_KEY`

- **@example**

  ```
  // Local with OpenAI
  stagehandOptions: {
    env: 'LOCAL',
    model: 'openai/gpt-4.1-mini',
    apiKey: 'sk-...',
  }

  // Browserbase cloud
  stagehandOptions: {
    env: 'BROWSERBASE',
    apiKey: 'bb-...',
    projectId: 'proj-...',
  }
  ```

### [**](#cacheDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L130)optionalcacheDir

**cacheDir?

<!-- -->

: string

Cache directory for observation caching to improve performance.

### [**](#domSettleTimeout)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L109)optionaldomSettleTimeout

**domSettleTimeout?

<!-- -->

: number = 30000

Time to wait for DOM to stabilize before performing AI operations (ms).

### [**](#env)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L45)optionalenv

**env?

<!-- -->

: LOCAL | BROWSERBASE = LOCAL | BROWSERBASE

Environment to run Stagehand in.

* `'LOCAL'`: Use local browser (default)
* `'BROWSERBASE'`: Use Browserbase cloud browsers

### [**](#llmClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L114)optionalllmClient

**llmClient?

<!-- -->

: LLMClient

Custom LLM client for AI operations.

### [**](#logInferenceToFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L125)optionallogInferenceToFile

**logInferenceToFile?

<!-- -->

: boolean = false

Enable logging of AI inference details to file for debugging.

### [**](#model)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L88)optionalmodel

**model?

<!-- -->

: [ModelConfiguration](https://crawlee.dev/js/api/stagehand-crawler.md#ModelConfiguration) = [ModelConfiguration](https://crawlee.dev/js/api/stagehand-crawler.md#ModelConfiguration)

AI model to use for act(), extract(), observe() operations. Can be a string like "openai/gpt-4.1-mini" or a detailed ModelConfiguration object.

* **@example**

  ```
  "openai/gpt-4.1-mini"
  ```

* **@example**

  ```
  "anthropic/claude-sonnet-4-20250514"
  ```

### [**](#projectId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L79)optionalprojectId

**projectId?

<!-- -->

: string

Browserbase project ID (required when env is 'BROWSERBASE').

### [**](#selfHeal)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L103)optionalselfHeal

**selfHeal?

<!-- -->

: boolean = true

Enable automatic error recovery for failed AI operations.

### [**](#systemPrompt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L119)optionalsystemPrompt

**systemPrompt?

<!-- -->

: string

Custom system prompt for AI operations.

### [**](#verbose)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L97)optionalverbose

**verbose?

<!-- -->

: 0 | 1 | 2 = 0 | 1 | 2

Logging verbosity level.

* 0: Minimal logging
* 1: Standard logging
* 2: Debug logging
