# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-filters.md

# cloudItemsFilters

Defines filter criteria for searching and filtering cloud security items.

### Examples

```graphql
input CloudItemsFilters {
  apps: [String]
  service: [String]
  type: [String]
  cloudProvider: [String]
  assetName: [String]
  accountId: [String]
  region: [String]
  serviceCategory: [String]
  cluster: [String]
  severities: [String]
  isExposed: [String]
  imageSource: [String]
  registryType: [String]
  registryName: [String]
  imageScanStatus: [String]
  artifactIds: [String]
}
```

### Fields

| Field                      | Description                                      | Supported fields |
| -------------------------- | ------------------------------------------------ | ---------------- |
| apps `[String]`            | Filter by specific application names             |                  |
| service `[String]`         | Filter by cloud service                          |                  |
| type `[String]`            | Filter by cloud service type                     |                  |
| cloudProvider `[String]`   | Filter by cloud provider (AWS, Azure, GCP, etc.) |                  |
| assetName `[String]`       | Filter by asset or resource names                |                  |
| accountId `[String]`       | Filter by cloud account identifiers              |                  |
| region `[String]`          | Filter by cloud regions                          |                  |
| serviceCategory `[String]` | Filter by service categories                     |                  |
| cluster `[String]`         | Filter by Kubernetes cluster names               |                  |
| severities `[String]`      | Filter by security issue severity levels         |                  |
| isExposed `[String]`       | Filter by exposure status (exposed, not exposed) |                  |
| imageSource `[String]`     | Filter by container image source                 |                  |
| registryType `[String]`    | Filter by container registry type                |                  |
| registryName `[String]`    | Filter by container registry name                |                  |
| imageScanStatus `[String]` | Filter by image scan status                      |                  |
| artifactIds `[String]`     | Filter by artifact ID                            |                  |

### References

#### Fields with this object

* [{} CloudItemsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-input)
