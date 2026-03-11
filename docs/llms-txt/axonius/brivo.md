# Source: https://docs.axonius.com/docs/brivo.md

# Brivo

Brivo is a cloud-based access control solution that helps protect building, employees, visitors, customers, residents and data.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default api.brivo.com )* - The hostname or IP address of the Brivo server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. The API Key is found on the user account on the [developer portal](https://developer.brivo.com/login/login?r=https%3A%2F%2Fdeveloper.brivo.com%2Fapps%2Fmykeys\&h=91a514f981cf98d481c2005b7ad5e404).

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Client Secret** and **Client ID** -  A Client ID and Secret are obtained by creating an Application in the Brivo OnAir sandbox account provided when registering as a developer. The client should select the type of authentication as Password when they create  the application.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Brivo](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Brivo.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch badge events** *(required, default: true)* - Select whether to fetch badge security events.
2. **Fetch extended user data**  - Select this option to fetch  additional data for users, including: Custom Fields, Assigned Credentials, Suspended Status, Groups.
   Enabling this may have a slight negative impact on performance for large datasets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Brivo API](https://apidocs.brivo.com/)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version  | Supported | Notes |
| -------- | --------- | ----- |
| Brivo v1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7