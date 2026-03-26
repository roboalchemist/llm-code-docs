# Source: https://docs.api7.ai/apisix/enterprise-feature/organization-and-rbac.md

# Organization and RBAC

## Organization Management[â](#organization-management "Direct link to Organization Management")

The organization module in API7 Enterprise includes users, roles, permission policies, licenses, audit, contact points, and settings.

* **Users**: The built-in `Admin` user in API7 Enterprise can manage users within the organization, including assigning roles to users and other user management tasks.
* **Roles**: The built-in `Super Admin` role is provided, and custom roles can be added or deleted. Roles assigned to users cannot be directly deleted; only unused roles can be removed.
* **Permission Policies**: A built-in permission policy called `super-admin-permission-policy` is bound to the `Super Admin` role. This policy grants full access to all operations and resources within API7 Enterprise. The role can also be associated with custom roles.

Built-in roles and policies are non-editable to ensure the security of the core system. Combining users, roles, and permission policies enables fine-grained [permission management](https://docs.api7.ai/apisix/enterprise-feature/permission-policies-and-boundaries.md), preventing privilege escalation and potential security vulnerabilities.

* **Licenses**: This module displays important information, such as the validity, issuance date, and licensed CPU cores.
* **Audit**: Detailed records of all user actions within API7 Enterprise are maintained. Each audit log contains a series of attributes, such as event, time, operator, resource ID, gateway group ID, and details of the audit logs.
* **Contact Points**: This can be integrated with alert policies to configure Webhook and email alert triggers, enhancing the gateway's monitoring and response capabilities.
* **Settings**: It includes configurations for API7 integrated authentication, SCIM provisioning, login options, and SMTP server settings. These features allow API7 Enterprise to manage users and permissions effectively, ensuring system security and stability.

## RBAC[â](#rbac "Direct link to RBAC")

RBAC (Role-Based Access Control) is an access management method where users are assigned roles to obtain permissions, enabling flexible and efficient access control. Besides the RBAC model, API7 Enterprise introduces a more flexible and powerful IAM (Identity and Access Management) policy model. It allows administrators to define specific policies, each consisting of a set of rules that specify the range of resources that users and roles can access.

API7 Enterprise supports enabling SCIM (System for Cross-domain Identity Management) configuration, which allows synchronizing user and group information from the source identity provider (IdP) to API7 Enterprise. Paste the SCIM token generated on the API7 dashboard and save it in the IdP system. After configuring SCIM, any updates made to users in the connected Identity Provider (IdP) systemâlike adding or removing usersâare automatically synchronized with API7 Enterprise. This saves users' efforts in user management across multiple systems, streamlining identity management and enhancing data consistency. API7 Enterprise automatically assigns roles to users imported from the IdP system based on relevant attributes (e.g., title, position, department). These roles are synchronized and refreshed upon user login.

API7 Enterprise also supports SSO (Single Sign-On) role mapping. When administrators add an SSO login option, corresponding SSO role mapping rules can be created. Role mappings may include multiple rules, which together determine users' roles and access rights. Role mappings take precedence over manual role assignments. When role mapping is enabled, any manual changes to user roles will be overwritten during the user's next login.

API7 Enterprise's role mapping supports four matching methods: Exact Match, Contain String, Exact Match in Array, and Contain String in Array. This allows for many-to-many mappings between internal roles and IdP roles.

For example, when creating an SSO login option and setting a role mapping for the `Super Admin` internal role, the role attribute can be set to `Position` in the IdP system. If the matching method is set to "exact match" (`=`), and the role value is set to `Apps Engineer`, all users with the Apps Engineer position will be assigned the `Super Admin` role. Since role mapping is dynamically applied, if the position of an `Apps Engineer` in the IdP system changes to `Ops Engineer`, that user will lose the `Super Admin` role on their next login to API7 Enterprise.

![Organization and RBAC](https://static.api7.ai/uploads/2024/11/27/VuAT9Z2S_organization-and-rbac.png)

## Key Features[â](#key-features "Direct link to Key Features")

* Provides a flexible IAM policy model, supporting fine-grained permission configuration based on users, roles, resources, and environments.
* Built-in support for SCIM configuration, enabling automatic synchronization of user and group information between mainstream IdP systems.
* Supports dynamic role mapping, allowing user roles to be dynamically adjusted based on flexible rule configurations.
* Suitable for multi-tenant, multi-team, and multi-department architectures, ensuring access control and data isolation between tenants.
* Highly compatible with major cloud platforms (such as AWS, Azure, and GCP), while also supporting locally deployed IdP systems.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Automate User Management[â](#automate-user-management "Direct link to Automate User Management")

API7 Enterprise supports enabling SCIM configuration, which, combined with organization and RBAC features, enables automatic synchronization and management of user information. Enterprises can import users from existing IdP systems and automatically assign roles based on user attributes (e.g., position, department, or project) in the IdP system. This approach not only improves system operation and management efficiency but also enhances security.

In fast-changing business environments, roles and permissions may need frequent adjustments. For example, when an employee changes roles, the user information in the IdP system is updated. API7 Enterprise can automatically synchronize the role changes, reducing manual complexity and improving data consistency.

### Multi-department or Multi-team Management[â](#multi-department-or-multi-team-management "Direct link to Multi-department or Multi-team Management")

Through the organization's hierarchical structure, businesses can create independent permission management rules for different departments, subsidiaries, or project teams, ensuring that permissions do not interfere with one another. For example, financial data is only accessible to the finance team, while the development team can access and manage the code repository. With fine-grained permission management, enterprises can precisely define access rules for shared resources, ensuring that only authorized personnel can view or modify specific resources.

RBAC provides flexible permission allocation, enabling businesses to adjust permission granularity according to actual needs. It allows for cross-department collaboration without compromising data security. By binding permissions to specific roles, businesses ensure that each employee can only access information within their responsibility scope, minimizing the risk of unauthorized access or errors.

### Achieve Fine-Grained Permission Access[â](#achieve-fine-grained-permission-access "Direct link to Achieve Fine-Grained Permission Access")

Compared to traditional broad permission allocations, the fine-grained control empowered by RBAC is more flexible and secure. For example, by defining role templates such as "view-only" and "admin," permissions are refined based on user roles, with the ability to expand across additional operational dimensions. This further strengthens access control precision and ensures the protection of sensitive data.

API7 Enterprise supports more complex access rules, such as attribute-based mappings, SSO-integrated role mappings, and condition-based role mappings. These enable administrators to make flexible adjustments in specific situations, addressing complex enterprise permission management needs and effectively reducing the risks of privilege abuse and operational mistakes.
