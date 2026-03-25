# Source: https://docs.axonius.com/docs/paloalto-xsoar.md

# Palo Alto Networks Cortex XSOAR

Cortex XSOAR is a security orchestration, automation, and response platform that integrates and automates threat detection and incident response.

**Related Enforcement Actions**
[Palo Alto Cortex XSOAR - Create Incident](/docs/paloalto-xsoar-create-incident)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Alerts/Incidents

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Palo Alto Networks Cortex XSOAR server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Version** - Select between v6 and v8.

3. **Standard API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For information on how to generate the API Key and API Key ID, see [Get started with Cortex XSOAR 8 APIs](https://cortex-panw.stoplight.io/docs/cortex-xsoar-8/kjn2q21a7yrbm-get-started-with-cortex-xsoar-8-ap-is).

4. **API Key ID** *(optional)* - Your unique token used to authenticate the API Key.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-K388SDWK.png)

## APIs

Axonius uses the [Cortex XSOAR 8 API](https://cortex-panw.stoplight.io/docs/cortex-xsoar-8/wsqd67wlbojbu-cortex-xsoar-8-overview). However, you can also choose to use version 6 in the [connection parameters](/docs/paloalto-xsoar#parameters).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 8       | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1