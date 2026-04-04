# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/feature/ai/apiPlugins/AnthropicPlugin.md

# [AnthropicPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AnthropicPlugin)

This plugin provides integration with Anthropic's generative AI models.

A typical JSON request body looks like this:

```
{
     model : "claude-opus-4-1-20250805",
     max_tokens : 10000,
     temperature : 0,
     messages : [
         {
             role : "user",
             content : "Hello"
         },
         {
             role : "assistant",
             content : "Hi there"
         }
     ]
     system : [
         { type : "text", text : "You are a helpful assistant" }
     ],
     tools : [
         {
             name : "add",
             description : "Add two numbers",
             input_schema : {
                 type : "object",
                 properties : {
                     a : { type : "number", description : "First number" },
                     b : { type : "number", description : "Second number" }
                 },
                 required : ["a", "b"]
             }
         }
     ]
}
```

A typical text response looks like this

```
{
  role : "assistant"
  content : [
     {
         type : "text",
         text : "Hello! How can I assist you today"
     }
   ]
}
```

A typical function call response looks like this

```
{
 role : "assistant",
 content : [
     { type : "text", text : "Let me add those numbers for you" },
     {
         type :" tool_use",
         id : "unique id",
         name : "add",
         input : { a : 1, b : 2 }
     }
    ]
}
```

And the function call response from the tool should look like this:

```
{
     role : "user",
     content : [
         {
             type : "tool_result",
             tool_use_id : "unique id",
             content : "3"
         }
     ]
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAnthropicPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AnthropicPlugin#property-isAnthropicPlugin)
Identifies an object as an instance of [AnthropicPlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/AnthropicPlugin) class, or subclass thereof.

[isAnthropicPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/AnthropicPlugin#property-isAnthropicPlugin-static)
Identifies an object as an instance of [AnthropicPlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/AnthropicPlugin) class, or subclass thereof.
