# Source: https://configcat.com/docs/advanced/config-v2.md

# Config V2 Overview

Config V2 is a new version of ConfigCat. It comes with a new Dashboard, Public Management API, SDKs, and features.

## What's new?[​](#whats-new "Direct link to What's new?")

* A bunch of new features and improvements listed below.
* New config editor UI on the Dashboard.
* [New and improved config JSON schema.](https://github.com/configcat/config-json)
* New API: [See the API Docs.](https://configcat.com/docs/docs/api/reference/configcat-public-management-api/.md)
* New SDKs: [See the supported SDK versions.](https://configcat.com/docs/docs/advanced/config-v2-sdk-compatibility/.md)

## How to migrate from Config V1 to Config V2?[​](#how-to-migrate-from-config-v1-to-config-v2 "Direct link to How to migrate from Config V1 to Config V2?")

See the [Config V2 Migration Guide](https://configcat.com/docs/docs/advanced/config-v2-migration-guide/.md). If you get stuck or have any questions about the migration, feel free to [contact us](https://configcat.com/support/).

## New features[​](#new-features "Direct link to New features")

### AND conditions[​](#and-conditions "Direct link to AND conditions")

With AND conditions, you can define more complex Targeting Rules, such as "serve this value for the users who use my Android app AND whose email domain is '@example.com'".

You can add multiple conditions to a Targeting Rule and they will be evaluated with an AND connection between them.

![AND conditions](/docs/assets/images/and-conditions-1885d725ca07feb98918be74caf847ac.png)

### New comparators[​](#new-comparators "Direct link to New comparators")

With the new comparators, you can create Targeting Rules based on date comparisons, array comparisons, and more.

* New text and confidential text comparators: `EQUALS`, `NOT EQUALS`, `STARTS WITH ANY OF`, `ENDS WITH ANY OF`, `NOT STARTS WITH ANY OF`, `NOT ENDS WITH ANY OF`.
* New array comparators: `ARRAY CONTAINS ANY OF`, `ARRAY NOT CONTAINS ANY OF`.
* New date comparators: `BEFORE`, `AFTER`.

![New comparators](/docs/assets/images/new-comparators-20f2a035bd85c2416e9bb89599234608.png)

### Prerequisite flags[​](#prerequisite-flags "Direct link to Prerequisite flags")

With prerequisite flags, you can create feature flags that depend on other feature flags. Prerequisite feature flags (aka. master feature flag, inter-dependent feature flag, global toggle) are particularly useful for managing complex feature dependencies and ensuring a smooth user experience during feature rollouts.

![Prerequisite flags](/docs/assets/images/prerequisite-flags-8d735217aefdcab04a16517a782f13b1.png)

### Comparison value hints[​](#comparison-value-hints "Direct link to Comparison value hints")

With comparison value hints, you can associate arbitrary text with your comparison values. This way you can add a description to your comparison value list items that helps you remember what they are for.

### Percentage Options within Targeting Rules[​](#percentage-options-within-targeting-rules "Direct link to Percentage Options within Targeting Rules")

You can add Percentage Options to your Targeting Rules. This is useful if you want to create more complex Targeting Rules, such as "turn on the feature for 20% of the users who are on iOS, and off for 80%".

![Percentage Options within Targeting Rules](/docs/assets/images/percentage-options-within-targeting-rules-19525180c556b212b688a76daa59f754.png)

### Custom Percentage Attributes[​](#custom-percentage-attributes "Direct link to Custom Percentage Attributes")

With custom Percentage Attributes, you can create Percentage Options based on custom attributes. This way you can create Percentage Options based on any of your user attributes. For example, you can create a Percentage Option that is based on the user's company or organization. So you can serve a value for 20% of the users from company A and serve another value for 80% of the users from company B.

![Custom Percentage Attributes](/docs/assets/images/custom-percentage-attributes-8b44f64042ed7947f08ccfa0b6f17c84.png)
