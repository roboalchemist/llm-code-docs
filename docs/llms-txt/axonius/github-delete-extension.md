# Source: https://docs.axonius.com/docs/github-delete-extension.md

# Github - Remove User Extensions

**Github - Remove User Extension**  removes a user extension for each GitHub user retrieved from the saved query supplied as a trigger (or users selected in the asset table).

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

* **Use stored credentials from the GitHub adapter** - Select this option to use the first connected Github adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **GitHub Domain** *(default: api.github.com)* - Enter the GitHub domain to use when running the Enforcement Action.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Organization** - The GitHub organization name.

  * **Authorization Token** - The GitHub access token.

  * **Authenticate Using GitHub App** - When selected, uses the GitHub app to authenticate.

  * **GitHub App ID** - The GitHub App ID.

  * **App Key File (pem)** - The GitHub App Key file. Select a file and click **Upload File**.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [GitHub - Remove a repository from an app installation](https://docs.github.com/en/rest/apps/installations?apiVersion=2022-11-28#remove-a-repository-from-an-app-installation) API.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).