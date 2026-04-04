# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/AI.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/AI.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/AI.md

# [AI](https://bryntum.com/docs/gantt/api/Gantt/feature/AI)

This feature provides an AI agent for the Gantt. It provides a chat panel that allows the user to send messages to the agent and see the responses. Which allows the user to use natural language to interact with the Gantt in different ways. For example, the user can ask the agent to filter the data, sort it, or select specific records. The agent can also perform data manipulation operations such as adding, updating, deleting records.

To use this feature, you need to provide a [promptUrl](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-promptUrl) to which the agent will send the prompts. On the other end of this URL, there should be a service that adds credentials to the request and forwards the prompt to the LLM API of your choice.

You also need to configure a [apiPlugin](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-apiPlugin) which ensures the prompt format matches the API you are using.

```
new Gantt({
  features : {
     ai : {
        promptUrl : '/ai/prompt',
        apiPlugin : OpenAIPlugin,
     }
  }
})
```

This is the minimum configuration required to get started, but you may also want to configure the following:

* [model](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-model) - Adds a model property to the prompt sent to the LLM API which is often required
* [chatButton](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-chatButton) - Change the appearance of the chat button and the chat panel
* [tools](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-tools) - Add custom tools to the agent's tool list, or remove existing unwanted tools
* [userSettings](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-userSettings) - Provide the current user's settings
* [userSettingsUpdate](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#event-userSettingsUpdate) - To listen for changes to the user's settings and save them

And for voice input/output, check out:

* [textToSpeechUrl](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-textToSpeechUrl) - To enable read aloud responses
* [transcribeUrl](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-transcribeUrl) - To enable voice input
* [voiceActivation](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI#config-voiceActivation) - Listens for voice commands which start a voice conversation with the agent

But these are not all configurations available. Check out the demo linked in the right panel for a full configuration example. And make sure to read this documentation to learn more about all available configurations.

This feature is **disabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[defaultRange](https://bryntum.com/docs/gantt/api/Gantt/feature/AI#config-defaultRange)
The date range to use for agent "conditions", when the user doesn't specify a given date range in the prompt. Available options are:

* `timeline` - Use the current timeline date range
* `in-view` - Use the current visible date range (scrolled in view)
* `all` - Use the entire date range of the Gantt

[tools](https://bryntum.com/docs/gantt/api/Gantt/feature/AI#config-tools)
Use this to add custom tools to the AI model's tool list or to remove existing tools. Provide an object with the tool names as keys and configuration objects as values. Please note that modifying existing tools is not supported, only removing them.

Specific tools for Gantt AI are:

* `getChildren` - Used by agent to retrieve child records for a parent Task
* `criticalPath` - Enables or disabled the [CriticalPaths](https://bryntum.com/docs/gantt/api/#Gantt/feature/CriticalPaths) feature
* `tableSections` - Expands or collapses the table sections
* `reloadGantt` - Reloads the Gantt data. Only available if the Gantt can be reloaded

Most tools from the [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/feature/AI#config-tools) are also available. But those tools that are related to the Scheduler's events will in Gantt be named according to the `TaskModel's` [$name](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#property-$name-static) property, or `Task` if that is not defined. These tools from the Scheduler are not available in the Gantt:

* `copyEvent`
* `getNextAvailableSlot`

Most tools from the [Grid](https://bryntum.com/docs/gantt/api/#Grid/feature/AI#config-tools) are also available. But those tools that are related to the Grid rows or records will in the Gantt be named according to the `ResourceModel's` [$name](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel#property-$name-static) property, or `Resource` if that is not defined. These tools from the Grid are not available in the Gantt:

* `selectRecords`

Also, the tools from [tools](https://bryntum.com/docs/gantt/api/#Core/feature/ai/AIBase#config-tools) are available

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAI](https://bryntum.com/docs/gantt/api/Gantt/feature/AI#property-isAI)
Identifies an object as an instance of [AI](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI) class, or subclass thereof.

[isAI](https://bryntum.com/docs/gantt/api/Gantt/feature/AI#property-isAI-static)
Identifies an object as an instance of [AI](https://bryntum.com/docs/gantt/api/#Gantt/feature/AI) class, or subclass thereof.
