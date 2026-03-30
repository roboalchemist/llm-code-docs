# Source: https://docs.knock.app/mapi-reference/environments/schemas/environment.md

### Environment

An environment object.

#### Attributes

- **created_at** (string) *required* - The timestamp of when the environment was created.
- **deleted_at** (string) - The timestamp of when the environment was deleted.
- **hide_pii_data** (boolean) - Whether PII data is hidden from the environment. Read more in the [data obfuscation docs](https://docs.knock.app/manage-your-account/data-obfuscation).
- **label_color** (string) - The color of the environment label to display in the dashboard.
- **last_commit_at** (string) - The timestamp of the most-recent commit in the environment.
- **name** (string) *required* - A human-readable name for the environment. Cannot exceed 255 characters.
- **order** (integer) *required* - The order of the environment. The lowest number is the first environment, the highest number is the last environment. The order will not always be sequential.
- **owner** (string) *required* - The owner of the environment.
- **slug** (string) *required* - A unique slug for the environment. Cannot exceed 255 characters.
- **updated_at** (string) *required* - The timestamp of when the environment was last updated.

#### Example

```json
{
  "created_at": "2022-10-31T19:59:03Z",
  "deleted_at": null,
  "hide_pii_data": false,
  "label_color": "#000000",
  "last_commit_at": "2022-10-31T19:59:03Z",
  "name": "Development",
  "order": 0,
  "owner": "system",
  "slug": "development",
  "updated_at": "2022-10-31T19:59:03Z"
}
```

