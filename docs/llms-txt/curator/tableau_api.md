# Source: https://docs.curator.interworks.com/curator_api/api_docs/tableau_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tableau API

> Tableau API endpoints for dashboard creation and management through Curator

## /Tableau/createDashboard

Creates a Dashboard record

**Common Parameters:**

* **title** *required*
  The title of your Dashboard
* **url** *required*
  This is the url of the Dashboard on the Tableau Server environment.
* **slug**
  This is the url of the Dashboard on the Curator environment.

***Note:** Other optional parameters, such as keywords, featured, etc. are supported but not listed here.*

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "success",
        "msg": "Created Dashboard record",
        "Dashboard": {...},
    }
```

## /Tableau/syncTags

Kicks off tag schedule which synchronizes tags from Tableau Server

**Returns:**

string

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": "Tag sync is complete"
    }
```

## /Tableau/syncGroups

Kicks off a schedule which synchronizes groups from Tableau Server.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": "Group sync is complete"
    }
```

## /Tableau/listUsers

Lists users and groups.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    [
        {
            "tableau_user_id": "21342134-236a-49f9-88e9-224272ab312c",
            "name": "CuratorDemo",
            "full_name": "Curator Demo",
            "site_role": "SiteAdministrator",
            "skip_sync": null,
            "groups": []
        },
        {
            "tableau_user_id": "12341234-89a3-4fde-acd9-a3b806995d69",
            "name": "admin",
            "full_name": "Administrator",
            "site_role": "ServerAdministrator",
            "skip_sync": null,
            "groups": []
        }
    ]
```

## /Tableau/setAuthentication

Sets the authentication type.

**Returns:**

array

## Tableau/setRest

Sets the REST credentials for Tableau Server Settings.

**Returns:**

array

## /Tableau/syncTableauDashboardIds

Kicks off tag schedule which synchronizes tags from Tableau Server

**Returns:**

string

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /Tableau/resetViews

Kicks off a schedule task which clears out the Dashboard views

**Returns:**

string

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /Tableau/refreshGroups

Kicks off tag schedule which clears the old groups and adds in new groups

**Returns:**

string

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /Tableau/refreshThumbnails

Kicks off task which refreshes all thumbnails.

**Returns:**

string

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": "Dashboard thumbnails are refreshed."
    }
```
