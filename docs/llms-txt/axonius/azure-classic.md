# Source: https://docs.axonius.com/docs/azure-classic.md

# Azure Classic VMs

Microsoft Azure is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through a global network of Microsoft-managed data centers. This adapter fetches information for classic VMs (deprecated by Microsoft).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Azure Client ID** *(required)* - An Azure Client ID, copy this from the app registrations.

2. **Azure Client Secret** *(required)* - An Azure Client Secret copy this from the app registrations.

3. **Azure Tenant ID** *(required)* - An Azure Tenant ID copy this from the app registrations.

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. **Certificate Private Key File (.pem)** *(required, default: empty)* - A classic Cloud Services private key. Generate an X509 certificate as detailed in [Generating and Uploading the X509 Certificate](/docs/azure-classic#generating-and-uploading-the-x509-certificate).

8. **Client Certificate File (.cer)** *(required)* - A Classic Cloud Services certificate. Generate an X509 certificate as detailed in [Generating and Uploading the X509 Certificate](/docs/azure-classic#generating-and-uploading-the-x509-certificate).

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="AzureClassic.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AzureClassic.png" className="border" />

## APIs

Axonius uses the [Azure REST API](https://docs.microsoft.com/en-us/rest/api/azure/)

## Required Permissions

Refer to [Creating an application in the Microsoft Azure Portal](/docs/microsoft-azure#/creating-an-application-in-the-microsoft-azure-portal) to create an application in Azure Portal and define permissions.

### Generating and Uploading the X509 Certificate

Refer to [Certificates Overview for Azure Cloud Services](https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-certs-create) (classic) for detailed information.
For each subscription that Axonius will monitor perform the following:

1. Go to Azure Portal.
2. Enter Subscriptions (search and enter).
3. Enter your subscription.
4. Enter Management Certificates.
5. Upload your `.cer` certificate public key file.

### Generating the Client Credentials

1. Fill in Axonius details in the App registrations screen; the Application IDs are generated.
2. Copy these to a safe place, and then enter in the Axonius Configuration page.

<Image alt="image-20211121-102525.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-20211121-102525.png" />

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                  | Supported | Notes |
| ---------------------------------------- | --------- | ----- |
| Azure Classic VM (build from 2014-05-01) | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5