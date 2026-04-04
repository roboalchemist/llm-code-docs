# Source: https://virustotal.readme.io/reference/get-activity-log.md

# Get Activity Logs

This endpoint is restricted to group administrators and retrieves the group's audit logs as follows, with all available relationships:

```json Example response
{
    "data": [ /* <_list of dictionaries_> List of logged actions */
        {
            "id": "<_string_> log identifier",
            "type": "activity_log_entry",
            "links": {
                "self": "https://www.virustotal.com/api/v3/activity_log_entries/<log identifier>"
            },
            "attributes": {/* <_dictionaries_> Logged action attributes */
                "info": {
                    "user": "<_string_> Identifier of the user that was affected by the action"
                },
                "ip": "<_string_> The IP address from which the user performed the action",
                "date": "<integer> UTC action timestamp",
                "action": "<_string_> Logged action such as: Remove admin from group, Add admin to group, etc"
            },
            "relationships": { /* <_dictionaries_> Dictionary of additional relationships that provide extra data */
                "group": {
                    "links": {
                        "self": "https://www.virustotal.com/api/v3/activity_log_entries/5323681776812032/relationships/group",
                        "related": "https://www.virustotal.com/api/v3/activity_log_entries/5323681776812032/group"
                    },
                    "meta": {
                        "count": 1
                    },
                    "data": {
                        "type": "group",
                        "id": "<_string_> Identifier of the group that was affected by the action"
                    }
                },
                "target": {
                    "links": {
                        "self": "https://www.virustotal.com/api/v3/activity_log_entries/<log identifier>/relationships/target",
                        "related": "https://www.virustotal.com/api/v3/activity_log_entries/<log identifier>/target"
                    },
                    "meta": {
                        "count": 1
                    },
                    "data": {
                        "type": "<_string_> Type of the entity that was affected by the action",
                        "id": "<_string_> Identifier of the entity that was affected by the action"
                    }
                },
                "user": {
                    "links": {
                        "self": "https://www.virustotal.com/api/v3/activity_log_entries/<log identifier>/relationships/user",
                        "related": "https://www.virustotal.com/api/v3/activity_log_entries/<log identifier>/user"
                    },
                    "meta": {
                        "count": 1
                    },
                    "data": {
                        "type": "user",
                        "id": "<_string_> Identifier of the user that performed the action"
                    }
                }
            }
        }
    ],
    "meta": {
        "count": "<_integer_> The total count of audit log entries",
        "cursor": "<_string_> Cursor"
    },
    "links": {
        "self": "https://www.virustotal.com/api/v3/groups/<group identifier>/activity_log_entries?limit=1",
        "next": "https://www.virustotal.com/api/v3/groups/<group identifier>/activity_log_entries?limit=1&cursor=CkYKEQoEZGF0ZRIJCMSl3uGjgJADEi1qEXN-dmlydXN0b3RhbGNsb3VkchgLEgtBY3Rpdml0eUxvZxiAgLHsxPP-CwwYACAB"
    }
} 
```

# Relationships

Logs may contain additional information in the form of relationships query parameter.

Available relationships are:

* `user`: provides information on the user that performed the action
* `group`: provides information on the group that was affected by the action
* `target`: provides information on the entity that was affected by the action. Currently, it refers only to a group, but we plan to expand this to include users, collections, and other entities in the future.

<Callout icon="🚧" theme="warn">
  Please note that although the UI displays the user who performed the action directly in the Username and User Email columns, this information is only accessible via the API through the user relationship.
</Callout>

# Filters

Available filters for logged actions retrieval:

* `date`: filters logs by date with YYYY-MM-DDTHH:MM:SS timestamp format. E.g.:`date:2025-10-27+`, `date:2025-10-27`, `date:2025-10-27-`
* `user`: filters logs by the identifier of the user who initiated the action. E.g.: `user:ana`.
* `target`: filters logs by the identifier of the targeted entity. Currently, only the group identifier, but we plan to expand supported targets to include users, collections, and other entities in the future. E.g.: `target:<my_group_id>`.
* `action`: filters logs by action performed. Available options are:  `ADD_GROUP_USER`, `DELETE_GROUP_USER`, `ADD_GROUP_ADMIN`, `DELETE_GROUP_ADMIN`,  `ADD_GROUP_SERVICE_ACCOUNT`, `DELETE_GROUP_SERVICE_ACCOUNT`, `CREATE_TENANT`, `DELETE_TENANT`. E.g.: `action:ADD_GROUP_USER`, `action:ADD_GROUP_SERVICE_ACCOUNT`

Note that several filters can be combined in the same request.

# Examples

Get all actions performed by the user Ana.

```python
import requests

group = "your group identifier"
filters="user:ana"
url = f"https://www.virustotal.com/api/v3/groups/{group}/activity_log_entries?filter={filters}"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

Get all logs related to giving admin privileges from August 2025, including the users that performed the action.

```python
import requests
import urllib

group = "your group identifier"
filters="date:2025-08-01+ AND date:2025-08-31- AND action:ADD_GROUP_ADMIN"
relationships = "user"
url = f"https://www.virustotal.com/api/v3/groups/{group}/activity_log_entries?filter={urllib.parse.quote(filters)}&relationships={relationships}"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

Get only the action and the IP address associated with each performed action.

```python
import requests

group = "your group identifier"
attributes = "action,ip"
url = f"https://www.virustotal.com/api/v3/groups/{group}/activity_log_entries?attributes={attributes}"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-enterprise",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [],
  "paths": {
    "/groups/{group}/activity_log_entries": {
      "get": {
        "summary": "Get Activity Logs",
        "description": "",
        "operationId": "get-activity-log",
        "parameters": [
          {
            "name": "group",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "filter",
            "in": "query",
            "description": "Filter logs by different properties",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "relationships",
            "in": "query",
            "description": "Provides additional information about the logs. Supported values: user, group, target",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of logs to retrieve. The maximum value is 40 logs.",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API Key.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
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
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
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