# Source: https://docs.axonius.com/docs/splunk.md

# Splunk

Splunk captures, indexes, and correlates real-time data in a searchable repository.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Aggregated Security Findings, Software, Business Applications, SaaS Applications, Tickets

## Parameters

1. **Host Name** *(required)* - The hostname of the Splunk search head.
   To use Splunk Cloud, follow these steps:
   1. Ensure that the Axonius Instance Public IP address is whitelisted in Splunk Admin Config Service. To add the Public IP address of the Axonius Instance to the IP Allow List in Splunk Cloud, follow these steps:
      **Settings** > **Server Settings** > **IP Allow List** > **Search Head API Access**
      * For a single address (not a subnet), enter the address appended with a /32.
        Example: xxx.xxx.xxx.xxx/32
        For more information, see  [Configure IP allow lists for Splunk Cloud Platform](https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ConfigureIPAllowList).
   2. Ensure that the user name has permission to query 'index' and '\_internal'.
   3. Enter the host name in the following format: `customerName.splunkcloud.com`

<Callout icon="📘" theme="info">
  Note

  Make sure that the `customerName` does not contain HTTP or HTTPS.
</Callout>

2. **Port** *(required)* - Specify an API port for the host. TCP/8089 is the typical default for both Splunk and Splunk Cloud. For more details, see  [Splunk Docs - Securing Splunk Enterprise](https://docs.splunk.com/Documentation/Splunk/8.0.3/Security/SecureSplunkonyournetwork). Open a ticket with Splunk to ensure port 8089 is open for your Splunk deployment.
3. **Protocol** *(required, default: HTTPS)* - Select either HTTP or HTTPS protocol when using the specific adapter connection. Splunk Cloud can only use HTTPS protocol.
4. **User Name** and **Password** *(optional)* - The user name and password for an account that has read access to the API. The user name must have read access to \_internal index.
   * To create a new user with read permissions, follow the  [tutorial in the official Splunk documentation](https://docs.splunk.com/Documentation/Splunk/7.3.0/Security/ConfigureuserswithSplunkWeb). Splunk Cloud users should follow the steps detailed in  [Accessing the Splunk Cloud Platform REST API](https://docs.splunk.com/Documentation/Splunk/8.2.4/RESTTUT/RESTandCloud) to access the API.

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

5. **API Token** *(optional)* - API token can be used instead of user name and password. The token must have read access to \_internal index.    If **User Name** and **Password** are not supplied, **API Token** is required. For more information, refer to  [Use Splunk Web to create authentication tokens](https://docs.splunk.com/Documentation/Splunk/9.0.1/Security/CreateAuthTokens#Use_Splunk_Web_to_create_authentication_tokens).

<Callout icon="📘" theme="info">
  Note

  For the following Splunk Macro fields:

  * Titles cannot contain the following keywords: DHCP, Cisco, VPN, Windows Login, Splunk agent version, Nexpose, and Landesk.

  * Macro titles should follow the format: `|application_namespace:macro_name`.

  * The | (pipe) prefix is only needed for macros that begin with a generating command such as search, tstats, pivot, etc.

  * 'application\_name' is the name of the application if the macro is outside of the default Splunk search.

  * 'macro\_name is the name of the existing macro in Splunk that you want to use.

  * Examples:

  `|foreignApp1:Windows-axonius`<br />
  `|macrostartingwithsearch`<br />
  `simplemacro`

  * If the macro string begins with 'search ', the associated search query is used exactly as entered. This means you can enter Search Processing Language (SPL) queries directly, without needing to add extra logic.
</Callout>

6. **SplunkLib Version** - Select the version of the Splunk library to use.
7. **Splunk Search Macros List** *(optional)* - Specify a comma-separated list of Splunk search macros names. For details on Splunk search macros, see  [Splunk Knowledge Manager Manual - Define search macros in Settings](https://docs.splunk.com/Documentation/Splunk/8.0.1/Knowledge/Definesearchmacros).
   * Axonius will run the Splunk search macros names and will consider the results as if those were received from a CSV file. This means the search macros must include at least one column of required data as specified in the [CSV adapter - Which fields will be imported with a devices file?](/docs/csv#which-fields-can-be-populated-for-each-file-import-type).
   * If supplied, Axonius will run the specified search macros and will fetch devices from the results for this adapter.

     * To execute macros that are defined outside of the default 'Search' Splunk application, specify the application namespace name before any applicable macro name followed by a colon.
   * If not supplied,  this adapter will not include any search macros results in the fetched data.
8. **Splunk Installed Software Search Macros List** *(optional)* - Specify a comma-separated list of Splunk search macro names that provide installed software information. For details on Splunk search macros, see  [Splunk Knowledge Manager Manual - Define search macros in Settings](https://docs.splunk.com/Documentation/Splunk/8.0.1/Knowledge/Definesearchmacros).
   * Axonius will run the Splunk search macros names and will consider the results as if those were received from a CSV file with installed software information. This means the search macros must include at least one column of required data as specified in the  [Which fields will be imported with a software applications file?](/docs/csv#which-fields-can-be-populated-for-each-file-import-type).
   * If supplied, Axonius will run the specified search macros and will fetch installed software from the results and associate them to device entities for this adapter.

     * To execute macros that are defined outside of the default 'Search' Splunk application, specify the application namespace name before any applicable macro name followed by a colon.
     * “if the results include the following columns, then Installed Security Patch data will be added to devices where available:
       `hostname` (required), `security_patch_name` (required), `state` (optional), `installed_on` (optional), `patch_id` (optional)
   * If not supplied, this adapter will not include any search macros results in the fetched data.
9. **Splunk Firewall Search Macros List** *(optional)* - Specify a comma-separated list of Splunk search macro names that provide firewall information.
10. **Splunk User Search Macros List** *(optional)* - Enter a list of macros. When populated this field is used to to query the macros that are defined within it to create User objects that will be parsed into Axonius. The macro should return at least one of the following fields to be used as a unique identifier: 'id', 'username', 'mail', 'name', 'userprincipalname'. Other fields that are not used as the user id will be added dynamically, i.e. any field the macro fetches should be available in Axonius.
11. **Splunk Ticket Search Macros List** *(optional)* - Specify a comma-separated list of Splunk search macro names that provide ticket information.
12. **Splunk SaaS Application Search Macros List** *(optional)* *(only for accounts with Axonius SaaS Applications)* - To execute a macro defined outside of the default "Search" Splunk application, specify the application namespace name before any applicable macro name with colon appended.
13. **Splunk Business Application Search Macros List** *(optional)* - Specify a comma-separated list of Splunk search macro names that provide business application information.
14. **Splunk Application Keys Search Macros List** - Specify a comma-separated list of Splunk search macro names that provide application key information.
15. **Splunk Containers Search Macros List** - Specify a comma-separated list of Splunk search macro names that provide container information.
16. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Splunk.png" />

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Number of days to fetch** *(required, default: 30)* - Specify the query size by number of days Axonius will request to fetch data from all the connections of this adapter.
2. **Maximum amount of records per search** *(required, default: 100000)* - Specify the maximum number of records Axonius should fetch from all the connections of this adapter.
3. **Windows login hours to fetch** *(required, default: 3)* - Specify the Windows login data query size by hours Axonius will request to fetch from all the connections of this adapter.
4. **Fetch devices from the splunk-nexpose plugin** - Select this option to fetch the devices data from splunk-nexpose plugin.
5. **Fetch devices from Cisco** *(required, default: true)* - By default Axonius fetches the devices data from Cisco data in Splunk. Clear this option to not fetch the devices data from Cisco data in Splunk.
6. **Fetch DHCP data** *(required, default: true)* - Select this option to fetch DCHP data. This option is only relevant for customers who have the `axonius_dhcp` Splunk macro and the `index=winevents sourcetype=DhcpSrvLog` Splunk search in their system.
7. **Fetch Winlogon data** *(required, default: true)* - By default Axonius fetches Winlogon data. Clear this option to not fetch Winlogon data.
8. **Fetch VPN data** *(required, default: true)* - By default Axonius fetches VPN data. Clear this option to not fetch VPN data.
9. **Fetch Splunk agent version** - Select this option to fetch information about the Splunk agent version.
10. **Fetch custom agents** - Select this option to fetch agent versions using the **Splunk Search Macros List**[connection parameter](/docs/splunk#parameters). For this parameter, enter a macro including the ‘name’ and ‘version’ fields. The results fetched from Splunk will be parsed under the aggregated **Agent Versions** field.
11. **Override default agent search timeframe to be one minute** - Select whether to limit the agent search timeframe for Splunk devices  to the most recent snapshot.
12. **Set time zone for last seen (+/- UTC)** - Select a Splunk time zone to adjust the value last seen. If default '+0' is selected and last seen is a time in the future, the value will be skipped. If '+0' is not selected and last seen is a time in the future, the value will be used as last seen with the defined time difference.
13. **Query to parse browsed applications from web activity logs** - Enter a query to parse browsed applications from web activity logs.
14. Custom Parsing refer to [Custom Parsing](/docs/adapter-custom-parsing)

<Callout icon="📘" theme="info">
  Note

  For details about general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* Splunk: [Splunk Enterprise REST API](https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTsearch#search.2Fjobs)
* Splunk Cloud: [Splunk Cloud Platform REST API](https://docs.splunk.com/Documentation/Splunk/9.4.0/RESTTUT/RESTandCloud)

## Permissions

The value supplied in [API Token](#parameters) must have the user role and read access to \_internal index    in order to fetch assets.

The credentials in use should have permission to use any specified macro.

For further information refer to [Create authentication tokens](https://docs.splunk.com/Documentation/Splunk/9.0.1/Security/CreateAuthTokens).

## **Related Enforcement Actions**

* [Splunk - Create and Update Assets](/docs/splunk-create-and-update-assets)