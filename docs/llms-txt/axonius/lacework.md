# Source: https://docs.axonius.com/docs/lacework.md

# Lacework

Lacework provides cloud security automation for AWS, Azure, and GCP with a comprehensive view of risks across cloud workloads and containers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Vulnerabilities, SaaS Applications, Containers, Compute Images

## Parameters

1. **Lacework Domain** *(required)* - The hostname or IP address of the Lacework server that Axonius can communicate.

2. **Access Key ID** *(required)* - The Access Key ID. It is recommended to use a Lacwork Service User to generate the needed API key. The Service User’s role must be Admin or have read-only access to all API endpoints as detailed [here](https://docs.lacework.net/onboarding/access-control-overview?tab=serviceadmin#service-users).

3. **Secret Key** *(required)* - An API secret key. Refer to [Generate API Access Keys and Tokens](https://support.lacework.com/hc/en-us/articles/360011403853-API-Access-Keys-and-Tokens) for information on how to generate the secret key.

4. **Sub Account** - Enter a sub account name to fetch data from a defined sub account. The authorization token needs to have org admin permissions to do this.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Lacework.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Lacework.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

All advanced settings for this adapter are under the **Endpoints Config** section. All endpoints except for Inventory, Machine Details, and Images contain the same vulnerability fetching settings, detailed below.

### Endpoints Config

1. **Fetch Devices of sub type inventory from Inventory Endpoint** - Toggle on to fetch devices from the Inventory endpoint (`api/v2/Inventory/search`).
2. **Fetch Devices of sub type machines from Machines Endpoint** - Toggle on to fetch devices from the Machines endpoint (`api/v2/Machines/search`).
3. **Fetch Devices of sub type machines\_details from Machine Details Endpoint** - Toggle on to fetch devices from the Machine Details endpoint (`api/v2/MachineDetails/search`).
4. **Fetch Devices of sub type k8 from K8s Pods Endpoint** - Toggle on to fetch devices from the K8s Pods endpoint (`api/v2K/8sPods/search`).
5. **Fetch Devices Containers of sub type container from Containers Endpoint** - Toggle on to fetch device containers from the Containers endpoint (`api/v2/Containers/search`).
6. **Fetch Devices Containers of sub type agent from Agents Info Endpoint** - Toggle on to fetch device containers from the Agents Info endpoint (`api/v2/AgentsInfo/search`).
7. **Fetch ComputeImage from Images Endpoint** - Toggle on to fetch compute images from the Images endpoint (`api/v2/Entities/Images/search`).

#### Vulnerability Fetching Settings

1. **Require hostname** - Select this option to require hostname.

2. **Enrich X Endpoint with Vulnerabilities** - Toggle on to add vulnerabilities data to the devices fetched from the selected endpoint.

3. **Fetch vulnerability in actions in the last X days** *(optional, default: 1)* - Enter a number of days to fetch vulnerability data from. This refers to the number of days in which vulnerability scans were committed, not to the vulnerability's discovery date or update date.

4. **Fetch vulnerability Last Updated in X Days** *(optional, default: 7)* - Enter a number of days to fetch updated vulnerability data from. This is most recommended to avoid fetching old vulnerabilities.

5. **Comma Separated Vulnerability Severity Include List** *(optional)* - Enter the severities you want to fetch. The default severities are Critical, High, Medium, and Low. You can also add the Info severity, however, it may slow down the fetch significantly and bring irrelevant results.

6. **Comma Separated Status Include List** *(optional, default: Active)* - Enter the vulnerability statuses you want to fetch.

7. **Comma Separated Vulnerability Response Fields include list** *(optional)* - Enter the vulnerability reponse fields (information retrieved from the API) you want to fetch. The default fields are: `cveProps, mid, severity, status, vulnId`. It is recommended to fetch these fields, however, if the fetch time is abnormally long, you can remove them.

## APIs

Axonius uses the [ Lacework API v2](https://docs.lacework.net/api/v2/docs/).

## Supported From Version

Supported from version 4.4