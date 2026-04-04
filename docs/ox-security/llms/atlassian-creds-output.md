# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/atlassian-creds-output.md

# atlassianCredsOutput

Atlassian-specific credential fields.

### Examples

```graphql
type AtlassianCredsOutput {
  organizationId: String
  apiKey: String
}
```

### Fields

| Field                   | Description                          | Supported fields |
| ----------------------- | ------------------------------------ | ---------------- |
| organizationId `String` | Organization identifier in Atlassian |                  |
| apiKey `String`         | API key for Atlassian services       |                  |

### References

#### Fields with this object

* [{} ExtraOptionalCreds.atlassian](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/extra-optional-creds)
