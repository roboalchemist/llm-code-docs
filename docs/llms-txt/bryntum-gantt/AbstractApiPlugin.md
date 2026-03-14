# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/feature/ai/apiPlugins/AbstractApiPlugin.md

# [AbstractApiPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin)

Abstract base class for AI API integration plugins.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAbstractApiPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#property-isAbstractApiPlugin)
Identifies an object as an instance of [AbstractApiPlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/AbstractApiPlugin) class, or subclass thereof.

[isAbstractApiPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#property-isAbstractApiPlugin-static)
Identifies an object as an instance of [AbstractApiPlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/AbstractApiPlugin) class, or subclass thereof.

[isApiPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#property-isApiPlugin)
Indicates that this class is an AI API plugin.

## Functions

Functions are methods available for calling on the class

[extractMessage](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#function-extractMessage)
Extracts the message from the AI response, converting it to the format expected by the AI feature. This method must be implemented by subclasses.

[beforePost](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#function-beforePost)
Converts the body content of the fetch request to match the API's expected format. This method must be implemented by subclasses. The body object must be modified in place.

[beforeApplyTrainingData](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#function-beforeApplyTrainingData)
Converts training data to match the API's expected format before applying it. This method must be implemented by subclasses. The trainingData array must be modified in place.

## Typedefs

Typedefs are type definitions for the class

[AIMessage](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#typedef-AIMessage)
Represents a complete message send by the AI API

[AIToolCall](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#typedef-AIToolCall)
Represents a tool call sent by the AI API

[AIFetchBody](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#typedef-AIFetchBody)
An object which will form the body content of the fetch call to the configured promptUrl

[AITool](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#typedef-AITool)
An object describing an AI tool

[AITrainingDataEntry](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AbstractApiPlugin#typedef-AITrainingDataEntry)
Contains an array of messages forming a training example
