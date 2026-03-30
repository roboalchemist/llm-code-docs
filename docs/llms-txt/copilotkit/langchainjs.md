# LangChain.js

Integrate LangChain JS chains as backend actions in your CopilotKit application.

### Find your CopilotRuntime

The starting point for this section is the `CopilotRuntime` you set up during quickstart (the CopilotKit backend endpoint).
For a refresher, see [Self-Hosting](https://docs.copilotkit.ai/guides/self-hosting) (or alternatively, revisit the [quickstart](https://docs.copilotkit.ai/quickstart)).

**First, find your `CopilotRuntime` instance in your code.** You can simply search your codebase for `CopilotRuntime`.

If you followed the quickstart, it'll be where you set up the `/api/copilotkit` endpoint.

### [Integrate LangChain JS actions with CopilotRuntime](https://docs.copilotkit.ai/guides/backend-actions/langchain-js-backend-actions\#integrate-langchain-js-actions-with-copilotruntime)

CopilotKit allows actions to return not only values but also LangChain streams. This means you can call LangChain chains directly and return their streams as part of your backend actions. Here's how to implement LangChain JS backend actions:

**Note** that `actions` is not merely an array of actions, but an array **generator**.
This generator takes `properties` and `url` as input.

This means you can **customize which backend actions are made available** according to the current frontend URL, as well as custom properties you can pass from the frontend.

/api/copilotkit/route.ts

```
import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";

const runtime = new CopilotRuntime({
  // ... existing configuration
  actions: ({properties, url}) => {
    // Note that actions returns not an array, but an array **generator**.
    // You can use the input parameters to the actions generator to expose different backend actions to the Copilot at different times:
    // `url` is the current URL on the frontend application.
    // `properties` contains custom properties you can pass from the frontend application.

    return [\
      {\
        name: "generateJokeForTopic",\
        description: "Generates a joke for a given topic.",\
        parameters: [\
          {\
            name: "topic",\
            type: "string",\
            description: "The topic to generate a joke about.",\
            required: true,\
          },\
        ],\
        handler: async ({topic}: {topic: string}) => {\
          const prompt = ChatPromptTemplate.fromMessages([\
            [\
              "system",\
              "You are a witty comedian. Generate a short, funny joke about the given topic. But make it sound like a pirate joke!",\
            ],\
            ["user", "Topic: {topic}"],\
          ]);\
          const chain = prompt.pipe(new ChatOpenAI());\
\
          return chain.stream({ // return directly chain.stream\
            topic: topic,\
          });\
        },\
      },\
    ]
  }
});

// ... rest of your route definition
```

### [Test your implementation](https://docs.copilotkit.ai/guides/backend-actions/langchain-js-backend-actions\#test-your-implementation)

After adding the LangChain JS action, test it by asking the copilot to generate a joke about a specific topic. Observe how it uses the LangChain components to generate and stream the response.

[Previous\\
\\
TypeScript (Node.js)](https://docs.copilotkit.ai/guides/backend-actions/typescript-backend-actions) [Next\\
\\
LangServe actions](https://docs.copilotkit.ai/guides/backend-actions/langserve-backend-actions)

### On this page

[Integrate LangChain JS actions with CopilotRuntime](https://docs.copilotkit.ai/guides/backend-actions/langchain-js-backend-actions#integrate-langchain-js-actions-with-copilotruntime) [Test your implementation](https://docs.copilotkit.ai/guides/backend-actions/langchain-js-backend-actions#test-your-implementation)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/backend-actions/langchain-js-backend-actions.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Read Agent State
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

[Shared State](https://docs.copilotkit.ai/coagents/shared-state)