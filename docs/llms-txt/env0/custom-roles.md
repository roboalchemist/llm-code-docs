# Source: https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/custom-roles.md

# Source: https://docs.envzero.com/changelogs/2022/10/custom-roles.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 👮‍♀️ Custom Roles

> Custom Roles have arrived 🎉, have fine grained control over what users can & can't do. env0's Custom Role allow you to restrict access based on predefined roles of individual users & teams within your organization. It helps ensure users access only information they need to do their jobs and prevents them from accessing information that doesn't pertain to them.

Custom Roles have arrived 🎉, now you can have fine-grained control over what users can and can't do. env0's Custom Role allows you to restrict access based on predefined roles of individual users and teams within your organization. It helps ensure users access only information they need to do their jobs and prevents them from accessing information that doesn't pertain to them.

### Role Creation & Management

First, create a role with your desired permissions.\
This can be done in the organization settings page -> roles tab -> add role button.\
You can also edit or delete roles from that page.

> 📘 More On Role Deletion
>
> When roles are deleted while being assigned the users \ team will update according to the role assignment level:\
> If the role assignment level is by organization, the user will receive the default "User" role.\
> If the role assignment level is by project the user will lose his access to that project and have no role in it.

### Role Assignment

Roles can be assigned to users or to teams on a project or organization level.

"Organization Roles" - can be assigned on the organization settings page in either the users or teams tab.\
"Project Roles" - can be assigned on the project setting page in either the users or teams tab.

> 📘 More On Role Assignment
>
> Env0's RBAC is cascading, meaning that if a user has a permission on an organization (via the role) he has that permission on every project in that organization. (but not the other way around, project permissions apply for their particular projects only)

Built with [Mintlify](https://mintlify.com).
