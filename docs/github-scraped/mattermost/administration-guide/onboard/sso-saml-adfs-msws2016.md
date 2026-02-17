# Configure SAML with Microsoft ADFS using Microsoft Windows Server 2016

This document provides steps to configure SAML 2.0 with Microsoft ADFS
for Mattermost and Microsoft Windows Server 2016.

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

## Prerequisites

- An Active Directory instance where all users have specified email and
  username attributes. For Mattermost servers running 3.3 and earlier,
  users must also have their first name and last name attributes
  specified.
- A running Microsoft Server. The screenshots used in this guide are
  from Microsoft Server 2012R2, but similar steps should work for other
  versions.
- An SSL certificate to sign your ADFS login page.
- ADFS installed on your Microsoft Server. You can find a detailed guide
  for deploying and configuring ADFS in [this Microsoft
  article](https://learn.microsoft.com/en-us/previous-versions/dynamicscrm-2016/deployment-administrators-guide/gg188612(v=crm.8)?redirectedfrom=MSDN).

On your ADFS installation, open the ADFS console. Select **Service**,
then select **Endpoints**. In the **Type** column, search for
`SAML 2.0/WS-Federation` and note down the value of **URL Path** column.
This is also known as the **SAML SSO URL Endpoint** in this guide. If
you chose the defaults for the installation, this will be `/adfs/ls`.

## Add a relying party trust

1. Open the ADFS management snap-in, then select **AD FS \> Relying
    Party Trusts \> Add Relying Party Trust** from the right sidebar.
    You can also right-click **Relying Party Trusts**, then select **Add
    Relying Party Trust** from the context menu.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_000.png)

2. On the **Welcome** screen of the configuration wizard, select
    **Claims aware**, then select **Start**.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_001.png)

3. On the **Select Data Source** screen, select **Enter data about the
    relying party manually**.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_002.png)

4. On the **Specify Display Name** screen, enter a **Display Name**
    (e.g., `Mattermost`). You can add optional notes.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_003.png)

5. On the **Configure Certificate** screen, leave the certificate
    settings at their default values.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_004.png)

If you would like to set up encryption for your SAML connection, select
**Browse**, then upload your Service Provider Public Certificate.

> ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_005.png)

1. On the **Configure URL** screen, select **Enable Support for the
    SAML 2.0 WebSSO protocol**, then enter the **SAML 2.0 SSO service
    URL** in the following
    format:`https://<your-mattermost-url>/login/sso/saml` where
    `<your-mattermost-url>` should typically match the
    `Mattermost Site URL <administration-guide/configure/environment-configuration-settings:site url>`{.interpreted-text
    role="ref"}.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_006.png)

2. On the **Configure Identifiers** screen, enter the **Relying party
    trust identifier**. This identifies the claims being requested. The
    **SAML 2.0 SSO service URL** format should be
    `https://<your-mattermost-url>/login/sso/saml` where
    `<your-mattermost-url>` matches your
    `Mattermost Site URL <administration-guide/configure/environment-configuration-settings:site url>`{.interpreted-text
    role="ref"}. Then choose **Next**.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_007.png)
    >
    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_008.png)

This string must match the **Service Provider Identifier** string. For
more information about the Relying party trust identifier and how prefix
matching is applied see [this
documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/how-uris-are-used-in-ad-fs).

Add your **SAML 2.0 SSO service URL** using this same process.

1. On the **Choose Access Control Policy** screen, select the access
    control policy suitable for your environment. This guide assumes the
    default values **Permit everyone** and an unchecked box.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_009.png)

2. On the **Ready to Add Trust** screen, review your settings.

    > ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_010.png)

3. On the **Finish** screen, select **Configure claims issuance policy
    for this application**, then select **Close**.

    ![image](../../images/SSO-SAML-ADFS_add-new-relying-party-trust_011.png)

## Create claim rules

1. In the **Issuance Transform Rules** tab of the **Claim Rules**
    editor, select **Add Rule...**.

    > ![image](../../images/SSO-SAML-ADFS_create-claim-rules_001.png)

2. On the **Choose Rule Type** screen, select **Send LDAP Attributes as
    Claims** from the drop-down menu, then select **Next**.

    > ![image](../../images/SSO-SAML-ADFS_create-claim-rules_002.png)

3. On the **Configure Claim Rule** screen, enter a **Claim Rule Name**
    of your choice, select **Active Directory** as the **Attribute
    Store**, then add the following mapping:

> - From the **LDAP Attribute column**, select `E-Mail-Addresses`. From
>   the **Outgoing Claim Type**, type `Email`.
> - From the **LDAP Attribute column**, select `E-Mail-Addresses`. From
>   the **Outgoing Claim Type**, type `Name ID`.
> - From the **LDAP Attribute column**, select `Given-Name`. From the
>   **Outgoing Claim Type**, type `FirstName`.
> - From the **LDAP Attribute column**, select `Surname`. From the
>   **Outgoing Claim Type**, type `LastName`.
> - From the **LDAP Attribute column**, select `SAM-Account-Name`. From
>   the **Outgoing Claim Type**, type `Username`.

The `FirstName` and `LastName` attributes are optional.

Select **Finish** to add the rule.

The entries in the **Outgoing Claim Type** column can be modified. The
entries may contain dashes but no spaces. They are used to map the
corresponding fields in Mattermost.

> ![image](../../images/SSO-SAML-ADFS_create-claim-rules_003.png)

1. Select **Add Rule** to create another new rule.

2. On the **Choose Rule Type** screen, select **Transform an Incoming
    Claim** from the drop-down menu, then select **Next**.

    > ![image](../../images/SSO-SAML-ADFS_create-claim-rules_004.png)

3. On the **Configure Claim Rule** screen, enter a **Claim Rule Name**
    of your choice, then:

> - Select **Name ID** for the **Incoming claim type**
> - Select **Unspecified** for the **Incoming name ID format**
> - Select **E-Mail Address** for the **Outgoing claim type**

Select **Pass through all claim values**, then select **Finish**.

> ![image](../../images/SSO-SAML-ADFS_create-claim-rules_005.png)

1. Select **Finish** to create the claim rule, then select **OK** to
    finish creating rules.
2. Open Windows PowerShell as an administrator, then run the following
    command:

> `Set-ADFSRelyingPartyTrust -TargetName <display-name> -SamlResponseSignature "MessageAndAssertion"`

where `<display-name>`is the name you specified in step 4 when you added
a relying party trust. In this example, `<display-name>` would be
`mattermost`.

This action adds the signature to SAML messages, making verification
successful.

## Export identity provider certificate

Next, export the identity provider certificate, which will be later
uploaded to Mattermost to finish SAML configuration.

1. Open the ADFS management snap-in, select **AD FS \> Service \>
    Certificates**, then double-click on the certificate under
    **Token-signing**. You can also right-click the field, then select
    **View Certificate** in the context menu.

    > ![image](../../images/SSO-SAML-ADFS_export-id-provider-cert_001.png)

2. On the **Certificate** screen, open the **Details** tab, select
    **Copy to File**, then select **OK**.

    > ![image](../../images/SSO-SAML-ADFS_export-id-provider-cert_003.png)

3. On the **Certificate Export Wizard** screen, select **Next**.

    > ![image](../../images/SSO-SAML-ADFS_export-id-provider-cert_004.png)

4. Select **Base-64 encoded X.509 (.CER)**, then select **Next** again.

    > ![image](../../images/SSO-SAML-ADFS_export-id-provider-cert_005.png)

5. On the **Certificate Export Wizard** screen, select **Browse** to
    specify the location where you want the Identity Provider
    Certificate to be exported, then specify the file name.

    > ![image](../../images/SSO-SAML-ADFS_export-id-provider-cert_006.png)

6. Select **Save**. On the **Certificate Export Wizard** screen, verify
    the file path is correct, then select **Next**.

7. In the **Completing the Certificate Export Wizard**, select
    **Finish**, then select **OK** to confirm the export was successful.

    > ![image](../../images/SSO-SAML-ADFS_export-id-provider-cert_007.png)

## Configure SAML Sign-On for Mattermost

Create a metadata URL by appending
\"FederationMetadata/2007-06/FederationMetadata.xml\" to the root URL of
the ADFS server, for example:
`https://<adfs.domain.com>/federationmetadata/2007-06/FederationMetadata.xml>`.

Next, start the Mattermost server, then log in to Mattermost as a system
admin. Go to **System Console \> Authentication \> SAML**, paste the
metadata URL in the **Identity Provider Metadata URL** field, then
select **Get SAML Metadata from IdP**.

This populates the **SAML SSO URL** and the **Identity Provider Issuer
URL** fields automatically. The Identity Provider Public Certificate is
also downloaded from the server and set locally.

The following fields can be selected:

:   - Set **Enable Login With SAML 2.0** to **true**.
    - Set **Enable Synchronizing SAML Accounts With AD/LDAP** to suit
      your environment.
    - Set **Override SAML bind data with AD/LDAP information** to suit
      your environment.

If you don\'t plan to use a metadata URL, you can manually enter the following fields:

:   - For **SAML SSO URL** use the
      `SAML 2.0/W-Federation URL ADFS Endpoint` you copied at the
      beginning of the process.

    - For **Identity Provider Issuer URL** use the
      `Relying party trust identifier` from ADFS.

    - For **Identity Provider Public Certificate** use
      the`X.509 Public Certificate`.

      ![image](../../images/SSO-SAML-ADFS_configure-saml_001.png)

2.  Configure Mattermost to verify the signature.

> - Set **Verify Signature** to `true`.
>
> - For **Service Provider Login URL** use the
>   `SAML 2.0 SSO service URL` you specified in ADFS.
>
>   ![image](../../images/SSO-SAML-ADFS_configure-saml_002.png)

1. Enable encryption.

> - Set **Enable Encryption** to `true`.
>
> - For **Service Provider Private Key** use the Service Provider
>   Private Key generated at the start of this process.
>
> - For **Service Provider Public Certificate** use the Service Provider
>   Public Certificate you generated at the start of this process.
>
> - Set **Sign Request** to suit your environment.
>
>   ![image](../../images/SSO-SAML-ADFS_configure-saml_003.png)

1. Set attributes for the SAML Assertions, which will be used to update
    user information in Mattermost. Attributes for email and username
    are required and should match the values you entered in ADFS
    earlier. See
    `documentation on SAML configuration settings <saml-enterprise>`{.interpreted-text
    role="ref"} for more detail.

For Mattermost servers running 3.3 and earlier, the first name and last
name attributes are also required fields.

> ![image](../../images/SSO-SAML-ADFS_configure-saml_004.png)

1. Select **Save**.
2. (Optional) If you configured `First Name` Attribute and the
    `Last Name` Attribute, go to **System Console \> Site Configuration
    \> Users and Teams**, then set **Teammate Name Display** to **Show
    first and last name**. This is recommended for a better user
    experience.

You're done! If you'd like to confirm SAML SSO is successfully enabled,
switch your system admin account from email to SAML-based authentication
from your profile picture via **Profile \> Security \> Sign-in Method \>
Switch to SAML SSO**, then log in with your SAML credentials to complete
the switch.

We also recommend that you post an announcement about how the migration
will work to your users.

You may also configure SAML for ADFS by editing the `config.json` file
to enable SAML based on
`SAML configuration settings <saml-enterprise>`{.interpreted-text
role="ref"}. You must restart the Mattermost server for the changes to
take effect.

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
