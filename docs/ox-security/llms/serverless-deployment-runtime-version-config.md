# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-runtime-version-config.md

# serverlessDeploymentRuntimeVersionConfig

Configuration of the runtime version for a serverless function.

### Examples

```graphql
type ServerlessDeploymentRuntimeVersionConfig {
  runtimeVersionArn: String
}
```

### Fields

| Field                      | Description                | Supported fields |
| -------------------------- | -------------------------- | ---------------- |
| runtimeVersionArn `String` | ARN of the runtime version |                  |

### References

#### Fields with this object

* [{} ServerlessDeploymentOperation.runtimeVersionConfig](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/serverless-deployment-operation)
