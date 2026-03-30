# Quickstart

Get started with CopilotKit in under 5 minutes.

Copilot Cloud (Recommended)

Use our hosted backend endpoint to get started quickly.

Self-hosting

Learn to host CopilotKit's runtime yourself with your own backend.

## [Install CopilotKit](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted\#install-copilotkit-1)

First, install the latest packages for CopilotKit.

npmpnpmyarnbun

```
npm install @copilotkit/react-ui @copilotkit/react-core @copilotkit/runtime
```

## [Set up a Copilot Runtime Endpoint](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted\#set-up-a-copilot-runtime-endpoint)

##### Choose your provider:

![OpenAI logo](https://docs.copilotkit.ai/icons/openai.png)OpenAI

If you are planning to use a single LangGraph agent in [agent-lock mode](https://docs.copilotkit.ai/coagents/multi-agent-flows) as your agentic backend, your LLM adapter will only be used for peripherals such as suggestions, etc.

If you are not sure yet, simply ignore this note.

### [Add your API key](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted\#add-your-api-key)

Next, add your API key to your `.env` file in the root of your project (unless you prefer to provide it directly to the client):

.env

```
OPENAI_API_KEY=your_api_key_here
```

Please note that the code below uses GPT-4o, which requires a paid OpenAI API key. **If you are using a free OpenAI API key**, change the model to a different option such as `gpt-3.5-turbo`.

### [Setup the Runtime Endpoint](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted\#setup-the-runtime-endpoint)

### [Serverless Function Timeouts](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted\#serverless-function-timeouts)

When deploying to serverless platforms (Vercel, AWS Lambda, etc.), be aware that default function timeouts may be too short for CopilotKit's streaming responses:

- Vercel defaults: 10s (Hobby), 15s (Pro)
- AWS Lambda default: 3s

**Solution options:**

1. Increase function timeout:








```
// vercel.json
{
     "functions": {
       "api/copilotkit/**/*": {
         "maxDuration": 60
       }
     }
}
```

2. Use [Copilot Cloud](https://cloud.copilotkit.ai/) to avoid timeout issues entirely

Next.js App RouterNext.js Pages RouterNode.js ExpressNode.js HTTPNestJS

Create a new route to handle the `/api/copilotkit` endpoint.

app/api/copilotkit/route.ts

```
import {
  CopilotRuntime,
  OpenAIAdapter,
  copilotRuntimeNextJSAppRouterEndpoint,
} from '@copilotkit/runtime';

import { NextRequest } from 'next/server';


const serviceAdapter = new OpenAIAdapter();
const runtime = new CopilotRuntime();

export const POST = async (req: NextRequest) => {
  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime,
    serviceAdapter,
    endpoint: '/api/copilotkit',
  });

  return handleRequest(req);
};
```

Your Copilot Runtime endpoint should be available at `http://localhost:3000/api/copilotkit`.

## [Configure the CopilotKit Provider](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted\#configure-the-copilotkit-provider)

layout.tsx

```
import "./globals.css";
import { ReactNode } from "react";
import { CopilotKit } from "@copilotkit/react-core";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        {/* Make sure to use the URL you configured in the previous step  */}
        <CopilotKit runtimeUrl="/api/copilotkit">
          {children}
        </CopilotKit>
      </body>
    </html>
  );
}
```

## [Choose a Copilot UI](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted\#choose-a-copilot-ui-1)

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

* * *

## [Next Steps](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted\#next-steps)

🎉 Congrats! You've successfully integrated a fully functional chatbot in your application! Give it a try now and see it in action. Want to
take it further? Learn more about what CopilotKit has to offer!

[**Connecting Your Data** \\
Learn how to connect CopilotKit to your data, application state and user state.](https://docs.copilotkit.ai/guides/connect-your-data) [**Generative UI** \\
Learn how to render custom UI components directly in the CopilotKit chat window.](https://docs.copilotkit.ai/guides/generative-ui) [**Frontend Actions** \\
Learn how to allow your copilot to take applications on frontend.](https://docs.copilotkit.ai/guides/frontend-actions) [**CoAgents (LangGraph)** \\
Check out our section about CoAgents, our approach to building agentic copilots and experiences.](https://docs.copilotkit.ai/coagents)

[Previous\\
\\
Introduction](https://docs.copilotkit.ai/) [Next\\
\\
Customize UI](https://docs.copilotkit.ai/guides/custom-look-and-feel)

### On this page

[Install CopilotKit](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted#install-copilotkit) [Get a Copilot Cloud Public API Key](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted#get-a-copilot-cloud-public-api-key) [Setup the CopilotKit Provider](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted#setup-the-copilotkit-provider) [Choose a Copilot UI](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted#choose-a-copilot-ui) [Install CopilotKit](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted#install-copilotkit-1) [Set up a Copilot Runtime Endpoint](https://docs.copilotkit.ai/direct-to-llm/guides/quickstart?copilot-hosting=self-hosted#set-up-a-copilot-runtime-endpoint) [Configure the CopilotKit Provider](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted#configure-the-copilotkit-provider) [Choose a Copilot UI](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted#choose-a-copilot-ui-1) [Next Steps](https://docs.copilotkit.ai/quickstart?copilot-hosting=self-hosted#next-steps)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/quickstart.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Connect Your Data
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageAdd the data to the Copilot

[Connecting Your Data](https://docs.copilotkit.ai/guides/connect-your-data)