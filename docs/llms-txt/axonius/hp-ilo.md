# Source: https://docs.axonius.com/docs/hp-ilo.md

# HP Integrated Lights-Out (iLO)

HP Integrated Lights-Out (iLO) is server management software that enables the configuration, monitoring, and updating of HPE servers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Hostname, IP or Subnet** *(required)* - Enter the  hostname,  IP addresses or an IP Address with a Subnet Mask blocks for the HP Integrated Lights-Out (iLO) server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![HPiLO](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPiLO.png)

## APIs

Axonius uses the [HPE iLO 5 RESTful API](https://servermanagementportal.ext.hpe.com/docs/redfishservices/ilos/ilo5/).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may also work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version  | Supported | Notes |
| -------- | --------- | ----- |
| HP iLO 5 | Yes       |       |