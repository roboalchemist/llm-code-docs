# Source: https://docs.lunary.ai/docs/integrations/javascript/custom-model.md

# Custom Models

If you're not using LangChain or OpenAI, you can still integrate Lunary with your own LLMs.

### Method 1: `wrapModel`

In addition to the `lunary.wrapAgent` & `lunary.wrapTool` methods, we provide a `wrapModel` method.

It allows to wrap any async function. It also takes the following options:

```ts  theme={null}
const wrapped = lunary.wrapModel(yourLlmModel, {
  nameParser: (args) => 'custom-model-1.3', // name of the model used
  inputParser: (args) => { // parse the input to message format
    return [{
      role: 'system',
      text: args.systemPrompt
    }, {
      role: 'user',
      text: args.userPrompt
    }]
  },
  extraParser: (args) => { // Report any extre properties like temperature
    return {
      temperature: args.temperature,
    }
  },
  outputParser: (result) => { // Parse the result
    return {
      role: 'ai',
      text: result.content,
    }
  },
  tokensUsageParser: async (result) => { // Return the number of tokens used
    return {
      completion: 10
      prompt: 10
    }
  },
})
```

### Method 2: `.trackEvent`

If you don't want to wrap your model, you can also use the `lunary.trackEvent` method.

First, track the start of your query:

```ts  theme={null}

// Report the start of the model
const runId = 'some-unique-id'
lunary.trackEvent('llm','start',{
  runId,
  name: 'custom-model-1.3',
  input: [{
    role: 'system',
    text: args.systemPrompt
  }, {
    role: 'user',
    text: args.userPrompt
  }],
  extra: {
    temperature: args.temperature,
  },
})

```

Run your model:

```ts  theme={null}
const result = await yourLlmModel('Hello!')
```

Then, track the result of your query:

```ts  theme={null}
lunary.trackEvent('llm','end',{
  runId,
  output: {
    role: 'ai',
    text: result.content,
  },
  tokensUsage: {
    completion: 10
    prompt: 10
  }
})
```

<Card title="Note">
  Input & output can be any object or array of object, however we recommend using the ChatMessage format:

  ```ts  theme={null}
  interface ChatMessage {
    role: "user" | "ai" | "system" | "function"
    text: string
    functions?: cJSON[]
    functionCall?: {
      name: string
      arguments: cJSON
    }
  }
  ```
</Card>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt