# Source: https://docs.api7.ai/apisix/enterprise-feature/dashboard-sso.md

# Dashboard SSO Options

The Single Sign-On (SSO) feature in the API7 Enterprise Dashboard simplifies user authentication by enabling access with a single set of credentials. By integrating with identity providers, such as Keycloak, Microsoft Entra ID (formerly Azure AD), Google, and Okta, enabling SSO eliminates the need for users to manage multiple logins, reducing friction and enhancing security. This centralized approach not only improves user experience but also strengthens compliance by allowing the enforcement of consistent access policies across all integrated systems.

The API7 Dashboard supports **LDAP**, **OpenID Connect (OIDC)**, and **SAML** protocols for SSO. LDAP integrates with directory services for centralized user authentication and management, making it a reliable choice for legacy systems and enterprise environments. OIDC, a modern protocol built on OAuth 2.0, provides token-based authentication for secure and user-friendly access to web and mobile applications. SAML, widely used in enterprise SSO setups, facilitates the secure exchange of authentication data between identity providers and service providers.

Consider an organization that uses API7 Enterprise to manage its API ecosystem, where administrators and developers regularly access the API7 Dashboard. Administrators handle tasks such as configuring routes, monitoring performance, and enforcing security policies, while developers are granted limited permissions, such as managing routes, to focus on their specific responsibilities. Without SSO, users need to maintain credentials specifically for the API7 Dashboard.

To streamline access, the organization integrates the API7 Dashboard with an identity provider supporting SAML, OpenID Connect (OIDC), or LDAP. Users now can log in to the Dashboard using their existing corporate credentials managed in the identity provider. API7 Enterprise validates tokens or assertions from the identity provider during login and redirects users to the Dashboard if successfully authenticated. This approach simplifies login for users, enforces consistent role-based access controls, and strengthens governance across the organization.

![SSO login with API7 dashboard diagram](https://static.api7.ai/uploads/2024/11/27/IoTn3XAt_sso.png)

## Key Features[â](#key-features "Direct link to Key Features")

* Integrate with identity providers using OpenID Connect (OIDC), SAML, or LDAP protocols.
* Allow customization of the SSO login option text on the API7 Dashboard login page. For instance, the SSO login button can be customized to display `Log in with Employee ID`.
* Enable SCIM provisioning to automatically synchronize user identities, roles, and access permissions from the identity provider, preventing configuration discrepancies.
* Support the definition of role mapping and permission mapping rules, which assign API7 roles and permissions to imported users by evaluating user attributes they were originally assigned in the identity providers.
* Reduce the risk of credential theft by minimizing repeated logins and mitigating password sprawl, where managing multiple credentials increases the chance of insecure storage and potential leaks.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Simplify Dashboard Access with SSO[â](#simplify-dashboard-access-with-sso "Direct link to Simplify Dashboard Access with SSO")

For organizations managing APIs with API7 Enterprise, the Dashboard serves as a central hub for tasks like route configuration, performance tracking, and policy management. Enabling SSO allows users to access the Dashboard using their existing corporate credentials. This approach simplifies user authentication, reduces the overhead of managing multiple credentials, and ensures access controls align with organizational policies, fostering both security and efficiency.

### Synchronize Roles and Permissions[â](#synchronize-roles-and-permissions "Direct link to Synchronize Roles and Permissions")

API7 Enterprise enables organizations to enforce consistent access controls by using role mapping and permission mapping rules. These mappings ensure that API7 roles and permissions are dynamically assigned to imported users based on attributes defined in the identity provider, such as department, job title, or group membership. The approach eliminates manual configuration errors and ensures that all users are granted access privileges aligned with organizational policies.

For example, a user assigned to the `CloudOps` team in the identity provider can automatically receive the role of a `Super Admin` in API7 Dashboard, which comes with escalated administrative privileges to manage API7 Enterprise resources to meet the operational needs. If the user's team changes in the identity provider, the role mapping will be dynamically updated the next time they log into API7 Enterprise. Similarly, the permission boundary mapping is also dynamic, should the relevant attributes change in the identity provider.

By leveraging attribute-based evaluations, API7 Enterprise allows organizations to adapt governance policies as their workforce or business structure evolves, ensuring policies remain effective and relevant.

### Centralize Identity Management[â](#centralize-identity-management "Direct link to Centralize Identity Management")

When API7 Enterprise integrates with an identity provider for authentication, it designates the identity provider as the single source of truth for user identities and access control. This means administrators only need to manage the identity provider to handle tasks like provisioning, de-provisioning, and updating user roles or attributes. Changes made in the identity provider will be propagated to API7 Dashboard, ensuring consistent and accurate access control without the risk of configuration drift, effectively simplifying administration and preventing orphaned accounts.

### Bridge Access in Hybrid Cloud Environments[â](#bridge-access-in-hybrid-cloud-environments "Direct link to Bridge Access in Hybrid Cloud Environments")

In organizations deploying a mix of on-premises and cloud-based applications, the SSO option in API7 Dashboard helps facilitate consistent authentication across both environments. Legacy on-premises systems, which could still remain critical to many operations, can utilize LDAP for authentication, ensuring compatibility with established infrastructures. Meanwhile, modern cloud-native platforms are typically designed to integrate with protocols such as OIDC and SAML, offering the scalability and flexibility required for dynamic IT landscapes. By bridging these environments, SSO simplifies identity management and enhances the user experience, eliminating the need for multiple credentials and repetitive logins.
