# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity-attributes.md

# serverlessDeploymentUserIdentityAttributes

Attributes of the session context for a serverless deployment.

### Examples

```graphql
type ServerlessDeploymentUserIdentityAttributes {
  creationDate: String
  mfaAuthenticated: String
}
```

### Fields

| Field                     | Description                                       | Supported fields |
| ------------------------- | ------------------------------------------------- | ---------------- |
| creationDate `String`     | Creation date of the session                      |                  |
| mfaAuthenticated `String` | Indicates if multi-factor authentication was used |                  |

### References

#### Fields with this object

* [{} ServerlessDeploymentUserIdentitySessionContext.attributes](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity-session-context)
