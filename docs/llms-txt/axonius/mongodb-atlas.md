# Source: https://docs.axonius.com/docs/mongodb-atlas.md

# MongoDB Atlas Administration

MongoDB Atlas Administration provides automated administration for MongoDB so customers can manage clusters, projects, users, and more.

## Asset Types Fetched

* Users, Activities
  , Compute Services
  , Databases
  , Alerts/Incidents, Application Resources

## Before You Begin

### APIs

Axonius uses the [MongoDB Atlas Administration API (2.0)](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/).

### Required Permissions

The following permissions are required to fetch assets:

* Organization Member - For fetching users
* Read Write role - For fetching projects
* Project Read Only - For fetching database users

## Deploying the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the MongoDB Atlas Administration server.

2. **Public API Key** and **Private Key**- The API keys associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Organization ID** - A unique 24-hexadecimal digit string that identifies the organization that contains your projects.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/mongodb%20atlas.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Databases from Databases** - Enable to fetch Databases from the Databases endpoint.
2. **Fetch AuditActivities from Audit Log** - Enable to fetch AuditActivities from the Audit Log endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 6.1