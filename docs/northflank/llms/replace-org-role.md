# Source: https://northflank.com/docs/v1/api/org/org-roles/replace-org-role.md

# Replace org role

Replaces all user-editable fields on a platform role for the authenticated org.

Required permission: Os > Admin > Roles > Manage

**Path parameters:**

{object}
- `roleId`: (string) (required) ID of the org role

**Request body:**

{object}
- `description`: (string) A description of the role. (pattern: ^[a-zA-Z0-9.,?\s\\/'"()[\];`%^&*\-_:!]+$) (max length: 200)
- `permissions`: {object}
  - `teamScope`: [array of] (string)
  - `projectScope`: [array of] (string)
  - `orgScope`: [array of] (string)
- `restrictions`: {object}
  - `enabled`: (boolean) (required) Whether restrictions are enabled.

**Response body:**

{object}
- `data`: {object}
  - `id`: (string) (required) ID of the role. (pattern: ^[A-Za-z0-9-]+$)
  - `name`: (string) (required) Display name of the role.
  - `description`: (string) Description of the role.
  - `restrictions`: {object}
    - `enabled`: (boolean) (required) Whether restrictions are enabled.
  - `createdAt`: (string) Creation time. (format: date-time)
  - `updatedAt`: (string) Last updated. (format: date-time)
  - `permissions`: {object}
    - `teamScope`: [array of] (string)
    - `projectScope`: [array of] (string)
    - `orgScope`: [array of] (string)

## API reference

PUT /v1/org-roles/{roleId}

### Example request

Request body

```curl
curl --header "Content-Type: application/json" \
  --header "Authorization: Bearer NORTHFLANK_API_TOKEN" \
  --request PUT \
  --data '{"description":"Role for developers."}' \
  https://api.northflank.com/v1/org-roles/{roleId}
```

```javascript
const payload = {
  "description": "Role for developers."
}

const response = await fetch('https://api.northflank.com/v1/org-roles/{roleId}', {
  method: 'PUT',
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

url = "https://api.northflank.com/v1/org-roles/{roleId}"

payload = {"description":"Role for developers."}
headers = {"Content-Type": "application/json", "Authorization": "Bearer NORTHFLANK_API_TOKEN"}

response = requests.request("PUT", url, headers = headers, json = payload)

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
  url := "https://api.northflank.com/v1/org-roles/{roleId}"

  var jsonStr = []byte(`{"description":"Role for developers."}`)
  req, err := http.NewRequest("PUT", url, bytes.NewBuffer(jsonStr))
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

200 OK: Details about the updated org role.

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

$ northflank update org-role

Options:

- `--roleId <roleId>`: ID of the org role

- `-f --file <file>`: Path to a JSON/YAML resource definition file

- `-i --input <definition>`: JSON/YAML resource definition string (takes precedence over --file)

- `--verbose `: Verbose output

- `--quiet `: No console output

- `-o --output <format>`: Output formatting 

```json
{
  "description": "Role for developers."
}
```

### Example Response

 Details about the updated org role.

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
await apiClient.update.orgRole({
  parameters: {
    "roleId": "developer"
  },
  data: {
    "description": "Role for developers."
  }    
});
```

### Example Response

 Details about the updated org role.

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

Previous: [Get org role](/docs/v1/api//org/org-roles/get-org-role)

Next: [Update org role](/docs/v1/api//org/org-roles/update-org-role)