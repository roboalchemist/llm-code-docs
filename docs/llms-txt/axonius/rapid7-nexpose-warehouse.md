# Source: https://docs.axonius.com/docs/rapid7-nexpose-warehouse.md

# Rapid7 Nexpose Warehouse

Rapid7 Nexpose Warehouse fetches device information directly from an external data warehouse.

## Asset Types Fetched

* Devices, Aggregated Security Findings, Software, SaaS Applications

## Parameters

<Callout icon="📘" theme="info">
  **Note**

  This adapter connects directly to the Rapid7 Nexpose Warehouse PostgreSQL database. Ensure the credentials you are using have access to the database and to all the tables on it.
</Callout>

1. **PostgreSQL Server** *(required)* - The hostname of the Rapid7 Nexpose PostgreSQL server.
2. **Port** *(required, default: 5432)* - The port used for the connection.
3. **Database** *(required)* - The name of the database.
4. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
5. **Do not fetch devices with no MAC address and no hostname** - Select whether to exclude fetching devices without MAC address and without hostname.
   * If enabled, Axonius will only fetch devices having MAC address or hostname.
   * If disabled, Axonius will fetch devices even if those do not have MAC address and no hostname.
6. **Enable SSL** *(optional)* - Toggle on to enable SSL connection. You can upload custom certificates including Root Certificate File, Client Certificate File, or Client Private Key File.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="connection parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-CPZ21IPR.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use psycopg2** *(optional)* - Select whether to use Psycopq 2.
2. **Aggregated Security Findings severity value include list** *(optional)* - Enter one or more comma-separated Aggregated Security Finding severity values to include in the fetch.
3. **Parse Rapid7 tags as fields** *(optional)* - Select to parse Rapid7 tags as fields.
4. **Keep large raw fields** *(optional)* - Select to include large raw fields in the fetch.
5. **Exclude devices without IP, hostname and MAC address**     - Select this option to exclude devices with no MAC address, no hostname and no IP address from the fetch. If the devices have none of these fields it is not fetched.
6. **Exclude devices without last seen and hostname** - Select this option to exclude devices in which Last Seen and hostname information is unavailable.
7. **Assets to fetch** - By default Axonius fetches data about all asset types. Clear asset types that you don't want to fetch. Devices are always fetched and if no values are selected all assets are fetched.
8. **Fetch Solution Fix** - Toggle on to fetch the solution fix for the Aggregated Security Findings fetched.
9. **Fetch Remediation Date when available** - Toggle on to fetch the Remediation Date information for each Security Finding belonging to an asset when the date is available.
   * When **Fetch Remediation Date when available** is selected, the **Remediated Aggregated Security Findings comparison date** option appears. Select a date to limit how many days back the query for Aggregated Security Findings remediation checks.
   * When **Fetch Remediation Date when available** is selected, the **Remediated Aggregated Security Findings comparison days** option appears. Set the number of days in the past to check for remediated dates on Aggregated Security Findings.
10. **Enable complex query fetch** - Enable this option to have the adapter utilize complex queries to fetch data from the database. This reduces overall memory consumption of the adapter. The following settings become available when you enable this:
    1. **Only fetch Aggregated Security Findings seen on devices in the last X number of day(s)** - Enter a number of days. This setting enables the system to fetch only Aggregated Security Findings that were seen on devices by Rapid7 Nexpose Warehouse in the set number of days. This allows the system to pull a recent history of the devices' Security Findings rather than the entire system history every fetch. This option is only enabled when **Enable complex query fetch** is enabled.
    2. **Enable unique Aggregated Security Findings** - Select this to fetch each individual Security Finding separately with its own unique data, such as Proof, Key (a unique identifier), network protocol associated with this finding, and more.
       * When this setting is unselected (default), Aggregated Security Findings are grouped by their CVE identifier. This way, even if the same vulnerability (for example CVE-2023-12345) appears multiple times on a device, it it listed as a single finding.
       * Enabling this setting might substantially increase the number of vulnerability records fetched, which might increase fetch duration and storage requirements in Axonius.
    3. **Fetch Vuln Solution Fix** - Select this to fetch remediation solution information for each vulnerability.
    4. **Fetch Vuln Category Name** - Select this to fetch vulnerability category classifications from Rapid7. A single vulnerability can belong to multiple categories, and all applicable categories are fetched.
    5. **Fetch Vuln Reference** - Select this to fetch external reference URLs for each vulnerability.
    6. **Remove public. prefix from queries** - This setting controls how the adapter formats database table names when querying the Rapid7 Nexpose Warehouse PostgreSQL database. Tables in the default schema are typically referenced as `public.table_name` (for example: `public.dim_asset`, `public.fact_asset_vulnerability_instance`). When you enable this setting, The adapter removes the `public.` prefix from all queries (for example, `SELECT * FROM public.dim_asset -> SELECT * FROM dim_asset`). This is mostly useful when your Rapid7 Nexpose Warehouse database uses a non-standard schema configuration.
    7. **Parse vulnerabilities only from successful fetch** - Select this to only parse vulnerability assets if their fetch is successful. If the fetch partially or completely fails, only vulnerabilities from the last successful fetch are parsed.
    8. **Insert both CVE and Plugin as Security Findings** - Select this option to parse each CVE ID and plugin ID in the vulnerability as Security Findings.
    9. **Send email report of dropped assets** - Select this option to send an email containing a CSV file of all assets dropped due to size limitation (bigger that 16mb). For each asset, the CSV file will list its ID and the number of vulnerabilities it contains.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Troubleshooting

Make sure you perform monthly maintenance and tuning on your On-Premise Rapid7 Postgresql database as explained by Rapid7. This ensures optimzed Axonius fetch performance.

* [Rapid7 Configuring maximum performance in an enterprise environment](https://docs.rapid7.com/nexpose/configuring-maximum-performance-in-an-enterprise-environment/)
* [Rapid7 Planning for Capacity Requirements](https://docs.rapid7.com/nexpose/planning-for-capacity-requirements/).