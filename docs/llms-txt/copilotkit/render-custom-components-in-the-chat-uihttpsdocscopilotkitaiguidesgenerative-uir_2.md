# [Render custom components in the chat UI](https://docs.copilotkit.ai/guides/generative-ui?ref=hackernoon.com\#render-custom-components-in-the-chat-ui)

When a user interacts with your Copilot, you may want to render a custom UI component. [`useCopilotAction`](https://docs.copilotkit.ai/reference/hooks/useCopilotAction) allows to give the LLM the
option to render your custom component through the `render` property.

Render a componentFetch data & renderrenderAndWaitForResponse (HITL)Render stringsCatch all renders

[`useCopilotAction`](https://docs.copilotkit.ai/reference/hooks/useCopilotAction) can be used with a `render` function and without a `handler` to display information or UI elements within the chat.

Here's an example to render a calendar meeting.

![Example of render-only Copilot action](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/render-only-example.png)

```
"use client" // only necessary if you are using Next.js with the App Router.
import { useCopilotAction } from "@copilotkit/react-core";

export function YourComponent() {
  useCopilotAction({
    name: "showCalendarMeeting",
    description: "Displays calendar meeting information",
    parameters: [\
      {\
        name: "date",\
        type: "string",\
        description: "Meeting date (YYYY-MM-DD)",\
        required: true\
      },\
      {\
        name: "time",\
        type: "string",\
        description: "Meeting time (HH:mm)",\
        required: true\
      },\
      {\
        name: "meetingName",\
        type: "string",\
        description: "Name of the meeting",\
        required: false\
      }\
    ],

    render: ({ status, args }) => {
      const { date, time, meetingName } = args;

      if (status === 'inProgress') {
        return <LoadingView />; // Your own component for loading state
      } else {
        const meetingProps: CalendarMeetingCardProps = {
          date: date,
          time,
          meetingName
        };
        return <CalendarMeetingCardComponent {...meetingProps} />;
      }
    },
  });

  return (
    <>...</>
  );
}
```

### What do the different status states mean?

### Why do I need "use client" in Next.js with the App Router?

## [Test it out!](https://docs.copilotkit.ai/guides/generative-ui?ref=hackernoon.com\#test-it-out)

After defining the action with a render method, ask the copilot to perform the task. For example, you can now ask the copilot to "show tasks" and see the custom UI component rendered in the chat interface.

You can read more about the `useCopilotAction` hook
[here](https://docs.copilotkit.ai/reference/hooks/useCopilotAction).

[Previous\\
\\
Backend Data](https://docs.copilotkit.ai/guides/connect-your-data/backend) [Next\\
\\
Frontend Actions](https://docs.copilotkit.ai/guides/frontend-actions)

### On this page

[Render custom components in the chat UI](https://docs.copilotkit.ai/guides/generative-ui?ref=hackernoon.com#render-custom-components-in-the-chat-ui) [Test it out!](https://docs.copilotkit.ai/guides/generative-ui?ref=hackernoon.com#test-it-out)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/generative-ui.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Agentic Generative UI
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

[Generative UI](https://docs.copilotkit.ai/coagents/generative-ui)