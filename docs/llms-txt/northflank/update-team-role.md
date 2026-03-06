# Source: https://northflank.com/docs/v1/api/team/team-roles/update-team-role.md

# Update team role

Updates a platform role for a team.

Required permission: Account > Admin > Roles > Manage

**Path parameters:**

{object}
- `teamId`: (string) (required) ID of the team
- `roleId`: (string) (required) ID of the team role

**Request body:**

{object}
- `name`: (string) The name of the role.
- `description`: (string) A description of the role. (pattern: ^[a-zA-Z0-9.,?\s\\/'"()[\];`%^&*\-_:!]+$) (max length: 200)
- `permissions`: {object}
  - `teamScope`: [array of] (string)
  - `projectScope`: [array of] (string)
- `restrictions`: {object}
  - `enabled`: (boolean) (required) Whether project restrictions are enabled.
  - `projects`: [array of] (string)
  - `restrictionMode`: (string) Whether the restriction is inclusive or exclusive. (enum: in, not-in)
- `members`: [array of] (string)

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

PATCH /v1/teams/{teamId}/roles/{roleId}

### Example request

Request body

```curl
curl --header "Content-Type: application/json" \
  --header "Authorization: Bearer NORTHFLANK_API_TOKEN" \
  --request PATCH \
  --data '{"name":"Developer","description":"Role for developers."}' \
  https://api.northflank.com/v1/teams/{teamId}/roles/{roleId}
```

```javascript
const payload = {
  "name": "Developer",
  "description": "Role for developers."
}

const response = await fetch('https://api.northflank.com/v1/teams/{teamId}/roles/{roleId}', {
  method: 'PATCH',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${NORTHFLANK_API_TOKEN}`
  },
  body: JSON.stringify(payload)
})

const json = await response.json()
console.log(json)
```

```python
import requests

url = "https://api.northflank.com/v1/teams/{teamId}/roles/{roleId}"

payload = {"name":"Developer","description":"Role for developers."}
headers = {"Content-Type": "application/json", "Authorization": "Bearer NORTHFLANK_API_TOKEN"}

response = requests.request("PATCH", url, headers = headers, json = payload)

print(response.json())
```

```go
package main

import (
  "bytes"
  "fmt"
  "io/ioutil"
  "net/http"
)

func main() {
  url := "https://api.northflank.com/v1/teams/{teamId}/roles/{roleId}"

  var jsonStr = []byte(`{"name":"Developer","description":"Role for developers."}`)
  req, err := http.NewRequest("PATCH", url, bytes.NewBuffer(jsonStr))
  req.Header.Set("Content-Type", "application/json")
  req.Header.Set("Authorization", "Bearer NORTHFLANK_API_TOKEN")

  client := &http.Client{}
  resp, err := client.Do(req)
  if err != nil {
    panic(err)
  }
  defer resp.Body.Close()

  fmt.Println("Response status:", resp.Status)
  fmt.Println("Response headers:", resp.Header)
  body, _ := ioutil.ReadAll(resp.Body)
  fmt.Println("Response body:", string(body))
}
```

### Example Response

200 OK: Details about the updated team role.

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

$ northflank patch team-role

Options:

- `--teamId <teamId>`: ID of the team

- `--roleId <roleId>`: ID of the team role

- `-f --file <file>`: Path to a JSON/YAML resource definition file

- `-i --input <definition>`: JSON/YAML resource definition string (takes precedence over --file)

- `--verbose `: Verbose output

- `--quiet `: No console output

- `-o --output <format>`: Output formatting 

```json
{
  "name": "Developer",
  "description": "Role for developers."
}
```

### Example Response

 Details about the updated team role.

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

Request body

```javascript
await apiClient.patch.teamRole({
  parameters: {
    "teamId": "my-team",
    "roleId": "developer"
  },
  data: {
    "name": "Developer",
    "description": "Role for developers."
  }    
});
```

### Example Response

 Details about the updated team role.

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

Previous: [Put team role](/docs/v1/api//team/team-roles/put-team-role)

Next: [Delete team role](/docs/v1/api//team/team-roles/delete-team-role)