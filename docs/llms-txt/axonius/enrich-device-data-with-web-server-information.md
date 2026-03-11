# Source: https://docs.axonius.com/docs/enrich-device-data-with-web-server-information.md

# Web Server Information - Enrich Asset Data

**Web Server Information - Enrich Asset Data** (Enrich Device Data with Web Server Information)  action enriches the web servers that are the results of the query  with information about the web server including the server type, its version and  operating system, the content management system (CMS) name and its version, the installed CMS plugins and versions and more.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

1. **Web server port** *(Default value: **443**)* - Specify the ports to use in order to fetch the web server information. You can specify more than one port in a comma-delimited list.
2. **Number of Parallel Connections** - specify the number of connections to be opened to control the performance of the scan. The default value for this field is **10**.
3. **Compute Node Name**  - The Axonius node to use when connecting to the specified host. For more details, see [Connecting Additional Axonius Nodes](/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

1. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
2. **Fetch data from SSL scanner** *(required, default: False)* - Check this option to fetch data from [Qualys SSL Labs](https://www.ssllabs.com/).
   * When this is enabled this  will enrich device data with SSL Labs data, that includes information about the server host, its endpoints and indications on exposure to known SSL vulnerabilities, such as Heartbleed and POODLE.
     * To enrich device with data from Qualys SSL Labs:
       * Host name is required. If the device data does not include a host name, one of the following can be used:
         * Device IP address, that must be a public IP address.
         * Domain, if fetched as part of the SSL Certificate data.
       * Port 443 must be opened for Axonius to use the SSL Labs API.
3. **Qualys SSL Labs API v4 registered email** *(optional)* - This field is available only when **Fetch data from SSL scanner** is enabled.  Enter a Qualys SSL Labs API v4 registered email. To register a valid email address via CLI, run the following command:

```
curl --location 'https://api.ssllabs.com/api/v4/register'  --header 'Content-Type: application/json' --data '{ "firstName":"John", "lastName":"Doe", "email":"john.doe@company.com", "organization":"Company"}'
```

<Callout icon="📘" theme="info">
  Note

  The **Qualys SSL Labs API v4 registered email** field is mandatory if you want to perform an SSL scan using Qualys.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).