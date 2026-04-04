# Source: https://docs.ox.security/api-documentation/api-reference/api--filters/types/enums/filter-page.md

# filterPage

Pages where filters can be applied in the application.

### Examples

```graphql
enum FilterPage {
  Issues
  Application
  Sboms
  ResolvedIssues
  PipelineIssues
  PipelineSummary
  Artifacts
  ArtifactSignInfos
  APIInventory
  IrrelevantApps
  DisappearedIssues
  CloudBom
  UnscannedArtifacts
}
```

### Enum values

| Enum value         | Description                         |
| ------------------ | ----------------------------------- |
| Issues             | Security issues page                |
| Application        | Application management page         |
| Sboms              | Software Bill of Materials page     |
| ResolvedIssues     | Resolved issues page                |
| PipelineIssues     | Pipeline issues page                |
| PipelineSummary    | Pipeline summary page               |
| Artifacts          | Artifacts management page           |
| ArtifactSignInfos  | Artifact signature information page |
| APIInventory       | API inventory page                  |
| IrrelevantApps     | Irrelevant applications page        |
| DisappearedIssues  | Disappeared issues page             |
| CloudBom           | Cloud Bill of Materials page        |
| UnscannedArtifacts | Unscanned artifacts page            |

### References

#### Queries using this object

* [\<?> getFilterLabels.page](https://docs.ox.security/api-documentation/api-reference/api--filters/queries/get-filter-labels)
