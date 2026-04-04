# Source: https://docs.tavus.io/sections/event-schemas/conversation-toolcall.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Tool Call Event

> This is an event broadcasted by Tavus.

A tool call event denotes when an LLM tool call should be made on the client side. The event will contain the name and arguments of the function that should be called.

Tool call events can be used to call external APIs or databases.

> **Note**: it is the client's responsibility to take action on these tool calls, as Tavus will not execute code server-side.

For more details on LLM tool calls, please take a look [here](/sections/conversational-video-interface/persona/llm-tool).


