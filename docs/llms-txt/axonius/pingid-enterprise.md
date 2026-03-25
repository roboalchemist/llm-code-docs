# Source: https://docs.axonius.com/docs/pingid-enterprise.md

# PingID Enterprise

PingID Enterprise is a cloud-based multi-factor authentication (MFA) platform that supports enterprise solutions for software applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PingID Enterprise server that Axonius can communicate with via the [Required Ports](#required-ports). The domain must be the same as the `idp_url` provided in the Client Properties File (see below).

2. **Client Properties File** *(required)* - Click **Upload File** to upload the file generated for this API client.  The file contains several account-specific settings, including values that you need to use when creating a PingID API request message.
   To download the Client Properties File:
   1. Log into the **PingOne administration console**.
   2. From the main menu, select **Setup** `>` **PingID Configuration**.
   3. In the **Client Integration** section, under **Integrate With PingFederate and Other Clients**, click the download link. You will be prompted to save the file in a local folder.
      For a step-by-step guide on how to use the Client Properties File, see [this section in the PingID API](https://apidocs.pingidentity.com/pingid-api/guide/pingid-api/pid_c_PingIDapiOverview#How-to-Use-the-PingID-API).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PingID Enterprise connection parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ZGXJBBW4.png)

## APIs

Axonius uses the [PingID API](https://apidocs.pingidentity.com/pingid-api/guide/pingid-api).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

To download the account properties file, you must have a PingID account **administrator** permission.

## Supported From Version

Supported from Axonius version 6.1