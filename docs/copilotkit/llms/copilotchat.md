# CopilotChat

The CopilotChat component, providing a chat interface for interacting with your copilot.

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/CopilotChat.gif)

A chatbot panel component for the CopilotKit framework. The component allows for a high degree
of customization through various props and custom CSS.

## [Install Dependencies](https://docs.copilotkit.ai/reference/components/chat/CopilotChat\#install-dependencies)

This component is part of the [@copilotkit/react-ui](https://npmjs.com/package/@copilotkit/react-ui) package.

```
npm install @copilotkit/react-core @copilotkit/react-ui
```

## [Usage](https://docs.copilotkit.ai/reference/components/chat/CopilotChat\#usage)

```
import { CopilotChat } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

<CopilotChat
  labels={{
    title: "Your Assistant",
    initial: "Hi! 👋 How can I assist you today?",
  }}
/>
```

### [Look & Feel](https://docs.copilotkit.ai/reference/components/chat/CopilotChat\#look--feel)

By default, CopilotKit components do not have any styles. You can import CopilotKit's stylesheet at the root of your project:

YourRootComponent.tsx

```
...
import "@copilotkit/react-ui/styles.css";

export function YourRootComponent() {
  return (
    <CopilotKit>
      ...
    </CopilotKit>
  );
}
```

For more information about how to customize the styles, check out the [Customize Look & Feel](https://docs.copilotkit.ai/guides/custom-look-and-feel/customize-built-in-ui-components) guide.

## [Properties](https://docs.copilotkit.ai/reference/components/chat/CopilotChat\#properties)

instructionsstring

Custom instructions to be added to the system message. Use this property to
provide additional context or guidance to the language model, influencing
its responses. These instructions can include specific directions,
preferences, or criteria that the model should consider when generating
its output, thereby tailoring the conversation more precisely to the
user's needs or the application's requirements.

onInProgress(inProgress: boolean) => void

A callback that gets called when the in progress state changes.

onSubmitMessage(message: string) => void \| Promise<void>

A callback that gets called when a new message it submitted.

onStopGenerationOnStopGeneration

A custom stop generation function.

onReloadMessagesOnReloadMessages

A custom reload messages function.

onRegenerate(messageId: string) => void

A callback function to regenerate the assistant's response

onCopy(message: string) => void

A callback function when the message is copied

onThumbsUp(message: string) => void

A callback function for thumbs up feedback

onThumbsDown(message: string) => void

A callback function for thumbs down feedback

iconsCopilotChatIcons

Icons can be used to set custom icons for the chat window.

labelsCopilotChatLabels

Labels can be used to set custom labels for the chat window.

makeSystemMessageSystemMessageFunction

A function that takes in context string and instructions and returns
the system message to include in the chat request.
Use this to completely override the system message, when providing
instructions is not enough.

AssistantMessageReact.ComponentType<AssistantMessageProps>

A custom assistant message component to use instead of the default.

UserMessageReact.ComponentType<UserMessageProps>

A custom user message component to use instead of the default.

MessagesReact.ComponentType<MessagesProps>

A custom Messages component to use instead of the default.

RenderMessageReact.ComponentType<RenderMessageProps>

A custom RenderMessage component to use instead of the default.

RenderActionExecutionMessageReact.ComponentType<RenderMessageProps>

A custom RenderActionExecutionMessage component to use instead of the default.

RenderAgentStateMessageReact.ComponentType<RenderMessageProps>

A custom RenderAgentStateMessage component to use instead of the default.

RenderResultMessageReact.ComponentType<RenderMessageProps>

A custom RenderResultMessage component to use instead of the default.

InputReact.ComponentType<InputProps>

A custom Input component to use instead of the default.

classNamestring

A class name to apply to the root element.

childrenReact.ReactNode

Children to render.

[Previous\\
\\
All Chat Components](https://docs.copilotkit.ai/reference/components/chat) [Next\\
\\
CopilotPopup](https://docs.copilotkit.ai/reference/components/chat/CopilotPopup)

### On this page

[Install Dependencies](https://docs.copilotkit.ai/reference/components/chat/CopilotChat#install-dependencies) [Usage](https://docs.copilotkit.ai/reference/components/chat/CopilotChat#usage) [Look & Feel](https://docs.copilotkit.ai/reference/components/chat/CopilotChat#look--feel) [Properties](https://docs.copilotkit.ai/reference/components/chat/CopilotChat#properties)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/components/chat/CopilotChat.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CrewAI Components Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

![CopilotKit Logo](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/copilotkit-logo.svg)