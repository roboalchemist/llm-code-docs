# Source: https://docs.axonius.com/docs/azure-advanced-settings.md

# Azure - Advanced Settings

## Accessing Advanced Configuration

1. Navigate to **Adapters** and search for `Azure` then click the adapter tile
2. In the left menu, select **Advanced Configuration** under **Advanced Settings**

## Advanced Configuration

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch update deployments**  - Select whether to fetch software update deployments from Microsoft Azure.
2. **List of tags to parse as fields** *(optional)* - Specify a comma-separated list of tag keys to be parsed as asset fields. Each tag is a key-value pair that is part of the **Adapter Tags** complex field.
   1. If supplied, all connections for this adapter will parse any of the listed tags that are associated with the fetched device as:
      1. Values of the **Adapter Tags** field.
      2. Designated field with the name of the tag key and the value of the tag value
   2. If not supplied, all connections for this adapter will only parse all tags as values of the **Adapter Tags** field.
3. **Parse all tags from asset as fields** - All tags from the asset will be parsed as fields in the Axonius asset.
4. **Fetch Security Center sub-assessments for devices** *(optional)* - Select to fetch security assessments (such as Qualys vulnerabilities) for devices, where available. This option requires the Security Center to be active in the subscription.
5. **Fetch Azure Arc-Enabled machine extensions** - Select this option to fetch machines enabled by Azure Arc.
6. **Consider last seen only for connected Arc-Enabled machines** - Select this option to use the **Last Seen** field as a reference timestamp only for Arc-enabled machines with the status *Connected*. For machines with any other status, the **Last Status Change** field will be used as a reference timestamp, reflecting the last time the device was disconnected.
7. **Fetch Advisor Recommendations for entities** - Select this option to fetch security recommendation from Azure Advisor. When enabled, an 'Advisor Recommendations' field is added to all fetched assets.
8. **Enrich Advisor Recommendations with assessment information** - Select to enrich the Advisor recommendations in virtual machines with additional data. You can only select this option when **Fetch Advisor Recommendations for entities** is enabled.
9. **Add backup protection information from recovery services into VMs** - Select this option to enrich Virtual Machines devices with their backup config information, if it exists.
10. **Fetch Azure Security alerts** - Select to fetch security alerts from Azure Security Center service as devices. Make sure you add permissions for `SecurityEvents.Read.All` to fetch Azure Security alerts.
11. **Fetch Defender Pricing** - Select to fetch the current pricing tier for all Defender plans under a subscription.
12. **Use Cloud ID as manufacturer serial number** - Select to use the unique ID for tracking support data as a manufacturer serial number.
13. **Use Asset Name as Hostname and Hostname as Asset Name** - Select to swap the information in the Asset Name with the Hostname field.
14. **Use Asset Name as Hostname and Hostname as Asset Name (15 chars)** - Select this option to switch between the asset name value and the hostname value if the hostname has 15 characters.
15. **Consider Azure Managed disks as encrypted** - Select to consider Azure managed disks as SSE encrypted.
16. **Use Instance view Computer Name as Hostname** - Select to swap the information from **os\_profile** `>` **computer\_name** to **instance\_view** `>` **computer\_name**.
17. **Fetch Azure Firewall Rules and Policies** *(optional)* - Select to fetch firewall rules and web application firewall policies configured in the asset's subnets.
18. **Do not save Subscription Tags to Adapter Tags for entity types** - From the drop-down, select the Azure entity types for which you don't want to have the Subscription Tags included in the Adapter Tags values.
19. **Fetch Activity Logs for Resource Groups from last X days** - Enrich resource groups with activity logs from the last X days.
20. **Azure services to fetch as assets** *(optional)* - Select one or more services from the list to fetch as Axonius assets. Some of the services require additional permissions to fetch - see [Additional Permissions](/docs/microsoft-azure#additional-permissions).
    The following options are available:

<Accordion title="Azure services to fetch as assets" icon="fa-info-circle">
  * Analysis Services
  * Apache Spark pools
  * API Connections
  * API Management
  * App Service plans
  * Application Gateway
  * Application Gateway HTTP Listener
  * Application Insights
  * Automation Accounts
  * Availability Sets
  * Availability Tests
  * Azure Arc-Enabled Machines
  * Azure Databricks
  * Azure Workbooks
  * Action Groups
  * B2C Tenants
  * Blob Containers
  * Certificates From Key Vaults. *Refer to[Fetching Certificates from Key Vaults](/docs/microsoft-azure#fetching-certificates-from-key-vaults)*
  * Communication Services
  * Connections
  * Container App
  * Container Groups
  * Container Registries
  * Cosmos DB Accounts
  * Data Factory
  * Database for PostgreSQL - Flexible Server
  * Database for PostgreSQL - Single Server
  * Database for MySQL - Flexible Server
  * Database for MySQL - Single Server
  * Database for MariaDB
  * Dedicated SQL pools
  * Disks
  * DNS Records
  * DNS Zones
  * Event Hubs
  * Event Hubs Namespaces
  * File Shares
  * Form recognizers
  * Front Door and CDN profiles
  * Front Door WAF policies
  * Firewalls
  * Function Apps
  * Key Vaults
  * Keys from Key Vaults - adds the keys from key vaults and displays them as the asset "secrets". *See the permissions required[here](/docs/microsoft-azure#fetching-keys-from-key-vaults).*
  * Recovery Service Vaults
  * Kubernetes Agent Pools
  * Kubernetes Clusters
  * Load Balancing Rules
  * Load Balancers
  * Local Network Gateways
  * Log Analytics MAC Addresses
  * Log Analytics Workspaces
  * Logic Apps
  * Machine Learning Service Registries
  * Machine Learning Service Workspaces
  * Machine Learning Web Services
  * Managed Identities
  * Management Groups -\* See the permissions required [here](/docs/microsoft-azure#fetching-management-groups).\*
  * NetApp Accounts
  * NetApp Volumes
  * Network Interfaces
  * Network Security Groups
  * Network Security Rules
  * Network Watchers
  * Policy Set Definitions
  * Private Endpoints
  * Public IP Addresses
  * Queues
  * Redis Caches
  * Relays
  * Resource Groups
  * Route Tables
  * Secrets From Key Vaults
  * Service Bus Namespaces
  * Sentinel Incidents
  * Shared dashboards
  * SignalR
  * Solutions
  * SQL Databases
  * SQL Databases Inaccessible By Server (fetches inaccessible databases as the asset Database with the Azure Entity Type SqlDB.)
  * SQL Managed Instances
  * SQL Servers
  * Subscription
  * Storage Accounts
  * Storage Accounts - Access Keys / Kerberos Keys
  * Synapse Workspaces
  * System Topics
  * Tables
  * Tenants
  * Virtual Machines - Selected by default, clear if you do not want to fetch.
  * Virtual Machine Scale Sets (fetches  Virtual Machine Scale Sets from Azure, and saves them as Compute Services.)
  * Virtual Network Gateways
  * Virtual Networks
  * WCF Relays
  * Web Apps
  * Web Application Firewall Policies
</Accordion>

18. **Filter Policy Definitions and Policy Set Definitions by Policy Assignment IDs** *(optional)* - Enter a list of policy assignment IDs to filter results by. Only Policy Set Definitions and Policy Definitions with resources that are compliant and/or non-compliant with the specified policy assignment ID(s) will be fetched.
19. **Fetch VM sizes** *(optional, default: false)* - Select this to fetch VM sizes information. Note that if you enable this option, the fetch time might increase significantly.
20. **Check device existence in the following log analytics query pack names** *(optional)* - Add the names of the query packs that you want to run on your devices to determine if the devices contain relevant logs. Please note that this feature does not return log data, just indications if devices were found that meet the queries' criteria.
    1. All the queries must include the '\_ResourceId' column to allow for correlating the log/query with the Device (Virtual Machine).
    2. For information on creating Query Packs and saving Queries inside the query packs, see [Log Analytics Query Packs](https://techcommunity.microsoft.com/t5/azure-observability-blog/log-analytics-query-packs/ba-p/2314721).
21. **Get cost data per subscription for the last X days** - In order to get the billing data per service, select Subscriptions in the  'Azure services to fetch as assets' field and enter a number between 1 and 365 in this field.

    <Callout icon="📘" theme="info">
      **Notes**

      * To enable fetching cost data from Azure,, you need to fetch Resource Groups and Subscriptions.
      * The billing data is parsed under the Cloud Billing field, under the Accounts/Tenants asset type.
    </Callout>
22. **Fetch Azure Update Manager report** - Select this option to fetch Azure Update Manager report to enrich Managed Devices with update and patch data, such as published date, patch ID, name, version, KB ID, reboot requirements, OS type, classification, severity, and more.
23. **Enrich Policy Metadata** - This advanced setting will only take effect if **Policy definition** is selected on **Services to Fetch**. This setting can significantly increase the fetch time. By enabling it Policies definition will be enriched with description and requirements fields
24. **Fetch Heartbeat Data from LogAnalytics** - Select this option to fetch Heartbeat data from an instance in Azure Log Analytics.