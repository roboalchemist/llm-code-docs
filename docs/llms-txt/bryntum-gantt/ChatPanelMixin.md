# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/chat/ChatPanelMixin.md

# [ChatPanelMixin](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin)

Mixin for [ChatPanel](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[avatar](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#config-avatar)
The path to an avatar to display at the top of the chat bubble area

[intro](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#config-intro)
An introductory text (or DomConfig) shown at the top of the chat bubble area

[messages](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#config-messages)
The initial messages to display in the chat bubble area (e.g. a bot greeting message "Hello, how may I help you?"

[bubbleTools](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#config-bubbleTools)
An array of `DomConfig` items to show tool icons associated with each remote speech bubble. Each tool can be clicked by the user to perform an action. Upon clicking a tool, the chat panel will trigger a {#event-bubbleToolClick} event with details.

[showTimestamp](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#config-showTimestamp)
Set to true to show a timestamp below each chat bubble

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChatPanelMixin](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#property-isChatPanelMixin)
Identifies an object as an instance of [ChatPanelMixin](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanelMixin) class, or subclass thereof.

[isChatPanelMixin](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#property-isChatPanelMixin-static)
Identifies an object as an instance of [ChatPanelMixin](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanelMixin) class, or subclass thereof.

[avatar](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#property-avatar)
The path to an avatar to display at the top of the chat bubble area

[intro](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#property-intro)
An introductory text (or DomConfig) shown at the top of the chat bubble area

[messages](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#property-messages)
The initial messages to display in the chat bubble area (e.g. a bot greeting message "Hello, how may I help you?"

[bubbleTools](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#property-bubbleTools)
An array of `DomConfig` items to show tool icons associated with each remote speech bubble. Each tool can be clicked by the user to perform an action. Upon clicking a tool, the chat panel will trigger a {#event-bubbleToolClick} event with details.

[showTimestamp](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#property-showTimestamp)
Set to true to show a timestamp below each chat bubble

[store](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#property-store)
A reference to the [data store](https://bryntum.com/docs/gantt/api/#Core/data/Store) storing all the chat messages.

## Functions

Functions are methods available for calling on the class

[addMessage](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#function-addMessage)
Add a message bubble to the chat log. Accepts data for the [ChatMessageModel](https://bryntum.com/docs/gantt/api/#Core/data/ChatMessageModel), or a Promise that later resolves to such data. When passed a promise, the bubble will show a loading indicator until resolved.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[localMessage](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#event-localMessage)
Fired when a client side message is added via the text input field (or by picking a predefined option bubble).

[bubbleToolClick](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanelMixin#event-bubbleToolClick)
Fired when chat bubble tool icon is clicked.
