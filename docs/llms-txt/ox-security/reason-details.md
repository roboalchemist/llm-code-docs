# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/reason-details.md

# reasonDetails

Detailed explanation of a reason with description and evidence.

### Examples

```graphql
type ReasonDetails {
  description: String
}
```

### Fields

| Field                | Description                               | Supported fields |
| -------------------- | ----------------------------------------- | ---------------- |
| description `String` | Textual description explaining the reason |                  |

### References

#### Fields with this object

* [{} Issue.resolvedReasonDetails](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
* [{} Issue.disappearedReasonDetails](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
