# useCopilotChatSuggestions

The useCopilotChatSuggestions hook generates suggestions in the chat window based on real-time app state.

useCopilotChatSuggestions is experimental. The interface is not final and
can change without notice.

`useCopilotReadable` is a React hook that provides app-state and other information
to the Copilot. Optionally, the hook can also handle hierarchical state within your
application, passing these parent-child relationships to the Copilot.

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/use-copilot-chat-suggestions/use-copilot-chat-suggestions.gif)

## [Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions\#usage)

### [Install Dependencies](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions\#install-dependencies)

This component is part of the [@copilotkit/react-ui](https://npmjs.com/package/@copilotkit/react-ui) package.

```
npm install @copilotkit/react-core @copilotkit/react-ui
```

### [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions\#simple-usage)

```
import { useCopilotChatSuggestions } from "@copilotkit/react-ui";

export function MyComponent() {
  const [employees, setEmployees] = useState([]);

  useCopilotChatSuggestions({
    instructions: `The following employees are on duty: ${JSON.stringify(employees)}`,
  });
}
```

### [Dependency Management](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions\#dependency-management)

```
import { useCopilotChatSuggestions } from "@copilotkit/react-ui";

export function MyComponent() {
  useCopilotChatSuggestions(
    {
      instructions: "Suggest the most relevant next actions.",
    },
    [appState],
  );
}
```

In the example above, the suggestions are generated based on the given instructions.
The hook monitors `appState`, and updates suggestions accordingly whenever it changes.

### [Behavior and Lifecycle](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions\#behavior-and-lifecycle)

The hook registers the configuration with the chat context upon component mount and
removes it on unmount, ensuring a clean and efficient lifecycle management.

## [Parameters](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions\#parameters)

instructionsstringrequired

A prompt or instructions for the GPT to generate suggestions.

minSuggestionsnumber

Default:"1"

The minimum number of suggestions to generate. Defaults to `1`.

maxSuggestionsnumber

Default:"1"

The maximum number of suggestions to generate. Defaults to `3`.

available'enabled' \| 'disabled'

Default:"enabled"

Whether the suggestions are available. Defaults to `enabled`.

classNamestring

An optional class name to apply to the suggestions.

[Previous\\
\\
useCopilotChat](https://docs.copilotkit.ai/reference/hooks/useCopilotChat) [Next\\
\\
useCoAgent](https://docs.copilotkit.ai/reference/hooks/useCoAgent)

### On this page

[Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions#usage) [Install Dependencies](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions#install-dependencies) [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions#simple-usage) [Dependency Management](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions#dependency-management) [Behavior and Lifecycle](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions#behavior-and-lifecycle) [Parameters](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions#parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/hooks/useCopilotChatSuggestions.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Anonymous Telemetry Management
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageHow to opt out of anonymous telemetry