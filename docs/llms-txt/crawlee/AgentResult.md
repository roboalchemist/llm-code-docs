# Source: https://crawlee.dev/js/api/stagehand-crawler/interface/AgentResult.md

# externalAgentResult<!-- -->

## Index[**](#Index)

### Properties

* [**actions](#actions)
* [**completed](#completed)
* [**message](#message)
* [**messages](#messages)
* [**metadata](#metadata)
* [**success](#success)
* [**usage](#usage)

## Properties<!-- -->[**](#Properties)

### [**](#actions)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L2931)externalactions

**actions: AgentAction\[]

### [**](#completed)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L2932)externalcompleted

**completed: boolean

### [**](#message)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L2930)externalmessage

**message: string

### [**](#messages)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L2946)externaloptionalmessagesexperimental

**messages?

<!-- -->

: ModelMessage\[]

The conversation messages from this execution. Pass these to a subsequent execute() call via the `messages` option to continue the conversation.

### [**](#metadata)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L2933)externaloptionalmetadata

**metadata?

<!-- -->

: Record\<string, unknown>

### [**](#success)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L2929)externalsuccess

**success: boolean

### [**](#usage)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@browserbasehq/stagehand/src/index.d.ts#L2934)externaloptionalusage

**usage?

<!-- -->

: { cached\_input\_tokens?

<!-- -->

: number; inference\_time\_ms: number; input\_tokens: number; output\_tokens: number; reasoning\_tokens?

<!-- -->

: number }

#### Type declaration

* ##### externaloptionalcached\_input\_tokens?<!-- -->: number
* ##### externalinference\_time\_ms: number
* ##### externalinput\_tokens: number
* ##### externaloutput\_tokens: number
* ##### externaloptionalreasoning\_tokens?<!-- -->: number
