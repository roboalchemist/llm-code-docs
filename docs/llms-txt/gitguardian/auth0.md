# Source: https://docs.gitguardian.com/platform/enterprise-administration/sso-providers/auth0.md

# Auth0

> Configure SAML-based Single Sign-On (SSO) with Auth0 for GitGuardian.

1. First, go to your dashboard, select "Application", and click on "Create Application"
2. Choose "Regular Web Applications" as type and a name.
   ![auth0 create app](/img/platform/enterprise-administration/sso-providers/auth0_create_app.png)
3. Go to your application addons. Click on "SAML2 Web App" and then on "Settings"
4. Fill the `Application Callback URL` with the `ACS URL` provided in GitGuardian dashboard.
   ![auth0 setup acs](/img/platform/enterprise-administration/sso-providers/auth0_setup_acs.png)
5. Then, copy-paste these settings to configure mappings, name identifier and message signatures:

```json
{
  "mappings": {
    "given_name": "first_name",
    "family_name": "last_name"
  },
  "signatureAlgorithm": "rsa-sha256",
  "digestAlgorithm": "sha256",
  "signResponse": true,
  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
  "nameIdentifierProbes": [
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
  ],
  "includeAttributeNameFormat": "false"
}
```

6. Finally, we need to configure the Identity Provider in GitGuardian dashboard. First, click on "Usage", then use these values:
   - `Entity id` field is filled with the `Issuer` value
   - `Single Sign-On URL` field is filled with the `Identity Provider Login URL` value
   - `X509 Cert` field is filled with the plain text value of the Identity Provider Certificate
   - Ensure that the checkbox **I have mapped the attributes first_name and last_name in my IdP** is checked
   - Ensure that the checkbox **I have specified that the response assertions with RSA_SHA256 as signature algorithm and SHA256 as digest algorithm** is unchecked

![auth0 idp settings](/img/platform/enterprise-administration/sso-providers/auth0_idp_settings.png)

7. **Important:** Don't forget to [reserve your email domain](../saml-sso-configuration#email-domain-reservation) to enable automatic SSO discovery.
