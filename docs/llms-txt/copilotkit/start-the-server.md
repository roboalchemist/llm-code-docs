# Start the server
poetry run demo
```

This will start a local agent server that you can connect to.

Choose your connection method

Now you need to connect your CrewAI Flow to CopilotKit.

Copilot Cloud (Recommended)

I want to host my Copilot on Copilot Cloud

Self-Hosted Copilot Runtime

I want to self-host the Copilot Runtime

### [Add a remote endpoint for your CrewAI Flow](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai\#add-a-remote-endpoint-for-your-crewai-flow)

Using Copilot Cloud, you need to connect a remote endpoint that will connect to your CrewAI Flow.

Self hosted (FastAPI)CrewAI Enterprise

**Running your FastAPI server in production**

Head over to [Copilot Cloud](https://cloud.copilotkit.ai/) sign up and setup a remote endpoint with the following information:

- OpenAI API key
- Your FastAPI server URL

**Running your FastAPI server locally**

If you're running your FastAPI server locally, you can open a tunnel to it so Copilot Cloud can connect to it.

```
npx copilotkit@latest dev --port 8000
```

### [Setup your CopilotKit provider](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai\#setup-your-copilotkit-provider)

The [`<CopilotKit>`](https://docs.copilotkit.ai/reference/components/CopilotKit) component must wrap the Copilot-aware parts of your application. For most use-cases,
it's appropriate to wrap the CopilotKit provider around the entire app, e.g. in your layout.tsx.

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

Looking for a way to run multiple CrewAI Flows? Check out our [Multi-Agent](https://docs.copilotkit.ai/crewai-flows/multi-agent-flows) guide.

### [Setup the Copilot UI](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai\#setup-the-copilot-ui)

The last step is to use CopilotKit's UI components to render the chat interaction with your agent. In most situations,
this is done alongside your core page components, e.g. in your `page.tsx` file.

page.tsx

```

import "@copilotkit/react-ui/styles.css";
import { CopilotPopup } from "@copilotkit/react-ui";

export function YourApp() {
  return (
    <main>
      <h1>Your main content</h1>

      <CopilotPopup
        labels={{
            title: "Popup Assistant",
            initial: "Hi! I'm connected to an agent. How can I help?",
        }}
      />
    </main>
  );
}
```

Looking for other chat component options? Check out our [Agentic Chat UI](https://docs.copilotkit.ai/crewai-flows/agentic-chat-ui) guide.

### [🎉 Talk to your agent!](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai\#-talk-to-your-agent)

Congrats! You've successfully integrated a CrewAI Flow chatbot to your application. To start, try asking a few questions to your agent.

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

## [What's next?](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai\#whats-next)

You've now got a CrewAI Flow running in CopilotKit! Now you can start exploring the various ways that CopilotKit
can help you build power agent native applications.

[**Implement Human in the Loop** \\
Allow your users and agents to collaborate together on tasks.](https://docs.copilotkit.ai/crewai-flows/human-in-the-loop) [**Utilize the Shared State** \\
Learn how to synchronize your agent's state with your UI's state, and vice versa.](https://docs.copilotkit.ai/crewai-flows/shared-state) [**Add some generative UI** \\
Render your agent's progress and output in the UI.](https://docs.copilotkit.ai/crewai-flows/generative-ui) [**Setup frontend actions** \\
Give your agent the ability to call frontend tools, directly updating your application.](https://docs.copilotkit.ai/crewai-flows/frontend-actions)

[Previous\\
\\
Introduction](https://docs.copilotkit.ai/crewai-flows) [Next\\
\\
Chat with an Agent](https://docs.copilotkit.ai/crewai-flows/agentic-chat-ui)

### On this page

[Prerequisites](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#prerequisites) [Getting started](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#getting-started) [Install CopilotKit](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#install-copilotkit) [Clone the coagents-starter repo](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#clone-the-coagents-starter-repo) [Create a .env file](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#create-a-env-file) [Add your API keys](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#add-your-api-keys) [Launch your local agent](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#launch-your-local-agent) [Add a remote endpoint for your CrewAI Flow](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#add-a-remote-endpoint-for-your-crewai-flow) [Setup your CopilotKit provider](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#setup-your-copilotkit-provider) [Install Copilot Runtime](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#install-copilot-runtime) [Setup a Copilot Runtime Endpoint](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#setup-a-copilot-runtime-endpoint) [Add your CrewAI Flow deployment to Copilot Runtime](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#add-your-crewai-flow-deployment-to-copilot-runtime) [Configure the CopilotKit Provider](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#configure-the-copilotkit-provider) [Setup the Copilot UI](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#setup-the-copilot-ui) [🎉 Talk to your agent!](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#-talk-to-your-agent) [What's next?](https://docs.copilotkit.ai/crewai-flows/quickstart/crewai#whats-next)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/crewai-flows/quickstart/crewai.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CopilotKit Configuration Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageMessage Streaming