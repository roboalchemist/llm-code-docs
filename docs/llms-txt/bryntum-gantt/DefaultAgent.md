# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/feature/ai/agents/DefaultAgent.md

# [DefaultAgent](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent)

Base class for AI agents. Not to be used directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[promptUrl](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent#config-promptUrl)
The URL to send text prompts to

## Functions

Functions are methods available for calling on the class

[sendMessages](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent#function-sendMessages)
Builds and performs a post request to the specified [promptUrl](https://bryntum.com/docs/gantt/api/#Core/feature/ai/agents/DefaultAgent#config-promptUrl). Handles system messages and message history. On response, it calls [processResponse](https://bryntum.com/docs/gantt/api/#Core/feature/ai/agents/DefaultAgent#function-processResponse)

[prompt](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent#function-prompt)
Takes a prompt text and uses [sendMessages](https://bryntum.com/docs/gantt/api/#Core/feature/ai/agents/DefaultAgent#function-sendMessages) to send a post request. Performs highlighting afterward.

[processResponse](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent#function-processResponse)
Processes the response from the post request in [sendMessages](https://bryntum.com/docs/gantt/api/#Core/feature/ai/agents/DefaultAgent#function-sendMessages). Takes care of tool calling.

[validateToolArguments](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent#function-validateToolArguments)
Validates tool arguments against the tool's parameter schema. Returns an error message if validation fails, null otherwise.

[validateSchema](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent#function-validateSchema)
Recursively validates a value against a JSON schema.

[buildSchemaHint](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent#function-buildSchemaHint)
Builds a hint string showing the expected format based on a schema.

[generateTrainingData](https://bryntum.com/docs/gantt/api/Core/feature/ai/agents/DefaultAgent#function-generateTrainingData)
Returns an array of messages objects useful for generating trainingData
