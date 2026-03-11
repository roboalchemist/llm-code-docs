# Source: https://docs.axonius.com/docs/prisma-cloud.md

# Palo Alto Networks Prisma Cloud

Palo Alto Networks Prisma Cloud is a native cloud security platform that provides visibility, threat prevention, compliance assurance, and data protection across multi-cloud environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Roles
* Groups
* Compute Services
* Application Services
* Networks, Load Balancers
* Databases
* Containers
* Object Storage
* Network Services
* File Systems
* Accounts/Tenants
* Serverless Functions
* Disks
* Compute Images
* Secrets
* Network/Firewall Rules
* Alerts/Incidents

## Parameters

1. **Prisma Cloud Domain** *(required)* - The URL for the **Prisma Cloud** domain.
2. **Access key ID** and **Secret key** *(required)* - The credentials for the **Access key ID** and **Secret key** that have the required permissions to fetch assets.
3. **Verify SSL**  - Select to verify the SSL certificate offered by the value supplied in **Prisma Cloud Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Prisma Cloud Domain**.
5. **Use Config Search API V2** - Select this option to run a fetch to get devices from API V2.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection)..

![Palo Alto Networks Prisma Cloud.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Palo%20Alto%20Networks%20Prisma%20Cloud.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch deleted devices** - Select this option to  fetch also 'deleted' devices.
2. **Fetch external resource finding** - Select to fetch users with external resources.
3. **Fetch only enabled users** - Select to fetch only active users.
4. **Fetch Users** *(required, default: true)* - When cleared, won't fetch information about Users.
5. **Fetch security groups** *(required, default: true)* - When cleared, won't fetch information from security groups.
6. **Fetch alerts from the last X days** *(optional, default: 0)* - Select how many days of alerts to fetch into devices.
7. **Resource types allow list** - Enter a comma-separated list of resource types to be fetched. The resource types list should be in capital letters. (ALL CAPS). The value should match the field `Resource Type` from the raw data. Note that in order to migrate from API V1 to API V2, you must also update your allow list.
8. **Use heuristic search** - Select this option to add the `heuristicSearch: true` parameter to the request.
9. **With resource JSON** - By default, Axonius includes resource JSON. Clear this option to not include resource JSON.
10. **Fetch from cloud accounts** *(optional)* - Enter a comma-separated list of account names to fetch from.
11. **Fetch from cloud types** - Select this option to fetch from cloud types only. When enabled the adapter will fetch cloud\_resources from AWS and Azure.
12. **Fetch CVE vulnerabilities** - Select this to enrich your fetched assets with CVE vulnerability data. Note that non-CVE vulnerabilities are not included in this enrichment.
13. **Fetch installed software package information** - Select this option to fetch the installed software package information, this includes the software name and version.
14. **Custom asset fetch rules** - Toggle on to be able to enter Prisma Cloud types to fetch data as the specified asset type, instead of as devices:
    * **Resource types to fetch as Compute Service assets** - Enter resource types to fetch as Compute Service assets and not as devices.
    * **Resource types to fetch as Network Service assets** - Enter resource types to fetch as Network Service assets and not as devices.
    * **Resource types to fetch as Secret assets** - Enter resource types to fetch as Secret assets and not as devices.
    * **Resource types to fetch as Account assets** - Enter resource types to fetch as Account assets and not as devices.
    * **Resource types to fetch as Load Balancer assets** - Enter resource types to fetch as Load Balancer assets and not as devices.
    * **Resource types to fetch as Database assets** - Enter resource types to fetch as Database assets and not as devices.
    * **Resource types to fetch as Network assets** - Enter resource types to fetch as Network assets and not as devices.
    * **Resource types to fetch as Security Role assets** - Enter resource types to fetch as Security Role assets and not as devices.
    * **Resource types to fetch as Group assets** - Enter resource types to fetch as Group assets and not as devices.
    * **Resource types to fetch as File System assets** - Enter resource types to fetch as File System assets and not as devices.
    * **Resource types to fetch as Network Devices assets** - Enter resource types to fetch as Network Devices assets and not as devices.
    * **Resource types to fetch as Application Service assets** - Enter resource types to fetch as Application Service assets and not as devices.
    * **Resource types to fetch as Compute Image assets** - Enter resource types to fetch as Compute Image assets and not as devices.
    * **Resource types to fetch as Container assets** - Enter resource types to fetch as Container assets and not as devices.
    * **Resource types to fetch as Object Storage assets** - Enter resource types to fetch as Object Storage assets and not as devices.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Prisma Cloud APIs](https://docs.prismacloud.io/en/classic/cspm-admin-guide/get-started-with-prisma-cloud/access-the-prisma-cloud-api).