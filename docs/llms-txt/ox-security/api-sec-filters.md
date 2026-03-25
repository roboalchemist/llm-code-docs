# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/api-sec-filters.md

# apiSecFilters

Filter criteria for searching and filtering API security items.

### Examples

```graphql
input ApiSecFilters {
  apps: [String]
  appIds: [String]
  titles: [String]
  endpoints: [String]
  methods: [String]
  framework: [String]
  languages: [String]
  issueIds: [String]
  apiId: [String]
  source: [String]
  severities: [String]
  reachability: [String]
  appTags: [String]
}
```

### Fields

| Field                   | Description                                                                                                       | Supported fields |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------- |
| apps `[String]`         | Filter by specific application names                                                                              |                  |
| appIds `[String]`       | Filter by specific application IDs                                                                                |                  |
| titles `[String]`       | Filter by API titles or names                                                                                     |                  |
| endpoints `[String]`    | Filter by specific API endpoints                                                                                  |                  |
| methods `[String]`      | Filter by HTTP methods                                                                                            |                  |
| framework `[String]`    | Filter by framework used to implement the APIs                                                                    |                  |
| languages `[String]`    | Filter by programming languages                                                                                   |                  |
| issueIds `[String]`     | Filter by specific security issue identifiers                                                                     |                  |
| apiId `[String]`        | Filter by specific API identifiers                                                                                |                  |
| source `[String]`       | Filter by source of the API definition                                                                            |                  |
| severities `[String]`   | Filter by security issue severity levels (0 - Info, 1 - Low, 2 - Medium, 3 - High, 4 - Critical, 5 - Appoxalypse) |                  |
| reachability `[String]` | Filter by API reachability status                                                                                 |                  |
| appTags `[String]`      | Filter by application tags                                                                                        |                  |

### References

#### Fields with this object

* [{} GetApiSecurityInput.filters](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/get-api-security-input)
