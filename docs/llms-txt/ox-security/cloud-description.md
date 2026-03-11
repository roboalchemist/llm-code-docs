# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-description.md

# cloudDescription

Description of a cloud resource or service.

### Examples

```graphql
type CloudDescription {
  type: CloudTypes
  subType: CloudSubTypes
  cloudEntityAttributes: CommonCloudAttributesUnion
}
```

### Fields

| Field                                                                                                                                                                   | Description                                                                           | Supported fields |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------- |
| type [`CloudTypes`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/cloud-types)                                                     | Type of cloud service                                                                 |                  |
| subType [`CloudSubTypes`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/cloud-sub-types)                                           | Subtype of the cloud service                                                          |                  |
| cloudEntityAttributes [`CommonCloudAttributesUnion`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/unions/common-cloud-attributes-union) | Attributes specific to the cloud entity, represented by a union of common cloud types |                  |

### References

#### Fields with this object

* [{} CloudArtifactData.cloudDescription](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-artifact-data)
