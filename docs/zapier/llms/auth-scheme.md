# Source: https://docs.zapier.com/platform/manage/auth-scheme.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Change authentication type

> If your API's authentication method changes, you’ll also need to update how Zapier authenticates user accounts in your integration.

## Impact to users

Changing your integration's authentication type (e.g., Basic Auth, API Key, or OAuth) is considered a **breaking change**. Zapier does not currently support automatic migration between different auth types. This means that users would need to make a new connection to your integration and manually modify each of their Zaps.

Because of this implication, any authentication change should be planned carefully to minimize disruption.

## Best practices

**If you must change your authentication method**, we recommend the following:

### Designing a Smooth Transition

1. Ensure your API can support both the old and new auth methods during the transition period.
2. Avoid immediately invalidating the old authentication credentials (e.g., API keys) after issuing new ones, so users aren’t abruptly disconnected.

### Creating a New Version

* [Clone](/platform/manage/clone) your integration to create a new version.
* [Remove](/platform/build/auth#how-to-remove-or-change-zapier-integration-authentication-scheme) the current authentication method and implement the new one.
* Once tested and ready, [promote](/platform/manage/promote) this new version so new users connect using the updated auth type.

### Managing Existing Users

* If the old auth method can continue working for a while, keep the older version available. This allows users to maintain their existing connections temporarily.
* New Zaps will always default to the promoted version, so users will be asked to reconnect using the new auth type when setting up new workflows.

## What to do before changing auth types

Changing your integration’s authentication type has broad impact. Please [contact us](https://developer.zapier.com/contact) as early as possible to let us know your plans.

While we can’t currently guarantee support for migrating user accounts across auth types, starting the conversation early allows us to:

* Better understand your use case
* Provide tailored guidance
* Coordinate timing to reduce disruption for your users

## Deprecating legacy authentication scheme

If you plan to discontinue support for the old authentication method:

* You’ll need to [deprecate](/platform/manage/deprecate) the integration version that uses it.
* Be aware this may be disruptive for users and should be carefully planned.
* Make sure users are informed and given ample time to transition.

> NOTE: This process is not supported for apps built in the legacy web builder. To update the authentication method, you must rebuild all triggers, actions, and searches in the new builder. Simply deleting and re-adding the authentication method will not work with components built in the legacy builder.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
