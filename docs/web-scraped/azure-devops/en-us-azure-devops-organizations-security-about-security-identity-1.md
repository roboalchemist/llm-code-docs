# Source: https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-security-identity?view=azure-devops

Title: About authentication, authorization, and security policies - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-security-identity?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Azure DevOps uses a combination of security concepts to ensure that only authorized users can access its features, functions, and data. Access is determined by two key processes: authentication, which verifies a user's credentials, and authorization, which grants permissions based on account entitlements. Together, these processes control what each user can do within Azure DevOps.

This article expands on [Get started with permissions, access, and security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops). It helps administrators understand the different account types, authentication and authorization methods, and security policies available to protect Azure DevOps environments.

* * *

**Account types**

*   Users
*   Organization owner
*   Service accounts
*   Service principals or managed identities
*   Job agents

**Authentication**

*   User credentials
*   Windows authentication
*   Two-factor authentication (2FA)
*   SSH key authentication
*   Microsoft Entra token
*   Personal access tokens
*   OAuth configuration
*   Active Directory authentication library

**Authorization**

*   Security group membership
*   Role-based access control
*   Access levels
*   Feature flags
*   Security namespaces and permissions

**Policies**

*   Privacy policy URL
*   Application connection and security policies
*   User policies
*   Git repository and branch policies

* * *

* * *

**Account types**

*   Users
*   Service accounts
*   Service principals or managed identities
*   Job agents

**Authentication**

*   User credentials
*   Windows authentication
*   Two-factor authentication (2FA)
*   SSH key authentication
*   Personal access tokens
*   OAuth configuration
*   Active Directory authentication library

**Authorization**

*   Security group membership
*   Role-based permissions
*   Access levels
*   Feature flags
*   Security namespaces and permissions

**Policies**

*   Git repository and branch policies

* * *

Azure DevOps supports software development from planning to deployment. It uses Microsoft Azure's platform as a service (PaaS) infrastructure and services, including Azure SQL databases, to provide a reliable, globally available service for your projects.

For more information about how Microsoft ensures your projects are safe, available, secure, and private, see the [Azure DevOps data protection overview](https://learn.microsoft.com/en-us/azure/devops/organizations/security/data-protection?view=azure-devops).

While human user accounts are the primary focus, Azure DevOps also supports various other account types for different operations:

*   **Organization owner**: The creator of an Azure DevOps Services organization or assigned owner. To find the owner for your organization, see [Look up the organization owner](https://learn.microsoft.com/en-us/azure/devops/organizations/security/look-up-organization-owner?view=azure-devops).
*   **Service accounts**: Internal Azure DevOps accounts used to support a specific service, such as Agent Pool Service, PipelinesSDK. For descriptions of service accounts, see [Security groups, service accounts, and permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops#collection-level-groups).
*   **Service principals or managed identities**: [Microsoft Entra applications or managed identities](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/service-principal-managed-identity?view=azure-devops) added to your organization to perform actions on behalf of a non-Microsoft application. Some service principals refer to internal Azure DevOps organization to support internal operations.
*   **Job agents**: Internal accounts used to run specific jobs on a regular schedule.
*   **Non-Microsoft accounts**: Accounts that require access to support webhooks, service connections, or non-Microsoft applications.

Throughout the security-related articles, "users" refers to all identities added to the Users Hub, which can include human users and service principals.

*   **Service accounts**: Internal Azure DevOps accounts used to support a specific service, such as Agent Pool Service, PipelinesSDK. For descriptions of service accounts, see [Security groups, service accounts, and permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops#collection-level-groups).
*   **Service principals or managed identities**: Microsoft Entra applications or managed identities added to your organization to perform actions on behalf of a non-Microsoft application. Some service principals refer to internal Azure DevOps organization to support internal operations.
*   **Job agents**: Internal accounts used to run specific jobs on a regular schedule.
*   **Non-Microsoft accounts**: Accounts that require access to support webhooks, service connections, or non-Microsoft applications.

The most effective way to manage accounts is by [adding them to security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops#security-groups-and-membership).

Note

The organization owner and members of the Project Collection Administrators group have full access to nearly all features and functions.

Authentication verifies a user's identity based on the credentials they provide during sign-in to Azure DevOps. Azure DevOps integrates with several identity systems to manage authentication:

*   **Microsoft Entra ID**: Recommended for organizations managing a large group of users. Provides robust, cloud-based authentication and user management.
*   **Microsoft account (MSA)**: Suitable for smaller user bases accessing Azure DevOps organizations. Supports cloud authentication.
*   **Active Directory (AD)**: Recommended for on-premises deployments with many users, using your existing AD infrastructure.

Microsoft Entra ID and Microsoft accounts both support cloud authentication. For more information, see [About accessing Azure DevOps with Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/access-with-azure-ad?view=azure-devops).

For on-premises environments, use Active Directory to efficiently manage user access. For more information, see [Set up groups for use in on-premises deployments](https://learn.microsoft.com/en-us/azure/devops/server/admin/setup-ad-groups).

Access your Azure DevOps organization programmatically without repeatedly entering your username and password by choosing one of the available [authentication methods](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops). Use the following methods to automate workflows, integrate with REST APIs, or build custom applications:

*   Use [OAuth](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops) to build applications that perform actions on behalf of users. Users must consent to the app. For new apps, use [Microsoft Entra OAuth](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/entra-oauth?view=azure-devops).
*   Use [service principals or managed identities](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/service-principal-managed-identity?view=azure-devops) to automate workflows or build tools that regularly access organization resources. These methods issue Microsoft Entra tokens on behalf of the application itself.
*   Use [Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/entra?view=azure-devops) for secure, cloud-based authentication and user management.
*   Use [personal access tokens (PATs)](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops) for ad-hoc requests or early prototyping. 

By default, your organization allows access for all authentication methods. Organization admins can [restrict access to these authentication methods by disabling security policies](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/change-application-access-policies?view=azure-devops). Tenant admins can further [reduce PAT risk by restricting the ways in which they can be created](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/manage-pats-with-policies-for-administrators?view=azure-devops). [](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-security-identity?view=azure-devops)

Authorization determines whether an authenticated identity has the required permissions to access a specific service, feature, function, object, or method in Azure DevOps. Authorization checks always occur after successful authentication—if authentication fails, authorization is never evaluated. Even after authentication, users or groups might be denied access to certain actions if they lack the necessary permissions.

Azure DevOps manages authorization through permissions assigned directly to users or inherited through security groups or roles. Access levels and feature flags can further control access to specific features. For more information, see [Get started with permissions, access, and security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops).

Security namespaces define user access levels for specific actions on Azure DevOps resources.

*   Each resource family, for example, work items or Git repositories, has its own unique namespace.
*   Within each namespace, there can be multiple access control lists (ACLs). 
    *   Each ACL contains a token, an inherit flag, and one or more access control entries (ACEs).
    *   Each ACE specifies an identity descriptor, a bitmask for allowed permissions, and a bitmask for denied permissions.

For more information, see [Security namespaces and permission reference](https://learn.microsoft.com/en-us/azure/devops/organizations/security/namespace-reference?view=azure-devops).

To secure your organization and code, organization-level ([Project Collection Administrator](https://learn.microsoft.com/en-us/azure/devops/organizations/security/look-up-project-collection-administrators?view=azure-devops)) or tenant-level ([Azure DevOps Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#azure-devops-administrator)) admins can enable or disable various security policies, depending on the policy scope. Key policies to consider include:

*   [Specify a privacy policy URL](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/add-privacy-policy-url?view=azure-devops) to describe how you handle internal and external guest data privacy.
*   Decide whether users in your organization are [allowed to create public projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/make-project-public?view=azure-devops).

If your organization is connected to Microsoft Entra ID, you have access to the following other security features:

*   [Restrict organization creation to specific users](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/azure-ad-tenant-policy-restrict-org-creation?view=azure-devops).
*   [Invite external guests to the organization](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/add-external-user?view=azure-devops).
*   [Allow team and project administrators to invite new users](https://learn.microsoft.com/en-us/azure/devops/organizations/security/restrict-invitations?view=azure-devops).
*   [Enable Conditional Access policy (CAP) validation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/change-application-access-policies?view=azure-devops#cap-support-on-azure-devops).
*   Track [auditing events and streams](https://learn.microsoft.com/en-us/azure/devops/organizations/audit/azure-devops-auditing?view=azure-devops) in your organization.

Review and configure these policies to strengthen your organization's security posture and ensure compliance with your data privacy and access requirements.

By default, users you add to an organization can view all organization and project information and settings. To limit access for specific users, you can enable the **Limit user visibility and collaboration to specific projects** preview feature. For more information, see [Project-scoped users group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions?view=azure-devops#project-scoped-users-group).

Warning

Consider the following limitations when using this preview feature:

*   The limited visibility features described in this section apply only to interactions through the web portal. With the REST APIs or `azure devops` CLI commands, project members can access the restricted data.
*   Users in the limited group can only select users who are explicitly added to Azure DevOps and not users who have access through Microsoft Entra group membership.
*   Guest users who are members in the limited group with default access in Microsoft Entra ID, can't search for users with the people picker.

To secure your code, set various Git repository and branch policies. For more information, see the following articles:

*   [Configure repository settings and policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/repository-settings?view=azure-devops)
*   [Configure branch policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops)
*   [Configure branch policy for an external service](https://learn.microsoft.com/en-us/azure/devops/repos/git/pr-status-policy?view=azure-devops)
*   [Use Azure Functions to create custom branch policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/create-pr-status-server-with-azure-functions?view=azure-devops)

Repositories and build and release pipelines pose unique security challenges that require additional security features. For more information, see the following articles.

*   [Securing Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/overview?view=azure-devops)
*   [Plan how to secure your YAML pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/approach?view=azure-devops)
*   [Repository protection](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/misc?view=azure-devops#protect-repositories)
*   [Pipeline resources](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/resources?view=azure-devops)
*   [Recommendations to securely structure projects in your pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/misc?view=azure-devops#protect-projects)
*   [Security through templates](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/templates?view=azure-devops)
*   [How to securely use variables and parameters in your pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/inputs?view=azure-devops)
*   [Recommendations to secure shared infrastructure in Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/misc?view=azure-devops#protect-shared-infrastructure)
*   [Other security considerations](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/misc?view=azure-devops)

*   [Default permissions and access assignments](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions-access?view=azure-devops)
*   [Add or delete users using Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory)
*   [Set up groups for use in on-premises deployments](https://learn.microsoft.com/en-us/azure/devops/server/admin/setup-ad-groups)
*   [Setting up HTTPS with Secure Sockets Layer (SSL)](https://learn.microsoft.com/en-us/azure/devops/server/admin/setup-secure-sockets-layer)
