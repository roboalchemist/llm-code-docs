# Source: https://docs.axonius.com/docs/identity-now-create-campaign.md

# SailPoint IdentityNow - Create Certification Campaign

**SailPoint IdentityNow - Create Certification Campaign** creates a certification campaign for users that result from the saved query supplied as a trigger (or users that were selected in the Users table) who have a specified, new manager.

*Certification* refers to Identity Security Cloud's mechanism for reviewing a user's set of permissions, and approving or removing those permissions. Different reviewers often require multiple certifications to approve a user's access. A set of various certifications is called a *Certification Campaign*. A certification campaign, which includes each employee's current permissions, is sent to the new manager of employees. The new manager reviews each employee's permissions, and reapproves/revokes each permission.

<Callout icon="📘" theme="info">
  Note

  This Enforcement Action currently supports only `SEARCH` campaigns with an `IDENTITY` type. For more information, see the [SailPoint API Guide](https://developer.sailpoint.com/docs/api/v3/create-campaign/).
</Callout>

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from SailPoint IdentityNow adapter** - Select this option to use the connected SailPoint IdentityNow adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action. To use this option, you must successfully configure a [SailPoint IdentityNow](/docs/sailpoint-identity-now) adapter connection.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Campaign Name** - Enter a name for the campaign.
* **Campaign Description** - Enter a description for the campaign.
* **New Manager ID** - Enter the ID of the new manager.

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **User Name or IP Address** - The hostname or IP address of the SailPoint IdentityNow server. The field format is *[https://sailpoint.api.identitynow.com/v3](https://sailpoint.api.identitynow.com/v3)*.

  * **Client ID** and **Client Secret** - The Client ID and Client Secret for an account that has the Required Permissions to the API. For more information, see [this explanation on the adapter's connection parameters](/docs/sailpoint-identity-now#parameters).

  * **SSO Provider** *(Only for accounts with SaaS Management capability)* - If your organization uses Okta for SSO, this adapter can be set as an SSO provider. see [Connecting your SSO Solution Provider](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).