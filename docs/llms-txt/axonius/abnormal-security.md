# Source: https://docs.axonius.com/docs/abnormal-security.md

# Abnormal Security

Abnormal Security is an email security provider that helps companies protect against targeted email attacks.

### Asset Types Fetched

* Users, Alerts/Incidents

<Callout icon="📘" theme="info">
  Note

  This adapter only brings users that have been noted in threats in the past 7 days from the fetch.
</Callout>

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the [Abnormal Security Client API](https://app.swaggerhub.com/apis/abnormal-security/abx/1.4.2#/info).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Abnormal Security server.

2. **Email Domain** - Email domain for filtering emails inside threats. Example of a valid email domain: axonius.com. Also can be a comma-separated list of email domains, i.e., axonius.com,axonius.io.

3. **Token** - An API Token associated with a user account that has permissions to fetch assets. For information on how to generate the token, see [Generating the authentication token](https://app.swaggerhub.com/apis/abnormal-security/abx/1.4.2#/info).

<Image alt="Abnormal Security" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Abnormal%20Security.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoints Config

Select and enable the settings listed under this section to enrich employees with additional data from specific endpoints.

* **Enrich Employee with Employee identity**, **Enrich Employee with Employee logins**, and **Enrich Employee with Campaigns details** - Enable each option to enrich the employee with information from the provided endpoint (for example, the Identity endpoint).
* **Enrich Employee with Threats details - CSV** - Enable this option to enrich the employee with information from the `threats_export/csv` endpoint. If you enable this, **don't** enable **Enrich Employee with Threats - API**.
* **Enrich Employee with Threats - API** - Enable this option to enrich the employee with threat info from the `threats` endpoint. This will automatically gather the threat details for the employee. If you enable this, **don't** enable **Enrich Employee with Threats details - CSV**. Enabling this makes the following setting available:
  * **Enrich Threats - API with Threats details - API** - Enable this option to enrich threats with information from the `threats_export/api` endpoint.

### "Days ago" Section

**Days ago - applies context on the following endpoints: Threats details CSV context, Threats details - CSV, Campaigns, Threats - API** - Expand this section to configure how far back the fetch of threat details should run. The default is to fetch data from the past 7 days.

This following settings allow you to fetch an asset from a specific endpoint and configure how far back the fetch should run.

**Example:**

**Fetch Users of sub type recipient from Recipient Employees** - Enable this option to fetch users of the subtype recipient from the Recipient Employees endpoint. After enabling this, expand the **Days ago - applies context on the following endpoints: Recipient Employees** section and configure how far back the fetch should run (the default is 7).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>