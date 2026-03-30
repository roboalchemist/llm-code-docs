# Source: https://docs.axonius.com/docs/workday-adaptive-planning.md

# Workday Adaptive Planning

Workday Adaptive Planning is a cloud-based planning and budgeting platform that helps organizations manage financial, workforce, and operational planning, providing data-driven insights for decision-making.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Workday Adaptive Planning server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Workday Adaptive Planning](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Workday%20Adaptive%20Planning.png)

## APIs

Axonius uses the [Workday Adaptive Planning API](https://doc.workday.com/adaptive-planning/en-us/integration/managing-data-integration/api-documentation/understanding-the-adaptive-planning-rest-api/api-methods/brk1623709249507.html?toc=1.3.1.3.0).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [User Name](#parameters) must have exportData permissions in order to fetch assets. For more information, see [Permissions and Data Access Control](https://doc.workday.com/adaptive-planning/en-us/integration/managing-data-integration/api-documentation/understanding-the-adaptive-planning-rest-api/tgm1623708513156.html?toc=1.3.1.1#:~:text=Permissions%20and%20Data%20Access%20Control).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v39     | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1.33.0