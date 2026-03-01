# Source: https://docs.curator.interworks.com/setup/authentication/signing_saml_login_requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Signing Login Requests

> Optional steps to configure Curator to sign SAML login requests.

This is an optional step in addition to configuring Curator for SAML authentication.  See these links for help
configuring SAML within Curator first:

* [Okta](/setup/authentication/okta_saml)
* [OneLogin](/setup/authentication/one_login_saml)
* [AzureAD](/setup/authentication/azure_ad_saml)

## Configuring Curator to Sign SAML Requests

If your SAML Identity Provider (IdP) requires SAML requests to be signed, you'll need a certificate and private key in
Curator's authentication settings. Curator can automatically generate these for you, or you can provide your own.

### Automatic Certificate Generation (Recommended)

Curator will automatically generate a self-signed certificate and private key when you import your IdP's SAML metadata
for the first time. This certificate is valid for 1 year and uses 4096-bit RSA encryption.

**Steps:**

1. <BackendNavPath levelOne="Settings" levelTwo="Security" levelThree="Authentication Settings" />
2. In the **General** section at the top, click **Import SAML Metadata** and upload your IdP's metadata XML file.
3. Curator will automatically generate and populate the **Service Provider Certificate** and **Service Provider Private
   Key** fields in the **SAML Advanced** section.
4. Expand the **SAML Advanced** section and toggle on the **Sign Log In Requests** and **Sign Logout Requests** options.
5. Save the changes.
6. You will likely need to send the certificate file to your SAML IdP administrator.

### Manual Certificate Generation (Optional)

If you prefer to generate certificates manually or need to regenerate them (e.g., for periodic security rotation), you
have two options:

#### Option 1: Use Curator's Regenerate Button

1. <BackendNavPath levelOne="Settings" levelTwo="Security" levelThree="Authentication Settings" />
2. Expand the **SAML Advanced** section.
3. Click the **Regenerate Certificate** button.
4. The **Service Provider Certificate** and **Service Provider Private Key** fields will be automatically populated.

#### Option 2: Generate Your Own Certificate

1. Generate a certificate and private key using an external tool (e.g., [SAMLTool.com](https://www.samltool.com/self_signed_certs.php)
   or OpenSSL).
2. Navigate to Curator's **Backend** > **Settings** > **Security** > **Authentication Settings** and expand the
   **SAML Advanced** section.
3. Copy the certificate contents and paste them into the **Service Provider Certificate** field.
4. Copy the private key contents and paste them into the **Service Provider Private Key** field.
5. Save the changes.

### Final Steps

After setting up your certificate (automatically or manually):

1. Toggle on the **Sign Log In Requests** and **Sign Logout Requests** options in the **SAML Advanced** section.
2. Save the changes.
3. Send the certificate file to your SAML IdP administrator.
4. If the **Certificate** field (the field above the **Service Provider Certificate**) is blank, you'll need to get an
   updated metadata file from your IdP administrator and import it using the button in the **General** section at the top
   of the page.
