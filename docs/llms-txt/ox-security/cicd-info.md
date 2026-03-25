# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/cicd-info.md

# cicdInfo

Represents information about a CICD pipeline associated with an application, including its type, system, job count, and location details.

### Examples

```graphql
type CicdInfo {
  type: String
  system: String
  latestDate: String
  lastMonthJobCount: String
  location: [CicdInfoLocation]
}
```

### Fields

| Field                                                                                                                                       | Description                                     | Supported fields                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| type `String`                                                                                                                               | Type of the CICD pipeline                       |                                                                                                                            |
| system `String`                                                                                                                             | System associated with the CICD pipeline        |                                                                                                                            |
| latestDate `String`                                                                                                                         | Date of the most recent job run in the pipeline |                                                                                                                            |
| lastMonthJobCount `String`                                                                                                                  | Number of jobs run in the last month            |                                                                                                                            |
| location [`[CicdInfoLocation]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/cicd-info-location) | Locations and context of the CICD jobs          | <p>runBy <code>String</code><br>foundBy <code>String</code><br>foundIn <code>String</code><br>link <code>String</code></p> |

### References

#### Fields with this object

* [{} ApplicationFlow.cicdInfo](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-flow)
