# Source: https://docs.axonius.com/docs/dynatrace.md

# Dynatrace

Dynatrace is a software intelligence platform providing application performance management and cloud infrastructure monitoring.

### Asset Types Fetched

* Devices, Aggregated Security Findings, Users, SaaS Applications, Compute Services, Load Balancers, Databases, Containers, Object Storage

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Dynatrace API](https://www.dynatrace.com/support/help/dynatrace-api).

### Permissions

* To execute user requests, the User sessions (DTAQLAccess) permission must be assigned to an API token.

* To execute entity requests, the Read entities (entities.read) permission must be assigned to an API token.

In addition
(DataExport), which is "Access problems and event feed, metrics and topology" permissions are required.

To learn how to obtain tokens and use them, see [Dynatrace API - Tokens and Authentication](https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication).

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Dynatrace Domain (for On-Premise)** *(required for on-prem or FedRAMP environments)* - If you are operating your own Dynatrace Managed installation or Dynatrace for Government (FedRAMP), you must specify your Dynatrace domain. This is optional if you are using the commercial SaaS instance of Dynatrace.
2. **Environment ID** - Specify the desired environment ID. Each environment that you monitor with Dynatrace is identified with a unique character string (Environment ID).
   * Within Dynatrace SaaS, your Dynatrace environment ID (otherwise known as a tenant ID), is included at the beginning of your Dynatrace environment´s URL:
     <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(730).png" />

   * If you are operating your own Dynatrace Managed installation, you can find your environment ID within your custom domain path after the /e/ subpath (see highlight in image below).
     <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(731).png" />

   * You can also find your environment ID listed on your Dynatrace account page along with your licensing details. To find this page, click the **User** button in the upper-right corner of the menu bar and select **Account settings**.
3. **API Key** - Specify the API token that you have created. For more details, see [Dynatrace API - Authentication](https://www.dynatrace.com/support/help/extend-dynatrace/dynatrace-api/basics/dynatrace-api-authentication/).
4. **API Version** *(default: v1)* - Select whether to use API v1 or v2.

<Image alt="Dynatrace.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dynatrace.png" />

### Optional Parameters

1. **Account UUID** - Enter an account UUID in order to fetch the users from a different API endpoint that includes more data and user groups. Find the account UUID on the *Account* `>` *Account management* API page, during creation of an OAuth client.
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch users** -  Select this option to fetch users.

<Callout icon="📘" theme="info">
  Note

  To fetch users, the User sessions (DTAQLAccess) permission must be assigned to an API token.
</Callout>

2. **Fetch vulnerabilities** - Toggle on  this option to fetch vulnerabilities.
3. **Fetch 'Security problems' extra info** - Select this option to fetch additional information about Dynatrace 'Security problems'. This option is only available if you toggle on **Fetch vulnerabilities**.
4. **Fetch process group instances** - Select this option to fetch Process Group instances.
5. **Categorize devices as compute services assets** - Select this option to categorize devices under different asset types.
6. **List of types to fetch** - From the dropdown select one or more entity types to fetch.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Dynatrace - Add Custom Tag](/docs/dynatrace-add-custom-tag)