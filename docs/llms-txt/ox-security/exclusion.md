# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/exclusion.md

# exclusion

Main exclusion entity containing all exclusion details and metadata.

### Examples

```graphql
type Exclusion {
  exclusionType: ExclusionType!
  exclusionId: String!
  modifiedIssues: Float
  modifiedBy: String!
  createdAt: DateTime!
  exclusionAppliedOn: String!
  exclusionTypeLabel: String!
  exclusionMatch: [ExclusionMatch!]!
  appName: String
  policyName: String
  appId: String
  policyId: String
  policyCategory: String
  appType: String
  comment: String
  exclusionScope: ExclusionScope
  oxIssueId: String
  issueName: String
  exclusionMode: ExclusionMode
  expiredAt: DateTime
  isActive: Boolean!
  inDayExpired: Boolean
  inWeekExpired: Boolean
  status: StatusMode
  fp: Boolean
  exclusionSubType: OxExclusionSubType
}
```

### Fields

| Field                                                                                                                                               | Description                                           | Supported fields                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------- |
| exclusionType [`ExclusionType!`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-type)               | Type of the exclusion (alert, policy, or application) |                                                               |
| exclusionId `String!`                                                                                                                               | Unique string identifier for the exclusion            |                                                               |
| modifiedIssues `Float`                                                                                                                              | Number of issues modified by this exclusion           |                                                               |
| modifiedBy `String!`                                                                                                                                | User who last modified the exclusion                  |                                                               |
| createdAt `DateTime!`                                                                                                                               | Timestamp when the exclusion was created              |                                                               |
| exclusionAppliedOn `String!`                                                                                                                        | Description of where this exclusion is applied        |                                                               |
| exclusionTypeLabel `String!`                                                                                                                        | Human-readable label for the exclusion type           |                                                               |
| exclusionMatch [`[ExclusionMatch!]!`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/exclusion-match)       | List of matching criteria for this exclusion          | <p>key <code>String!</code><br>value <code>String!</code></p> |
| appName `String`                                                                                                                                    | Name of the application this exclusion applies to     |                                                               |
| policyName `String`                                                                                                                                 | Name of the policy this exclusion applies to          |                                                               |
| appId `String`                                                                                                                                      | ID of the application this exclusion applies to       |                                                               |
| policyId `String`                                                                                                                                   | ID of the policy this exclusion applies to            |                                                               |
| policyCategory `String`                                                                                                                             | Category of the policy this exclusion applies to      |                                                               |
| appType `String`                                                                                                                                    | Type of application this exclusion applies to         |                                                               |
| comment `String`                                                                                                                                    | User comment explaining the reason for this exclusion |                                                               |
| exclusionScope [`ExclusionScope`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-scope)             | Scope of application for this exclusion               |                                                               |
| oxIssueId `String`                                                                                                                                  | Ox-specific issue identifier                          |                                                               |
| issueName `String`                                                                                                                                  | Name of the issue this exclusion applies to           |                                                               |
| exclusionMode [`ExclusionMode`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-mode)                | Mode of operation for this exclusion                  |                                                               |
| expiredAt `DateTime`                                                                                                                                | Date when this exclusion expires                      |                                                               |
| isActive `Boolean!`                                                                                                                                 | Whether this exclusion is currently active            |                                                               |
| inDayExpired `Boolean`                                                                                                                              | Whether this exclusion expires within one day         |                                                               |
| inWeekExpired `Boolean`                                                                                                                             | Whether this exclusion expires within one week        |                                                               |
| status [`StatusMode`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/status-mode)                             | Current status of the exclusion                       |                                                               |
| fp `Boolean`                                                                                                                                        | Whether this exclusion is marked as a false positive  |                                                               |
| exclusionSubType [`OxExclusionSubType`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/ox-exclusion-sub-type) | Sub type of the exclusion                             |                                                               |

### References

#### Fields with this object

* [{} GetExclusionsRes.exclusions](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/get-exclusions-res)
