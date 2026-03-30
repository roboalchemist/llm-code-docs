# useCopilotChat

`useCopilotChat` is a React hook that lets you directly interact with the
Copilot instance. Use to implement a fully custom UI (headless UI) or to
programmatically interact with the Copilot instance managed by the default
UI.

## [Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotChat\#usage)

### [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotChat\#simple-usage)

```
import { useCopilotChat } from "@copilotkit/react-core";
import { Role, TextMessage } from "@copilotkit/runtime-client-gql";

export function YourComponent() {
  const { appendMessage } = useCopilotChat();

  appendMessage(
    new TextMessage({
      content: "Hello World",
      role: Role.User,
    }),
  );

  // optionally, you can append a message without running chat completion
  appendMessage(yourMessage, { followUp: false });
}
```

`useCopilotChat` returns an object with the following properties:

```
const {
  visibleMessages, // An array of messages that are currently visible in the chat.
  appendMessage, // A function to append a message to the chat.
  setMessages, // A function to set the messages in the chat.
  deleteMessage, // A function to delete a message from the chat.
  reloadMessages, // A function to reload the messages from the API.
  stopGeneration, // A function to stop the generation of the next message.
  reset, // A function to reset the chat.
  isLoading, // A boolean indicating if the chat is loading.
} = useCopilotChat();
```

## [Parameters](https://docs.copilotkit.ai/reference/hooks/useCopilotChat\#parameters)

idstring

A unique identifier for the chat. If not provided, a random one will be
generated. When provided, the `useChat` hook with the same `id` will
have shared states across components.

headersRecord<string, string> \| Headers

HTTP headers to be sent with the API request.

initialMessagesMessage\[\]

System messages of the chat. Defaults to an empty array.

makeSystemMessageSystemMessageFunction

A function to generate the system message. Defaults to `defaultSystemMessage`.

[Previous\\
\\
useCopilotAdditionalInstructions](https://docs.copilotkit.ai/reference/hooks/useCopilotAdditionalInstructions) [Next\\
\\
useCopilotChatSuggestions](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions)

### On this page

[Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotChat#usage) [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotChat#simple-usage) [Parameters](https://docs.copilotkit.ai/reference/hooks/useCopilotChat#parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/hooks/useCopilotChat.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Human-in-the-Loop Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

[Human in the Loop (HITL)](https://docs.copilotkit.ai/coagents/human-in-the-loop)