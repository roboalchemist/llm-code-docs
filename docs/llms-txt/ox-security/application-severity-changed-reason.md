# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-severity-changed-reason.md

# applicationSeverityChangedReason

Represents a reason for a severity change in an application.

### Examples

```graphql
type ApplicationSeverityChangedReason {
  tagId: String
  changeNumber: Float
  shouldBeSeverityFactor: Boolean
  requiredHits: Int
  reason: String
  shortName: String
  changeCategory: String
  changePlusReasonFacet: String
  extraInfo: [ApplicationExtraInfo]
}
```

### Fields

| Field                                                                                                                                                | Description                                                         | Supported fields                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| tagId `String`                                                                                                                                       | The identifier of the tag associated with the severity change       |                                                                                                                                      |
| changeNumber `Float`                                                                                                                                 | The numerical change in severity                                    |                                                                                                                                      |
| shouldBeSeverityFactor `Boolean`                                                                                                                     | Indicates whether the change should be considered a severity factor |                                                                                                                                      |
| requiredHits `Int`                                                                                                                                   | The number of required hits to trigger the severity change          |                                                                                                                                      |
| reason `String`                                                                                                                                      | The reason for the severity change                                  |                                                                                                                                      |
| shortName `String`                                                                                                                                   | A short, user-friendly name for the change reason                   |                                                                                                                                      |
| changeCategory `String`                                                                                                                              | The category of the change, such as 'Vulnerability' or 'Compliance' |                                                                                                                                      |
| changePlusReasonFacet `String`                                                                                                                       | A combination of change category and reason for faceting purposes   |                                                                                                                                      |
| extraInfo [`[ApplicationExtraInfo]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-extra-info) | Additional information associated with the severity change          | <p>key <code>String</code><br>link <code>String</code><br>snippet <a href="extra-info-snippet"><code>ExtraInfoSnippet</code></a></p> |

### References

#### Fields with this object

* [{} Application.severityChangedReason](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
