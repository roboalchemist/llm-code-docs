Source: https://docs.slack.dev/changelog/2018/04/01/oauth-flow-changes-for-workspace-token-preview-apps

# OAuth flow changes for workspace token preview apps

April 1, 2018

Workspace apps are deprecated

[Learn more](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

We're simplifying the installation process for workspace apps.

Now workspace apps can and should use the [`oauth.access`](/reference/methods/oauth.access) method instead of `oauth.token` during the verification code exchange phase of app installation via OAuth 2.0.

When used with workspace apps, the response for `oauth.access` morphs into a response similar to that of `oauth.token`, but with a few improvements detailed [below](#token_acess).

Now [`oauth.access`](/reference/methods/oauth.access) may be used by workspace apps instead of `oauth.token`, simplifying a common hurdle when getting started with workspace apps.

Finally, we're replacing `apps.permissions.info` with `apps.permissions.scopes.list` and `apps.permissions.resources.list`.

## What's changing? {#what}

All of these changes are for workspace apps that are part of our developer preview.

* [`oauth.access` now works with workspace apps](#token_access)
* [`oauth.token` is deprecated](#token_deprecation)
* [Two new methods replace `apps.permissions.info`](#permissions_methods)
* [Now you can expedite single channel access](#single_channel_flow)

### Exchange tokens using oauth.access instead {#token_access}

Now you can exchange `code` values for tokens using [`oauth.access`](/reference/methods/oauth.access), just like traditional Slack apps. The output received from `oauth.access` is the same as found in `oauth.token`.

Here's the new response structure:

```json
{    "ok": true,    "access_token": "xoxa-access-token-string",    "token_type": "app",    "app_id": "A012345678",    "app_user_id": "U0NKHRW57",    "team_name": "Subarachnoid Workspace",    "team_id": "T061EG9R6",    "authorizing_user": {        "user_id": "U061F7AUR",        "app_home": "D0PNCRP9N"    },    "installer_user": {        "user_id": "U061F7AUR",        "app_home": "D0PNCRP9N"    },    "scopes": {        "app_home": [            "chat:write",            "im:history",            "im:read"        ],        "team": [],        "channel": [            "channels:history",            "channels:read",            "chat:write"        ],        "group": [            "chat:write"        ],        "mpim": [            "chat:write"        ],        "im": [            "chat:write"        ],        "user": []    }}
```text

This structure communicates a short story:

1. An access token has been awarded or refreshed on the workspace identified by `T061EG9Z9` (_"Subarachnoid Workspace"_) for your Slack app identified by the ID `A012345678`.
2. The user who originally installed the app is the same user currently performing the authorization flow, user `U061F7AUR`. You can send them messages on the `app_home` conversation channel, `D0PNCRP9N`.
3. The user approved the app for the [`chat:write`](/reference/scopes/chat.write) scope, but access was only granted to a single public channel resource, `C061EG9T2`.
4. The app is automatically awarded the ability to read, write, and peruse the history of its conversation with the installing user in its `app_home`.

If your app is subscribed to permissions-related events on the Events API, you'll receive more detail about the resources your scopes apply to.

## Looking for the `permissions` field from `oauth.token`?

The `permissions` attribute isn't returned in `oauth.access`.

This response is now consolidated by removing its exhaustive list of existing `permissions`.

To retrieve a list of all permissions awarded by a workspace to your app, use `apps.permissions.resources.list` with `apps.permissions.scopes.list` and/or monitor permission events with the [Events API](/apis/events-api/).

## We added a `scopes` attribute to `oauth.access`

The now-removed `permissions` attribute housed a listing of all `scopes` assigned by a workspace to your app.

You'll now find a `scopes` attribute top-level. Instead of describing all the awarded scopes, it lists only the scopes assigned in this particular installation sequence.

Scopes are grouped by resource type:

* `app_home` - your app's direct message conversation with the installer of this app
* `team` - team-level permissions assigned to your app
* `channel` - public channels
* `group` - private channels
* `mpim` - multi-member direct messages
* `im` - direct messages
* `user` - users

`oauth.access` won't tell you the wildcard status of any resources. The new `apps.permissions.scopes.list` and `apps.permissions.resources.list` methods won't either. Continue using `apps.permissions.info` to retrieve wildcard awards.

### Deprecation of oauth.token {#token_deprecation}

`oauth.token`, we hardly knew you! We originally developed this message in isolation of `oauth.access` to separate concerns during the preview but as we get ready for general availability, we've upgraded `oauth.access` to take on this role and keep the OAuth process consistent.

### New methods replace apps.permissions.info {#permissions_methods}

`apps.permissions.info` will retire in July 2018. We broke the method up into two distinct chunks, future proofing your app for the possibility of zillions of awarded, valuable resources.

* `apps.permissions.scopes.list` catalogs the scopes awarded to your app. It does not indicate which resources those scopes are tied to. All scopes apply to all resources.
* `apps.permissions.resources.list` catalogs the resources granted to your app. The scopes found in the method above apply to each resource.

### Single-channel authorization flow added {#single_channel_flow}

To request access to only a single channel, add `single_channel=true` to the querystring you generate for the `oauth/authorize` step. Users will be asked to approve your app's requested scopes just for a single channel they choose. When the approval process is complete, the response to `oauth.token` or `oauth.access` will contain a `single_channel_id` field noting the channel resource.

Repeating this process multiple times on the same workspace adds additional channel grants to your app, one by one.

This approach is especially useful when using [`chat.postMessage`](/reference/methods/chat.postMessage) as a replacement to [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks).

## What isn't changing? {#what_not}

* Traditional Slack app usage of `oauth.access` remains unchanged. Keep on exchanging those tokens like you're used to.

## What happens if I do nothing? {#nothing}

If your app is _not_ part of the workspace app developer preview, you'll experience nothing.

If your app _is_ part of the preview:

* If you still use `oauth.token` when its retired on July 17, your workspace app will not be able to complete installations until you switch to `oauth.access` instead.
* Eventually `apps.permissions.info` will stop working. Use `apps.permissions.resources.list` and `apps.permissions.scopes.list` instead.

## When did this happen? {#when}

We made these changes today, April 17, 2018.

On **July 17, 2018**, `oauth.token` will retire and cease serving requests. `oauth.access` will be the canonical way to exchange verification codes for tokens for all Slack apps once more. `apps.permissions.info` will stop working.

## Tags:

* [Breaking change](/changelog/tags/breaking-change)
* [Announcement](/changelog/tags/announcement)
