# Source: https://docs.curator.interworks.com/curator_api/api_docs/content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Content

> Content API endpoints for creating and managing files and content within Curator

## /content/createFile

Creates a file model

Example Usage:

[Python Script](https://curator.interworks.com/file/api-example-createfile)

**Parameters:**
**file**

The file

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /content/createNavMenu

Creates a nav menu model

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /content/deleteFile

deletes a file model by ID

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /content/listFiles

Lists file content types.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    [
        {
            "id": 1,
            "title": "HexTileAlt",
            "description": "",
            "slug": "hex-tile-alt",
            "restrict_group_access": 0,
            "created_at": "2017-09-12 16:11:10",
            "updated_at": "2017-09-12 16:11:10"
        },
        {
            "id": 2,
            "title": "Logo 196",
            "description": "",
            "slug": "logo-196",
            "restrict_group_access": 0,
            "created_at": "2017-12-15 17:15:07",
            "updated_at": "2017-12-15 17:15:07"
        }
    ]
```

## /content/listDashboards

Lists Tableau dashboard content types with associated keywords.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    [
        {
            "id": 1,
            "title": "Sales Dashboard",
            "description": "Dashboard showing sales metrics",
            "slug": "sales-dashboard",
            "url": "https://tableau.example.com/#/views/Sales/Dashboard",
            "server": "https://tableau.example.com",
            "site": "Default",
            "restrict_group_access": 0,
            "created_at": "2023-01-15 10:30:00",
            "updated_at": "2024-01-10 14:22:00",
            "keywords": [
                {
                    "id": 2,
                    "title": "Scorecard",
                    "created_at": "2023-08-15T10:24:49.000000Z",
                    "created_by": "admin (backend)",
                    "updated_at": "2023-08-21T07:53:26.000000Z",
                    "updated_by": "admin (backend)",
                    "favoritable": 1,
                    "pivot": {
                        "dashboard_id": 1,
                        "keyword_id": 2
                    }
                },
                {
                    "id": 4,
                    "title": "Pink Cards",
                    "created_at": "2023-08-23T07:28:05.000000Z",
                    "created_by": "admin (backend)",
                    "updated_at": "2023-08-23T07:28:05.000000Z",
                    "updated_by": "admin (backend)",
                    "favoritable": 1,
                    "pivot": {
                        "dashboard_id": 1,
                        "keyword_id": 4
                    }
                }
            ]
        },
        {
            "id": 2,
            "title": "Marketing Dashboard",
            "description": "",
            "slug": "marketing-dashboard",
            "url": "https://tableau.example.com/#/views/Marketing/Overview",
            "server": "https://tableau.example.com",
            "site": "Default",
            "restrict_group_access": 0,
            "created_at": "2023-02-20 09:15:00",
            "updated_at": "2023-12-05 11:45:00"
        }
    ]
```

## /content/listNavMenus

Lists nav menu links.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    [
        {
            "id": 1,
            "parent_id": null,
            "title": "Main Menu",
            "description": "The main menu items",
            "url": null,
            "enabled": 1,
            "parameters": null,
            "query_string": null,
            "is_external": 0,
            "link_target": "_self",
            "created_at": {
                "date": "2017-10-08 14:51:28.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "updated_at": {
                "date": "2018-03-08 19:41:42.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "link_type": "custom_url",
            "notice_id": null,
            "restrict_group_access": 0
        },
        {
            "id": 2,
            "parent_id": 1,
            "title": "Home",
            "description": "Website Home Page",
            "url": "home",
            "enabled": 1,
            "parameters": null,
            "query_string": null,
            "is_external": 0,
            "link_target": "_self",
            "created_at": {
                "date": "2017-10-08 14:51:28.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "updated_at": {
                "date": "2018-01-16 15:24:38.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "link_type": "custom_url",
            "notice_id": null,
            "restrict_group_access": 0
        }
    ]
```
