# Source: https://documentation.wazuh.com/current/user-manual/user-administration/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# User administration

Learn how to change the user passwords, how to create new internal users and how to integrate Wazuh with different Identity Providers (IdP) to implement Single Sign-On (SSO).

In the password management section, you can find instructions on how to use the Wazuh passwords tool to change the passwords of both the Wazuh indexer and the Wazuh manager API users.

The RBAC section contains directions on how to create Wazuh indexer users, also known as internal users, assign them different roles and map them to the Wazuh manager API. Find out how to create an admin user, a read-only user, a custom user, and a user with permission to read and manage only a group of agents.

In the single sign-on section, you can find instructions on how to integrate Wazuh with different Identity Providers to implement Single Sign-On. Find instructions for Okta, Microsoft Entra ID, PingOne, Google, Jumpcloud and OneLogin.

In the LDAP integration section, you can find instructions on how to integrate Wazuh with LDAP/Active Directory to authenticate and authorize users.

> * [Password management](password-management.md)
>   * [Changing the password for single user](password-management.md#changing-the-password-for-single-user)
>   * [Changing the passwords for all users](password-management.md#changing-the-passwords-for-all-users)
>   * [Changing the passwords using a formatted file](password-management.md#changing-the-passwords-using-a-formatted-file)
>   * [Changing the passwords in a distributed environment](password-management.md#changing-the-passwords-in-a-distributed-environment)
> * [Wazuh RBAC - How to create and map internal users](rbac.md)
>   * [Creating and setting a Wazuh admin user](rbac.md#creating-and-setting-a-wazuh-admin-user)
>   * [Creating and setting a Wazuh read-only user](rbac.md#creating-and-setting-a-wazuh-read-only-user)
>   * [Creating an internal user and mapping it to Wazuh](rbac.md#creating-an-internal-user-and-mapping-it-to-wazuh)
>   * [Use case: Give a user permissions to read and manage a group of agents](rbac.md#use-case-give-a-user-permissions-to-read-and-manage-a-group-of-agents)
> * [Single Sign-On](single-sign-on/index.md)
>   * [Required parameters](single-sign-on/index.md#required-parameters)
>   * [Identity Providers](single-sign-on/index.md#identity-providers)
> * [LDAP integration](ldap.md)
>   * [LDAP server configuration](ldap.md#ldap-server-configuration)
>   * [Authentication and authorization configuration](ldap.md#authentication-and-authorization-configuration)
>   * [Map LDAP role to Wazuh dashboard](ldap.md#map-ldap-role-to-wazuh-dashboard)
