# Source: https://docs.tavus.io/sections/event-schemas/conversation-echo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Echo Interaction

> This is an event developers may broadcast to Tavus.

By broadcasting this event, you are able to tell the replica what to exactly say. Anything that is passed in the `text` field will be spoken by the replica.

This is commonly used in combination with the [Interrupt Interaction](/sections/event-schemas/conversation-interrupt).


