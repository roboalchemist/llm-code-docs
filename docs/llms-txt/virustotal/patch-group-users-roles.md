# Source: https://virustotal.readme.io/reference/patch-group-users-roles.md

# Manage Roles

Use this endpoint to manage users' **group roles** and **feature permissions** as well as users' **daily API allowance**.

For roles and feature permissions, the following operations are available in the request body:

* `roles`: replaces all existing roles with the ones provided in the request.
* `add_roles`: appends new roles to the user. If a role already exists, it will be updated with the new configuration.
* `remove_roles`: revokes only the specific roles provided in the request.

Existing privileges are:

* `USER_ROLE_GROUP_ADMIN`: for group administrators
* `USER_ROLE_PRIVATE_SCANNING`: for access to Private Scanning

For managing users' daily API allowance, the `allowed` field must be specified within the `context_attributes` -> `quota_limits` -> `api_requests_daily` object, as shown in the example below.

# Examples

Lower the user's daily API cap to 10.

```python
import requests

group_id = "my_group_id"
user_id = "user_1"
allowance = 10

url = f"https://www.virustotal.com/api/v3/groups/{group_id}/relationships/users"
payload = {
    'data': [
        {
            'type': 'user',
            'id': user_id,
            'context_attributes': {
                'quota_limits': {
                    'api_requests_daily': {
                        'allowed': allowance
                    }
                }
            }
        }
    ]
}
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
}
res = requests.patch(url, json=payload, headers=headers)
```

Clear all individual settings and grant administrative privileges within the group to both user\_1 and user\_2.

```python
import requests

group_id = "my_group_id"  
user_id_1 = "user_1"  
user_id_2 = "user_2"  
roles = ["USER_ROLE_GROUP_ADMIN"]

url = f"<https://www.virustotal.com/api/v3/groups/{group_id}/relationships/users">  
payload = {  
    'data': [  
        {  
            'type': 'user',  
            "id": user_id_1,  
            'context_attributes': {  
                'roles': roles  
            }  
        },  
        {  
            'type': 'user',  
            "id": user_id_2,  
            'context_attributes': {  
                'roles': roles  
            }  
        }  
    ]  
}  
headers = {  
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"  
}  
res = requests.patch(url, json=payload, headers=headers)
```

Grant the user access to Private Scanning.

```python
import requests

group_id = "my_group_id"  
user_id = "user_1"  
roles = ["USER_ROLE_PRIVATE_SCANNING"]

url = f"<https://www.virustotal.com/api/v3/groups/{group_id}/relationships/users">  
payload = {  
    'data': [  
        {  
            'type': 'user',  
            "id": user_id,  
            'context_attributes': {  
                'add_roles': roles  
            }  
        }  
    ]  
}  
headers = {  
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"  
}  
res = requests.patch(url, json=payload, headers=headers)
```

Revoke the user's access to Private Scanning.

```python
import requests

group_id = "my_group_id"  
user_id = "user_1"  
roles = ["USER_ROLE_PRIVATE_SCANNING"]

url = f"<https://www.virustotal.com/api/v3/groups/{group_id}/relationships/users">  
payload = {  
    'data': [  
        {  
            'type': 'user',  
            "id": user_id,  
            'context_attributes': {  
                'remove_roles': roles  
            }  
        }  
    ]  
}  
headers = {  
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"  
}  
res = requests.patch(url, json=payload, headers=headers)
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/groups/{id}/relationships/users": {
      "patch": {
        "description": "",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Group id"
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key.",
            "required": true
          }
        ],
        "operationId": "patch_groups-id-relationships-users",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "string",
                    "format": "json"
                  }
                },
                "required": [
                  "data"
                ]
              }
            }
          }
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```