# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/pipeline-scan-result.md

# pipelineScanResult

Pipeline scan result indicating the outcome of a security scan in the CI/CD pipeline.

### Examples

```graphql
enum PipelineScanResult {
  none
  monitor
  block
}
```

### Enum values

| Enum value | Description                                          |
| ---------- | ---------------------------------------------------- |
| none       | No scan result available or scan not performed       |
| monitor    | Issues were found but did not block the pipeline     |
| block      | Critical issues were found that blocked the pipeline |

### References

#### Fields with this object

* [{} Pipeline.scanResult](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/pipeline)
