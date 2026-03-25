# Source: https://docs.axonius.com/docs/manageengine-service-desk-plus-leg.md

# ManageEngine Service Desk Plus (SDP) -

ManageEngine Service Desk Plus (SDP) is an IT help desk and customer support system.

<Callout icon="❗️" theme="error">
  Note

  This adapter was updated and replaced with the newer [ManageEngine ServiceDesk Plus](/docs/manageengine-service-desk-plus)
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ManageEngine SDP server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Port** *(required, default: 8080)* - The port used for the connection.

3. **API Key** *(required)* - An API Key associated with a user account that has  permissions to fetch assets.
   To generate an API Key, see [Generate an API Key](/docs/manageengine-service-desk-plus#generate-api-key).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="ManageEngine_SDP" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngine_SDP.png" />

## APIs

Axonius uses the [ManageEngine ServiceDesk Plus REST API](https://help.servicedeskplus.com/api/rest-api.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Generate an API Key

<Callout icon="📘" theme="info">
  Note

  * Only an administrator can generate the authentication key for technicians with login permission.

  * If a login for the technician is disabled, then the API key is deleted.
</Callout>

**To generate an API Key**

1. From the User section, click **Admin** `>` **Technicians** icon.
2. If you want to generate the API key for an existing technician, click  ![Edit\_icon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Edit_icon.png)
   (**Edit**) on the same row as the desired technician. If you want to generate the API key for a new technician, click **Add New Technician**, enter the technician details and provide the login permission.  The **Generate API Key** window appears.

<Image alt="Generate API Key.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Generate%20API%20Key.png" />

3. In **Key expires on**, click the **Never expires** option to generate a permanent API Key.
4. Click **Generate**. If a key is already generated for the technician, click **Regenerate**.
5. Copy the API Key and paste it into the Axonius **API Key** parameter.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7