# Source: https://docs.tavus.io/sections/event-schemas/conversation-user-started-stopped-speaking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# User Started/Stopped Speaking Event

> This is an event broadcasted by Tavus.

A `user.started_speaking/stopped_speaking event` is broadcasted by Tavus at specific times: 

`conversation.user.started_speaking` means the user has just started speaking.

`conversation.user.stopped_speaking` means the user has just stopped speaking.

These events are intended to act as triggers for actions within your application. For instance, you may want to
take some user facing action, or backend process at times related to when the user started or stopped speaking.

The `inference_id` can be used to correlate other events and tie things like `conversation.utterance` or `tool_call`
together. 

Keep in mind that with `speculative_inference`, the `inference_id` will frequently change while the user is speaking so
that the `user.started_speaking inference_id` will not usually match the `conversation.utterance inference_id`.


