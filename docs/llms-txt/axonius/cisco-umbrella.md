# Source: https://docs.axonius.com/docs/cisco-umbrella.md

# Cisco Umbrella

Cisco Umbrella is a secure internet gateway in the cloud, including DNS and IP layer enforcement and command and control callback blocking.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Roles
* SaaS Applications

## Parameters

1. **Cisco Umbrella Domain** *(optional, default: `https://api.umbrella.com`)* - The hostname or IP address of the Cisco Umbrella server.

2. **Network API Key** and **Network API Secret** *(optional)* - The API Key and API Secret for the Umbrella Network Devices API. For more information, see <Anchor label="Cisco Umbrella API Authentication" target="_blank" href="https://developer.cisco.com/docs/cloud-security/umbrella-api-authentication/">Cisco Umbrella API Authentication</Anchor>.

3. **Management API v2 Key** and **Management API v2 Secret** *(required)* - Enter the API Key and API Secret for the Umbrella Management API. For more information, see <Anchor label="Cisco Umbrella API Authentication" target="_blank" href="https://developer.cisco.com/docs/cloud-security/umbrella-api-authentication/">Cisco Umbrella API Authentication</Anchor>.

4. **Fetch deployments scope** (devices) *(default: true)*,  **Fetch admin scope** (users and roles) *(default: true)*,  **Fetch reports scope (SaaS applications)** *(only used to fetch SaaS data)* *(default: true)*  - Axonius fetches all data, using one connection, make sure you use an API key that has all permissions. However, it is possible to set API keys with permissions to fetch only a certain type of data. For that, select the scope that your API key has permissions to fetch data from. If you have different API keys for each scope, set up a different connection with the corresponding scope/resource selected.

5. **mspID** *(optional, default: empty)* - The managed service provider ID. It is required if you are using Cisco Umbrella for MSPs.

6. **Organization ID** *(optional, default: empty)* - Every Umbrella organization is a separate instance of Umbrella and has its own dashboard. Organizations are identified by their name and their organization ID (Org ID). The Org ID is a unique number. You can have access to several organizations. Once you are logged into the correct dashboard, check the URL in the address bar: `https://dashboard.umbrella.com/o/<OrgID>/#/< page>`. represents your unique Umbrella Org ID.

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CiscoUmbrellaNew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoUmbrellaNew.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **List the users in the organization** - Select this option to fetch a list of users in the organization. Note that this setting is only for CAASM.
* **Ignore SaaS Applications Repository and parse all applications** - Select this option to skip validating apps agains the Axonius SaaS Applications Repository and parse all apps coming from the Cisco Umbrella API.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Cisco Cloud Security APIs](https://developer.cisco.com/docs/cloud-security/#!introduction).

## Required Permissions

The following permissions are required to fetch SaaS data:

* admin.roles:read
* admin.users:read
* deployments.roamingcomputers:read
* reports.aggregations:read

## Setting Up the Integration

Log into Umbrella.

1. Navigate to **Admin** `>` **API Keys**. If in a Multi-org, Managed Service Provider (MSP), or Managed Secure Service Provider (MSSP) console, navigate to **Console Settings** `>` **API Keys**.
2. Click **API Keys** and then click **Add**.
3. Enter a name for the key. A name must contain less than 256 characters.
4. Check all scopes and grant all read only access.
5. Choose **Never expire**.
6. Click **Generate Key**.
7. Copy and save your API Key and Key Secret.

<Callout icon="📘" theme="info">
  Note

  Copy the generated **API Key** and **Key Secret** to  **Network API Key** / **Network API Secret**, and to **Management API Key** and **Management API Secret**.
</Callout>

7. Click **Accept** and **Close**.