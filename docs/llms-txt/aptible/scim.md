# Source: https://www.aptible.com/docs/core-concepts/security-compliance/authentication/scim.md

# Provisioning (SCIM)

> Learn about configuring Cross-domain Identity Management (SCIM) on Aptible

<Frame> <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5260a9ef9a9db23bb071b37d227c3f4a" alt="" data-og-width="2798" width="2798" data-og-height="1610" height="1610" data-path="images/scim-app-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=071934bf1f70707bafb512a0cd4ae747 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=824ed9af14a135f5150b6d3a69185cd3 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=54b811abcf11736862deaa76eeaaab5b 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=fb58221cd08909817daaeaa58d5e7630 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=30b6e5063e17a311d283de916ad069c9 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e9b2db705777beebe884e66910bcf195 2500w" /> </Frame>

## Overview

Aptible has implemented **SCIM 2.0** (System for Cross-domain Identity Management) to streamline the management of user identities across various systems. This implementation adheres closely to [RFC 7643](https://datatracker.ietf.org/doc/html/rfc7643), ensuring standardized communication and data exchange. SCIM 2.0 simplifies provisioning by automating the processes for creating, updating, and deactivating user accounts and managing roles within your organization. By integrating SCIM, Aptible enhances your ability to manage user data efficiently and securely across different platforms.

## How-to Guides

We offer detailed guides to help you set up provisioning with your Identity Provider (IdP). These guides cover the most commonly used providers:

* [Aptible Provisioning with Okta](/how-to-guides/platform-guides/scim-okta-guide)
* [Aptible Provisioning with Entra ID (formerly Azure AD)](/how-to-guides/platform-guides/scim-entra-guide)

These resources will walk you through the steps necessary to integrate SCIM with your preferred provider, ensuring a seamless and secure setup.

## Provisioning FAQ

### How Does SCIM Work?

SCIM (System for Cross-domain Identity Management) is a protocol designed to simplify user identity management across various systems. It enables automated processes for creating, updating, and deactivating user accounts. The main components of SCIM include:

1. **User Provisioning**: Automates the creation, update, and deactivation of user accounts.
2. **Group Management**: Manages roles (referred to as "Groups" in SCIM) and permissions for users.
3. **Attribute Mapping**: Synchronizes user attributes consistently across systems.
4. **Secure Token Exchange**: Utilizes OAuth bearer tokens for secure authentication and authorization of SCIM API calls.

### How long is a SCIM token valid for Aptible?

A SCIM token is valid for one year. After the year, if it expires, you will receive an error in your IDP indicating that your token is invalid.

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-token-invalid.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=bdea02197c187d3f51e721cae94ef400" alt="" data-og-width="1512" width="1512" data-og-height="230" height="230" data-path="images/scim-token-invalid.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-token-invalid.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=dac78c4259ffa603f635b268e3c5a0bf 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-token-invalid.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c9e5b90cf9bf9ef9bc4f45a7b3554dbb 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-token-invalid.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=aa204a0694bd9815d1e71c2b3a0a3b94 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-token-invalid.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c1a2f62e1b42337006fc55c3e7766a6e 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-token-invalid.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8c145808a89d3a16ef7dfcbee102d0c8 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-token-invalid.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a90584e0334f23a2bc7827abf031f238 2500w" />

### Aptible Does Not Seem to Support Groups but Roles Instead. How Does That Work with SCIM?

Aptible leverages **Roles** instead of **Groups**. Despite this, the functionality is similar, and SCIM Groups are mapped to Aptible Roles. This mapping ensures that permissions and access controls are maintained consistently.

### What Parts of the SCIM Specifications Aren't Included in Aptible's SCIM Implementation?

Aptible aims to continually enhance support for SCIM protocol components. However, some parts are not currently implemented:

1. **Search Queries Using POST**: Searching for resources using POST requests is not supported.
2. **Bulk Operations**: Bulk operations for creating, updating, or deleting resources are not supported.
3. **/Me Endpoint**: Accessing the authenticated user's information via the /Me endpoint is not supported.
4. **/Schemas Endpoint**: Retrieving metadata about resource types via the /Schemas endpoint is not supported.
5. **/ServiceProviderConfig Endpoint**: Accessing service provider configuration details via the /ServiceProviderConfig endpoint is not supported.
6. **/ResourceTypes Endpoint**: Listing supported resource types via the /ResourceTypes endpoint is not supported.

### How Much Support is Required for Filtering Results?

While the SCIM protocol supports extensive filtering capabilities, Aptible's primary use case for filtering is straightforward. Aptible checks if a newly created user or group exists in your application based on a matching identifier. Therefore, supporting the `eq` (equals) operator is sufficient.

### I am connecting to an account with users who are already set up. How Does SCIM Behave?

When integrating SCIM with an account that already has users, SCIM will:

1. **Match Existing Users**: It will identify existing users based on their unique identifier (email) and update their information if needed rather than creating new accounts.
2. **Create New Users**: If a user does not exist, SCIM will create a new account with the specified attributes and assign the default role (referred to as "Group" in SCIM).
3. **Role Assignments**: Newly created users will receive the default role. Existing role assignments for users already in the system will not be altered. SCIM will not remove or change existing roles.

### How Do I Correctly Disable SCIM and Retain a Clean Data Set?

To disable SCIM and manage the associated data within your Aptible Organization:

1. **Retaining Created Roles and Users**: If you want to keep the roles and users created by SCIM, simply disable SCIM as an Aptible Organization owner. This action will remove the SCIM association but leave the created users and roles intact.

2. **Removing SCIM-Created Data**: If you wish to remove users and roles created by SCIM, begin by unassigning any users and roles in your Identity Provider (IDP) that were created via SCIM. This action will soft delete these objects from your Aptible Organization. After all assignments have been removed, you can then deactivate the SCIM integration, ensuring a clean removal of all associated data.

### What authentication methods are supported by the Aptible SCIM API?

Aptible's SCIM implementation uses the **OAuth 2.0 Authorization Code grant flow** for authentication. It does not support the Client Credentials or Resource Owner Password Credentials grant flows. The Authorization Code grant flow is preferred for SaaS and cloud integrations due to its enhanced security.

### What is Supported by Aptible?

Aptible's SCIM implementation includes the following features:

1. **User Management**: Automates the creation, update, and deactivation of user accounts.
2. **Role Management (Groups)**: This function assigns newly created users the specified default role (referred to as "Groups" in SCIM).
3. **Attribute Synchronization**: Ensures user attributes are consistently synchronized across systems.
4. **Secure Authentication**: Uses OAuth bearer tokens for secure SCIM API calls.
5. **Email as Unique Identifier**: Uses email as the unique identifier for validating and matching user data.

### I see you have guides for Identity Providers, but mine is not included. What should I do?

Aptible follows the SCIM 2.0 guidelines, so you should be able to integrate with us as long as the expected attributes are correctly mapped.

> 📘 Note We cannot guarantee the operation of an integration that has not been tested by Aptible. Proceeding with an untested integration is at your own risk.

**Required Attributes:**

* **`userName`**: The unique identifier for the user, essential for correct user identification.
* **`displayName`**: The name displayed for the user, typically their full name; used in interfaces and communications.
* **`active`**: Indicates whether the user is active (`true`) or inactive (`false`); crucial for managing user access.
* **`externalId`**: A unique identifier used to correlate the user across different systems; helps maintain consistency and data integrity.

**Optional but recommended Attributes:**

* **`givenName`**: The user's first name; can be used as an alternative in conjunction with familyName to `displayName`.
* **`familyName`**: The user's last name; also serves as an alternative in conjunction with givenName to `displayName`.

**Supported Operations**

* **Sorting**: Supports sorting by `userName`, `id`, `meta.created`, and `meta.lastModified`.
* **Pagination**: Supports `startIndex` and `count` for controlled data fetching.
* **Filtering**: Supports basic filtering; currently limited to the `userName` attribute.

By ensuring these attributes are mapped correctly, your Identity Provider should integrate seamlessly with our system.

### Additional Notes

* SCIM operations ensure that existing user data and role assignments are not disrupted unless explicitly updated.
* Users will only be removed if they are disassociated from SCIM on the IDP side; they will not be removed by simply disconnecting SCIM, ensuring safe user account management.
* Integrating SCIM with Aptible allows for efficient and secure synchronization of user data across your identity management systems.

For more detailed instructions on setting up SCIM with Aptible, please refer to the [Aptible SCIM documentation](#) or contact support for assistance.
