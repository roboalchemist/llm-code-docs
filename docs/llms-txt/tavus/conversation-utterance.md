# Source: https://docs.tavus.io/sections/event-schemas/conversation-utterance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Utterance Event

> This is an event broadcasted by Tavus.

An utterance contains the content of the what was spoken and an indication of who spoke it (i.e. the user or replica). Each utterance event includes all of the words spoken by the user or replica measured from when the person started speaking to when they finished speaking. This could include multiple sentences or phrases.

Utterance events can be used to keep track of what the user or the replica has said.

To track when how long an utterance lasts, please refer to duration in "[User Started/Stopped Speaking](/sections/event-schemas/conversation-user-started-stopped-speaking)" and "[Replica Started/Stopped Speaking](/sections/event-schemas/conversation-replica-started-stopped-speaking)" events.


