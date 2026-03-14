# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/ticket.md

# ticket

Represents a ticket or issue created in an external issue tracking system.

### Examples

```graphql
type Ticket {
  provider: Provider
  ticketId: String
  createdBy: String
  issueId: String
  issueName: String
  appName: String
  appId: String
  category: String
  assignee: String
  reporter: String
  link: String
  project: String
  issueType: String
  key: String
}
```

### Fields

| Field                                                                                                           | Description                                      | Supported fields |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------- |
| provider [`Provider`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/provider) | Ticket provider or system                        |                  |
| ticketId `String`                                                                                               | Unique identifier of the ticket                  |                  |
| createdBy `String`                                                                                              | User who created the ticket                      |                  |
| issueId `String`                                                                                                | Associated issue ID                              |                  |
| issueName `String`                                                                                              | Name or title of the associated issue            |                  |
| appName `String`                                                                                                | Name of the application related to the issue     |                  |
| appId `String`                                                                                                  | ID of the application related to the issue       |                  |
| category `String`                                                                                               | Category of the ticket                           |                  |
| assignee `String`                                                                                               | User assigned to the ticket                      |                  |
| reporter `String`                                                                                               | User who reported the ticket                     |                  |
| link `String`                                                                                                   | URL or link to the ticket in the external system |                  |
| project `String`                                                                                                | Project name or identifier the ticket belongs to |                  |
| issueType `String`                                                                                              | Type of issue                                    |                  |
| key `String`                                                                                                    | Key or short identifier of the ticket            |                  |

### References

#### Fields with this object

* [{} Issue.tickets](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
