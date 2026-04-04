# Guardrails  Cloud Only

## [Introduction](https://docs.copilotkit.ai/guides/guardrails\#introduction)

Copilot Cloud provides content moderation capabilities through the `guardrails_c` configuration, helping ensure safe and appropriate AI interactions. The system uses OpenAI's content moderation capabilities to enforce these guardrails.

This feature is only available with [Copilot Cloud](https://cloud.copilotkit.ai/).

## [Implementation](https://docs.copilotkit.ai/guides/guardrails\#implementation)

```
import { CopilotKit } from "@copilotkit/react-core";

export default function App() {
  return (
    <CopilotKit
      publicApiKey={process.env.COPILOTKIT_PUBLIC_API_KEY}
      guardrails_c={{
        // Topics to explicitly block
        invalidTopics: ["politics", "explicit-content", "harmful-content"],
        // Topics to explicitly allow
        validTopics: ["business", "technology", "general-assistance"],
      }}
    >
      {/* Your app */}
    </CopilotKit>
  );
}
```

[Previous\\
\\
Authenticated Actions](https://docs.copilotkit.ai/guides/authenticated-actions) [Next\\
\\
Copilot Suggestions](https://docs.copilotkit.ai/guides/copilot-suggestions)

### On this page

[Introduction](https://docs.copilotkit.ai/guides/guardrails#introduction) [Implementation](https://docs.copilotkit.ai/guides/guardrails#implementation)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/guardrails.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## LangSmith Observability
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this page

Observability