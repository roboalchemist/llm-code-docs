# Source: https://docs.curator.interworks.com/curator_api/api_docs/user_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User API

> User management API endpoints for creating and managing backend users

## /user/createBackendUser

Creates a backend user

**Returns:**

array

## /user/createFrontendGroup

Creates a Frontend Group.

*Note: To add members to your Frontend Group, use the addUserToGroup API endpoint.*

**Example Request:**

`POST [your_domain]/api/v1/User/createFrontendGroup?apikey=[your_api_key_here]&name=[group_name_here]`

```JSON  theme={null}
    {
        "platforms": {
            "tableau":[
                {
                    "server":"tableau us", // Name of your Tableau Server Connection
                    "site":"__DEFAULT__",
                    "group":"Alligator Admins" // Display Name of your Tableau Server Group
                }
            ],
            "thoughtspot":[
                "Europe Sales" // Display Name of your ThoughSpot Group
            ]
        },
        "custom_attributes": {
            "color": "blue"
        }
    }
```

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": "Successfully added platform groups to frontend group 30 and added syncing to the queue",
        "metadata": [
            {
                "tableau_server": "tableau us|||https://tableau.your-domain.com",
                "tableau_site": "__DEFAULT__",
                "tableau_group": "Alligator Admins|||[tableau_group_id_here]"
            },
            {
                "thoughtspot_group": "Europe Sales|||[thoughtspot_group_id_here]"
            }
        ],
        "tableauGroupsNotFound": "",
        "thoughtspotGroupsNotFound": ""
    }
```

## /user/fetchUser

Returns the currently logged in user's information.

**Returns:**

array

## /user/getManageablePermissions

Gets a listing of available manageable permissions

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "status": "Success",
        "permissions": [
            "InterWorks.datamanager.data_structure",
            "InterWorks.datamanager.data",
            "InterWorks.tableauviz.access_tableau_settings",
            "InterWorks.tableauviz.access_dashboards",
            "InterWorks.integration.manage_scripts",
            "InterWorks.integration.run_scripts",
            "InterWorks.integration.manage_commands",
            "InterWorks.integration.run_commands",
            "InterWorks.integration.manage_api_relay",
            "InterWorks.usermgmt.manage_backend_users",
            "InterWorks.usermgmt.manage_frontend_users",
            "InterWorks.content.access_content",
            "InterWorks.portal.access_portal_settings",
            "InterWorks.portal.manage_upgrade",
            "InterWorks.portal.api_keys"
        ]
    }
```

## /user/addUserToGroup

Adds a user to a group (syncs with Tableau if possible)

**Returns:**

array

## /user/listGroups

Lists groups.

**Returns:**

array

## /user/listUsers

Lists users and groups.

**Returns:**

array

## /user/removeUserFromGroup

Removes a user from a group (syncs with Tableau if possible)

**Returns:**

array
