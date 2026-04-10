# Source: https://developers.kit.com/kit-app-store/authentication.md

# Source: https://developers.kit.com/api-reference/authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Authentication

> Authenticating with the Kit API for apps and personal use

We support two authentication mechanisms in the V4 API:

* **OAuth 2.0** for apps available for all creators in the Kit App Store
* **API keys** for automating simple tools and integrations for your own account

## OAuth

We support the [Authorization Code Grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) and depending on the type of app you're building we support two ways of issuing access tokens:

* For web servers, you'll use the [refresh token flow](/api-reference/oauth-refresh-token-flow)
* For Single Page Apps (SPA) or mobile apps, you'll use the [Proof Key for Code Exchange (PKCE) flow](/api-reference/oauth-proof-key-for-code-exchange-flow)

<img width="800" alt="OAuth app flow" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/OAuth-Guidelines-api.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=5bb3d7d6d160bb7cb6561eecade7c952" data-path="images/api/OAuth-Guidelines-api.png" />

<Tip>
  We've found these two resources to be helpful for learning more about how OAuth 2.0 works:

  <ul>
    <li><a href="https://www.oauth.com/playground/">Okta's OAuth Playground</a></li>
    <li><a href="https://developer.okta.com/blog/2019/10/21/illustrated-guide-to-oauth-and-oidc">David Neal's An Illustrated Guide to OAuth and OpenID Connect</a></li>
  </ul>
</Tip>

### Creating and configuring your OAuth powered app

For apps and full API V4 support, you will need to authenticate via OAuth 2.0. In order to set this up in your Kit account, first you have to [create an app](/kit-app-store/building-apps#creating-your-app) and turn on [API access](/kit-app-store/building-apps#api-and-plugin-access).

Once you have turned on API authentication for your app you will be offered 3 settings to configure:

* `Authorization URL`
* `Redirect URIs`
* `Secure application`

<img width="800" alt="OAuth configuration" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/oauth-app-configuration.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=c295e3f08ae90debb2e50eae1785a304" data-path="images/api/oauth-app-configuration.png" />

##### Authorization URL

The `Authorization URL` should be a URL on your system that we will link to during app installation so you can initiate OAuth and store the returned access tokens. We will link the user to this URL with a `redirect` query param, e.g. `?redirect=https://app.kit.com/apps`. When the authorization flow is complete, you need to redirect the user back to that provided redirect URL so they can continue their session within the Kit app.

##### Redirect URI(s)

Once a user has logged in or signed up with your service, you will redirect them back to the Kit OAuth server for the creator to grant access to the Kit API for your service. On this request you will specify the callback URI that Kit will reach out to with a temporary authorization code, that you will be able to exchange for an access and refresh token, once consent is given by the user.

For security, the value in the `redirect_uri` property sent to the Kit OAuth server must match one of the Redirect URIs you have set up in the above app configuration screen.

##### Secure application

If your app will be used in an insecure location where the client secret can't be kept confidential - such as mobile or single page apps, you will have to turn this setting off. When unchecked this will enforce use of the [Proof Key for Code Exchange (PKCE) flow found above](/api-reference/authentication#oauth-flows).

##### Post-installation redirect

Your app may also include the option to alternatively send creators to your app, or an externally hosted onboarding flow, post signup. This can be configured using the `Redirect URL after install` field in your [app details setting page](/kit-app-store/app-details-page). An example of this flow can be seen below.

<AccordionGroup>
  <Accordion title="Example redirect flow">
    <img width="1000" alt="example redirect flow" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/example-redirect-flow.gif?s=a5edb0b666ed88fa29381ae689da5323" data-path="images/kit_app_store/example-redirect-flow.gif" />
  </Accordion>

  <Accordion title="Redirect flow settings">
    <img width="1000" alt="example redirect flow" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/kit_app_store/post-install-redirect-url.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=524d65d71af958527a96898c664f774b" data-path="images/kit_app_store/post-install-redirect-url.png" />
  </Accordion>
</AccordionGroup>

## API keys

API key authentication is the simplest way to access V4 of the API, tailored for programmatic access to your own Kit account for simple account automation, or for pulling account data for deeper external analysis. We do not offer any official support for apps or public integrations that rely upon API keys for authentication - for apps, please follow the OAuth guide below.

We also offer some restrictions when using API keys:

* When using API Keys, no more than 120 requests over a rolling 60 second period for a given API Key (we offer limits of 600 requests using OAuth)
* Some of our endpoints require OAuth authentication - for example, our bulk and purchase creation endpoints. Please check the endpoint specific documentation for authentication requirements

### Creating V4 API keys

To use API Key authentication, you must first create a V4 API Key. To do this, visit the ["Developer" tab in your account settings](https://app.kit.com/account_settings/developer_settings).

<img width="800" alt="v4 api key settings" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/v4-keys.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=59288ff59aaf1b55da3d2005e14d7ace" data-path="images/api/v4-keys.png" />

Here:

<Steps>
  <Step title="Click on Add a new key" />

  <Step title="Give it an internal name" />

  <Step title="Copy and save the API key for future use">
    <Warning>Please make sure to save your API key at this point and keep it somewhere safe, as you'll not be able to access it again after leaving the screen.</Warning>
  </Step>
</Steps>

<img width="600" alt="V4 api key created" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/v4-key-created.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=7c2c6de34a13b015b857a8798a6394d1" data-path="images/api/v4-key-created.png" />

### Resetting & deleting V4 API keys

If you have misplaced your API key, you will not be able to retrieve it again and will instead have to reset it from within your ["Developer" settings](https://app.kit.com/account_settings/developer_settings). To reset your key, first click on the "Edit" button on the key you want to update:

<img width="800" alt="edit v4 api key" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/edit-v4-key.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=7200bdd318deb22644ad40dd6b44dffd" data-path="images/api/edit-v4-key.png" />

Then click on the "Reset" button to re-roll the key to a new value.

<img width="600" alt="reset v4 api key" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/reset-v4-key.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=16a4db7cd548ca66a8046b4280eed077" data-path="images/api/reset-v4-key.png" />

Click "Reset" once more to confirm your action.

<img width="400" alt="reset v4 api key confirmation" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/reset-keys-confirmation.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=1d89f04477c3f673ab008fb331230ee4" data-path="images/api/reset-keys-confirmation.png" />

Your V4 key is now reset. At this point, any script or process that was relying on the previous iteration of the key will fail to authenticate, so you will need to replace it with the new value provided here.

<Warning>Again, it is important that you save your API key at this point and keep it somewhere safe, as you'll not be able to access it again after leaving the screen.</Warning>

<img width="600" alt="v4 api key reset" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/v4-key-reset.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=eaf4d2c0c26a2cf3cc2cdc1fd985f4aa" data-path="images/api/v4-key-reset.png" />

### Deleting V4 API keys

If you ever no longer need an API Key, you can also delete it by editing the API Key, and click on "Delete API Key".

<img width="600" alt="delete v4 api key" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/api/reset-v4-key.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=16a4db7cd548ca66a8046b4280eed077" data-path="images/api/reset-v4-key.png" />

### Using V4 API keys

To use V4 API key authentication, pass the key alongside a `X-Kit-Api-Key` header when making requests.

For example, the following request will return your account information:

```shell  theme={null}
curl --request GET \
  --url https://api.kit.com/v4/account \
  --header 'X-Kit-Api-Key: <YOUR_V4_API_KEY>'
```


Built with [Mintlify](https://mintlify.com).