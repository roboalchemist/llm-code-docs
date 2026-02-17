# Configure SAML with Okta

The following process provides steps to configure SAML 2.0 with Okta for
Mattermost.

See the encryption options documentation for details on what
`encryption methods <deployment-guide/encryption-options:saml encryption support>`{.interpreted-text
role="ref"} Mattermost supports for SAML.

.. This page is intentionally not accessible via the LHS navigation pane
because it\'s common content included on other docs pages.

## Before you begin

Before you begin, you need to generate encryption certificates for
encrypting the SAML connection.

1. You can use the [Bash
    script](https://github.com/mattermost/docs/tree/master/source/scripts/generate-certificates)
    from the `mattermost/docs` repository on GitHub, or any other
    suitable method. See the
    `generate self-signed certificates </scripts/generate-certificates/gencert>`{.interpreted-text
    role="doc"} documentation for details on generating a self-signed
    x509v3 certificate for use with multiple URLs / IPs.
2. Save the two files that are generated. They are the private key and
    the public key. In the System Console, they are referred to as the
    **Service Provider Private Key** and the **Service Provider Public
    Certificate** respectively.

## Set Up a connection app for Mattermost Single Sign-On

1. Log in to Okta as an administrator.

2. Switch to the **Classic UI**, using the drop-down in the upper left.

3. Go to **Admin Dashboard \> Applications \> Add Application**.

4. Select **Create New App**, then choose **SAML 2.0** as the Sign on
    method.

    > ![In Okta, switch to the Classic UI, then go to the Admin Dashboard \> Applications \> Add Application to create a new app. Choose SAML 2.0 as the Sign on method.](../../images/okta_1_new_app.png)

5. Enter **General Settings** for the application, including **App
    name** and **App logo** (optional). It\'s recommended to display the
    application icon to users, including in the Okta Mobile app. If
    you'd like to use a Mattermost logo for the application, you can
    download one [from our
    page](https://handbook.mattermost.com/operations/operations/publishing/publishing-guidelines/brand-and-visual-design-guidelines).

    > ![In Okta, under General Settings, enter an App name and an optional logo. Mattermost recommends displaying the application icon to users and within the Okta mobile app. Select Next to continue.](../../images/okta_2_general_settings.png)

6. Enter **SAML Settings**, including:

> - **Single sign on URL:**
>   `https://<your-mattermost-url>/login/sso/saml` where
>   `https://<your-mattermost-url>` should typically match the
>   `Mattermost Site URL <administration-guide/configure/environment-configuration-settings:site url>`{.interpreted-text
>   role="ref"}.
>
> - **Audience URI:** For instance, `mattermost`
>
> - **Name ID format:** `unspecified`
>
> - **Application username:** `Email`
>
>   > ![In Okta, under Configure SAML, enter required SAML settings.](../../images/okta_3_initial_saml_settings.png)

1. To set up encryption for your SAML connection, select **Show
    Advanced Settings**.

    ![In Okta, under Configure SAML, set up encryption for your SAML connection by selecting Show Advanced Settings.](../../images/okta_4_initial_saml_settings.png)

2. Set **Assertion Encryption** as **Encrypted**, then upload the
    Service Provider Public Certificate you generated earlier to the
    **Encryption Certificate** field.

    > ![In Advanced Settings, set the Assertion Encryption as Encrypted, then upload the generated Service Provider Public Certificate to the Encryption Certificate field](../../images/okta_5_advanced_saml_settings.png)

3. Enter attribute statements used to map attributes between Okta and
    Mattermost. For more information on which attributes are
    configurable, see our
    `documentation on SAML configuration settings <administration-guide/configure/authentication-configuration-settings:saml 2.0>`{.interpreted-text
    role="ref"}. Email and username attributes are required. For SAML
    with Okta, an
    `ID attribute <administration-guide/configure/authentication-configuration-settings:id attribute>`{.interpreted-text
    role="ref"} is also required, and that ID must be mapped to
    `user.id`.

    > ![Enter attribute statements used to map attributes between Okta and Mattermost. Email and username attributes are required. Okta also requires an ID attribute that must be mapped to user.id.](../../images/okta_6_attribute_statements.png)

4. Select **Next**. Then, set Okta support parameters for the
    application. Recommended settings:

> - **I'm an Okta customer adding an internal app**
>
> - **This is an internal app that we have created**
>
>   > ![Set recommended Okta support parameters for the application, including I\'m an Okta customer adding an internal app and This is an internal app that we have created.](../../images/okta_7_support_configuration.png)

1. Select **Finish**.

2. In the Mattermost System Console, go to **Authentication \> SAML
    2.0**, then set **Override SAML bind data with AD/LDAP information**
    to **false** if currently set to **true**. You can re-enable
    `this configuration setting <administration-guide/configure/authentication-configuration-settings:override saml bind data with ad/ldap information>`{.interpreted-text
    role="ref"} later when once setup is complete.

3. On the next screen, select the **Sign On** tab, then select **View
    Setup Instructions**.

4. Select the **Identity Provider metadata** link, then copy the link
    from the browser URL field. This will be used during the SAML
    configuration steps in the next section.

    ![In the Mattermost System Console, after disabling the Override SAML bind data with AD/LDAP information setting, select the Sign On tab, then select View Setup Instructions. Select the Identity Provider metadata link, then copy the link from the browser URL field to a convenient location.](../../images/okta_8_view_instructions.png)

5. Take note of **Identity Provider Single Sign-On URL** (also known as
    **SAML SSO URL**), and the Identity Provider Issuer, as both may be
    needed to configure SAML for Mattermost.

6. Download the X.509 Certificate file and save it. You may need to
    upload it to Mattermost in a later step.

    ![Download the X.509 certificate file and save it. You\'ll upload this certificate file to Mattermost later.](../../images/okta_9_view_instructions.png)

## Configure SAML Sign-On for Mattermost

Start the Mattermost server and log in to Mattermost as a system admin.
Go to **System Console \> Authentication \> SAML 2.0**, then paste the
copied Identity Provider Metadata URL in the **Identity Provider
Metadata URL** field and select **Get SAML Metadata from IdP**.

This populates the **SAML SSO URL** and the **Identity Provider Issuer
URL** fields automatically. The Identity Provider Public Certificate is
also downloaded from the server and set locally.

Alternatively you can enter the following fields manually:

:   - **SAML SSO URL:** `Identity Provider Single Sign-On URL` from
      Okta, specified earlier.

    - **Identity Provider Issuer URL:** `Identity Provider Issuer` from
      Okta, specified earlier.

    - **Identity Provider Public Certificate:** X.509 Public Certificate
      file you downloaded from Okta earlier.

      > ![In the Mattermost System Console, go to Authentication \> SAML 2.0 to manually enter the SAML SSO URL and Identity Provider Issuer URL, and upload the Identity Provider Public Certificate manually.](../../images/okta_10_mattermost_basics.png)

2.  Configure Mattermost to verify the signature. The **Service Provider
    Login URL** is the `Single sign on URL` you specified in Okta
    earlier.

    > ![On the SAML 2.0 page, configure Mattermost to verify the signature, and set the Service Provider Login ULR as the Single sign on URL configured in Okta.](../../images/okta_11_mattermost_verification.png)

3.  Enable encryption based on the parameters provided earlier.

    > ![On the SAML 2.0 page, enable encryption and upload both the Service Provider Private Key and the Service Provider Public Certificate.](../../images/okta_12_mattermost_encryption.png)

4.  Configure Mattermost to sign SAML requests using the Service
    Provider Private Key.

1.  

    Set attributes for the SAML Assertions used to update user information in Mattermost.

    :   - Attributes for Email, Username, and Id are required and should
          match the values you entered in Okta earlier.

        ![Set attributes for the SAML Assertions used to update user information in Mattermost.  Attributes for Email, Username, and Id are required and should match the values set in Okta.](../../images/okta_13_mattermost_attributes.png)

6.  (Optional) Customize the login button text.

    > ![You can customize the login button text. By default, the text displays as \"With SAML\".](../../images/okta_14_mattermost_login_button.png)

7.  Select **Save**.

1. (Optional) If you configured `First Name` Attribute and `Last Name`
    Attribute, go to **System Console \> Site Configuration \> Users and
    Teams**, then set **Teammate Name Display** to **Show first and last
    name**. This is recommended for a better user experience.

Once complete, and to confirm SAML SSO is successfully enabled, switch
your system admin account from email to SAML-based authentication from
your profile picture via **Profile \> Security \> Sign-in Method \>
Switch to SAML SSO**, then log in with your SAML credentials to complete
the switch.

We also recommend that you post an announcement for your users to
explain how the migration will work.

You may also configure SAML for Okta by editing the `config.json` file
to enable SAML based on
`SAML configuration settings <saml-enterprise>`{.interpreted-text
role="ref"}. You must restart the Mattermost server for the changes to
take effect.

Configure SAML synchronization with AD/LDAP
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

In addition to configuring SAML sign-in, you can optionally configure
synchronizing SAML accounts with AD/LDAP. When configured:

- Mattermost queries AD/LDAP for relevant account information and
  updates SAML accounts based on changes to attributes (first name, last
  name, and nickname)
- Accounts disabled in AD/LDAP are deactivated in Mattermost, and their
  active sessions are revoked once Mattermost synchronizes attributes.

To configure SAML synchronization with AD/LDAP:

1. Go to **System Console \> Authentication \> SAML 2.0**, then set
    **Enable Synchronizing SAML Accounts With AD/LDAP** to **true**.

2. Go to **System Console \> Authentication \> AD/LDAP** to open the
    AD/LDAP wizard, navigate to the **Connection Settings** section,
    then set **Enable Synchronization with AD/LDAP** to **true**.

3. To ignore guest users when sychronizing, go to **System Console \>
    Authentication \> SAML 2.0**, then set **Ignore Guest Users when
    Synchronizing with AD/LDAP** to **true**.

4. Set the rest of the AD/LDAP settings based on
    `configuration settings documentation <administration-guide/configure/authentication-configuration-settings:ad/ldap>`{.interpreted-text
    role="ref"} to connect Mattermost with your AD/LDAP server.

    If you don\'t want to enable AD/LDAP sign-in, go to **System Console
    \> Authentication \> AD/LDAP** wizard, navigate to the **Connection
    Settings** section, then set **Enable sign-in with AD/LDAP** to
    **false**.

5. To specify how often Mattermost synchronizes SAML user accounts with
    AD/LDAP, go to **System Console \> Authentication \> AD/LDAP**
    wizard, navigate to the **Sync Performance** section, then set a
    **Synchronization Interval** in minutes. The default setting is 60
    minutes. If you want to synchronize immediately after disabling an
    account, go to the **Sync History** section and select **AD/LDAP
    Synchronize Now**.

6. To confirm that Mattermost can successfully connect to your AD/LDAP
    server, go to **System Console \> Authentication \> AD/LDAP**
    wizard, navigate to the **Connection Settings** section, then select
    **Test Connection**.

Once the synchronization with AD/LDAP is enabled, user attributes are
synchronized with AD/LDAP based on their email address. If a user with a
given email address doesn\'t have an AD/LDAP account, they will be
deactivated in Mattermost on the next AD/LDAP sync.

To re-activate the account:

1. Add the user to your AD/LDAP server.
2. Purge all caches in Mattermost by going to **System Console \>
    Environment \> Web Server**, then select **Purge All Caches**.
3. Run AD/LDAP synchronization by going to **System Console \>
    Authentication \> AD/LDAP** wizard, navigating to the **Sync
    History** section, then select **AD/LDAP Synchronize Now**.
4. Purge all caches again in Mattermost by going to **System Console \>
    Environment \> Web Server**, then select **Purge All Caches** again.
    This re-activates the account in Mattermost.

:::: note
::: title
Note
:::

\- If a user is deactivated from AD/LDAP, they will be deactivated in
Mattermost on the next sync. They will be shown as \"Deactivated\" in
the System Console users list, all of their sessions will expire and
they won\'t be able to log back in to Mattermost. - If a user is
deactivated from SAML, their session won\'t expire until they\'re
deactivated from AD/LDAP. However, they won\'t be able to log back in to
Mattermost. - SAML synchronization with AD/LDAP is designed to pull user
attributes such as first name and last name from your AD/LDAP, not to
control authentication. In particular, the user filter cannot be used to
control who can log in to Mattermost, this should be controlled by your
SAML service provider\'s group permissions.
::::

See
`technical description of SAML synchronization with AD/LDAP <administration-guide/onboard/sso-saml-technical>`{.interpreted-text
role="ref"} for more details.

### Override SAML data with AD/LDAP data

Alternatively, you can choose to override SAML bind data with AD/LDAP
information. For more information on binding a user with the SAML ID
Attribute, please refer to this
`documentation <administration-guide/onboard/sso-saml-okta:how to bind authentication to id attribute instead of email>`{.interpreted-text
role="ref"}.

This process overrides SAML email address with AD/LDAP email address
data or SAML Id Attribute with AD/LDAP Id Attribute if configured. We
recommend using this configuration with the SAML ID Attribute to help
ensure new users are not created when the email address changes for a
user.

To ensure existing user accounts do not get disabled in this process,
ensure the SAML IDs match the LDAP IDs by exporting data from both
systems and comparing the ID data. Mapping ID Attributes for both
AD/LDAP and SAML within Mattermost to fields that hold the same data
will ensure the IDs match as well.

1. Set the SAML `Id Attribute` by going to **System Console \>
    Authentication \> SAML 2.0 \> Id Attribute**.
2. Set **System Console \> Authentication \> SAML 2.0 \> Override SAML
    bind data with AD/LDAP information** to **true**.
3. Set **System Console \> Authentication \> SAML 2.0 \> Enable
    Synchronizing SAML Accounts With AD/LDAP** to **true**.
4. Run AD/LDAP sync by going to **System Console \> Authentication \>
    AD/LDAP** wizard, navigating to the **Sync History** section, then
    select **AD/LDAP Synchronize Now**.

.. This page is intentionally not accessible via the LHS navigation pane
because it\'s common content included on other docs pages.

## Frequently Asked Questions

### What encryption options are supported for SAML?

See the encryption options documentation for details on what
`encryption methods <deployment-guide/encryption-options:saml encryption support>`{.interpreted-text
role="ref"} Mattermost supports for SAML.

### How to bind authentication to Id attribute instead of email

Alternatively, you can use an `Id` attribute instead of email to bind
the user. We recommend choosing an ID that is unique and will not change
over time.

Configuring with an `Id` attribute allows you to reuse an email address
for a new user without the old user\'s information being exposed. For
instance, if a user with an email address <joe.smith@mattermost.com> was
once an employee, a new employee named Joe Smith can use the same email.
This configuration is also useful when a user\'s name changes and their
email needs to be updated.

This process was designed with backwards compatibility to email binding.
Here is the process applied to new account creations and to accounts
logging in after the configuration:

- A user authenticated with SAML is bound to the SAML service user using
  the Id Attribute (as long as it has been configured) or bound by email
  using the email received from SAML.
- When the user tries to login and the SAML server responds with a valid
  authentication, then the server uses the \"Id\" field of the SAML
  authentication to search the user.
- If a user bound to that ID already exists, it logs in as that user.
- If a user bound to that ID does not exist, it will search base on the
  email.
- If a user bound to the email exists, it logs in with email and updates
  the autentication data to the ID, instead of the email.
- If a user bound to the ID or email does not exist, it will create a
  new Mattermost account bound to the SAML account by ID and will allow
  the user to log in.

:::: note
::: title
Note
:::

Existing accounts won\'t update until they log in to the server.
::::

### Can SAML via Microsoft ADFS be configured with Integrated Windows Authentication (IWA)?

Yes. IWA is supported on the browser, with support added to iOS and
Android mobile apps in Q2/2019 (mobile apps v1.18 and later).

However, IWA is not supported on the Mattermost Desktop Apps due to a
limitation in Electron. As a workaround you may create a browser desktop
shortcut for quick access to Mattermost, just like a Desktop App.

### Can I provision and deprovision users who log in via SAML?

Yes, but this relies on AD/LDAP to do so. Currently, we do not support
SCIM. See
`"How do I deactivate users?" <administration-guide/onboard/ad-ldap:how do i deactivate users?>`{.interpreted-text
role="ref"} for more information.

### How do I migrate users from one authentication method (e.g. email) to SAML?

See the
`mmctl user migrate-auth <administration-guide/manage/mmctl-command-line-tool:mmctl user migrate-auth>`{.interpreted-text
role="ref"} command documentation for details.

### How is SAML different from OAuth 2.0 and OpenId Connect?

OAuth 2.0 was primarily intended for delegated authorization, where an
app is authorized to access resources, such as Google contact list. It
doesn't deal with authentication.

OpenID Connect is built on top of OAuth 2.0, which supports
authentication and thus direct SSO.

SAML is like OpenID Connect, except typically used in enterprise
settings. OpenID Connect is more common in consumer websites and
web/mobile apps.

Learn more at
<https://hackernoon.com/demystifying-oauth-2-0-and-openid-connect-and-saml-12aa4cf9fdba>.
