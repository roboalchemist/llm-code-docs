# Anonymous Telemetry

We use anonymous telemetry (metadata-only) to learn how to improve CopilotKit.

- Open-source telemetry is **completely anonymous**
- We **do not collect any data** about end-users (the users interacting with your copilot)
- We **do not collect any application data** flowing through your system, only CopilotKit metadata
- We do not sell or share any data with third parties
- We do not use cookies or trackers in open-source telemetry
- To minimize the frequency of data sent, we apply batching and sampling to telemetry

## [How to opt out of anonymous telemetry](https://docs.copilotkit.ai/telemetry\#how-to-opt-out-of-anonymous-telemetry)

You can opt out of open-source telemetry in multiple ways.

In CopilotRuntime, simply set `COPILOTKIT_TELEMETRY_DISABLED=true`. We also respect [Do Not Track (DNT)](https://consoledonottrack.com/).

Alternatively, you can directly set the `telemetryDisabled` flag to `true` when configuring your Copilot Runtime endpoint.

## [How to adjust telemetry sample rate](https://docs.copilotkit.ai/telemetry\#how-to-adjust-telemetry-sample-rate)

The default sample rate is `0.05` (5%). You can adjust it by setting the `COPILOTKIT_TELEMETRY_SAMPLE_RATE` to any value between 0 and 1.

## [Get in touch](https://docs.copilotkit.ai/telemetry\#get-in-touch)

If you have any questions or concerns, please reach out at [hello@copilotkit.ai](mailto:hello@copilotkit.ai).

[Previous\\
\\
Documentation Contributions](https://docs.copilotkit.ai/contributing/docs-contributions) [Next\\
\\
LangSmith](https://docs.copilotkit.ai/observability/langsmith)

### On this page

[How to opt out of anonymous telemetry](https://docs.copilotkit.ai/telemetry#how-to-opt-out-of-anonymous-telemetry) [How to adjust telemetry sample rate](https://docs.copilotkit.ai/telemetry#how-to-adjust-telemetry-sample-rate) [Get in touch](https://docs.copilotkit.ai/telemetry#get-in-touch)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/(other)/telemetry/index.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Shared State Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is shared state?