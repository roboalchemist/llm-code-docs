# Threads

Learn how to load chat messages and threads within the CopilotKit framework.

LangGraph supports threads, a way to group messages together and ultimately maintain a continuous chat history. CopilotKit
provides a few different ways to interact with this concept.

This guide assumes you have already gone through the [quickstart](https://docs.copilotkit.ai/quickstart) guide.

## [Loading an Existing Thread](https://docs.copilotkit.ai/coagents/persistence/loading-message-history\#loading-an-existing-thread)

To load an existing thread in CopilotKit, you can simply set the `threadId` property on `<CopilotKit>` like so.

When using LangGraph platform, the `threadId` must be a UUID.

```
import { CopilotKit } from "@copilotkit/react-core";

<CopilotKit threadId="37aa68d0-d15b-45ae-afc1-0ba6c3e11353">
  <YourApp />
</CopilotKit>
```

## [Dynamically Switching Threads](https://docs.copilotkit.ai/coagents/persistence/loading-message-history\#dynamically-switching-threads)

You can also make the `threadId` dynamic. Once it is set, CopilotKit will load the previous messages for that thread.

```
import { useState } from "react";
import { CopilotKit } from "@copilotkit/react-core";

const Page = () => {
  const [threadId, setThreadId] = useState("af2fa5a4-36bd-4e02-9b55-2580ab584f89");
  return (
    <CopilotKit threadId={threadId}>
      <YourApp setThreadId={setThreadId} />
    </CopilotKit>
  )
}

const YourApp = ({ setThreadId }) => {
  return (
    <Button onClick={() => setThreadId("679e8da5-ee9b-41b1-941b-80e0cc73a008")}>
      Change Thread
    </Button>
  )
}
```

## [Using setThreadId](https://docs.copilotkit.ai/coagents/persistence/loading-message-history\#using-setthreadid)

CopilotKit will also return the current `threadId` and a `setThreadId` function from the `useCopilotContext` hook. You can use `setThreadId` to change the `threadId`.

```
import { useCopilotContext } from "@copilotkit/react-core";

const ChangeThreadButton = () => {
  const { threadId, setThreadId } = useCopilotContext();
  return (
    <Button onClick={() => setThreadId("d73c22f3-1f8e-4a93-99db-5c986068d64f")}>
      Change Thread
    </Button>
  )
}
```

[Previous\\
\\
Loading Agent State](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state) [Next\\
\\
Message Persistence](https://docs.copilotkit.ai/coagents/persistence/message-persistence)

### On this page

[Loading an Existing Thread](https://docs.copilotkit.ai/coagents/persistence/loading-message-history#loading-an-existing-thread) [Dynamically Switching Threads](https://docs.copilotkit.ai/coagents/persistence/loading-message-history#dynamically-switching-threads) [Using setThreadId](https://docs.copilotkit.ai/coagents/persistence/loading-message-history#using-setthreadid)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/persistence/loading-message-history.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Human-in-the-Loop Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is Human-in-the-Loop (HITL)?