# Source: https://configcat.com/docs/targeting/targeting-overview.md

# Targeting Overview

Targeting allows you to enable or disable a feature for specific users or groups of users in your application. Typical use cases are:

* [Beta testing](https://configcat.com/docs/docs/glossary/.md#beta-testing)
* [A/B testing](https://configcat.com/docs/docs/glossary/.md#ab-testing)
* [Phased rollouts, canary releases](https://configcat.com/docs/docs/glossary/.md#canary-release)

## How does it work?[​](#how-does-it-work "Direct link to How does it work?")

1. On the [ConfigCat Dashboard](https://app.configcat.com), you add [Targeting Rules](https://configcat.com/docs/docs/targeting/targeting-rule/targeting-rule-overview/.md) and/or [Percentage Options](https://configcat.com/docs/docs/targeting/percentage-options/.md) to your feature flag.
2. You pass a [User Object](https://configcat.com/docs/docs/targeting/user-object/.md) to the ConfigCat SDK in your application.
3. The ConfigCat SDK will use the User Object and the rules defined on the Dashboard to determine whether the feature should be enabled for the user.

## What is what?[​](#what-is-what "Direct link to What is what?")

![Targeting Overview](/docs/assets/targeting/targeting-overview/what-is-what_192dpi.png)

### Feature Flag / Setting[​](#feature-flag--setting "Direct link to Feature Flag / Setting")

A *setting* is a set of rules that yields a **boolean**, **string**, **integer** or **double** value, which can be used to configure your application. It is also known as a configuration value, configuration setting, configuration parameter, etc.

A *feature flag* is a **boolean** setting used to decide whether an application feature should be turned ON or OFF. It is also known as a feature toggle, feature switch, feature flipper, conditional feature, etc.

info

Throughout this documentation, we generally use the term *feature flag* to refer to both feature flags and settings for simplicity because feature flags are the most common type of settings.

### Targeting Rule[​](#targeting-rule "Direct link to Targeting Rule")

A *Targeting Rule* consists of a collection of conditions and a value to serve. If the conditions are met (the Targeting Rule *matches*), the value is served, i.e. returned as the result of the feature flag evaluation. More about Targeting Rules [here](https://configcat.com/docs/docs/targeting/targeting-rule/targeting-rule-overview/.md).

### Condition[​](#condition "Direct link to Condition")

A *condition* is a logical expression that can be evaluated to true or false. There are three types of conditions: [User Condition](https://configcat.com/docs/docs/targeting/targeting-rule/user-condition/.md), [Flag Condition (Prerequisite)](https://configcat.com/docs/docs/targeting/targeting-rule/flag-condition/.md), [Segment Condition](https://configcat.com/docs/docs/targeting/targeting-rule/segment-condition/.md). For a Targeting Rule to match, all of its conditions must evaluate to true.

### Percentage Options[​](#percentage-options "Direct link to Percentage Options")

*Percentage Options* divide users into groups, each receiving a specific value. The groups are allocated according to the specified percentage split. Percentage Options are often used for A/B testing or phased rollouts. More about Percentage Options [here](https://configcat.com/docs/docs/targeting/percentage-options/.md).

### "To all users" / "To all other" / "To unidentified" value[​](#to-all-users--to-all-other--to-unidentified-value "Direct link to \"To all users\" / \"To all other\" / \"To unidentified\" value")

A feature flag always contains a trivial "rule", a simple value after the actual rules. This value is returned when none of the preceding rules yields a result.

### Default value[​](#default-value "Direct link to Default value")

The ConfigCat SDK's feature flag evaluation functions (e.g. `GetValue`) require you to provide a *default value*. This value will be returned in case the SDK fails to fetch the config or some other error occurs during the evaluation of the feature flag.

### User Object[​](#user-object "Direct link to User Object")

A *User Object* is a collection of *user attributes* that describe the properties of a user. Referencing these attributes in conditions allows you to define rules for targeting users. More about the User Object [here](https://configcat.com/docs/docs/targeting/user-object/.md).

## Examples[​](#examples "Direct link to Examples")

### Phased rollout / Canary release / Percentage rollout scenario[​](#phased-rollout--canary-release--percentage-rollout-scenario "Direct link to Phased rollout / Canary release / Percentage rollout scenario")

#### Context[​](#context "Direct link to Context")

Our demo company, Whisker Co. is about to release a new feature called **Park Weather Info**. The stakeholders want to make sure that the release of the new feature goes smoothly and it is received well by the customers.

#### Goal[​](#goal "Direct link to Goal")

To make sure that the new feature is working as expected before releasing it to everyone, we initially want to make the feature available to the employees and to 20% of the customers only.

#### Solution[​](#solution "Direct link to Solution")

Let's create a feature flag called **Enable Park Weather Info** with a Targeting Rule that matches the employees at Whisker Co. and Percentage Options set to **20% ON** and **80% OFF** for the rest of the users (i.e. for the customers).

Here is what such a feature flag looks like on the Dashboard:

![Phased rollout example](/docs/assets/targeting/targeting-overview/phased-rollout-example_192dpi.png)

Here is how we get the value of the feature flag in your application:

```
// Create the User Object
const userObject = {
  // Used by the Percentage Options to split the users into groups
  identifier: '867428724',
  // Used by the Targeting Rule's User Condition to determine whether
  // the user is an employee at Whisker Co.
  email: 'isaac@whisker.cc',
};

// Get the value of the feature flag
const value = await configCatClient.getValueAsync(
  // Feature flag key
  'enableParkWeatherInfo',
  // Default value - by providing `false` we specify that the feature should not be
  // enabled if the SDK fails to fetch the config or some other error occurs
  false,
  // User Object
  userObject,
);
```
