# Source: https://docs.axonius.com/docs/update-azure-ad-user.md

# Microsoft Entra ID (formerly Azure AD) - Update User

**Microsoft Entra ID - Update User** updates the information in the Microsoft Entra ID user account for:

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

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Microsoft Entra ID adapter** - Select this option to use [Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad) adapter credentials.
  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* Fill in additional user information such as Email, Birthday, etc.
* **Image (use "Configure Dynamic Values" to select an image)** -  Leave this field blank unless you want to update the User's profile image. In this case, configure a Dynamic Value statement, as follows:
  1. Under **Required Fields**, enable the **Configure Dynamic Values** toggle.
  2. Using the **Wizard**, configure the Dynamic Value **All** statement as follows (see the screen below): Set the image in the action configuration (**Image (use "Configure Dynamic Values" to select an image)**) to be the first non-empty valid image from the selected adapters’ **Image** field. You can click **Syntax** to see the statement syntax.
     * If you do not configure a Dynamic Values statement to set the image or none of the selected adapters in the statement has an image, then no image is uploaded, unless an image is uploaded manually via the File-Upload button.

<Callout icon="📘" theme="info">
  Note

  When you manually upload an image, the uploaded image will be used for all users affected by the enforcement action, unless Dynamic Values are configured.
</Callout>

<Image alt="EntraID_Image" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntraID_Image.png" />

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  **Azure Client ID** - The Application ID of the Axonius application, as detailed in the [Required Permissions](#required-permissions) section.

  * **Azure Client Secret** *(required)* - A user created key for the Axonius application, as detailed in the [Required Permissions](#required-permissions) section.

  * **Azure Tenant ID** - The ID for Microsoft Entra ID, as detailed in the [Required Permissions](#required-permissions) section.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **Cloud Environment** - Select your Microsoft Azure or Microsoft Entra ID cloud environment type.

  * **Azure Oauth Authorization Code** (optional) - The authorization code to connect to Microsoft Intune. For more information see [Generate the OAuth Authorization Code](/docs/microsoft-azure-active-directory-ad#generate-the-oauth-authorization-code).

  * **Azure OAuth - Redirect URI/Reply URL** - The location where the authorization server sends the user once the Azure has been successfully authorized and granted an authorization code or an access token. For more information, see [Redirect URI (reply URL) restrictions and limitations](https://learn.microsoft.com/en-us/entra/identity-platform/reply-url).

  * **Is Azure AD B2C** - Select this option to cause Axonius to consider that this Microsoft Entra ID adapter connection is configured as B2C.

  * **Account Tag** - Specify a tag for Axonius to tag all devices fetched from this adapter for the Azure Cloud instance ("nickname").

  * **Device Groups Blocklist** (optional) - Enter a group or groups whose devices will be ignored and not fetched. If you want to enter more than one group, separate with commas.

  * **HTTPS Proxy** - A proxy to use when connecting to the selected Microsoft Azure/Entra ID cloud environment.

  * **HTTPS Proxy User Name** and **Password** (optional) - The user name and password to use when connecting to the selected Microsoft Azure / Azure AD cloud environment via the value supplied in HTTPS Proxy.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.

  <Callout icon="📘" theme="info">
    Note

    The following parameters are only relevant for customers who have SaaS Management enabled.
  </Callout>

  * **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).
  * **User Name** and **Password** - The credentials for a user account that has the permissions needed to fetch SaaS data.
  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user. For more information, see E [nable or Exclude Multi-Factor Authentication](/docs/microsoft-azure-active-directory-ad#enable-or-exclude-multifactor-authentication).
  * **SSO Provider** - If your organization uses Microsoft Entra ID for SSO, you can select this check box. For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).
</Callout>

## APIs

Axonius uses the [Micrososft - Update User](https://learn.microsoft.com/en-us/graph/api/user-update?view=graph-rest-1.0\&tabs=http) API.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).