# Source: https://docs.axonius.com/docs/elastic-fleet.md

# Elastic Fleet

Elastic Fleet is a management component that offers centralized control over Elastic Agents, policies, and integrations for data collection and protection.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Kibana Serverless API](https://www.elastic.co/docs/api/doc/serverless/operation/operation-get-fleet-agents).

### Permissions

**Fleet-Specific Privileges**:

* `fleet-agents-read`: Required for GET `/api/fleet/agents` endpoint
* `fleet-agent-policies-read`: For accessing agent policy information
* `fleet-enrollment-api-keys-read`: For retrieving enrollment tokens

#### Supported From Version

Supported from Axonius version 7.0.10

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Elastic Fleet server.
2. **Authentication Type** - Select the Authentication Type, either **API Key** or **Basic**.

<Tabs>
  <Tab title="API Key">
    **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.
  </Tab>

  <Tab title="Basic">
    **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.
  </Tab>
</Tabs>

<Image alt="ElasticFleet.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ElasticFleet.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

### Related Enforcement Actions

[Elastic Fleet - Update Tags](https://docs.axonius.com/axonius-help-docs/docs/elastic-fleet-update-tags)