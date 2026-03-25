# Source: https://docs.knock.app/api-reference/channels/bulk/update_message_status.md

### Bulk update message statuses for channel

Bulk update the status of messages for a specific channel. The channel is specified by the `channel_id` parameter. The action to perform is specified by the `action` parameter, where the action is a status change action (e.g. `archive`, `unarchive`).

**Endpoint:** `POST /v1/channels/{channel_id}/messages/bulk/{action}`

**Rate limit tier:** 2

