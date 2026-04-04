# Customize Instructions

Learn how to customize the behavior of your AI assistant.

There are three main ways to customize the behavior of your AI assistant:

- [Appending to the prompt](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior#appending-to-the-prompt-recommended)
- [Passing the `instructions` parameter](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior#passing-the-instructions-parameter)
- [Overwriting the default `makeSystemMessage`)](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior#overwriting-the-default-makesystemmessage-not-recommended)

## [Appending to the prompt (Recommended)](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior\#appending-to-the-prompt-recommended)

CopilotKit provides the [useCopilotAdditionalInstructions](https://docs.copilotkit.ai/reference/hooks/useCopilotAdditionalInstructions) hook which allows you to add content to the prompt with whatever
you want.

Home.tsx

```
import { CopilotKit, useCopilotAdditionalInstructions } from "@copilotkit/react-core";
import { CopilotPopup } from "@copilotkit/react-ui"

function Chat() {
  useCopilotAdditionalInstructions({
    instructions: "Do not answer questions about the weather.",
  });
  return <CopilotPopup />
}

export function Home() {
  return (
    <CopilotKit>
      <Chat />
    </CopilotKit>
  )
}
```

You can even conditionally add instructions based on the application's state.

Home.tsx

```
function Chat() {
  const [showWeather, setShowWeather] = useState(false);

  useCopilotAdditionalInstructions({
    instructions: "Do not answer questions about the weather.",
    available: showWeather ? "enabled" : "disabled"
  }, showWeather);
}
```

## [Advanced](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior\#advanced)

If appending to the prompt is not enough, you have some other options, specifically around updating the prompt directly.

### [Passing the `instructions` parameter](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior\#passing-the-instructions-parameter)

The `instructions` parameter is the recommended way to customize AI assistant behavior. It will remain compatible with performance optimizations to the CopilotKit platform.

It can be customized for **Copilot UI** as well as **programmatically**:

Copilot UIHeadless UI

Copilot UI components accept an `instructions` property:

CustomCopilot.tsx

```
import { CopilotChat } from "@copilotkit/react-ui";

<CopilotChat
  instructions="You are a helpful assistant specializing in tax preparation. Provide concise and accurate answers to tax-related questions."
  labels={{
    title: "Tax Preparation Assistant",
    initial: "How can I help you with your tax preparation today?",
  }}
/>
```

### [Overwriting the default system message](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior\#overwriting-the-default-system-message)

For cases requiring complete control over the system message, you can use the `makeSystemMessage` function. We highly recommend reading CopilotKit's default system message before deciding to overwrite it, which can be found [here](https://github.com/CopilotKit/CopilotKit/blob/e48a34a66bb4dfd210e93dc41eee7d0f22d1a0c4/CopilotKit/packages/react-core/src/hooks/use-copilot-chat.ts#L240-L258).

This approach is **not recommended** as it may interfere with more advanced optimizations made by CopilotKit. **Only use this approach if the other options are not enough.**

Copilot UIHeadless UI

```
import { CopilotChat } from "@copilotkit/react-ui";

const CustomCopilot: React.FC = () => (
  <CopilotChat
    instructions="You are a knowledgeable tax preparation assistant. Provide accurate and concise answers to tax-related questions, guiding users through the tax filing process."
    labels={{
      title: "Tax Preparation Assistant",
      initial: "How can I assist you with your taxes today?",
    }}
    makeSystemMessage={myCustomTaxSystemMessage}
  />
);
```

[Previous\\
\\
Remote Endpoint (LangGraph Platform)](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint) [Next\\
\\
Authenticated Actions](https://docs.copilotkit.ai/guides/authenticated-actions)

### On this page

[Appending to the prompt (Recommended)](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior#appending-to-the-prompt-recommended) [Advanced](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior#advanced) [Passing the instructions parameter](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior#passing-the-instructions-parameter) [Overwriting the default system message](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior#overwriting-the-default-system-message)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/custom-ai-assistant-behavior.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Loading Agent State
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageSetting the threadId

Persistence