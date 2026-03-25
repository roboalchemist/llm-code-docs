# Source: https://docs.knock.app/mapi-reference/branches/schemas/branch.md

### Branch

A branch object.

#### Attributes

- **created_at** (string) *required* - The timestamp of when the branch was created.
- **deleted_at** (string) - The timestamp of when the branch was deleted.
- **last_commit_at** (string) - The timestamp of the most-recent commit in the branch.
- **slug** (string) *required* - A unique slug for the branch. Cannot exceed 255 characters.
- **updated_at** (string) *required* - The timestamp of when the branch was last updated.

#### Example

```json
{
  "created_at": "2022-10-31T19:59:03Z",
  "deleted_at": null,
  "last_commit_at": "2022-10-31T19:59:03Z",
  "slug": "feature-branch",
  "updated_at": "2022-10-31T19:59:03Z"
}
```

