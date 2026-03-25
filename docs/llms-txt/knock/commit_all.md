# Source: https://docs.knock.app/mapi-reference/commits/commit_all.md

### Commit all changes

Commit all changes across all resources in the development environment.

#### Endpoint

`PUT /v1/commits`

#### Query parameters

- **environment** (string) *required* - The environment slug.
- **branch** (string) - The slug of a branch to use. This option can only be used when `environment` is `"development"`.
- **commit_message** (string) - An optional message to include in a commit.
- **resource_type** (string) - Filter changes to commit by resource type(s). Accepts a single type or array of types. Can be combined with resource_id to filter for specific resources.
- **resource_id** (string) - Filter changes to commit by resource identifier. Must be used together with resource_type.

#### Responses

##### 200

OK

###### Example

```json
{
  "result": "success"
}
```

