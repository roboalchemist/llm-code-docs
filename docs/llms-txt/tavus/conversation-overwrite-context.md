# Source: https://docs.tavus.io/sections/event-schemas/conversation-overwrite-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Overwrite Conversational Context Interaction

> This is an event developers may broadcast to Tavus.

By broadcasting this event, you are able to overwrite the `conversational_context` that the replica uses to generate responses. 

If `conversational_context` was not provided during conversation creation, the replica will start using the `context` you provide in this event as `conversational_context`.

<a href="/api-reference/conversations/create-conversation" target="_blank">Learn more about configuring the `conversational_context`</a>.


