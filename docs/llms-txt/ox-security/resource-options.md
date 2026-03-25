# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/resource-options.md

# resourceOptions

Configuration options for resource monitoring.

### Examples

```graphql
type ResourceOptions {
  resourceName: ResourceName
  hideMonitorNewResourcesCheckbox: Boolean
  showSettingsPerResource: Boolean
}
```

### Fields

| Field                                                                                                                             | Description                                         | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------- |
| resourceName [`ResourceName`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/resource-name) | Type of resource being monitored                    |                  |
| hideMonitorNewResourcesCheckbox `Boolean`                                                                                         | Whether to hide the option to monitor new resources |                  |
| showSettingsPerResource `Boolean`                                                                                                 | Whether to show per-resource configuration options  |                  |

### References

#### Fields with this object

* [{} Connector.resourceOptions](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
