Source: https://docs.slack.dev/changelog/2018/04/01/scoping-file-rights-for-writes-in-workspace-token-apps

# Scoping file rights for writes in workspace token apps

April 1, 2018

Workspace apps are deprecated

[Learn more](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

We're simplifying some permission scopes as part of the workspace apps developer preview.

Beginning today, workspace apps must request [`files:write`](/reference/scopes/files.write) instead of `files:write:user` during installation or when seeking elevated permissions.

Now `files:write` represents your app's ability to upload and manage files.

Experiencing _déjà vu_? This is just like [that time](/changelog/2018-01-the-right-chat-write-for-workspace-token-apps) we did this for `chat:write`.

## What's changing? {#whats-changing}

Workspace apps currently requesting the _classic_ `files:write:user` scope must begin asking for [`files:write`](/reference/scopes/files.write) instead.

Your app still uses [`files.upload`](/reference/methods/files.upload) and other methods the same way as before.

When receiving an authorization grant with `oauth.token` or `apps.permissions.info`, instead of receiving the `files:write:user` scope, you'll receive `files:write`.

## What isn't changing? {#what-isnt-changing}

[`files:read`](/reference/scopes/files.read) is still `files:read`, whether you're working with a workspace app or otherwise.

### Traditional Slack apps have nothing to fear. {#traditional-slack-apps-have-nothing-to-fear}

Slack apps that are not part of the developer preview are not impacted by this change. Bot users are also left unharmed.

`files:write:user` and `files:write:bot` remain functional, distinct OAuth scopes for traditional Slack apps.

### Existing workspace token grants are already converted {#existing-workspace-token-grants-are-already-converted}

We automatically migrated existing grants for `files:write:user` to `files:write`. You won't need to re-negotiate existing workspace token installations.

## How do I prepare? {#how-do-i-prepare}

If your workspace app requests the `files:write:user` scope to gain the ability to post messages, you'll need to request `files:write` instead. It's a drop-in replacement.

## When is this happening? {#when-is-this-happening}

This change just happened, today, on April 17, 2018.

Something amiss? [Let us know](https://slack.com/help/requests/new).

**Tags:**

* [Breaking change](/changelog/tags/breaking-change)
* [announcement](/changelog/tags/announcement)
