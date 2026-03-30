# Source: https://docs.axonius.com/docs/microsoft-active-directory-ad.md

# Microsoft Active Directory (AD)

## Overview

**Active Directory (AD)** is Microsoft’s directory service that stores information about users, groups, devices, and other resources in a Windows domain. It is commonly used for authentication, authorization, and centralized management in enterprise environments.

The Microsoft Active Directory adapter connects Axonius to an AD domain. It retrieves user, group, device, and organizational information to support asset inventory, correlation, and security analysis. The adapter supports LDAP, LDAPS, and Kerberos connection methods.

### Use cases the adapter solves

The adapter connects to Active Directory to identify users and devices, collecting data such as group memberships, organizational units, OS type, and distribution. This helps detect unmanaged Windows systems, verify agent coverage, analyze user access, and find over-privileged or inactive accounts, organizational units, OS type, and distribution. This helps detect unmanaged Windows systems, verify agent coverage, analyze user access, and find over-privileged or inactive accounts.

## Types of Assets Fetched

![](https://files.readme.io/ec086cdf823db1e0ed64d98c6c85dcd48fda2e0e85f020a1c48e19102d693c7e-devices.svg) Devices ![](https://files.readme.io/3df2652b3ae372a16f17272613c0d7ca2c6495ed1eee7d209569c3860086ebd1-users.svg) Users ![](https://files.readme.io/085e5879d236e9ffb784ca783b50d7ce35047123bbd547ddde8bd16a82d5eedb-groups.svg) Groups  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Url.svg) Domains & URLs ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/OU.svg) Organizational Units ![](https://files.readme.io/66e2d736ae845c1f84043eca01fd81bda00e2ea2e120bedc93ae071ae0c4317e-compute-services.svg) Compute Services ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Networks.svg) Networks ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts.svg) Accounts/Tenants ![](https://files.readme.io/634d21eaf6e9f69a19cd0f00cba1bc8d45f48efd6b450685f11540af9e6efe3d-permissions.svg) Permissions

***

## Data Retrieved from Active Directory

* **Devices**: hostname, domain, OU, trusts, site, network details (interfaces, VLANs, IPs, MACs)
* **Users**: username/UPN, display name, email, group memberships, OU memberships, password & logon data, account state, computed “Is Admin”
* **Groups**: group metadata, memberships, customized group attributes (optional)
* **Permissions**: user and group permissions (when Fetch Permissions via WinRM is enabled)
* **Networks**: AD sites and subnets (when Fetch Subnets from Sites is enabled)

<Callout icon="📘" theme="info">
  **Note**:

  '**Is Admin**':

  Axonius describes 'Is Admin' for users in Active Directory. 'Is Admin' is described as 'Yes':

  * If the user is a member of the "Domain Admins" group (Default Active Directory Domain-Wide Admin Group)
  * Or a member of any of the groups listed in the Admin Groups setting on the 'Advanced Configuration' screen.
  * Or part of the Administrators group.

  **'Last Seen in Domain**'
  Axonius shows you the 'Last Seen in Domain'. This value is calculated by Axonius by gathering all the information that indicates movement on that asset (for instance 'last password change', 'last logon', 'last logoff' and more). It is then sorted to get the value which is the most recent, and this is the value that populates the 'Last Seen in Domain' field.
</Callout>

## Before You Begin

### Authentication Methods

* Service Account with username/password
* Kerberos authentication (realm-based with SASL GSSAPI)

### Required Permissions

The service account used by the adapter must have the following permissions:

* Read access to the domain
* Membership in the **Remote Management Users** group
* Membership in the **Account Operators** group
* Interactive logon disabled

<br />

## Related Enforcement Actions

Refer to [Active Directory Related Enforcement Actions](https://docs.axonius.com/axonius-help-docs/docs/active-directory-related-enforcement-actions) .

<br />