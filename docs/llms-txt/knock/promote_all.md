# Source: https://docs.knock.app/mapi-reference/commits/promote_all.md

### Promote all changes

Promote all changes across all resources to the target environment from its preceding environment.

#### Endpoint

`PUT /v1/commits/promote`

#### Query parameters

- **to_environment** (string) *required* - A slug of the target environment to which you want to promote all changes from its directly preceding environment.

For example, if you have three environments “development”, “staging”, and “production” (in that order), setting this param to “production” will promote all commits not currently in production from staging.

When this param is set to `"development"`, the `"branch"` param must be provided.

- **branch** (string) - The slug of the branch to promote all changes from.
- **resource_type** (string) - Filter commits to promote by resource type(s). Accepts a single type or array of types. Can be combined with resource_id to filter for specific resources.
- **resource_id** (string) - Filter commits to promote by resource identifier. Must be used together with resource_type.

#### Responses

##### 200

OK

###### Example

```json
{
  "result": "success"
}
```

