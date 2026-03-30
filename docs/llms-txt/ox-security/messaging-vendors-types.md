# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/messaging-vendors-types.md

# messagingVendorsTypes

Defines the supported messaging platforms for issue notifications and communications.

### Examples

```graphql
enum MessagingVendorsTypes {
  Slack
  Teams
}
```

### Enum values

| Enum value | Description                        |
| ---------- | ---------------------------------- |
| Slack      | Slack messaging platform           |
| Teams      | Microsoft Teams messaging platform |

### References

#### Fields with this object

* [{} IssueMessage.messagingVendor](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-message)
