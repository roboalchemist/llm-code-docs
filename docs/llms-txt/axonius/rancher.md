# Source: https://docs.axonius.com/docs/rancher.md

# Rancher

Rancher is an open-source multi-cluster orchestration platform that enables operations teams to deploy, manage, and secure enterprise Kubernetes.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Rancher server that  Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password**   - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. If you use API Key to connect, then these parameters are not required.

3. **API Key** -  An API Key associated with a user account that has permissions to fetch assets.  You can either connect the adapter using the Username and password or use an API Key.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Rancher](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rancher.png)

## Required Ports

* HTTPS (443)

## APIs

Axonius uses the [Rancher API](https://rancher.com/docs/rancher/v2.x/en/api/).

## Required Permissions

The value supplied in [User Name](#parameters) or API Key must have local admin credentials.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| Rancher API V3 | Yes       |       |