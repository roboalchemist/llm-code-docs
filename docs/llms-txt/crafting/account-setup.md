# Source: https://docs.sandboxes.cloud/docs/account-setup.md

# Account Setup

Setting up account is the first thing need to be done for setting up Crafting. In this page, we talk about topics regarding account setup on Crafting platform.

* [Create an Account](#create-an-account)
* [Add Administrators and Users](#add-administrators-and-users)
  * [Domain-based automatic user creation](#domain-based-automatic-user-creation)
  * [SAML integration](#saml-integration)
* [Service Account and Login Token](#service-account-and-login-token)
* [Role-based Access Control (RBAC)](#role-based-access-control-rbac)

## Create an Account

To create an account on Crafting for a new organization, please [contact us](https://crafting.dev/contact). We support account setup on our [SaaS platform](https://docs.sandboxes.cloud/docs/crafting-saas) or on your cloud using [Crafting Enterprise ](https://docs.sandboxes.cloud/docs/crafting-enterprise) . We also offer setup assistant and free trials to fit your specific dev needs. When installing [Crafting Express](https://docs.sandboxes.cloud/docs/crafting-express) the admin account is automatically created during the procedure.

## Add Administrators and Users

Administrators can add other administrators and users into the organization. From the `Team -> Members` page on our web console, you can see every member in the organization account and add new member by click `Add` button, and fill in information in the following dialog.

<Image align="center" className="border" border={true} width="40% " src="https://files.readme.io/8198102-image.png" />

After clicking `Add`, an invite will be sent to the newly added member, who can login using their email to the system (See [Login](https://docs.sandboxes.cloud/docs/login))

It can also be done via CLI

```shell
$ cs org member add <EMAIL> [--admin]
```

Creating users one by one is often troublesome with large teams. Crafting supports following ways to support large teams.

### Domain-based automatic user creation

On Crafting platform, the admin can set up an `Organization Domain`, that way, all users with emails from that domain can automatically be added as Crafting users for that organization. The user will be created on-demand upon first login.

### SAML integration

For customers adopting [Crafting Enterprise](https://docs.sandboxes.cloud/docs/crafting-enterprise), a SAML identity provider can be configured to provide the login service for Crafting. For more details, please [contact us](https://crafting.dev/contact).

## Service Account and Login Token

Crafting allows the user to create service accounts for accessing the Crafting platform, which would be useful in following scenarios:

* Internal tool integration: Team admin can create a service account to be used by tools such as CI  tool, automation scripts, etc., so that these tools can leverage Crafting platform. See [Git Service Integration for Preview](https://docs.sandboxes.cloud/docs/git-integration) for some example.
* External demos or collaborations: Team admin can grant temporary access to external collaborators, e.g., customers, partners, vendors, etc., to let them access the Crafting system to work with the team members.

To create a service account, go to `Team -> Service Accounts` and click `Add` highlighted below, and then fill in the name. Note that a service account always assumes the email only as a placeholder.

<Image align="center" className="border" border={true} src="https://files.readme.io/f9de415-image.png" />

<Image align="center" width="60% " src="https://files.readme.io/9ab1de2-image.png" />

After clicking `Confirm`, a service account is created. **A service account is an non-user account and can only be accessed by a login token**, so let's see how to create an login token to access that account. On the same page, click `Add` highlighted below, and fill the dialog.

<Image align="center" className="border" border={true} src="https://files.readme.io/033e63e-image.png" />

<Image align="center" width="70% " src="https://files.readme.io/3998dc0-image.png" />

After creating the login-token, it can be logged from CLI and web browser. The instruction can be found by clicking the following expanding button highlighted below.

![](https://files.readme.io/d3d46b3-image.png)

The login token will expire according to the `Expire At`, and you can delete it any time. Similarly the `Service Account` can be disabled (by editing) or deleted in this page.

### Revoking access and best practices

Once a `Login Token` is used, the active session is under the identity of a service account. Deleting the Login Token doesn't invalidate the session. To disable the session, disable/delete the Service Account.

If the Service Account is to be shared with external contributors, create `Service Account` on-demand and delete it when no longer needed

### System service accounts

These are reserved service accounts, with emails suffixed by `@sys.sandbox`. They are used by the Crafting Sandbox internally. The users may be able to see them, but not allowed to change them. The currently available service accounts are:

* `support@sys.sandbox`: this account is used by the supporting personnel from Crafting to perform support operations in the organization, like troubleshooting.

## Role-based Access Control (RBAC)

The Enterprise edition of Crafting supports Role-based Access Control (RBAC), which offers fine-grained access control for users in custom defined roles. The access control can be defined with respect to specific types of resources, such as templates, sandboxes, resources, etc. It also helps large engineering organizations to organize teams' assets into different folders. For more information regarding RBAC, please [contact us](https://crafting.dev/contact).