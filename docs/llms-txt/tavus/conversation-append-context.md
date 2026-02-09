# Source: https://docs.tavus.io/sections/event-schemas/conversation-append-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Append Conversational Context Interaction

> This is an event developers may broadcast to Tavus.

By broadcasting this event, you are able to append additional context to the existing `conversational_context` that the replica uses to generate responses. 

If `conversational_context` was not provided during conversation creation, the replica will start using the `context` you provide in this event as the initial `conversational_context`.

Learn more about the `conversational_context`: [Create Conversation](/api-reference/conversations/create-conversation)


