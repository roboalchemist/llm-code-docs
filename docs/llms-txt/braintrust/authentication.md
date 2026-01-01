# Source: https://braintrust.dev/docs/reference/authentication.md

# Authentication

export const FigmaEmbed = ({url}) => {
  return <iframe style={{
    border: "1px solid rgba(0, 0, 0, 0.1)",
    marginTop: "12px"
  }} width="100%" height="450" src={url} allowFullScreen />;
};

Braintrust has a unique [architecture](/reference/architecture) which involves deploying your API endpoints
and data in your own cloud environment. These endpoints are secured so that only users from your organization can access
them. In fact, you could even run these endpoints in a VPN that Braintrust's servers can't access, and the application
will work! This guide walks through how your users and services are able to authenticate within this architecture.

## End-user authentication

The most common form of authentication is end-user authentication to the Braintrust application. Users authenticate with
your enterprise's identity provider (e.g. Google, Okta) and receive credentials directly to their browser. These credentials
are later used to communicate with the Braintrust API endpoint deployed in your cloud.

<FigmaEmbed url="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2Fscdqze6h44YEOXrIEGEn03%2FBraintrust-Auth-Architecture%3Ftype%3Dwhiteboard%26node-id%3D0%253A1%26t%3Ds4p2mdIsk2uSbFuA-1" />

## API authentication

You can authenticate on behalf of users in your experiments or services using an API key. Braintrust API keys
inherit their user's permissions, and essentially are another way to authenticate as a user. To increase security,
API keys are not stored anywhere, and are only displayed to the user once. If you lose an API key, you will need
to generate a new one (and can deactivate the old one).

You can create an API key on the <a href="https://www.braintrust.dev/app/settings?subroute=api-keys" target="_blank">settings page</a>.

<FigmaEmbed url="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FYxvgewtB4Vu8fIjbe0YqCH%2FBraintrust-API-Auth-Architecture%3Ftype%3Dwhiteboard%26node-id%3D0%253A1%26t%3Ds4p2mdIsk2uSbFuA-1" />

## Configure SSO

Make it easy for your team to access Braintrust with your company's existing login system. We use [Clerk](https://clerk.com/) behind the scenes to support several SSO/SAML providers:

### SSO

* Google
* Microsoft

### SAML

* Okta Workforce
* Microsoft Entra ID
* Google Workspace
* Custom SAML provider

### OpenID Connect (OIDC)

* Custom OIDC provider

To get set up, email us at [support@braintrust.dev](mailto:support@braintrust.dev) to exchange the appropriate configuration URLs. Once everything's configured, we'll turn it on for your domain and your team can start signing in using their regular work credentials.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt