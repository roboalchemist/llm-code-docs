# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity-session-context.md

# serverlessDeploymentUserIdentitySessionContext

Session context for the user identity performing a serverless deployment.

### Examples

```graphql
type ServerlessDeploymentUserIdentitySessionContext {
  sessionIssuer: ServerlessDeploymentUserIdentitySessionIssuer
  attributes: ServerlessDeploymentUserIdentityAttributes
}
```

### Fields

| Field                                                                                                                                                                                                 | Description                       | Supported fields                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sessionIssuer [`ServerlessDeploymentUserIdentitySessionIssuer`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity-session-issuer) | Details about the session issuer  | <p>type <code>String</code><br>principalId <code>String</code><br>arn <code>String</code><br>accountId <code>String</code><br>userName <code>String</code></p> |
| attributes [`ServerlessDeploymentUserIdentityAttributes`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity-attributes)           | Attributes of the session context | <p>creationDate <code>String</code><br>mfaAuthenticated <code>String</code></p>                                                                                |

### References

#### Fields with this object

* [{} ServerlessDeploymentUserIdentity.sessionContext](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity)
