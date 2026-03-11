# Source: https://docs.knock.app/mapi-reference/commits/schemas/commit.md

### Commit

A commit is a change to a resource within an environment, made by an author.

#### Attributes

- **author** (object) *required* - The author of the commit.
- **commit_message** (string) - The optional message about the commit.
- **created_at** (string) *required* - The timestamp of when the commit was created.
- **environment** (string) *required* - The environment of the commit.
- **id** (string) *required* - The unique identifier for the commit.
- **resource** (object) *required* - The resource object associated with the commit.

#### Example

```json
{
  "author": {
    "email": "john.doe@example.com",
    "name": "John Doe"
  },
  "commit_message": "This is a commit message",
  "created_at": "2021-01-01T00:00:00Z",
  "environment": "development",
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "resource": {
    "identifier": "my-email-layout",
    "type": "email_layout"
  }
}
```

