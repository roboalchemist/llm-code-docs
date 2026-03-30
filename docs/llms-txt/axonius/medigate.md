# Source: https://docs.axonius.com/docs/medigate.md

# Medigate

Medigate is a medical device security platform that protects connected medical devices on health care provider networks, allowing inventory management and facilitating detection and prevention capabilities.

### Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password
* API Token

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Medigate Domain** - Enter the hostname of the Medigate server. When hosted by Medigate, the hostname used for API access with a token is `api.medigate.io`
2. **User Name** and **Password** (For old API) *(optional)* - The user name and password for the user used in the connection. Use this when you are connecting API V1. Vulnerabilities are only fetched when using API V1.

<Callout icon="📘" theme="info">
  Note

  **User Name** and **Password** are required when using API V1 and then API Token is not required.
</Callout>

3. **API Token (for new API)** *(optional)* - The API token - use this when you are connecting using API V2. When using API V2, vulnerabilities are not fetched.

<Callout icon="📘" theme="info">
  Note

  **API Token** is required when using API V2 and then **User Name** and **Password** are not required.
</Callout>

<Image align="left" alt="Medigate.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Medigate.png" />

### Optional Parameters

1. **Rate Limit (requests per second)** *(integer)*- Enter a value to configure the number of requests the adapter is allowed to make each second. The default is no value, meaning no limit is set.
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](https://docs.axonius.com/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **CIDR Exclusion List** *(optional)* - Specify in a comma-separated list the CIDR ranges of assets that you want to exclude from the fetch.
2. **Fetch Vulnerabilities** - Select this option to fetch vulnerabilities.
3. **Additional Custom Attributes** - Enter the following information to fetch additional custom attributes for each device from the API.
   * **Attribute** - Specify the name of the attribute in Medigate (i.e., custom\_attribute\_1).
   * **Attribute Name** - Specify the actual name of the field the attribute represents (i.e., Location, Owner, etc.). This will be the name of the field after parsing it in Axonius.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

### Related Enforcement Actions

* [Medigate by Claroty - User Actions](/docs/medigate-user-action)