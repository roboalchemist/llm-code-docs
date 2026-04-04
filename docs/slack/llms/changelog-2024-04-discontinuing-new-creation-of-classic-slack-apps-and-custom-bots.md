Source: https://docs.slack.dev/changelog/2024-04-discontinuing-new-creation-of-classic-slack-apps-and-custom-bots

# Discontinuing new creation of classic apps and legacy custom integration bots

April 2, 2024

As of **June 4, 2024**, you can no longer create new classic apps or legacy custom integration bot users. Read on to learn how this may impact you and your team.

After more than 10 years of platform evolution at Slack, there are just too many ways to create an app. Our oldest technique for creating bot users will no longer be available after **June 4, 2024**. Additionally, we're going to discontinue allowing creation of new "classic" apps, our oldest OAuth-based app model, which we superceded with our more granular permission model over four years ago.

Your existing classic apps and [legacy custom integration bot users](/legacy/legacy-custom-integrations/legacy-custom-integrations-bot-users) will continue functioning, though you will not be able to create new ones beginning on **June 4, 2024**.

## What's changing {#what}

Beginning **June 4, 2024**:

* The path [`https://api.slack.com/apps?new_classic_app=1`](https://api.slack.com/apps?new_classic_app=1) will stop working. You can create Slack apps from [app management](https://api.slack.com/apps) or explore app creation via the Slack CLI.
* The [custom bot legacy custom integration](https://slack.com/apps/A0F7YS25R-bots) found in the Slack Marketplace and in administrative locations will no longer allow you to create new bots or add them to Slack. Bot users may be added to workspaces by installing Slack apps.

## What isn't changing {#what-isnt-changing}

Existing classic apps and legacy custom integration bot users will continue operating. We recommend migrating existing legacy use cases.

## How do I prepare? {#how}

If you don't regularly create new classic apps or legacy custom integration bot users, there's nothing for you to do. You'll go on creating whatever it is you do create and building great things.

If you're still regularly creating new classic apps or custom bots, for example to use the legacy RTM API, you will need to choose from the available alternatives instead.

[This migration guide for classic apps](/legacy/legacy-app-migration/migrating-classic-apps) is helpful in understanding the key differences between app types.

[Create Slack apps](https://api.slack.com/apps) using the standard app management techniques.

Much of what people use bots and apps for can now be achieved with [Workflow Builder](https://slack.com/features/workflow-automation) and [coded workflows](/tools/deno-slack-sdk/guides/getting-started), which supports [Deno-flavored TypeScript](/tools/deno-slack-sdk/tutorials/workflow-builder-custom-step/) as well as custom steps for the Bolt framework (see our tutorials for [JavaScript](/tools/bolt-js/tutorials/custom-steps-workflow-builder-new) and [Python](/tools/bolt-python/tutorial/custom-steps-workflow-builder-new)).

It's possible you wanted to create a classic app or a legacy custom bot in order to use the legacy RTM API. Your best alternative is to use these same updated techniques, though you'll find that some of the quirks of the legacy RTM API, like presence subscriptions, do not have modern equivalents.

## What if I do nothing? {#nothing}

After **June 4, 2024** if you enter a situation where you typically would create a classic app or custom bot, you won't be able to. You'll have to create a Slack app. You might decide to read a book or write a letter to a friend. In any case, you can still learn and implement with our alternatives.

## When does this happen? {#when}

On **June 4, 2024** we'll stop allowing new creation of classic apps and legacy custom integration bot users.

* * *

If you have questions or concerns about our plans for classic apps or custom bots, please contact us.

**Tags:**

* [Deprecation](/changelog/tags/deprecation)
