# Source: https://docs.axonius.com/docs/hpe-san.md

# HPE SAN

HPE storage area networking (SAN) provides storage solutions for performance, scalability, and manageability.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the HPE SAN server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings). The API highly recommends the usage of the CA certificate, as referred here:[cURL as the REST API Client](https://infosight.hpe.com/InfoSight/media/cms/active/public/pubs_REST_API_Reference_NOS_52x.whz//htr1449782645359.html).  Use any web browser to export the array CA certificate” and then add it to the Axonius system.

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![HPESAN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPESAN.png)

## APIs

Axonius uses the [Nimble REST API](https://infosight.hpe.com/InfoSight/media/cms/active/public/pubs_REST_API_Reference_NOS_52x.whz//htr1449782645093.html).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                 | Supported | Notes |
| ----------------------- | --------- | ----- |
| Nimble REST API 5.2.1.0 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8