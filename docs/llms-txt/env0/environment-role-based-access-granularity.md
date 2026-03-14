# Source: https://docs.envzero.com/changelogs/2023/05/environment-role-based-access-granularity.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🚦 Environment RBAC Granularity

> With env0's current RBAC granularity, you could manage users or teams, and structure their permissions by associating roles on a given project. Now you will be able to assign those roles to a specific environment, without giving extra permissions to a whole project. This enhancement could give you a better way to depict your organization's needs allowing you to have better permissions granularity.

With env0's current [RBAC granularity](/guides/admin-guide/user-role-and-team-management/user-management#manage-users-of-a-project), you could manage users or teams, and structure their permissions by associating roles on a given project. Now you will be able to assign those roles to a specific environment, without giving extra permissions to a whole project. This enhancement could give you a better way to depict your organization's needs allowing you to have better permissions granularity.

## ✨ Environment Role Assignments ✨

env0 allows you to create [Custom Roles](/guides/admin-guide/user-role-and-team-management/rbac) and assign them to a specific user (or team), on the global **Organization** scope, specific **Project**, and now also [in a specific **Environment**](/guides/admin-guide/environments/access).

On the Environment page, you can now find the **Access** tab.

<div style={{ textAlign: 'center', border: '1px solid #000', display: 'inline-block' }}>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/05/dfe63ee-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=218355d39bfe497c287497e617a26d5a" alt="Feature demonstration screenshot showing new functionality" width="1007" height="933" data-path="images/changelogs/2023/05/dfe63ee-image.png" />
</div>

There you can assign access to either **Users** or **Teams** to this specific environment.

You can read more about it [here](/guides/admin-guide/user-role-and-team-management/rbac)

Built with [Mintlify](https://mintlify.com).
