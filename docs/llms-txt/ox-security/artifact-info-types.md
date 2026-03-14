# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/artifact-info-types.md

# artifactInfoTypes

Types of artifacts that can be analyzed for security issues.

### Examples

```graphql
enum ArtifactInfoTypes {
  Container
  Lambda
  NPM
  Yarn
  Serverless
}
```

### Enum values

| Enum value | Description                     |
| ---------- | ------------------------------- |
| Container  | Container image artifact        |
| Lambda     | AWS Lambda function artifact    |
| NPM        | NPM package artifact            |
| Yarn       | Yarn package artifact           |
| Serverless | Serverless application artifact |

### References

#### Fields with this object

* [{} IArtifactInfo.type](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/i-artifact-info)
