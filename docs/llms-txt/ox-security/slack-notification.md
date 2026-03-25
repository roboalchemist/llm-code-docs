# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/slack-notification.md

# slackNotification

Details about a Slack notification sent for the issue.

### Examples

```graphql
type SlackNotification {
  channelName: String
  timestamp: String
}
```

### Fields

| Field                | Description                                               | Supported fields |
| -------------------- | --------------------------------------------------------- | ---------------- |
| channelName `String` | Name of the Slack channel where the notification was sent |                  |
| timestamp `String`   | Timestamp of when the notification was sent               |                  |

### References

#### Fields with this object

* [{} Issue.slackNotification](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
