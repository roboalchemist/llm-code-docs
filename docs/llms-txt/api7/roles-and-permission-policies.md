# Source: https://docs.api7.ai/enterprise/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/roles-and-permission-policies.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/roles-and-permission-policies.md

# Roles and Permission Policies

In this document, you will learn the concept of roles and permission policies, an advanced and exclusive feature in API7 Enterprise.

## Overview[â](#overview "Direct link to Overview")

Roles: Define user groups with specific access levels. You can create custom roles to categorize users with similar permission needs. **A single role can be associated with multiple permission policies.**

Permission Policies: These act as blueprints, outlining the allowed actions (permissions) for specific resources within API7 Enterprise (e.g., gateway groups, published services). **A single permission policy can be shared and applied to multiple roles, or directly applied to a user as permission boundary.**

There are two ways to use permission policies:

* By associating permission policies with roles, you can efficiently assign appropriate access levels to different user groups. This simplifies access control management and ensures users only have the permissions they need to perform their tasks.
* Applying permission policy as boundary to specific users will define the maximum allowable permissions for a user, acting as a safeguard against excessive privilege escalation.

**In general, a user's effective permissions are determined by the intersection of assigned roles and permission boundaries.**

## How Roles and Permission Policies Work[â](#how-roles-and-permission-policies-work "Direct link to How Roles and Permission Policies Work")

A user's action is permitted only when:

* Allowed by at least one assigned role.
* Allowed by at least one permission boundary (if present).
* Not denied by any assigned role or permission boundary.

Consider a scenario where you have created a custom role called `Gateway Group Manager` and attached it to a permission policy named `Gateway Group Basics Actions`. This permission policy grants the `GetGatewayGroups` action to all gateway group resources(resource scope is `*`), allowing users with the `Gateway Group Manager` role to view gateway group list on the Dashboard, and retrieve gateway group list directly using the `Get all gateway groups` API or leverage API7 tools like the ADC and API7 Ingress Controller. Also created a permission policy named `Prohibit License Operation`, which will deny all actions related license. Applied this permission policy as a user's permission boundary, then it will enforce strict access limits to license, preventing users from exceeding pre-defined privileges regardless of assigned roles.

Key Points:

* Roles are used to categorize users based on their shared permission requirements. Changes to the attached permission policy of a role will propagate to all users within that role.
* Permission policies specifying authorized or prohibited actions for designated resources within API7 Enterprise(including API7 Gateway and API7 Portal).
* Attaching a permission policy to multiple roles grants the associated permissions to all users within those roles.
* Permission policies can be as detailed or broad as needed. Start with a base set and refine them as your access control requirements evolve.
* Permission boundary limits the maximum allowable permissions for a user, regardless of their assigned roles. Permission policy used as user permission boundary typically contain a set of deny statements.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Built-in Super Admin Role[â](#built-in-super-admin-role "Direct link to Built-in Super Admin Role")

API7 Enterprise starts with a single, pre-defined role named `Super Admin` for initial system setup. This role is associated with the built-in `super-admin-permission-policy` granting full access to all actions and resources within API7 Enterprise. Both the pre-defined role and policy are non-editable to ensure core system security.

The initial `admin` account is permanently tied to the `Super Admin` role, and its role cannot be changed.

### Expanding Access Control with Custom Roles[â](#expanding-access-control-with-custom-roles "Direct link to Expanding Access Control with Custom Roles")

While the built-in role and policy offer full access, API7 Enterprise empowers you to create custom roles with granular permissions. You can even attach the `super-admin-permission-policy` to your custom roles for scenarios requiring extensive access.

Here is an example scenario: Isolating Environments and Tailoring Security

By associating permission policies with specific gateway groups, you can define granular security controls for each environment. This allows you to enforce stricter access limitations in environments like Production, compared to more relaxed settings in development environments like Test or UAT.

1. Define Granular Permission Policies

Create specific permission policies for each gateway group, such as `test-gateway-group-full-access`, `uat-gateway-group-full-access`, and `production-gateway-group-full-access`. These policies will define the allowed actions and resources within each environment.

2. Assign Roles with Controlled Access

Create custom roles to categorize users with similar access needs. Attach the appropriate permission policies to each role:

* Development Team Member: Grant access to the `test-gateway-group-full-access` policy, allowing them to make changes solely in the test environment.
* Development Team Leader: Assign access to both `test-gateway-group-full-access` and `uat-gateway-group-full-access` policies. This enables them to work in both test and UAT environments, potentially including the ability to synchronize stable configurations from test to UAT.
* Testing Engineer: Attach `uat-gateway-group-full-access` and `production-gateway-group-full-access` policies. This restricts their access to UAT and Production environments, focusing on new API testing and publishing tasks.

### Preventing Users from Exceeding Pre-defined Privileges[â](#preventing-users-from-exceeding-pre-defined-privileges "Direct link to Preventing Users from Exceeding Pre-defined Privileges")

The roles of a user may change frequently, and you may need a safeguard to ensure the limitations. For example, permission boundaries can be used to prevent users from Department A from accessing resources owned by Department B. Permission boundaries can also be used to prevent accidental access to critical system components like license or organization settings. By explicitly denying access to these areas, you can create a robust security layer that protects sensitive configurations from unauthorized modifications.

## How to Configure Permission Policies[â](#how-to-configure-permission-policies "Direct link to How to Configure Permission Policies")

API7 Enterprise currently stores permission policies as JSON documents. Creating and editing these policies involves using a JSON editor to define the details and then manually copying the edited JSON code back into API7 Enterprise for configuration.

Future versions of API7 Enterprise are planned to include a visual editor for permission policies. Please stay tuned for updates.

### JSON Policy Document Structure[â](#json-policy-document-structure "Direct link to JSON Policy Document Structure")

As illustrated in the following example, a JSON policy document includes these elements:

```
// PermissionPolicy demo
{
    "statement": [
        {
            "resources": [
                "arn:gatewaygroup:<[^:]*>" // Required field, the scope of operable resources, specified by resource ID, wildcards can be used. In this example, it refers to all gateway group resources.
            ],
            "actions": [
                "GatewayGroup:DeleteGatewayGroup" // Required field, allowed actions, selected from a predefined set of actions. Note that the actions should be compatible with the resource type. In this example, it refers to the action of deleting a gateway group.
            ],
    
            "conditions": {  // Optional field, filters operable resources by label. In this example, it refers to all gateway groups with the label "Environment Type: Production".
                "gateway_group_label": {
                    "type": "MatchLabel",
                    "options": [
                        {
                            "key": "EnvType",
                            "operator": "exact_match",
                            "value": "Production"
                        }
                    ]
                }
            },
            "effect": "allow" 
        }
    ]
}
```

* A single permission policy in API7 Enterprise can contain multiple statements, which may overlap in terms of the resources or actions they govern. Generally, statements within a policy function with an OR relationship. If any single statement grants permission (using "allow") for a user, they are authorized to perform the action on the specified resource.

* API7 Enterprise enforces a principle of "deny overrides allow" for permission policies.

  <!-- -->

  * For a specific role, if multiple permission policies are associated, as long as any one policy has any statement defined as "deny", then all "allow" statements for the same resource and action in all other associated permission policies will be invalid.
  * For a specific user, if any role or the user's permission boundary policy ultimately "deny" a certain resource and action, then the user will not be able to perform the specified action on this resource, regardless of whether other roles allow it or not.

### Example[â](#example "Direct link to Example")

In this example, assume there are three gateway groups:

* Name: Test gateway group, with label `EnvType:Test`, `Department:A`
* Name: Blue gateway group, with label `EnvType:Production`, `Department:B`
* Name: Green gateway group, with label `EnvType:Production`, `Department:A`

Consider a user assigned to a role with the above example permission policy. This user can delete `Blue gateway group`and `Green gateway group` through the Dashboard or API7 tools, but not `Test gateway group.`

However, if the `Test gateway group` 's label is changed to `EnvType:Production`, the user can then delete it due to the matching label. Similarly, a newly created `Black gateway group` with the `EnvType:Production` label would also be deleted by this user.

### About Using Labels in Permission Policy Condition[â](#about-using-labels-in-permission-policy-condition "Direct link to About Using Labels in Permission Policy Condition")

Using labels in permission policy condition instead of using resource ID can have the following advantages and disadvantages:

#### Advantages[â](#advantages "Direct link to Advantages")

* Dynamic Access Control: Labels are adaptable and can be updated at anytime. Resource IDs cannot be edit.
* Scalability: A single label can be applied to multiple resources, simplifying policy management for growing resources. Using label can avoid the following situation
  <!-- -->
  :A
  <!-- -->
  user creates a new resource (e.g., a gateway group) but cannot access it because the permission policies referencing the old resource ID do not include the new one.

#### Disadvantages[â](#disadvantages "Direct link to Disadvantages")

* Reduced Clarity: Labels introduce an abstraction layer, potentially making it harder to understand which specific resources a policy applies to at a glance.
* Misconfiguration Risks: Inconsistent or inaccurate labeling can lead to unintended access grants or denials.
* Dynamic Access Control Leading to Unexpected Behavior: While labels offer flexibility, they can introduce dynamic access control. This means a user's ability to access a specific resource might change based on updates to the resource labels, potentially leading to less predictable access behavior compared to using static resource IDs.

Finding the Right Balance:

* Labels for Broader Categories: Use labels for broader access control categories (e.g., "production", "test"). Resource IDs for Granular Control: Use resource IDs for specific resources requiring fine-grained control (e.g., a unique ID for a critical API endpoint).
* Clear Labeling Practices: Ensure consistent and well-defined labeling conventions throughout your API environment.

By understanding these trade-offs and implementing best practices, you can leverage labels effectively to enhance the security and manageability of your API7 Enterprise permission policies.

### Useful Tips[â](#useful-tips "Direct link to Useful Tips")

#### Grant Least Privilege[â](#grant-least-privilege "Direct link to Grant Least Privilege")

Granting users only the minimum permissions needed for their designated tasks within the API environment. To achieve this, first clearly define user and role needs. Then, craft permission policies with a restricted set of actions and resources. Finally, add more permissions only when absolutely necessary, ensuring a balance between efficiency and strong access control.

Benefits:

* Reduced Attack Surface: Limiting permissions minimizes the potential impact of compromised accounts.
* Enhanced Accountability: Clear user access limitations promote better ownership and responsibility.
* Simplified Management: Maintaining least privilege simplifies permission management and reduces the risk of accidental oversights.

#### Configure the Permissions of Roles and Permission Policies[â](#configure-the-permissions-of-roles-and-permission-policies "Direct link to Configure the Permissions of Roles and Permission Policies")

As with other resources in API7 Enterprise, roles and permission policies themselves require well-defined access control. Here are two common approaches:

1. Consolidated Permissions: Specified users can update the role itself and modify all its attached permission policies. This streamlines their workflow by managing both aspects together. All permission policies only attached to a single role can help simplify the design in this scenario.

2. Separate Access Control: Manage access control for roles and permission policies independently. This allows for frequently changing users within roles while maintaining stable policy content.

The optimal approach depends on your specific needs. Consider factors like:

* Frequency of role membership changes
* Importance of maintaining stable policy content

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Getting Started

  <!-- -->

  * [Update User Roles](https://docs.api7.ai/enterprise/3.3.x/getting-started/rbac.md)
  * [Create Custom Role](https://docs.api7.ai/enterprise/3.3.x/getting-started/create-custom-role.md)

* Best Practice
  <!-- -->
  * [Design Custom Role System](https://docs.api7.ai/enterprise/3.3.x/best-practices/design-custom-role-system.md)

* Reference

  <!-- -->

  * [Permission Policy Actions and Resources](https://docs.api7.ai/enterprise/3.3.x/reference/permission-policy-action-and-resource.md)
  * [Permission Policy Examples](https://docs.api7.ai/enterprise/3.3.x/reference/permission-policy-examples.md)
