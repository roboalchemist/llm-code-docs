# Source: https://developers.webflow.com/data/reference/authentication.mdx

***

title: Authentication
slug: data/reference/authentication
subtitle: Make authenticated requests to the Webflow API
hidden: false
'og:title': Authenticating with the Webflow API
'og:description': >-
Learn how to authenticate with the Webflow API to securely access and manage
your Webflow projects. Follow our guide for seamless integration and API token
management.
'og:keywords': 'Webflow API, Webflow API Key, Webflow API Token'
----------------------------------------------------------------

This guide covers the options for authenticating requests to the Webflow API, including the different methods available and how to choose the best approach for your needs.

## Getting a token

To access the Webflow API, you need to authenticate your requests using a bearer token, which must be included in the authorization header of each API request. There are types of bearer tokens you can create: [Site Tokens](/data/reference/site-token) and [OAuth tokens](/data/reference/oauth-app). Each method is suited to different use cases, and choosing the right one depends on your specific needs.

<CardGroup>
  <Card
    title="Site Token"
    href="/data/reference/site-token"
    iconSize="12"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/KPIs.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/KPIs.svg" alt="" className="block dark:hidden" />
        </>
    }
  >
    Site Tokens provide a simple way to authenticate API requests for a specific Webflow site.

    <br />

    **When to use**<br />
    Best suited for internal tools and single-site integrations where you control the environment.

    <br />

    <a href="/data/reference/site-token">
      <button class="button cc-secondary">Get a Site Token</button>
    </a>
  </Card>

  <Card
    title="Workspace Token"
    href="/data/reference/workspace-token"
    iconSize="12"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/SiteMultiple.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/SiteMultiple.svg" alt="" className="block dark:hidden" />
        </>
    }
  >
    Workspace Tokens provide access for all sites in a Webflow Workspace.

    <br />

    **When to use**<br />
    Best suited for read-only uses, such as monitoring and auditing multiple sites.

    <br />

    <a href="/data/reference/workspace-token">
      <button class="button cc-secondary">Get a Workspace Token</button>
    </a>
  </Card>

  <Card
    title="OAuth"
    href="/data/reference/oauth-app"
    iconSize="12"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/App.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/App.svg" alt="" className="block dark:hidden" />
        </>
    }
  >
    OAuth Tokens are used for complex integrations that span multiple sites or require user-specific access.

    <br />

    **When to use**<br />
    Ideal for public integrations, Apps in the Webflow Marketplace, or any scenario requiring secure, user-specific access.

    <br />

    <a href="/data/reference/oauth-app">
      <button class="button cc-secondary">Get OAuth Token</button>
    </a>
  </Card>
</CardGroup>

<Note title="Quickstart Tip">
  If you're eager to explore the API without setting up full authentication, use our API playground available in the [API reference. ](/data/reference/sites/list)Authenticate once and make requests directly from the documentation.
</Note>

## Sending a request

Sending a request to the Webflow API v2 is straightforward. Include your bearer token in the Authorization header:

```curl cURL
curl --request GET \
     --url https://api.webflow.com/v2/sites \
     --header 'accept: application/json' \
     --header 'authorization: Bearer YOUR_TOKEN'
```

Replace `YOUR_TOKEN` with your actual API token. This setup authenticates your request, allowing access to Webflow resources.

## Revoking a token

To maintain the security of your integration, it's important to revoke access tokens when they're no longer needed or if you suspect they have been compromised. Revoking a token immediately invalidates it, ensuring that it can no longer be used to access the Webflow API.

You can revoke tokens programmatically through the Webflow API or manage them directly within the Webflow dashboard.

<Tabs>
  <Tab title="Site Token">
    Webflow users can remove Site Tokens from the Site Settings. This ensures that unused tokens are securely revoked.

    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/4b37c5fcf7a8b5678a6908078260d3ac50402765a6dd0935149d0c2ac9ad16c9/assets/images/2457dbd-Screenshot_2024-07-31_at_6.13.34_PM.png" alt="Site Token Removal" />
  </Tab>

  <Tab title="OAuth Token">
    You can programmatically revoke an access token obtained through the OAuth 2.0 flow by making a call to the API. For detailed instructions, see our OAuth Authorization Docs.

    <br />

    <br />

    <button class="button cc-primary" onclick="window.location.href='https://developers.webflow.com/data/reference/oauth-app#revoke-an-access-token'">
      View OAuth docs
    </button>
  </Tab>
</Tabs>

## Securing and storing your API tokens

When working with the Webflow API, safeguarding your API tokens is critical to maintaining the security and integrity of your application. API tokens are like passwords for your application—they provide access to sensitive data and actions. Protecting them is essential to prevent unauthorized use and potential security breaches.

### Best practices for token security

1. **Use environment variables**
   Store API tokens in environment variables rather than in your source code. This reduces the risk of accidentally exposing tokens, especially if your code is shared or made public.
2. **Regular token rotation and revocation**
   Regularly rotate your API tokens to minimize risk. If you suspect a token has been compromised, revoke it immediately and generate a new one.

## Troubleshooting

Despite best efforts, issues with API tokens can still occur. Here are common pitfalls and tips to resolve them:

<Accordion title="Expired or invalid tokens">
  * Implement a system to refresh tokens automatically before they expire, or prompt users to re-authenticate.
  * Check token validity and handle expired tokens gracefully in your application.
</Accordion>

<Accordion title="Scope and permission errors">
  * Ensure your tokens include the correct scopes for the actions you intend to perform. Review the Webflow API documentation for an API endpoint  to verify required scopes.
</Accordion>

#### Debugging tips

* Log and review error messages to identify where the authentication process is breaking down.
* Start with minimal scopes to test and gradually increase permissions as needed.
* Verify that your requests include the authorization header with the token.
