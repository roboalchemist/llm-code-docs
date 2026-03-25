# Source: https://docs.axonius.com/docs/run-absolute-reach-scripts.md

# Absolute - Run Script

**Absolute - Run Script** runs an Absolute script on:

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

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Absolute adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  * To use this option, you must successfully configure an [Absolute](/docs/absolute) adapter connection.

  * The credentials used for the adapter connection must have the required permissions to run scripts.
</Callout>

* **Script UID** - The system-defined unique identifier for the script.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Absolute Domain** *(optional)* - Your Absolute domain. The Absolute API access is limited to two regions:

  * Canadian Data Center (CADC) - *[https://api.absolute.com](https://api.absolute.com)*

  * US Data Center (USDC) - *[https://api.us.absolute.com](https://api.us.absolute.com)*

  * **Data center** *(optional)* - Specify the regional data center (must be in lowercase):

  * uscd - For the US Data Center.

  * cadc - For the Canadian Data Center.

  * **Token ID**  and **Client Secret** *(required)* -  The Absolute API requires an authentication token which consists of two parts: token ID and secret key. These are generated from the Absolute console, using a custom user role, defined by your organization, or the Guest user role.
    For more details about creating a Token ID and a Secret Key, see [Working with Absolute APIs](https://www.absolute.com/media/2221/abt-api-working-with-absolute.pdf).

  <Callout icon="📘" theme="info">
    Note

    The System Administrator of your Absolute console can assign the role.
  </Callout>

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Title** *(optional)* -  The user-defined title of the run-script request.

* **Max run time** *(optional)* - The maximum length of time a script is allowed to run on a device.

* **Max run time unit** *(optional)* - The unit of time used for **Max run time**.

* **Display mode** *(optional)* - The visibility of the Windows PowerShell dialog when the script runs on a device.

* **Run privileges** *(optional)* - The permissions used to run the script.

* **Run when**  *(optional, default: UserIsOrIsNotSigedIn)* - The run condition that determines when the script is allowed to run, according to the sign-in status of the user. Valid conditions include:
  * UserIsOrIsNotSigedIn *(default)* - The script runs regardless of whether a user is logged in or not.
  * UserIsSignedIn - The script runs only when a user is logged in.
  * NoUserIsSignedIn - The script runs only when no user is logged in.

* **Command line** *(optional)* - The PowerShell command line parameters used to execute the script.

* **Startup dir** *(optional)* - The directory location used by the agent to download and run scripts on the device.

* **Always run 32 bits** - Run 32-bit version: Version of PowerShell used on 64-bit Windows devices.

* **Windows script option** *(optional)* - The configurations used to execute the PowerShell script on Windows devices.

* **Mac script option** *(optional)* - The configurations used to execute the Bash script on Mac devices.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).