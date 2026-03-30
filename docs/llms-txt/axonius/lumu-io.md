# Source: https://docs.axonius.com/docs/lumu-io.md

# Lumu

Lumu is a cybersecurity platform that provides real time network monitoring and threat detection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Alerts/Incidents

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Lumu server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  The company's API key is found in the Defender menu of the Lumu Portal and is self-managed by company administrators.
</Callout>

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Lumu](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Lumu.png)

## APIs

Axonius uses the Lumu Defender API as well as the following APIs:

* Retrieve users - /api/administration/users
* Retrieve incidents - /api/incidents/all
* Retrieve incident details - /api/incidents/`{incident_uuid}`/details
* Retrieve labels - /api/administration/labels

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.31.0