# CopilotKit

The CopilotKit provider component, wrapping your application.

This component will typically wrap your entire application (or a sub-tree of your application where you want to have a copilot). It provides the copilot context to all other components and hooks.

## [Example](https://docs.copilotkit.ai/reference/components/CopilotKit\#example)

You can find more information about self-hosting CopilotKit [here](https://docs.copilotkit.ai/guides/self-hosting).

```
import { CopilotKit } from "@copilotkit/react-core";

<CopilotKit runtimeUrl="<your-runtime-url>">
  // ... your app ...
</CopilotKit>
```

## [Properties](https://docs.copilotkit.ai/reference/components/CopilotKit\#properties)

publicApiKeystring

Your Copilot Cloud API key. Don't have it yet? Go to [https://cloud.copilotkit.ai](https://cloud.copilotkit.ai/) and get one for free.

guardrails\_c{ validTopics?: string\[\]; invalidTopics?: string\[\]; }

Restrict input to specific topics using guardrails.
@remarks

This feature is only available when using CopilotKit's hosted cloud service. To use this feature, sign up at [https://cloud.copilotkit.ai](https://cloud.copilotkit.ai/) to get your publicApiKey. The feature allows restricting chat conversations to specific topics.

runtimeUrlstring

The endpoint for the Copilot Runtime instance. [Click here for more information](https://docs.copilotkit.ai/concepts/copilot-runtime).

transcribeAudioUrlstring

The endpoint for the Copilot transcribe audio service.

textToSpeechUrlstring

The endpoint for the Copilot text to speech service.

headersRecord<string, string>

Additional headers to be sent with the request.

For example:

```
{
  "Authorization": "Bearer X"
}
```

childrenReactNoderequired

The children to be rendered within the CopilotKit.

propertiesRecord<string, any>

Custom properties to be sent with the request
For example:

```
{
  'user_id': 'users_id',
}
```

credentialsRequestCredentials

Indicates whether the user agent should send or receive cookies from the other domain
in the case of cross-origin requests.

showDevConsoleboolean \| 'auto'

Whether to show the dev console.

If set to "auto", the dev console will be show on localhost only.

agentstring

The name of the agent to use.

forwardedParametersPick<ForwardedParametersInput, 'temperature'>

The forwarded parameters to use for the task.

authConfig\_c{ SignInComponent: React.ComponentType<{ onSignInComplete: (authState: AuthState) => void; }>; }

The auth config to use for the CopilotKit.
@remarks

This feature is only available when using CopilotKit's hosted cloud service. To use this feature, sign up at [https://cloud.copilotkit.ai](https://cloud.copilotkit.ai/) to get your publicApiKey. The feature allows restricting chat conversations to specific topics.

threadIdstring

The thread id to use for the CopilotKit.

mcpEndpointsArray<{ endpoint: string; apiKey?: string }>

Config for connecting to Model Context Protocol (MCP) servers.
Enables CopilotKit runtime to access tools on external MCP servers.

This config merges into the `properties` object with each request as `mcpEndpoints`.
It offers a typed method to set up MCP endpoints for requests.

Each array item should have:

- `endpoint`: MCP server URL (mandatory).
- `apiKey`: Optional API key for server authentication.

Note: A `createMCPClient` function is still needed during runtime initialization to manage these endpoints.

[Previous\\
\\
CopilotTextarea](https://docs.copilotkit.ai/reference/components/CopilotTextarea) [Next\\
\\
useCopilotReadable](https://docs.copilotkit.ai/reference/hooks/useCopilotReadable)

### On this page

[Example](https://docs.copilotkit.ai/reference/components/CopilotKit#example) [Properties](https://docs.copilotkit.ai/reference/components/CopilotKit#properties)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/components/CopilotKit.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Frontend Actions Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?