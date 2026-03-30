# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-extra-info.md

# applicationExtraInfo

Provides additional contextual information for a severity change.

### Examples

```graphql
type ApplicationExtraInfo {
  key: String
  link: String
  snippet: ExtraInfoSnippet
}
```

### Fields

| Field                                                                                                                                    | Description                                              | Supported fields                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| key `String`                                                                                                                             | The key associated with the extra information            |                                                                                                                                                                            |
| link `String`                                                                                                                            | A link to further information or context                 |                                                                                                                                                                            |
| snippet [`ExtraInfoSnippet`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/extra-info-snippet) | A snippet of code or text related to the severity change | <p>detectionType <code>String</code><br>fileName <code>String</code><br>snippetLineNumber <code>Int</code><br>language <code>String</code><br>text <code>String</code></p> |

### References

#### Fields with this object

* [{} ApplicationSeverityChangedReason.extraInfo](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-severity-changed-reason)
* [{} SaasBomItem.extraInfo](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/objects/saas-bom-item)
