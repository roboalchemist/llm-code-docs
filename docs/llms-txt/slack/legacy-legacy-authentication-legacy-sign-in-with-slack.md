Source: https://docs.slack.dev/legacy/legacy-authentication/legacy-sign-in-with-slack

# Legacy Sign in with Slack

This article describes an outdated approach to Sign in with Slack.

The [modern Sign in with Slack](/authentication/sign-in-with-slack/) builds on the OpenID Connect protocol, allowing a more familiar and flexible sign in flow. [Check out the modern Sign in with Slack flow now](/authentication/sign-in-with-slack/#migrate).

New Sign in with Slack apps using this outdated protocol may no longer be created after July 22, 2021.

**Sign in with Slack** extends our existing [OAuth 2.0](/authentication) application approval flow to simplify logging in users to your website, service, or application.

* It's understandable for users.
* It's secure. Slack interfaces with SSO providers and handles two-factor authentication so you have less to worry about.

Use your favorite library or build it yourself; logging users in is a few HTTP requests away.

![Sign in with Slack approval process screenshot&quot; title=&quot;Sign in with Slack approval process screenshot](/assets/images/sign-in-with-slack-approval-f5d32f6f54de9e3b3d7e75738236f160.png)

* * *

## Things to keep in mind before you begin {#prereqs}

Sign in with Slack is a _specific feature_ available to [Slack apps](https://api.slack.com/apps).

Your app uses [the Slack OAuth 2.0 flow](/authentication) to negotiate _limited permissions_ from a Slack user.

### Overview {#overview}

Here's what your app receives from the Sign in with Slack dance:

* Access to _basic_ information about a user who goes through the OAuth flow—an ID and a name.
* Optionally, with more [scopes](#scopes) that you request and the user grants, you receive a few more pieces of information like the user's email address and their avatar in Slack.

Here's what a _user_ gains from using Sign in with Slack:

* The simplicity of signing in only to Slack, rather than signing into many additional apps
* The confidence that Slack account security is maintained

Sign in with Slack can benefit both your app and your users. Keep in mind that there are [limitations](#exceptions) as well, though.

### Everybody can sign in with Slack. Here are the exceptions. {#exceptions}

Workspace administrators may configure whether **Sign in with Slack** is available to their members, separately from any application installation restrictions already in place.

Guest accounts can not use **Sign in with Slack**.

Slack users with an anonymized _Apple relay email address_ (for example, if a user signs into Slack via Apple) may not use **Sign in with Slack**.

* * *

## Implementation Overview {#implementation}

![Negotiating tokens with Slack&#39;s OAuth 2.0 authorization flow&quot; title=&quot;Negotiating tokens with Slack&#39;s OAuth 2.0 authorization flow](/assets/images/slack_oauth_flow_diagram-2ac3fb389a06f9078480b7905c6edb59.png)

### Token negotiation flow {#token-negotiation-flow}

1. User arrives at your site and clicks **Sign in with Slack** button
2. User arrives at `slack.com/oauth/v2/authorize?client_id=CLIENT_ID&user_scope=identity.basic` and briefly approves sign in
3. User arrives at your specified redirect URL with a `code` parameter
4. Your server exchanges `code` for an access token using `slack.com/api/oauth.v2.access`
5. Your server uses the resultant access token to request user & workspace details with `slack.com/api/users.identity`, passing the awarded token as a HTTP authorization header or POST parameter

On the user's first login, we'll ask them to approve your app to access their user and basic workspace information and then send them to your redirect URL to complete sign in.

On subsequent logins, we'll provide an accelerated version of the approval process, still requiring a click, and _then_ send the user back to your redirect.

* **Already have a Slack app and redirect URL?** [Skip ahead](#button_setup).

## Details {#details}

### Create your Slack app if you haven't already {#create_slack_app}

You'll need credentials to use **Sign in with Slack**. To retrieve your Client ID and secret, you'll need to create a Slack app if you haven't already.

Even if you're just implementing **Sign in with Slack** and don't have a Slack App for workspaces to "install," you'll still need to create a Slack App record.

[Create an app](https://api.slack.com/apps?new_app=1)

### Prepare your redirect URI {#prepare-redirect}

After saving your application record, you'll find a panel detailing your Client ID, Client Secret, and Redirect URI configuration:

![OAuth redirect configuration&quot; style=&quot;width: 80%](data:image/png;base64,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)

Save your client ID and secret in a safe, secure place. You'll need both later in this process.

#### What's a redirect URL? {#redirect-url}

Redirect URLs are specific URLs on your site or application that handle a crucial part of the authentication flow. By registering your redirect URLs as part of your application record, you're instructing Slack the valid locations to send authorization codes.

When a user lands on your redirect URL with an authorization code, you'll then perform server-side operations to exchange the authorization code for a bearer token, representing the user's approval of your product or application.

As you develop, you can specify redirects on `localhost` but we recommend using a publicly available server supporting SSL once your integration is user-facing.

Once you've decided where in your application you'll be sending users, provide it on this configuration screen and save your work.

### Set up your Sign in with Slack Button {#button_setup}

Point your buttons to `https://slack.com/oauth/v2/authorize` and include a `user_scope` parameter set only to `identity.basic` (and potentially related scopes we'll discuss soon), along with your `client_id`.

If your application record contains multiple redirect URLs, specify the one you want to use as the `redirect_uri` parameter.

```json
[<img src="https://api.slack.com/img/sign_in_with_slack.png" />](https://slack.com/oauth/v2/authorize?user_scope=identity.basic&client_id=your_client_id)
```text

#### Valid parameters {#valid-parameters}

Parameter

Purpose

Examples

Required?

`user_scope`

A comma- or space-separated list of permissions you're requesting the user to approve. If you're just logging users in, set this to `identity.basic`. You can't ask for `identity.email`, `identity.team`, or `identity.avatar` without also asking for `identity.basic`. To ask for additional permission scopes, you must use the [Add to Slack flow](/legacy/legacy-slack-button) instead.

`identity.basic` `identity.basic identity.email` `identity.basic identity.team identity.avatar`

Yes

`client_id`

The unique identifier of the client.

`1048553852.9553671552`

Yes

`redirect_uri`

The URL the user should return to once Slack has validated their approval. Must be URL-encoded as per [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt) and correspond to a registered URL associated with your application record.

`http%3A%2F%2Flocalhost%3A3000%2Fslack%2Fauth%2Fredirect` `https%3A%2F%2Fyourapp.com%2Fslack%2Fauth%2Fredirect` Note that these are the URL-encoded versions of `http://localhost:3000/slack/auth/redirect` and `https://yourapp.com/slack/auth/redirect`

No

`state`

An optional string of characters you've generated to maintain state. If specified, Slack will send this value back to your redirect URI along with the user. This value is frequently used to validate that your application initiated the login sequence. It is best to use a non-human-readable value.

`aabbCCddeeFF` `resumeSignIn`

No

`team`

ID of a workspace to attempt to restrict the login to. When a valid workspace ID is passed to `team` and the authenticating user is already signed in to that workspace, passing this parameter ensures the user will auth against that workspace. If the user is not signed in yet, the user will be asked to specify a workspace to sign in to. That workspace will then be used as they complete the authorization flow, regardless of any `team` parameter you provided when the flow began.

No

Once you have your hand-crafted button and redirect URI ready, it's time to focus on the process itself.

### Authorization {#authorization}

After a user clicks your **Sign in with Slack** button, their web browser should arrive on Slack's servers.

Your application will wait patiently while the user handles some business or Slack just sends them on their way back to your redirect URL.

The user will be prompted to approve your Slack app.

If a user decides not to perform Sign in with Slack, they'll be redirected to your `redirect_uri` where you may also receive an `error` parameter. (See [OAuth docs](//legacy/legacy-authentication/#step_2a_-_denied_requests))

Either way, your next steps are the same.

The game is afoot. The user's browser has redirected them to your specified redirect URL. It's time for your application to stop waiting and _do_ something again.

#### Interpret parameters {#interpret-parameters}

When your redirect URI was triggered, Slack includes a fresh `code` parameter, along with any `state` parameter you had affixed to your sign in URL.

The `code` parameter is an authorization code that you will exchange for a long-lived access token. It can only be exchanged once and you only have ten minutes to exchange it.

If you're using a `state` parameter, you'll want to verify that the state matches your expectations. If it doesn't, display an error message and do not attempt the next steps.

### Obtain an access token {#obtain-access-token}

We'll now complete the OAuth negotiation sequence by building a request to [`oauth.v2.access`](/reference/methods/oauth.v2.access).

Use the `code` parameter you just received in conjunction with your secure client secret and client ID to prepare your request parameters:

* `client_id` - the client ID issued when you created your app
* `client_secret` - also issued when you created your app
* `code` - that `code` parameter we just told you about
* `redirect_uri` - only include this if you've explicitly specified it in your **Sign in with Slack** button. When provided, it must match exactly, though properly URL-encoded.

We'll then take those parameters and perform a HTTP GET to `https://slack.com/api/oauth.v2.access` like:

```text
GET https://slack.com/api/oauth.v2.access?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&code=XXYYZZ
```text

In response, you'll receive an `application/json` payload containing your access token.

```json
{    "ok": true,    "app_id": "A0118NQPZZC",    "authed_user": {        "id": "U065VRX1T0",        "scope": "identity.basic,identity.email,identity.avatar,identity.team",        "access_token": "xoxp-yoda-yoda-yoda",        "token_type": "user"    },    "team": {        "id": "T024BE7LD"    },    "enterprise": null,    "is_enterprise_install": false}
```text

See the [oauth.v2.access](/reference/methods/oauth.v2.access) documentation for details on error conditions.

#### Response breakdown {#response-breakdown}

Here's a breakdown of `oauth.v2.access`'s typical response for Slack apps.

* `ok` tells you whether the request completed successfully. Always look for a `true` value here before proceeding.
* `app_id` echoes back the ID for your Slack app.
* `authed_user` is an object about the user who just authorized your application for sign in. It contains the token!
  * `id` is the user's ID.
  * `scope` are the comma-separated user scopes the user granted you, in this case the `identity.*` scopes you asked for.
  * `access_token` is the token you can use to call Sign in with Slack identity methods.
  * `token_type` is always `user` for Sign in with Slack.
* `team` will include a single field called `id` for the workspace ID
* `enterprise` will populate with an `id` field when the workspace belongs to an Enterprise organization.
* `is_enterprise_install` will be `true` when the workspace is part of an Enterprise organization.

If you're using **Sign in with Slack** for more than just sign in, the list of scopes may include other scopes you've requested and received for this user. See [Appending Scopes](//legacy/legacy-authentication/#appending_scopes) for more information. But beware, you can't ask for Sign in with Slack scopes at the same time as other scopes.

The values will be more useful to you when obtaining information about the user in the next step.

#### Storing identity access tokens {#storing-identity-access-tokens}

If you'll be saving your identity tokens for later, you'll want to securely store them adjacent to **both a user's ID and team ID**. Consider these three pieces of information a **triad**.

You've authenticated a _specific user_ represented by `user_id`, within a _specific team_ represented by `team_id`, and that authentication is symbolized by the `access_token` you've been awarded.

Be careful not to distribute access tokens (or your client secret) in public code repositories or other unsecured locations. Read our article on [safely storing credentials](/security).

#### Using Sign in with Slack and Add to Slack together {#using-sign-in-with-slack-and-add-to-slack-together}

If the user logging in with **Sign in with Slack** has previously approved your application for other scopes using _Add to Slack_, then the resultant access tokens will contain both the `identity.*` scopes you used for sign in and any scopes you asked for when using [Add to Slack](/legacy/legacy-slack-button). To ask for permissions beyond `identity.*`, request them with the Add to Slack flow.

### Using tokens to retrieve user and team information {#request_info}

Now that you've negotiated your token, use it to make requests with the API.

You'll call the _[`users.identity`](/reference/methods/users.identity)_ API method, requiring the `identity.basic` scope—this method is the primary means to identify users.

If the bearer token you received in the above step was `xoxp-1111827393-16111519414-20367011469-5f89a31i07`, you'd send your request like:

```text
GET https://slack.com/api/users.identityAuthorization: Bearer xoxp-1111827393-16111519414-20367011469-5f89a31i07
```text

The response will be in JSON and contain a few fields you'll want to look out for:

```json
{  "ok": true,  "user": {    "name": "Sonny Whether",    "id": "U0G9QF9C6"  },  "team": {    "id": "T0G9PQBBK"  }}
```text

* `ok` tells you whether the request completed successfully. Always look for a `true` value here before proceeding.
* `user` and `user_id` gives you the user’s real name and unique user ID
* `team` and `team_id` gives you their team name and unique ID

To retrieve additional information about the team member, such as their email address, team name, or image avatar, you'll need to request additional scopes during the authorization phase.

With those scopes approved, the response for `users.identity` will be modified to include the associated data, such that your response may look like:

```json
{  "ok": true,  "user": {    "name": "Sonny Whether",    "id": "U0G9QF9C6",    "email": "sonny@captain-fabian.com",    "image_24": "https://secure.gravatar.com/avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg?s=24&d=https%3A%2F%2Fdev.slack.com%2Fimg%2Favatars%2Fava_0010-24.v1441146555.png",    "image_32": "https://secure.gravatar.com/avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg?s=32&d=https%3A%2F%2Fdev.slack.com%2Fimg%2Favatars%2Fava_0010-32.v1441146555.png",    "image_48": "https://secure.gravatar.com/avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg?s=48&d=https%3A%2F%2Fdev.slack.com%2Fimg%2Favatars%2Fava_0010-48.v1441146555.png",    "image_72": "https://secure.gravatar.com/avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg?s=72&d=https%3A%2F%2Fdev.slack.com%2Fimg%2Favatars%2Fava_0010-72.v1441146555.png",    "image_192": "https://secure.gravatar.com/avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg?s=192&d=https%3A%2F%2Fdev.slack.com%2Fimg%2Favatars%2Fava_0010-192.v1443724322.png",    "image_512": "https://secure.gravatar.com/avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg?s=512&d=https%3A%2F%2Fdev.slack.com%2Fimg%2Favatars%2Fava_0010-512.v1443724322.png"  },  "team": {    "id": "T0G9PQBBK",    "name": "Captain Fabian's Naval Supply"  }}
```text

#### Identity Scopes {#scopes}

* `identity.basic` - request access to basic information about the user and use **Sign in with Slack** to log them in. You must request this scope in order to request any of the scopes below.
* `identity.email` - request access to the user's email address
* `identity.team` - request access to the user's team name
* `identity.avatar` - request access to the user's profile image/avatar

**Important**: Use these scopes and **Sign in with Slack** **_only_** when you're logging users into your application or site. Use the Add to Slack flow when asking teams to approve your Slack App using non-identity.\* scopes.

### You're done! {#youre-done}

Time for your application to do its thing.

### Revoking tokens {#revoking-tokens}

**Sign in with Slack** access tokens do not automatically expire. Users can revoke tokens at any time, and so can you:

If you're off-boarding a user or otherwise wish to revoke a token during your development process, use the new [`auth.revoke`](/reference/methods/auth.revoke) API method. The token you specify as the `token` URL parameter will be revoked.

For example, issuing an HTTP POST to `https://slack.com/api/auth.revoke` with the `token` POST parameter set to `xoxp-2323827393-16111519414-20367011469-5f89a31i07` would give you this response:

```json
{  "ok": true,  "revoked": true}
```text

After execution, the specified token will no longer be functional for API requests.

## Use cases {#use-cases}

There are many ways to use **Sign in with Slack**. Here are some of our favorites.

### Binding Slack team members to service accounts {#binding-slack-team-members}

Your Slack app may be part of a larger service, with its own notion of user accounts and identity.

**Sign in with Slack** can be used to associate a team member with a specific account in your service.

If your app is interacting with an unrecognized user via a [bot user](/legacy/legacy-bot-users) or [slash command](/interactivity/implementing-slash-commands), you can send the user a message containing an authorization URL requesting identity-related scopes, or a link to a page on your site that presents a **Sign in with Slack** button.

### Confirming identity for internal projects {#confirming-identity}

Many teams use custom integrations or team-focused Slack apps to work with internal services and applications. Use **Sign in with Slack** to confirm your organization's team members and log users in to your team's content.

### Business inquiries {#business-inquiries}

Use **Sign in with Slack** to make it easier for your potential customers to request more information about your products or services.

## Helpful resources {#helpful-resources}

### How is Sign in with Slack different from Add to Slack? {#differences}

Using Sign in with Slack makes your app a _specific_ type of Slack app. Sign in with Slack allows you to use the [`users.identity`](/reference/methods/users.identity) method for context on the _user logging in_ to your app or service. You can think of Sign in with Slack as a very particular feature, an exact tool for an exact job—to gain basic information about users for the purpose of onboarding them to your app or service .

The **Add to Slack** flow, in contrast, is much more generally applicable. It's intended for users to **install an app to Slack**. It can be used with _any app_. Most of the time, if your app is doing something beyond gaining basic information about a user to power your service, it **should not** use Sign in with Slack. It can, however, use the **Add to Slack** flow.

### Assets {#assets}

Please use these assets when presenting team members the opportunity to use **Sign in with Slack**.

This HTML snippet references our CDN-hosted buttons:

```text
<img src="https://platform.slack-edge.com/img/sign_in_with_slack.png" srcset="https://platform.slack-edge.com/img/sign_in_with_slack.png 1x, https://platform.slack-edge.com/img/sign_in_with_slack.png 2x" />
```text

Example rendering:

![](https://platform.slack-edge.com/img/sign_in_with_slack.png)

If you want to host the assets yourself, please download this image:

[Download PNG (170px by 40px)](https://platform.slack-edge.com/img/sign_in_with_slack.png)

[Download PNG (Retina, 344px by 80px)](https://platform.slack-edge.com/img/sign_in_with_slack@2x.png)

### Libraries {#libraries}

You can implement the OAuth 2.0 authorization sequence yourself but if you want to use an existing library, almost any supporting the [authorization code grant](https://tools.ietf.org/html/rfc6749#section-4.1) flow should work well with **Sign in with Slack**.

While most existing OAuth 2.0 libraries should cooperate with **Sign in with Slack**, some libraries built to utilize the [Add to Slack button](/legacy/legacy-slack-button) may need modifications to recognize these new scopes and the alternate [users.identity](/reference/methods/users.identity) method used to retrieve identification details after token negotiation.

* Java
  * [scribejava](https://github.com/scribejava/scribejava) - among the simplest OAuth 2.0 libraries available for Java.
* Ruby
  * [omniauth-slack](https://github.com/kmrshntr/omniauth-slack) - easily negotiate tokens in Ruby on Rails, Sinatra and other Ruby-based applications with this plugin for [OmniAuth](https://github.com/intridea/omniauth).
* PHP
  * [oauth2-slack](https://github.com/bramdevries/oauth2-slack) - A Slack-specific extension to [oauth2-client](https://github.com/thephpleague/oauth2-client).
