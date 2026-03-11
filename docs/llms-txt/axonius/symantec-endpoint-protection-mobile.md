# Source: https://docs.axonius.com/docs/symantec-endpoint-protection-mobile.md

# Symantec Endpoint Protection Mobile

Symantec Endpoint Protection Mobile is a security solution that offers mobile device protection and management.

### Asset Types Fetched

* Devices, Users, Organizational Units

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Token

### APIs

Axonius uses the [Symantec Endpoint Protection Mobile RESTul API](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection-mobile/1-0/integrations/about-the-rest-api-v132113870-d4221e15634.html).

### Permissions

Access to the endpoint in the SEP Mobile API is controlled through an API token mechanism. This token must be associated with an account that has appropriate permissions to access organizational device data.

**Access Control Summary**:

* Authentication is performed using an `auth_token` (API token). While the `organization_id` is not required for authentication itself, it is often required as part of the request payload or parameters when accessing most API endpoints.
* The API token must be tied to an account with sufficient privileges to view mobile device inventory within the organization. Typically this means administrative or integration-level roles.
* Role-Based Access Control (RBAC) applies: accounts with restricted roles may receive incomplete data or encounter authorization failures when calling endpoints outside their permissions.

**Recommendations**:

* Ensure that the account used to obtain the API token has organization-wide visibility over device data.

* Review role permissions assigned to the account, especially if you observe partial or filtered results when querying devices.

#### Supported From Version

Supported from Axonius version 6.1.73

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Symantec Endpoint Protection Mobile server.
2. **Authentication Token** - An Authentication Token associated with a user account that has the Required Permissions to fetch assets.

![Symantec Endpoint Protection Mobile.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Symantec%20Endpoint%20Protection%20Mobile.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Multi-Processing Workers** *(optional, default: 1)*  - Specify the number of workers to use when fetching entities. Increase this value to allow for multi-processing in an attempt to speed up fetch times. The maximum value is 20.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>