# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/conversation-blocks/client-events.md

# Client Events

Client Events allow you to control the UI state of the chatbot such as opening/closing minimizing and much more.

### Minimize Chatbot

This client event can be used at any point in a chatbot to minimize the chatbot widget. This event can be used in multiple ways such as minimizing the chatbot window upon the chat completion so that users know that they have reached the end of the conversation. This is a [reference video](https://www.loom.com/share/5d504a0d3c994ece8836538e80cb4b61) of its working.

### Maximize Chatbot

This client event is used to maximize/open the chatbot window from a point where the window is in a minimized state/closed. This is a [video](https://www.loom.com/share/1e9a7fdbfc094c238342331024e9d145?sid=dc8e91d9-e889-4001-a23b-b84a4cb43707) of it’s working.

### Show Close Button

The above client event can be used to show an ‘X’  symbol on the top right corner of the chatbot window for the users to be able to end the chat once the resolution has been provided or incase the user wants to restart a fresh conversation with the chatbot. This also comes handy in between conversational flows where we can enable or disable it for certain steps per need basis. Here is a [reference video](https://www.loom.com/share/442ec5e6b168425cb7990f6d0c7d1ead?sid=a333b8ef-57ef-4fa1-b16d-9547eeec6761) of it’s working.

### Hide Close Button

The ‘Hide Close Button’ event can be used anywhere in the chatbot wherein the client doesn’t want the users to be able to end the chat for example a step which is mandatory to move forward in the chatbot conversation. Triggering this event will remove the ‘X’ symbol from the top right corner of the chatbot window this refraining the users from ending the chat. You can find the reference [video here](https://www.loom.com/share/bc674131acf3492e953c4b4ec6ad98cb?sid=49ffb6d4-f2ed-49f7-9d00-f5d2d9f37f7d).

### Show Escape Hatch

In case a user does not find the required topic/solution on the chatbot, they can use the escape hatch which appears on the bottom most part of the chatbot window to land on a specific page/window or as configured by the client. For example if the chatbot is designed to serve the technical queries and a user wants help on the sales part, we can configure this event to achieve so. Here is a [reference video](https://www.loom.com/share/dc8bb8d36f5248379f35b5f1e641b5b7?sid=d9cf9ba0-bf35-4821-8694-f76846c81d68) of its working.

### Hide Escape Hatch

This event in the chatbot when triggered hides the escape hatch phrase so that the users are not diverted out of the chatbot in case the solution is present within the chatbot. This can be used by us as per our need in the conversational flow to help users maintain the continuity in the flow inturn yielding to a solution. [Click here](https://www.loom.com/share/74a6ea1276b94c8db26133b3148e7eb7?sid=0330472e-18d3-4dff-8aaa-c6e9e0e74cd6) to check out the reference video.

### Show Restart Button

An event which when triggered allows a user to restart the conversation from any point through a conversation. A dedicated button shows up on the top  right corner of the chatbot window allowing the user to click on it and in turn restarting the conversation. For instance, this feature becomes very handy in cases where a user wants to explore various services offered by the chatbot to better understand and decide the course of action. Please check the reference [video here](https://www.loom.com/share/080d5f7b49744e99940f111a9a2817a7?sid=bd544447-34ff-4103-b599-7f100f4b9e91)

### Hide Restart Button

The event which when triggered can be used to hide the ‘Restart Conversation Button’ from the top right corner of the chatbot thus restricting the users from restarting the conversation from any point in the flow. This will allow the chatbot to keep the users streamlined to the intended solution and hence providing a better resolution rate. Please find the video [reference here](https://www.loom.com/share/ef5f21c6ac864f9790fdd87ab530a62f?sid=a4094af8-d30d-4352-9c1b-830b977b10ad).
