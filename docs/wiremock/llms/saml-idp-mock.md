# Source: https://docs.wiremock.io/security/saml-idp-mock.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# The SAML Identity Provider Mock

> How to mock a SAML Identity Provider

<img src="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-logo.png?fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=4169234fd1585d9dda7b736c6848d523" alt="SAML IDP" data-og-width="799" width="799" data-og-height="278" height="278" data-path="images/saml-idp/saml-logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-logo.png?w=280&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=bb9c372d4cfeffb556ebae263c294004 280w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-logo.png?w=560&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=6029f4078a0887bc1ee43e7982867bfb 560w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-logo.png?w=840&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=888030ddacdb8aed26befeab1b48b7f9 840w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-logo.png?w=1100&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=e69d7dee00c40ae08615030dfa073602 1100w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-logo.png?w=1650&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=2009cc2e4233374b4e5afda61fe1ae8d 1650w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-logo.png?w=2500&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=0288ba7ff3670955915b0ad3bf9ccd16 2500w" />

These instructions will help you set up a SAML Identity Provider Mock in your WireMock Cloud account.

The SAML IDP Mock is a template that simulates a SAML Identity Provider (IdP). It
generates signed SAML responses with configurable user attributes, making it suitable
for testing SAML-based SSO integrations without needing a real IdP.

Instructions are provided for using it as an Auth0 Enterprise Connection, but should be
broadly applicable to use with any other Service Provider (SP).

## Setting up the mock

To set up the SAML Identity Provider Mock in your WireMock Cloud account, follow these steps:

1. Log in to you [WireMock Cloud](https://app.wiremock.cloud/mock-apis) account.
2. Click **Create new mock API**.
3. On the `Choose protocol` screen, choose `Template library`.

<img src="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/template-library.png?fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=e3b403e5d1c3e4488bcc43e8d5a1e6c0" alt="Choose Template" data-og-width="1076" width="1076" data-og-height="841" height="841" data-path="images/saml-idp/template-library.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/template-library.png?w=280&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=32995d41b9301ba19a2c9e4ece98fb4d 280w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/template-library.png?w=560&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=81a0ed0958ae7f51754245c86e26a566 560w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/template-library.png?w=840&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=18987123ba010d3f5538cb2093060b0a 840w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/template-library.png?w=1100&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=73c0cb61822bc359c5cd2f2995944ea0 1100w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/template-library.png?w=1650&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=4b7349917ba7286323574ff6850b1e9f 1650w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/template-library.png?w=2500&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=30ba2aaf684745f6b21d9cc3210cb7bf 2500w" />

4. On the template library screen, search for `SAML` and click **Create Mock API** on the `SAML IDP` template.

<img src="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/search-saml.png?fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=b0049d9f3d779d59ad49340d6c43469b" alt="Search Templates" data-og-width="1081" width="1081" data-og-height="701" height="701" data-path="images/saml-idp/search-saml.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/search-saml.png?w=280&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=621ebbb86ad6bf8cc3edbe4824d4a7da 280w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/search-saml.png?w=560&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=e6a9e50c718744bab77d4d6a8f3fa365 560w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/search-saml.png?w=840&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=21b7b64ed9c6eff8fbdce2c5db078b71 840w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/search-saml.png?w=1100&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=510f801589d0dcd3803483257618e288 1100w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/search-saml.png?w=1650&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=67e0f7ab760234de9213219760193751 1650w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/search-saml.png?w=2500&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=76876facebccfd4123b25369871dffbe 2500w" />

5. Give your mock API a name and click **Continue**.
6. This will create the mock API from the template in your WireMock Cloud account.

## How it works

The template provides an interactive web UI with a three-step flow:

1. **Instructions** (`/`) — Setup guide for connecting the mock IdP to your Service Provider (e.g. Auth0)
2. **Login** (`/login`) — A form to configure the post-back URL, email address, and optional extra SAML attributes
3. **Send Response** (`/send-response`) — Builds a signed SAML response and POSTs it back to your SP's ACS URL

The mock IdP also serves its X.509 signing certificate at `/certificate.pem`.

## SAML response structure

The response includes:

* **Issuer** — mock API's base URL
* **Subject** — NameID using email (format: `emailAddress`)
* **Conditions** — NotBefore (now - 1 min), NotOnOrAfter (now + 5 min), with audience from the SAML request
* **Attributes** — `email` attribute plus any extra `<saml:Attribute>` tags from the login form
* **AuthnStatement** — `PasswordProtectedTransport` context class
* **Signature** — SHA-256 digest, RSA-SHA256 signature, enveloped signature transform

## Setup

To set up the SAML Identity Provider Mock as an Enterprise Connection, copy the base URL
of the mock API and open it in your browser.  You should see a page with instructions for
setting up the connection.

<img src="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/base-url.png?fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=869e80818ce672eae86b1f77ff9d487f" alt="Copy Base URL" data-og-width="1135" width="1135" data-og-height="124" height="124" data-path="images/saml-idp/base-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/base-url.png?w=280&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=10adeeb708ceacff63ca87e158db3594 280w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/base-url.png?w=560&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=dce6eb8a06f0d269311effe3b33a3270 560w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/base-url.png?w=840&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=5d87eea1d865f837142214a69ee3683a 840w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/base-url.png?w=1100&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=8f2672e078b9a2fd4b145b09ec8ab399 1100w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/base-url.png?w=1650&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=9551952cd286f6b68926dd27c4e6003c 1650w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/base-url.png?w=2500&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=cef9db0fd7ab7d706ab16d831567cacf 2500w" />

You will see the following instructions:

<img src="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/instructions.png?fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=f36e367ba45fc46f6c11ea6a34be1894" alt="Instructions" data-og-width="670" width="670" data-og-height="621" height="621" data-path="images/saml-idp/instructions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/instructions.png?w=280&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=c23a9a5f92b4c1a8d010cf64bbd96742 280w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/instructions.png?w=560&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=6c94878fd7b1ab4f8ccdf20f88e6023e 560w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/instructions.png?w=840&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=5826159720e7cccde1394b7bacb87e9a 840w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/instructions.png?w=1100&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=2fc5ab4a9a8c32f2287f6cfa4b1d578c 1100w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/instructions.png?w=1650&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=050a9d2af40117fdee5b563e97a3298e 1650w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/instructions.png?w=2500&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=68e05c1d7d158f4859e46e08a2bd6bd0 2500w" />

1. Download the signing certificate from `/certificate.pem`
2. In Auth0, navigate to **Authentication** > **Enterprise**, click **SAML** > **Create**
3. Set **Sign In URL** to `<mock api base url>/login`
4. Upload the certificate from step 1
5. Toggle off **Enable Sign Out** and **Sign Request**
6. Click **Create**

In the `Login Experience` tab you should specify your domain in the `Identity Provider domains` field
and remember to toggle on the applications you want to associate with this connection in the `Applications` tab.

## Using with your app

1. Login to your application using an account with an email address that matches the domain you specified in the connection setup.
2. This should recognize the connection associated with the domain and redirect you to the `/login` page of the mock IdP.
3. This will display the following form:

<img src="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/login-form.png?fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=688532ab8fd6b2b5c2903732a16509cb" alt="Login Form" data-og-width="662" width="662" data-og-height="1001" height="1001" data-path="images/saml-idp/login-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/login-form.png?w=280&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=422f09c949a38495274c4b146ddcc419 280w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/login-form.png?w=560&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=4a24ba77604ad3fda0ae06ae997a42d7 560w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/login-form.png?w=840&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=14e88055e797758474d13bb21ea98966 840w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/login-form.png?w=1100&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=4821baab1dfec6fe57a3871cf37594fa 1100w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/login-form.png?w=1650&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=83b43965f28c9e21a3cc56b51c6951b9 1650w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/login-form.png?w=2500&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=ad25be8f9b6cb3063f81b80612d0619b 2500w" />

1. Fill out the post-back URL as defined by your IDP.  **This is a required field**. This is likely to be the same
   across all authentication requests for the same domain/connection.  If this is the case you could update the response template to
   hardcode this value.
2. Enter the email address of the user you want to authenticate. **This is a required field**.
3. The `Extra attribute(s)` allows you to send arbitrary extra `<saml:Attribute>` tags.
   It is important to remove all whitespace to ensure SAML hashing and signing work correctly.  For example

```xml  theme={null}
<saml:Attribute Name="groups"><saml:AttributeValue>admins</saml:AttributeValue><saml:AttributeValue>developers</saml:AttributeValue><saml:AttributeValue>finance</saml:AttributeValue></saml:Attribute>
```

Once you have filled out the form, click on the `Build SAML Response` button. This will
take you to the `/send-response` page of the mock IdP, showing the SAML response that was built.

<img src="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-response.png?fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=e0933f7d77ea8c5a738709c0692293fd" alt="SAML Response" data-og-width="668" width="668" data-og-height="1259" height="1259" data-path="images/saml-idp/saml-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-response.png?w=280&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=c12cf22671e28e0099e8a3dfa3428658 280w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-response.png?w=560&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=4b98a564cbfb79640b288ed44504d520 560w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-response.png?w=840&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=6dbc4121ce6d7994f3d9c7186c3a9ff1 840w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-response.png?w=1100&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=d582672549c2544d8cf0b42f51c91625 1100w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-response.png?w=1650&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=9013e4246b4e3c8324bd6b7339732b82 1650w, https://mintcdn.com/wiremockinc/kyjqjQXnKn13jeNt/images/saml-idp/saml-response.png?w=2500&fit=max&auto=format&n=kyjqjQXnKn13jeNt&q=85&s=75018c7f0038115710db4881b91ba818 2500w" />

This form shows you the SAML response that was built along with the parsed values for you to use for debugging if required.
Click on the `Send SAML Response to Service Provider` button to send the response back to your SP.

You should then be authenticated and redirected back to your application.

## Questions and feedback

If you're not sure how something works or have a suggestion for improving this simulation, please get in touch with us
via [info@wiremock.io](mailto:info@wiremock.io) or the chat widget.
