# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/feature/ai/apiPlugins/OpenAIPlugin.md

# [OpenAIPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/OpenAIPlugin)

This plugin provides integration with OpenAI's generative AI models.

A typical JSON request body looks like this:

```
{
     model : "gpt-4-1",
     temperature : 0,
     messages : [
         {
             role = "system",
             content = "You are a helpful assistant"
         }
         {
             role : "user",
             content : "Hello"
         },
         {
             role : "assistant",
             content : "Hi there"
         }
     ]
     tools : [
         {
             function : {
                 name : "add",
                 description : "Add two numbers",
                 parameters : {
                     type : "object",
                     properties : {
                         a : { type : "number", description : "First number" },
                         b : { type : "number", description : "Second number" }
                     },
                     required : ["a", "b"]
                 }
             },
             type : 'function',
             strict : false
         }
     ]
}
```

A typical text response looks like this

```
{
  choices : [
     {
         message : {
             role : "assistant",
             content : "Hello! How can I assist you today"
         }
     }
   ]
}
```

A typical function call response looks like this

```
{
 choices : [
    {
         message : {
             role : "assistant",
             tool_calls : [
                 {
                     id : "unique-id",
                     type : "function",
                     function : {
                         name : "add",
                         arguments : { a : 1, b : 2 }
                     }
                 }
             ]
         }
     }
    ]
}
```

And the function call response from the tool should look like this:

```
{
     role : "tool",
     content : "3",
     tool_call_id : "unique-id"
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isOpenAIPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/OpenAIPlugin#property-isOpenAIPlugin)
Identifies an object as an instance of [OpenAIPlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/OpenAIPlugin) class, or subclass thereof.

[isOpenAIPlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/OpenAIPlugin#property-isOpenAIPlugin-static)
Identifies an object as an instance of [OpenAIPlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/OpenAIPlugin) class, or subclass thereof.
