Source: https://docs.slack.dev/legacy/legacy-custom-integrations/legacy-custom-integrations-tokens

# Legacy custom integrations: tokens

Legacy tester tokens [may no longer be created.](/changelog/2020-02-legacy-test-token-creation-to-retire)

Legacy tester tokens were an early way to create tokens capable of doing anything a Slack user could do on Slack.

* * *

## Migrating from legacy tokens {#migrating-from-legacy}

If you were using a legacy token to make calls with the [Web API](/apis/web-api/), you'll need to generate a new one for your Slack app.

[Create an app](https://api.slack.com/apps?new_app=1)

For testing and development, you can quickly and easily [create a Slack app](/app-management/quickstart-app-settings) and install it in your workspace in just a few clicks. Your tokens are displayed after installation completes. See our [quickstart](/app-management/quickstart-app-settings) to get started... well, quickly.

You may then [use the app's settings](https://api.slack.com/apps) to progressively add additional permission scopes needed for testing, though you'll need to reinstall the app with each additional permission.

If you want to install in more than one workspace or to better customize scopes, follow our [guide to the OAuth flow](/authentication/installing-with-oauth). OAuth is required to install an app in multiple workspaces in an Enterprise organization. Then, [prepare it for distribution](/app-management/distribution).

* * *

## Legacy information {#legacy-info}

Though we recommend that all legacy custom integrations should [migrate to Slack apps](/legacy/legacy-custom-integrations/legacy-custom-integrations-migration), we also understand that some will still need to maintain older integrations. This section contains any information about using legacy tokens that is specific to the legacy implementation.

### Legacy token management {#token-mgmt}

Legacy tokens are just for you

Never share legacy tokens with other users or applications. Do not publish Legacy tokens in public code repositories. [Review token safety tips](/security).

Legacy tokens have the power of passwords, and should be treated with the same care. You should revoke them if they're not being used. Slack will automatically revoke any old tokens if unused for a long period of time.

## Legacy token capabilities {#capabilities}

Tokens generated with this tool were associated with the currently signed in user and team. Heed our warnings. **Build a Slack app instead.**

The tokens will automatically be granted the following scopes:

* `identify` - identifies your personal user information like name and team
* `read` - allows this token to request data about channels, messages, team members, and more
* `post` - allows this token to post content to your channels and perform other write actions like edit your profile
* `client` - allows this token to connect to the real time streaming API and perform most actions your user account is capable of throughout the Slack service
* `admin` - only attached if the current user is an admin for that team. Allows retrieval and modification of team-wide administrative information.

**These tokens provide access to your private data and that of your team.** Keep these tokens to yourself and do not share them with others. Tester tokens are not intended to replace Auth 2.0 tokens.

## Revoking legacy tokens {#revoke}

Unused legacy tokens are periodically invalidated by Slack. Use your tokens regularly to avoid automatic revocation.

The old interface allows you to manually re-issue existing tester tokens. They're listed as the **Slack API Tester** app.

Programmatically revoke your tester tokens by using them with the [`auth.revoke`](/reference/methods/auth.revoke) method.

Tester tokens detected in public GitHub repositories will be automatically revoked for your protection.
