# Source: https://docs.axonius.com/docs/configuring-data-aggregation-settings.md

# Configuring Data Aggregation Settings

**To configure Data Aggregation settings:**

1. From the top right corner of the Axonius platform, click the **System Settings** icon (![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png)). The **System Settings** page opens.
2. In the left-side categories and subcategories pane, expand **Data** and select **Data Aggregation**.

<Image align="center" border={true} width="40% " src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/Data_Aggregation_Menu.png" className="border" />

<Callout icon="📘" theme="info">
  Note

  Aggregation settings do not impact correlation settings.
</Callout>

3. The following parameters are available for configuration:

* **Maximum adapters to execute asynchronously** *(required, default: 20)* - Define the number of adapters that  - as part of the discovery cycle - will be executed to fetch asset information in parallel.
* **Socket read-timeout in seconds** *(required, default: 5 seconds)* - Define the number of seconds to wait for any initial or existing connection response before reporting a connection timeout.
* **Convert all hostnames to uppercase** *(default: false)*  - Enable this option so that starting from the next data fetch, Axonius converts all fetched hostnames to uppercase. Otherwise, Axonius leaves fetched hostnames in the format received from each adapter connection.
* **Convert all asset names to uppercase** *(default: false)* - Enable this option so that starting from the next data fetch, Axonius converts all fetched asset names to uppercase. Otherwise, Axonius leaves fetched asset names in the format received from each adapter connection.
* **Set "Short Hostname" as uppercase-hostname with no domain** *(default: false)* - Some adapters set a field called short hostname on devices. Enable this setting to transform the short username to uppercase with a node domain on Axonius.
* **Convert Preferred Hostname to lowercase** *(default: false)* - Enable this option to convert the value of the preferred hostname on Axonius to lowercase.
* **Convert Preferred Hostname to uppercase** *(default: false)* - Enable this option to convert the value of the preferred hostname on Axonius to uppercase.
* **Convert Preferred Hostname (FQDN) to lowercase** *(default: false)* - Enable this option to  convert the value of the preferred hostname FQDN to lowercase on Axonius.
* **Set asset name as hostname, if hostname does not exist** *(default: false)* - Use this option to set the **Host Name** field in Axonius with the **Asset Name** field value, if no hostname was fetched for the asset. It is recommended to enable this setting.
  * If enabled, if no hostname has been fetched for an asset, the **Host Name** field is set with the **Asset Name** field value for that asset.
  * If disabled, if no hostname has been fetched for an asset, the **Host Name** field remains empty for that asset.
* **Set hostname as asset name, if asset name does not exist** *(default: false)*  - Enable this option to fill the Asset Name field in Axonius with the value of the Host Name field, if no asset name was fetched for the asset.  It is recommended to enable this setting.
* **Calculate "Equals" values list every X hours** *(required, default: 6)* - Some fields support the equals operators for dynamic lists/values. Set the frequency to refresh this list. The default value is 6 hours.
* **Convert preferred** Settings:
  * **Convert preferred asset name to** *(default: no conversion)* - Select an option for converting the case of the value of the preferred asset name in Axonius.
  * **Convert preferred domain to** *(default: no conversion)* - Select an option for converting the case of the value of the preferred domain in Axonius.
  * **Convert preferred device model to** *(default: no conversion)* - Select an option for converting the case of the value of the preferred device model in Axonius.
  * **Convert preferred device manufacturer to** *(default: no conversion)* - Select an option for converting the case of the value of the preferred device manufacturer in Axonius.
  * Each of the above four **Convert preferred** options can be set to one of the following:
    * **no conversion** - Not make any changes.
    * **lowercase** - Convert to lowercase in Axonius.
    * **uppercase** - Convert to uppercase in Axonius.
    * **title** - Convert the case of the value to a string where the first character in every word is uppercase. If the word contains a number or a symbol, the first letter after the number or the symbol is converted to uppercase. A number is any number from 0 to infinity; examples of symbols are  ! / @ / # / \_ / etc.). For example, `hello_world` becomes `Hello_World`; `hello3world` becomes `Hello3World`.
* **Convert Preferred VMware type Device Serial to UUID format** *(default: false)* - Select this option so that the serial number of a device that starts with VMware, will have the UUID value format of XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX. In all other cases, even if this is selected, no change will be made to the serial number of the device.
* **Remove domain from preferred hostname** *(default: False)* - Select this option to remove the domain value from the **Preferred Host Name** field.
* **Remove domain from preferred asset name** *(default: false)* - Select this option to remove the domain value from the **Preferred Asset Name** field.
* **Remove domain from preferred user** *(default: false)* - Select this option to remove the domain name from the **Preferred User Name** field.
* **Remove trailing spaces from preferred values**  *(default: true)* - By default, Axonius removes trailing spaces (before and after the values) from preferred fields. Clear this option to keep spaces.
* **Preferred OS fields: Allow the following adapters (comma separated list)** *(optional)* - Enter a comma separated list of adapters to include in the Preferred OS calculations. Once an adapter is in the allow list, the Preferred OS fields will only be calculated using adapters in this list. The adapter name is the full Adapter name as it appears as part of the URL when viewing the adapter in the Axonius URL while looking at the adapter in the Axonius console.
* **Preferred OS fields: Ignore the following adapters (comma separated list)** *(optional)* - Enter a comma separated list of adapters to exclude from the Preferred OS. Once an adapter is in the ignore list, it is excluded from the preferred OS list. The adapter name is the full Adapter name as it appears as part of the URL when viewing the adapter in the Axonius URL while looking at the adapter in the Axonius console.
* **Remove loopback ip addresses from preferred IPs** *(default: true)* - Enable this option to remove the loopback IP address from the list of preferred IP addresses.
* **Remove link local ip addresses from preferred IPs** *(default: true)* - Enable this option to remove to remove the link-local IP address from the list of preferred IP addresses.
* **Update adapters connections status periodically (every 1:30 hours)** *(default: false)* - Select whether to update the status of all the adapter connections every 1:30 hours. Otherwise, Axonius updates the status of all the adapter connections as part of a discovery cycle.
* **Number of enforcement tasks that can run in parallel** *(required, default: 10)* - Specify the number of enforcement tasks that can run simultaneously.
* **Support inferring unverified SaaS Applications from extensions** *(default: false)* - Enable this option to add all extensions to SaaS applications even when the vendors aren't recognized by the Axonius internal Vendors database.
* **Ignore the following strings when discovering SaaS applications (comma-separated list)** *(optional)* - Enter a comma-separated list of strings to ignore in the process of [discovering and matching SaaS Applications](/docs/managing-saas-applications-discovery).
* **Set SaaS Management active user definition** *(default: false)* - Enter the exact number of days after a user's last access to a SaaS application before their status changes to 'Inactive' as reflected in all relevant fields across the SaaS Management module.
* **Ignore default definitions and designate application extensions of these types as SaaS Applications** *(default: SSO, IDP, Admin Consent, Bookmark)* - The extension types listed are converted to SaaS Applications by default. Use this setting to determine which application extensions are matched to SaaS Applications by default. If you remove an extension type from this list. If it is matched by the Axonius SaaS Applications Repository, it is automatically moved to the SaaS Applications page. Otherwise, you can use [**SaaS Application Discovery Management**](/docs/managing-saas-applications-discovery) to match the extension to a SaaS Application, if a default matching doesn't already exist.
* **Split Application Settings by unique configuration values** - Select this option to ungroup application settings that contain multiple configuration values, typically when settings differ based on specific roles, groups, or users. By default, these variations may be aggregated into a single setting. Enabling this option splits each unique configuration value into a separate asset, allowing for granular visibility and querying of each distinct instance.