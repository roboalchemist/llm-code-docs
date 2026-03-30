# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity-session-issuer.md

# serverlessDeploymentUserIdentitySessionIssuer

Details about the issuer of a session in a serverless deployment operation.

### Examples

```graphql
type ServerlessDeploymentUserIdentitySessionIssuer {
  type: String
  principalId: String
  arn: String
  accountId: String
  userName: String
}
```

### Fields

| Field                | Description                             | Supported fields |
| -------------------- | --------------------------------------- | ---------------- |
| type `String`        | Type of the session issuer (e.g., Role) |                  |
| principalId `String` | Principal ID of the session issuer      |                  |
| arn `String`         | ARN of the session issuer               |                  |
| accountId `String`   | Account ID of the session issuer        |                  |
| userName `String`    | Username of the session issuer          |                  |

### References

#### Fields with this object

* [{} ServerlessDeploymentUserIdentitySessionContext.sessionIssuer](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity-session-context)
