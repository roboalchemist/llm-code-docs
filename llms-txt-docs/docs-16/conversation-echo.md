# Source: https://docs.tavus.io/sections/event-schemas/conversation-echo.md

# Echo Interaction

> This is an event developers may broadcast to Tavus.

By broadcasting this event, you are able to tell the replica what to exactly say. Anything that is passed in the `text` field will be spoken by the replica.

This is commonly used in combination with the [Interrupt Interaction](/sections/event-schemas/conversation-interrupt).


