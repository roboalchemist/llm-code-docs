Source: https://docs.slack.dev/legacy/legacy-authentication

# Legacy authentication

This article describes an outdated approach to apps. [Slack apps](/app-management/quickstart-app-settings) are installed with the [V2 OAuth 2.0 flow](/authentication/installing-with-oauth).

OAuth 2.0 is a protocol that lets your app request authorization to private details in a user's Slack account without getting their password. It's also the vehicle by which Slack apps are installed on a team.

Your app asks for specific [permission scopes](/reference/scopes) and is rewarded with access tokens upon a user's approval.

You'll need to [register your app](https://api.slack.com/apps) before getting started. A registered app is assigned a unique Client ID and Client Secret which will be used in the OAuth flow. The Client Secret should not be shared.

The easiest way to enable workspaces to install your app is with the **[Add to Slack](/legacy/legacy-slack-button)** button.

**[Sign in with Slack](/authentication/sign-in-with-slack/)** is the best way to log individual members into your application.

## The OAuth Flow {#flow}

Slack uses OAuth 2.0's [authorization code grant flow](https://tools.ietf.org/html/rfc6749#section-4.1) to issue access tokens on behalf of users.

![Negotiating tokens with Slack&#39;s OAuth 2.0 authorization flow&quot; title=&quot;Negotiating tokens with Slack&#39;s OAuth 2.0 authorization flow](/assets/images/slack_oauth_flow_diagram-2ac3fb389a06f9078480b7905c6edb59.png)

The OAuth flow is your key to unlocking access tokens. There's no path to programmatically create (or retrieve) app access tokens without a user's input.

### Step 1 - Sending users to authorize and/or install {#send_users}

Your web or mobile app should redirect users to the following URL:

`https://slack.com/oauth/authorize`

The following values should be passed as GET parameters:

* `client_id` - issued when you created your app (required)
* `scope` - permissions to request (required)
* `redirect_uri` - URL to redirect back to ([see below](#redirect_urls)) (optional)
* `state` - unique string to be passed back upon completion (optional)
* `team` - Slack team ID of a workspace to attempt to restrict to (optional)

The `scope` parameter is a space-separated list of OAuth scopes, indicating which parts of the Slack user's account you'd like your app to be able to access. The complete list of scopes can be found [here](/legacy/legacy-authentication/legacy-oauth-scopes).

The `state` parameter should be used to avoid forgery attacks by passing in a value that's unique to the user you're authenticating and checking it when auth completes.

Redirect URLs and URIs must use HTTPS, and must _not_ contain an anchor (`#`).

**Streamline this step** further with a [Direct Install URL](/slack-marketplace/distributing-your-app-in-the-slack-marketplace#direct_install).

#### How the team parameter behaves {#team_parameter}

When a valid team ID is passed to `team` and the authenticating user is already signed in to that workspace, passing this parameter ensures the user will auth against that workspace.

If the user is not signed in yet, the user will be asked to specify a workspace to sign in to. That workspace will then be used as they complete the authorization flow, regardless of any `team` parameter you provided when the flow began.

If you omit the optional `team` parameter, the user will be allowed to choose which workspace they are authenticating against.

For the best user experience, use the [Add to Slack](/legacy/legacy-slack-button) button to direct users to approve your application for access and [Sign in with Slack](/authentication/sign-in-with-slack/) to log users in.

### Step 2 - Users are redirected to your server with a verification code {#redirect_users}

If the user authorizes your app, Slack will redirect back to your specified `redirect_uri` with a temporary code in a `code` GET parameter, as well as a `state` parameter if you provided one in the previous step. If the states don't match, the request may have been created by a third party and you should abort the process.

Authorization codes may only be exchanged once and expire 10 minutes after issuance.

### Step 3 - Exchanging a verification code for an access token {#exchanging_code}

If all is well, exchange the authorization code for an access token using the [`oauth.access`](/reference/methods/oauth.access) API method ([method documentation](/reference/methods/oauth.access)).

`https://slack.com/api/oauth.access`

* `client_id` - issued when you created your app (required)
* `client_secret` - issued when you created your app (required)
* `code` - a temporary authorization code (required)
* `redirect_uri` - must match the originally submitted URI (if one was sent)

You'll receive a JSON response containing an `access_token` (among other details):

```json
{    "access_token": "xoxp-23984754863-2348975623103",    "scope": "read"}
```text

Access tokens for all apps are also known as bearer tokens. See [token types](/authentication/tokens) for an overview of all the kinds of tokens involved in the Slack platform.

You can then use this token to call [API methods](/reference/methods) on behalf of the user. The token will continue functioning until the installing user either revokes the token and/or uninstalls your application.

Slack apps can be installed multiple times by the same user _and_ additional users on the same workspace. Your app is considered "installed" as long as one of these tokens is still valid.

User and bot access tokens awarded to Slack apps do not expire.

This is an opportunity to get users back to work by [redirecting them to deep links](/interactivity/deep-linking) within Slack.

#### Bot user access tokens {#bots}

If your Slack app includes a [bot user](/legacy/legacy-bot-users), upon approval the JSON response will contain an additional node containing an access token to be specifically used for your bot user, within the context of the approving workspace.

When you connect to [`rtm.connect`](/reference/methods/rtm.connect) or use [Web API](/apis/web-api/) methods on behalf of your bot user, you should use this bot user access token instead of the top-level access token granted to your application.

Here's a more verbose example JSON response including a Bot user access token:

```json
{    "access_token": "xoxp-XXXXXXXX-XXXXXXXX-XXXXX",    "scope": "incoming-webhook,commands,bot",    "team_name": "Team Installing Your Hook",    "team_id": "XXXXXXXXXX",    "incoming_webhook": {        "url": "https://hooks.slack.com/TXXXXX/BXXXXX/XXXXXXXXXX",        "channel": "#channel-it-will-post-to",        "configuration_url": "https://teamname.slack.com/services/BXXXXX"    },    "bot":{        "bot_user_id":"UTTTTTTTTTTR",        "bot_access_token":"xoxb-XXXXXXXXXXXX-TTTTTTTTTTTTTT"    }}
```text

Within this response, the `bot` node contains two fields related to your bot user: `bot_user_id` and `bot_access_token`. Bot access tokens always begin with `xoxb`.

Bot user tokens may be revoked by all installing users having uninstalled your Slack app from their workspace.

Secure your bot user tokens, as with all tokens and credentials

Do not share tokens with users or anyone else. Bot user tokens have particularly expansive capabilities not afforded to typical user tokens issued on behalf of members.

#### Denied requests {#denied_requests}

If the user denies your request, Slack redirects back to your `redirect_uri` with an `error` parameter.

[http://yourapp.com/oauth](http://yourapp.com/oauth)? error=access\_denied

Applications should handle this condition appropriately.

## Storing tokens and credentials {#storage}

Store your application's credentials and user tokens with care. Read our article on [safely storing credentials](/security).

Restrict [Web API](/apis/web-api/) access to only IP addresses you trust by [allowlisting specific IP addresses](/security#verify).

## Using access tokens {#using_tokens}

The tokens awarded to your app can be used in requests to the [Web API](/apis/web-api/).

Many different types of tokens are used on the Slack platform. See our [index of token types](/authentication/tokens) for a tour.

The **best** way to communicate your access tokens, also known as bearer tokens, is by presenting them in a request's `Authorization` HTTP header:

```text
GET /api/conversations.list?limit=50Authorization: Bearer xoxb-1234-abcdefgh
```text

This approach is **required** when using `application/json` with a write method.

Alternatively, you may send the token as a querystring or POST body attribute of the `application/x-www-form-urlencoded` variety:

In a query string:

```text
GET /api/conversations.list?limit=50&token=xoxb-1234-abcdefgh
```text

Or a POST body:

```text
POST /api/conversations.listContent-type: application/x-www-form-urlencodedtoken=xoxb-1234-abcdefgh&limit=50
```text

## Redirect URIs {#redirect_urls}

The `redirect_uri` parameter is optional. If left out, Slack will redirect users to the callback URL configured in your app's settings. If provided, the redirect URL's host and port must exactly match the callback URL and use HTTPS. The redirect URL's path must reference a subdirectory of the callback URL.

```text
CALLBACK: https://example.com/pathGOOD: https://example.com/pathGOOD: https://example.com/path/subdir/otherBAD:  http://example.com/barBAD:  http://example.com/BAD:  http://example.com:8080/pathBAD:  http://oauth.example.com:8080/pathBAD:  http://example.org
```text

## Handling multiple authorizations {#multiple}

Your application may send a user through the OAuth flow multiple times.

You can utilize this behavior to re-verify a user's identity or to retrieve a user's access token again as needed. You can also use it to upgrade an access token's [OAuth scopes](/legacy/legacy-authentication/legacy-oauth-scopes).

If your application _requires_ a basic set of permissions to function, but can utilize _optional_ permissions for advanced functionality, requesting additional scopes separately ensures that your application will have the access it needs to function without initially deterring users from approving it.

When your user is ready to indulge themselves in features requiring additional permissions, send them through the OAuth flow again, this time requesting the additional scopes you need.

For example, if your app uses Slack to sign in to your service, you may want to restrict your initial OAuth request to just the `identify` scope. If that same app also has an optional feature to import files from Slack using `files:read`, you can initiate the application approval process again, within context of the user's action, so they understand why the additional permissions are being requested.

This ensures that your app retains critical functionality (signing in to your app) without requiring optional permissions (access to the user's files) and also provides better context for the user.

### Appending scopes {#appending_scopes}

When you initially send a user through the OAuth flow, you receive a token that has the set of scopes you requested. Any subsequent time(s) you send that same user through the OAuth flow, any new scopes you request will be added to that initial set.

For example, if you initially request `channels:read` and `channels:write` from a user, the initial token will only be scoped to `channels:read channels:write` (plus `identify`, which is automatically included in any OAuth grant for a classic app). If you send that same user through a second OAuth flow, this time requesting `files:write`, the resulting token will have the new scope added to the previous set: `channels:read channels:write files:write identify`.

This process can be repeated any number of times, and each scope you request is **additive** to the scopes you've already been awarded. It is not possible to downgrade an access token's scopes.

As you make [Web API](/apis/web-api/) requests, a `x-oauth-scopes` HTTP header will be returned with every response indicating which scopes the calling token currently has:

```text
x-oauth-scopes: identity.basic,reactions:read
```text

### Verifying user identity without installing anything {#verifying_user}

Use [Sign in with Slack](/authentication/sign-in-with-slack/) instead when you just want to log members in and verify their identity without having them "install" something. If you need to ask for specific authorization scopes from a user, you can switch to the [Add to Slack](/legacy/legacy-slack-button) flow to request them. Additional scopes awarded there will be appended to the same OAuth token for that user.

## Revoking tokens and uninstalling apps {#revoking_tokens}

For workspace apps, use [`apps.uninstall`](/reference/methods/apps.uninstall) to uninstall an app completely, revoking all tokens.

If you want to dispose of a single OAuth access token, use [`auth.revoke`](/reference/methods/auth.revoke). This includes both [_refresh tokens_](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021) and _access tokens_ for workspace apps. It works with tokens from [Sign in with Slack](/authentication/sign-in-with-slack/) as well as from [Add to Slack](/legacy/legacy-slack-button).

For classic apps, revoking the last token associated between your application and a workspace effectively uninstalls the app for that workspace.

Revoking tokens and asking a user to authenticate again is the best way to _start over_ and incrementally add more limited [OAuth scopes](/legacy/legacy-authentication/legacy-oauth-scopes) to a token.
