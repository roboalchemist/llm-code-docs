# Source: https://docs.mage.ai/production/authentication/oidc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Sign in with OIDC

> Enable signing in with OIDC in Mage.

### Pre-requisites

First, you'll need to enable user authentication within Mage. You can find out more about
this in the [Overview page](/production/authentication/overview).

### Enable OIDC sign in

By default, users will not see the "Sign in with OIDC" option in their sign in page.

<Steps>
  <Step title="Add Oauth application">
    You will need to add Mage as a client for your OIDC provider. The way to do this will
    be different depending on your OIDC provider. The redirect URL should be `https://<your-mage-url>/oauth`.
  </Step>

  <Step title="Retrieve credentials">
    Once you have registered Mage, you will need to retrieve the client ID, client secret,
    and the OIDC discovery URL for your provider.
  </Step>

  <Step title="Set environment variables">
    Set the following environment variables in your Mage setup.

    | Name                 | Value               |
    | -------------------- | ------------------- |
    | `OIDC_DISCOVERY_URL` | `<oidc domain url>` |
    | `OIDC_CLIENT_ID`     | `<client id>`       |
    | `OIDC_CLIENT_SECRET` | `<client secret>`   |
  </Step>
</Steps>

You should now see a "Sign in with OIDC" button when you start Mage and attempt to sign in.

Mage will fetch the following OIDC endpoints from the discovery URL:

* authorization\_endpoint
* token\_endpoint
* userinfo\_endpoint


Built with [Mintlify](https://mintlify.com).