# Source: https://docs.axonius.com/docs/one-password-suspend-user.md

# 1Password - Suspend User

**1Password - Suspend User** suspends a user in 1Password for each asset that matches the parameters of the selected saved query, and the other Enforcement Action settings or the assets selected on the relevant asset page.

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

* **Use stored credentials from  1Password adapter** - Select this option to use the first SAS Concur connected adapter credentials.[1Password](/docs/one-password)

  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

## Required Fields

These fields are required to run the Enforcement Action.

* **Deauthorize Devices After** - An integer representing the amount of time given between the suspend command, and the actual suspension. The default is 0 (zero).
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **OnePassword Address** - The domain of the OnePassword server.
    ::: info (Note:)

  * The address should not contain a prefix of *http\://* or *https\://*.

  * Do not add any specific endpoint after the domain.

  * For example: *agilebits.1password.com*
</Callout>

* **Email** - The user's email address.

* **Password** - The password of the account that is suspending the user.

* **Secret Key** - The Secret Key of the account that is suspending the user.

* **MFA Secret** - The Multi-factor Secret of the account that is suspending the user.
  :::

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The account used by the adapter to access 1Password must be administrator/owner.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).