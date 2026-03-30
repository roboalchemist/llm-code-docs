# Source: https://docs.axonius.com/docs/claroty-cloud.md

# Claroty xDome

Claroty xDome is a cyber-physical security (CPS) platform for IoT security.

### Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications, Databases

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* API Token for on-prem

### Permissions

Consult with your vendor for permissions for reading the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Claroty Domain** -  Enter the hostname of the Claroty server. When hosted by Claroty, the hostname used for API access with a token is `api.claroty.com`
2. **User Name** and **Password** *(For legacy API)* - The user name and password for the user used in the connection. Use this when you are connecting using the older version of the API.

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Token** - The API token - use this when you are connecting using the new API.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

<Image alt="Claroty%20Cloud" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ClarotyCloud.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **CIDR Exclusion List** - Specify in a comma-separated list the CIDR ranges of assets that you want to exclude from the fetch.
2. **Parse device OS information** - Select this option to parse the OS information for each device.
3. **Ignore retired devices** - Select this option so the adapter will filter retired devices using the API.
4. **Fetch vulnerabilities** - check this option to fetch vulnerability data from Claroty xDome (parsed as Aggregated Security Findings).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Claroty xDome - User Actions](/docs/claroty-cloud-user-action-per-entity)