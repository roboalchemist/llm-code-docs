# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issues-export-column-keys.md

# issuesExportColumnKeys

Keys for the columns in the issues export.

### Examples

```graphql
enum IssuesExportColumnKeys {
  Severity
  Category
  Name
  Application
  Overdue
  ApproachingDue
  FirstSeen
  Count
  SLA
  IssueOwner
  FalsePositiveComment
}
```

### Enum values

| Enum value           | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| Severity             | Severity column key of the issue for sla report             |
| Category             | Category column key of the issue for sla report             |
| Name                 | Name column key of the issue for sla report                 |
| Application          | Application column key of the issue for sla report          |
| Overdue              | Overdue column key of the issue for sla report              |
| ApproachingDue       | ApproachingDue column key of the issue for sla report       |
| FirstSeen            | FirstSeen column key of the issue for sla report            |
| Count                | Count column key of the issue for sla report                |
| SLA                  | SLA column key of the issue for sla report                  |
| IssueOwner           | IssueOwner column key of the issue for sla report           |
| FalsePositiveComment | FalsePositiveComment column key of the issue for sla report |

### References

#### Fields with this object

* [{} IssuesExportColumn.key](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-export-column)
