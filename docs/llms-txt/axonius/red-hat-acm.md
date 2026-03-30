# Source: https://docs.axonius.com/docs/red-hat-acm.md

# Red Hat Advanced Cluster Management for Kubernetes

Red Hat Advanced Cluster Management for Kubernetes provides visibility and control over clusters and applications from a single console.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Compute Services

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Red Hat Advanced Cluster Management for Kubernetes server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Token** *(required)* - An API Token associated with a user account that has permissions to fetch assets. For information on how to configure an API Token, see [here](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_security_for_kubernetes/4.3/html/configuring/configure-api-token#create-api-token_configure-api-token).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![red hat acm connection parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-4HN8PK3J.png)

## APIs

Axonius uses the [Red Hat Advanced Cluster Management for Kubernetes](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_security_for_kubernetes/4.3/html/configuring/configure-api-token) API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version     | Supported | Notes |
| ----------- | --------- | ----- |
| Version 4.3 | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1