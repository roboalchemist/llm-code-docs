Source: https://docs.slack.dev/reference/events/message/reply_broadcast

# reply_broadcast message

### (No longer served) A message thread's reply was broadcast to a channel

## Facts

## Required Scopes

[`channels:history`](/reference/scopes/channels.history)

[`groups:history`](/reference/scopes/groups.history)

[`im:history`](/reference/scopes/im.history)

[`mpim:history`](/reference/scopes/mpim.history)

## Compatible APIs

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info {#usage-info}

The `reply_broadcast` message subtype is no longer served. It has been replaced with [`thread_broadcast`](/reference/events/message/thread_broadcast).

See [message threading](/messaging#threading) for more information.
