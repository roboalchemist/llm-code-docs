# [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#role-management) Role Management

> 💡 You can access this in **Access Management > User & Role Management** _if available see [this page for details](https://qdrant.tech/documentation/cloud-rbac/)._

A **Role** contains a set of **permissions** that define the ability to perform or control specific actions in Qdrant Cloud. Permissions are accessible through the Permissions tab in the Role Details page and offer fine-grained access control, logically grouped for easy identification.

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#built-in-roles) Built-In Roles

Qdrant Cloud includes some built-in roles for common use-cases. The permissions for these built-in roles cannot be changed.

There are three types:

- The **Base Role** is assigned to all users, and provides the minimum privileges required to access Qdrant Cloud.
- The **Admin Role**  has all available permissions, except for account write permissions.
- The **Owner Role** has all available permissions assigned, including account write permissions. There can only be one Owner per account currently.

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/built-in-roles.png)

## [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#custom-roles) Custom Roles

An authorized user can create their own custom roles with specific sets of permissions, giving them more control over who has what access to which resource.

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/custom-roles.png)

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#creating-a-custom-role) Creating a Custom Role

To create a new custom role, click on the **Add** button at the top-right corner of the **Custom Roles** list.

- **Role Name**: Must be unique across roles.
- **Role Description**: Brief description of the role’s purpose.

Once created, the new role will appear under the **Custom Roles** section in the navigation.

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/create-custom-role.png)

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#editing-a-custom-role) Editing a Custom Role

To update a specific role’s permissions, select it from the list and click on the **Permissions** tab. Here, you’ll find logically grouped options that are easy to identify and edit as needed. Once you’ve made your changes, save them to apply the updated permissions to the role.

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/update-permission.png)

### [Anchor](https://qdrant.tech/documentation/cloud-rbac/role-management/\#renaming-deleting-and-duplicating-a-custom-role) Renaming, Deleting and Duplicating a Custom Role

Each custom role can be renamed, duplicated or deleted via the action buttons located to the right of the role title bar.

- **Rename**: Opens a dialog allowing users to update both the role name and description.
- **Delete**: Triggers a confirmation prompt to confirm the deletion. Once confirmed, this action is irreversible. Any users assigned to the deleted role will automatically be unassigned from it.
- **Duplicate:** Opens a dialog asking for a confirmation and also allowing users to view the list of permissions that will be assigned to the duplicated role

![image.png](https://qdrant.tech/documentation/cloud/role-based-access-control/role-actions.png)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-rbac/role-management.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-rbac/role-management.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-143-lllmstxt|>
## databricks
- [Documentation](https://qdrant.tech/documentation/)
- [Send data](https://qdrant.tech/documentation/send-data/)
- Qdrant on Databricks