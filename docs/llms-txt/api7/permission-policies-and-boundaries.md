# Source: https://docs.api7.ai/apisix/enterprise-feature/permission-policies-and-boundaries.md

# Permission Policies and Boundaries

In API7 Enterprise, permission policies and boundaries are core access control mechanisms to ensure resource security and compliance with user roles.

* **Permission Policies** refer to a set of rules and guidelines that clearly define the operations users are authorized to perform and the resource scope they can access, such as gateway groups and published services. A single permission policy can be associated with multiple roles, granting all users in those roles the specified permissions. It can also be applied as a permission boundary for certain users to prevent unauthorized access.

* **Permission Boundaries** refer to the limits or permission scope, usually defining the resources a user can access or the operations they can perform. Permission boundaries can be used to set the maximum permissions an entity can have, regardless of their assigned roles or policies. Users cannot exceed the defined access scope, even if broader permissions are granted by their roles.

API7 Enterprise includes a built-in `Super Admin` role, which is associated with the built-in permission policy called `super-admin-permission-policy`, granting full access to all operations and resources within API7 Enterprise. Besides, API7 Enterprise follows a "deny overrides allow" principle for permission policies. If any policy for a role or user contains a "deny" statement, it invalidates any "allow" statements for the same resource or action, regardless of other associated policies.

Consider John, a development team member, with his restricted permission boundary to `Full Access to Test Gateway Group`. To manage developer permissions in a more granular way, the `Development Team Member` role is assigned the permission policy `Full Access to Test Gateway Group`, while the Test Engineer role is assigned the permission policy `Full Access to Prod Gateway Group`. Since a user's effective permissions are determined by the intersection of permissions attached to roles and permission boundaries, even if Johnâs role is changed to `Test Engineer`, his permission boundary remains unchanged and John still cannot access the prod gateway group.

![How Permission Policies and Boundaries Work in API7 Enterprise](https://static.api7.ai/uploads/2024/11/27/lhwvAzlP_permission-policy-and-boundary.png)

## Features of Permission Policies and Boundaries[â](#features-of-permission-policies-and-boundaries "Direct link to Features of Permission Policies and Boundaries")

* Permission policies and permission boundaries must be applied together with roles and users.
* Dynamic permission management allows changes to roles as positions shift without affecting the established permission rules.
* Setting permission boundaries minimizes the risk of misconfigurations and effectively prevents excessive permissions and potential security vulnerabilities.
* Granular access control supports defining precise access permissions for specific resources and users.
* Permission policies are flexible and can be combined in various ways to meet complex permission management needs.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Prevent Unauthorized Access[â](#prevent-unauthorized-access "Direct link to Prevent Unauthorized Access")

Frequent role changes within organizations necessitate robust safeguards. Permission boundaries can effectively prevent users in one department from accessing resources owned by another. For example, users in department A can be restricted from accessing sensitive files and systems belonging to department B to maintain information isolation and security. Furthermore, permission boundaries can prevent users from inadvertently accessing critical system components, such as licenses or organizational settings. Unauthorized access to these critical components could result in severe security risks. By explicitly denying access to these parts, organizations can build a strong defense to protect sensitive configurations from unauthorized modification or breaches.

### Isolate Development Environments[â](#isolate-development-environments "Direct link to Isolate Development Environments")

Before introducing permission policies and boundaries, isolating development environments posed numerous challenges that impacted security, compliance, and productivity. API7 Enterprise addresses these issues by leveraging permission policies and boundaries to logically separate development environments, ensuring that each role only has access to the resources necessary for their responsibilities.

For example, associate the `Development Team Member` role with `Full Access to Test Gateway Group`, enabling modifications exclusively in the testing environment. Assign the `Development Team Lead` both `Full Access to Test Gateway Group` and `Full Access to UAT Gateway Group`, granting access to both testing and UAT environments. Grant the Test Engineer both `Full Access to UAT Gateway Group` and `Full Access to Prod Gateway Group`, confining their work to UAT and production environments for API testing and release tasks.

### Granular Permission Management[â](#granular-permission-management "Direct link to Granular Permission Management")

In enterprises with diverse teams and multi-environment operations, implementing fine-grained permission management is essential to maintain security and ensure compliance. API7 Enterprise addresses this need through advanced role assignments and permission policies, enabling tailored access control. For instance, application engineers can be assigned permission policies specific to the test environment, while operations engineers are granted access to production resources through separate policies.

Additionally, individual users can be assigned specific permission boundaries, restricting their access to designated gateway group resources. This prevents permission overlaps and mitigates risks caused by misconfigurations. By confining teams to their allocated permissions, API7 Enterprise ensures operational independence across environments while simplifying permission management and configuration, resulting in improved efficiency and security.
