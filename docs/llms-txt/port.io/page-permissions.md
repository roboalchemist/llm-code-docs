# Source: https://docs.port.io/customize-pages-dashboards-and-plugins/page/page-permissions.md

# Page permissions

Page permissions are used to control access to [catalog pages](/customize-pages-dashboards-and-plugins/page/catalog-page.md) and [dashboard pages](/customize-pages-dashboards-and-plugins/page/dashboard-page.md) in the software catalog.

Using these permissions, you can control which users and/or teams can **view** or **edit** a specific page.

## Update page permissions[â](#update-page-permissions "Direct link to Update page permissions")

Only users with the `admin` role can update the permissions of a catalog page.

Admins can:

* Define which users and/or teams can **view** the page.
* Define which users and/or teams can **edit** the page.
* Allow all users in the organization to **view** the page.

Update page permissions using one of the following methods:

* UI
* API
* Terraform
* Pulumi

Click on the permissions ![](/img/icons/permissions.svg) button in the top-right corner of the page.

Choose the user/s or team/s that you would like to give `view` or `edit` permissions to, then click on `Done`.

To allow all users in the organization to view the page, use the toggle in the bottom of the permissions modal.

To update page permissions, you will need to specify the roles, teams or users that should have permissions for the page.

To perform an update, make an **HTTP PATCH** request to the following URL: `https://api.port.io/v1/pages/{page_identifier}/permissions`.

Here is an example request body that updates the permissions to allow all users in the organization to **view** the page:

```
{
  "read": {
    "roles": ["Admin", "Member"]
  }
}
```

Here is another example that updates the permissions to allow a specific user and team to **edit** the page:

```
{
  "update": {
    "users": ["user1@example.com"],
    "teams": ["team1"]
  }
}
```

Page permissions API

The `PATCH` API will perform updates only to keys that are specified in the request body. Be sure to include only the relevant keys in the request body (users, roles or teams)

If you do not specify a specific key (for example `users` in the request, user permissions to the specific page will remain unchanged).

When making changes to permissions, any role, user or team that does not appear in the corresponding key in the request body will lose permissions to the page (this is how you remove permissions).

See the [Terraform provider documentation](https://registry.terraform.io/providers/port-labs/port-labs/latest/docs/resources/port_page_permissions#example-usage) for examples.

Port Pulumi

See all the supported variables in the Port Pulumi [documentation](https://www.pulumi.com/registry/packages/port/api-docs/pagepermissions/#create)

* Python
* Typescript
* Golang

```
from port_pulumi import Page, PagePermissions

# Allow read access to all admins and a specific user and team:
microservices_permissions = PagePermissions(
    "microservices_permissions",
    page_identifier="microservice_blueprint_page",
    read={
        "roles": [
            "Admin",
        ],
        users: ["normaluser@gmail.com"],
        teams: ["Super Team"],
    },
)
```

```
import * as port from "@port/pulumi";

// Allow read access to all admins and a specific user and team:
const microservicesPermissions = new port.PagePermissions("microservices_permissions", {
    pageIdentifier: "microservice_blueprint_page",
    read: {
        roles: ["Admin"],
        users: ["normaluser@gmail.com"],
        teams: ["Super Team"],
    },
});
```

```
package main

import (
	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	ctx := pulumi.NewContext()
	
	// Allow read access to all admins and a specific user and team:
	microservicesPermissions, err := port.NewPagePermissions(ctx, "microservices_permissions", &port.PagePermissionsArgs{
		PageIdentifier: pulumi.String("microservice_blueprint_page"),
		Read: &port.PagePermissionsReadArgs{
			Roles: pulumi.StringArray{
				pulumi.String("Admin"),
			},
			Users: pulumi.StringArray{
				pulumi.String("normaluser@gmail.com"),
			},
			Teams: pulumi.StringArray{
				pulumi.String("Super Team"),
			},
		},
	})
	if err != nil {
		// Handle error
	}
	// You can use the microservicesPermissions variable as needed in your code.
}
```

### Examples[â](#examples "Direct link to Examples")

Let's present a set of page permissions and then explore how different `PATCH` request bodies change the effective permissions of the page.

Given the following permissions for a page:

```
{
  "read": {
    "roles": ["Admin", "Member"],
    "users": [],
    "teams": []
  }
}
```

#### Add permissions to role[â](#add-permissions-to-role "Direct link to Add permissions to role")

Making an **HTTP PATCH** request with the following body will give the `Services-Moderator` role permissions to view the page (without removing the permissions of any existing role):

```
{
  "read": {
    "roles": ["Admin", "Member", "Services-Moderator"]
  }
}
```

#### Remove permissions from role[â](#remove-permissions-from-role "Direct link to Remove permissions from role")

Making an **HTTP PATCH** request with the following body will remove the `Member` roles' permissions to view the page:

```
{
  "read": {
    "roles": ["Admin"]
  }
}
```

#### Add permissions to user[â](#add-permissions-to-user "Direct link to Add permissions to user")

Making an **HTTP PATCH** request with the following body will give the specified users permissions to view the page (without changing the permissions of existing `roles`):

```
{
  "read": {
    "users": ["exampleUser1@example.com", "exampleUser2@example.com"]
  }
}
```

#### Add permissions to team[â](#add-permissions-to-team "Direct link to Add permissions to team")

Making an **HTTP PATCH** request with the following body will give the specified teams permissions to view the page (without changing the permissions of existing `roles`):

```
{
  "read": {
    "teams": ["team1", "team2"]
  }
}
```

info

It is possible to update multiple permission keys (`roles`, `teams` and/or `users`) in a single `PATCH` request, just keep in mind that any `role`, `team` or `user` that is not specified and previously had permissions to the page, will lose those permissions.

## Lock pages[â](#lock-pages "Direct link to Lock pages")

Locking the page affects widgets that have Filter and/or Hide functionality.

See the section below for the different methods to lock a page:

* UI
* API

Users that have permissions to update a page (usually users with the `admin` role) can lock the page's widgets.

1. Save the page in the desired view by clicking the `save page` button.
2. Open the page menu and click on `lock page`.

To lock a page, make an **HTTP PATCH** request to the following URL: `https://api.port.io/v1/pages/{page_identifier}`

with the following body:

```
{
  "locked": true
}
```

A locked page will have the `Lock` icon next to the page's title:

![](/img/software-catalog/pages/LockedPage.png)
