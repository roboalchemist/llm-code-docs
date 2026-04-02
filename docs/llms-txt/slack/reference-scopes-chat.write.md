Source: https://docs.slack.dev/reference/scopes/chat.write

# chat:write scope

Send messages as your Slack app

## Facts

## Supported token types

[`Bot`](/authentication/tokens#bot)

[`User`](/authentication/tokens#user)

## Compatible API methods

[`assistant.threads.setStatus`](/reference/methods/assistant.threads.setstatus)

[`chat.delete`](/reference/methods/chat.delete)

[`chat.deleteScheduledMessage`](/reference/methods/chat.deletescheduledmessage)

[`chat.meMessage`](/reference/methods/chat.memessage)

[`chat.postEphemeral`](/reference/methods/chat.postephemeral)

[`chat.postMessage`](/reference/methods/chat.postmessage)

[`chat.scheduleMessage`](/reference/methods/chat.schedulemessage)

[`chat.update`](/reference/methods/chat.update)

## Usage info {#usage-info}

For [Slack apps](/quickstart), `chat:write` replaces both `chat:write:user` and `chat:write:bot`. [Here's a bit more detail on why perspectival scopes are disappearing.](/legacy/legacy-app-migration/differences-between-classic-apps-and-granular-slack-apps#perspective)
