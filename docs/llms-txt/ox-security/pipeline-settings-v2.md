# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/pipeline-settings-v2.md

# pipelineSettingsV2

Enhanced version of pipeline settings with additional configuration options and granular control.

### Examples

```graphql
type PipelineSettingsV2 {
  isDefaultSettings: Boolean!
  isGithubConnected: Boolean
  isBitbucketConnected: Boolean
  isGitlabConnected: Boolean
  apps: JSONObject
  settings: JSONObject
  branchSettings: JSONObject
}
```

### Fields

| Field                          | Description                                                                             | Supported fields |
| ------------------------------ | --------------------------------------------------------------------------------------- | ---------------- |
| isDefaultSettings `Boolean!`   | Indicates whether system-wide default pipeline settings are being used                  |                  |
| isGithubConnected `Boolean`    | Status of GitHub integration connection                                                 |                  |
| isBitbucketConnected `Boolean` | Status of Bitbucket integration connection                                              |                  |
| isGitlabConnected `Boolean`    | Status of GitLab integration connection                                                 |                  |
| apps `JSONObject`              | List of application identifiers with their pipeline configurations                      |                  |
| settings `JSONObject`          | Global pipeline settings as key-value pairs, affecting all configured applications      |                  |
| branchSettings `JSONObject`    | Branch-specific pipeline settings, allowing different configurations per branch pattern |                  |

### References

#### Fields with this object

* [{} AuditLog.pipelineSettingsV2](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
