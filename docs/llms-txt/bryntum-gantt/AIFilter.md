# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/ai/AIFilter.md

# [AIFilter](https://bryntum.com/docs/gantt/api/Grid/feature/ai/AIFilter)

AI-powered filter feature for Grid. Allows users to type natural language queries to filter grid data.

Setup requires:

* A [promptUrl](https://bryntum.com/docs/gantt/api/#Grid/feature/ai/AIFilter#config-promptUrl) to which to send the prompt (typically your own backend service, which in turn forwards to an AI service)
* An [AIFilterField](https://bryntum.com/docs/gantt/api/#Grid/widget/AIFilterField) to input the prompt
* A configured [apiPlugin](https://bryntum.com/docs/gantt/api/#Grid/feature/ai/AIFilter#config-apiPlugin) to modify the prompt and process the response according to the API you are using (currently available: [OpenAIPlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/OpenAIPlugin), [GooglePlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/GooglePlugin) and [AnthropicPlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/AnthropicPlugin))
* Describe your model fields with the [description](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-description) property on data fields.

Example usage:

```
new Grid({
   features : {
     aiFilter : {
         promptUrl : '/ai/prompt',
         apiPlugin : OpenAIPlugin,
         model : 'gpt-4-1',
     }
   },
   tbar : [{
         type        : 'aifilterfield',
         width       : 400,
         placeholder : 'Ask AI to filter…'
   }],
   store : {
     fields : [
         { name : 'name', type : 'string', description : 'The name of the person' },
         { name : 'age', type : 'number', description : 'The age of the person' },
         { name : 'country', type : 'string', description : 'The country the person lives in' }
     ]
   }
})
```

This feature is **disabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[unsuccessfulFilterMessage](https://bryntum.com/docs/gantt/api/Grid/feature/ai/AIFilter#config-unsuccessfulFilterMessage)
The text to show in the toast when the text input did not result in any filter being applied

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAIFilter](https://bryntum.com/docs/gantt/api/Grid/feature/ai/AIFilter#property-isAIFilter)
Identifies an object as an instance of [AIFilter](https://bryntum.com/docs/gantt/api/#Grid/feature/ai/AIFilter) class, or subclass thereof.

[isAIFilter](https://bryntum.com/docs/gantt/api/Grid/feature/ai/AIFilter#property-isAIFilter-static)
Identifies an object as an instance of [AIFilter](https://bryntum.com/docs/gantt/api/#Grid/feature/ai/AIFilter) class, or subclass thereof.
