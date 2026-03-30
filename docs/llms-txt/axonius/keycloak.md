# Source: https://docs.axonius.com/docs/keycloak.md

# Keycloak

Keycloak is an open source identity and access management solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Keycloak domain** *(required)* - The domain or IP address of the Keycloak admin.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Realm name** *(optional, default: master)* - The desired realm name to fetch users.
4. **Client ID** *(optional, default: admin-cli)* - The client entity associated with Keycloak admin.
5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Keycloak.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Keycloak.png)

## APIs

Axonius uses the [Keycloak Admin REST API](https://www.keycloak.org/docs-api/latest/rest-api/index.html).

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to the realm that was supplied in [Client ID](#parameters) or to master realm.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                | Supported | Notes |
| ---------------------- | --------- | ----- |
| Keycloak Version 9.0.3 | Yes       |       |