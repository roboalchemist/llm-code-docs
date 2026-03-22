# Source: https://docs.roboflow.com/developer/rest-api/manage-project-folders.md

# Manage Project Folders

You can manage your Project Folders programmatically using the Roboflow API.

**Note:** This feature is only available for Enterprise workspaces.

**Note**: Your `api_key` must be sent in all requests. The `api_key` can be sent as a query parameter or as a top level attribute in the post body.

## Creating a Project Folder

<mark style="color:green;">`POST`</mark> `/:workspace/groups`

Creates a Project Folder.

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Body**

<table><thead><tr><th width="164">Name</th><th width="223">Type</th><th width="287">Description</th><th data-type="checkbox">Required</th></tr></thead><tbody><tr><td><code>api_key</code></td><td>string</td><td>The api key of the workspace where the Project Folder should be created</td><td>true</td></tr><tr><td><code>name</code></td><td>string</td><td>The name of the Project Folder</td><td>false</td></tr><tr><td><code>projects</code></td><td>Array&#x3C;string></td><td>A list of ids of projects that should be moved to this folder</td><td>false</td></tr><tr><td><code>external_id</code></td><td>string</td><td>The id of this Project Folder in an external system</td><td>false</td></tr><tr><td><code>auth_groups</code></td><td>Map&#x3C;"read" | "write<br>, Array&#x3C;string></td><td>A list of permission groups that should have read/write access to the projects within this Folder. (Note: please contact Roboflow before using this feature as it requires additional set up)</td><td>false</td></tr></tbody></table>

#### Example Request

```
curl --location 'https://api.roboflow.com/<workspace_id>/groups?api_key=<api_key>' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Client Demos",
    "projects": ["client-demo-project-1", "another-project-id"],
    "external_id": "jfowke123jfiowje",
    "auth_groups": {
        "read": [],
        "write": []
    }
}'
```

**Response**

{% tabs %}
{% tab title="200" %}

```json
{
  "id": "<project_folder_id>"
}
```

{% endtab %}

{% tab title="401" %}

```json
{
  "error": "Invalid request"
}
```

{% endtab %}
{% endtabs %}

## Get Project Folder

<mark style="color:green;">`GET`</mark> `/:workspace/groups/:folderId`

Retrieves a Project Folder by ID

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Query**

<table><thead><tr><th>Name</th><th>Type</th><th>Description</th><th data-type="checkbox">Required</th></tr></thead><tbody><tr><td><code>api_key</code></td><td>string</td><td>API Key of workspace where Project Folder exists</td><td>true</td></tr></tbody></table>

**Example Request**

```
curl --location 'https://api.roboflow.com/<workspace_id>/groups?api_key=<your_api_key>' \
--header 'Content-Type: application/json'
```

**Response**

{% tabs %}
{% tab title="200" %}

```json
{
  "data": Array<#ProjectFolder>
}
```

{% endtab %}

{% tab title="404" %}
The project folder specified by the `folderId` param does not exist, or no project folders exist in the workspace that belongs to the provided api key
{% endtab %}
{% endtabs %}

## Update a Project Folder

<mark style="color:green;">`POST`</mark> `/:workspace/groups/:folderId`

Updates a Project Folder's properities

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Query**

<table><thead><tr><th>Name</th><th></th><th></th><th data-type="checkbox">Required</th></tr></thead><tbody><tr><td><code>returnUpdated</code></td><td>boolean</td><td>When set, returns the full resource payload in the response</td><td>false</td></tr></tbody></table>

**Body**

<table><thead><tr><th width="164">Name</th><th width="223">Type</th><th width="287">Description</th><th data-type="checkbox">Required</th></tr></thead><tbody><tr><td><code>api_key</code></td><td>string</td><td>The api key of the workspace where the Project Folder should be created</td><td>true</td></tr><tr><td><code>name</code></td><td>string</td><td>The name of the Project Folder</td><td>false</td></tr><tr><td><code>projects</code></td><td>Array&#x3C;string></td><td>A list of ids of projects that should be moved to this folder</td><td>false</td></tr><tr><td><code>external_id</code></td><td>string</td><td>The id of this Project Folder in an external system</td><td>false</td></tr><tr><td><code>auth_groups</code></td><td>Map&#x3C;"read" | "write<br>, Array&#x3C;string></td><td>A list of permission groups that should have read/write access to the projects within this Folder. (Note: please contact Roboflow before using this feature as it requires additional set up)</td><td>false</td></tr></tbody></table>

**Example Request**

```
curl --location 'https://api.roboflow.com/<workspace_id>/groups/<folder_id>?api_key=<api_key>&returnUpdated=true' \
--header 'Content-Type: application/json' \
--data '{
    "name": "A new name"
}'
```

**Response**

{% tabs %}
{% tab title="204" %}
No Content. Resource was updated successfully
{% endtab %}

{% tab title="200" %}

```
// Only when query param ?returnUpdated=true
{
    "data": Array<#ProjectFolder>
}
```

{% endtab %}
{% endtabs %}

## Add Project(s) to Folder

<mark style="color:green;">`PATCH`</mark> `/:workspace/groups/:folderId/projects`

Adds one or more projects to an existing folder

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Body**

<table><thead><tr><th>Name</th><th>Type</th><th>Description</th><th data-type="checkbox">Required</th></tr></thead><tbody><tr><td><code>projects</code></td><td>Array&#x3C;string></td><td>A list of project ids to add to the Project Folder</td><td>true</td></tr></tbody></table>

**Example Request**

```
curl --location --request PATCH 'https://api.roboflow.com/<workspace_id>/groups/example-folder-id/projects?api_key=<api_key>' \
--header 'Content-Type: application/json' \
--data '{
    "projects": ["dog-breeds-mi53"]
}'
```

**Response**

{% tabs %}
{% tab title="204" %}
No Content. Project was added to the group successfully
{% endtab %}
{% endtabs %}

## Remove Project(s) to Folder

<mark style="color:red;">`DELETE`</mark> `/:workspace/groups/:folderId/projects`

Removes one or more projects from an existing folder and places it back into the top level workspace

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Body**

<table><thead><tr><th>Name</th><th>Type</th><th>Description</th><th data-type="checkbox">Required</th></tr></thead><tbody><tr><td><code>projects</code></td><td>Array&#x3C;string></td><td>A list of project ids to remove from the Project Folder</td><td>true</td></tr></tbody></table>

**Example Request**

```
curl --location --request PATCH 'https://api.roboflow.com/<workspace_id>/groups/example-folder-id/projects?api_key=<api_key>' \
--header 'Content-Type: application/json' \
--data '{
    "projects": ["dog-breeds-mi53"]
}'
```

**Response**

{% tabs %}
{% tab title="204" %}
No Content. Project was removed from the group successfully
{% endtab %}
{% endtabs %}

## Delete Project Folder

<mark style="color:red;">`DELETE`</mark> `/:workspace/groups/:folderId`

Deletes a project Folder. All projects within the folder will be placed back into the top level workspace and not deleted.

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Example Request**

<pre><code><strong>curl --location --request DELETE 'https://api.roboflow.com/&#x3C;workspace_id>/groups/example-folder-id/projects?api_key=&#x3C;api_key>' \
</strong>--header 'Content-Type: application/json'
</code></pre>

**Response**

{% tabs %}
{% tab title="204" %}
No Content. Project Folder was successfully deleted
{% endtab %}
{% endtabs %}
