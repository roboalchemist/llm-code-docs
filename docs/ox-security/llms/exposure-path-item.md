# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/exposure-path-item.md

# exposurePathItem

Describes an item in the exposure path showing how a resource is accessible.

### Examples

```graphql
type ExposurePathItem {
  type: String
  name: String
  cbomId: String
}
```

### Fields

| Field           | Description                                           | Supported fields |
| --------------- | ----------------------------------------------------- | ---------------- |
| type `String`   | Type of component in the exposure path                |                  |
| name `String`   | Name of the component                                 |                  |
| cbomId `String` | Cloud Bill of Materials identifier for this component |                  |

### References

#### Fields with this object

* [{} CloudItem.exposurePath](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item)
* [{} Workload.exposurePath](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/workload)
