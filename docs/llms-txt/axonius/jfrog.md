# Source: https://docs.axonius.com/docs/jfrog.md

# JFrog Artifactory

JFrog Artifactory is a DevOps solution for housing and managing artifacts, binaries, packages, files, containers, and components throughout the software development lifecycle.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the JFrog Artifactory server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Token** *(optional)* - A Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information about how to create a token, see [ACCESS - JFrog Help Center](https://jfrog.com/help/r/jfrog-rest-apis/create-token).

<Callout icon="📘" theme="info">
  Note

  JFrog is in the process of deprecating the use of API Keys. As of Artifactory version 7.98.x, Artifactory no longer supports creating new API Keys. Therefore, the only authentication option is to use **User Name** and **Password**.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![JFrog](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JFrog.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch repositories artifacts** - Select whether to fetch repository artifacts.
2. **Fetch Users** - By default Axonius fetches users. Clear this option to not fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [JFrog REST API](https://www.jfrog.com/confluence/display/JFROG/REST+API).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Required Permissions

The value supplied in [Token](#parameters) must be associated with credentials that have Read-only permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 1.0.0   | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.6