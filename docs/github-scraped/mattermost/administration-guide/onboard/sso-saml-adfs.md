# Configure SAML with Microsoft ADFS for Windows Server 2012

The following process provides steps to configure SAML 2.0 with
Microsoft ADFS for Mattermost.

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

The following are basic requirements to use ADFS for Mattermost:

:   - An Active Directory instance where all users have a specified
      email and username attributes. For Mattermost servers running 3.3
      and earlier, users must also have their first name and last name
      attributes specified.
    - A Microsoft Server running. The screenshots used in this guide are
      from Microsoft Server 2012R2, but similar steps should work for
      other versions.
    - An SSL certificate to sign your ADFS login page.
    - ADFS installed on your Microsoft Server. You can find a detailed
      guide for deploying and configuring ADFS in [this Microsoft
      article](https://learn.microsoft.com/en-us/previous-versions/dynamicscrm-2016/deployment-administrators-guide/gg188612(v=crm.8)?redirectedfrom=MSDN).

On your ADFS installation, note down the value of the **SAML
2.0/W-Federation URL** in ADFS Endpoints section, also known as the
**SAML SSO URL Endpoint** in this guide. If you chose the defaults for
the installation, this will be `/adfs/ls/`.

## Add a relying party trust

1. In the ADFS management sidebar, go to **AD FS \> Trust Relationships
    \> Relying Party Trusts**, then select **Add Relying Party Trust**.
    A configuration wizard opens for adding a new relying party trust.

    > ![image](../../images/adfs_1_add_new_relying_party_trust.png)

2. On the **Welcome** screen, select **Start**.

    > ![image](../../images/adfs_2_start_wizard.png)

3. On the **Select Data Source** screen, select **Enter data about the
    relying party manually**.

    > ![image](../../images/adfs_3_select_data_source.png)

4. On the **Specify Display Name** screen, enter a **Display Name** to
    recognize the trust, such as `Mattermost`, then add any notes you
    want to make.

    > ![image](../../images/adfs_4_specify_display_name.png)

5. On the **Choose Profile** screen, select **AD FS profile**.

    > ![image](../../images/adfs_5_choose_profile.png)

6. On the **Configure Certificate** screen, leave the certificate
    settings at their default values.

    > ![image](../../images/adfs_6_configure_certificate_default.png)

However, if you would like to set up encryption for your SAML
connection, select **Browse**, then upload your Service Provider Public
Certificate.

> ![image](../../images/adfs_7_configure_certificate_encryption.png)

1. On the **Configure URL** screen, select **Enable Support for the
    SAML 2.0 WebSSO protocol**, then enter the **SAML 2.0 SSO service
    URL**, similar to `https://<your-mattermost-url>/login/sso/saml`
    where `<your-mattermost-url>` should typically match the
    `Mattermost Site URL <administration-guide/configure/environment-configuration-settings:site url>`{.interpreted-text
    role="ref"}.

    > ![image](../../images/adfs_8_configure_url.png)

2. On the **Configure Identifiers** screen, enter the **Relying party
    trust identifier** (also known as the **Identity Provider Issuer
    URL**) of the form `https://<your-idp-url>/adfs/services/trust`,
    then click **Add**.

    > ![image](../../images/adfs_9_configure_identifiers.png)

3. On the **Configure Multi-factor Authentication Now** screen, you may
    enable multi-factor authentication. This is beyond the scope of this
    documentation.

    > ![image](../../images/adfs_10_configure_mfa.png)

4. On the **Choose Issuance Authorization Rules** screen, select
    **Permit all users to access this relying party**.

    ![image](../../images/adfs_11_authorization.png)

5. On the **Ready to Add Trust** screen, review your settings.

    ![image](../../images/adfs_12_ready_to_add_trust.png)

6. On the **Finish** screen, select **Open the Edit Claim Rules dialog
    for this relying party trust when the wizard closes**, then select
    **Close**. You exit the configuration wizard, and a **Claim Rules**
    editor opens.

    ![image](../../images/adfs_13_finish_trust.png)

## Create claim rules

1. In the **Issuance Transform Rules** section of the **Claim Rules**
    editor, select **Add Rule...** to open an **Add Transform Claim Rule
    Wizard**.

    > ![image](../../images/adfs_14_claim_rules_editor.png)

2. On the **Choose Rule Type** screen, select **Send LDAP Attributes as
    Claims** from the drop-down menu, then select **Next**.

    > ![image](../../images/adfs_15_choose_rule_type.png)

3. In the **Configure Claim Rule** screen, enter a **Claim Rule Name**
    of your choice, select **Active Directory** as the **Attribute
    Store**, then complete the following:

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

Note that the entries in the **Outgoing Claim Type** column can be
chosen to be something else. They can contain dashes but no spaces. They
will be used to map the corresponding fields in Mattermost later.

> ![image](../../images/adfs_16_configure_claim_rule.png)

1. Create another new rule by selecting **Add Rule**.

2. On the **Choose Rule Type** screen, select **Transform an Incoming
    Claim** from the drop-down menu, then select **Next**.

    > ![image](../../images/adfs_17_transformation_of_incoming_claim.png)

3. On the **Configure Claim Rule** screen, enter a **Claim Rule Name**
    of your choice, then:

> - Select **Name ID** for the **Incoming claim type**.
> - Select **Unspecified** for the **Incoming name ID format**.
> - Select **E-Mail Address** for the **Outgoing claim type**.

Select **Pass through all claim values**, then select **Finish**.

> ![image](../../images/adfs_18_configure_incoming_claim.png)

1. Select **Finish** to create the claim rule, then select **OK** to
    finish creating rules.
2. Open Windows PowerShell as an administrator, then run the following
    command:

> `Set-ADFSRelyingPartyTrust -TargetName <display-name> -SamlResponseSignature "MessageAndAssertion"`

where `<display-name>` is the name you specified in step 4 when adding a
relying party trust. In this example, `<display-name>` would be
`mattermost`.

This action adds the signature to SAML messages, making verification
successful.

## Export identity provider certificate

Next, export the identity provider certificate, which will be later
uploaded to Mattermost to finish SAML configuration.

1. In the ADFS management sidebar, go to **AD FS \> Service \>
    Certificates**, then double click on the certificate under
    **Token-signing**. Alternatively, you can right-click on the field,
    then select **View Certificate**.

    > ![image](../../images/adfs_19_export_idp_cert_start.png)

2. On the **Certificate** screen, go to the **Details** tab, then
    select **Copy to File**, followed by **OK**. This opens a
    **Certificate Export Wizard**.

    > ![image](../../images/adfs_20_export_idp_cert_copy.png)

3. On the **Certificate Export Wizard** screen, select **Next**, then,
    select the option **Base-64 encoded X.509 (.CER)**, and select
    **Next** again.

    > ![image](../../images/adfs_21_export_idp_cert_wizard.png)

4. On the **Certificate Export Wizard** screen, select **Browse** to
    specify the location where you want the Identity Provider
    Certificate to be exported, then specify the file name.

    > ![image](../../images/adfs_21-2_export_idp_cert_wizard.png)

5. Select **Save**. In the **Certificate Export Wizard** screen, verify
    the file path is correct, then select **Next**.

6. In the **Completing the Certificate Export Wizard**, select
    **Finish**, then select **OK** to confirm the export was successful.

    > ![image](../../images/adfs_21-3_export_idp_cert_wizard.png)

## Configure SAML Sign-On for Mattermost

Create a metadata URL by appending
\"FederationMetadata/2007-06/FederationMetadata.xml\" to the root URL of
the ADFS server, for example:
`https://<adfs.domain.com>/federationmetadata/2007-06/FederationMetadata.xml>`.

Next, start the Mattermost server and log in to Mattermost as a system
admin. Go to **System Console \> Authentication \> SAML**, paste the
metadata URL in the **Identity Provider Metadata URL** field, then
select **Get SAML Metadata from IdP**.

This populates the **SAML SSO URL** and the **Identity Provider Issuer
URL** fields automatically. The Identity Provider Public Certificate is
also downloaded from the server and set locally.

Alternatively you can enter the following fields manually:

:   - **SAML SSO URL**: **SAML 2.0/W-Federation URL** ADFS Endpoint you
      copied earlier.

    - **Identity Provider Issuer URL**: `Relying party trust identifier`
      from ADFS you specified earlier.

    - **Identity Provider Public Certificate**:
      `X.509 Public Certificate` you downloaded earlier.

      ![image](../../images/adfs_22_mattermost_basics.png)

2.  Configure Mattermost to verify the signature. The **Service Provider
    Login URL** is the SAML 2.0 SSO service URL you specified in ADFS
    earlier.

    > ![image](../../images/adfs_23_mattermost_verification.png)

3.  Enable encryption by uploading the Service Provider Private Key and
    Service Provider Public Certificate you generated earlier.

    > ![image](../../images/adfs_24_mattermost_encryption.png)

4.  Configure Mattermost to sign SAML requests using the Service
    Provider Private Key.

1. Set attributes for the SAML Assertions, which will be used to update
    user information in Mattermost. Attributes for email and username
    are required and should match the values you entered in ADFS
    earlier. See
    `documentation on SAML configuration settings <saml-enterprise>`{.interpreted-text
    role="ref"} for more detail.

For Mattermost servers running 3.3 and earlier, the `FirstName` and
`LastName` attributes are also required fields.

> ![image](../../images/adfs_25_mattermost_attributes.png)

1. (Optional) Customize the login button text.

> ![image](../../images/adfs_26_mattermost_login_button.png)

1. Select **Save**.
2. (Optional) If you configured a `FirstName` and `LastName` Attribute,
    go to **System Console \> Site Configuration \> Users and Teams**,
    then set **Teammate Name Display** to **Show first and last name**.
    This is recommended for a better user experience.

If you'd like to confirm SAML SSO is successfully enabled, switch your
system admin account from email to SAML-based authentication from your
profile picture via **Profile \> Security \> Sign-in Method \> Switch to
SAML SSO**, then log in with your SAML credentials to complete the
switch.

We recommend that you post an announcement about how the migration will
work for your users.

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
