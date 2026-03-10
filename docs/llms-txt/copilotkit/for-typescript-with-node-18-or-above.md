# For TypeScript with Node 18 or above
npx @langchain/langgraph-cli dev --host localhost --port 8000
```

After starting the LangGraph server, the deployment URL will be `http://localhost:8000`.

### Having trouble?

Choose your connection method

Now you need to connect your LangGraph agent to CopilotKit.

Copilot Cloud (Recommended)

I want to host my Copilot on Copilot Cloud

Self-Hosted Copilot Runtime

I want to self-host the Copilot Runtime

### [Add a remote endpoint for your LangGraph agent](https://docs.copilotkit.ai/coagents/quickstart/langgraph\#add-a-remote-endpoint-for-your-langgraph-agent)

Using Copilot Cloud, you need to connect a remote endpoint that will connect to your LangGraph agent.

Local (LangGraph Studio)Self hosted (FastAPI)LangGraph Platform

When running your LangGraph agent locally, you can open a tunnel to it so Copilot Cloud can connect to it.
First, make sure you're logged in to [Copilot Cloud](https://cloud.copilotkit.ai/), and then authenticate the CLI by running:

```
npx copilotkit@latest login
```

Once authenticated, run:

```
npx copilotkit@latest dev --port 8000
```

### [Setup your CopilotKit provider](https://docs.copilotkit.ai/coagents/quickstart/langgraph\#setup-your-copilotkit-provider)

The [`<CopilotKit>`](https://docs.copilotkit.ai/reference/components/CopilotKit) component must wrap the Copilot-aware parts of your application. For most use-cases,
it's appropriate to wrap the CopilotKit provider around the entire app, e.g. in your layout.tsx.

Since we're using Copilot Cloud, we need to grab our public API key from the [Copilot Cloud dashboard](https://cloud.copilotkit.ai/).

layout.tsx

```
import "./globals.css";
import { ReactNode } from "react";
import { CopilotKit } from "@copilotkit/react-core";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        {/* Use the public api key you got from Copilot Cloud  */}
        <CopilotKit
          publicApiKey="<your-copilot-cloud-public-api-key>"
          agent="sample_agent" // the name of the agent you want to use
        >
          {children}
        </CopilotKit>
      </body>
    </html>
  );
}
```

Looking for a way to run multiple LangGraph agents? Check out our [Multi-Agent](https://docs.copilotkit.ai/coagents/multi-agent-flows) guide.

## [Choose a Copilot UI](https://docs.copilotkit.ai/coagents/quickstart/langgraph\#choose-a-copilot-ui)

You are almost there! Now it's time to setup your Copilot UI.

First, import the default styles in your root component (typically `layout.tsx`) :

```
import "@copilotkit/react-ui/styles.css";
```

Copilot UI ships with a number of built-in UI patterns, choose whichever one you like.

CopilotPopupCopilotSidebarCopilotChatHeadless UI

`CopilotPopup` is a convenience wrapper for `CopilotChat` that lives at the same level as your main content in the view hierarchy. It provides **a floating chat interface** that can be toggled on and off.

![Popup Example](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/popup-example.gif)

```
import { CopilotPopup } from "@copilotkit/react-ui";

export function YourApp() {
  return (
    <>
      <YourMainContent />
      <CopilotPopup
        instructions={"You are assisting the user as best as you can. Answer in the best way possible given the data you have."}
        labels={{
          title: "Popup Assistant",
          initial: "Need any help?",
        }}
      />
    </>
  );
}
```

### [🎉 Talk to your agent!](https://docs.copilotkit.ai/coagents/quickstart/langgraph\#-talk-to-your-agent)

Congrats! You've successfully integrated a LangGraph agent chatbot to your application. To start, try asking a few questions to your agent.

```
Can you tell me a joke?
```

```
Can you help me understand AI?
```

```
What do you think about React?
```

### Having trouble?

* * *

## [What's next?](https://docs.copilotkit.ai/coagents/quickstart/langgraph\#whats-next)

You've now got a LangGraph agent running in CopilotKit! Now you can start exploring the various ways that CopilotKit
can help you build power agent native applications.

[**Implement Human in the Loop** \\
Allow your users and agents to collaborate together on tasks.](https://docs.copilotkit.ai/coagents/human-in-the-loop) [**Utilize the Shared State** \\
Learn how to synchronize your agent's state with your UI's state, and vice versa.](https://docs.copilotkit.ai/coagents/shared-state) [**Add some generative UI** \\
Render your agent's progress and output in the UI.](https://docs.copilotkit.ai/coagents/generative-ui) [**Setup frontend actions** \\
Give your agent the ability to call frontend tools, directly updating your application.](https://docs.copilotkit.ai/coagents/frontend-actions)

[Previous\\
\\
Introduction](https://docs.copilotkit.ai/coagents) [Next\\
\\
Chat with an Agent](https://docs.copilotkit.ai/coagents/agentic-chat-ui)

### On this page

[Prerequisites](https://docs.copilotkit.ai/coagents/quickstart/langgraph#prerequisites) [Getting started](https://docs.copilotkit.ai/coagents/quickstart/langgraph#getting-started) [Install CopilotKit](https://docs.copilotkit.ai/coagents/quickstart/langgraph#install-copilotkit) [Clone the coagents-starter repo and install dependencies:](https://docs.copilotkit.ai/coagents/quickstart/langgraph#clone-the-coagents-starter-repo-and-install-dependencies) [Install dependencies:](https://docs.copilotkit.ai/coagents/quickstart/langgraph#install-dependencies) [Install dependencies:](https://docs.copilotkit.ai/coagents/quickstart/langgraph#install-dependencies-1) [Create a .env file](https://docs.copilotkit.ai/coagents/quickstart/langgraph#create-a-env-file) [Add your API keys](https://docs.copilotkit.ai/coagents/quickstart/langgraph#add-your-api-keys) [Start your LangGraph Agent](https://docs.copilotkit.ai/coagents/quickstart/langgraph#start-your-langgraph-agent) [Add a remote endpoint for your LangGraph agent](https://docs.copilotkit.ai/coagents/quickstart/langgraph#add-a-remote-endpoint-for-your-langgraph-agent) [Setup your CopilotKit provider](https://docs.copilotkit.ai/coagents/quickstart/langgraph#setup-your-copilotkit-provider) [Install Copilot Runtime](https://docs.copilotkit.ai/coagents/quickstart/langgraph#install-copilot-runtime) [Setup a Copilot Runtime Endpoint](https://docs.copilotkit.ai/coagents/quickstart/langgraph#setup-a-copilot-runtime-endpoint) [Add your LangGraph deployment to Copilot Runtime](https://docs.copilotkit.ai/coagents/quickstart/langgraph#add-your-langgraph-deployment-to-copilot-runtime) [Configure the CopilotKit Provider](https://docs.copilotkit.ai/coagents/quickstart/langgraph#configure-the-copilotkit-provider) [Choose a Copilot UI](https://docs.copilotkit.ai/coagents/quickstart/langgraph#choose-a-copilot-ui) [🎉 Talk to your agent!](https://docs.copilotkit.ai/coagents/quickstart/langgraph#-talk-to-your-agent) [What's next?](https://docs.copilotkit.ai/coagents/quickstart/langgraph#whats-next)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/quickstart/langgraph.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CrewAI Support
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageCopilot Infrastructure for CrewAI Crews