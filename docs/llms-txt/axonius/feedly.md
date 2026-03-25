# Source: https://docs.axonius.com/docs/feedly.md

# Feedly

Feedly is a news aggregator application for various web browsers and mobile devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Feedly server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Token** *(required)* - Enterprise Access token. Refer to <Anchor label="Authorization | Feedly API" target="_blank" href="https://developers.feedly.com/reference/authorization">Authorization | Feedly API</Anchor> for information on this token and how to generate it.

3. **Stream ID** *(required)* - Enter *GET /v3/streams/:streamId/ids* or *GET /v3/streams/ids?streamId=:streamId*. Remember to URL-encode *streamid*. Learn more about getting the Stream ID at <Anchor label="TI Integration | Feedly API" target="_blank" href="https://developers.feedly.com/reference/building-your-first-ti-integration">TI Integration | Feedly API</Anchor>.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Feedly" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Feedly.png" className="border" />

## APIs

Axonius uses the <Anchor label="Feedly API" target="_blank" href="https://developers.feedly.com/reference/introduction">Feedly API</Anchor>.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 8080**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V3      | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.0.