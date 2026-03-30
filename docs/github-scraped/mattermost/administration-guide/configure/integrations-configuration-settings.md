# Integrations configuration settings

Review and manage the following integration configuration options in the
System Console by selecting the **Product**
[\|product-list\|](##SUBST##|product-list|) menu, selecting **System
Console**, and then selecting **Integrations**:

- [Integrations management](#integrations-management)
- [Bot Accounts](#bot-acocunts)
- [GIF](#gif)
- [CORS](#cors)

:::: tip
::: title
Tip
:::

System admins managing a self-hosted Mattermost deployment can edit the
`config.json` file as described in the following tables. Each
configuration value below includes a JSON path to access the value
programmatically in the `config.json` file using a JSON-aware tool. For
example, the `EnableIncomingWebhooks` value is under `ServiceSettings`.

- If using a tool such as [jq](https://stedolan.github.io/jq/), you\'d
  enter:
  `cat config/config.json | jq '.ServiceSettings.EnableIncomingWebhooks'`
- When working with the `config.json` file manually, look for an object
  such as `ServiceSettings`, then within that object, find the key
  `EnableIncomingWebhooks`.
::::

------------------------------------------------------------------------

## Integrations management

Access the following configuration settings in the System Console by
going to **Integrations \> Integration Management**.

### Enable incoming webhooks

Developers building integrations can create webhook URLs for public
channels and private channels. See the [incoming
webhooks](https://developers.mattermost.com/integrate/webhooks/incoming/)
developer documentation to learn about creating webhooks, viewing
samples, and letting community know about integrations you\'ve built.

**True**: Incoming webhooks are allowed. To manage incoming webhooks,
select **Integrations** from the Mattermost Product menu. The webhook
URLs created can be used by external applications to create posts in any
public or private channels that you have access to.

**False**: The **Integrations \> Incoming Webhooks** section of the
Mattermost Product menu is hidden and all incoming webhooks are
disabled.

:::: important
::: title
Important
:::

Security note: By enabling this feature, users may be able to perform
[phishing attacks](https://en.wikipedia.org/wiki/Phishing) by attempting
to impersonate other users. To combat these attacks, a BOT tag appears
next to all posts from a webhook. Enable at your own risk.
::::

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnableIncomingWebhooks": true` with options `true` and `false`.

  -----------------------------------------------------------------------

### Enable outgoing webhooks

Developers building integrations can create webhook tokens for public
channels. Trigger words are used to fire new message events to external
integrations. For security reasons, outgoing webhooks are only available
in public channels. See the [outgoing
webhooks](https://developers.mattermost.com/integrate/webhooks/outgoing/)
developer documentation to learn about creating webhooks and viewing
samples.

**True**: Outgoing webhooks will be allowed. To manage outgoing
webhooks, select **Integrations** from the Mattermost Product menu.

**False**: The **Integrations \> Outgoing Webhooks** of the Mattermost
Product menu is hidden and all outgoing webhooks are disabled.

:::: important
::: title
Important
:::

Security note: By enabling this feature, users may be able to perform
[phishing attacks](https://en.wikipedia.org/wiki/Phishing) by attempting
to impersonate other users. To combat these attacks, a BOT tag appears
next to all posts from a webhook. Enable at your own risk.
::::

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnableOutgoingWebhooks": true` with options `true` and `false`.

  -----------------------------------------------------------------------

:::: note
::: title
Note
:::

Disabling this configuration setting in larger deployments may improve
server performance in the following areas:

- Reduced Network Traffic: Outgoing webhooks generate network requests
  to external services. Disabling them reduces the amount of traffic and
  resource usage related to those requests.
- Decreased Load on Server: Handling webhook events and managing
  connections to external services uses server resources. By disabling
  outgoing webhooks, the server workload is reduced, allowing it to
  allocate more resources to other important tasks.
- Improved Response Time: When outgoing webhooks are enabled, the server
  waits for the external services to return responses, potentially
  slowing down the performance if the external services are slow or
  unresponsive. Disabling them removes this dependency, leading to
  faster response times for user requests.
- Lower Memory Usage: Webhooks need memory to process and store data
  about the requests and responses. Disabling them can free up memory
  which can be used to improve overall server performance.
- Simplified Error Handling: Managing errors and retries for outgoing
  webhook failures can add complexity and overhead. Disabling outgoing
  webhooks can simplify error handling and reduce the processing
  overhead associated with it.
- However, outgoing webhooks are often essential for integrating
  Mattermost with other services and workflows. It's important to
  balance performance improvements with the needs of your organization
  and users.
::::

### Enable custom slash commands

Slash commands send events to external integrations that send a response
back to Mattermost.

**True**: Allow users to create custom slash commands from **Main Menu
\> Integrations \> Commands**.

**False**: Slash commands are hidden in the **Integrations** user
interface.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"EnableCommands": false` with
  options `true` and `false`.

  -----------------------------------------------------------------------

### Enable OAuth 2.0 service provider

**True**: Mattermost acts as an OAuth 2.0 service provider allowing
Mattermost to authorize API requests from external applications.

**False**: Mattermost does not function as an OAuth 2.0 service
provider.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnableOAuthServiceProvider": true` with options `true` and `false`.

  -----------------------------------------------------------------------

:::: note
::: title
Note
:::

Cloud admins can\'t modify this configuration setting.
::::

### Enable dynamic client registration

**True**: Enables Dynamic Client Registration (DCR) allowing
applications to programmatically register OAuth 2.0 clients without
manual admin intervention via the `POST /api/v4/oauth/apps/register`
endpoint.

**False**: Dynamic Client Registration is disabled. OAuth 2.0
applications must be registered manually through the System Console.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnableDynamicClientRegistration": false` with options `true` and
  `false`.

  -----------------------------------------------------------------------

:::: important
::: title
Important
:::

**Security Warning**: When enabled, the DCR endpoint
(`/api/v4/oauth/apps/register`) is **publicly accessible without
authentication**. Any user or application can register OAuth clients on
your Mattermost server. Only enable this setting if you understand and
accept this security model, or have additional network-level access
controls in place.
::::

:::: note
::: title
Note
:::

Cloud admins can\'t modify this configuration setting.
::::

### Integration request timeout

The number of seconds to wait for external integration HTTP requests,
before timing out, including [custom slash
commands](https://developers.mattermost.com/integrate/slash-commands/custom/),
[outgoing
webhooks](https://developers.mattermost.com/integrate/webhooks/outgoing/),
[interactive
messages](https://developers.mattermost.com/integrate/plugins/interactive-messages/),
and [interactive
dialogs](https://developers.mattermost.com/integrate/plugins/interactive-dialogs/).
Increase this value if you have external integrations that can take some
time to generate an HTTP response, or experience delayed responses due
to latency.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"OutgoingIntegrationRequestsDefaultTimeout": 3`.

  -----------------------------------------------------------------------

### Enable integrations to override usernames

**True**: Webhooks, slash commands, OAuth 2.0 apps, and other
integrations, will be allowed to change the username they are posting
as. If no username is present, the username for the post is the same as
it would be for a setting of `False`.

**False**: **(Default)** Custom slash commands can only post as the
username of the user who used the slash command. OAuth 2.0 apps can only
post as the username of the user who set up the integration. For
incoming webhooks and outgoing webhooks, the username is \"webhook\".
See <https://developers.mattermost.com/integrate/other-integrations/>
for more details.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnablePostUsernameOverride": false` with options `true` and `false`.

  -----------------------------------------------------------------------

### Enable integrations to override profile picture icons

**True**: Webhooks, slash commands, and other integrations, will be
allowed to change the profile picture they post with.

**False**: **(Default)** Webhooks, slash commands, and OAuth 2.0 apps
can only post with the profile picture of the account they were set up
with. See
<https://developers.mattermost.com/integrate/other-integrations/> for
more details.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnablePostIconOverride": false` with options `true` and `false`.

  -----------------------------------------------------------------------

### Enable personal access tokens

**True**: Users can create [personal access
tokens](https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/)
for integrations in **Profile \> Security**. They can be used to
authenticate against the API and give full access to the account.

To manage who can create personal access tokens or to search users by
token ID, go to the **System Console \> Users** page.

**False**: Personal access tokens are disabled on the server.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnableUserAccessTokens": false` with options `true` and `false`.

  -----------------------------------------------------------------------

### Enforce incoming webhook channel locking

When enabled, this setting enforces that all incoming webhooks must be
locked to their designated channel and cannot post messages to other
channels. This provides administrators with greater control over webhook
security and ensures that webhooks can only post to their intended
channels.

**True**: Incoming webhooks are required to be locked to their specific
channel. The **Lock to this channel** option is automatically enabled
and cannot be disabled when creating or editing webhooks.

**False**: **(Default)** Incoming webhook creators can choose whether to
lock webhooks to a specific channel by selecting **Lock to this
channel**, or allow the webhook to post to any public channel or private
channel the webhook creator is a member of.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnforceIncomingWebhookChannelLocking": false` with options `true` and
  `false`.

  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Bot accounts

Access the following configuration settings in the System Console by
going to **Integrations \> Bot Accounts**.

### Enable bot account creation

**True**: **(Default for Cloud deployments)** Users can create bot
accounts for integrations in **Integrations \> Bot Accounts**. Bot
accounts are similar to user accounts except they cannot be used to log
in. See
[documentation](https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/)
to learn more.

**False**: **(Default for self-hosted deployments)** Bot accounts cannot
be created through the user interface or the RESTful API. Plugins can
still create and manage bot accounts.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"EnableBotAccountCreation": false` with options `true` and `false`.

  -----------------------------------------------------------------------

### Disable bot accounts when owner is deactivated

**True**: When a user is deactivated, disables all bot accounts managed
by the user. To re-enable bot accounts, go to **Integrations \> Bot
Accounts**.

**False**: When a user is deactivated, all bot accounts managed by the
user remain active.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"DisableBotsWhenOwnerIsDeactivated": false` with options `true` and
  `false`.

  -----------------------------------------------------------------------

------------------------------------------------------------------------

## GIF

Access the following configuration settings in the System Console by
going to **Integrations \> GIF**.

### Enable GIF picker

**True**: Allow users to select GIFs from the emoji picker via a GIPHY
integration.

**False**: GIFs cannot be selected in the emoji picker.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"EnableGifPicker": true` with
  options `true` and `false`.

  -----------------------------------------------------------------------

:::: important
::: title
Important
:::

`Link previews <administration-guide/configure/site-configuration-settings:enable message link previews>`{.interpreted-text
role="ref"} must be enabled in order to display GIF link previews.
Mattermost deployments restricted to access behind a firewall must open
port 443 (for all request types) for this feature to work.
::::

------------------------------------------------------------------------

## CORS

The following configuration settings are applicable only to self-hosted
deployments. Access the following configuration settings in the System
Console by going to **Integrations \> CORS**.

### Enable cross-origin requests from

Enable HTTP cross-origin requests from specific domains.

- Type `*` to allow CORS from any domain.
- Enter a specific domain or multiple domains separated by spaces.
- Type `null` to prevent CORS from any domain.
- Leave blank to disable it and use the Mattermost **Site URL** instead.

:::: note
::: title
Note
:::

Ensure you\'ve entered your
`Site URL <administration-guide/configure/environment-configuration-settings:site url>`{.interpreted-text
role="ref"} before enabling this setting to prevent losing access to the
System Console after saving. If you lose access to the System Console
after changing this setting, you can set your Site URL through the
`config.json` file.
::::

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"AllowCorsFrom": ""` with
  string input.

  -----------------------------------------------------------------------

### CORS exposed headers

Whitelist of headers that will be accessible to the requester.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"CorsExposedHeaders": ""`
  with string input.

  -----------------------------------------------------------------------

### CORS allow credentials

**True**: Requests that pass validation will include the
`Access-Control-Allow-Credentials` header.

**False**: Requests won\'t include the
`Access-Control-Allow-Credentials` header.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"CorsAllowCredentials": false` with options `true` and `false`.

  -----------------------------------------------------------------------

### CORS debug

**True**: Prints messages to the logs to help when developing an
integration that uses CORS. These messages will include the structured
key value pair `"source": "cors"`.

**False**: Debug messages not printed to the logs.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"CorsDebug": false` with
  options `true` and `false`.

  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Embedding

The following configuration settings are applicable only to self-hosted
deployments. Access the following configuration settings in the System
Console by going to **Integrations \> Embedding**.

### Frame ancestors

Enter a space-separated list of domains that are allowed to embed the
Mattermost web client via an iFrame. Leave blank to disallow embedding.
Leave blank to disable embedding. Blank by default.

  ------------------------------------------------------------------
  This feature\'s `config.json` setting is `"FrameAncestors".`

  ------------------------------------------------------------------

:::: note
::: title
Note
:::

Embedding Mattermost via an iFrame can provide seamless integration for
collaboration into an organization's existing tools and workflows.
However, you must ensure that correct configurations are in place to
allow communication between the iframe and the parent domain without
violating security.
::::
