# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/ecs.md

# ecs

Amazon ECS resource attributes.

### Examples

```graphql
type ECS {
  os: String
  cpu: String
  memory: String
  containers: String
  registeredAt: Float
  registeredBy: String
  account: String
  zone: String
}
```

### Fields

| Field                 | Description                                                | Supported fields |
| --------------------- | ---------------------------------------------------------- | ---------------- |
| os `String`           | Operating system running on the ECS                        |                  |
| cpu `String`          | CPU resources allocated                                    |                  |
| memory `String`       | Memory resources allocated                                 |                  |
| containers `String`   | Number or list of containers running                       |                  |
| registeredAt `Float`  | Timestamp (epoch) when the ECS was registered              |                  |
| registeredBy `String` | Identifier or name of the entity who registered the ECS    |                  |
| account `String`      | Cloud account associated with the ECS                      |                  |
| zone `String`         | Cloud availability zone or region where the ECS is located |                  |

### References

#### Fields with this object

* [{} CommonCloudAttributesUnion](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/unions/common-cloud-attributes-union)
