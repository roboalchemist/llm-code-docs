# Source: https://docs.axonius.com/docs/tanium-add-or-remove-tag-tofrom-assets.md

# Tanium - Add or Remove Tag to/from Assets

**Tanium - Add or Remove Tag to/from Assets** adds or removes tags to or from:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

These fields are required to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Tanium Interact adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

* **Action type** - Select whether to **Add tags** or **Remove tags**.

* **Tags names** - Enter the names of the tags to add or remove, separated by a blank space.

* **Os type** *(default: Automatically)* - Select the OS of target assets. *Automatically* tells the Enforcement Action to determine the OS type automatically.

* `{{snippet.Instance Name}}`

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Hostname or IP Address** - Host name or IP address of the Tanium server.
  * **User Name or API Token ID** - The Tanium credentials to use to connect to the Tanium server.
  * **Password or API Token** - The Tanium credentials to use to connect to the Tanium server.
  * **Names of Saved Questions to fetch** - Enter the names of the saved questions to fetch, separated by a comma. Tags will be added or removed from these questions.
  * **Re-ask every fetch** - When fetching data for a connection, ask Tanium to issue a new question to get the current results for each value supplied to **Names of Saved Questions to fetch (comma separated)**.
  * **Re-ask if results are older than N hours** *(default: 24)* - When fetching data for a connection, if the results for each value supplied to **Names of Saved Questions to fetch (comma separated)** are older than this many hours, ask Tanium to issue a new question to get the current results.
    * If the value provided is 0, no age check is performed and a new question will not be issued based on the value supplied here.
  * **Re-asking waits until all answers are returned** - When a new question is issued for a Saved Question, wait until the question expires (10 minutes) before fetching assets.
  * **Use Server Side Export** - Utilize Tanium's Server Side Export to export all of the data on the Tanium platform into one XML file instead of paging through the data utilizing the Tanium REST API.
  * **Parse Dynamic Fields** *(default: enabled)* - Enable/disable the creation of adapter specific dynamic fields being created for every sensor included in the supplied Saved Questions.
  * **Parse Advanced View** *(default: enabled)* - Enable/disable the processing of raw data from Tanium into the Advanced View of each asset.
  * **Get hostname from "Short Hostname" instead of "Computer Name"** - When selected, the hostname will be parsed with local name of the machine.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Expire minutes** - The number of minutes the action created will take to expire.
* **Computer Group Name Prefix** *(default: Axonius)* - The computer group name prefix to be used.
* **Max devices per deploy** *(default: 10)* - The max number of assets per group.

See [Tanium Interact adapter documentation](/docs/tanium-sq) for more details.

## Required Permissions

The user must have permission to manage actions and action groups (more information on that can be found on [Tanium Console and Interact Requirements](https://docs.tanium.com/platform_user/platform_user/requirements.html#role_permissions_actions) in the “User role requirements” section.

If your environment has **Action Approval** configured, you can assign a role to the Axonius user to bypass it (see [Managing Action Approval](https://docs.tanium.com/platform_user/platform_user/action_approval.html)) or you can approve the action each time it runs.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).