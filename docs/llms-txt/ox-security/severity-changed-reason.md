# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/severity-changed-reason.md

# severityChangedReason

Information describing the reason why severity changed for an issue.

### Examples

```graphql
type SeverityChangedReason {
  changeNumber: Float
  withoutAutoNumbering: Boolean
  evidenceLabel: String
  reason: String
  shortName: String
  changeCategory: String
  extraInfo: [SeverityChangedExtraInfo]
  extraInfoContainer: [ExtraInfoContainer]
  order: Int
}
```

### Fields

| Field                                                                                                                                                   | Description                                                     | Supported fields                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| changeNumber `Float`                                                                                                                                    | Numerical value representing the amount of severity change      |                                                                                                                                                                                                                             |
| withoutAutoNumbering `Boolean`                                                                                                                          | Indicates if numbering should be skipped for automatic sequence |                                                                                                                                                                                                                             |
| evidenceLabel `String`                                                                                                                                  | Label for the evidence supporting the severity change           |                                                                                                                                                                                                                             |
| reason `String`                                                                                                                                         | Description or explanation for the severity change              |                                                                                                                                                                                                                             |
| shortName `String`                                                                                                                                      | Short name or identifier for the reason                         |                                                                                                                                                                                                                             |
| changeCategory `String`                                                                                                                                 | Category of the change for organizational purposes              |                                                                                                                                                                                                                             |
| extraInfo [`[SeverityChangedExtraInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/severity-changed-extra-info) | Additional detailed information related to the severity change  | <p>key <code>String</code><br>value <code>String</code><br>link <code>String</code><br>snippet <a href="snippet-info"><code>SnippetInfo</code></a><br>iconLink <code>String</code><br>callBranch <code>\[String]</code></p> |
| extraInfoContainer [`[ExtraInfoContainer]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/extra-info-container)     | Containers with extra contextual information                    | <p>layerSha <code>String</code><br>layerNum <code>Int</code><br>artifactName <code>String</code><br>sha <code>String</code><br>registryName <code>String</code></p>                                                         |
| order `Int`                                                                                                                                             | Order of the severity change reason                             |                                                                                                                                                                                                                             |

### References

#### Fields with this object

* [{} Issue.severityChangedReason](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
* [{} Issue.aggSFsForCalcDisplay](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
