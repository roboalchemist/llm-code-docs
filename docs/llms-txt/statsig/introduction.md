# Source: https://docs.statsig.com/statsigcli/introduction.md

# Source: https://docs.statsig.com/statsig-warehouse-native/introduction.md

# Source: https://docs.statsig.com/statsig-warehouse-native/geotests/introduction.md

# Source: https://docs.statsig.com/statsig-warehouse-native/cure/introduction.md

# Source: https://docs.statsig.com/metrics/introduction.md

# Source: https://docs.statsig.com/integrations/terraform/introduction.md

# Source: https://docs.statsig.com/integrations/introduction.md

# Source: https://docs.statsig.com/integrations/azureai/introduction.md

# Source: https://docs.statsig.com/infrastructure/introduction.md

# Source: https://docs.statsig.com/infrastructure/api_proxy/introduction.md

# Source: https://docs.statsig.com/guides/sidecar-experiments/introduction.md

# Source: https://docs.statsig.com/data-warehouse-ingestion/introduction.md

# Source: https://docs.statsig.com/console-api/introduction.md

# Source: https://docs.statsig.com/autotune/contextual/introduction.md

# Source: https://docs.statsig.com/access-management/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspace Management Overview

Statsig provides a few different solutions for access management as you scale out adoption in your team/org/company.

We have simple settings like automatically adding new users with the same email domain to your project, but we also offer SSO to simplify the process for inviting your team to your Projects.

To get started, learn more about Statsig's [organization](/access-management/organizations) and [project](/access-management/projects) abstractions.

***

## SSO vs SCIM

In many enterprise environments, [SSO](/access-management/sso/overview) and [SCIM](/access-management/scim/overview) are used together to enhance both security and usability.

* SSO handles the authentication aspect, allowing users to log in once to access multiple applications.
* SCIM ensures that user accounts and permissions are consistently managed across those applications.

### Example Scenario:

* Onboarding a New Employee:
  * SCIM: Automatically provisions the employee’s user accounts in all necessary applications based on their role.
  * SSO: Allows the employee to access all these applications with a single set of login credentials.
* Offboarding an Employee:
  * SCIM: Automatically deactivates or deletes user accounts, removing access.
  * SSO: No longer authenticates the user since their credentials are disabled.

### Summary:

* SSO focuses on simplifying the user login experience by centralizing authentication across multiple applications.
* SCIM focuses on automating the management of user identities and attributes across different systems.

By using both SSO and SCIM, organizations can achieve a more secure, efficient, and user-friendly approach to identity and access management.


Built with [Mintlify](https://mintlify.com).