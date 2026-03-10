# Fully Headless UI

Fully customize your Copilot's UI from the ground up using headless UI

The built-in Copilot UI can be customized in many ways -- both through CSS and by passing in custom sub-components.

CopilotKit also offers **fully custom headless UI** through the `useCopilotChat` hook. Everything built with the built-in UI (and more) can be implemented with the headless UI, providing deep customizability.

```
import { useCopilotChat } from "@copilotkit/react-core";
import { Role, TextMessage } from "@copilotkit/runtime-client-gql";

export function CustomChatInterface() {
  const {
    visibleMessages,
    appendMessage,
    setMessages,
    deleteMessage,
    reloadMessages,
    stopGeneration,
    isLoading,
  } = useCopilotChat();

  const sendMessage = (content: string) => {
    appendMessage(new TextMessage({ content, role: Role.User }));
  };

  return (
    <div>
      {/* Implement your custom chat UI here */}
    </div>
  );
}
```

## [Resetting the chat history](https://docs.copilotkit.ai/guides/custom-look-and-feel/headless-ui\#resetting-the-chat-history)

In some cases, users may want to reset the chat to clear the conversation history and start fresh. This can be useful when:

- The current conversation has become too long or confusing.
- You want to test different prompts or approaches from a clean slate.
- A user needs to reset the context to ensure the AI responds appropriately.

This simple method allows you to reset the chat state with a button click.

Why Reset the Chat?

Resetting the chat clears all conversation history, helping you start fresh or troubleshoot AI responses.

PreviewCode

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/concepts/customize-look-and-feel/reset-chat.gif)

[Previous\\
\\
Custom Sub-Components](https://docs.copilotkit.ai/guides/custom-look-and-feel/bring-your-own-components) [Next\\
\\
Connecting Your Data](https://docs.copilotkit.ai/guides/connect-your-data)

### On this page

[Resetting the chat history](https://docs.copilotkit.ai/guides/custom-look-and-feel/headless-ui#resetting-the-chat-history)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/custom-look-and-feel/headless-ui.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Agent State Writing Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

[Shared State](https://docs.copilotkit.ai/coagents/shared-state)