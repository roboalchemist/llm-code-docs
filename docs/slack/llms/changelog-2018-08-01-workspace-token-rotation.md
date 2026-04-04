Source: https://docs.slack.dev/changelog/2018/08/01/workspace-token-rotation

# Workspace token rotation

August 1, 2018

Workspace apps are deprecated

[Learn more](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

Workspace apps use an **access token** to represent all the permissions granted to your app by a workspace.

Workspace tokens are so potent and powerful that apps should take great care to keep them safe and secret. We're releasing a OAuth 2.0-based token expiration and rotation system that will make workspace tokens short-lived while providing your app a secure means to refresh tokens as needed.

For more detail on the ins and outs of token rotation, check out our [full documentation](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

## What's changing? {#what}

We made OAuth 2.0-based token rotation flow available to [workspace apps](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

## How do I prepare? {#how}

Learn how to enable token rotation, use refresh tokens, expire tokens, and secure your app by following our guide to [rotating and refreshing credentials](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

Token rotation is supported by `node-slack-sdk` today: refer to its [refresh token docs](http://docs.slack.dev/tools/node-slack-sdk/web-api#using-refresh-tokens) to learn how. Python support is on the way.

## What if I do nothing? {#nothing}

If you aren't building a workspace app, nothing happens. Token rotation support is not available to traditional Slack apps.

If your workspace app is not marked as distributed and is only installed in its "home workspace," then enabling token rotation is optional but encouraged.

If you enable distribution for any workspace app, refreshing tokens will become required.

## When is this happening? {#when}

Token expiration, refresh tokens, and our OAuth 2.0 token refresh flow are all available now for workspace apps now. They aren't available for traditional apps yet.

**Tags:**

* [New feature](/changelog/tags/new-feature)
