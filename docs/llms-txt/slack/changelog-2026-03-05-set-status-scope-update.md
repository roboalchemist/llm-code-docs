Source: https://docs.slack.dev/changelog/2026/03/05/set-status-scope-update

# Set status method scope update

March 5, 2026

The [`assistant.threads.setStatus`](/reference/methods/assistant.threads.setStatus) API method now accepts either the [`assistant:write`](/reference/scopes/assistant.write) or [`chat:write`](/reference/scopes/chat.write) scope. This allows channel-based apps to use [AI loading states](/ai/developing-agents#loading-states) in channels, without having to request `assistant:write` or use the AI assistant split view. The `assistant.threads.setStatus` API method will eventually no longer accept the `assistant:write` scope in favor of the `chat:write` scope exclusively, so update your app soon!

**Tags:**

* [Announcement](/changelog/tags/announcement)
