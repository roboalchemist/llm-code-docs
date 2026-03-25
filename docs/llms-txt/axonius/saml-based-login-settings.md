# Source: https://docs.axonius.com/docs/saml-based-login-settings.md

# SAML-Based Login Settings

Use SAML-based login to enable login using your existing enterprise identity provider, such as Okta or Microsoft Active Directory (AD).

## Configuring General SAML-Based Login Parameters

These parameters apply to all SAML integrations and only need to be entered once.

* Under the **SAML-Based Login Settings** section, toggle on **Allow SAML-based Logins**.
* **Restrict to SAML login only** - Enable this option to allow only SAML-based logins. Manual login is disabled.
* **Logout from SAML provider on logout from Axonius** *(default: enabled)* - Enable this option to log out from the SAML provider when the user logs out from Axonius.
* **Axonius external URL** - This is optional. Used to access Axonius from an external URL. If the communication to Axonius is being proxied, then this should be the external domain, i.e., the proxy domain.
* **Ignore user name case when logging in** - When selected, the case of the user name will be ignored. This prevents a new Axonius account being created when a user connects with the same user name but is cased differently. For example: `example@demo.com` and `eXamPle@Demo.com`. In this case, a new account will not be created.

## Configuring a SAML Instance

To configure a SAML instance, use the configuration sections below. Not all configurations require all the sections to be configured. You can configure as many instances as necessary for your environment.

### Creating a SAML Instance with a Metadata File

Using metadata files is the easiest and quickest way to configure a SAML instance with a provider. It contains all the URLs needed to create a SAML connection.  When multiple SAML instances are being used, each instance has its own metadata file for download.

**To create a SAML instance using the metadata file:**

1. Configure the following settings for each SAML instance. Learn about [Using Multiple SAML Providers](/docs/saml-based-login-settings#using-multiple-saml-providers).
   * **Name of the identity provider** *(required)* - If your identity provider supports metadata URL parsing, you can use the link to automatically fill in some details. If it doesn't, fill them manually in the **Name of the identity provider** field. Note that the name of the identity provider can be any string you like; It is used only to identify the identity provider within Axonius.
   * **Unique name of IdP** *(required)* - A unique name for the identity provider that cannot be changed after it is saved. This name must be added to the SSO provider when creating the connection. The IDP name:
     * Cannot contain spaces, hyphens, or a long word.
     * Can be up to 10 characters and may contain numbers.
     * Examples: AxSSO00001, AxLogin001, AxAzure001

<Callout icon="📘" theme="info">
  IdP Note

  After configuring this option and saving, the IdP field will become inactive and cannot be changed. The option will appear in the list of available identity providers for the user. The IdP must be added to paths.
</Callout>

2. Click **Save** at the bottom of the page to save the instance.
3. Click **Download Metadata file**. The file is downloaded to your local Downloads folder.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLMetaDataFileDownload.png)
4. On the provider portal, fill out any necessary fields and upload the metadata file you downloaded from Axonius.
5. Next, copy the metadata URL from the provider and paste it into the **Metadata URL** field in Axonius.
6. To customize the integration further, you may need to fill other options described below.

### Configuring a SAML Instance without Using the Metadata File

Use the following steps to configure a SAML provider instance. This section is required for all SAML instances.

**To configure a SAML instance without using the metadata File:**

1. Configure the following settings for each SAML provider. Learn about [Using Multiple SAML Providers](/docs/saml-based-login-settings#using-multiple-saml-providers).

* **Name of the identity provider** *(required)* - If your identity provider supports metadata URL parsing, you can use the link to automatically fill in some details. If it doesn't, fill them manually in the **Name of the identity provider** field. Note that the name of the identity provider can be any string you like; It is used only to identify the identity provider within Axonius.
* **Unique name of IdP** *(required)* - A unique name for the identity provider that cannot be changed after it is saved. This name must be added to the SSO provider when creating the connection. The IdP name:
  * Cannot contain spaces, hyphens, or a long word.
  * Up to 10 characters and may contain numbers.
    * Examples: AxSSO00001, AxLogin001, AxAzure001

<Callout icon="📘" theme="info">
  IdP Note

  After configuring this option and saving, the IdP field will become inactive and cannot be changed. The option will appear in the list of available identity providers for the user. The IdP must be added to paths.
</Callout>

* **Automatically redirect all logins to the identity provider** - Select whether to automatically redirect all users to the configured SAML identity provider.
  * When this is enabled, any user who tries to log in to Axonius will be automatically redirected to the configured SAML identity provider.
    * To access the Axonius login page without being redirected, use the following URL: *https\://\[Axonius host name / IP address]/?redirect=false*
  * When this is disabled, any user who tries to log in to Axonius will need to manually click the 'Login with SAML' option to login with the configured SAML identity provider.
* **Metadata URL** *(optional)* - Paste the URL that some SSO providers offer  that can be used in Axonius to fill in all the other details.

<Callout icon="💡" theme="warn">
  When not using the Metadata URL, the following fields must be filled in:

  * **Single sign-on service URL** - A URL that is needed for the SAML Authentication.

  * **Entity ID** - The ID of the Axonius entity in the identity provider.

  * **Single logout service URL** - A URL that is needed for the SAML Authentication.

  * **Signing certificate (Base64 encoded)** - Click **Upload File** to upload the base64-encoded signing certificate provided by your identity provider. Some environments require the certificate in PEM format. For information about viewing the certificate details, see [Viewing the Signing Certificate Details](#viewing-the-signing-certificate-details).

  These URLs are validated. When invalid, an error message is displayed at the bottom of the page.
</Callout>

* **Do not send AuthnContextClassRef** (Applies to: Microsoft Active Directory and Microsoft EntraID) - The SAML `AuthNRequest` will not include the `AuthnContextClassRef` SAML attribute:
  `\<saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport\<saml:AuthnContextClassRef> >`

2. In the identity provider console, define the credentials and SAML settings. These settings provide the values listed below and are used to enable SAML authentication in Axonius:

| Name                                 | Value                                                                             | Comment                                                                                       |
| ------------------------------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Signing certificate (Base64 encoded) | \`https\://\<axonius\_hostname>/api/login/saml/metadata/                          | A one-time URL for identity providers that support metadata URL parsing                       |
| Entity ID / Audience URI             | https\://\<axonius\_hostname>/api/login/saml/metadata/?idp=`<unique name of idp>` |                                                                                               |
| Reply URL / Single Sign on URL       | https\://\<axonius\_hostname>/api/login/saml/acs                                  | Assertion Consumer Service URL                                                                |
| Sign on URL / Default Relay State    | https\://\<axonius\_hostname>/api/login/saml                                      | Optional. This is useful only if you want to allow identity-provider initiated authentication |

<Callout icon="📘" theme="info">
  Note

  When creating an integration using the metadata files, these URLs are included in the metadata file and are filled in automatically in the provider portal.
</Callout>

## Viewing the Certificate Details

After you have uploaded a certificate (such as a CA file, IdP Signing certificate, or Private Key), the **Show certificate details** button becomes available. Clicking it opens a read-only modal with the following information:

* **Certificate Information** - Displays the Certificate Name/Alias, Issuer (CA), Subject, and Serial Number.
* **Validity Information** - Shows the Issued Date, Expiration Date, and the total Validity Period.
* **Technical Information** - Includes the Public Key Algorithm, Key Size, Signature Algorithm, and the Certificate Fingerprint (SHA-256 hash).
* **Certificate Status** - Indicates the Revocation status and whether the certificate is Self-Signed.
* **Metadata** - Displays system-related information, including the Upload Date and the user who performed the upload.

## Service Provider Signing Configuration

Configuring service provider signing is optional. You need a *private key* file and a *certificate* file saved on your system before performing this configuration.

To configure service provider signing:

* Click **Enable Service Provider signing** and fill in the following details:
  * **Enable AuthnRequestsSigned** - When selected, the service provider will sign authentication requests that it sends to the IdP.
  * **Enable WantAssertionsSigned** - When selected, the IdP wants the authentication requests it receives from the service provider to be signed.
  * **Signing Private Key** *(required)* - Click **Upload File** to upload the private key file (`.key`) that is required for SP signing. Click **Show certificate details** to verify the technical information of the uploaded file.
  * **Signing Certificate** *(required)* - Click **Upload File** to upload the signing certificate file (`.crt`). Click **Show certificate details** to view the certificate issuer, validity status, and public key information.

## Configuring SAML Session Reauthentication

Configuring reauthentication is optional. When configured, users will be required to reauthenticate according to the timeout.

To configure session reauthentication:

* Click **Enable SAML session reauthentication** and enter the **Reauthentication timeout claim key** as it is configured in IdP on the identity provider side, such as Okta or Azure. When the timeout is reached, the Login box is displayed and the user must reauthenticate.

## SAML User Parameters Mapping

When using SAML, Axonius uses your SAML parameters to identify users and assign roles to them.

Axonius requires the following attributes to be sent by the provider. You can map the terms your SAML uses to Axonius. If you do not map user parameters, Axonius will use the default parameters sent by your provider.

<Image alt="SAML_UserParametersMapping" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAML_UserParametersMapping.png" />

1. **User name** - The ID of the user in that identity provider. For example, in Active Directory or Azure Active Directory, this is the user principal name. If you do not fill in a value, the system uses the default from the identity provider.
2. **First name** -  The given/first name of the user. If you do not fill in a value, the system uses the 'givenname' value.
3. **Last name** - The surname of the user. If you do not fill in a value, the system uses the 'surname' value.
4. **Email** -  The email address of the user. If you do not fill in a value, the system uses the 'emailaddress' value.
5. **Department** -  The department of the user. If you do not fill in a value, the system uses the 'department' value.
6. **Job Title** -  The job title of the user. If you do not fill in a value, the system uses the 'title' value.

## Passing User Group Membership from Okta to Axonius with SAML

By default, group membership is not passed from Okta to an Axonius instance with SAML login. **Custom Group Attributes** need to be set in Okta. in order to pass user role assignments. They enable values such as group assignments, email addresses, and other values to be passed.

For more information about passing a user's group membership with SAML, see [How to pass a user's group membership in a SAML Assertion from Okta](https://support.okta.com/help/s/article/How-to-pass-a-user-s-group-membership-in-a-SAML-Assertion-from-Okta?language=en_US).

## User Assignment Settings

There are two ways users are assigned roles when they log in with SAML:

* **Default assignment** - Use default assignments when a user does not match an existing rule.
* **Rules** - This is the preferred way to assign roles to users.

### Configuring Default Assignment Settings

Use user assignment default settings to configure the access level assigned to users automatically when they don't match any of the configured assignment rules.

**To configure default assignments:**

1. Select which type of login the rule apply:
   * **New users only** - Default role assignment is evaluated only for new users. The role for existing Axonius users will not be reevaluated and will remain as is. If an existing user logs in and does not match any of the configured rules, that user is assigned the same role assigned that last time they logged in.
   * **New and existing users** - Default role assignment is evaluated for new users and also for existing users on every login.
2. In **Default role for SAML user**, select the default role assigned to assign. For details on managing user roles in Axonius, see [Manage Roles](/docs/manage-roles).

   <Callout icon="🚧" theme="warn">
     Important

     When a new user attempts to log in and does not match any of the existing role assignment rules, log in is refused and they are returned to the login page.
   </Callout>

* **Default data scope for SAML user** - Select the data scope to assign. For details about data scopes, see [Managing Data Scopes](/docs/data-scope-management).

### Configuring Rules for Assignment Settings

Use user assignment rules to determine what role and data scope a user is assigned when they log in. They are evaluated starting from the first rule in the list.

<Image align="center" alt="SAML - UserAssignmentSettings.png" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/eea7e3a3b4367e8c55b5e2c2c8a269a572a1fff5/Images/SAML%20-%20UserAssignmentSettings.png" />

**To create user assignment rules:**

1. Expand **User Assignment Rules**.

2. Select which type of login the rule apply:
   * **Apply on** -
     * **New users only** - Role assignment is evaluated only for new users. The role for existing Axonius users will not be reevaluated and will remain as is.
     * **New and existing users** - Role assignment is evaluated for new users and also for existing users on every login.

3. Configure the following fields for each rule:

   * **Key** *(case sensitive, exact match)* - A key is one of the user attributes from the identity provider.
   * **Value** *(case sensitive, exact match)* - The value, from the identity provider, of the attribute specified in **Key**.
   * **Role** - The role to be assigned. For details on managing user roles in Axonius, see [Manage Roles](/docs/manage-roles).
   * **Data Scope** - The data scope to be assigned. For details about data scopes, see [Managing Data Scopes](/docs/data-scope-management).

4. Click `+` to add as many rules as necessary. Click **X** to delete a rule.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLUserAssnmntRules.png)

   When a user's attributes match the **key/value** pair, they are logged in and assigned the selected role and data scope in Axonius. To reorder the rules, click the handle to the left of the rule and drag and drop rules into the order you want. The user's assigned role is determined based on the [Role Assignment Rules Logic](/docs/identity-providers-settings#role-assignment-rules-logic).

## SAML Advanced Settings

The following advanced settings are available:

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLAdvancedSettings2.png" />

### Using ADFS Compatible URLs

* **Create ADFS compatible URLs** - When using ADFS SAML authentication, select **Create ADFS compatible URLs** to have Axonius create and use ADFS compatible URLs.

#### Using SAML Credentials to Create Dynamic Data Scopes

Use Dynamic Data Scopes to allow users to log in without manually creating a Data Scope for each situation. When using an identity provider, Data Scopes can be assigned to users dynamically when they log in by mapping a Data Scope to their SAML login profile. This is done with JSON code.

**To enable Dynamic Data Scope mapping**

1. In System Settings, on the **LDAP & SAML** page, scroll down to **SAML Advanced Settings**.
2. Toggle on **Set Dynamic Data Scope**.
3. In the **Dynamic Data Scope mapping rule** box, paste the JSON mapping rule code. See [Creating the JSON Mapping Rule](/docs/saml-based-login-settings#creating-the-json-mapping-rule) below on how to create the JSON code.
4. Click **Save** to save the changes.

### Creating a JSON Mapping Rule

Use the following template to create the JSON mapping code:

```
{
"": {
  "": {
   "": ""
  }
 }
}
```

For example, use the following JSON to dynamically create Data Scopes based on the *viewer* role permissions. The Asset Scope query will compare the defined Axonius field value with the value of the defined SAML field.

```
{
"viewer": {
  "devices": {
   "adapters_data.active_directory_adapter.name": "test"
  }
 }
}
```

**To create JSON mapping code**

1. On the Queries page, select the Asset Scope Query that creates the Data Scope.
2. In the query drawer, click **Run Query**. The results are displayed on the asset page.
3. In the query bar, select and copy the Axonius field name, as shown here:

   <Image align="center" alt="SAML-JSON-mapping-blur.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAML-JSON-mapping-blur.png" className="border" />

<Callout icon="📘" theme="info">
  Note

  Do not include the quotation marks in the selection.
</Callout>

5. In the JSON template, enter the following values:
   * For **role name**, enter the name of the role from which the auto-created roles will be copied. (Valid options are **view** or **edit**.)
   * For **module name**, enter the name of the Axonius module. (Valid options are **devices** or **users**.)
   * For **axonius field**, paste the name of the Axonius field copied above.
   * For **SAML field**, enter the name of the SAML field to map to the **axonius field** field.
6. Create the JSON code directly in the **Dynamic Data Scope mapping rule** text box or in any text editor and then paste it into the text box.
7. Click **Save**.

## Using Multiple SAML Providers

Configure multiple SAML providers to allow users with different identity providers to easily log in to Axonius.

**To configure multiple SAML providers**

1. Enter the configuration details for the first SAML provider.
2. Click **Add New SAML**.
3. Fill in the configuration details for the provider according to the directions above. See [Configuring a SAML Provider](/docs/saml-based-login-settings#configuring-a-saml-provider).
4. Make sure to use a unique IdP.
5. To delete a SAML configuration, click the trashcan icon next to the configuration you want to delete.

***

See [Using Identity Providers](/docs/identity-providers-settings) for general information about using identity providers.
For information about LDAP-based login settings, see [LDAP Login Settings](/docs/ldap-login-settings).