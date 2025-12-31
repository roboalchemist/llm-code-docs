# Source: https://infisical.com/docs/documentation/platform/sso/keycloak-saml.md

# Keycloak SAML

> Learn how to configure Keycloak SAML for Infisical SSO.

<Info>
  Keycloak SAML SSO is a paid feature.

  If you're using Infisical Cloud, then it is available under the **Pro Tier**. If you're self-hosting Infisical,
  then you should contact [sales@infisical.com](mailto:sales@infisical.com) to purchase an enterprise license to use it.
</Info>

<Steps>
  <Step title="Prepare the SAML SSO configuration in Infisical">
    In Infisical, head to the **Single Sign-On (SSO)** page and select the **General** tab. Click **Connect** for **SAML** under the Connect to an Identity Provider section. Select **Keycloak**, then click **Connect** again.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/connect-saml.png" alt="SSO connect section" />

    Next, copy the **Valid redirect URI** and **SP Entity ID** to use when configuring the Keycloak SAML application.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/init-config.png" alt="Keycloak SAML initial configuration" />
  </Step>

  <Step title="Create a SAML client application in Keycloak">
    2.1. In your realm, navigate to the **Clients** tab and click **Create client** to create a new client application.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/clients-list.png" alt="SAML keycloak list of clients" />

    <Info>
      You don’t typically need to make a realm dedicated to Infisical. We recommend adding Infisical as a client to your primary realm.
    </Info>

    In the General Settings step, set **Client type** to **SAML**, the **Client ID** field to `https://app.infisical.com`, and the **Name** field to a friendly name like **Infisical**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/create-client-general-settings.png" alt="SAML keycloak create client general settings" />

    <Info>
      If you’re self-hosting Infisical, then you will want to replace [https://app.infisical.com](https://app.infisical.com) with your own domain.
    </Info>

    Next, in the Login Settings step, set both the **Home URL** field and **Valid redirect URIs** field to the **Valid redirect URI** from step 1 and press **Save**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/create-client-login-settings.png" alt="SAML keycloak create client login settings" />

    2.2. Once you've created the client, under its **Settings** tab, make sure to set the following values:

    * Under **SAML Capabilities**:
      * Name ID format: email (or username).
      * Force name ID format: On.
      * Force POST binding: On.
      * Include AuthnStatement: On.
    * Under **Signature and Encryption**:
      * Sign documents: On.
      * Sign assertions: On.
      * Signature algorithm: RSA\_SHA256.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-saml-capabilities.png" alt="SAML keycloak client SAML capabilities" />

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-signature-encryption.png" alt="SAML keycloak client signature encryption" />

    2.3. Next, navigate to the **Client scopes** tab select the client's dedicated scope.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-scopes-list.png" alt="SAML keycloak client scopes list" />

    Next click **Add predefined mapper**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-mappers-empty.png" alt="SAML keycloak client mappers empty" />

    Select the **X500 email**, **X500 givenName**, and **X500 surname** attributes and click **Add**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-mappers-predefined.png" alt="SAML keycloak client mappers predefined" />

    Now click on the **X500 email** mapper and set the **SAML Attribute Name** field to **email**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-mappers-email.png" alt="SAML keycloak client mappers email" />

    Repeat the same for **X500 givenName** and **X500 surname** mappers, setting the **SAML Attribute Name** field to **firstName** and **lastName** respectively.

    Next, back in the client scope's **Mappers**, click **Add mapper** and select **by configuration**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-mappers-by-configuration.png" alt="SAML keycloak client mappers by configuration" />

    Select **User Property**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-mappers-user-property.png" alt="SAML keycloak client mappers user property" />

    Set the the **Name** field to **Username**, the **Property** field to **username**, and the **SAML Attribute Name** to **username**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-mappers-username.png" alt="SAML keycloak client mappers username" />

    Repeat the same for the `id` attribute, setting the **Name** field to **ID**, the **Property** field to **id**, and the **SAML Attribute Name** to **id**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-mappers-id.png" alt="SAML keycloak client mappers id" />

    Once you've completed the above steps, the list of mappers should look like this:

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/client-mappers-completed.png" alt="SAML keycloak client mappers completed" />
  </Step>

  <Step title="Retrieve Identity Provider (IdP) Information from Keycloak">
    Back in Keycloak, navigate to Configure > Realm settings > General tab > Endpoints > SAML 2.0 Identity Provider Metadata and copy the IDP URL. This should appear in various places and take the form: `https://keycloak-mysite.com/realms/myrealm/protocol/saml`.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/realm-saml-metadata.png" alt="SAML keycloak realm SAML metadata" />

    Also, in the **Keys** tab, locate the RS256 key and copy the certificate to use when finishing configuring Keycloak SAML in Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/realm-settings-keys.png" alt="SAML keycloak realm settings keys" />
  </Step>

  <Step title="Finish configuring SAML in Infisical">
    Back in Infisical, set **IDP URL** and **Certificate** to the items from step 3. Also, set the **Client ID** to the `https://app.infisical.com`.

    Once you've done that, press **Update** to complete the required configuration.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/idp-values.png" alt="SAML Okta paste values into Infisical" />
  </Step>

  <Step title="Enable SAML SSO in Infisical">
    Enabling SAML SSO allows members in your organization to log into Infisical via Keycloak.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/keycloak/enable-saml.png" alt="SAML keycloak enable SAML" />
  </Step>

  <Step title="Enforce SAML SSO in Infisical">
    Enforcing SAML SSO ensures that members in your organization can only access Infisical
    by logging into the organization via Keycloak.

    To enforce SAML SSO, you're required to test out the SAML connection by successfully authenticating at least one Keycloak user with Infisical;
    Once you've completed this requirement, you can toggle the **Enforce SAML SSO** button to enforce SAML SSO.

    <Warning>
      We recommend ensuring that your account is provisioned the application in Keycloak
      prior to enforcing SAML SSO to prevent any unintended issues.
    </Warning>

    <Info>
      In case of a lockout, an organization admin can use the [Admin Login Portal](https://infisical.com/docs/documentation/platform/sso/overview#admin-login-portal) in the `/login/admin` path e.g. [https://app.infisical.com/login/admin](https://app.infisical.com/login/admin).
    </Info>
  </Step>
</Steps>

<Tip>
  If you are only using one organization on your Infisical instance, you can configure a default organization in the [Server Admin Console](../admin-panel/server-admin#default-organization) to expedite SAML login.
</Tip>

<Note>
  If you're configuring SAML SSO on a self-hosted instance of Infisical, make
  sure to set the `AUTH_SECRET` and `SITE_URL` environment variable for it to
  work:

  <div class="height:1px;" />

  * `AUTH_SECRET`: A secret key used for signing and verifying JWT. This
    can be a random 32-byte base64 string generated with `openssl rand -base64
        32`.

  <div class="height:1px;" />

  * `SITE_URL`: The absolute URL of your self-hosted instance of Infisical including the protocol (e.g. [https://app.infisical.com](https://app.infisical.com))
</Note>
