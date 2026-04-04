# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/compliance-item.md

# complianceItem

Represents compliance data associated with a specific standard, control, and category, along with relevant links and descriptions.

### Examples

```graphql
type ComplianceItem {
  standard: String
  standardLink: String
  control: String
  category: String
  description: String
  categoryLink: String
  controlLink: String
}
```

### Fields

| Field                 | Description                                   | Supported fields |
| --------------------- | --------------------------------------------- | ---------------- |
| standard `String`     | Compliance standard name                      |                  |
| standardLink `String` | Link to the compliance standard documentation |                  |
| control `String`      | Control associated with the standard          |                  |
| category `String`     | Category of the compliance control            |                  |
| description `String`  | Description of the compliance control         |                  |
| categoryLink `String` | Link to the compliance category documentation |                  |
| controlLink `String`  | Link to the specific control documentation    |                  |

### References

#### Fields with this object

* [{} Issue.compliance](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
