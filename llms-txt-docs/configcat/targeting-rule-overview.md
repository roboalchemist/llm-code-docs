# Source: https://configcat.com/docs/targeting/targeting-rule/targeting-rule-overview.md

# Targeting Rule

## What is a Targeting Rule?[​](#what-is-a-targeting-rule "Direct link to What is a Targeting Rule?")

*Targeting Rules* allow you to set different feature flag values for specific users or groups of users in your application.

You can set conditions based on user attributes, feature flags, or segments within a Targeting Rule.

### AND and OR relationships[​](#and-and-or-relationships "Direct link to AND and OR relationships")

The conditions within a Targeting Rule are in an **AND** relationship, meaning that all of them must evaluate to true for the Targeting Rule to match.

The Targeting Rules are in an **OR** relationship, meaning that the Targeting Rule which matches first in order, from top to bottom, will provide the value of the feature flag.

## How to add a Targeting Rule?[​](#how-to-add-a-targeting-rule "Direct link to How to add a Targeting Rule?")

You can add a Targeting Rule to a feature flag by clicking the **+IF** ("Add targeting rule") button on the Dashboard. To add more Targeting Rules, click the **+OR** button at the bottom of the last Targeting Rule.

![Add targeting rule](/docs/assets/targeting/targeting-rule/add-targeting-rule_192dpi.png)

## How does it work? - Anatomy of a Targeting Rule[​](#how-does-it-work---anatomy-of-a-targeting-rule "Direct link to How does it work? - Anatomy of a Targeting Rule")

A Targeting Rule consists of an *IF part* and a *THEN part*.

![Targeting rule anatomy](/docs/assets/targeting/targeting-rule/targeting-rule-anatomy_192dpi.png)

### IF part[​](#if-part "Direct link to IF part")

The *IF part* contains the conditions, which are logical expressions that evaluate to true or false.

The conditions are in an **AND** relationship, meaning that all of them must evaluate to true for the Targeting Rule to match.

The conditions can be added to the Targeting Rule on the Dashboard, using the **+AND** ("Add AND condition") button. There are three types of conditions:

* [User Condition](https://configcat.com/docs/docs/targeting/targeting-rule/user-condition/.md) - A condition that is based on some property of the user.
* [Flag Condition (Prerequisite)](https://configcat.com/docs/docs/targeting/targeting-rule/flag-condition/.md) - A condition that is based on the value of another feature flag.
* [Segment Condition](https://configcat.com/docs/docs/targeting/targeting-rule/segment-condition/.md) - A condition that is based on a segment.

### THEN part[​](#then-part "Direct link to THEN part")

The *THEN part* determines the result of the feature flag when the Targeting Rule matches. It can be either a simple value or Percentage Options.

## Multiple Targeting Rules and ordering[​](#multiple-targeting-rules-and-ordering "Direct link to Multiple Targeting Rules and ordering")

The order of Targeting Rules matters because they are in an **OR** relationship, meaning that the Targeting Rule which matches first in order, from top to bottom, will provide the value of the feature flag.

### How to change the order of the Targeting Rules?[​](#how-to-change-the-order-of-the-targeting-rules "Direct link to How to change the order of the Targeting Rules?")

The order of the Targeting Rules can be changed on the Dashboard by dragging and dropping the Targeting Rules.

![Change targeting rule order](/docs/assets/targeting/targeting-rule/targeting-rule-reorder_192dpi.png)

## Examples[​](#examples "Direct link to Examples")

### AND relationship between Conditions[​](#and-relationship-between-conditions "Direct link to AND relationship between Conditions")

#### Context[​](#context "Direct link to Context")

In our demo company (Whisker Co.) we have a new feature in our mobile app that notifies frequent shopper cat owners about the cat-friendly cafés in the neighborhood.

#### Goal[​](#goal "Direct link to Goal")

Since this feature is new, we want to make sure that only frequent shoppers and cat owners who have the right version of the app receive these notifications. The earlier versions of the app don't have this feature, so we want to make sure that only those who are running version 3.0.0 or higher receive the notifications.

#### Solution[​](#solution "Direct link to Solution")

We can achieve this by adding a Targeting Rule to the **Enable Cafe Notifications** feature flag. The Targeting Rule will have two conditions:

* a Segment Condition, which requires that the user is in segment **Frequent Shoppers**,
* a User Condition, which requires that the user attribute **AppVersion** is greater than or equal to **3.0.0**.

On the Dashboard:

![AND relationship example](/docs/assets/targeting/targeting-rule/and-example_192dpi.png)

In the code:

```
const userObject = {
  identifier: userId,
  email: userEmail,
  custom: {
    AppVersion: '3.1.2'
  },
};

const value = await configCatClient.getValueAsync("enableCafeNotifications", false, userObject);
```
