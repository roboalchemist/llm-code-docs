# Source: https://docs.axonius.com/docs/identity-overview.md

# Identity Assets Overview

The Identify category is a category for Identity related assets.
They include:

* **[Users](/docs/users-page)** - Digital records of users, from basic identifying information to assigned groups, configurations, and actual sign-in accounts for individuals or machines.

* **Groups** - User groups, which typically affect permissions.

* **Roles** - Assets describing roles attachable to other services, which affect permissions.

* **Organizational Units** - Assets referring to distinct divisions or departments within a larger organization, often used to organize operations.

* **Accounts** - Lists discovered accounts and tenants for various SaaS, cloud, or on-premises services and applications.

* **Certificates** - Lists discovered certificates within SaaS, cloud, or on-premises services and applications.

* **Permissions**  - User-related permissions discovered from SaaS applications, typically fetched by adapters such as Okta, Microsoft EntraID, and AWS.

* **Rules** - A set of conditions that determine which identities receive specific entitlements or permissions.

* **Profiles** - A set of entitlements or permissions grantable to a managed identity.

* **Managed Identities** - A specific type of user that can be managed via the Axonius platform as part of the Identities module.

* **Job Titles** - Assets related to job titles, fetched by identity-related adapters such as Okta.

* **Justifications** - Why a specific entitlement/permission was granted or not granted.

Each Identity type is presented on its own page.

* All the Assets pages have similar capabilities as described in [Assets Page](/docs/assets-page).
* Learn about [Working with Assets](/docs/working-with-assets-pages)

## Association Fields

Association fields pull data from one asset to display in an associated asset. The following Association fields exist between the asset entities in this section:
**AD Group Members** - This field displays the AD users who belong to this group. For each user, the field shows their username, email, Internal User ID, and SID. You can also choose to display just one of these parameters.