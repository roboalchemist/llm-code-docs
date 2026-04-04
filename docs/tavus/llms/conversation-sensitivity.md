# Source: https://docs.tavus.io/sections/event-schemas/conversation-sensitivity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Sensitivity Interaction

> This is an event developers may broadcast to Tavus.

By broadcasting this event, you are able to update the VAD (Voice Activity Detection) sensitivity of the replica in
two dimensions. 
- `participant_pause_sensitivity`
- `participant_interrupt_sensitivity`

The supported values are `low`, `medium`, and `high`.

[Learn more about configuring the `sensitivity`](/sections/conversational-video-interface/persona/stt).


