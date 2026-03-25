# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/app-filters.md

# appFilters

Input type to apply additional application-level filters.

### Examples

```graphql
input AppFilters {
  fakeApp: Boolean
  appId: [String]
  categories: [String]
  cicd: [String]
  repoTypes: [String]
  orchestrators: [String]
  artifacts: [String]
  artifactsSystem: [String]
  cloudDeployments: [String]
  kubernetes: [String]
  sca: [String]
  sast: [String]
  secretSearch: [String]
  iac: [String]
  securityToolSource: [String]
  oxInPipeline: [String]
  languages: [String]
  riskScore: Range
  businessPriority: Range
  pkgManagers: [String]
  isMonoRepoChild: [String]
  tags: [String]
  appClassification: [String]
  originBranchName: [String]
  irrelevantReasons: [String]
  reachability: [String]
  toolName: [String]
}
```

### Fields

| Field                                                                                                                    | Description                                                   | Supported fields                                        |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------- |
| fakeApp `Boolean`                                                                                                        | Filter test or demo applications                              |                                                         |
| appId `[String]`                                                                                                         | Filter by specific application identifiers                    |                                                         |
| categories `[String]`                                                                                                    | Filter by application categories                              |                                                         |
| cicd `[String]`                                                                                                          | Filter by CI/CD system types                                  |                                                         |
| repoTypes `[String]`                                                                                                     | Filter by repository types                                    |                                                         |
| orchestrators `[String]`                                                                                                 | Filter by orchestration systems                               |                                                         |
| artifacts `[String]`                                                                                                     | Filter by artifact types                                      |                                                         |
| artifactsSystem `[String]`                                                                                               | Filter by artifact storage systems                            |                                                         |
| cloudDeployments `[String]`                                                                                              | Filter by cloud deployment types                              |                                                         |
| kubernetes `[String]`                                                                                                    | Filter by Kubernetes configurations                           |                                                         |
| sca `[String]`                                                                                                           | Filter by SCA (Software Composition Analysis) findings        |                                                         |
| sast `[String]`                                                                                                          | Filter by SAST (Static Application Security Testing) findings |                                                         |
| secretSearch `[String]`                                                                                                  | Filter by secret detection findings                           |                                                         |
| iac `[String]`                                                                                                           | Filter by Infrastructure as Code findings                     |                                                         |
| securityToolSource `[String]`                                                                                            | Filter by security tool sources                               |                                                         |
| oxInPipeline `[String]`                                                                                                  | Filter by Ox pipeline integration status                      |                                                         |
| languages `[String]`                                                                                                     | Filter by programming languages                               |                                                         |
| riskScore [`Range`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range)        | Filter by risk score range                                    | <p>from <code>Float</code><br>to <code>Float</code></p> |
| businessPriority [`Range`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range) | Filter by business priority score range                       | <p>from <code>Float</code><br>to <code>Float</code></p> |
| pkgManagers `[String]`                                                                                                   | Filter by package managers                                    |                                                         |
| isMonoRepoChild `[String]`                                                                                               | Filter monorepo child applications                            |                                                         |
| tags `[String]`                                                                                                          | Filter by application tags                                    |                                                         |
| appClassification `[String]`                                                                                             | Filter by application classification                          |                                                         |
| originBranchName `[String]`                                                                                              | Filter by repository branch names                             |                                                         |
| irrelevantReasons `[String]`                                                                                             | Filter by irrelevancy reasons                                 |                                                         |
| reachability `[String]`                                                                                                  | Filter by application reachability                            |                                                         |
| toolName `[String]`                                                                                                      | Filter by third party tool name                               |                                                         |

### References

#### Fields with this object

* [{} GetApplicationsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
