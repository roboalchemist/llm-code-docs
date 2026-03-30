# Source: https://docs.axonius.com/docs/paloalto-prisma-access-insights.md

# Palo Alto Networks Prisma Access Insights

Prisma Access Insights is a monitoring tool that provides visibility into network traffic and security events.

<Callout icon="📘" theme="info">
  Note

  The Palo Alto Networks Prisma Access Insights adapter retrieves operational insights like user and device activity, Incident summaries, and application usage for monitoring. The adapter focuses on policy enforcement, network security, and traffic management, but does not work if Panorama manages Prisma Access. In short, Insights is for monitoring, while Prisma Access is for security management.
</Callout>

### Asset Types Fetched

* Devices
* Users
* Applications
* Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

An access token (also known as a bearer token) is required for authentication. To generate the access token, you need a Client ID, Client Secret, and TSG ID from your OAuth 2.0 service.

For detailed steps on generating the token, refer to [Access Tokens | Develop with Palo Alto Networks](https://pan.dev/sase/docs/access-tokens/).

### APIs

Axonius uses the [Prisma Access Insights 3.0 APIs](https://pan.dev/access/api/insights/).

### Permissions

To retrieve activity data from the Prisma Access Insights API, the API token must be associated with a service account that has sufficient rights to:

* Access the Prisma Access Insights product
* Perform read actions on activity and resource data
* Query user, device, and site-related telemetry through Insights API endpoints

If the service account does not have the appropriate RBAC roles assigned, the API requests may return partial results, no data, or trigger permission-related errors.

#### Supported From Version

Supported from Axonius version 6.1.69

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Palo Alto Networks Prisma Access Insights server.
2. **Client ID** and **Client Secret**  - The credentials for a user account that has the  Required Permissions to fetch assets.
3. **Tenant Service Group (TSG) ID** - Enter your tenant's unique ID. This ID is required to set the scope of the access token.  Do not include the **tsg\_id** prefix.
4. **PANW region** - Enter the `x-panw-region` header specific to your region. For more information and a list of regions, see [About x-panw-region](https://pan.dev/sase/docs/api-call/#about-x-panw-region).
5. **Fetch devices from the last X hours** - Specify the number of hours back from which to begin to fetch devices.

<Image alt="Palo Alto Networks Prisma Access Insights.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Palo%20Alto%20Networks%20Prisma%20Access%20Insights.png" />

### Optional Parameters

1. **Platform type (required to fetch applications)** - Select the platform type from the dropdown, either **Prisma Access** or **NGFW**.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).