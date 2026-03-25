# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/types/enums/third-party-upload-data-type.md

# thirdPartyUploadDataType

Supported formats for uploaded data.

### Examples

```graphql
enum ThirdPartyUploadDataType {
  JSON
  SARIF
}
```

### Enum values

| Enum value | Description             |
| ---------- | ----------------------- |
| JSON       | Data is JSON format     |
| SARIF      | Data is in SARIF format |

### References

#### Mutations using this object

* [<\~> uploadThirdPartyFileBase64.fileType](https://docs.ox.security/api-documentation/api-reference/api--file-download/mutations/upload-third-party-file-base64)
