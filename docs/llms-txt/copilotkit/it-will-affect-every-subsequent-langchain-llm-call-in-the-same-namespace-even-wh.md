# it will affect every subsequent LangChain LLM call in the same namespace, even when `config` is not explicitly provided
response = await model2.ainvoke(*state["messages"]) # implicitly uses the modified config!
```

[Previous\\
\\
Using Agent Execution Parameters](https://docs.copilotkit.ai/coagents/advanced/adding-runtime-configuration) [Next\\
\\
Manually emitting messages](https://docs.copilotkit.ai/coagents/advanced/emit-messages)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming#implementation) [Disable all streaming](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming#disable-all-streaming)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/advanced/disabling-state-streaming.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Integrate Your LLM
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this page