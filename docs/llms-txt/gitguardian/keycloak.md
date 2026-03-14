# Source: https://docs.gitguardian.com/platform/enterprise-administration/sso-providers/keycloak.md

# Keycloak

> Configure SAML-based Single Sign-On (SSO) with Keycloak for GitGuardian.

1. Navigate to "Realm Settings" under the "General" tab in Keycloak, and copy the 'SAML 2.0 Identity Provider Metadata'. For example: `https://$YOUR_KEYCLOAK_DOMAIN/realms/master/protocol/saml/descriptor`.

   ![keycloak realm endpoint](/img/platform/enterprise-administration/sso-providers/keycloak_realm_endpoint.png)

2. Go to the "Keys" tab, and click on the 'Certificate' button next to the RS256 algorithm. Copy the displayed certificate.

   ![keycloak realm certificate](/img/platform/enterprise-administration/sso-providers/keycloak_realm_certificate.png)

3. To configure the Identity Provider in the GitGuardian dashboard, use the following values:
   - The `Entity Id` field should be filled with the Keycloak SAML 2.0 Identity Provider Metadata URL, excluding `/protocol/saml/descriptor` from the end. Example: `https://$YOUR_KEYCLOAK_DOMAIN/realms/master`.
   - The `Single Sign-On URL` field should include the Keycloak SAML 2.0 Identity Provider URL, excluding `/descriptor` from the end. Example: `https://$YOUR_KEYCLOAK_DOMAIN/realms/master/protocol/saml`.
   - In the `X509 Cert` field, paste the certificate copied in the previous step.
   - Ensure that the checkbox **I have mapped the attributes first_name and last_name in my IdP** is checked.
4. To configure the "Client" (Service Provider) in Keycloak:
   - Navigate to the Clients menu and click on 'Create client'. Use the following values:
     - Set the `Client type` field to `SAML`.
     - Fill the `Client ID` field with the `SP Entity ID` from the GitGuardian dashboard.
   - Click on 'Next', then:
     - Fill the `Home URL` field with the URL of your GitGuardian dashboard. For example: `https://dashboard.gitguardian.com` (SaaS) or `https://gitguardian.mycorp.local` (Self-Hosted).
     - Fill the `Valid Redirect URIs` and `Master SAML Processing URL` fields with the `ACS URL`.
5. Click on 'Save', then configure these settings on the newly created client:
   - In 'SAML capabilities', set the `Name ID Format` to `email`.
   - Set `Force POST Binding` and `Include AuthnStatement` to `ON`.
   - In 'Signature and Encryption', set `Sign documents` and `Sign assertions` fields to `ON`.
   - `Signature algorithm` should be `RSA_SHA256`.
   - Set `SAML signature key name` to `NONE`.
   - In 'Logout settings', set `Front Channel Logout` to `ON`.
   - Click on 'Save'.
   - In the 'Keys' tab, set `Client signature required` to `OFF`.

   ![keycloak clients](/img/platform/enterprise-administration/sso-providers/keycloak_clients.png)

6. Still in the same client, under the 'Client scopes' tab, edit the 'Dedicated scope and mappers for this client' and configure a new mapper for the first name:
   - Choose `User Property` as the `Mapper Type`.
   - The `Name` field should be `firstName`.
   - The `Property` field should be `firstName`.
   - Set the `SAML Attribute Name` to `first_name` and the `SAML Attribute NameFormat` to `Basic`.
7. For the last name, create a second mapper:
   - Again, select `User Property` for the `Mapper Type`.
   - The `Name` field should be `lastName`.
   - The `Property` field should be `lastName`.
   - Set the `SAML Attribute Name` to `last_name` and the `SAML Attribute NameFormat` to `Basic`.

   ![keycloak mappers](/img/platform/enterprise-administration/sso-providers/keycloak_mappers.png)

8. In the "Client Scopes" tab, note the 'Assigned Default Client Scopes'. For example, `role_list`.

   ![keycloak client scopes](/img/platform/enterprise-administration/sso-providers/keycloak_client_scopes.png)

9. Edit the client scope(s) listed in the previous step by navigating to the "Client Scopes" menu. Go to the "Mappers" tab, edit the Role list mapper, and ensure the `Single Role Attribute` field is set to `ON`.

   ![keycloak client scopes Single Role Attribute](/img/platform/enterprise-administration/sso-providers/keycloak_client_scopes_single_role_attribute.png)

10. Finalize your setup by testing the SSO authentication using the `Login URL` provided in the GitGuardian dashboard [SAML configuration page](https://dashboard.gitguardian.com/settings/workspace/auth/saml).
11. **Important:** Don't forget to [reserve your email domain](../saml-sso-configuration#email-domain-reservation) to enable automatic SSO discovery.
