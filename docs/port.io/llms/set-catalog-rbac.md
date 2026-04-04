# Source: https://docs.port.io/build-your-software-catalog/set-catalog-rbac.md

# Set catalog RBAC

[YouTube video player](https://www.youtube.com/embed/p-pNcvVfdUE)

<br />

Port provides granular control to ensure that every user only sees the parts of the catalog that are relevant to them.

Port's catalog RBAC capabilities are enabled by utilizing [permissions controls](/sso-rbac/users-and-teams/manage-users-teams.md).

Page permissions

In order to manage who can view certain **pages** in Port, check out [page permissions](/customize-pages-dashboards-and-plugins/page/page-permissions.md).

## Common usage[â](#common-usage "Direct link to Common usage")

The catalog RBAC mechanism allows admins to finely control which users have access to specific information in the software catalog, for example:

* Allow a user to edit a single specific property on an entity.
* Create a fully read-only view for a developer.

## Set access controls for catalog data[â](#set-access-controls-for-catalog-data "Direct link to Set access controls for catalog data")

The default permissions assigned to every blueprint upon creation specify that users with the `admin` role, and users with the specific blueprint `moderator` role, can perform any action on a blueprint.<br /><!-- -->See [RBAC permissions](/sso-rbac/users-and-teams/manage-users-teams.md) for more information about the different roles.

It is possible to assign global permissions controls for a blueprint's **entities**, using the following steps:

1. Go to the [Builder page](https://app.getport.io/settings/data-model) of your portal.

2. Select your desired blueprint, click on the `...` button in the top-right corner, and select `Permissions`:

3. A dialog will open, with the `Permissions` tab selected. Here you can set the permissions for the blueprint's entities.

Permissions are divided into the following sections:

* General
* Basic
* Advanced (entity owners)
* Advanced (dynamic read policy)

This section allows you to assign permissions for a **role** (Member, Admin or Moderator).

Click on the dropdown in the desired role row and select the permissions that will be assigned to it.

![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-dropdown-read.png)

<br />

<br />

**Set *granular* access controls to catalog data**

It is possible to assign more granular permissions controls on entities, allowing you to restrict users to editing only certain **properties** or **relations**.

To do so, open the permissions dropdown in the desired row, then click on `Update properties`.<br /><!-- -->This will open a dialog, where you can select the properties and relations that the selected role will be able to update.

![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-dropdown-update-properties.png)![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-choose-properties-and-relations.png)

**Edit via JSON (click to expand)**

To edit permissions via JSON, click on the `Edit JSON` button in the top-right corner of the dialog.

To give permissions to a role, add it to the `roles` array in the permission scope you desire (`read`, `register`, `unregister`, `update`, `updateProperties` or `updateRelations`):

```
{
  "entities": {
    "read": {
      "roles": ["myBlueprint-moderator", "Admin", "Member"],
      // ...other permissions
    },
    "register": {
      "roles": ["myBlueprint-moderator", "Admin", "Member"],
      // ...other permissions
    },
    "unregister": {
      "roles": ["myBlueprint-moderator", "Admin", "Member"],
      // ...other permissions
    },
    "update": {
      "roles": ["myBlueprint-moderator", "Admin", "Member"],
      // ...other permissions
    },
    "updateProperties": {
      "$identifier": {
        "roles": ["myBlueprint-moderator", "Admin", "Member"],
        // ...other permissions
      }
      // ...other properties
    },
    "updateRelations": {
      "service": {
        "roles": ["myBlueprint-moderator", "Admin", "Member"],
        // ...other permissions
      }
      // ...other relations
    }
  }
}
```

This section allows you to assign permissions for a **user** or **team**.

find a user or team

If there isn't currently a row for the user or team, search for them in search box and select them. This will also automatically give them Read access.

Click on the dropdown in the desired user or team row and select the permissions that will be assigned to it.

![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-dropdown-read-register.png)

<br />

"None"

If you see `None` as the permission, it means that the user or team only has permissions for `updateProperties` or `updateRelations`.

**Set *granular* access controls to catalog data**

It is possible to assign more granular permissions controls on entities, allowing you to restrict users to editing only certain **properties** or **relations**.

To do so, click on the dropdown in the desired row, then click on `Update properties`.<br /><!-- -->This will open a dialog, where you can select the properties and relations that the selected user or team will be able to update.

![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-dropdown-update-properties.png)![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-choose-properties-and-relations.png)

**Edit via JSON (click to expand)**

To edit permissions via JSON, click on the `Edit JSON` button in the top-right corner of the dialog.

To give permissions to a user or team, add the user or team identifier to the `users` or `teams` array in the permission scope you desire (`read`, `register`, `unregister`, `update`, `updateProperties` or `updateRelations`):

```
{
  "entities": {
    "read": {
      "users": ["my-user@example.port.io"],
      "teams": ["my-team"],
      // ...other permissions
    },
    "register": {
      "users": ["my-user@example.port.io"],
      "teams": ["my-team"],
      // ...other permissions
    },
    "unregister": {
      "users": ["my-user@example.port.io"],
      "teams": ["my-team"],
      // ...other permissions
    },
    "update": {
      "users": ["my-user@example.port.io"],
      "teams": ["my-team"],
      // ...other permissions
    },
    "updateProperties": {
      "$identifier": {
        "users": ["my-user@example.port.io"],
        "teams": ["my-team"],
        // ...other permissions
      }
      // ...other properties
    },
    "updateRelations": {
      "service": {
        "users": ["my-user@example.port.io"],
        "teams": ["my-team"],
        // ...other permissions
      }
      // ...other relations
    }
  }
}
```

This section allows you to assign permissions based on **entity owners**.

Click on the dropdown in the desired row and select the permissions that will be assigned to it.

![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-dropdown-none.png)

<br />

<br />

**Set *granular* access controls to catalog data**

It is possible to assign more granular permissions controls on entities, allowing you to restrict users to editing only certain **properties** or **relations**.

To do so, click on the dropdown in the desired row, then click on `Update properties`.<br /><!-- -->This will open a dialog, where you can select the properties and relations that the selected entity owners will be able to update.

![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-dropdown-update-properties.png)![](/img/software-catalog/role-based-access-control/permissions/blueprint-permission-choose-properties-and-relations.png)

**Edit via JSON (click to expand)**

To edit permissions via JSON, click on the `Edit JSON` button in the top-right corner of the dialog.

To give permissions to entity owners, set `ownedByTeam` to `true` in the permission scope you desire (`read`, `register`, `unregister`, `update`, `updateProperties` or `updateRelations`):

```
{
  "entities": {
    "read": {
      "ownedByTeam": true,
      // ...other permissions
    },
    "register": {
      "ownedByTeam":  true,
      // ...other permissions
    },
    "unregister": {
      "ownedByTeam":  true,
      // ...other permissions
    },
    "update": {
      "ownedByTeam":  true,
      // ...other permissions
    },
    "updateProperties": {
      "$identifier": {
        "ownedByTeam":  true,
        // ...other permissions
      }
      // ...other properties
    },
    "updateRelations": {
      "service": {
        "ownedByTeam":  true,
        // ...other permissions
      }
      // ...other relations
    }
  }
}
```

#### Important notes

* In the context of the `register` permission, setting a user or team as an entity owner means that they can only create a new entity if they assign it to a team that they are a member of.
* When entity owners permissions are configured the `Read` policy is ignored.

This section allows you to assign `read` permissions based on a **dynamic policy**.

![](/img/software-catalog/role-based-access-control/permissions/blueprint-permissions-read-policy-button.png)

**Edit via JSON (click to expand)**

To edit permissions via JSON, click on the `Edit JSON` button in the top-right corner of the dialog.

To configure a read policy, add a `policy` query to the `read` scope. The `policy` key allows you to give **dynamic** `read` permissions to users, by using [search queries](/search-and-query/structure-and-syntax.md#rules).

You can also use [contextual query rules](/search-and-query/structure-and-syntax.md#contextual-query-rules) to get the context of the user executing the query.

In the following example, `on-call` users are granted `read` access only to entities that share the same `region` as one of their owning teams:

```
{
  "entities": {
    // ...other scopes
    "read": {
      "policy": {
        "combinator": "and",
        "rules": [
          {
            "property": {
              "context" : "user",
              "property": "isOnCall"
            },
            "operator": "=",
            "value": "true"
          },
          {
            "property": "region",
            "operator": "containsAny",
            "value": {
              "context" : "userTeams",
              "property": "region"
            }
          },
        ]
      }
      // ...other permissions
    }
  }
}
```

conflicting permissions

When **entity owners** permissions are configured, the **dynamic read policy** is ignored.

Affected components

Setting `read` permissions on entities takes effect at the API level, meaning that any component in Port that fetches entities will be affected by these permissions.<br /><!-- -->For example, a table widget that displays entities will only show entities that the user has read permissions for.

## Permission simulator[â](#permission-simulator "Direct link to Permission simulator")

The permission simulator allows you to test and validate blueprint permissions before saving them.<br /><!-- -->You can simulate `read`, `register` (create), `update`, and `unregister` (delete) access for any user in your organization and quickly understand why access is granted or denied.

### Use the simulator[â](#use-the-simulator "Direct link to Use the simulator")

1. Go to the [Builder page](https://app.getport.io/settings/data-model), open a blueprint, and click `Permissions`.

2. In the **Permission Simulator** section at the bottom of the page, select:

   <!-- -->

   * A user from your organization.
   * An operation: `read`, `register` (create), `update`, or `unregister` (delete).

3. Review the results table to see all entities the selected user can access for the selected operation.

4. (Optional) Select a specific entity to open the detailed access breakdown.

5. In the detail view, review:

   <!-- -->

   * The visual flow (user â granted/denied â entity).
   * Which checks passed or failed.
   * The exact check that granted access (if access is granted).

Test changes before saving

The simulator evaluates pending permission changes from the form, not only the saved configuration.<br /><!-- -->This lets you verify impact in real time before applying your changes.

### How permissions are evaluated[â](#how-permissions-are-evaluated "Direct link to How permissions are evaluated")

The simulator evaluates five checks. Access is granted if **any one** of the following checks passes:

1. **Role check** - verifies whether the user's role is included in the operation's allowed `roles`.
2. **Owned by team** - when `ownedByTeam` is enabled, verifies whether the user belongs to at least one team in the entity's `$team`.
3. **Team list** - verifies whether the user belongs to any team listed in the operation's `teams`.
4. **User list** - verifies whether the user is explicitly listed in the operation's `users`.
5. **Policy** (read only) - for `read` simulations, verifies whether the entity matches the configured `policy` query.

When access is granted, the simulator indicates the granting path, for example: "Has role `Admin` which allows this operation".<br /><!-- -->For policy-based access, the evaluated query is also displayed.

## Software catalog RBAC examples[â](#software-catalog-rbac-examples "Direct link to Software catalog RBAC examples")

Refer to the [examples](/build-your-software-catalog/set-catalog-rbac/examples.md) page for practical examples of Port's RBAC.

## FAQ[â](#faq "Direct link to FAQ")

Since the catalog RBAC can be very granular, in some instances it might not be perfectly clear what the resulting assigned permissions would do, this part aims to provide some real-world examples and the behavior of Port's RBAC in those instances.

### What happens if a user lacks the permissions to edit a required property of the blueprint?[â](#what-happens-if-a-user-lacks-the-permissions-to-edit-a-required-property-of-the-blueprint "Direct link to What happens if a user lacks the permissions to edit a required property of the blueprint?")

In this case the user will not be able to register or update entities as a whole because they can't provide a value for the required property.

### What happens if the `ownedByTeam` setting is enabled for entity registration, but the user can't edit the `team` property?[â](#what-happens-if-the-ownedbyteam-setting-is-enabled-for-entity-registration-but-the-user-cant-edit-the-team-property "Direct link to what-happens-if-the-ownedbyteam-setting-is-enabled-for-entity-registration-but-the-user-cant-edit-the-team-property")

In this case the user will not be able to register a new entity since they can't select a value for the entity's team field and mark it as owned by their team.
