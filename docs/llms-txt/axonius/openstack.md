# Source: https://docs.axonius.com/docs/openstack.md

# OpenStack

OpenStack is an open source software solution for creating private and public clouds.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

You can configure a number of connections for the OpenStack adapter. It is possible to both configure the parameters here, and in addition to use a JSON file to enter credentials for any number of connections.  Axonius uses all of the connections configured (both using the credentials  below, and those in the JSON file)

1. **Authentication URL** *(optional)* - An authentication URL for the Identity service.
2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets.
   * Administrator Credentials can fetch from multiple projects to which they are assigned. That is, if a user exists across multiple projects/tenants the user must have admin right in order to also be used in a successful fetch.
   * Non-administrator credentials can only fetch from a single project.
3. **Project** *(optional)* - The project name.
4. **Domain** *(optional, default: empty)* - The Domain of the project. This is a required part of the scope object.
5. **Additional openstack hosts JSON file** - You can  configure a connection using parameters in this dialog box, or also upload additional connection parameters them from a JSON file here. Click to upload the file.
   The JSON file is   in the format of a single list containing dictionaries, where each dictionary must at least contain the   **Authentication URL** and should contain the additional fields above, *User Name/Password*, *Project* and *Domain*, if they were not configured in the adapter configuration pane itself.  If the JSON file does not contain the User Name/Password, Project and Domain, then the settings are used from the Configuration screen when the fetch is performed.
   The  JSON file should be in the format below:

```json
[
  {
    "auth_url": "<auth url>", # (1)
    "username": "<username>", # (2)
    "password": "<password>", # (2)
    "project": "<project>", # (3)
    "domain": "<domain>", # (4)
    "verify": True/False # Verify SSL
  }
]
```

Each field in the configuration screen above  must either be configured in the dialog box, or in the JSON file, or both. When the configuration values are contained in the JSON file, the values in the file are used for that connection. If any values are not in the file for a specific connection, the values for that field ar taken from this dialog box.

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="openstack" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/openstack.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Fetch Hypervisors as Assets** - Select this option to fetch  Hypervisor entities as Assets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [OpenStack API](https://docs.openstack.org/api-quick-start/api-quick-start.html#authentication-and-api-request-workflow).