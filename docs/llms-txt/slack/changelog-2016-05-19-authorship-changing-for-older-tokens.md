Source: https://docs.slack.dev/changelog/2016/05/19/authorship-changing-for-older-tokens

# Authorship changing for older tokens

May 19, 2016

Long ago, a small number of enterprising users and developers scoured through client-side code to discover embedded user tokens and began posting messages and performing other skunkworks operations with them. We applaud this adventurous spirit!

Today we take the first step in retiring usage of these antiquated tokens, by changing their behavior when used to post messages through [`chat.postMessage`](/reference/methods/chat.postMessage).

## What's changing: {#whats-changing}

These changes effect only outmoded tokens using `chat.postMessage`, which can be identified by their leading characters of `xoxo-` and `xoxs-`.

Instead of allowing the authoring identity to be altered using the `username`, `icon_url`, and `icon_emoji` parameters, messages posted with these outdated tokens will default to the original user's identity.

So if _@jane_ uses these tokens in a script to post as _@captain\_janeway_, posts will now be attributed to _@jane_. The tokens belong to _@jane_ after all.

## When it's happening: {#when-its-happening}

**Today** — this change is effective immediately. These tokens are seldom used and the impact on teams and workflows should be minimal.

## How to adapt: {#how-to-adapt}

We strongly suggest those using these vintage tokens to migrate to [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) or use [scoped OAuth tokens](/legacy/legacy-authentication/legacy-oauth-scopes) to continue posting with `chat.postMessage`.

Another viable, though discouraged option is to use [test tokens](/legacy/legacy-custom-integrations/legacy-custom-integrations-tokens).

We recommend migrating even if you're fine with this new behavior, as these tokens are not meant to be used for this purpose.

Please review the tokens you're using and adapt your usage as necessary. Have questions? We're happy to help! Feel free to contact us [here](https://slack.com/help/requests/new).

Thank you!

**Tags:**

* [Announcement](/changelog/tags/announcement)
