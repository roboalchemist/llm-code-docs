Source: https://docs.slack.dev/changelog/2018-01-the-right-chat-write-for-workspace-token-apps

# The right chat:write for workspace token apps

January 11, 2018

Workspace apps are deprecated

[Learn more](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

Legacy workspace apps are deprecated and will retire in August 2021. Learn more.

We're simplifying some permission scopes as part of the workspace apps developer preview.

Beginning today, workspace apps must request [`chat:write`](/reference/scopes/chat.write) instead of `chat:write:user` during installation or when seeking elevated permissions.

Now `chat:write` represents your app's ability to post messages in the channels and contexts granted to it.

## What's changing? {#whats-changing}

Workspace apps currently requesting the _classic_ `chat:write:user` scope must begin asking for [`chat:write`](/reference/scopes/chat.write) instead.

Your app still uses [`chat.postMessage`](/reference/methods/chat.postMessage) and other methods the same way as before.

When receiving an authorization grant with `oauth.token` or `apps.permissions.info`, instead of receiving the `chat:write:user` scope, you'll receive `chat:write`.

## What isn't changing? {#what-isnt-changing}

### Traditional Slack apps have nothing to fear. {#traditional-slack-apps-have-nothing-to-fear}

Slack apps that are not part of the developer preview are not impacted by this change. Bot users are also left unharmed.

`chat:write:user` and `chat:write:bot` remain functional, distinct OAuth scopes for traditional Slack apps.

### Existing workspace token grants are already converted {#existing-workspace-token-grants-are-already-converted}

We automatically migrated existing grants for `chat:write:user` to `chat:write`. You won't need to re-negotiate existing workspace token installations.

## How do I prepare? {#how-do-i-prepare}

If your workspace app requests the `chat:write:user` scope to gain the ability to post messages, you'll need to request `chat:write` instead. It's a drop-in replacement.

## When is this happening? {#when-is-this-happening}

This change already happened, today, on January 11, 2018.

Something amiss? [Let us know](https://slack.com/help/requests/new).

**Tags:**

* [Breaking change](/changelog/tags/breaking-change)
* [Announcement](/changelog/tags/announcement)
