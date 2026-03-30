# Source: https://northflank.com/docs/v1/api/team/team-roles/get-team-role.md

# Get team role

Gets details about a specific platform role.

Required permission: Account > Admin > Roles > Read

**Path parameters:**

{object}
- `teamId`: (string) (required) ID of the team
- `roleId`: (string) (required) ID of the team role

**Response body:**

{object}
- `data`: {object}
  - `id`: (string) (required) ID of the role. (pattern: ^[A-Za-z0-9-]+$)
  - `name`: (string) (required) Display name of the role.
  - `description`: (string) Description of the role.
  - `restrictions`: {object}
    - `enabled`: (boolean) (required) Whether project restrictions are enabled.
    - `projects`: [array of] (string)
    - `restrictionMode`: (string) Restriction mode.
  - `createdAt`: (string) Creation time. (format: date-time)
  - `updatedAt`: (string) Last updated. (format: date-time)
  - `permissions`: {object}
    - `teamScope`: [array of] (string)
    - `projectScope`: [array of] (string)

## API reference

GET /v1/teams/{teamId}/roles/{roleId}

### Example Response

200 OK: Details about the team role.

```json
{
  "data": {
    "id": "developer",
    "name": "Developer",
    "description": "Role for developers.",
    "createdAt": "2021-01-20T11:19:53.175Z",
    "updatedAt": "2021-01-20T11:19:53.175Z"
  }
}
```

## CLI reference

$ northflank get team-role

Options:

- `--teamId <teamId>`: ID of the team

- `--roleId <roleId>`: ID of the team role

- `--verbose `: Verbose output

- `--quiet `: No console output

- `-o --output <format>`: Output formatting 

### Example Response

 Details about the team role.

```json
{
  "id": "developer",
  "name": "Developer",
  "description": "Role for developers.",
  "createdAt": "2021-01-20T11:19:53.175Z",
  "updatedAt": "2021-01-20T11:19:53.175Z"
}
```

## JavaScript client reference

### Example request



```javascript
await apiClient.get.teamRole({
  parameters: {
    "teamId": "my-team",
    "roleId": "developer"
  }    
});
```

### Example Response

 Details about the team role.

```json
{
  "data": {
    "id": "developer",
    "name": "Developer",
    "description": "Role for developers.",
    "createdAt": "2021-01-20T11:19:53.175Z",
    "updatedAt": "2021-01-20T11:19:53.175Z"
  },
  "rawResponse": "...",
  "request": "...",
  "error": "..."
}
```

Previous: [Create team role](/docs/v1/api//team/team-roles/create-team-role)

Next: [Put team role](/docs/v1/api//team/team-roles/put-team-role)