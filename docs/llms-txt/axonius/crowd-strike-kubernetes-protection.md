# Source: https://docs.axonius.com/docs/crowd-strike-kubernetes-protection.md

# CrowdStrike Kubernetes Protection

CrowdStrike Kubernetes Protection provides cloud-native application security, including breach prevention, workload protection, and cloud security posture management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Compute Services
* Containers

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the CrowdStrike Kubernetes Protection server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(optional)* - Credentials provided by CrowdStrike Kubernetes Protection for authentication to the API for read access.  To learn how to create the Client ID and Client Secret, see [creating credentials](/docs/crowdstrike-falcon#creating-credentials-latest-api).

3. **Verify SSL** - Select this option to verify the SSL certificate of the server against the CA database inside of Axonius.  To learn more, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to this proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CrowdStrikeKubernetesProtection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CrowdStrikeKubernetesProtection.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

Under Advanced Settings, you can toggle the following options on/off to fetch different entities from different endpoints. The options are:

1. **Fetch Containers from Containers Endpoint** - When this setting is enabled, the following settings may be configured:
   * **Fetch Containers Last Seen in X Days** *(default: 15)* - Specify the number of past days you want to fetch containers from.
   * **Additional FQL** - Enter an additional FQL query to filter the containers fetch.
2. **Fetch ComputeServices of sub type compute\_services\_clusters from Cluster Endpoint**
3. **Fetch ComputeServices of sub type compute\_services\_cloud\_clusters from Cloud Endpoint**
4. **Fetch ComputeServices of sub type compute\_services\_nodes from Nodes Endpoint**
5. **Fetch ComputeServices of sub type compute\_services\_pods from PODs Endpoint**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the CrowdStrike Kubernetes Protection API reference.

To access the API  from your CrowdStrike console:

1. From the left hand menu, select **Support and resources**.
2. Select **Documentation**.

<Image align="center" alt="CSDocumentation.png" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-39EOB6DY.png" />

4. Select **CrowdStrike API** and then **CrowdStrike OAuth2-Based APIs**.

<Image align="center" alt="CSAuth2" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-94BP36Q4.png" />

6. Select the Swagger link suitable for the tenant you are using.
7. In the Swagger page, scroll down to **kubernetes-protection**.

<Image align="center" alt="CSKubernetesProtection" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-PGLGGKL0.png" />

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following port:

* **TCP port 443**

## Required Permissions

The values supplied in [Client ID](#parameters) and [Client Secret](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                   | Supported | Notes |
| ------------------------- | --------- | ----- |
| kubernetes-protection: v1 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.8