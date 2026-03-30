# Tool-based Generative UI

Render your agent's tool calls with custom UI components.

This video demonstrates the [implementation](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based#implementation) section applied
to our [coagents starter\\
project](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter-crewai-crews).

## [What is this?](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based\#what-is-this)

Tools are a way for the LLM to call predefined, typically, deterministic functions. CopilotKit allows you to render these tools in the UI
as a custom component, which we call **Generative UI**.

## [When should I use this?](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based\#when-should-i-use-this)

Rendering tools in the UI is useful when you want to provide the user with feedback about what your agent is doing, specifically
when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## [Implementation](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based\#implementation)

### [Run and connect your agent](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based\#run-and-connect-your-agent)

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already,
you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/crewai-crews/quickstart/crewai) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter-crewai-crews) as a starting point
as this guide uses it as a starting point.

### [Render the tool call in your frontend](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based\#render-the-tool-call-in-your-frontend)

In the case of CrewAI Crew agents, there is one tool call that indicates that the crew is being executed. It has the same name as the crew. In this example, the crew is named `research_crew`. To display progress of the crew, we just need to add a `useCopilotAction` hook to render the tool call in
the UI.

Important

In order to render a tool call in the UI, the name of the action must match
the name of the tool.

app/page.tsx

```
import { useCopilotAction } from "@copilotkit/react-core";
// ...

const YourMainContent = () => {
  // ...

  useCopilotAction({
    name: "research_crew",
    parameters: [\
      {\
        name: "topic",\
      },\
      {\
        name: "current_year",\
      },\
    ],
    render({ args, status }) {
      return (
        <div className="m-4 p-4 bg-gray-100 rounded shadow">
          <h1 className="text-center text-sm">
            Researching {args.topic} in {args.current_year}{" "}
            {status == "complete" ? "✅" : "⏳"}
          </h1>
        </div>
      );
    },
  });
  // ...
};
```

### [Give it a try!](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based\#give-it-a-try)

Try giving the crew enough information to complete the task, i.e. "Research the state of AI in 2025". You should see the custom UI component that we added render the tool call and display the arguments that were passed to the tool.

## [Rendering Arbitrary Tool Calls](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based\#rendering-arbitrary-tool-calls)

When working with agents, they may call tools that you haven't explicitly defined UI components for. You can use a catch-all action to render these tool calls:

```
import {
  useCopilotAction,
  CatchAllActionRenderProps,
} from "@copilotkit/react-core";

useCopilotAction({
  name: "*",
  followUp: false,
  render: ({ name, args, status, result }: CatchAllActionRenderProps<[]>) => {
    return (
      <div className="m-4 p-4 bg-gray-100 rounded shadow">
        <h2 className="text-sm font-medium">Tool: {name}</h2>
        <pre className="mt-2 text-xs overflow-auto">
          {JSON.stringify(args, null, 2)}
        </pre>
        {status === "complete" && (
          <div className="mt-2 text-xs text-green-600">✓ Complete</div>
        )}
      </div>
    );
  },
});
```

This will render any tool call that doesn't have a specific UI component defined for it, displaying the tool name, arguments, and completion status.

[Previous\\
\\
Agentic Generative UI](https://docs.copilotkit.ai/crewai-crews/generative-ui/agentic) [Next\\
\\
Human in the Loop (HITL)](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop)

### On this page

[What is this?](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based#what-is-this) [When should I use this?](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based#implementation) [Run and connect your agent](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based#run-and-connect-your-agent) [Render the tool call in your frontend](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based#render-the-tool-call-in-your-frontend) [Give it a try!](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based#give-it-a-try) [Rendering Arbitrary Tool Calls](https://docs.copilotkit.ai/crewai-crews/generative-ui/tool-based#rendering-arbitrary-tool-calls)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/crewai-crews/generative-ui/tool-based.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## LangGraph Platform Deployment
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageDeploy a Graph to LangGraph Platform

[Backend Actions & Agents](https://docs.copilotkit.ai/guides/backend-actions)