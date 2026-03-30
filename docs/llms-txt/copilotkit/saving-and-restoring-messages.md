# Saving and restoring messages

Learn how to save and restore message history.

See [Loading Message History](https://docs.copilotkit.ai/coagents/persistence/loading-message-history) for an automated way to load the chat history.

As you're building agentic experiences, you may want to persist the user's chat history across runs.
One way to do this is through the use of `localstorage` where chat history is saved in the browser.
In this guide we demonstrate how you can store the state into `localstorage` and how it can be inserted
into the agent.

The following example shows how to save and restore your message history using `localStorage`:

```
import { useCopilotMessagesContext } from "@copilotkit/react-core";
import { ActionExecutionMessage, ResultMessage, TextMessage } from "@copilotkit/runtime-client-gql";

const { messages, setMessages } = useCopilotMessagesContext();

// save to local storage when messages change
useEffect(() => {
  if (messages.length !== 0) {
    localStorage.setItem("copilotkit-messages", JSON.stringify(messages));
  }
}, [JSON.stringify(messages)]);

// initially load from local storage
useEffect(() => {
  const messages = localStorage.getItem("copilotkit-messages");
  if (messages) {
    const parsedMessages = JSON.parse(messages).map((message: any) => {
      if (message.type === "TextMessage") {
        return new TextMessage({
          id: message.id,
          role: message.role,
          content: message.content,
          createdAt: message.createdAt,
        });
      } else if (message.type === "ActionExecutionMessage") {
        return new ActionExecutionMessage({
          id: message.id,
          name: message.name,
          scope: message.scope,
          arguments: message.arguments,
          createdAt: message.createdAt,
        });
      } else if (message.type === "ResultMessage") {
        return new ResultMessage({
          id: message.id,
          actionExecutionId: message.actionExecutionId,
          actionName: message.actionName,
          result: message.result,
          createdAt: message.createdAt,
        });
      } else {
        throw new Error(`Unknown message type: ${message.type}`);
      }
    });
    setMessages(parsedMessages);
  }
}, []);
```

[Previous\\
\\
Self Hosting (Copilot Runtime)](https://docs.copilotkit.ai/guides/self-hosting) [Next\\
\\
Overview](https://docs.copilotkit.ai/tutorials/ai-todo-app/overview)

### On this page

No Headings

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/messages-localstorage.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Copilot Suggestions Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageSimple Usage