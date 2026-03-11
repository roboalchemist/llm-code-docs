# Source: https://docs.axonius.com/docs/tag-in-sentinelone.md

# SentinelOne - Add or Remove Tag to/from Assets

**SentinelOne - Add or Remove Tag to/from Assets**  adds, removes or replaces the tags on SentinelOne assets that match the selected query or devices that were selected in the asset table.

To be able remove or override tags, you must supply the existing tag key and existing tag value from the SentinelOne management console. If the tag does not exist, the Enforcement Action will fail and return the error message: “Could not find tag - ”

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

**Use stored credentials from the SentinelOne adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

* When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [SentinelOne](/docs/sentinelone) adapter connection.
  </Callout>

* **Tag Key** - Specify a tag name.

* **Tag Value** - Specify a tag value.

* **Add or remove tag** - Select whether to add or remove tags. Select one of the following actions:

  * **Add tag** - Adds a new tag.
  * **Remove tag** - Removes the tag specified in **Tag key**.
  * **Override tag** - Replaces the value of the tag specified in **Tag key** with the contents of **Tag value**.

  <Callout icon="📘" theme="info">
    Note

    To remove or override a tag you must supply the existing tag key and existing tag value from the SentinelOne management console.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **SentinelOne Domain** - The hostname or IP Address of the SentinelOne management server. This field format is '\[instance].sentinelone.net'.

  <Callout icon="📘" theme="info">
    Note

    If **Use stored credentials from the SentinelOne adapter**  is not enabled, these fields are required.
  </Callout>

  * **User Name** and **Password** - The user name and password for an account that has site viewer access to the management server.

  <Callout icon="📘" theme="info">
    Note

    * The **User Name** and **Password** parameters take precedence over the **API Token** parameter.
    * If **API Token** is not supplied, **User Name** and **Password** fields are required.
  </Callout>

  * **2FA Secret** *(only for accounts with SaaS Management capability)* - The secret generated in SentinelOne for setting up two-factor authentication for the adapter user created for collecting SaaS data.
  * **Singularity Data Lake (SDL) API Key** (*optional*) - Enter the API Key from the Singularity Data Lake in order to enable the SDL queries in Advanced Settings. Note: This requires Log Read Access permission.
  * **API token** - The API token is created within the My User Profile of the account with viewer access to the management server.

  <Callout icon="📘" theme="info">
    Note

    * When Two Factor Authentication is used, you must use **API Token** and leave the **User Name** and **Password** fields empty.
    * If **User Name** and **Password** are not supplied, **API Token** field is required.
  </Callout>

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

### Tag Scope

Some tags are associated with a specific scope. To add or remove such tags, you must provide the following parameters:

* **Scope Level** - Select Account, Group, or Site.
* **Account/Group/Site ID** - provide the specific ID required for SentinelOne to find the tag.

## Required Permissions

The account used to add or remove tags must have the edit(write) or admin permissions on the agent's role scope permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).