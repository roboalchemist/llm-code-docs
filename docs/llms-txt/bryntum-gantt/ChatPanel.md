# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/chat/ChatPanel.md

# [ChatPanel](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanel)

A generic chat panel which displays chat bubbles from the local input or a remote data source such as an AI agent. The example below is not connected to a backend but will give you an idea of how easy it would be to let it drive an AI agent.

Basic configuration
-------------------

To preload the chat panel with a chat history, use [messages](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel#config-messages). You can set an [intro message](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel#config-intro), show an [avatar](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel#config-avatar) and set a [title](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel#config-title).

After the user adds a new message via the text input field, a [localMessage](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel#event-localMessage) event is fired. You can send this to your server, and once your remote chat service sends a message to the client, you can add it to the log using [addMessage](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel#function-addMessage).

```
const chatPanel = new ChatPanel({
    appendTo      : targetElement,
    title         : 'Acme Sales Support',
    async onLocalMessage({ text }){
         const
             response = await fetch('chatServer.php'),
             text = await response.text();

         this.addMessage({ fromOther : true, text });
    }
});
```

On remote speech bubbles, you can show a time stamp using [showTimestamp](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel#config-showTimestamp) and you can also define a list of action icons via [bubbleTools](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel#config-bubbleTools)

The text input field can be configured using the `items` object:

```
const chatPanel = new ChatPanel({
    appendTo      : targetElement,
    title         : 'Acme Sales Support',
    height        : '30em',
    showTimestamp : true,
    items : {
        messageField : {
            placeholder : 'Ask me anything'
        }
    }
});
```

Displaying selectable option chips
----------------------------------

A remote chat response can also present a list of actions, letting the user pick one before continuing the chat.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChatPanel](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanel#property-isChatPanel)
Identifies an object as an instance of [ChatPanel](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel) class, or subclass thereof.

[isChatPanel](https://bryntum.com/docs/gantt/api/Core/widget/chat/ChatPanel#property-isChatPanel-static)
Identifies an object as an instance of [ChatPanel](https://bryntum.com/docs/gantt/api/#Core/widget/chat/ChatPanel) class, or subclass thereof.
