# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/chat/AIChatPanelMixin.md

# [AIChatPanelMixin](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin)

Mixin for AIChatPanel

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showReadAloud](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#config-showReadAloud)
Set to `true` to show an icon which reads the message back to the user.

[showConfidenceIndicator](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#config-showConfidenceIndicator)
Set to `true` to show an icon which displays the confidence level supplied by the AI.

[showRecordButton](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#config-showRecordButton)
Set to `true` to show a button in the message field which starts and stops microphone recording

[showCloseButton](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#config-showCloseButton)
Set to `true` to show a close button in the panel header which hides the chat panel when clicked.

[autoReadAloud](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#config-autoReadAloud)
Set to `true` to always read aloud received messages. Set to `false` to not read aloud responses to recorded messages. Defaults to `audio-input` which reads received messages aloud if they are a response to a local audio message.

[formatText](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#config-formatText)
Configure with a function that takes a string and returns a formatted string which will be rendered as message content. Defaults to a built-in simple Markdown parser.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[showReadAloud](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#property-showReadAloud)
Set to `true` to show an icon which reads the message back to the user.

[showConfidenceIndicator](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#property-showConfidenceIndicator)
Set to `true` to show an icon which displays the confidence level supplied by the AI.

[showRecordButton](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#property-showRecordButton)
Set to `true` to show a button in the message field which starts and stops microphone recording

[showCloseButton](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#property-showCloseButton)
Set to `true` to show a close button in the panel header which hides the chat panel when clicked.

[autoReadAloud](https://bryntum.com/docs/gantt/api/Core/widget/chat/AIChatPanelMixin#property-autoReadAloud)
Set to `true` to always read aloud received messages. Set to `false` to not read aloud responses to recorded messages. Defaults to `audio-input` which reads received messages aloud if they are a response to a local audio message.
