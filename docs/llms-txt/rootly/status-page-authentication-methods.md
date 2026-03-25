# Source: https://docs.rootly.com/configuration/status-page-authentication-methods.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication Methods

> Configure authentication for public status pages to control access using password or SAML-based single sign-on.

## Overview

Rootly provides multiple authentication methods to secure access to your public status pages. You can choose from no authentication, password protection, or enterprise-grade SAML authentication depending on your security requirements.

Authentication is only available for **public status pages**. Private status pages require users to be logged in to Rootly by default.

## Authentication Methods

<AccordionGroup>
  <Accordion title="No Authentication" icon="unlock">
    Your status page is publicly accessible to anyone with the URL. This is the default setting and is suitable for:

    * Public-facing service status pages
    * External customer communications
    * Maximum visibility during incidents
  </Accordion>

  <Accordion title="Password Authentication" icon="key">
    Protect your status page with a shared password. Anyone with the password can access the page.

    **Best for:**

    * Partner or vendor portals
    * Limited external stakeholder access
    * Quick setup without SSO infrastructure

    **How to configure:**

    1. Navigate to your status page settings
    2. Go to the **Authentication** tab
    3. Select "Password" as the authentication method
    4. Enter your desired password
    5. Save the changes

    Share the password securely with stakeholders who need access.
  </Accordion>

  <Accordion title="SAML Authentication" icon="shield-check">
    Enterprise-grade single sign-on using SAML 2.0 protocol. Users authenticate through your identity provider (IdP) without needing separate credentials.

    **Best for:**

    * Enterprise customers with existing SSO infrastructure
    * Compliance requirements (SOC 2, ISO 27001)
    * Centralized access control and audit logs
    * Multiple status pages with different IdP configurations

    **Supported features:**

    * SAML 2.0 authentication flow
    * Single Logout (SLO)
    * Per-status-page IdP configuration
    * X.509 certificate validation
    * Multiple name identifier formats
  </Accordion>
</AccordionGroup>

## Configuring SAML Authentication

### Prerequisites

Before configuring SAML authentication, you'll need:

* Access to your Identity Provider (IdP) admin console (e.g., Okta, Azure AD, Google Workspace)
* Your IdP's SSO Service URL
* Your IdP's X.509 certificate
* Permissions to create SAML applications in your IdP

### Step 1: Enable SAML in Rootly

1. Navigate to your status page settings
2. Select the **Authentication** tab
3. Choose "SAML" as the authentication method

### Step 2: Configure Your Identity Provider

You'll need to create a new SAML application in your IdP with the following information from Rootly:

**Service Provider (SP) Details:**

| Field                        | Description                            | Example                                    |
| ---------------------------- | -------------------------------------- | ------------------------------------------ |
| **Entity ID / Audience URL** | Unique identifier for your status page | `https://status.company.com/saml/metadata` |
| **ACS URL / Callback URL**   | Where SAML responses are sent          | `https://status.company.com/saml/consume`  |
| **Metadata URL**             | Complete SP metadata (optional)        | `https://status.company.com/saml/metadata` |

<Info>
  These URLs are automatically generated after you save your status page and will be displayed in the Authentication tab for easy copying.
</Info>

### Step 3: Configure SAML Settings in Rootly

Enter the following information from your Identity Provider:

<ParamField path="IdP SSO Service URL" type="string" required>
  The SAML authentication endpoint provided by your IdP

  **Example:** `https://your-company.okta.com/app/abc123/sso/saml`
</ParamField>

<ParamField path="IdP Certificate" type="string" required>
  The X.509 certificate from your IdP for validating SAML responses. Paste the full certificate including the BEGIN/END lines.

  ```
  -----BEGIN CERTIFICATE-----
  MIIDpDCCAoygAwIBAgIGAXoTpGkZMA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQG
  ...
  -----END CERTIFICATE-----
  ```
</ParamField>

<ParamField path="Name Identifier Format" type="select" default="Email Address">
  The format for user identification in SAML assertions

  **Options:**

  * Email Address (default)
  * Unspecified
  * Persistent
  * Transient
</ParamField>

<ParamField path="IdP Single Logout URL" type="string">
  Optional endpoint for SAML Single Logout functionality

  **Example:** `https://your-company.okta.com/app/abc123/slo/saml`
</ParamField>

### Step 4: Test Authentication

1. Save your SAML configuration
2. Open your status page URL in a private/incognito browser window
3. Click the sign-in option
4. You should be redirected to your IdP for authentication
5. After successful authentication, you'll be redirected back to the status page

## Common Identity Provider Guides

<CardGroup cols={2}>
  <Card title="Okta" icon="circle-nodes">
    Configure SAML with Okta using the Entity ID, ACS URL, and download the certificate from your Okta application settings.
  </Card>

  <Card title="Azure AD" icon="microsoft">
    Use Azure AD Enterprise Applications to create a custom SAML app. Copy the Login URL and certificate from the SAML Signing Certificate section.
  </Card>

  <Card title="Google Workspace" icon="google">
    Configure a custom SAML app in the Google Admin console. Use the SSO URL and download the IDP certificate.
  </Card>

  <Card title="OneLogin" icon="id-card">
    Create a SAML application in OneLogin and configure the ACS URL. Download the X.509 certificate from the SSO tab.
  </Card>
</CardGroup>

## Security Considerations

<Warning>
  **Certificate Management:** SAML certificates have expiration dates. Monitor your certificate expiration and update it in Rootly before it expires to prevent authentication failures.
</Warning>

Rootly's SAML implementation includes:

* **X.509 Certificate Validation** - All SAML responses are verified using your IdP's certificate
* **Signature Verification** - Protects against tampering and man-in-the-middle attacks
* **Replay Attack Protection** - SAML assertions are validated for freshness
* **Audit Logging** - All authentication attempts are logged for compliance
* **Secure Session Management** - Encrypted cookies with automatic expiration

## Troubleshooting

### "Invalid SAML Response" Error

* Verify your IdP certificate is correctly formatted with BEGIN/END lines
* Check that the certificate hasn't expired
* Ensure the ACS URL in your IdP matches exactly (including https\://)

### "Authentication Failed" Error

* Confirm the SSO Service URL is correct
* Check that the SAML application is assigned to the correct users in your IdP
* Verify the Name Identifier Format matches your IdP configuration

### Users Cannot Access After Authentication

* Ensure the status page authentication method is set to "SAML"
* Check that your IdP is sending the SAML response to the correct ACS URL
* Verify there are no network/firewall restrictions blocking the SAML flow

### Certificate Expiration

If your SAML certificate expires:

1. Download the new certificate from your IdP
2. Navigate to your status page Authentication settings
3. Update the IdP Certificate field with the new certificate
4. Save the changes

<Tip>
  Set a calendar reminder 30 days before your certificate expiration date to ensure uninterrupted access.
</Tip>

## Switching Authentication Methods

You can change authentication methods at any time:

1. Navigate to your status page settings
2. Go to the **Authentication** tab
3. Select a different authentication method
4. Configure any required fields
5. Save your changes

<Warning>
  Changing from SAML or Password to "No Authentication" will make your status page publicly accessible immediately.
</Warning>

## API Configuration

Authentication methods can also be configured via the Rootly API:

```json  theme={null}
PATCH /v1/status_pages/:id
{
  "authentication_method": "saml",
  "saml_idp_sso_service_url": "https://your-idp.com/sso/saml",
  "saml_idp_cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----",
  "saml_name_identifier_format": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
}
```

See the [Rootly API documentation](/api-reference/overview) for complete details.

## Related Resources

<Card title="Public and Private Status Pages" icon="eye" href="/configuration/public-and-private-status-pages">
  Learn about the differences between public and private status pages
</Card>

<Card title="Status Page Overview" icon="signal-bars" href="/configuration/status-pages">
  Get started with creating and managing status pages
</Card>


Built with [Mintlify](https://mintlify.com).