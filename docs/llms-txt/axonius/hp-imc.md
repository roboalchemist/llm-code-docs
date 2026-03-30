# Source: https://docs.axonius.com/docs/hp-imc.md

# HPE Intelligent Management Center (IMC)

HPE Intelligent Management Center (IMC) is a networking solution that delivers management across campus core and data center networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **HPE IMC Domain** *(required)* - The hostname or IP address of the HPE IMC server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![HPE Intelligent Management Center.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPE%20Intelligent%20Management%20Center.png)

## APIs

Axonius uses the [HPE IMC Extended API](https://support.hpe.com/hpesc/public/docDisplay?docId=emr_na-c03382045).

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.
The specified user must be a member of the default administrator group, or a group with administrator rights and with the **RESTful Web Services Call** option selected.
![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(862\).png)

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| HPE IMC v5.1 or later | Yes       |       |