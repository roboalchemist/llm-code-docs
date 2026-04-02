Source: https://docs.slack.dev/changelog/2023-07-its-later-already-for-stars-and-reminders

# It's later already for stars and reminders

July 31, 2023

Starting in March 2023, Slack began rolling out a new collection of features collectively called [**_Save it for Later_**](https://slack.com/help/articles/13453851074067-Save-it-for-Later). It gives you a new **_Later_** section on Slack where things you save for later (with or without a reminder attached to it) are kept.

This new collection of features replaces our previous **_Saved Items_** (also known as _starred items_, or just _stars_) and **_Reminders_** features.

As part of this new feature roll out, the existing APIs to interface with saved items and reminders have become degraded or useless. There are no direct APIs for **_Save it for Later_** to integrate with. With the current suite of built-in functions, web API methods, events, and triggers offered by Slack it is possible to recreate some (but certainly not all) use cases the impacted APIs supported.

We aim to give ample notice for every platform feature developers would consider a “breaking change.” We apologize we were unable to provide this information to developers ahead of the **_Save it for Later_** release.

## What changed? {#what}

Beginning March 2023, a number of APIs around saved items and reminders began to degrade as the new **_Save it for Later_** feature was made available to workspaces.

* [`reminders.add`](/reference/methods/reminders.add) - Reminders can only be set for another user with a bot token. The user argument is ignored and is effectively retired for user tokens.
* [`stars.list`](/reference/methods/stars.list) - Users no longer can create _stars_ or _saved items_ in the same way previously supported. This method is somewhat frozen in time and will not accurately reflect items the user would find in their _Later_ tab. This method will be retired.
* [`stars.add`](/reference/methods/stars.add) and [`stars.remove`](/reference/methods/stars.remove) - They will function but every act performed will have no user-facing impact. These methods will be retired.

## How do I prepare? {#how}

If your app relies on these methods, we recommend retiring the functionality in your app. APIs for **_Save it for Later_** are not yet available and we don’t have a timeline for when or if they'll be made available.

To create reminders for users, use the [scheduled trigger functionality](/tools/deno-slack-sdk/guides/creating-scheduled-triggers) built into workflow builder and our new [developer automation platform](/workflows).

## What if I do nothing? {#nothing}

The `stars.*` Web API methods will continue responding to your requests until they are retired. The **_Saved Items_** your app or integration work with using these methods won't be user-visible or impact the **_Later_** feature on Slack. Items a user stores with **_Later_** will not be returned to your app. Once these methods are fully retired, the API will return a `method_deprecated` error.

If you try to specify a `user` with `reminders.add` it will ignore the argument unless your app is using a bot token. Reminders will always be created for the same user who owns the token used to call `reminders.add`.

## When does this happen? {#when}

**_Save it for Later_** began gradually rolling out to users in March 2023. Everyone has it now. Expect the APIs mentioned above to be marked deprecated and to return the `method_deprecated` error once fully retired.

**Tags:**

* [Deprecation](/changelog/tags/deprecation)
* [Breaking change](/changelog/tags/breaking-change)
