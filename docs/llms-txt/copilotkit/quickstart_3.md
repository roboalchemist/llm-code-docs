# Quickstart

Get started with CopilotKit in under 5 minutes.

Copilot Cloud (Recommended)

Use our hosted backend endpoint to get started quickly.

Self-hosting

Learn to host CopilotKit's runtime yourself with your own backend.

## [Install CopilotKit](https://docs.copilotkit.ai/quickstart?component=Headless+UI\#install-copilotkit)

First, install the latest packages for CopilotKit.

npmpnpmyarnbun

```
npm install @copilotkit/react-ui @copilotkit/react-core
```

## [Get a Copilot Cloud Public API Key](https://docs.copilotkit.ai/quickstart?component=Headless+UI\#get-a-copilot-cloud-public-api-key)

Navigate to [Copilot Cloud](https://cloud.copilotkit.ai/) and follow the instructions to get a public API key - it's free!

## [Setup the CopilotKit Provider](https://docs.copilotkit.ai/quickstart?component=Headless+UI\#setup-the-copilotkit-provider)

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
        <CopilotKit publicApiKey="<your-copilot-cloud-public-api-key>">
          {children}
        </CopilotKit>
      </body>
    </html>
  );
}
```

## [Choose a Copilot UI](https://docs.copilotkit.ai/quickstart?component=Headless+UI\#choose-a-copilot-ui)

You are almost there! Now it's time to setup your Copilot UI.

First, import the default styles in your root component (typically `layout.tsx`) :

```
import "@copilotkit/react-ui/styles.css";
```

Copilot UI ships with a number of built-in UI patterns, choose whichever one you like.

CopilotPopupCopilotSidebarCopilotChatHeadless UI

The built-in Copilot UI can be customized in many ways -- both through css and by passing in custom sub-components.

CopilotKit also offers **fully custom headless UI**, through the `useCopilotChat` hook. Everything built with the built-in UI (and more) can be implemented with the headless UI, providing deep customizability.

```
import { useCopilotChat } from "@copilotkit/react-core";
import { Role, TextMessage } from "@copilotkit/runtime-client-gql";

export function CustomChatInterface() {
  const {
    visibleMessages,
    appendMessage,
    setMessages,
    deleteMessage,
    reloadMessages,
    stopGeneration,
    isLoading,
  } = useCopilotChat();

  const sendMessage = (content: string) => {
    appendMessage(new TextMessage({ content, role: Role.User }));
  };

  return (
    <div>
      {/* Implement your custom chat UI here */}
    </div>
  );
}
```

* * *

## [Next Steps](https://docs.copilotkit.ai/quickstart?component=Headless+UI\#next-steps)

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

[Install CopilotKit](https://docs.copilotkit.ai/quickstart?component=Headless+UI#install-copilotkit) [Get a Copilot Cloud Public API Key](https://docs.copilotkit.ai/quickstart?component=Headless+UI#get-a-copilot-cloud-public-api-key) [Setup the CopilotKit Provider](https://docs.copilotkit.ai/quickstart?component=Headless+UI#setup-the-copilotkit-provider) [Choose a Copilot UI](https://docs.copilotkit.ai/quickstart?component=Headless+UI#choose-a-copilot-ui) [Install CopilotKit](https://docs.copilotkit.ai/quickstart?component=Headless+UI#install-copilotkit-1) [Set up a Copilot Runtime Endpoint](https://docs.copilotkit.ai/quickstart?component=Headless+UI#set-up-a-copilot-runtime-endpoint) [Configure the CopilotKit Provider](https://docs.copilotkit.ai/quickstart?component=Headless+UI#configure-the-copilotkit-provider) [Choose a Copilot UI](https://docs.copilotkit.ai/quickstart?component=Headless+UI#choose-a-copilot-ui-1) [Next Steps](https://docs.copilotkit.ai/quickstart?component=Headless+UI#next-steps)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/quickstart.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## LangGraph SDK Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pagecopilotkit\_customize\_config

Python