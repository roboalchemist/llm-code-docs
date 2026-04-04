# Source: https://docs.zapier.com/platform/manage/versions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Versions

> Versions in Developer Platform allow developers to create multiple iterations of their integration to experiment with and implement new features without affecting existing users. Each integration can have many versions, but only one version can have a public status at a one time.

Versions allow you to have:

* **Seamless user experience**: Existing users have uninterrupted service, while new features are being tested and deployed.
* **Incremental upgrades**: Developers can facilitate phased roll outs of new features, allowing for thorough testing and feedback collection before full deployment.
* **Version management**: Developers have a structured approach to migrate users to updated versions and deprecate older versions when applicable.

## Version numbering

Zapier uses [semantic versioning](https://semver.org/) (semver) for integration versions. A version number has three parts: `MAJOR.MINOR.PATCH` (for example, `1.2.3`).

* **PATCH** version (e.g., `1.0.0` → `1.0.1`): For backward-compatible bug fixes, help text updates, or minor improvements that don't affect functionality
* **MINOR** version (e.g., `1.0.3` → `1.1.0`): For new features or functionality that don't break existing Zaps, such as adding new triggers or actions
* **MAJOR** version (e.g., `1.3.6` → `2.0.0`): For changes that break compatibility with existing Zaps, such as removing triggers/actions, changing authentication, or modifying required fields

Choosing the right version number helps communicate the impact of your changes to users and ensures appropriate migration paths.

### Labeled versions for development

In addition to semantic versions, you can use **labeled versions** while building features. These use a label suffix like `2.0.0-beta` or `0.0.0-my-feature` and let you defer version number decisions until you're ready. Learn more about [working with labeled versions](/platform/manage/labeled-versions).

## Managing versions in Platform UI

To manage your versions:

1. Log into the [Platform UI](https://zapier.com/app/developer).
2. Select your **integration**.
3. In the *Manage* section in the left sidebar, click your **Versions**.

This page shows a list of all versions of the integration, along with status, number of active users and active Zaps on each. For public integrations will also show the changelogs input when a new version is promoted.

<Frame><img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b443129368e61bdaa86c6f5a741fbe8a.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=a3e3165b6461c8fc5b2ff5a69ca9bc91" alt="" data-og-width="1185" width="1185" data-og-height="803" height="803" data-path="images/b443129368e61bdaa86c6f5a741fbe8a.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b443129368e61bdaa86c6f5a741fbe8a.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=705ce8eb0c80893ab8edff51827fb563 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b443129368e61bdaa86c6f5a741fbe8a.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=6c5904f307ecd5b4ec84e931f4f0a333 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b443129368e61bdaa86c6f5a741fbe8a.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=acce758b69f819d49db97b2b38e5432c 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b443129368e61bdaa86c6f5a741fbe8a.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=02c0aeb84143e96f8f53ffd7e5e1e5df 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b443129368e61bdaa86c6f5a741fbe8a.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=5bed4a0c0c403955059b21b3a38e8e57 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b443129368e61bdaa86c6f5a741fbe8a.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=65c5e757b1688659d310439ed81a5bf9 2500w" /></Frame>

Learn more on:

* [Work with labeled versions](/platform/manage/labeled-versions)
* [Clone a version](/platform/manage/clone)
* [Promote a version](/platform/manage/promote)
* [Migrate users to a new version](/platform/manage/migrate)
* [Deprecate or delete an version](/platform/manage/deprecate)

## Managing versions in Platform CLI

Integrations created with the Platform CLI cannot be edited in the Platform UI, however you can view the available versions in the Platform UI. You can also run the [`zapier-platform versions`](https://github.com/zapier/zapier-platform/blob/master/packages/cli/docs/cli.md#versions) command (or deprecated `zapier versions`) to see the same information in your local terminal.

### What do I do if I am blocked from promoting or migrating integration versions?

Zapier may fix bugs or add new features to your integration and release these as part of a new integration version.

In the event that Zapier has made changes to an integration version you own, you will be unable to do the following until you update your local files by running `zapier pull`:

* push changes to the promoted version
* promote a new version
* migrate from one version to another version

Run `zapier pull` to update your local files with the latest version and remove these restrictions. Any destructive file changes will prompt you with a confirmation dialog before continuing.

## Who can view your versions?

For public integrations, which are searchable in the Zap editor or in the app directory, a user who selects your integration in the Zap Editor will be using the current public version by default.

For both [private and public integrations](/platform/quickstart/private-vs-public-integrations), only team members added to the integration, or users with whom you have shared private versions with specifically, will see those versions as well.

### **How will my users identify a new version?**

As an integration admin, you will always see all the integration versions when connecting the app, but the end user should see only the published version.

For end users, the public version will be the one showing only the name of the integration, with no version number on it.

For private integrations, you can either invite the users to the new version via the users’ email addresses or use the sharing link to invite the users.

## Editing versions

To make sure that existing Zaps can continue to work consistently, the Developer Platform only allows you to edit versions that have a private status and have fewer than 5 users. Versions that are public or have more than 5 users will show a warning message prompting you to clone the version instead.

<Frame><img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b5cbf5a37ce60ba89eb555c0429eca6.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c95eecca846390ac131465d25ddb0edf" alt="" data-og-width="1179" width="1179" data-og-height="188" height="188" data-path="images/8b5cbf5a37ce60ba89eb555c0429eca6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b5cbf5a37ce60ba89eb555c0429eca6.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=edba2a5efd284df7f5731002b3f61f7d 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b5cbf5a37ce60ba89eb555c0429eca6.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=7f7a14aee25bf1bfbde3c4c5fc69f1bb 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b5cbf5a37ce60ba89eb555c0429eca6.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=291102bc217fc3edc22435017eabadeb 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b5cbf5a37ce60ba89eb555c0429eca6.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=632e4db57a09183612fe4663371aceda 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b5cbf5a37ce60ba89eb555c0429eca6.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=89b4ccabd13cc3abf32675938d52247e 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b5cbf5a37ce60ba89eb555c0429eca6.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9068bdd52050dac8193248f079b0a555 2500w" /></Frame>

When making integration updates in newer versions, consider the potential impact on user migration and existing Zaps. Ensuring your API and app integration on Zapier remains backwards compatible is crucial to [avoid disruption to users](/platform/manage/planning-changes).

### **Is there any way to bulk-update the API endpoints?**

While there's no automatic way to do this in the Platform UI, you might consider migrating your integration to the CLI, which can streamline the process of updating endpoints. You can find more information on how to export your integration to the Platform CLI in this guide: [Export Integration to Platform CLI](/platform/manage/export-cli).

If updating the base URL is your main concern, you could use environment variables to host the base URL. You can reference it using `{{process.env.YOUR_KEY}}`, which might make future bulk updates easier.

***

[*Need help? Tell us about your problem and we'll connect you with the right resource or contact support.*](https://developer.zapier.com/contact)
