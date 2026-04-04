# Source: https://docs.knock.app/cli/branch/merge.md

# Source: https://docs.knock.app/api-reference/users/merge.md

### Merge users

Merge two users together, where the user specified with the `from_user_id` param will be merged into the user specified by `user_id`.

#### Endpoint

`POST /v1/users/{user_id}/merge`

**Rate limit tier:** 2

#### Path parameters

- **user_id** (string) *required* - The id of the user to merge into.

#### Request body

A set of parameters to merge one user into another.

##### Example

```json
{
  "from_user_id": "user_1"
}
```

#### Responses

##### 200

OK

###### Example

```json
{
  "__typename": "User",
  "created_at": null,
  "email": "ian.malcolm@chaos.theory",
  "id": "user_id",
  "name": "Dr. Ian Malcolm",
  "updated_at": "2024-05-22T12:00:00Z"
}
```

