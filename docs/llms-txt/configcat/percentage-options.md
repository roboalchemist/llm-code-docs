# Source: https://configcat.com/docs/targeting/percentage-options.md

# Percentage Options

## What are Percentage Options?[​](#what-are-percentage-options "Direct link to What are Percentage Options?")

Using *Percentage Options*, you can define that a certain percentage of users should receive a specific value.

This way, you can gradually release a new feature to a subset of users. Instead of releasing a feature to all users simultaneously, a specific percentage of users are selected to receive access to the feature. This allows developers to control and monitor the impact of the new feature in a controlled manner.

## How to add Percentage Options?[​](#how-to-add-percentage-options "Direct link to How to add Percentage Options?")

You can add Percentage Options to a feature flag by clicking the **+%** button on the Dashboard.

![Add percentage options](/docs/assets/targeting/percentage-options/add-percentage-options_192dpi.png)

## How does it work? - Anatomy of Percentage Options[​](#how-does-it-work---anatomy-of-percentage-options "Direct link to How does it work? - Anatomy of Percentage Options")

Percentage Options is a list of *% value* and *served value* pairs, where % values add up to 100.

It divides users into groups according to the percentage split defined by the % values. The grouping is random and based on the [Percentage Evaluation Attribute](#percentage-evaluation-attribute). By default, this is the [User Object's](https://configcat.com/docs/docs/targeting/user-object/.md) **Identifier** attribute. However, you can use any other user attribute as the basis of the grouping.

info

If the Percentage Evaluation Attribute is not present in the [User Object](https://configcat.com/docs/docs/targeting/user-object/.md), the ["To unidentified" value](https://configcat.com/docs/docs/targeting/targeting-overview/.md#to-all-users--to-all-other--to-unidentified-value) will be returned. (Read more about the feature flag evaluation algorithm [here](https://configcat.com/docs/docs/targeting/feature-flag-evaluation/.md).)

Percentage Options are designed to be [sticky](#stickiness) and [consistent](#consistency) across all SDKs, ensuring a reliable experience.

### % value[​](#-value "Direct link to % value")

Any number between 0 and 100 that represents a randomly allocated group of your users.

### Served value[​](#served-value "Direct link to Served value")

The value to return when the user falls into the group determined by the % value.

### Number of Percentage Options[​](#number-of-percentage-options "Direct link to Number of Percentage Options")

In the case of a feature flag (boolean setting), there must be two options. One for the **ON** and one for the **OFF** state.

In the case of a string, integer or double setting, the maximum number of options [depends on your subscription plan](https://configcat.com/docs/docs/subscription-plan-limits/.md). You can add options by clicking the **+% OPTION** button.

## Percentage Options within Targeting Rules[​](#percentage-options-within-targeting-rules "Direct link to Percentage Options within Targeting Rules")

Percentage Options can be used in combination with Targeting Rules.

In this case, the Percentage Options will be evaluated only if the Targeting Rule matches. In other words, the Percentage Options apply only to the users that matched the Targeting Rule.

info

If the Percentage Evaluation Attribute is not present in the [User Object](https://configcat.com/docs/docs/targeting/user-object/.md), the targeting rule will be skipped - despite the matching Targeting Rule. Read more about the feature flag evaluation algorithm [here](https://configcat.com/docs/docs/targeting/feature-flag-evaluation/.md).

![Percentage options within targeting rules](/docs/assets/targeting/percentage-options/percentage-options-within-targeting-rule_192dpi.png)

## Percentage Evaluation Attribute[​](#percentage-evaluation-attribute "Direct link to Percentage Evaluation Attribute")

The *Percentage Evaluation Attribute* (sometimes called *percentage attribute*) is the user attribute by which users are grouped. By default, it is the [User Object's](https://configcat.com/docs/docs/targeting/user-object/.md) **Identifier** attribute. However, you can use any other user attribute as the basis of the grouping (see the example use case [below](#percentage-options-based-on-other-user-attributes)).

### How to change the Percentage Evaluation Attribute?[​](#how-to-change-the-percentage-evaluation-attribute "Direct link to How to change the Percentage Evaluation Attribute?")

In the top right corner of the feature flag, open the kebab (3 dots) menu and choose the **Change percentage attribute** item.

info

The selected Percentage Evaluation Attribute applies to all Percentage Options within the feature flag - but only in the current ConfigCat environment.

![Change percentage attribute](/docs/assets/targeting/percentage-options/change-percentage-attribute_192dpi.png)

## Stickiness[​](#stickiness "Direct link to Stickiness")

*Stickiness* means that the same user will always get the same value for the same percentage split in the case of a specific feature flag, regardless of the history of the feature flag. This is achieved by implementing a deterministic hashing algorithm based on the feature flag's key and the Percentage Evaluation Attribute.

For example, if you have a feature flag with a Percentage Option of **20% ON**, then you change the Percentage Option to **40% ON**, and then back to **20% ON**, the same 20% of users will get the **ON** value for the feature flag just like the first time.

For a demonstration of this concept, see this [example scenario](https://configcat.com/docs/docs/targeting/feature-flag-evaluation/.md#example-scenarios-for-percentage-options).

## Consistency[​](#consistency "Direct link to Consistency")

*Consistency* means that the same user will always get the same value for the same percentage split in the case of a specific feature flag, no matter which SDK is used. This is achieved by using the same hashing algorithm across all SDKs.

For example, if you have a feature flag with a Percentage Option of **20% ON**, then the same 20% of users will get the **ON** value across all SDKs. No matter if a user is on iOS, Android, or Web, they will always get the same value for the feature flag.

## Randomness[​](#randomness "Direct link to Randomness")

The same user might get different values for the same percentage split in the case of different feature flags. This is because the hashing algorithm is based on the combination of the feature flag's key and the Percentage Evaluation Attribute. Since feature flag keys are unique, the resulting hashes will usually be different as well.

For example, if you have two feature flags with Percentage Options of **20% ON**, then a different 20% of users will get the **ON** value for each feature flag.

## Examples[​](#examples "Direct link to Examples")

### Simple phased rollout / Canary release / Percentage rollout scenario[​](#simple-phased-rollout--canary-release--percentage-rollout-scenario "Direct link to Simple phased rollout / Canary release / Percentage rollout scenario")

#### Context[​](#context "Direct link to Context")

Our demo company, Whisker Co. is about to release a new feature called **Park Weather Info**. The stakeholders want to make sure that the new feature is received well by the customers.

#### Goal[​](#goal "Direct link to Goal")

To get some feedback from our customers before releasing it to everyone, we initially want to make the feature available to 20% of the customers only.

#### Solution[​](#solution "Direct link to Solution")

Let's create a feature flag called **Enable Park Weather Info** with Percentage Options set to **20% ON** and **80% OFF**.

![Simple phased rollout example](/docs/assets/targeting/percentage-options/simple-phased-rollout-example_192dpi.png)

### A/B/n testing scenario[​](#abn-testing-scenario "Direct link to A/B/n testing scenario")

#### Context[​](#context-1 "Direct link to Context")

The marketing specialists at Whisker Co. want to introduce a discount strategy to boost webshop purchases. They have several ideas but lack the statistical data needed to determine which would be most effective.

#### Goal[​](#goal-1 "Direct link to Goal")

To learn which is the most effective discount strategy, we want to perform an A/B/C test.

#### Solution[​](#solution-1 "Direct link to Solution")

We need a string or integer setting for this task because we need to represent 3 different variations. Let's create a string setting named **Discount Type** (as textual values tell more than numbers).

The go-to feature for A/B testing is Percentage Options. So let's add one with 3 options, each covering 1/3rd of our customers.

![A/B/n testing example](/docs/assets/targeting/percentage-options/abn-testing-example_192dpi.png)

info

To make all this useful, that is, to measure the effectiveness of the different strategies, we also need to integrate with an analytics service like [Amplitude](https://configcat.com/docs/docs/integrations/amplitude/.md) or [Mixpanel](https://configcat.com/docs/docs/integrations/mixpanel/.md) and update our application to send feature flag evaluation results to it.

### Complex phased rollout / Canary release / Percentage rollout scenario[​](#complex-phased-rollout--canary-release--percentage-rollout-scenario "Direct link to Complex phased rollout / Canary release / Percentage rollout scenario")

#### Context[​](#context-2 "Direct link to Context")

Whisker Co. is about to release a new feature called **Park Weather Info**. The stakeholders want to make sure that the release of the new feature goes smoothly and it is received well by the customers.

#### Goal[​](#goal-2 "Direct link to Goal")

To do some in-house testing and also get some feedback from our customers before releasing it to everyone, we initially want to make the feature available to the employees and to 20% of the customers only.

#### Solution[​](#solution-2 "Direct link to Solution")

Let's create a feature flag called **Enable Park Weather Info** with a Targeting Rule that matches the employees at Whisker Co. and Percentage Options set to **20% ON** and **80% OFF** for the rest of the users (i.e. for the customers).

![Complex phased rollout example](/docs/assets/targeting/percentage-options/complex-phased-rollout-example_192dpi.png)

### Platform-specific phased rollout[​](#platform-specific-phased-rollout "Direct link to Platform-specific phased rollout")

#### Context[​](#context-3 "Direct link to Context")

Whisker Co. is about to release a new feature called **Cafe Notifications** in their mobile app, which has an Android and an iOS version. We know that the userbase of the iOS app is much larger than the Android app. The stakeholders want to make sure that the new feature is received well by the customers.

#### Goal[​](#goal-3 "Direct link to Goal")

To get some feedback from our customers before releasing it to everyone, we initially want to make the feature available to a limited number of customers only. We also want to release the feature to roughly the same number of Android and iOS users.

#### Solution[​](#solution-3 "Direct link to Solution")

Let's create a feature flag called **Cafe Notifications** with two Targeting Rules: one that matches Android users and one that matches iOS users. Then change the THEN part of both to Percentage Options. Finally, let's set the percentages so that the feature is enabled for roughly the same number of users (e.g. 60% for Android users, 20% for iOS users).

![Platform-specific phased rollout example](/docs/assets/targeting/percentage-options/platform-specific-phased-rollout-example_192dpi.png)

### Percentage Options based on other user attributes[​](#percentage-options-based-on-other-user-attributes "Direct link to Percentage Options based on other user attributes")

#### Context[​](#context-4 "Direct link to Context")

Let's imagine that at Whisker Co., we have a custom attribute named **Tenant ID** that is used to identify the tenants of our customers.

#### Goal[​](#goal-4 "Direct link to Goal")

We want to release a new feature, **Park Weather Info**, to 20% of our customers based on their **Tenant ID**.

#### Solution[​](#solution-4 "Direct link to Solution")

Let's create a feature flag called **Enable Park Weather Info** with Percentage Options set to **20% ON** and **80% OFF**. Finally, let's set the Percentage Evaluation Attribute to **Tenant ID** as described [here](#percentage-evaluation-attribute).

![Custom percentage attribute example](/docs/assets/targeting/percentage-options/custom-percentage-attribute-example_192dpi.png)
