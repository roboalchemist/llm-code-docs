# CopilotSidebar

The CopilotSidebar component, providing a sidebar interface for interacting with your copilot.

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/CopilotSidebar.gif)

A chatbot sidebar component for the CopilotKit framework. Highly customizable through various props and custom CSS.

See [CopilotPopup](https://docs.copilotkit.ai/reference/components/chat/CopilotPopup) for a popup version of this component.

## [Install Dependencies](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar\#install-dependencies)

This component is part of the [@copilotkit/react-ui](https://npmjs.com/package/@copilotkit/react-ui) package.

```
npm install @copilotkit/react-core @copilotkit/react-ui
```

## [Usage](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar\#usage)

```
import { CopilotSidebar } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

<CopilotSidebar
  labels={{
    title: "Your Assistant",
    initial: "Hi! 👋 How can I assist you today?",
  }}
>
  <YourApp/>
</CopilotSidebar>
```

### [Look & Feel](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar\#look--feel)

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

## [Properties](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar\#properties)

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

defaultOpenboolean

Default:"false"

Whether the chat window should be open by default.

clickOutsideToCloseboolean

Default:"true"

If the chat window should close when the user clicks outside of it.

hitEscapeToCloseboolean

Default:"true"

If the chat window should close when the user hits the Escape key.

shortcutstring

Default:"'/'"

The shortcut key to open the chat window.
Uses Command-\[shortcut\] on a Mac and Ctrl-\[shortcut\] on Windows.

onSetOpen(open: boolean) => void

A callback that gets called when the chat window opens or closes.

WindowReact.ComponentType<WindowProps>

A custom Window component to use instead of the default.

ButtonReact.ComponentType<ButtonProps>

A custom Button component to use instead of the default.

HeaderReact.ComponentType<HeaderProps>

A custom Header component to use instead of the default.

[Previous\\
\\
CopilotPopup](https://docs.copilotkit.ai/reference/components/chat/CopilotPopup) [Next\\
\\
CopilotTextarea](https://docs.copilotkit.ai/reference/components/CopilotTextarea)

### On this page

[Install Dependencies](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar#install-dependencies) [Usage](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar#usage) [Look & Feel](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar#look--feel) [Properties](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar#properties)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/components/chat/CopilotSidebar.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CrewAI Flows Quickstart
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pagePrerequisites