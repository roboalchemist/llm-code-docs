# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/aws-cloud-formation-info.md

# awsCloudFormationInfo

Configuration for AWS CloudFormation integration.

### Examples

```graphql
type AWSCloudFormationInfo {
  baseURL: String
  urlParams: String
}
```

### Fields

| Field              | Description                          | Supported fields |
| ------------------ | ------------------------------------ | ---------------- |
| baseURL `String`   | Base URL for CloudFormation template |                  |
| urlParams `String` | URL parameters for Cloud Formation   |                  |

### References

#### Fields with this object

* [{} Connector.awsCloudFormationInfo](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
* [{} Connector.awsCloudFormationOrganizationInfo](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
