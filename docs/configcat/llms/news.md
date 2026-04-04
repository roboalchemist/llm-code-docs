# Source: https://configcat.com/docs/news.md

# News & Product Updates

Copy page

Here, you'll find all the latest updates, enhancements, and new features we've added to our service. Stay tuned to this page to keep up with all the latest news from ConfigCat!

<!-- -->

## Feature flag evaluation in GitHub Actions[​](#feature-flag-evaluation-in-github-actions "Direct link to Feature flag evaluation in GitHub Actions")

#### Feb 2, 2026[​](#feb-2-2026 "Direct link to Feb 2, 2026")

We have released a new GitHub Action that can evaluate feature flags in GitHub workflows.

For more details about how to use the action, [see the documentation](https://configcat.com/docs/integrations/github-eval.md).

***

## Enhanced SDK key filtering with Proxy Profile selection rules[​](#enhanced-sdk-key-filtering-with-proxy-profile-selection-rules "Direct link to Enhanced SDK key filtering with Proxy Profile selection rules")

#### Jan 30, 2026[​](#jan-30-2026 "Direct link to Jan 30, 2026")

We're happy to announce that we improved the Proxy Profile's SDK key selection mechanism.

In addition to manual configuration, you can now build custom selection rules that respond to future product, config, and environment creation/deletion/renaming.

![Proxy Profile selection rules](/docs/assets/proxy/profile-selection-rules2.png)

For more details about how selection rules work, [see the documentation](https://configcat.com/docs/advanced/proxy/proxy-overview.md#selection-rules).

***

## New payment currencies (AUD, GBP) available[​](#new-payment-currencies-aud-gbp-available "Direct link to New payment currencies (AUD, GBP) available")

#### Jan 27, 2026[​](#jan-27-2026 "Direct link to Jan 27, 2026")

You can now pay your ConfigCat subscription in **Australian dollars (AUD)** and **British pounds (GBP)**, in addition to USD and EUR.

To switch from your current payment currency, contact [](mailto:sales@configcat.com)<sales@configcat.com>. We will help you with the change.

If you prefer another currency, just let us know at [](mailto:sales@configcat.com)<sales@configcat.com>. We will check what is possible and get back to you.

***

## More control over your Slack notifications[​](#more-control-over-your-slack-notifications "Direct link to More control over your Slack notifications")

#### Jan 19, 2026[​](#jan-19-2026 "Direct link to Jan 19, 2026")

Good news! We listened to your feedback and made our Slack integration more flexible.

You can now control whether Slack notifications show or hide sensitive targeting data. This gives more context in private channels, while keeping safe defaults for shared ones.

Until now, comparison values used with confidential (hashed) operators were always masked in Slack. This remains the default behavior.

From now on, you can optionally change this setting for existing Slack integrations on the [Integrations page](https://app.configcat.com/product/integrations).<br /><!-- -->When creating a new Slack integration, you will be asked during setup whether targeting rule values should be sent in cleartext.

No action is required to keep sensitive data hidden for existing integrations. We recommend keeping this setting disabled for shared or public Slack channels.

![Slack integration sensitive data](/docs/assets/news/slack-sensitive_192dpi.png)

***

## ConfigCat MCP Server[​](#configcat-mcp-server "Direct link to ConfigCat MCP Server")

#### Sept 30, 2025[​](#sept-30-2025 "Direct link to Sept 30, 2025")

We just released a new official ConfigCat's Model Context Protocol (MCP) Server. AI tools like Cursor can now interact with ConfigCat via our new MCP server.

* **Complete set of tools for ConfigCat's Public Management API operations** You can Create, Read, Update and Delete any entities like Feature Flags, Configs, Environments or Products within ConfigCat.
* **Enables your code editor to understand your feature flags** Integrate the appropriate ConfigCat SDK, implement feature flags in your project, remove Zombie (stale) flags and more.

[]()

For more info about how to set up the MCP server, [see Documentation](https://configcat.com/docs/advanced/mcp-server.md).

***

## Automatic ConfigCat Proxy configuration with Proxy profiles / OpenFeature Remote Evaluation Protocol[​](#automatic-configcat-proxy-configuration-with-proxy-profiles--openfeature-remote-evaluation-protocol "Direct link to Automatic ConfigCat Proxy configuration with Proxy profiles / OpenFeature Remote Evaluation Protocol")

#### Aug 22, 2025[​](#aug-22-2025 "Direct link to Aug 22, 2025")

We have two exciting [ConfigCat Proxy](https://configcat.com/docs/advanced/proxy/proxy-overview.md) related news:

1. From the [v2.0.0](https://github.com/configcat/configcat-proxy/releases/tag/v2.0.0) version, the Proxy has the ability to use [Proxy profiles](https://app.configcat.com/organization/proxy-profiles) to determine which SDK keys to download and distribute.

   info

   You need to be an Organization Admin to access the Proxy profiles page on the Dashboard.

   ![Proxy profiles page](/docs/assets/news/proxy-profiles.png)

   [See the documentation](https://configcat.com/docs/advanced/proxy/proxy-overview.md#1-automatic-configuration-with-proxy-profiles) for more information on how to set up your Proxy with profiles.

2. From the [v2.0.0](https://github.com/configcat/configcat-proxy/releases/tag/v2.0.0) version, the Proxy conforms to the [OpenFeature Remote Evaluation Protocol](https://github.com/open-feature/protocol) (OFREP), which means it can be used with OFREP compatible OpenFeature providers. [See the API documentation](https://configcat.com/docs/advanced/proxy/endpoints.md#openfeature-remote-evaluation-protocol-ofrep) for the OFREP implementation with usage examples.

***

## New SDK for JavaScript with Cloudflare Workers support[​](#new-sdk-for-javascript-with-cloudflare-workers-support "Direct link to New SDK for JavaScript with Cloudflare Workers support")

#### Aug 15, 2025[​](#aug-15-2025 "Direct link to Aug 15, 2025")

We just released the [new, revamped ConfigCat SDK for JavaScript platforms](https://configcat.com/docs/sdk-reference/js/overview/). Unlike the previous platform-specific SDKs, it ships as a [single, unified NPM package](https://www.npmjs.com/package/@configcat/sdk) that supports multiple JS environments.

![Unified NPM package](/docs/assets/news/unified-js-sdk_192dpi.png)

The new SDK combines and, thus, supersedes these SDKs:

* [ConfigCat SDK for JavaScript frontend applications](https://configcat.com/docs/sdk-reference/js/)
* [ConfigCat SDK for JavaScript Server-Side Rendered applications](https://configcat.com/docs/sdk-reference/js-ssr/)
* [ConfigCat SDK for Node.js](https://configcat.com/docs/sdk-reference/node/)
* [ConfigCat SDK for Chromium Extensions](https://github.com/configcat/js-chromium-extension-sdk)

The legacy SDKs remain available for use but won't receive new features and improvements any more. They will continue getting security updates until official support ends on August 31, 2026.

The new SDK maintains strong backward compatibility, so in most cases migration is simple and straightforward. For details, see the "Migration to the new SDK" section in the SDK references linked above.

But there are other advantages to upgrading to the new SDK sooner rather than later:

* Most notably, it adds support for **Deno**, **Bun** and **Cloudflare Workers**. Plus, makes the Browser and Chromium Extension SDKs work in **Web Workers** too.
* Another improvement worth mentioning is that the new SDK is a **zero-dependency library**, which can spare you some package management-related headaches. It distributes **ES2017-compatible code** to allow you to minimize the library's footprint in your application bundles.
* A nice new feature is **query string-based flag overrides** (especially handy during development) and the possibility of **custom flag override data sources** - even with full feature flags, not just simple values (useful for testing).
* Then there is a **new hook** named `configFetched` for observing config fetch errors and **new options** named `configFetcher` and `logFilter` for customizing config fetching and logging.
* Error reporting received nice improvements as well: among others, the SDK now includes **error codes** to help identify error causes.

For the full list of new features and improvements, take a look at the [release notes](https://github.com/configcat/js-unified-sdk/releases/tag/v1.0.0).

***

## New ConfigCat OpenFeature providers[​](#new-configcat-openfeature-providers "Direct link to New ConfigCat OpenFeature providers")

#### July 4, 2025[​](#july-4-2025 "Direct link to July 4, 2025")

We're happy to share that we have released new OpenFeature providers for the following platforms:

* [Angular](https://configcat.com/docs/sdk-reference/openfeature/angular.md)
* [React](https://configcat.com/docs/sdk-reference/openfeature/react.md)
* [NestJS](https://configcat.com/docs/sdk-reference/openfeature/nestjs.md)
* [Swift (iOS)](https://configcat.com/docs/sdk-reference/openfeature/swift.md)
* [Kotlin (Android)](https://configcat.com/docs/sdk-reference/openfeature/kotlin.md)
* [Ruby](https://configcat.com/docs/sdk-reference/openfeature/ruby.md)

[See the documentation](https://configcat.com/docs/sdk-reference/openfeature/overview.md) for the complete list of currently supported platforms.

***

## Quality of Life improvements[​](#quality-of-life-improvements "Direct link to Quality of Life improvements")

#### Jun 3, 2025[​](#jun-3-2025 "Direct link to Jun 3, 2025")

We've just rolled out a set of updates that make working with feature flags in ConfigCat smoother and more practical. Here's what's new:

### Zombie flag Report improvements[​](#zombie-flag-report-improvements "Direct link to Zombie flag Report improvements")

Stale feature flags can build up quickly and lead to technical debt. We've improved the Zombie Flags feature to make it more useful and easier to manage:

* **New Zombie Flags page** The original email report didn't offer immediate feedback. That's why we created the new [Zombie Flags page](https://app.configcat.com/product/zombie-flags), where you can instantly view stale flags and filter them by product. If you're using our [Code References](https://configcat.com/docs/advanced/code-references/overview.md) feature, the page also shows exactly where the flags appear in your code, making it easier to clean things up.
* **Ignore flags by tag** If you have long-lived feature flags that are meant to stay, you can now tag them (for example, with “permanent”) and exclude them from the Zombie Flags Report.
* **Less noise, more focus** The previous report included any flag that was stale in at least one selected environment. Now, you can adjust the settings so only flags that are stale in all selected environments appear in the report.
* **Now available via API** You can also check stale flags programmatically using the [Zombie (stale) flags](https://configcat.com/docs/api/reference/get-staleflags.md) endpoint in our Public Management API.

Narrow down your [Zombie Flags Report](https://app.configcat.com/my-account/zombie-flags-report) email with the new preferences, try out our new [Zombie Flags page](https://app.configcat.com/product/zombie-flags), or check the [documentation](https://configcat.com/docs/zombie-flags.md) to learn more.

![Zombie Flags page](/docs/assets/news/zombie-page_192dpi.png)

### Clone feature flag[​](#clone-feature-flag "Direct link to Clone feature flag")

Cloning a feature flag now lets you quickly create a new flag in any config. It copies over all the targeting rules, values across environments, and tags, making setup faster and more consistent.

![Clone feature flag](/docs/assets/news/clone-feature-flag_192dpi.png)

### Copy all feature flag rules[​](#copy-all-feature-flag-rules "Direct link to Copy all feature flag rules")

We've made it easier to copy flag values across environments. Now, you can:

* Copy rules for an entire config, or
* Choose specific feature flags to copy.

![Copy all feature flag rules](/docs/assets/news/copy-all-feature-flag-values_192dpi.png)

### A Smoother Flag Creation Experience[​](#a-smoother-flag-creation-experience "Direct link to A Smoother Flag Creation Experience")

When creating a new feature flag, you no longer have to set values separately for each environment. You can now set them once globally, then fine-tune as needed later.

We truly hope you'll love these new features and improvements. Happy feature flagging! ❤️

***

## 🚀 Refer & Earn with ConfigCat[​](#-refer--earn-with-configcat "Direct link to 🚀 Refer & Earn with ConfigCat")

#### May 30, 2025[​](#may-30-2025 "Direct link to May 30, 2025")

Earn up to **$10,000 per referral** just by sharing something you already love.

### Here’s how it works:[​](#heres-how-it-works "Direct link to Here’s how it works:")

* 👥 The people you refer get **10% off** any paid plan.
* 💰 You earn **20% of their payments**, up to **$10,000 per referral**.
* 💸 Get paid via **PayPal** (more payout options coming soon).
* 🔗 Share your unique referral link via **email, LinkedIn, or QR code** – powered by [Cello](https://cello.so/).

![Refer and Earn](/docs/assets/news/refer-and-earn.png)

![Refer and Earn](/docs/assets/news/invite.png)

> This isn’t just a referral program - it’s our way of saying *thank you* for being part of the ConfigCat community.<br /><!-- -->You help us grow, and we make sure you benefit too.

✅ No cold outreach. No contact sharing. You're simply sharing something you already use and like.

**Ready to start earning?**<br /><!-- -->Click the **“Refer & Earn”** button in your ConfigCat dashboard and let the rewards roll in.

***

## User provisioning (SCIM) is here\![​](#user-provisioning-scim-is-here "Direct link to User provisioning (SCIM) is here!")

#### May 21, 2025[​](#may-21-2025 "Direct link to May 21, 2025")

**We're happy to announce that ConfigCat now supports user provisioning using SCIM (System for Cross-domain Identity Management)!**

SCIM makes it easy to sync users and groups from your Identity Provider into your ConfigCat Organization. Once synced, you can link Identity Provider groups to ConfigCat permission groups, so users are placed in the right roles without manual work.

We've tested the feature with [Entra ID (Azure AD)](https://configcat.com/docs/advanced/team-management/scim/identity-providers/entra-id.md), [Okta](https://configcat.com/docs/advanced/team-management/scim/identity-providers/okta.md) and [OneLogin](https://configcat.com/docs/advanced/team-management/scim/identity-providers/onelogin.md), but any Identity Provider that supports the SCIM 2.0 protocol should work too.

SCIM provisioning is available on all ConfigCat plans, including the Free plan. Each plan includes limits for synced users, groups, and permission assignments. See details [here](https://configcat.com/docs/subscription-plan-limits.md).

Read our [documentation](https://configcat.com/docs/advanced/team-management/scim/scim-overview.md) and set up the User provisioning on the [Authentication & Provisioning](https://app.configcat.com/organization/authentication) page in your ConfigCat Dashboard.

info

You'll need to be an Organization Admin to access it.

![Identity Provider groups](/docs/assets/news/scim-groups.png)

![Identity Provider users](/docs/assets/news/scim-users.png)

***

## Import from LaunchDarkly is here\![​](#import-from-launchdarkly-is-here "Direct link to Import from LaunchDarkly is here!")

#### Apr 29, 2025[​](#apr-29-2025 "Direct link to Apr 29, 2025")

**Thinking about moving away from LaunchDarkly? ConfigCat just made that easier for you.**

If you're curious about switching to a LaunchDarkly alternative, ConfigCat has good news for you: we've launched a new feature called the "Import from LaunchDarkly" tool, which makes it a breeze to migrate LaunchDarkly feature flags and segments into ConfigCat.

It's available on all plans, even the Free plan. So if you're just exploring, you can give it a go with zero commitment. (Just a heads-up: your plan's limits still apply. If you bump into anything, [contact us](https://configcat.com/support/?prefilled=ld-import-limit), and we'll surely figure out a solution for you!)

You can find the import tool on the [Organization Overview](https://app.configcat.com/organization) page in your ConfigCat Dashboard:

![Launching the import tool](/docs/assets/migration-from-launchdarkly/launch-import-tool_192dpi.png)

info

You'll need to be an Organization Admin to access it.

If you decide to make the full switch, we've prepared a [migration guide](https://configcat.com/docs/advanced/migration-from-launchdarkly.md) to walk you through the whole process.

So why not make the jump? You'll land on your paws anyway. <!-- -->🐱

***

## Price Adjustment & Smart Plan Update[​](#price-adjustment--smart-plan-update "Direct link to Price Adjustment & Smart Plan Update")

#### Feb 17, 2025[​](#feb-17-2025 "Direct link to Feb 17, 2025")

As of 17th February 2025, we've made the following updates:

### Price adjustment[​](#price-adjustment "Direct link to Price adjustment")

Due to changes in the EUR-USD exchange rate, we've made an adjustment to our prices:

* Our EUR plans will have a 10% increase
* Our USD plans will have a 1% increase

This applies only to new upgrades and future customers.

### Smart plan Update[​](#smart-plan-update "Direct link to Smart plan Update")

* The Smart Plan now has a product limit of 10.

Existing Smart plan customers are not affected by this change.

***

## What's new in 2025[​](#whats-new-in-2025 "Direct link to What's new in 2025")

#### Jan 20, 2025[​](#jan-20-2025 "Direct link to Jan 20, 2025")

We have a few important updates to share with you, including new integrations, changes to our pricing, and some highly requested features. Here's what's happening:

### 🚀 ConfigCat now available in JetBrains Marketplace[​](#-configcat-now-available-in-jetbrains-marketplace "Direct link to 🚀 ConfigCat now available in JetBrains Marketplace")

We're happy to announce that the ConfigCat Feature Flag plugin is now available on the JetBrains Marketplace. You can now manage your feature flags directly from 15 supported JetBrains IDEs. Check out the plugin [here](https://configcat.com/docs/integrations/intellij/).

### 🌓 Dark Mode & UI Facelift[​](#-dark-mode--ui-facelift "Direct link to 🌓 Dark Mode & UI Facelift")

Dark Mode has been one of the most requested features, and we're happy to announce that it's now available!<br /><!-- -->Plus, we've given the UI a fresh, modern look to make things even easier and more enjoyable to use.

![Darkmode](/docs/assets/news/darkmode.png)

### 💳 Multiple Payment Sources[​](#-multiple-payment-sources "Direct link to 💳 Multiple Payment Sources")

You can now add backup credit cards to your organization, making your payments more flexible and secure.

### 📈 Price adjustments and Plan updates[​](#-price-adjustments-and-plan-updates "Direct link to 📈 Price adjustments and Plan updates")

We're making a few changes to our pricing plans, which will take effect on 17th February 2025.

* *Price adjustment* Over the past few years, the constantly fluctuating USD/EUR exchange rate has significantly widened the gap between our EUR and USD pricing. We're making adjustments to bring these prices closer together:

  <!-- -->

  * Our EUR plans will have a 10% increase
  * Our USD plans will have a 1% increase This change will only apply to upgrades and will affect future customers starting on the 17th February 2025.

* *Updates to Free and Smart plans*

  * Free Plan: The Product limit has been increased to 2. Existing Free plan users have automatically received this benefit.
  * Smart Plan (effective from 17 February 2025): The Product limit will be capped at 10. Existing Smart plan customers will not be affected by this change.

***

## Disable two-factor authentication permission[​](#disable-two-factor-authentication-permission "Direct link to Disable two-factor authentication permission")

#### Oct 8, 2024[​](#oct-8-2024 "Direct link to Oct 8, 2024")

You can disable two-factor authentication for your team members. This feature is useful if someone loses the device used for two-factor authentication.

*Only team members with Organization Admin role or with 'Can disable two-factor authentication for other team members' permission can disable two-factor authentication.*

[Open Team Members page on our Dashboard](https://app.configcat.com/product/members)

***

## Introducing ConfigCat Playground: Test Feature Flags Easily in a safe environment[​](#introducing-configcat-playground-test-feature-flags-easily-in-a-safe-environment "Direct link to Introducing ConfigCat Playground: Test Feature Flags Easily in a safe environment")

#### Sept 26, 2024[​](#sept-26-2024 "Direct link to Sept 26, 2024")

We've just released the ConfigCat Playground, a simulator that provides a safe virtual environment where you can try out everything ConfigCat has to offer.

This new feature gives you virtual devices and a virtual app that can be connected to your ConfigCat feature flags. This lets you test feature flags and targeting rules without needing to connect any real applications.

Please do not use the Playground with feature flags already connected to live applications. We highly recommend using feature flags from non-production environments when experimenting in the Playground.

To get started, simply click on the **"Test in Playground"** option in the **...** menu of any boolean feature flag inside your ConfigCat Dashboard.

![ConfigCat Playground](/docs/assets/news/playground.png) ![Test in Playground option in the ... menu](/docs/assets/news/playground-context-menu.png)

***

## New ConfigCat OpenFeature providers[​](#new-configcat-openfeature-providers-1 "Direct link to New ConfigCat OpenFeature providers")

#### Sept 6, 2024[​](#sept-6-2024 "Direct link to Sept 6, 2024")

We're happy to share that we have released new OpenFeature providers for the following platforms:

* [PHP](https://configcat.com/docs/sdk-reference/openfeature/php.md)
* [Python](https://configcat.com/docs/sdk-reference/openfeature/python.md)
* [Rust](https://configcat.com/docs/sdk-reference/openfeature/rust.md)

[See the documentation](https://configcat.com/docs/sdk-reference/openfeature/overview.md) for the complete list of currently supported platforms.

***

## Integration management via Public Management API and Terraform[​](#integration-management-via-public-management-api-and-terraform "Direct link to Integration management via Public Management API and Terraform")

#### Aug 13, 2024[​](#aug-13-2024 "Direct link to Aug 13, 2024")

From now on, you can manage your Integrations through the ConfigCat Public Management API and Terraform provider. See the docs for details:

* ConfigCat Public Management API: use the [Integrations](https://api.configcat.com/docs/index.html#tag/Integrations) endpoints.

* ConfigCat Feature Flags Provider for Terraform: use the [configcat\_integration ](https://registry.terraform.io/providers/configcat/configcat/latest/docs/resources/integration)resource.

***

## New ConfigCat SDK for Unreal Engine[​](#new-configcat-sdk-for-unreal-engine "Direct link to New ConfigCat SDK for Unreal Engine")

#### Jul 31, 2024[​](#jul-31-2024 "Direct link to Jul 31, 2024")

We just released a new official ConfigCat SDK supporting Unreal Engine applications.

![ConfigCat SDK for Unreal Engine](/docs/assets/news/unreal.jpg)

[See Documentation](https://configcat.com/docs/sdk-reference/unreal.md)

***

## New ConfigCat SDK for Rust[​](#new-configcat-sdk-for-rust "Direct link to New ConfigCat SDK for Rust")

#### Jul 19, 2024[​](#jul-19-2024 "Direct link to Jul 19, 2024")

We just released a new official ConfigCat SDK supporting Rust applications.

[See Documentation](https://configcat.com/docs/sdk-reference/rust.md)

***

## Ability to connect multiple integrations[​](#ability-to-connect-multiple-integrations "Direct link to Ability to connect multiple integrations")

#### Jun 27, 2024[​](#jun-27-2024 "Direct link to Jun 27, 2024")

We're happy to share that we have added the ability to connect multiple [integrations](https://app.configcat.com/integrations) of the same type.<br />Moreover, it's now possible to apply environment/config filters on each individual integration.

![Multiple integrations menu](/docs/assets/news/multi_integ_1.png) ![Multiple integrations dialog](/docs/assets/news/multi_integ_2.png)

***

## Advanced feature flag analytics with Twilio Segment[​](#advanced-feature-flag-analytics-with-twilio-segment "Direct link to Advanced feature flag analytics with Twilio Segment")

#### Jun 14, 2024[​](#jun-14-2024 "Direct link to Jun 14, 2024")

We're happy to share that we have introduced a new way to track your feature flags in your analytics tools. From now on you can [send feature flag change events and](https://configcat.com/docs/integrations/segment.md#changeevents) and [send feature flag evaluation analytics](https://configcat.com/docs/integrations/segment.md#analytics) to Twilio Segment.

***

## Introducing the ConfigCat Feature Flags Tutorial[​](#introducing-the-configcat-feature-flags-tutorial "Direct link to Introducing the ConfigCat Feature Flags Tutorial")

#### Jun 11, 2024[​](#jun-11-2024 "Direct link to Jun 11, 2024")

We're excited to launch our [Feature Flags Tutorial](https://tutorial.configcat.com/?lm=13), a comprehensive guide designed to enhance your skills in feature management. This tutorial covers everything from basic toggling and simple targeting to advanced techniques like percentage rollouts and handling rollbacks.

![Feature Flags Tutorial](/docs/assets/news/tutorial_192dpi.png)

### Tutorial Highlights:[​](#tutorial-highlights "Direct link to Tutorial Highlights:")

* Begin with toggling a feature flag on and off to see its immediate impact on a user interface, simulating real-world user scenarios.
* Simple Targeting: Learn to apply basic targeting rules by enabling a feature for all users except those in a specific country.
* Dogfooding: Practice internal testing by setting the feature to be visible only to users from your company.
* Percentage Rollout: Advance to partial feature deployment by enabling a new feature for a percentage of your users, testing its acceptance incrementally.
* Rollback: Master the ability to quickly revert changes for specific user groups when encountering issues during rollout.

This step-by-step guide is ideal for anyone looking to integrate feature flags into their projects efficiently.

[Explore the Tutorial](https://tutorial.configcat.com/?lm=14)

***

## Advanced feature flag analytics with Mixpanel, Amplitude and Google Analytics[​](#advanced-feature-flag-analytics-with-mixpanel-amplitude-and-google-analytics "Direct link to Advanced feature flag analytics with Mixpanel, Amplitude and Google Analytics")

#### May 15, 2024[​](#may-15-2024 "Direct link to May 15, 2024")

We're happy to share that we have introduced new ways to track your feature flags in your analytics tools.

From now on you can:

* [Monitor feature flag change events in Mixpanel with Annotations](https://configcat.com/docs/integrations/mixpanel/#annotations)
* [Send feature flag evaluation analytics to Mixpanel Experiments](https://configcat.com/docs/integrations/mixpanel/#experiments)
* [Send feature flag evaluation analytics to Amplitude Experiments](https://configcat.com/docs/integrations/amplitude/#experiments)
* [Send feature flag evaluation analytics to Google Analytics](https://configcat.com/docs/integrations/google-analytics)

***

## Webhook and Product preference management in Public Management API and Terraform[​](#webhook-and-product-preference-management-in-public-management-api-and-terraform "Direct link to Webhook and Product preference management in Public Management API and Terraform")

#### May 8, 2024[​](#may-8-2024 "Direct link to May 8, 2024")

From now on, you can manage your Webhooks and Product preferences through the ConfigCat Public Management API and the Terraform provider. See the docs for details:

* ConfigCat Public Management API: use the [Webhooks ](https://api.configcat.com/docs/index.html#tag/Webhooks), [Get Product Preferences](https://api.configcat.com/docs/index.html#tag/Products/operation/get-product-preferences) and [Update Product Preferences](https://api.configcat.com/docs/index.html#tag/Products/operation/update-product-preferences) endpoints.

* ConfigCat Feature Flags Provider for Terraform: use the [configcat\_webhook ](https://registry.terraform.io/providers/configcat/configcat/latest/docs/resources/webhook)and [configcat\_product\_preferences](https://registry.terraform.io/providers/configcat/configcat/latest/docs/resources/product_preferences) resources.

***

## ConfigCat Proxy Released\![​](#configcat-proxy-released "Direct link to ConfigCat Proxy Released!")

#### Apr 17, 2024[​](#apr-17-2024 "Direct link to Apr 17, 2024")

We're happy to announce the official release of [ConfigCat Proxy](https://github.com/configcat/configcat-proxy). 🎉

ConfigCat Proxy allows you to host feature flag evaluation service in your own infrastructure.<br /><!-- -->The Proxy provides the following:

🚀 **Performance**: Faster evaluation for stateless or short-lived apps.<br />🦾 **Reliability**: Continuous operation, even if ConfigCat CDN is down.<br />🔐 **Security**: Protect config JSON files from exposure to frontend and mobile apps.<br />📈 **Scalability**: Easily handle varying application loads.<br />📡 **Streaming**: Real-time feature flag change notifications via SSE and gRPC.<br />

Learn more about ConfigCat Proxy [here](https://configcat.com/docs/advanced/proxy/proxy-overview/).

***

## Introducing Config V2: More Powerful Feature Flagging\![​](#introducing-config-v2-more-powerful-feature-flagging "Direct link to Introducing Config V2: More Powerful Feature Flagging!")

#### Apr 05, 2024[​](#apr-05-2024 "Direct link to Apr 05, 2024")

We're thrilled to announce the upcoming launch of Config V2, the next generation of ConfigCat. This major update introduces a number of enhancements including a revamped Dashboard, Public Management API, updated SDKs, and a host of new features designed to streamline your feature flag and configuration management experience.

### What's New in Config V2?[​](#whats-new-in-config-v2 "Direct link to What's New in Config V2?")

* A modernized config editor UI for an enhanced Dashboard experience.
* Advanced targeting rules with AND conditions for more precise user targeting.
* New comparators and prerequisite flags for complex rule creation.

### Gradual Release & Opt-in[​](#gradual-release--opt-in "Direct link to Gradual Release & Opt-in")

Config V2 will be rolled out gradually over the next three months. Interested customers are encouraged to opt-in early by [contacting our support team](https://configcat.com/support/)

### Seamless Migration, No Immediate Changes Required[​](#seamless-migration-no-immediate-changes-required "Direct link to Seamless Migration, No Immediate Changes Required")

Post-release, rest assured that your existing configurations will continue to function just as before. There's no immediate pressure to migrate, allowing you to transition to Config V2 when it suits you best.

Here is a [detailed guide](https://configcat.com/docs/advanced/config-v2/) to know more about Config V2 and the new features.

***

## ConfigCat customer experience survey[​](#configcat-customer-experience-survey "Direct link to ConfigCat customer experience survey")

#### Mar 22, 2024[​](#mar-22-2024 "Direct link to Mar 22, 2024")

Please take a moment to share your experience with ConfigCat. Fill out [this survey](https://forms.gle/VepSDp3pF9FCVzAE9) and help us improve our product!<br /><!-- -->Thank you for your time! 🙏

***

## Join the Config V2 Beta Program[​](#join-the-config-v2-beta-program "Direct link to Join the Config V2 Beta Program")

#### Jan 19, 2024[​](#jan-19-2024 "Direct link to Jan 19, 2024")

We're looking for ConfigCat users willing to participate in the beta testing of Config V2.

### What is Config V2?[​](#what-is-config-v2 "Direct link to What is Config V2?")

Config V2 is a new version of ConfigCat. It brings together a bundle of highly requested features like AND conditions, new comparators (Text Equals, Text Starts with Any of, Text Ends with Any of, Before/After), Prerequisite flags, and more. [Read more about Config V2 and the new features.](https://configcat.com/docs/advanced/config-v2.md)

You can get early access to the new features and shape the final product with your feedback.

### How to join the beta program?[​](#how-to-join-the-beta-program "Direct link to How to join the beta program?")

1. [Apply via this form](https://forms.gle/wEFxKYs5Lv5iiLUF8)
2. Join the **#config-v2-beta-testing** channel in our [Community Slack](https://configcat.com/slack/) to give feedback.

***

## Resource ordering in Public Management API and Terraform[​](#resource-ordering-in-public-management-api-and-terraform "Direct link to Resource ordering in Public Management API and Terraform")

#### Jan 9, 2024[​](#jan-9-2024 "Direct link to Jan 9, 2024")

From now on, you can change the order of your products, configs and environments trough the ConfigCat Public Management API and the Terraform provider. See the docs for details:

* *ConfigCat Public Management API*: specify the order argument in the [Products](https://configcat.com/docs/api/reference/products.md), [Configs](https://configcat.com/docs/api/reference/configs.md), [Environment](https://configcat.com/docs/api/reference/environments.md) and [Feature Flags & Settings](https://configcat.com/docs/api/reference/feature-flags-settings.md) endpoints
* *ConfigCat Feature Flags Provider for Terraform*: specify the order argument of the [configcat\_product](https://registry.terraform.io/providers/configcat/configcat/latest/docs/resources/product#argument-reference), [configcat\_config](https://registry.terraform.io/providers/configcat/configcat/latest/docs/resources/config#argument-reference), [configcat\_environment](https://registry.terraform.io/providers/configcat/configcat/latest/docs/resources/environment#argument-reference) and [configcat\_setting](https://registry.terraform.io/providers/configcat/configcat/latest/docs/resources/setting#argument-reference).

***

## ConfigCat OpenFeature Providers available[​](#configcat-openfeature-providers-available "Direct link to ConfigCat OpenFeature Providers available")

#### Jan 5, 2024[​](#jan-5-2024 "Direct link to Jan 5, 2024")

OpenFeature now supports ConfigCat via dedicated providers for their SDKs. So if you prefer using ConfigCat via the OpenFeature API, you can now do so with the following providers:

* [ConfigCat OpenFeature Provider for Java](https://github.com/open-feature/java-sdk-contrib/tree/main/providers/configcat)
* [ConfigCat OpenFeature Provider for Go](https://github.com/open-feature/go-sdk-contrib/tree/main/providers/configcat)
* [ConfigCat OpenFeature Provider for JavaScript](https://github.com/open-feature/js-sdk-contrib/tree/main/libs/providers/config-cat)

***

## ConfigCat Proxy Beta[​](#configcat-proxy-beta "Direct link to ConfigCat Proxy Beta")

#### Nov 17, 2023[​](#nov-17-2023 "Direct link to Nov 17, 2023")

We're happy to share that the ConfigCat Proxy is now in the Beta phase and we need your help to make it even better!

📚 Want to learn more about the ConfigCat Proxy? Get all the details [here](https://configcat.com/docs/advanced/proxy/proxy-overview.md).

🔧 We'd like to invite you to participate in the beta testing. If you're interested, join the dedicated **#configcat-proxy-beta** channel in our [Slack Community](https://configcat.com/slack). Share your experiences, ask questions, and collaborate with our team and fellow community members.

***

## New cleartext comparators in Segments[​](#new-cleartext-comparators-in-segments "Direct link to New cleartext comparators in Segments")

#### Oct 26, 2023[​](#oct-26-2023 "Direct link to Oct 26, 2023")

ConfigCat now supports two new cleartext comparators: IS ONE OF and IS NOT ONE OF.

![New cleartext comparators](/docs/assets/images/isoneofcleartext-ac6dd72b09032cd397f39bccd1651c2f.png)

These new comparators allow you to check if a given value is part of a list or not. This is in addition to the hashed confidential versions that were previously available.

***

## Unique tag names[​](#unique-tag-names "Direct link to Unique tag names")

#### Oct 4, 2023[​](#oct-4-2023 "Direct link to Oct 4, 2023")

Now, tag names within a product must be unique. This new feature ensures better organization and avoids any potential confusion with colliding tag names.

***

## Manage Permission Groups with Terraform[​](#manage-permission-groups-with-terraform "Direct link to Manage Permission Groups with Terraform")

#### Aug 23, 2023[​](#aug-23-2023 "Direct link to Aug 23, 2023")

Introducing Permission Group management in [**ConfigCat Feature Flags Provider for Terraform**](https://registry.terraform.io/providers/configcat/configcat/latest/docs)! Use the [**configcat\_permission\_group**](https://registry.terraform.io/providers/configcat/configcat/latest/docs/resources/permission_group) resource for control and the [**configcat\_permission\_groups**](https://registry.terraform.io/providers/configcat/configcat/latest/docs/data-sources/permission_groups) data source for access to existing Permission Groups.

***

## Some updates regarding SLA guaranteed Uptime[​](#some-updates-regarding-sla-guaranteed-uptime "Direct link to Some updates regarding SLA guaranteed Uptime")

#### Aug 15, 2023[​](#aug-15-2023 "Direct link to Aug 15, 2023")

We're excited to announce important updates to our Service Level Agreement (SLA) concerning uptime commitments.

We're increasing our uptime commitment for the following plans:

| Uptime Changes  | Previous | Current         |
| --------------- | -------- | --------------- |
| Free Plan       | 99%      | 99% (No Change) |
| Pro Plan        | 99.8%    | 99.9%           |
| Smart Plan      | 99.9%    | 99.95%          |
| Enterprise Plan | 99.9%    | 99.99%          |
| Dedicated Plan  | 99.9%    | 99.99%          |

By enhancing our SLA terms, we aim to provide a more consistent and trustworthy service that you can depend on, day in and day out.

***

## Old SDKs will stop working after October 1st, 2023[​](#old-sdks-will-stop-working-after-october-1st-2023 "Direct link to Old SDKs will stop working after October 1st, 2023")

#### Aug 10, 2023[​](#aug-10-2023 "Direct link to Aug 10, 2023")

All ConfigCat SDKs released before Feb, 2020 will stop working after October 1st, 2023. Please, upgrade all your SDKs to the latest.

Although we aim to keep older SDK versions functional, those trailing more than one major or minor release lack official support and SLA. Many of these outdated SDKs will no longer remain functional.

### Affected SDKs and versions[​](#affected-sdks-and-versions "Direct link to Affected SDKs and versions")

| SDK Type | Latest available version | Will stop working |
| -------- | ------------------------ | ----------------- |
| Python   | v8.0.0                   | < v3.0.2          |
| Ruby     | v7.0.0                   | < v2.0.3          |
| .NET     | v8.2.0                   | < v4.0.0          |
| Go       | v8.0.0                   | < v4.0.0          |
| Java     | v8.2.2                   | < v4.0.0          |
| Android  | v9.0.1                   | < v4.0.0          |
| JS       | v8.1.0                   | < v3.0.0          |
| JS-SSR   | v7.1.0                   | < v1.0.2          |
| Node     | v10.1.0                  | < v4.0.0          |
| PHP      | v7.1.1                   | < v3.0.2          |
| Swift    | v9.4.0                   | < v4.0.0          |

***

## Introducing Network Traffic limits for all plans[​](#introducing-network-traffic-limits-for-all-plans "Direct link to Introducing Network Traffic limits for all plans")

#### Aug 1, 2023[​](#aug-1-2023 "Direct link to Aug 1, 2023")

We are introducing [**Network Traffic**](https://configcat.com/docs/network-traffic.md) limits for all plans. The usage is based on the Network Traffic your applications are making to the ConfigCat CDN.

### Why are we introducing these limits?[​](#why-are-we-introducing-these-limits "Direct link to Why are we introducing these limits?")

Our cloud provider charges us for the Network Traffic we use to serve your feature flags. By introducing these limits, we can cover these costs and continue providing the service. Instead of raising prices for all users in general, we decided to specifically reflect the network-related operation costs in our current pricing plans.

### What are the limits?[​](#what-are-the-limits "Direct link to What are the limits?")

| Free       | Pro         | Smart     | Enterprise |
| ---------- | ----------- | --------- | ---------- |
| 20 GB / mo | 100 GB / mo | 1 TB / mo | 4 TB / mo  |

### What to expect?[​](#what-to-expect "Direct link to What to expect?")

94% of our users will not be affected by these limits. If you are in the 6% that exceeds the limit, we will reach out to you directly to assist in the next 3 months in finding the best solution for your specific use case. Rest assured that even if you exceed the limit, your feature flags will continue to work seamlessly.

If you have any further questions or need assistance, please don't hesitate to [**reach out to us**](https://configcat.com/support). We're here to help!

***

## Introducing "Test with User"[​](#introducing-test-with-user "Direct link to Introducing \"Test with User\"")

#### Jul 26, 2023[​](#jul-26-2023 "Direct link to Jul 26, 2023")

We're pleased to announce the arrival of "Test with User" for feature flags!

With "Test with User," you can now test your feature flags before deploying them to production. Wondering how your flags will perform for specific users? This feature allows you to see the evaluation results based on a given User Object.

***

## Chromium Extension SDK (Beta)[​](#chromium-extension-sdk-beta "Direct link to Chromium Extension SDK (Beta)")

#### Dec 3, 2022[​](#dec-3-2022 "Direct link to Dec 3, 2022")

A new JS SDK for Chromium Extensions supporting the [Manifest V3](https://developer.chrome.com/docs/extensions/mv3/intro/) API is now on public beta and available via [npm](https://www.npmjs.com/package/configcat-js-chromium-extension).

[Open on GitHub](https://github.com/configcat/js-chromium-extension-sdk)

***

## New ConfigCat SDK for C++[​](#new-configcat-sdk-for-c "Direct link to New ConfigCat SDK for C++")

#### Oct 7, 2022[​](#oct-7-2022 "Direct link to Oct 7, 2022")

We just released a new official ConfigCat SDK supporting C++ applications.

[See Documentation](https://configcat.com/docs/sdk-reference/cpp.md)

***

## New ConfigCat SDK for React[​](#new-configcat-sdk-for-react "Direct link to New ConfigCat SDK for React")

#### Sept 6, 2022[​](#sept-6-2022 "Direct link to Sept 6, 2022")

We just released a new official ConfigCat SDK supporting React applications.

[See Documentation](https://configcat.com/docs/sdk-reference/react.md)

***

## monday.com integration[​](#mondaycom-integration "Direct link to monday.com integration")

#### Jul 18, 2022[​](#jul-18-2022 "Direct link to Jul 18, 2022")

Turn your features On / Off right from a monday.com item.

[ConfigCat Feature Flags monday.com app](https://monday.com/marketplace/10000079)

***

## ISO/IEC 27001:2013 certification[​](#isoiec-270012013-certification "Direct link to ISO/IEC 27001:2013 certification")

#### Jun 27, 2022[​](#jun-27-2022 "Direct link to Jun 27, 2022")

We're happy to announce that ConfigCat has achieved the ISO/IEC 27001:2013 certification for Information Security Management Systems (ISMS).

[Read more and download the certificates here](https://configcat.com/iso/)

***

## Reordering feature flags and other entities[​](#reordering-feature-flags-and-other-entities "Direct link to Reordering feature flags and other entities")

#### Mar 22, 2022[​](#mar-22-2022 "Direct link to Mar 22, 2022")

Click the Reorder icon on any overview to change the ordering of your feature flags, environments, configs or products.

***

## Copy feature flag values between environments[​](#copy-feature-flag-values-between-environments "Direct link to Copy feature flag values between environments")

#### Feb 23, 2022[​](#feb-23-2022 "Direct link to Feb 23, 2022")

You can copy feature flag values (including segment, targeting, percentage rules) from one environment to another.

***

## Segments are here[​](#segments-are-here "Direct link to Segments are here")

#### Feb 15, 2022[​](#feb-15-2022 "Direct link to Feb 15, 2022")

Segments let you group your users based on any of their properties (e.g: Beta Testers). You can target the same segment with multiple feature flags.

[Go to segments on our Dashboard](https://app.configcat.com/product/segments)

***

## TV Mode[​](#tv-mode "Direct link to TV Mode")

#### Dec 15, 2021[​](#dec-15-2021 "Direct link to Dec 15, 2021")

Display your feature flags on the TVs around the office!

[Config overview on our Dashboard](https://app.configcat.com/overview)

***

## Config Overview[​](#config-overview "Direct link to Config Overview")

#### Nov 17, 2021[​](#nov-17-2021 "Direct link to Nov 17, 2021")

Introducing a new overview to track your feature flag values in all your environments side-by-side.

Open the environment menu to access the overview.

[Open config overview on our Dashboard](https://app.configcat.com/overview)

***

## "Which projects are using this flag?"[​](#which-projects-are-using-this-flag "Direct link to \"Which projects are using this flag?\"")

#### Nov 2, 2021[​](#nov-2-2021 "Direct link to Nov 2, 2021")

ConfigCat: "Say no more fam! Let me show you!"

[See the documentation for details](https://configcat.com/docs/advanced/code-references/overview.md)

***

## Searching feature flags instead of Ctrl+F[​](#searching-feature-flags-instead-of-ctrlf "Direct link to Searching feature flags instead of Ctrl+F")

#### Oct 5, 2021[​](#oct-5-2021 "Direct link to Oct 5, 2021")

Added a search bar to the feature flags page.

We recommend using it instead of Ctr+F and Cmd+F since the page is lazy loaded. So it might not yield results from parts of the page that are not currently rendered.

***

## Environment colors are finally here[​](#environment-colors-are-finally-here "Direct link to Environment colors are finally here")

#### Sep 24, 2021[​](#sep-24-2021 "Direct link to Sep 24, 2021")

Just updated the UX on the product overview page and added a few small features.

* You can choose from a number of colors for your environments.
* Also adding descriptions helps teammates to find their way around environments and configs.

[Set your colors and add descriptions on the product overview page on our Dashboard](https://app.configcat.com/product)

***

## Send less invitations using SAML SSO, Auto-assign users and product join requests[​](#send-less-invitations-using-saml-sso-auto-assign-users-and-product-join-requests "Direct link to Send less invitations using SAML SSO, Auto-assign users and product join requests")

#### Sep 23, 2021[​](#sep-23-2021 "Direct link to Sep 23, 2021")

To make organization level user management more convenient we added a bunch of new features:

* Added an [organization overview on our Dashboard page](https://app.configcat.com/) to see products more clearly.
* Team members can send join requests to admins if they want to join a product.
* Whenever someone signs up to ConfigCat using a verified email domain, they could be automatically assigned to products.
* SAML Single Sign-On supporting all of the major identity providers.
* Improved layout for admins to [manage organization members](https://app.configcat.com/organization/members) on our Dashboard page.

*Only team members with Organization Admin role can access these features.*

[Set up user provisioning and SAML Single Sign-On on our Dashboard](https://app.configcat.com/organization/authentication)

***

## New Organization Admin functionalities[​](#new-organization-admin-functionalities "Direct link to New Organization Admin functionalities")

#### Aug 13, 2021[​](#aug-13-2021 "Direct link to Aug 13, 2021")

* Organization Admins can remove a member from the whole organization.
* Organization Admins can modify a member's permissions globally.

*Only team members with Organization Admin role can access these features.*

[Open Organization Members & Roles page on our Dashboard](https://app.configcat.com/organization/members)

***

## Disable Two-factor authentication[​](#disable-two-factor-authentication "Direct link to Disable Two-factor authentication")

#### Aug 4, 2021[​](#aug-4-2021 "Direct link to Aug 4, 2021")

Disable Two-factor authentication for your team members. This feature is useful if somebody lost the device used for Two-factor authentication.

*Only team members with Organization Admin role can disable Two-factor authentication.*

[Open Organization Members & Roles page on our Dashboard](https://app.configcat.com/organization/members)

***

## Export / Import[​](#export--import "Direct link to Export / Import")

#### Jul 28, 2021[​](#jul-28-2021 "Direct link to Jul 28, 2021")

Export (download), and import (upload) Configs, Environments, and Feature Flags from, and to file.

[Open Export / Import page on our Dashboard](https://app.configcat.com/product/exportimport)

***

## Dashboard v3 released[​](#dashboard-v3-released "Direct link to Dashboard v3 released")

#### Jun 30, 2021[​](#jun-30-2021 "Direct link to Jun 30, 2021")

Hope you like it.

Tell us your opinion over [Slack](https://configcat.com/slack) or [Email](mailto:team@configcat.com).

***

## Help us grow[​](#help-us-grow "Direct link to Help us grow")

#### Jun 10, 2021[​](#jun-10-2021 "Direct link to Jun 10, 2021")

If you like ConfigCat, you can help us grow by leaving a review. Plus Capterra is giving **20€ as a reward** to the first 100 reviewers.

Any of the following works:

* [TrustRadius](https://www.trustradius.com/welcome/configcat)
* [Trust Pilot](https://www.trustpilot.com/evaluate/configcat.com)
* [G2 Crowd](https://www.g2.com/products/configcat/reviews/start)
* [Capterra](https://reviews.capterra.com/new/187099) (**20€ reward**)
* [Alternative.me](https://alternative.me/configcat)
* [AlternativeTo](https://alternativeto.net/software/configcat/reviews)

***

## Visual Studio Code Extension[​](#visual-studio-code-extension "Direct link to Visual Studio Code Extension")

#### May 06, 2021[​](#may-06-2021 "Direct link to May 06, 2021")

Turn your features On / Off and manage your Feature Flags from Visual Studio Code.

* [Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=ConfigCat.configcat-feature-flags)

***

## Detailed Permission Group system[​](#detailed-permission-group-system "Direct link to Detailed Permission Group system")

#### Mar 10, 2021[​](#mar-10-2021 "Direct link to Mar 10, 2021")

Permission Groups can be customized in more advanced levels:

* Resource-based permissions (Configs, Environments, Tags, Webhooks)

* Create/Update and Delete permissions are separated

* Team member management permission

* Product preferences permission

* Product Audit Log/Statistics permission

* Integration management permission

* SDK Key View/Rotate permissions

* [Fine-tune Permission Groups on our Dashboard](https://app.configcat.com/product/permission-groups)

***

## Zombie Flags (Stale Flags) Report via email[​](#zombie-flags-stale-flags-report-via-email "Direct link to Zombie Flags (Stale Flags) Report via email")

#### Mar 4, 2021[​](#mar-4-2021 "Direct link to Mar 4, 2021")

Feature flags have a tendency to multiply rapidly. In order to keep the tech-debt low, we recommend removing the flags no longer needed. You can now set up a regular email report with a list of these zombie or stale flags.

* [Set up the Zombie Flags Report on our Dashboard](https://app.configcat.com/zombie-flags-report)

***

## Invoice download[​](#invoice-download "Direct link to Invoice download")

#### Feb 8, 2021[​](#feb-8-2021 "Direct link to Feb 8, 2021")

You can download all your current and previous invoices from the Billing & Invoices page.

* [Open Billing & Invoices on our Dashboard](https://app.configcat.com/organization/billing)

***

## Accepting USD payments[​](#accepting-usd-payments "Direct link to Accepting USD payments")

#### Nov 26, 2020[​](#nov-26-2020 "Direct link to Nov 26, 2020")

We are accepting payments in USD from now on.

* [See plans on our Dashboard](https://app.configcat.com/organization/plans)

***

## ConfigCat & Zoho Flow[​](#configcat--zoho-flow "Direct link to ConfigCat & Zoho Flow")

#### Nov 21, 2020[​](#nov-21-2020 "Direct link to Nov 21, 2020")

ConfigCat's Zoho Flow integration is now available.

* [Detailed Docs and Setup Guide](https://configcat.com/docs/integrations/zoho-flow.md)

***

## Default Permission Group[​](#default-permission-group "Direct link to Default Permission Group")

#### Nov 13, 2020[​](#nov-13-2020 "Direct link to Nov 13, 2020")

Set a default Permission Group for Team member invites. The chosen group will be the default on the permission group list when inviting others. So you can be sure not to invite someone as an admin by accident.

***

## Amplitude integration[​](#amplitude-integration "Direct link to Amplitude integration")

#### Oct 28, 2020[​](#oct-28-2020 "Direct link to Oct 28, 2020")

Annotate your setting changes on your Amplitude charts.

* [Docs and Setup Guide](https://configcat.com/docs/integrations/amplitude.md)

***

## ConfigCat Feature Flags Provider for Terraform[​](#configcat-feature-flags-provider-for-terraform "Direct link to ConfigCat Feature Flags Provider for Terraform")

#### Oct 16, 2020[​](#oct-16-2020 "Direct link to Oct 16, 2020")

Configure and access ConfigCat resources via Terraform.

* [ConfigCat Feature Flags Provider for Terraform](https://registry.terraform.io/providers/configcat/configcat/latest/docs)

***

## Data Governance - Action required[​](#data-governance---action-required "Direct link to Data Governance - Action required")

#### Oct 10, 2020[​](#oct-10-2020 "Direct link to Oct 10, 2020")

Addressing global data handling and processing trends, we have introduced the Data Governance feature in ConfigCat. We require all our customers to make a statement if they want to use our:

* **Global CDN**: providing geo-location based load balancing on server nodes all around the globe to ensure low response times.

* **EU CDN**: Staying compliant with GDPR by using ConfigCat EU CDN. This way your data will never leave the EU.

* [Read more on Data Governance and CDN](https://configcat.com/docs/advanced/data-governance.md)

***

## Organization Management[​](#organization-management "Direct link to Organization Management")

#### Sep 07, 2020[​](#sep-07-2020 "Direct link to Sep 07, 2020")

Featuring:

* **Organization Admin** and **Billing Manager** roles.

* General **security** preferences for the entire organization.

* Customizable **SSO** methods.

* Organization level **audit logs** and usage **statistics**.

* [See Docs](https://configcat.com/docs/organization.md)

***

## Public Management API v1 released[​](#public-management-api-v1-released "Direct link to Public Management API v1 released")

#### Jul 08, 2020[​](#jul-08-2020 "Direct link to Jul 08, 2020")

You can programmatically **CREATE**, **UPDATE**, **DELETE** Feature Flags, Configs, Products and Environments from now on!

* [See Docs and examples](https://configcat.com/docs/api/reference/configcat-public-management-api.md)

***

## Tags & Filtering[​](#tags--filtering "Direct link to Tags & Filtering")

#### May 29, 2020[​](#may-29-2020 "Direct link to May 29, 2020")

Add colored tags to your feature flags.

***

## Jira Cloud Plugin[​](#jira-cloud-plugin "Direct link to Jira Cloud Plugin")

#### May 28, 2020[​](#may-28-2020 "Direct link to May 28, 2020")

Turn your features On / Off right from a Jira Issue.

* [ConfigCat Jira Cloud Plugin](https://marketplace.atlassian.com/apps/1222421/configcat-feature-flags?hosting=cloud\&tab=overview)

***

## Slack App[​](#slack-app "Direct link to Slack App")

#### April 12, 2020[​](#april-12-2020 "Direct link to April 12, 2020")

Get updated via a Slack Channel message when someone changes a feature flag.

* [ConfigCat Feature Flags in Slack App Directory](https://configcat.slack.com/apps/A011CN2QZJB-configcat-feature-flags)

***

## API Key --> SDK Key[​](#api-key----sdk-key "Direct link to API Key --> SDK Key")

#### April 7, 2020[​](#april-7-2020 "Direct link to April 7, 2020")

Renamed API Key to SDK Key since it was more confusing as the Public Management API went to production. The API and the API Key are not related. This is a breaking change in some of the SDKs, released under new major versions.

***

## New JavaScript SDK for SSR[​](#new-javascript-sdk-for-ssr "Direct link to New JavaScript SDK for SSR")

#### April 3, 2020[​](#april-3-2020 "Direct link to April 3, 2020")

New JavaScript SDK supporting Server Side Rendered (SSR) frameworks like [NuxtJS](https://nuxtjs.org).

* [See Documentation](https://configcat.com/docs/sdk-reference/js-ssr.md)

***

## Trello Power-Up[​](#trello-power-up "Direct link to Trello Power-Up")

#### March 30, 2020[​](#march-30-2020 "Direct link to March 30, 2020")

Turn your features On / Off right from a Trello Card.

* [ConfigCat Power-Up](https://trello.com/power-ups/5e694b66d2511a3601ebd0fb)

***

## Integrations[​](#integrations "Direct link to Integrations")

#### March 21, 2020[​](#march-21-2020 "Direct link to March 21, 2020")

Connect the apps you use everyday and be more productive. Check out the [Integrations tab](https://app.configcat.com/product/integrations) in our Dashboard.

***

## View SDK Key permission[​](#view-sdk-key-permission "Direct link to View SDK Key permission")

#### March 21, 2020[​](#march-21-2020-1 "Direct link to March 21, 2020")

Visibility of information that is normally useful for developers only - like SDK Keys and code examples - can be set for [Permission Groups](https://app.configcat.com/product/permission-groups) on our Dashboard.

***

## Audit log improvements[​](#audit-log-improvements "Direct link to Audit log improvements")

#### March 20, 2020[​](#march-20-2020 "Direct link to March 20, 2020")

User friendly Feature Flag or Setting value changes in the [Audit log on our Dashboard](https://app.configcat.com/auditlog) to improve readability.

***

## Long text improvements[​](#long-text-improvements "Direct link to Long text improvements")

#### March 20, 2020[​](#march-20-2020-1 "Direct link to March 20, 2020")

Feature Flag or Setting text values and Targeting comparison values can be viewed and updated in a `textarea`.

***

## Upper case key generation mode[​](#upper-case-key-generation-mode "Direct link to Upper case key generation mode")

#### March 17, 2020[​](#march-17-2020 "Direct link to March 17, 2020")

Besides "camelCase" and "lower\_case" we have added an "UPPER\_CASE" key generation mode to preferences.

* [Open Preferences on in our Dashboard](https://app.configcat.com/product/preferences)

***

## Statistics[​](#statistics "Direct link to Statistics")

#### March 15, 2020[​](#march-15-2020 "Direct link to March 15, 2020")

See detailed statistics about the number of config.json downloads made towards ConfigCat CDN. Also a pie-chart of the SDK types and versions being used.

* [Open Stats on our Dashboard](https://app.configcat.com/product/statistics)

***

## ConfigCat Zap[​](#configcat-zap "Direct link to ConfigCat Zap")

#### March 12, 2020[​](#march-12-2020 "Direct link to March 12, 2020")

Zapier integration is now accessible.

* [Detailed Docs and Setup Guide](https://configcat.com/docs/integrations/zapier.md)

***

## Public Management API (Beta)[​](#public-management-api-beta "Direct link to Public Management API (Beta)")

#### March 11, 2020[​](#march-11-2020 "Direct link to March 11, 2020")

Released Public Management API to Beta. From now on you can execute Dashboard management operations programmatically.

* [API Documentation](https://configcat.com/docs/api/reference/configcat-public-management-api.md)

***

## Sensitive text comparators[​](#sensitive-text-comparators "Direct link to Sensitive text comparators")

#### March 3, 2020[​](#march-3-2020 "Direct link to March 3, 2020")

Introduced sensitive text comparators to make sure sensitive info (like email address, user name) is kept hidden in Targeting Rules. Comes handy in front-end applications.

* [Detailed Docs about comparators](https://configcat.com/docs/targeting/targeting-rule/user-condition.md#comparator)
* [Related blog post](https://configcat.com/blog/2020/03/02/sensitive-comparators/)

***

## Semantic version based user targeting[​](#semantic-version-based-user-targeting "Direct link to Semantic version based user targeting")

#### March 3, 2020[​](#march-3-2020-1 "Direct link to March 3, 2020")

Especially useful for Mobile developers.

* [Detailed Docs about comparators](https://configcat.com/docs/targeting/targeting-rule/user-condition.md#comparator)
* [Related blog post](https://configcat.com/blog/2020/01/27/semver)

***

## Ruby SDK[​](#ruby-sdk "Direct link to Ruby SDK")

#### Oct 29, 2019[​](#oct-29-2019 "Direct link to Oct 29, 2019")

It is out!

* [Ruby SDK Docs](https://configcat.com/docs/sdk-reference/ruby.md)
* [GitHub repo](https://github.com/configcat/ruby-sdk)
* [Blog post](https://configcat.com/blog/2019/10/29/ruby-sdk/)

***
