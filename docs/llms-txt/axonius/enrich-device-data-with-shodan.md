# Source: https://docs.axonius.com/docs/enrich-device-data-with-shodan.md

# Shodan - Enrich Asset Data

**Shodan - Enrich Asset Data** enriches each of the assets that are the results of the query with additional data from Shodan, such as: hostname, ports open to the world, vulnerabilities, address information (country, region, city), ISP, and more.
The data enrichment is done per device based on its public IP address (IPv4).

<Callout icon="📘" theme="info">
  Note

  You can use the **IPv4 Public Subnets** devices saved query as the trigger for the enforcement set that executes the **Shodan - Enrich Asset Data** action.
  For more details, see [Configuring Triggers](/docs/configuring-triggers).
</Callout>

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Select Shodan adapter specific connection** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Shodan](/docs/shodan) adapter connection.
</Callout>

* **API key** - Specify the API key you have defined. See [Generating a Shodan API Key](/docs/enrich-device-data-with-shodan#generating-a-shodan-api-key).
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Shodan domain** - *(default: api.shodan.io)* The Shodan domain. You can change it, if required.
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **Use hostname as enrichment option** - When selected, the hostname is used instead of the IP address.

### Generating a Shodan API Key

**To generate a Shodan API key:**

1. Register for an account in Shodan.
2. Visit your registered email ID and activate the account.
3. Login to your account and you will find the API keys under the Profile Overview tab.
4. Copy the API key and this is the value for *\_shodan*api** field in the *config.py* file.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).