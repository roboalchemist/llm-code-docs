# Source: https://docs.baseten.co/organization/access.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Access control

> Manage access to your Baseten organization with role-based access control.

Baseten uses role-based access control (RBAC) to manage organization access.
Every organization member has one of two roles.

| Permission               | Admin | Member |
| :----------------------- | ----- | ------ |
| Manage members           | ✅     | ❌      |
| Manage billing           | ✅     | ❌      |
| Deploy models and Chains | ✅     | ✅      |
| Call models              | ✅     | ✅      |

**Admins** have full control over the organization, including member management and billing.
**Members** can deploy and call models but cannot manage organization settings or other users.

<Note>
  If your organization uses multiple teams, see [Teams](/organization/teams) for information about team-level roles and permissions.
</Note>
