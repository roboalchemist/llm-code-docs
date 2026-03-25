# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-message.md

# issueMessage

Message related to an issue, sent via a messaging vendor.

### Examples

```graphql
type IssueMessage {
  messagingVendor: MessagingVendorsTypes
  recipients: [Recipient]
  createdAt: Date
}
```

### Fields

| Field                                                                                                                                              | Description                                 | Supported fields                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------- |
| messagingVendor [`MessagingVendorsTypes`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/messaging-vendors-types) | Vendor/service used to send the message     |                                                                                          |
| recipients [`[Recipient]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/recipient)                            | List of recipients who received the message | <p>name <code>String!</code><br>id <code>String!</code><br>type <code>String!</code></p> |
| createdAt `Date`                                                                                                                                   | Date and time when the message was created  |                                                                                          |

### References

#### Fields with this object

* [{} Issue.messages](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
