# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/ChatMessageModel.md

# [ChatMessageModel](https://bryntum.com/docs/gantt/api/Core/data/ChatMessageModel)

A ChatMessageModel defines a message in the [ChatPanel](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel) widget.

## Fields

Fields belong to a Model class and define the Model data structure

[fromOther](https://bryntum.com/docs/gantt/api/Core/data/ChatMessageModel#field-fromOther)
A boolean indicating the source of the message. `true` if it's a remote message, `false` for a local message

[text](https://bryntum.com/docs/gantt/api/Core/data/ChatMessageModel#field-text)
The message text

[options](https://bryntum.com/docs/gantt/api/Core/data/ChatMessageModel#field-options)
An array of strings to present to the user in the UI. After user picks a value, the conversation can continue.

[timestamp](https://bryntum.com/docs/gantt/api/Core/data/ChatMessageModel#field-timestamp)
The timestamp of this message

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChatMessageModel](https://bryntum.com/docs/gantt/api/Core/data/ChatMessageModel#property-isChatMessageModel)
Identifies an object as an instance of [ChatMessageModel](https://bryntum.com/docs/gantt/api/#Core/data/ChatMessageModel) class, or subclass thereof.

[isChatMessageModel](https://bryntum.com/docs/gantt/api/Core/data/ChatMessageModel#property-isChatMessageModel-static)
Identifies an object as an instance of [ChatMessageModel](https://bryntum.com/docs/gantt/api/#Core/data/ChatMessageModel) class, or subclass thereof.
