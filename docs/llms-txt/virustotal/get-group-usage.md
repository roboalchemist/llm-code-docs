# Source: https://virustotal.readme.io/reference/get-group-usage.md

# Get a group's usage per feature

This endpoint retrieves a group's usage data for a **specified feature**, **broken down by user**.

```json Example response
{
    "data": /* <_list of dictionaries_> List of users */
    [
        {
            "id": "<_string_> User identifier",
            "type": "user",
            "links":
            {
                "self": "https://www.virustotal.com/api/v3/users/<user identifier>"
            },
            "attributes": "<_dictionary_> User object attributes. When the 'attributes' request parameter is used, only specified attributes are listed. ",
            "relationships": /* <_list of dictionaries_> (optional) List of objects descriptors related to the user. It is included only when the 'relationships' request parameter is used. */
            {
                "<_string_> Relationship name":
                {
                    "data": /* <_list of dictionaries_> List of objects descriptors. */
                    [
                        {
                            "type": "<_string_> Object type",
                            "id": "<_string_> Object identifier"
                        }
                    ],
                    "links":
                    {
                        "self": "https://www.virustotal.com/api/v3/users/<user identifier>/relationships/<relationship name>?limit=20",
                        "related": "https://www.virustotal.com/api/v3/users/<user identifier>/<object type>"
                    }
                }
            },
            "context_attributes":
            {
                "quota_consumed_from_group": "<_integer_> Consumed specified feature quota"
            }
        }
    ],
    "links":
    {
        "self": "https://www.virustotal.com/api/v3/groups/gti_testers/users_consuming_quota/..."
    }
}
```

By default, all user attributes are included. To retrieve a specific subset, provide a comma-separated list of desired [user attributes](https://virustotal.readme.io/reference/user-object#object-attributes) using the `attributes` request parameter.

Additionally, you can specify the desired types of user relationships (e.g., votes, graphs, comments, or mentions) by providing a comma-separated list of them using the `relationships` request parameter.

You can also sort users by their consumption of the chosen feature, in either ascending (`asc`) or descending (`desc`) order, using the `order` request parameter.

> 🚧 Time range restrictions
>
> This endpoint supports a maximum time range of the current and the 2 previous months. The `period` request parameter can be specified in two formats (YYYY-MM, YYYY-MM-DD), depending on the requested feature, to retrieve data for a particular month.

Available features and `period` formats are:

* `intelligence_hunting_rules` - count of active Livehunt jobs per user. They are not tied to a period of time so they don't support the `period` request parameter.
* `api_requests_daily` - daily count of API requests per user. `period` formats: YYYY-MM (complete month consumption), YYYY-MM-DD (specific day consumption).
* `api_requests_monthly` - monthly count of API requests per user. `period` formats: YYYY-MM (complete month consumption), YYYY-MM-DD (specific day consumption).
* `intelligence_downloads_monthly` - monthly count of files downloads per user. `period` format: YYYY-MM.
* `intelligence_retrohunt_jobs_monthly` - monthly count of Retrohunt jobs per user. `period` format: YYYY-MM.
* `intelligence_vtdiff_creation_monthly` - monthly count of VTDiff jobs per user. `period` format: YYYY-MM.
* `intelligence_searches_monthly` - monthly count of Intelligence Searches per user. `period` format: YYYY-MM.
* `private_scans_monthly` - monthly count of File Private Scans per user. `period` format: YYYY-MM.
* `private_urlscans_monthly` - monthly count of URL Private Scans per user. `period` format: YYYY-MM.

If the `period` parameter is not specified, you will get the current month consumption.

# Examples

Get consumption of web interface intelligence searches from the past month (2025-04).

```python
import requests

id = "your group identifier"
quota_name = "intelligence_searches_monthly"

url = f"https://www.virustotal.com/api/v3/groups/{id}/users_consuming_quota/{quota_name}?period=2025-04"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

Get API consumption from 2025-05-06 of all users and their votes and comments.

```python
import requests

id = "your group identifier"
quota_name = "api_requests_daily"

url = f"https://www.virustotal.com/api/v3/groups/{id}/users_consuming_quota/{quota_name}?period=2025-05-06&relationships=votes,comments"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

List 10 users (email address and 2FA status) who have downloaded the most files in the last month, via web interface.

```python
import requests

id = "your group identifier"
quota_name = "intelligence_downloads_monthly"
attributes = "email,has_2fa"

url = f"https://www.virustotal.com/api/v3/groups/{id}/users_consuming_quota/{quota_name}?order=desc&limit=10&attributes={attributes}"
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
    "/groups/{id}/users_consuming_quota/{quota_name}": {
      "get": {
        "description": "",
        "responses": {
          "200": {
            "description": ""
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
            "description": "Group ID"
          },
          {
            "in": "path",
            "name": "quota_name",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Quota Name"
          },
          {
            "in": "query",
            "name": "period",
            "schema": {
              "type": "string"
            },
            "description": "A string in format YYYY-MM-DD (for daily quotas) or YYYY-MM (for monthly quotas)",
            "required": false
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "format": "int32"
            },
            "required": false,
            "description": "Maximum number of users quota to retrieve (Max 40)"
          },
          {
            "in": "query",
            "name": "order",
            "schema": {
              "type": "string"
            },
            "description": "Sort users based on their consumption ('desc' for descendant, 'asc' for ascendant)"
          },
          {
            "in": "query",
            "name": "attributes",
            "schema": {
              "type": "string"
            },
            "description": "Comma-separated users' attributes to return (by default, all attributes are returned)"
          },
          {
            "in": "query",
            "name": "relationships",
            "schema": {
              "type": "string"
            },
            "description": "Comma-separated users' [relationships](https://virustotal.readme.io/reference/user-object#relationships) to return (by default, no relationships are returned)"
          },
          {
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            },
            "description": "Continuation cursor"
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API key"
          }
        ],
        "operationId": "get_groups-id-users-consuming-quota-quota-name"
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