# Source: https://docs.curator.interworks.com/setup/authentication/one_login_saml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OneLogin

> A guide to setting up OneLogin SAML authentication for Curator.

## Server Setup

If the server is not already setup for web traffic, install Apache, MySQL, PHP, and dependencies. You can do this with
the commands in the setup documentation.

## Tableau Cloud Setup

Tableau has excellent documentation on connecting OneLogin to Tableau Cloud.
[https://onlinehelp.tableau.com/current/online/en-us/saml\_config\_onelogin.htm](https://onlinehelp.tableau.com/current/online/en-us/saml_config_onelogin.htm)

Make sure to follow the additional setup steps in the Tableau Cloud documentation.

If a Tableau login button appears where a Dashboard should be after configuring SAML, be sure to follow the steps to
enable iFrame embedding in the following document:
[https://help.tableau.com/current/online/en-us/saml\_config\_okta.htm#optional-enable-iframe-embedding](https://help.tableau.com/current/online/en-us/saml_config_okta.htm#optional-enable-iframe-embedding)

## OneLogin App Setup

In the OneLogin system, ensure you have turned OFF framing protection by going to "Settings->Account Settings". At the
bottom of the page, ensure that "Framing Protection" is disabled by "checking" the box next to it. (Make sure to hit
"Save" after checking the box! They hide it at the top of the page.)

Then, setup a new App of type "Tableau Cloud SSO". (In addition to the one you already setup for Tableau Cloud)

Name this one after your Curator portal.

For the "Consumer URL", paste in the url to the homepage of Curator. For "Audience", put in the Curator URL without the
trailing /, or http/https.

Go to the "SSO" tab for the settings needed for the Curator Setup.

## Curator Setup

In the /backend settings, go to the Settings->Tableau Server Settings->Authentication area. Select "SAML". For the
Entity ID and IdP ID, put in the "Audience" that you added to OneLogin.

For the SignOn URL, put the "SAML 2.0 Endpoint (HTTP)" URL found in the SSO tab of the App in OneLogin.

For the SignOut URL, put the "SLO Endpoint (HTTP)" URL found in the SSO tab of the App in OneLogin.

Hover over "More Actions" in the OneLogin system. Export the SAML Metadata. Open this file with a text editor and
copy/paste the certificate from the file into the Certificate area of Tableau Server.
