# Source: https://docs.axonius.com/docs/exabeam.md

# Exabeam

Exabeam is a cloud-based platform combining SIEM, threat detection, investigation, and response (TDIR) and XDR capabilities. Integrate Exabeam with the Axonius Cybersecurity Asset Management Platform.

**Related Enforcement Actions**

* [**Exabeam - Update Context Table**](/docs/exabeam-update-context-table)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Domain Name or IP Address** *(required)* - The hostname or IP address of the Exabeam server.

2. **Login Method** *(required, default: Username and Password)* - Select from the dropdown whether to login via **Username and Password** or **Cluster Authentication Token**.

3. **User Name** and **Password** *(required)* - When the **Username and Password** (default) login method is selected from the **Login Method** dropdown, specify the credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Cluster Authentication Token**   - When the **Cluster Authentication Token** login method is selected from the **Login Method** dropdown, specify the cluster authentication token. An Admin must create the token. For more information, see [Generating a Cluster Authentication Token](/docs/exabeam#generating-a-cluster-authentication-token).

5. **Access Token**   - When the **Access Token** login method is selected from the **Login Method** dropdown, specify an **API Key** and an **API Secret**. Refer to [Exabeam documentation](https://docs.exabeam.com/en/apis/all/api-get-started-guide/api-keys/create-an-api-key.html).

6. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

10. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Exabeam1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Exabeam1.png" />

## APIs

Axonius uses the [Exabeam API Documentation](https://developers.exabeam.com/exabeam).

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions and an 'advanced\_analyst' role to fetch assets.

## Generating a Cluster Authentication Token

To generate a token:

1. From Exabeam, select **Settings > Core > Admin Operations > Cluster Authentication Token**. The Cluster Authorization Token page is displayed.
2. Click the ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Plus_Exabeam.png) symbol. The Setup Token dialog is displayed.
3. Enter the **Token Name** and **Expiry Date** in the relevant fields.

<Callout icon="📘" theme="info">
  Note

  Token names can contain only letters, numbers, and spaces.
</Callout>

4. In the Permission Level section, select the **Default Roles** for the token.
5. Click **Add Token**. Use the generated file to allow your APIs to authenticate by token. Ensure that your API uses 'ExaAuthToken' in its requests. For curl clients, the request structure resembles the following:

```
curl -H "ExaAuthToken:<generated_token>" https://<external_host>:<api_port>/<api_request_path>
```

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                   | Supported | Notes |
| ----------------------------------------- | --------- | ----- |
| Advanced Analytics version i52 or greater | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5