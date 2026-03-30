# Source: https://crawlee.dev/js/api/stagehand-crawler/class/Stagehand.md

# externalStagehand<!-- -->

V3

Purpose: A high-level orchestrator for Stagehand V3. Abstracts away whether the browser runs **locally via Chrome** or remotely on **Browserbase**, and exposes simple entrypoints (`act`, `extract`, `observe`) that delegate to the corresponding handler classes.

Responsibilities:

* Bootstraps Chrome or Browserbase, ensures a working CDP WebSocket, and builds a `V3Context`.
* Manages lifecycle: init, context access, cleanup.
* Bridges external page objects (Playwright/Puppeteer) into internal frameIds for handlers.
* Provides a stable API surface for downstream code regardless of runtime environment.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**browserbaseSessionId](#browserbaseSessionId)
* [**bus](#bus)
* [**disableAPI](#disableAPI)
* [**experimental](#experimental)
* [**llmClient](#llmClient)
* [**logInferenceToFile](#logInferenceToFile)
* [**stagehandMetrics](#stagehandMetrics)
* [**verbose](#verbose)

### Accessors

* [**browserbaseDebugURL](#browserbaseDebugURL)
* [**browserbaseSessionID](#browserbaseSessionID)
* [**browserbaseSessionURL](#browserbaseSessionURL)
* [**context](#context)
* [**history](#history)
* [**isBrowserbase](#isBrowserbase)
* [**logger](#logger)
* [**metrics](#metrics)

### Methods

* [**act](#act)
* [**addToHistory](#addToHistory)
* [**agent](#agent)
* [**close](#close)
* [**connectURL](#connectURL)
* [**extract](#extract)
* [**init](#init)
* [**isAgentReplayActive](#isAgentReplayActive)
* [**observe](#observe)
* [**recordAgentReplayStep](#recordAgentReplayStep)
* [**updateMetrics](#updateMetrics)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3638)externalconstructor

* ****new Stagehand**(opts): [V3](https://crawlee.dev/js/api/stagehand-crawler/class/Stagehand.md)

- #### Parameters

  * ##### externalopts: V3Options

  #### Returns [V3](https://crawlee.dev/js/api/stagehand-crawler/class/Stagehand.md)

## Properties<!-- -->[**](#Properties)

### [**](#browserbaseSessionId)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3612)externaloptionalbrowserbaseSessionId

**browserbaseSessionId?

<!-- -->

: string

### [**](#bus)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3605)externalreadonlybus

**bus: EventEmitter\<DefaultEventMap>

Event bus for internal communication. Emits events like 'screenshot' when screenshots are captured during agent execution.

### [**](#disableAPI)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3625)externalreadonlydisableAPI

**disableAPI: boolean

### [**](#experimental)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3623)externalreadonlyexperimental

**experimental: boolean

### [**](#llmClient)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3600)externalllmClient

**llmClient: LLMClient

### [**](#logInferenceToFile)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3624)externalreadonlylogInferenceToFile

**logInferenceToFile: boolean

### [**](#stagehandMetrics)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3637)externalstagehandMetrics

**stagehandMetrics: StagehandMetrics

### [**](#verbose)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3627)externalverbose

**verbose: 0 | 1 | 2

## Accessors<!-- -->[**](#Accessors)

### [**](#browserbaseDebugURL)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3617)externalbrowserbaseDebugURL

* **get browserbaseDebugURL(): undefined | string

- #### Returns undefined | string

### [**](#browserbaseSessionID)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3615)externalbrowserbaseSessionID

* **get browserbaseSessionID(): undefined | string

- #### Returns undefined | string

### [**](#browserbaseSessionURL)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3616)externalbrowserbaseSessionURL

* **get browserbaseSessionURL(): undefined | string

- #### Returns undefined | string

### [**](#context)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3702)externalcontext

* **get context(): V3Context

- Expose the current CDP-backed context.

  ***

  #### Returns V3Context

### [**](#history)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3655)externalhistory

* **get history(): Promise\<readonly
  <!-- -->
  HistoryEntry\[]>

- Async property for history so callers can `await v3.history`. Returns a frozen copy to avoid external mutation.

  ***

  #### Returns Promise\<readonly<!-- --> HistoryEntry\[]>

### [**](#isBrowserbase)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3621)externalisBrowserbase

* **get isBrowserbase(): boolean

- Returns true if the browser is running on Browserbase.

  ***

  #### Returns boolean

### [**](#logger)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3709)externallogger

* **get logger(): (logLine) => void

- #### Returns (logLine) => void

  * * **(logLine): void

    - #### Parameters

      * ##### externallogLine: LogLine

      #### Returns void

### [**](#metrics)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3643)externalmetrics

* **get metrics(): Promise\<StagehandMetrics>

- Async property for metrics so callers can `await v3.metrics`. When using API mode, fetches metrics from the API. Otherwise returns local metrics.

  ***

  #### Returns Promise\<StagehandMetrics>

## Methods<!-- -->[**](#Methods)

### [**](#act)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3677)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3678)externalact

* ****act**(instruction, options): Promise<[ActResult](https://crawlee.dev/js/api/stagehand-crawler/interface/ActResult.md)>
* ****act**(action, options): Promise<[ActResult](https://crawlee.dev/js/api/stagehand-crawler/interface/ActResult.md)>

- Run an "act" instruction through the ActHandler.

  New API:

  * act(instruction: string, options?: ActOptions)
  * act(action: Action, options?: ActOptions)

  ***

  #### Parameters

  * ##### externalinstruction: string
  * ##### externaloptionaloptions: [ActOptions](https://crawlee.dev/js/api/stagehand-crawler/interface/ActOptions.md)

  #### Returns Promise<[ActResult](https://crawlee.dev/js/api/stagehand-crawler/interface/ActResult.md)>

### [**](#addToHistory)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3656)externaladdToHistory

* ****addToHistory**(method, parameters, result): void

- #### Parameters

  * ##### externalmethod: agent | act | extract | observe | navigate
  * ##### externalparameters: unknown
  * ##### externaloptionalresult: unknown

  #### Returns void

### [**](#agent)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3734)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3739)externalagent

* ****agent**(options): { execute: (instructionOrOptions) => Promise\<AgentStreamResult> }
* ****agent**(options): { execute: (instructionOrOptions) => Promise<[AgentResult](https://crawlee.dev/js/api/stagehand-crawler/interface/AgentResult.md)> }

- Create a v3 agent instance (AISDK tool-based) with execute(). Mirrors the v2 Stagehand.agent() tool mode (no CUA provider here).

  When stream: true, returns a streaming agent where execute() returns AgentStreamResult When stream is false/undefined, returns a non-streaming agent where execute() returns AgentResult

  ***

  #### Parameters

  * ##### externaloptions: [AgentConfig](https://crawlee.dev/js/api/stagehand-crawler.md#AgentConfig) & { stream: true }

  #### Returns { execute: (instructionOrOptions) => Promise\<AgentStreamResult> }

  * ##### externalexecute: (instructionOrOptions) => Promise\<AgentStreamResult>

    * * **(instructionOrOptions): Promise\<AgentStreamResult>

      - #### Parameters

        * ##### externalinstructionOrOptions: string | AgentStreamExecuteOptions

        #### Returns Promise\<AgentStreamResult>

### [**](#close)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3704)externalclose

* ****close**(opts): Promise\<void>

- Best-effort cleanup of context and launched resources.

  ***

  #### Parameters

  * ##### externaloptionalopts: { force?<!-- -->: boolean }
    * ##### externaloptionalforce: boolean

  #### Returns Promise\<void>

### [**](#connectURL)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3700)externalconnectURL

* ****connectURL**(): string

- Return the browser-level CDP WebSocket endpoint.

  ***

  #### Returns string

### [**](#extract)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3689)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3690)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3691)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3692)externalextract

* ****extract**(): Promise<{ pageText: string }>
* ****extract**(options): Promise<{ pageText: string }>
* ****extract**(instruction, options): Promise<{ extraction: string }>
* ****extract**\<T>(instruction, schema, options): Promise\<InferStagehandSchema\<T>>

- Run an "extract" instruction through the ExtractHandler.

  Accepted forms:

  * extract() → pageText
  * extract(options) → pageText
  * extract(instruction) → defaultExtractSchema
  * extract(instruction, schema) → schema-inferred
  * extract(instruction, schema, options)

  ***

  #### Returns Promise<{ pageText: string }>

### [**](#init)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3665)externalinit

* ****init**(): Promise\<void>

- Entrypoint: initializes handlers, launches Chrome or Browserbase, and sets up a CDP context.

  ***

  #### Returns Promise\<void>

### [**](#isAgentReplayActive)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3649)externalisAgentReplayActive

* ****isAgentReplayActive**(): boolean

- #### Returns boolean

### [**](#observe)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3696)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3697)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3698)externalobserve

* ****observe**(): Promise<[Action](https://crawlee.dev/js/api/stagehand-crawler/interface/Action.md)\[]>
* ****observe**(options): Promise<[Action](https://crawlee.dev/js/api/stagehand-crawler/interface/Action.md)\[]>
* ****observe**(instruction, options): Promise<[Action](https://crawlee.dev/js/api/stagehand-crawler/interface/Action.md)\[]>

- Run an "observe" instruction through the ObserveHandler.

  ***

  #### Returns Promise<[Action](https://crawlee.dev/js/api/stagehand-crawler/interface/Action.md)\[]>

### [**](#recordAgentReplayStep)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3650)externalrecordAgentReplayStep

* ****recordAgentReplayStep**(step): void

- #### Parameters

  * ##### externalstep: AgentReplayStep

  #### Returns void

### [**](#updateMetrics)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L3657)externalupdateMetrics

* ****updateMetrics**(functionName, promptTokens, completionTokens, reasoningTokens, cachedInputTokens, inferenceTimeMs): void

- #### Parameters

  * ##### externalfunctionName: V3FunctionName
  * ##### externalpromptTokens: number
  * ##### externalcompletionTokens: number
  * ##### externalreasoningTokens: number
  * ##### externalcachedInputTokens: number
  * ##### externalinferenceTimeMs: number

  #### Returns void
