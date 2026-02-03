# Source: https://docs.tavus.io/sections/event-schemas/conversation-replica-started-stopped-speaking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Replica Started/Stopped Speaking Event

> This is an event broadcasted by Tavus.

A `replica.started_speaking/stopped_speaking event` is broadcasted by Tavus at specific times: 

`conversation.replica.started_speaking` means the replica has just started speaking.

`conversation.replica.stopped_speaking` means the replica has just stopped speaking.

When the `replica.stopped_speaking` event is sent, a `duration` field will be included in the event's `properties` object, indicating how long the replica was speaking for in seconds. This value may also be null.

These events are intended to act as triggers for actions within your application. For instance, you may want to
start a video or show a slide at times related to when the replica started or stopped speaking.

The `inference_id` can be used to correlate other events and tie things like `conversation.utterance or tool_call`
together.


