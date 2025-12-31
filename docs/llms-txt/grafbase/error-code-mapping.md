# Source: https://grafbase.com/docs/gateway/configuration/error-code-mapping.md

# Error Code Mapping

Gateway [error codes](https://grafbase.com/docs/gateway/errors.md) can be overridden with the following configuration:

```toml
[graph.error_code_mapping]
OPERATION_VALIDATION_ERROR = "MY_CUSTOM_CODE"
```