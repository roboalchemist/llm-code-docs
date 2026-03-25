iced
# Module event 
Source 
## Enums§
EventA user interface event.StatusThe status of an `Event` after being processed.
## Functions§
listenReturns a `Subscription` to all the ignored runtime events.listen_rawCreates a `Subscription` that produces a message for every runtime event,
including the redraw request events.listen_withCreates a `Subscription` that listens and filters all the runtime events
with the provided function, producing messages accordingly.