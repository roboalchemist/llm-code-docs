# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/feature/ai/apiPlugins/GooglePlugin.md

# [GooglePlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/GooglePlugin)

This plugin provides integration with Google's generative AI models.

A typical JSON request body looks like this:

```
{
     model : "gemini-1.5-pro",
     contents : [
         {
             role : "user",
             parts : [
                 { text : "Hello" }
             ]
         },
         {
             role : "model",
             parts : [
                 { text : "Hi there" }
             ]
         }
     ]
     systemInstruction : {
         parts : [
             { text : "You are a helpful assistant" }
         ]
     },
     tools : [
         {
             functionDeclarations : [
                 {
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
                 }
             ]
         }
     ],
     generationConfig : {
         temperature : 0
     }
}
```

A typical text response looks like this

```
{
  candidates : [
     {
         role : "model",
         content : {
             parts : [
                 { text : "Hello! How can I assist you today" }
             ]
         }
     }
   ],
}
```

A typical function call response looks like this

```
{
 candidates : [
    {
         role : "model",
         content : {
             parts : [
                 {
                     functionCall : {
                         name : "add",
                         args : { a : 1, b : 2 }
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
     role : "user",
     parts : [
         {
             functionResult : {
                 name : "add",
                 response : "3"
             }
         }
     ]
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGooglePlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/GooglePlugin#property-isGooglePlugin)
Identifies an object as an instance of [GooglePlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/GooglePlugin) class, or subclass thereof.

[isGooglePlugin](https://bryntum.com/docs/gantt/api/Core/feature/ai/apiPlugins/GooglePlugin#property-isGooglePlugin-static)
Identifies an object as an instance of [GooglePlugin](https://bryntum.com/docs/gantt/api/#Core/feature/ai/apiPlugins/GooglePlugin) class, or subclass thereof.
