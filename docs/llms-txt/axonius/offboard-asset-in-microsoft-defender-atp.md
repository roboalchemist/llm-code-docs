# Source: https://docs.axonius.com/docs/offboard-asset-in-microsoft-defender-atp.md

# Offboard Assets - Microsoft Defender ATP

**Offboard Assets - Microsoft Defender ATP** removes assets from Microsoft Defender ATP for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  NOTE

  To use the actions below, you must successfully configure a [Microsoft Defender for Endpoint](/docs/microsoft-defender-atp) adapter connection.
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

<Callout icon="📘" theme="info">
  Notes

  * It will take 7 days after offboardng to see an inactive status.

  * The API will returns with a Status 200 response, indicating that the POST action completed successfully and the next time the device becomes available/online, **Defender for Endpoint** will offboard the device automatically without notification or approval.

  * This API is supported on Windows 11, Windows 10, version 1703 and later; on Windows Server 2019 and later; and on Windows Server 2012 R2 and Windows Server 2016 when using the new, unified agent for Defender for Endpoint. This API is not supported on macOS or Linux devices.

  * To check if the device is offboard - See [How to check if Offboarding of a Device was successfull?](https://www.reddit.com/r/DefenderATP/comments/o15caf/how_to_check_if_offboarding_of_a_device_was/) If there are still no changes in the status after 7 days, ask the client to have Microsoft Defender ATP support to check the issue.
</Callout>

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Use stored credentials from Microsoft Defender for Endpoint (Microsoft Defender ATP) adapter** - Select this option to use the first connected Microsoft Defender for Endpoint adapter credentials.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Source Host Name** *(default: api.securitycenter.microsoft.com)* - The domain name of the Defender ATP host. Use the specific based location URL if the URL is without location:
  * EU - api-eu.securitycenter.microsoft.com
  * UK - api-uk.securitycenter.microsoft.com
  * USA - api-us.securitycenter.microsoft.com

* **Tenant ID** - The Defender ATP tenant name.

* **Client ID** - The Defender ATP client ID.

* **Client Secret** - The Defender ATP client secret.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

## Required Permissions

The Microsoft Entra ID (Azure AD) application configured in the [Defender ATP adapter](/docs/microsoft-defender-atp) must have the following Application permission:

* Machine.Isolate

See [Microsoft Defender ATP](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/isolate-machine?view=o365-worldwide#permissions) documentation for more information.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).