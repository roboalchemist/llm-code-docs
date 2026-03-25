# Source: https://docs.axonius.com/docs/reset-users-password-in-ms-ad.md

# Microsoft AD - Reset Users' Passwords

**Microsoft Active Directory (AD) - Reset Users' Passwords** causes Active Directory to prompt users to change their password, next time that they try to login to their system for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined, or assets selected on the relevant asset page.

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

* **Use stored credentials from Active Directory adapter** (*required, default: False*) - Select this option to use the first connected [Microsoft Active Directory (AD](/docs/microsoft-active-directory-ad)) adapter credentials.

<Callout icon="📘" theme="info">
  NOTE

  * To use this option, you must successfully configure a [Microsoft Active Directory (AD](/docs/microsoft-active-directory-ad)) adapter connection.

  * The user name and the password used for the adapter connection must have the  permissions to fetch assets.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **User Name** and **Password** (*optional, default: empty*) - Provide credentials to connect and to execute the command on the windows device: user name and password.

<Callout icon="📘" theme="info">
  NOTE

  If **Use stored credentials from Active Directory adapter** is toggled off, these fields need to be configured.
</Callout>

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

## Required Permissions

In order to reset passwords Privileged Authentication Administrator is required. Refer to [Microsoft Entra Built in Roles](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#privileged-authentication-administrator) for more information.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).