# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/gpt-info.md

# gptInfo

Information related to GPT-generated content for an issue.

### Examples

```graphql
type GPTInfo {
  gptResponse: String
  user: String
  createdAt: Date
}
```

### Fields

| Field                | Description                               | Supported fields |
| -------------------- | ----------------------------------------- | ---------------- |
| gptResponse `String` | Response text from GPT                    |                  |
| user `String`        | User who requested or interacted with GPT |                  |
| createdAt `Date`     | Date when the GPT response was created    |                  |

### References

#### Fields with this object

* [{} Issue.gptInfo](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
