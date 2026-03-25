# Source: https://docs.axonius.com/docs/six-clicks-report-test-result.md

# 6clicks - Report Test Result

**6clicks - Report Test Result** creates a test result on an existing test in 6clicks and sends the notification to:

* Findings returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  This action is intended to run only on **Findings** assets.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the 6clicks adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [6clicks](/docs/six-clicks) adapter connection.
</Callout>

* **Test Name** - The name of an existing test in 6clicks.
* **Test Description** -  A description of the test result, limited to 3000 characters.
* **Test Result** - Select which result to report: Pending, Pass, Fail, or Error.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(default: `https://api-au.6clicks.io`)* - The hostname or IP address of the 6clicks server.

  * **API Key**  - An API Key associated with a user account that has the [Required Permissions](/docs/six-clicks-report-test-result#required-permissions) to fetch assets.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [6clicks Developer API](https://api-au.6clicks.io/swagger/index.html).

## Required Permissions

Choose one of these snippets:

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Read Tests via `GET /controls-api/1.0/tests`
* Post Test Results via `POST /controls-api/1.0/tests/{testKey}/results`

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).