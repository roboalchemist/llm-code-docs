# Source: https://docs.prefect.io/v3/api-ref/python/prefect-events-subscribers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# subscribers

# `prefect.events.subscribers`

Flow run subscriber that interleaves events and logs from a flow run

## Classes

### `FlowRunSubscriber` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/subscribers.py#L26" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Subscribes to both events and logs for a specific flow run, yielding them
in an interleaved stream.

This subscriber combines the event stream and log stream for a flow run into
a single async iterator. When a terminal event (Completed, Failed, or Crashed)
is received, the event subscription stops but log subscription continues for a
configurable timeout to catch any straggler logs.


Built with [Mintlify](https://mintlify.com).