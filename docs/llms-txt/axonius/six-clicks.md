# Source: https://docs.axonius.com/docs/six-clicks.md

# 6clicks

6clicks is a governance, risk, and compliance platform that offers automated risk assessment and management solutions.

### Asset Types Fetched

* Business Applications

<Callout icon="📘" theme="info">
  Note

  While 6clicks assets map to Axonius Business Applications, devices are not directly linked to 6clicks. To create the desired Business Application context within Axonius, you can build relationships by either:

  * Defining a custom field for Axonius Device assets referencing Business Applications.

  * Using [Axonius Custom Relationships](/docs/managing-custom-relationships#creating-a-custom-relationship) to establish links between Devices and Business Applications.
</Callout>

## Before You Begin

### APIs

Axonius uses the [6clicks Developer API](https://api-au.6clicks.io/swagger/index.html).

### Permissions

To access the necessary endpoints, the API key must be associated with a user account that has the following permissions:

* Read Tests via `GET /controls-api/1.0/tests`
* Post Test Results via `POST /controls-api/1.0/tests/{testKey}/results`

These permissions ensure that the API key can retrieve asset data and interact with the necessary components within 6clicks.

#### Supported From Version

Supported from Axonius version 7.0.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api-au.6clicks.io`)* - The hostname or IP address of the 6clicks server.
2. **API Key**  - An API Key associated with a user account that has the [Required Permissions](/docs/six-clicks#permissions) to fetch assets.

<Image alt="6clicks_connection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-OOEJOJF7.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

### Related Enforcement Actions

[6clicks - Report Test Result](/docs/six-clicks-report-test-result)