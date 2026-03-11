# Source: https://docs.knock.app/mapi-reference/members/retrieve.md

# Source: https://docs.knock.app/mapi-reference/branches/retrieve.md

# Source: https://docs.knock.app/mapi-reference/translations/retrieve.md

# Source: https://docs.knock.app/mapi-reference/commits/retrieve.md

# Source: https://docs.knock.app/mapi-reference/message_types/retrieve.md

# Source: https://docs.knock.app/mapi-reference/guides/retrieve.md

# Source: https://docs.knock.app/mapi-reference/partials/retrieve.md

# Source: https://docs.knock.app/mapi-reference/email_layouts/retrieve.md

# Source: https://docs.knock.app/mapi-reference/broadcasts/retrieve.md

# Source: https://docs.knock.app/mapi-reference/workflows/retrieve.md

# Source: https://docs.knock.app/mapi-reference/channel_groups/retrieve.md

# Source: https://docs.knock.app/mapi-reference/environments/retrieve.md

### Get an environment

Returns a single environment by the `environment_slug`.

#### Endpoint

`GET /v1/environments/{environment_slug}`

#### Path parameters

- **environment_slug** (string) *required* - The slug of the environment to retrieve.

#### Responses

##### 200

OK

###### Example

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

