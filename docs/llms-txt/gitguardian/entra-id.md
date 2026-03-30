# Source: https://docs.gitguardian.com/platform/enterprise-administration/sso-providers/entra-id.md

# Microsoft Entra ID

> Configure SAML-based Single Sign-On (SSO) with Microsoft Entra ID for GitGuardian.

:::tip
GitGuardian also supports SCIM provisioning for Microsoft Entra ID. See the [SCIM configuration guide](../scim-configuration) for setup instructions.
:::

1. First, go to the [Microsoft Entra admin center](https://entra.microsoft.com/), click on "Add enterprise application" at the bottom of the page, then "Create your own application".
2. In the new panel that appears on the right, provide a name (e.g. "GitGuardian") and select "Integrate any other application you don't find in the gallery (Non-gallery)". Finally, click on the "Create" button.
   ![entra-id start](/img/platform/enterprise-administration/sso-providers/entra_id_start.png)
3. After a few seconds, you will be redirected to your newly created application. Click on "Set up single sign on" and choose the SAML sign-on method.
   ![entra-id select sso](/img/platform/enterprise-administration/sso-providers/entra_id_select_sso.png)
4. Now, you need to configure the Service Provider in Microsoft Entra ID. Click on Edit in the "Basic SAML Configuration" box. Use these values:
   - `Identifier (Entity Id)` field is filled with the `SP Entity ID` value on GitGuardian dashboard.
   - `Reply URL (Assertion Consumer Service URL)` field is filled with the `ACS URL` value on GitGuardian dashboard.
      Don't forget to click on "Save".
      ![entra-id setup sp](/img/platform/enterprise-administration/sso-providers/entra_id_setup_sp.png)
5. Now, some mappings need to be done. Select 'Edit' on the 'Attributes & Claims' box. Click on 'Add new claim'. Leave 'Namespace' empty and use these values:
   - Name: `first_name` + Source attribute: `user.givenname`
      Don't forget to click on "Save".
      ![entra-id mapping first_name](/img/platform/enterprise-administration/sso-providers/entra_id_mapping_first_name.png)
   - Name: `last_name` + Source attribute: `user.surname`
      Don't forget to click on "Save".
      ![entra-id mapping last_name](/img/platform/enterprise-administration/sso-providers/entra_id_mapping_last_name.png)
6. You also need to make sure that the Unique User Identifier (Name ID) claim is set to user.mail.
   ![entra-id userid](/img/platform/enterprise-administration/sso-providers/entra_id_userid.png)
7. Then, setup how responses and assertions are signed: Select 'Edit' on the 'SAML Certificates' box and choose 'Sign SAML response and assertion' as Signing Option and 'SHA-256' as Signing Algorithm:
   ![entra-id signature](/img/platform/enterprise-administration/sso-providers/entra_id_signature.png)
8. Now, you need to configure the Identity Provider in GitGuardian dashboard. Use these values:
   - `Entity Id` field is filled with the `Microsoft Entra Identifier`
   - `Single Sign-On URL` field is filled with the `Login URL`
   - `X509 Cert` field is filled with the certificate. Download the Base64 certificate, use `cat` and copy/paste the plaintext value.
   - Ensure that the checkbox **I have mapped the attributes first_name and last_name in my IdP** is checked
     ![entra-id idp config](/img/platform/enterprise-administration/sso-providers/entra_id_idp_config.png)
9. Test your app configuration by clicking on "Test".
10. **Important:** Don't forget to [reserve your email domain](../saml-sso-configuration#email-domain-reservation) to enable automatic SSO discovery.
