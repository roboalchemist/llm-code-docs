# Source: https://docs.axonius.com/docs/identities-data-model-basic-concepts.md

# Identities Data Model - Basic Concepts

The following sections explain some of the concepts used in Identities.

## Entitlements

A broad term used to by us define anything assigned to a user. This is represented in the platform in the form of roles, groups, permissions, app assignments, resources and more.

## Users vs Managed Identities

Managed Identities is a subset of the Users asset, but it differs in that it only includes users that can actually be modified. For example, while CrowdStrike EDR may report users under the Users asset, these are merely artifacts of its reporting structure and not entities that can be actively managed. As a result, CrowdStrike EDR users would not appear under Managed Identities. This classification is manually adjusted by the IDM team.

## Managed Identities General Fields

* **Assigned Permissions** - Keeps a record of the atomic permissions assigned directly to the user.
* **Assigned Groups** - Keeps a record of the groups assigned directly to the user.
* **Assigned Roles** - Keeps a record of the roles assigned directly to the user.
* **Direct Assigned Applications** - Maintains a record of applications assigned directly to the user, which are third-party entities granted access through Single Sign-On and/or Identity Providers.
* **User Associated Resources** - Keeps a record of the resources assigned directly to the user. Resources are critical data objects within applications which are not files. For example: code repositories in GitHub, databases and tables in MySQL, vaults in 1Password.
* **Nested Permissions / Groups / Roles / Resources or Assigned Applications** - Keeps a record of the entitlements assigned directly or indirectly to the user. Each item points to its parent (if indirectly assigned).
* **Previous Permissions / Groups / Roles / Assigned Applications** - Keeps a record of all entitlements that had been previously assigned to the user, however were removed since.
* **Authentication Factors** - Keeps a record of the multi factor authentication modules the user have enrolled to, including its security strength classification according to the industry. To measure whether these have been used, it's essential to enable audit log retrieval from the MFA provider to track their usage timestamps.
* **Is Super Admin** - Keeps a record if the user has an owner level access to the app. This classification is manually adjusted by the IDM team.
* **Has Administrative Permissions** - Keeps a record if the user has any privileged level rights. This classification is manually adjusted by the IDM team.
* **Is User Suspended** - Maintains a record of user accounts that exist, however access to them had been manually halted.
* **Is Locked** - Maintains a record of user accounts that exist, however access to them had been automatically halted, probably by one of the vendor’s security mechanisms.
* **Is Used Deleted** - Maintains a record of whether the user is deleted. Some vendors maintain such users, and hence it should be reported that way. Generally, this flag will switch to True if an adapter’s fetch cycle completes successfully and no record of the same identity is found.
* **Is User External** - Maintains a record of whether the user is external to the organization, as classified by the vendor (e.g., collaborators in Google Drive).
* **Is User Deleted** - Maintains a record of whether the user has recently been deleted.
* **Is Service Account** - Keeps a record if the user is used for non-human activities. Either classified by the vendor itself (i.e. Integration Users in Workday, or Service Principals in Entra ID), or by IDM’s service account classifier.
* **Last Logon Date and Latest Activity Time** - The Last Logon Date records the user's most recent successful authentication, while the Latest Activity Time tracks the last action performed within the application. This distinction exists because authentication may not always be required frequently (e.g., when was the last time you signed into your Zoom app on your device?). This data depends on the customer enabling audit log fetching in the adapter’s advanced configuration. If audit logs are not enabled or the information is unavailable, the Latest Activity Time will default to the Last Logon Date.

## Managed Identities HR Fields

The platform maintains various aggregated human resources fields, such as User Department, but these are influenced by all connected adapters, regardless of type. For instance, Slack may contribute to this data, even though it may not accurately reflect the customer's actual organizational structure. Hence there exist such fields which are populated only by HR systems. For more information see here.

## Resource ID and Name in Directly Assigned Entitlements Fields

Each directly assigned entitlement includes a resource ID and name. If these fields are empty, the entitlement applies at the account level. Otherwise, it is scoped to a specific resource. For example, a user in a GitHub account may have a general user role without a resource ID or name. However, if they are granted admin access to a specific repository, a separate entry will indicate their admin role, with the resource ID and name referencing that repository.

## Justifications in Directly Assigned Entitlements Fields

Each directly assigned entitlement contains a justification object that details the history of how the user obtained it and whether it resulted from a legitimate operation or an out-of-band change.