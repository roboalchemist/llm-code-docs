# Source: https://docs.startree.ai/corecapabilities/security/manage-access.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Access

> Manage secure, fine-grained access to StarTree resources with Role-Based Access Control (RBAC), enabling administrators to define custom policies, create roles, and assign them to users or groups through the Security Manager interface integrated with your organization's Identity Provider (IDP).

Role-Based Access Control (RBAC) enables granular control over data access within the StarTree environment. RBAC ensures that access is restricted to authorized users. The StarTree Security Manager provides a powerful mechanism to craft policies that match the needs of any data team.

When you enable access control, StarTree integrates with your organization's Identity Provider (IDP) to authenticate users and groups. After successful authentication, StarTree enforces access control policies based on the roles you assign.

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/security/images/rbac_diagram.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=4caf548444312fdd2b4ab76d2bdac471" alt="" width="760" height="442" data-path="corecapabilities/security/images/rbac_diagram.png" />

The diagram shows a typical RBAC system containing users/groups, their roles, and the associated policies. Together, these attributes form the set of rules that define who can access a resource.

<Info>
  Access Control features require initial configuration and may involve integration with your existing identity provider. Contact StarTree Support or your account team to discuss your specific requirements and enable these features.
</Info>

Using the Security Manager you can:

* **Define and manage custom policies:** Create and modify fine-grained access control rules based on specific conditions and requirements.
* **Create and manage custom roles:** Group together related permissions and policies into easily manageable roles.
* **Assign roles to users and groups:** Granularly control access to StarTree resources for different entities within the organization.

## Access Control Capabilities

StarTree provides two levels of access control to meet different security requirements:

### Table-Level Access Control (RBAC)

Traditional Role-Based Access Control provides all-or-nothing access to resources:

* **Resource-level granularity**: Control access to entire tables, databases, clusters, and environments
* **Pre-seeded roles**: Ready-to-use roles like `table-reader`, `system-admin`, and `rbac-admin`
* **Custom role definition**: Create roles tailored to your organization's needs
* **Multi-IDP support**: Works seamlessly with Okta, Azure AD, Google Workspace, and Auth0
* **API & UI management**: Manage policies through both web interface and REST APIs

### Row-Level Access Control

<Warning>
  Row-Level Access Control is currently in beta. Contact your customer success manager for a private preview.
</Warning>

Advanced access control that restricts access to specific rows within tables using conditional policies and SQL expressions.

Learn more about implementing [Row-Level Access Control](/corecapabilities/security/row-level-access-control) for fine-grained data access.

## Policies, Roles, and Assignments

StarTree utilizes Role-Based Access Control (RBAC) to manage data access. RBAC is a security model where access rights are defined by assigning roles to users, users groups, and API tokens. Roles are collections of policies that define permissions for specific resources.

### Policies

A policy defines the rules that govern access to specific resources. It outlines which actions (like reading, writing, or deleting) are permitted or prohibited on a particular resource, such as a table.

Policies are the building blocks for granular control over data access within the StarTree platform.

In the Policies screen, you can:

* View existing policies: Easily browse and review all defined policies within the system.
* Create new policies: Define custom policies with specific conditions and permissions, such as:
  * Resource-level access: Control access to specific tables, workspaces, and environments.
  * Operation-level access: Control allowed operations on resources (e.g., read, write, delete, query).

### Roles

A Role represents a collection of one or more policies. It acts as a container for a set of permissions that define what actions a user or group is authorized to perform on specific resources.

Think of it as a job title or a set of responsibilities. For example, a 'Data Analyst' role might include policies granting read access to certain tables, the ability to run queries, and potentially limited write access for specific purposes.

Roles simplify user access management by grouping together relevant policies, making it easier to assign permissions to users based on their job functions or responsibilities.

The Roles screen allows you to:

* View existing roles: Easily browse and review all defined roles within the system.
* Create new roles: Define custom roles by grouping together relevant policies and permissions.
* Edit roles: Add or remove policies associated with an existing custom role.

### Role Assignments

Role assignment is the process of associating a specific role with a particular user or group. This effectively grants the assigned entity the permissions defined within the associated role.

Think of it as assigning a job title to an employee. When you assign the 'Data Analyst' role to a user, they automatically inherit all the permissions associated with that role, such as read access to specific datasets and the ability to run queries.

Role Assignment is the crucial step that connects users and groups to the specific permissions defined within Roles, enabling effective and granular control over data access within the StarTree environment.

<Info>
  By default, the first user in an environment is assigned the `system-admin` role, which grants them full access to all resources and actions in their StarTree environment. When inviting new users, you can easily control user access by assigning roles. You can also update or remove roles at any time to ensure that users have the correct level of access.
</Info>

In the Role Assignments screen, you can:

* View existing assignments: Easily browse and review all assignments within the system.
* Create new assignments: Grant permission by assigning a role to a user or a group.
  * Assign roles to users: Grant roles to individual users based on their email.
  * Assign roles to groups: Groups are defined and managed within your organization's Identity Provider (IDP). This could be a system like [Okta](https://help.okta.com/asa/en-us/content/topics/adv_server_access/docs/setup/create-a-group.htm), [Azure AD](https://learn.microsoft.com/en-us/entra/fundamentals/groups-view-azure-portal), or [Google Workspace](https://support.google.com/a/answer/9400082?hl=en\&ref_topic=25840\&sjid=9852883180017174836-NC).
* Delete assignments: Delete an assignment to revoke access from a user or a group.

<Info>
  Role assignments can't be edited. To change an assignment, delete the existing assignment and create a new one with a different role.
</Info>

## Create a custom policy

You can create a custom policy to define fine-grained access to specific resources. For example, you can define a policy that allows read-only access to a specific table.

To create a custom policy, follow these steps:

1. Open the Security Manager by navigating to [https://dp.your\_environment\_id.startree.cloud/security-manager](https://dp.your_environment_id.startree.cloud/security-manager).
2. Click **Policies** in the left navigation menu.
3. Click **Create policy**.
4. Enter a name and a description for the new policy.
5. Provide the policy configuration in JSON format.

   See our [Custom policies](/corecapabilities/security/custom-policies) page to learn more about writing your own policy configuration.
6. Click **Create policy** to save the new policy.

## Testing a custom policy

Due to potential propagation delays of up to an hour, we recommended testing your policy before saving it. StarTree provides an API that allows you to simulate access requests and see how your policies would be applied.

You can use the following `curl` command to send a request to the Simulate API:

```bash  theme={null}
curl --location 'https://rbac-manager.<envt-url>/api/v1/rbac-manager/simulate-access' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <Token>' \
--data '{
    "policyDocumentJson": "<policy JSON>",
    "subjectTypeToSubject": {
        "<subject-type>": "<subject-id>"
    },
    "resourceSrn2String": "<resource_srn2>",
    "action": "<action>"
}'
```

* `policyDocumentJson` is the JSON content of the policy you want to test.
* `subjectTypeToSubject` identifies the subject (user email, group name, or API token) that the API will use to simulate the policy with. The values can be one of the following pairs:

| subject-type    | subject-id                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------ |
| `email`         | the user's email address (e.g., `john.doe@example.com`)                                    |
| `group`         | The name of the group the user belongs to, as defined in your organization's IDP           |
| `service-token` | The username portion of the service token (see how to obtain a service token's username  ) |

* `resourceSrn2String`specifies the resource that the you want to simulate access to.
* `action` is the action that you want to simulate on the resource (e.g., `Query`, `DeleteTable`, `UpdateSchema`).

<Note>
  The simulate access API takes into account all roles assigned to the specified subject(s). This means that if a user belongs to multiple groups or has multiple roles directly assigned, the API will evaluate the cumulative effect of all associated policies to determine access.
</Note>

<Info>
  If you saved the policy without testing it using the simulate API, and you don't want to wait for the changes to propagate, you can still test the new policy immediately by using a private browsing window, or by clearing your browser's cache. After clearing your cache or using a private window, you should be able to see the effects of your policy changes immediately.
</Info>

## Create a custom role

You can create a custom role to group together policies, allowing for precise control over what actions users can perform on specific resources.

Creating a custom role involves the following steps:

1. Open the Security Manager by navigating to [https://dp.your\_environment\_id.startree.cloud/security-manager](https://dp.your_environment_id.startree.cloud/security-manager).
2. Click “Roles” in the left navigation menu.
3. Click **Create role**.
4. Enter a name and a description for the new role.
5. Select the policies to be included in the new role.

   You can click the **Policy Details** button to view the detailed configuration of a policy.
6. Click **Create role** to save the new role.

## Assign roles to users and groups

In the role assignments screen you can attach roles to individual users and groups.

* Individual users are identified using their email address.
* Groups are defined and managed within your organization's Identity Provider (IDP). This could be a system like [Okta](https://help.okta.com/asa/en-us/content/topics/adv_server_access/docs/setup/create-a-group.htm), [Azure AD](https://learn.microsoft.com/en-us/entra/fundamentals/groups-view-azure-portal), or [Google Workspace](https://support.google.com/a/answer/9400082).

To assign a role to users or groups, follow these steps:

1. Access the Security Manager by navigating to [https://dp.your\_environment\_id.startree.cloud/security-manager](https://dp.your_environment_id.startree.cloud/security-manager).
2. Click **Role Assignments** in the left navigation menu.
3. Click **Assign role**.
4. Select the role that you want to assign.
5. Select the appropriate **Subject type**, depending on whether the subjects are individual users or groups.
6. Provide the list of user emails or group names, separated by commas
7. Click **Assign role** to save the new assignment.

## Guidance for Customer Admins

For each StarTree Environment, a customer admin is designated. The responsibility of this person is to govern access to users/services in the customer organization via Security Manager. For a newly created environment, only the customer admin will have the ability to log into StarTree data plane. Rest of the users will be denied access until they're explicitly assigned a role by the customer admin.

**Default workspace access control**

In most environments, users prefer to create and manage datasets in the default workspace. This is the workspace that comes default with the environment. In order to grant access to this default workspace, customer admin can choose one of the following roles to assign to their users/services:

* <u>owner-default</u>: This is a predefined role that grants workspace owner permissions for the ***default*** workspace to the subject. This will allow the subject to create/modify/delete datasets and do other workspace operations.
* <u>reader-default</u>: This is a predefined role that grants workspace read permissions for the ***default*** workspace to the subject. This will allow the subject to list and query any datasets in the workspace.

<Info>
  Note that subject must be assigned a role before getting access to data plane including things like Data Portal / Query console. If the above 2 roles are too generic or not restrictive enough, customer admin can create a custom role+policy to fine tune access.
</Info>

Built with [Mintlify](https://mintlify.com).
