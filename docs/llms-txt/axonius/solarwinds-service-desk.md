# Source: https://docs.axonius.com/docs/solarwinds-service-desk.md

# SolarWinds Service Desk (Samanage)

SolarWinds Service Desk (formerly Samanage) is a unified, cloud-based IT service desk and asset management platform.

<br />

### Asset Types Fetched

* Devices, Users, Software, SaaS Applications, Tickets

<br />

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

<br />

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address**  - The hostname or IP address of the SolarWinds Service Desk server.
2. **API Key** - An API Key associated with a user account that has permissions to fetch assets. For details, see [Token authentication for API integration](https://documentation.solarwinds.com/en/success_center/swsd/content/completeguidetoswsd/token-authentication-for-api-integration.htm).

<Image alt="SolarWinds Service Desk connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/SolarWindsServiceDesk_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy**  - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](https://docs.axonius.com/docs/adding-a-new-adapter-connection) .