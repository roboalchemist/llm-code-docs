# Source: https://docs.pentaho.com/pba/semantic-model-editor/sharing-a-semantic-model/permissions-for-semantic-models.md

# Permissions for semantic models

The Semantic Model Editor permissions model defines how a user accesses and manages semantic models. Users inherit permissions from their individual assignments, roles, and groups. By default, no access is granted unless explicitly assigned.

There are two permission levels:

* [Global permissions](#global-permissions) apply across all models.
* [Content-level permissions](#content-level-permissions) apply to specific models.

For a user to be allowed to perform a given action in Semantic Models, the user needs to be authorized simultaneously at these two levels (global and content) for that action.

## Global permissions

Permissions for the Semantic Model Editor that are available to administrators for assigning to users, roles, or groups.&#x20;

{% hint style="warning" %}
**Important:** To grant an ability to a user, you must manually assign both the global permission and corresponding content-level permission for that ability to the user. Inherited permissions do not currently satisfy validation requirements for granting an ability to a user.
{% endhint %}

<table><thead><tr><th width="253.11114501953125">Permission</th><th>Grants ability</th></tr></thead><tbody><tr><td>Display SME entry point</td><td>Access the Semantic Model Editor UI</td></tr><tr><td>View semantic models</td><td>View accessible models</td></tr><tr><td>Create semantic models</td><td>Create models</td></tr><tr><td>Edit semantic models</td><td>Edit accessible models</td></tr><tr><td>Delete semantic models</td><td>Delete accessible models</td></tr><tr><td>Change connection</td><td>Modify accessible models connection</td></tr><tr><td>Share semantic models</td><td>Share accessible models</td></tr><tr><td>Import semantic models</td><td>Manage imported models</td></tr></tbody></table>

## Content-level permissions

Permissions for individual semantic models that the owner of the model can assign to other users on the platform.&#x20;

{% hint style="warning" %}
**Important:** To grant an ability to a user, you must manually assign both the content-level permission and corresponding global permission for that ability to the user. Inherited permissions do not currently satisfy validation requirements for granting an ability to a user.
{% endhint %}

Only users with the Share permission (and the corresponding global permissions) can assign content-level permissions to others. Users can grant only permissions they also hold at both the global and content levels.

<table><thead><tr><th width="254.888916015625">Permission</th><th>Grants ability (if global permission also exists)</th></tr></thead><tbody><tr><td>View</td><td>View the model</td></tr><tr><td>Edit</td><td>Edit the model</td></tr><tr><td>Delete</td><td>Delete the model</td></tr><tr><td>Change connection</td><td>Change the connection used in the model</td></tr><tr><td>Share</td><td>Share the model</td></tr></tbody></table>

## Permission inheritance

{% hint style="warning" %}
**Important:** Inherited permissions do not currently satisfy validation requirements for granting an ability to the user. If the user is not manually assigned both the content-level and global permission for an ability, the ability is not granted.
{% endhint %}

The following permissions automatically grant related permissions at the same level, either the content-level or global level, to ensure consistent functionality:

| Assigned permission | Also grants |
| ------------------- | ----------- |
| Create              | Share, View |
| Edit                | View        |
| Share               | View        |
| Import              | Share, View |

**Example:** Assigning **Edit** also grants **View**.
