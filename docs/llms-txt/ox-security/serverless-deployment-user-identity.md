# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity.md

# serverlessDeploymentUserIdentity

Identity of the user who performed the serverless deployment.

### Examples

```graphql
type ServerlessDeploymentUserIdentity {
  type: String
  principalId: String
  arn: String
  accountId: String
  accessKeyId: String
  sessionContext: ServerlessDeploymentUserIdentitySessionContext
}
```

### Fields

| Field                                                                                                                                                                                                    | Description                               | Supported fields                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type `String`                                                                                                                                                                                            | Type of user identity (e.g., AssumedRole) |                                                                                                                                                                                                                                                                                     |
| principalId `String`                                                                                                                                                                                     | Principal ID of the user                  |                                                                                                                                                                                                                                                                                     |
| arn `String`                                                                                                                                                                                             | ARN of the user identity                  |                                                                                                                                                                                                                                                                                     |
| accountId `String`                                                                                                                                                                                       | Account ID of the user                    |                                                                                                                                                                                                                                                                                     |
| accessKeyId `String`                                                                                                                                                                                     | Access key ID used for the session        |                                                                                                                                                                                                                                                                                     |
| sessionContext [`ServerlessDeploymentUserIdentitySessionContext`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-user-identity-session-context) | Session context details                   | <p>sessionIssuer <a href="serverless-deployment-user-identity-session-issuer"><code>ServerlessDeploymentUserIdentitySessionIssuer</code></a><br>attributes <a href="serverless-deployment-user-identity-attributes"><code>ServerlessDeploymentUserIdentityAttributes</code></a></p> |

### References

#### Fields with this object

* [{} ServerlessDeploymentOperation.userIdentity](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-operation)
