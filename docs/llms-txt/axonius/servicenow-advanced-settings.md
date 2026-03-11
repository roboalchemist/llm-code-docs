# Source: https://docs.axonius.com/docs/servicenow-advanced-settings.md

# ServiceNow Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter or to a specific connection. Refer to [Advanced Configuration for Adapters](https://docs.axonius.com/docs/advanced-configuration-for-adapters).
</Callout>

You can use **Advanced Configuration** settings to fine-tune how the ServiceNow adapter fetches data.
These settings can be applied globally to all adapter connections, or customized for individual connections.

Per-connection customization is useful when you need multiple fetch cycles for the same data source, for example:

* A light, frequent fetch for quick updates.
* A less frequent, more resource-intensive fetch for deeper data collection.

***

## Accessing Advanced Configuration

* Navigate to the **Adapters** page → search for `ServiceNow` → click on the adapter tile.
* On the left menu, select **Advanced Configuration** under Advanced Settings.

***

## Advanced Configuration Parameters

At the top of the Advanced Configuration, you can choose asset types that are relevant to specific advanced configurations.

* From the dropdown, select one or more asset types.
* The relevant advanced configurations are displayed.
* Next to certain configurations, you can find a small info icon. Hover over the icon to see more information.
* The Advanced Configuration page is divided into sections, which can be collapsed to make it easier to navigate.

<br />

### Settings field descriptions

<Accordion title="Fetch Settings">
  1. **Fetch Assets** - Select this option to allow Axonius to fetch devices from ServiceNow.
  2. **Assets tables to fetch** - By default, Axonius fetches all tables of assets. To filter out tables of assets from the fetch, deselect one or more of the options in the table.
  3. **Assets sub-tables to fetch** - By default, Axonius fetches all sub-tables of assets. To filter out sub-tables of assets from the fetch, deselect one or more of the options in the table.
  4. **Table schema mapping** - This option helps you parse assets into categories by creating an array, where each row contains the fields listed below.\
     Click **+ Add Table** to create a new array (you can create multiple tables) or **x** to delete a table.
     * **Asset type** - From the dropdown, select a supported asset type.
     * **Table name** - Type a string representing the name of the table, for example: `u_cmdb_ci_computer`
     * **Query** *(optional)* - Enter a list of strings to be used as the `sysparm_filter` API parameter. See the [ServiceNow documentation on Query Parameters](https://developer.servicenow.com/dev.do#!/learn/learning-plans/xanadu/servicenow_application_developer/app_store_learnv2_rest_xanadu_more_about_query_parameters) for more information.
     * **Fields to fetch** *(optional)* - Enter fields to fetch from the corresponding table. If you leave this field empty, all fields will be fetched by default.
  5. **Table View Override** - Use this option if you need to fetch fields that are not available in the default view of the table. Click **+ Add Table**, then provde the **Table name** and the **View override** - the name of the view you want to fetch instead of the default view. Each table can only be specified once.
  6. **Fetch users** - Select this option to fetch all users in the system.
  7. **Fetch roles for users** - Select this option to fetch the roles used by each user.
  8. **Use existing user data during device fetching** - Select this option to add various user fields to the devices (for example: Owner, Assigned To, etc.) based on the associated Users Assets fields. The **Fetch users data** option will be ignored.
  9. **Fetch only parsed fields for users** - Enabled to fetch only parsed fields from ServiceNow.
     * If disabled (default setting), fetches all fields from ServiceNow, shows them all in “view advanced” section and parses only the fields required.
  10. **Custom User Schema** - Use these settings to add a JSON file to fetch information from one object to another. Refer to [Custom User Schema](https://docs.axonius.com/axonius-help-docs/docs/servicenow-adv-settings-custom-user-schema)
  11. **Additional user table names**  - Enter one or more ServiceNow table names separated by commas from which Axonius will fetch entries and parse them into users.  Table names should be of the format `cmdb_ci_my_linux_server`.

      * You can use this setting in 2 ways:
        1. A list of tables to fetch in addition to the built-in tables. In this case the format should be table\_name(, table\_name). When the table names are separated by commas.
        2. A list of tables with filters. In this case the format should be  (table\_name(:sysparm\_query)(;table\_na…)), where sysparm\_query is a ServiceNow query with ServiceNow operators as defined in [Operators available for filters and queries](https://www.servicenow.com/docs/bundle/xanadu-platform-user-interface/page/use/common-ui-elements/reference/r_OpAvailableFiltersQueries.html) and each table name together with a query (filter) is  separated by a semicolon. (Fields in brackets are optional parameters)
           * When supplied, the adapter will fetch data from all of the additional tables listed, make them into users, then proceed with fetching the default hardcoded subset of tables Axonius usually fetches from. The tables listed in this field take precedence over the default ServiceNow tables queried by Axonius, a Ci fetched from  these tables will now be totally ignored as redundant in the later “default” fetching process.

      <Callout icon="📘" theme="info">
        The settings here for filters on the table names listed in this field apply *exclusively* to the list of tables in this field. Other advanced settings that you make do not serve as filters to the table names listed in this field.

        For example:    if **Additional device table names**==`cmdb_ci_ip_switch:install_statusIN1;cmdb_ci_ip_router:install_statusIN1;` and **Install status number exclude list**==`2,3,4`, then all of the ServiceNow built in device tables will be fetched with **excluded of install\_status of 2,3,4** and the specific tables in **Additional device table names** will be an “inclusion” of install\_status of **1**.
      </Callout>
  12. **Fetch users data for devices** *(default: Enabled)* - Select this option to fetch user data and add relevant user fields to the devices (for example: Owner, Assigned To, etc.).
      * The **Users** table in ServiceNow is a large table. Therefore, if you are running Axonius on-premises, fetching this data requires more time, RAM, and CPU from the adapter's connections.
  13. **Fetch last user transaction from syslog\_transaction table** - Select this option to fetch and parse the latest transaction (from syslog\_transaction table) for each ServiceNow user, to the field “Last Transaction”.
  14. **Fetch VPN devices from 'cmdb\_ci\_vpn' table** *(default: Enabled)* - Select this option to fetch VPN devices from 'cmdb\_ci\_vpn' table.
  15. **Fetch only cmdb ci computer table** - Select this option to fetch only devices from the cmdb\_ci\_computer table. The adapter will not fetch any other device tables.
  16. **Do not fetch devices without IP address, MAC address and serial number** - Select this option to only collect information of devices if they have an IP address, MAC address, and serial number.
  17. **Exclude VMs tables** - Select this option to not collect device assets from tables in ServiceNow that are related to Virtual Machines.
  18. **Install status exclude list** *(optional)* - Specify a comma-separated list one or more install statuses to exclude from the fetched data. If supplied, this adapter will not fetch devices from ServiceNow if their install status is in the specified list. This field only accepts integers (such as 7, and not strings).
  19. **Install status include list** *(optional)* - Specify a comma-separated list of one or more install statuses to include in the fetched data. If supplied, this adapter will only fetch devices from ServiceNow if their install status is in the specified list. This field only accepts integers (such as 7, and not strings).
      * The values supplied in this field are applicable only if **Install status exclude list** is empty.
  20. **Operational status exclude list** *(optional)* - Specify a comma-separated list of one or more operational statuses to exclude from the fetched data. If supplied, this adapter will not fetch devices from ServiceNow if their operational status is in the specified list.
  21. **Operational status include list** *(optional)* - Specify a comma-separated list of one or more operational statuses to include in the fetched data. If supplied, this adapter will only fetch devices from ServiceNow if their operational status is in the specified list.

      * The values supplied in this field are applicable only if **Operational status exclude list** is empty.

      <Callout icon="📘" theme="info">
        In order for the above Install Status and Operational Status Include/exclude fields to work correctly, the Axonius ServiceNow user account must have access to the sys\_choice table.

        For the *Install Status* and *Operational Status* include/exclude fields to function correctly, the adapter must have read access to the `sys_choice` table.
      </Callout>
  22. **Populate device and applications upstream and downstream fields** - Select this option to populate the “upstream“ and “downstream“ fields for devices and applications.
  23. **Upstream / downstream fields: display as flat list** - Select to display the Upstream and Downstream field values for Devices as a flat list rather than a graph. The Relation Depth displayed in this format is greater - up to 10.
  24. **Fetch upstream related Application Services information** - Select this option to parse information from the Application Services table (cmdb\_ci\_service\_discovered) of any application service existing in a device upstream relations.
  25. **Fetch upstream related Application Services extended information** - Select whether to fetch information from the cmdb\_ci\_service\_auto table and additional fields from the cmdb\_ci\_service\_discovered table not fetched by the **Fetch upstream related Application Services information** parameter.
  26. **Fetch upstream related FCI details from 'u\_applications'** - Select this option to fetch information from u\_applications table and enrich devices with it.
  27. **Fetch upstream related Certificate information from 'cmdb\_ci\_certificate'** - Select this option to fetch the certificate information of device assets from ServiceNow.
  28. **Fetch upstream related Business Application** - Select whether to fetch the Business Application information of device assets from ServiceNow.
  29. **Fetch upstream related Application from 'cmdb\_ci\_appl' table**  - Select to fetch information from the 'cmdb\_ci\_appl' table about applications related to a device.
  30. **Fetch active compliance policy exceptions from 'sn\_compliance\_policy\_exception'** Select this option to link 'active' compliance policy exceptions as identified by ServiceNow Governance, Risk and Compliance (GRC) to the respective devices.
  31. **Fetch model information from 'cmdb\_model'** *(default: Enabled)* - Enable this setting If the 'model\_id' field value is a reference to the cmdb\_model table.
      * If enabled, this adapter will use the reference in the 'model\_id' field to fetch the device\_model and device\_manufacturer from the cmdb\_model table.
      * If disabled, this adapter will fetch only the value of the 'model\_id'.
  32. **Fetch active model lifecycle information from 'cmdb\_hardware\_model\_lifecycle'** - Select this option to fetch active model lifecycle information from the cmdb\_hardware\_model\_lifecycle table and parse it as a list object named “Model Lifecycle”.
  33. **Fetch NIC information from 'cmdb\_ci\_network\_adapter' table** *(default: Enabled)* - If enabled, this adapter will fetch network interface information from the cmdb\_ci\_network\_adapter table and from the matching cmdb\_ci\_ip\_address table.
  34. **Fetch only discovered NICs with IP information from 'cmdb\_ci\_network\_adapter' table** - Select whether to fetch network interface information from the cmdb\_ci\_network\_adapter table that has an IP address.
  35. **Fetch Platform Offering from ‘service\_offering' table** - Select to fetch information from the ‘service\_offering’ table and enrich the device with the service offer name if a direct reference exists between the device and the table. Check the *Fetch device relations* field to search for a relation between the service offering and the device and create a new structure for the device called “CMDB Service Offering” with the details of the service offering.
  36. **Fetch Software package information from 'cmdb\_sam\_sw\_install'/'cmdb\_software\_instance' table** - Select this option to fetch software package information from the ''cmdb\_sam\_sw\_install'/'cmdb\_software\_instance' table.
  37. **Fetch CI key-values(tags) information from cmdb\_key\_value table** - Select this option to fetch the table cmdb\_key\_value and  enrich each device that has matching key-value records in the cmdb\_key\_value table.
  38. **Fetch running processes information from cmdb\_running\_process table** - Select this option to fetch running processes information.
  39. **Fetch ALM information from alm\_asset table** *(default: true)* - By default Axonius fetches additional data for existing devices from alm\_asset table. Clear this option if you do not want to fetch ALM information.
  40. **Fetch Device contract information from 'ast\_contract' for the following parent contract numbers** - Specify a comma-separated list of parent contract numbers. This option requires the '[Contract Management](https://docs.servicenow.com/bundle/paris-it-asset-management/page/product/contract-management/reference/r_TablesInstalledWContractMgmt.html)' plugin.
      * If supplied, this adapter will fetch contract information (number, short description) for the specified list, and will add the contract information to the devices associated with the contract (**Contracts** complex field), based on the relationship defined in ServiceNow.
      * If not supplied, this adapter will not fetch contract information.
  41. **Fetch Device divestiture contract information from 'ast\_contract' for the following parent contract numbers**  - Specify a comma-separated list of parent contract numbers. This option requires the '[Contract Management](https://docs.servicenow.com/bundle/paris-it-asset-management/page/product/contract-management/reference/r_TablesInstalledWContractMgmt.html)' plugin.
      * If supplied, this adapter will fetch divestiture contract information (number, short description) for the specified list, and will add the divestiture contract information to the devices associated with the contract (**Divestiture Contracts** complex field), based on the relationship defined in ServiceNow.
      * If not supplied, for this adapter will not fetch divestiture contract information.
  42. **Additional device table names** *(optional)*  - Enter one or more ServiceNow table names separated by commas from which Axonius will fetch entries and parse them into devices.  Table names should be of the format 'cmdb\_ci\_my\_linux\_server'
      You can use this setting in 2 ways:
      1. A list of tables to fetch in addition to the built-in tables. In this case the format should be table\_name(, table\_name). When the table names are separated by commas.
      2. A list of tables with filters. In this case the format should be  (table\_name(:sysparm\_query)(;table\_na…)), when sysparm\_query is a ServiceNow query with ServiceNow operators as defined in [Operators available for filters and queries](https://docs.servicenow.com/en-US/bundle/tokyo-platform-user-interface/page/use/common-ui-elements/reference/r_OpAvailableFiltersQueries.html) and each table name together with a query (filter) is  separated by a semicolon. (Fields in brackets are optional parameters)
      * When supplied, this adapter will fetch data from all of the additional tables listed, make them into devices, then proceed with fetching the default hard coded subset of tables Axonius usually fetches from. The tables listed in this field take precedence over the default ServiceNow tables queried by Axonius, a Ci fetched from  these tables will now be totally ignored as redundant in the later “default” fetching process.
      * When not supplied, this adapter will not fetch data from any additional tables.
  43. **ServiceNow Fields are true** - Enter one or more parameters, separated by commas, and filter only devices where these parameters are true. If the device does not have the field, the device is fetched.
  44. **Fetch PC attributtes** - Fetch device PC Attributes from the 'u\_pc\_attributes' table, where `u_type=Attributes`
  45. **Fetch Device CI Exceptions** - Select this option to fetch records from the u\_configuration\_item\_exception table and enrich the device with related exception information such as exception name, reason, related software etc.
  46. **Fetch Portfolio fields from u\_ip\_portfolio\_mapping table** - Select this option to fetch Portfolio fields in the u\_ip\_portfolio\_mapping table.
  47. **Fetch common cost center details** - Select this option to fetch information from the cmn\_cost\_center table.
  48. **Fetch Table Hierarchy** - Select this option to create the table hierarchy of a device.
  49. **Enrich CMDB CI Associations** - Select this option to enrich each device with the services that the devices are associated with.
  50. **Fetch Databases As Assets** - Enter a (comma-separated) list of tables. Axonius fetches the records from those table and parses them as database entities.
  51. **Fetch Business Application as Asset** - Toggle on to fetch Business Application as an asset.
      * **Business Application tables list** - Enter a list of tables to fetch Business Application from (default is 'cmdb\_ci\_business\_app').
  52. **Do not fetch devices or users marked as excluded** - Select this option to fetch assets that have the u\_exclude\_from\_discovery field set as True in ServiceNow.
      * If disabled, this adapter will fetch all assets from ServiceNow.
      <Callout icon="📘" theme="info">
        As a prerequisite, u\_exclude\_from\_discovery field must be created and defined in ServiceNow as a Boolean field.
      </Callout>
  53. **Include assets if they have the following field with the following value(s)** - Enter one or more ServiceNow tables with a specified value, in the format table\_name:field\_name:(filtered\_value,filtered\_value). Table Name is optional. Separate entries with semi-colons. The table name must be exactly one of the values listed here: `cmdb_ci_computer,cmdb_ci_vm,cmdb_ci_vm_instance,cmdb_ci_printer,cmdb_ci_netgear,u_cmdb_ci_computer_atm,cmdb_ci_comm,cmdb_ci_cluster,cmdb_ci_cluster_vip,cmdb_ci_facility_hardware,cmdb_ci_msd,u_cmdb_ci_dinar_infrastructure_object,cmdb_ci_vpn.`

  * If a field is supplied, this adapter will fetch devices which have a ServiceNow table that contains a field with the value defined.
    **Examples**:\
    `fieldname:value`

    `fieldname.fieldname` (use this if the fieldname is a reference and not a regular string. In this case you can only filter by .walking, you need to enter the name of the internal field of the referred table.)

  `fieldname:value1,value2`

  `tablename:fieldname:value1,value2`

  <Callout icon="❗️" theme="error">
    The filters here overwrite any other filters you set for tables. If you choose this setting, you cannot choose other predefined ServiceNow advanced settings table filters as well.
  </Callout>

  54. **Exclude assets if they have the following field with the following value(s)** - Enter one or more ServiceNow tables with a specified value, in the format table\_name:field\_name:filtered\_value,filtered\_value. Separate entries with semi-colons. The following table names are supported: `cmdb_ci_computer,cmdb_ci_vm,cmdb_ci_vm_instance,cmdb_ci_printer,cmdb_ci_netgear,u_cmdb_ci_computer_atm,cmdb_ci_comm,cmdb_ci_cluster,cmdb_ci_cluster_vip,cmdb_ci_facility_hardware,cmdb_ci_msd,u_cmdb_ci_dinar_infrastructure_object,cmdb_ci_vpn.`

      * If a field is supplied, this adapter will exclude devices from the adapter fetch which have a ServiceNow table that contains a field with the value defined.

        <Callout icon="❗️" theme="error">
          The filters here overwrite any other filters you set for tables. If you choose this setting, you cannot choose other predefined ServiceNow advanced settings table filters as well.
        </Callout>
  55. **Fetch properties settings** - Select this option to fetch general ServiceNow settings.
      <Callout icon="📘" theme="info">
        To fetch settings using this advanced configuration, ensure that there are no ACL configurations blocking the records from the sys\_properties table in ServiceNow.
      </Callout>
  56. **Fetch password policy settings** - Select this option to fetch password policy related settings.
  57. **Fetch groups** - Select this option to fetch ServiceNow groups as assets.
  58. **Fetch roles** - Select this option to fetch ServiceNow roles as assets.
  59. **Fetch users' group membership** - Select this option to fetch ServiceNow users group membership.
  60. **Fetch active extensions from 'v\_plugins'** - Select this option to fetch active extensions.
  61. **Fetch entities from 'cmdb\_ci\_ip\_network' as Networks assets** - Select this option to fetch entities from 'cmdb\_ci\_ip\_network' as Networks assets.
  62. **Fetch Activities From X days Ago** - Enter the number of days to retrieve recent activities information.
  63. **Ignore SaaS Applications Repository and parse all applications** - Select this option to fetch all applications even if they are not in the Axonius SaaS Applications Repository.
  64. **Use the software sys\_id as the SaaS Application ID** - This setting is useful when a software name matches multiple entries in the SaaS Applications Repository. Enable it to maintain ID uniqueness when the fetch returns duplicate records. For example, when this is enabled, software names such as "Figma" and "Helios Figma" are treated as two different applications. WHen this is disabled, "Figma" and "Helios Figma" are treated as one application in case "Helios Figma" not in the repository.
  65. **Custom Assets schema for Devices, Business Applications, Databases** - Use these settings to add a JSON file to fetch information from one object to another. Refer to [Custom Asset Schema](https://docs.axonius.com/axonius-help-docs/docs/servicenow-adv-settings-custom-asset-schema)
  66. **Fetch Assets Relations** - Select this option to fetch assets relations from the cmdb\_rel\_ci.
  67. **Fetch dynamic dropdown values** - When selected, field values for the dynamic dropdown lists in the related Enforcement Actions are fetched and populated into the lists.
  68. **Fetch from the following Read Replica category (Must be supported on instance)** - Fetch from the specified Read Replica.
</Accordion>

<Accordion title="Parsing Settings">
  1. **Save only active users** - Select this option to save only users with **active** field set to `true`.
  2. **Users Email  include list** - Enter a comma-separated list of email strings. Only users whose email addresses contain any of these strings will be fetched. The strings don’t need to be full email addresses, partial matches are allowed because the filter uses a **Contains** search.
  3. **Resolve Username based only on name field** - Select this option so that the Username field in Axonius will display the value of the name field in the ServiceNow record.
  4. **JSON fields to show in basic view** - You can configure fields that generally appear in JSON to appear in Basic view. Refer to [Showing JSON Fields in Basic View](/docs/servicenow-showing-adv-settings-json-fields-in-basic-view)
  5. **Parse IP addresses from device raw "ip\_address" field** - Select this option to parse IP addresses from the device raw "ip\_address" field.
  6. **Exclude disposed and decommissioned devices** - Select this option to not collect information on devices if their status in ServiceNow is 'Disposed' or 'Decommissioned'.
  7. **Ignore retired devices that have not been seen by the source in the last X hours** *(default: 0)* - Enter 1 or more hours to ignore retired devices that have not been seen by the source. A value of 0 means to fetch all devices.
  8. **Use 'cmdb\_ci' table instead of 'alm\_asset' table for install status and location** - Select this option to collect the **location** and **Install Status** directly from the record instead of  from the **'alm\_asset'** table.
  9. **Save only virtual devices** - Select this option to save only devices with **virtual** or **u\_is\_virtual** fields set to `true`.
  10. **Parse operational status** - Select this option to parse the operational status from the '**operational\_status**' field.
  11. **Populate device and applications upstream and downstream fields** - Select this option to populate the device and applications upstream and downstream fields, which are used for the asset graph.
  12. **Upstream / downstream fields: display as flat list** - Select to display the Upstream and Downstream field values for Devices as a flat list rather than a graph. The Relation Depth displayed in this format is greater - up to 10.
  13. **Populate the Device Company field with z\_support\_group\_manager\_company** - Select this field to populate the Device Company field in the adapter basic view with the “z\_support\_group\_manager\_company” data.
  14. **Populate the Device Company field with z\_assigned\_to\_company** - Select this field to populate the Device Company field in the adapter basic view with the “z\_sassigned\_to\_company” data.
  15. **Populate the Device Owner based on assigned\_to parsed field** - Select this option to populate the Axonius owner aggregated field based on the ServiceNow "assigned to" field instead of the "opened by" field.
  16. **When company does not exist, use owner as Company** - If the "company" field value in a device doesn't exist, it will use the device owner as the company value.
  17. **Device hostname parsing preferences** - This section includes custom hostname parsing options for Devices, including fallback options when the hostname is missing from the raw data. Toggle on **Enable custom hostname parsing** to reveal the following options:

      a. **Remove domain suffix from hostname field** - Select this option to remove the domain suffix from the ServiceNow Hostname field.

      b. **Select hostname fallback option** - Select a fallback option in case hostname is missing:

      * **Default fallback options - use alias or fqdn**
      * **Use asset\_tag raw device field as hostname fallback** - Select this option to take the hostname value from the asset\_tag ServiceNow field value (instead of from the name).
      * **Use ci field as name and hostname when they are missing** - Select this option to use the ci field as the name and hostname when they are missing.
      * **Use asset name as hostname fallback**

      c. **Select hostname parsing option** - Select how to parse the device hostname:

      * **Default parsing order**
      * **Use dns\_domain device raw field as hostname** - Select this option to to take the hostname value from the dns\_domain ServiceNow field value (instead of from the name).
      * **Use asset name as hostname**
      * **Use referenced ci field (cmdb\_ci) as name and hostname** - Select this option to use the referenced ci field (cmdb\_ci) as the name and hostname.\*\*
      * **Custom hostname source preference order** - When selected, a **Hostname source preference order** is revealed. Here you can select the order of raw fields to use for the device hostname. The system will use the first available field in the order you define. The default order is \`host\_name, fqdn, u\_fqdn. You can also click **Add fallback hostname raw field** to create a custom hostname raw field. Click X next to each row to remove it from the order.
  18. **Use "asset" raw device field as Asset Name** - Use the value of the device's "asset" raw field as the value for Asset Name. This setting applies only to devices.
  19. **RAM from source in GB**  - Select this option to display the RAM data fetched from ServiceNow in GB memory units instead of MB memory units.
  20. **Parse only IPv4 for devices (exclude IPv6)** - Select whether to only parse IP addresses in IPv4 format for devices. By default Axonius parses IP addresses both in IPv4 format and IPv6 format.
  21. **Extract software version and name from Software Name** - Select this option to extract the correct software name and version when the field fetched by ServiceNow does not contain this correctly.
  22. **Use 'last\_discovered' device field exclusively as 'last\_seen'** - Select this option to compute the 'last\_seen' field from the 'last\_discovered' raw field, if this field does not exist 'last\_seen' will not exist.
      * When disabled, this adapter will use `max('last_discovered', ‘sys_updated_on’)` to compute last\_seen.
  23. **Use sys\_id as device ID (Might cause device duplication)** - Select this option to only use the devices' sys\_id field for the adapter device ID (recommended if the device name might change). If you enable this after the first fetch has already been done, it might cause duplicate devices.
  24. **Use ServiceNow Domain in Asset ID (Might cause device duplication)** - Select this option to only use the ServiceNow Domain in the Asset ID. If you enable this after the first fetch has already been done, it might cause duplicate devices.
  25. **Do not use 'Last Seen' for the following tables** -
      * Enter one or more ServiceNow table names separated by commas that will not be filtered by  'Last Seen'. This capability overrides the Table Schema Mapping query
      * To avoid calculating 'Last Seen' for all devices, enter `*` in the field.
  26. **Always populate serial number** - When selected, **Device Manufacturer Serial** is parsed even if it contains exclusion keywords, such as "VMware Virtual Platform".
  27. **Exclude Devices OS list** - Specify an Operating System name to not fetch devices which run this Operating System.
  28. **Append device model to OS string if the following strings are in the model field** - Models containing one of the strings entered in this field (separated by commas) are appended to the OS string.
  29. **Do not add serial number metadata** *(optional)* - Select this option so that metadata such as "VMWare-", "VMWare Inc.", "VMWare Virtual Platform" and any other device model data will not be added to ServiceNow serial numbers.
  30. **Use "VM Object ID" as "AWS Cloud ID"** - Use this setting to use the VM Object ID to identify AWS Cloud IDs. When you select this option, if the value of the `object_id` confirms to the following rules:
      * getting `vm_object_id` from `object_id`,
      * if `vm_object_id` starts from ‘i-’ and length > 10\
        Then Axonius uses the value of the `object_id` in the  `device.cloud_id`  field.
  31. **Devices: Unset Downstream and Upstream fields if not populated in fetch results** *(optional, default: disabled)* - Select this option to automatically clear existing field values in the **Downstream** and **Upstream** complex object fields on devices when no new values are returned during a ServiceNow fetch. This is useful for optimizing 'delta fetches' (double fetching).
  32. **Enrich devices with SecOps Vulnerable Items** - Select this option to enrich the devices with open VITs from the sn\_vul\_vulnerable\_item table.
  33. **Enter additional date fields to consider as 'last seen'** - Enter values (comma separated) from fields to calculate the 'Device last seen field'.
  34. **Specify Class Names (Tables) to parse as Network Device assets** - Enter device class names to locate for fetching devices as Network Device assets.
  35. **JSON fields to show in basic view (Devices, Business Applications, Databases)** - You can configure fields that generally appear in JSON to appear in Basic view. Refer to [Showing JSON Fields in Basic View](https://docs.axonius.com/axonius-help-docs/docs/showing-json-fields-in-basic-view)
  36. **Custom Raw fields mapping** - Enter a JSON file to duplicate raw fields to different raw fields. This will enable the adapter to treat the asset like a classic ServiceNow asset (rather than a proprietary one).
  37. **Clear Network Interfaces if MAC addresses are not found** - Select this to remove previous network interfaces from the device's MAC Address field if no MAC addresses are found (the mac\_address field in the 'cmdb\_ci\_network\_adapter' table is empty).
</Accordion>

<Accordion title="Advanced Configuration">
  1. **Fetch "cmdb\_software\_product\_model" table for Various Software enrichment** - Select this option to fetch and process data from the `cmdb_software_product_model` table in ServiceNow. This is only supported in adapters that enable Device Software Enrichment. Currently, only [FlexNet Manager Suite Cloud](/docs/flexnet-manager-suite-cloud) enables this enrichment type.

     <Callout icon="📘" theme="info">
       You can enrich the Axonius Software table with ServiceNow CMDB data from the CMDB table. For more information, see [Enriching Software Assets with ServiceNow CMDB Data](https://docs.axonius.com/docs/enriching-software-assets-with-servicenow-cmdb-data).
     </Callout>

  2. **Use the following field when filtering last updated** *(optional)* - Enter a ServiceNow field name to be used as the field that Axonius filters by for the following configurations *Fetch devices updated in ServiceNow in the last X hours*  and\
     *Fetch users updated in ServiceNow in the last X hours*
     * If a field is set, this adapter will fetch devices or users which have the set field that was updated in the time defined.
     * When not supplied, this adapter will fetch devices or users which were last updated according to the ‘sys\_updated\_on’ ServiceNow field.

  3. **Entries fetched per page** *(required, default: 100)* - Specify the maximum number of entries for this adapter to fetch per page when connecting to the ServiceNow server.
     * The supplied value lets you control the performance of all the connections for this adapter. To reduce the number of requests sent to ServiceNow, but to avoid impact on overall performance, you can reduce the **Number of requests to perform in parallel** value and increase the **Entries fetched per page** value.

  4. **Date Format** - Generally, ServiceNow automatically identifies the date format. In some cases, the identification is ambiguous. You can set a specific date format for timestamps in ServiceNow. From the dropdown, select either: **Automatically Identify**, **DD/MM/YYYY** or **MM/DD/YYYY**. The default is **Automatically Identify**.

  5. **Custom Parsing** - Select this option to define how to parse specific fields from the raw data fetched. See [Adapter Custom Parsing](https://docs.axonius.com/docs/adapter-custom-parsing) for more information.

  6. **Number of requests to perform in parallel** *(default: 10)* - Enter the number of requests to perform in parallel.

  7. **Enable real-time asset updates (Supported events: New or Updated Users, New Tickets)** - Select this option to update assets in real-time with New or Updated Users and New Tickets events.

  8. **Fetch EC Action ticket updates** *(optional, default: enabled)* - Select this option to configure the adapter to fetch updates on tickets created by Axonius users. The updated ticket information is displayed in the **Tickets** table showing information on all tickets in the system (**Assets> Tickets**) or on Tickets of a specific asset (in the **Asset Profile** of the relevant asset).
</Accordion>