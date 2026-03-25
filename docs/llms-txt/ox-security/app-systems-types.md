# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-systems-types.md

# appSystemsTypes

Types of systems that can be associated with applications.

### Examples

```graphql
enum AppSystemsTypes {
  cicd
  cloudDeployments
}
```

### Enum values

| Enum value       | Description                                          |
| ---------------- | ---------------------------------------------------- |
| cicd             | Continuous Integration/Continuous Deployment systems |
| cloudDeployments | Cloud deployment environments                        |

### References

#### Fields with this object

* [{} SystemFilter.name](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/system-filter)
