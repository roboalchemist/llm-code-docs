# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/cloud-types.md

# cloudTypes

Supported cloud providers.

### Examples

```graphql
enum CloudTypes {
  AWS
  GCP
  Azure
  Kubernetes
  OpenShift
}
```

### Enum values

| Enum value | Description           |
| ---------- | --------------------- |
| AWS        | Amazon Web Services   |
| GCP        | Google Cloud Platform |
| Azure      | Microsoft Azure       |
| Kubernetes | Kubernetes            |
| OpenShift  | Red Hat OpenShift     |

### References

#### Fields with this object

* [{} CloudDescription.type](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-description)
