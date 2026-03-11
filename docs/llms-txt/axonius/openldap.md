# Source: https://docs.axonius.com/docs/openldap.md

# OpenLDAP

OpenLDAP Software is an open source implementation of the Lightweight Directory Access Protocol.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Groups

## Parameters

1. **Host** *(required)* - The hostname, IP address or the complete URL format of the OpenLDAP server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets to log in for the simple bind.

3. **Use SSL** - Specify whether to use the connection on a secure port. When selected, the secure port is usually set to 636.

4. **Port** *(optional)* - The port used for the connection. A customized port can be used. The default is 389 for connections without SSL, and 636 for SSL connections.

5. **Fallback Host** *(optional)* - Enter a host to use in case connecting with the first one fails.

6. **Fallback Port** *(optional)* - Enter a port to use in case connecting with the first one fails.

7. **Users Custom Attributes** *(optional, comma-separated)* -  A comma-separated list of additional user attributes to fetch.

8. **Devices Custom Attributes** *(optional, comma-separated)* - A comma-separated list of additional device attributes to fetch.

9. **Users Object Classes** *(required, comma-separated)* - Enter one or more object classes of users, separated by commas.

10. **Devices Object Classes** *(required, comma-separated)* - Enter one or more object classes of devices, separated by commas.

11. **Override Search Base** *(optional)* - Specify the desired search base location to search for a particular directory object. When this parameter is left empty, the adapter uses the default search base location.

12. **Retrieve operational attributes** *(optional)* - Select whether to retrieve LDAP operational attributes, which are used internally by the server.

13. **Fetch Devices** *(required, default: true)* - Select whether to fetch devices.

14. **Fetch Users** *(required, default: true)* - Select whether to fetch users.

15. **Use RACF Schema** - Select this option to update the adapter that this LDAP Tree is from an IBM RACF server so it can use a proper schema to retrieve the tree nodes and sub-tree nodes.

16. **Search Receive Timeout** *(optional, default: 10)* - This variable defines the length of time the adapter will wait for the LDAP Server to respond when searching, before throwing a timeout exception.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="openldap" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-RHNR4XWW.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Correlate Mail Using Owner Email** - Select whether to populate the **Mail** field with the contents of the specific **Owner Email** field.
* **Fetch Groups** - Select to fetch Groups. This will also enrich Users with Groups data. When this is enabled, you have the option to enter a comma-separated list of Groups Object Classes to fetch.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Host](#parameters) via the following ports:

* Port 389 for a connection without SSL
* Port 636 for an SSL connection

## Required Permissions

The value supplied in [User Name](#parameters) must have read-only permissions for the OpenLDAP server.

## Supported From Version

Supported from Axonius version 4.5