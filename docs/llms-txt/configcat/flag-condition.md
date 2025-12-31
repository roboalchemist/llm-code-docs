# Source: https://configcat.com/docs/targeting/targeting-rule/flag-condition.md

# Flag Condition (Prerequisite)

## What is a Flag Condition? What is a prerequisite flag?[​](#what-is-a-flag-condition-what-is-a-prerequisite-flag "Direct link to What is a Flag Condition? What is a prerequisite flag?")

A *Flag Condition* is a condition that is based on the comparison of another feature flag's value and a preset value (*comparison value*). In other words, a Flag Condition creates a dependency between the feature flag containing the condition (*dependent flag*) and another feature flag (*prerequisite flag*, aka. master feature flag, master switch, inter-dependent feature flag, global toggle, etc.)

This allows you to control the value of multiple feature flags by changing the value of a single, central feature flag. Prerequisite flags are useful for managing complex feature dependencies and ensuring a smooth user experience during feature rollouts.

## How does the Flag Condition work?[​](#how-does-the-flag-condition-work "Direct link to How does the Flag Condition work?")

The prerequisite flag is evaluated with the same User Object as the one used to evaluate the dependent flag, and then the result is checked against the comparator that you set on the Dashboard.

The prerequisite flag can be other than a feature flag (boolean setting), in which case the prerequisite flag's evaluated value will be compared to the comparison value that you set on the Dashboard. The comparison is done according to the selected comparator and will result in true or false. This will be the result of the condition.

For more details on the evaluation of Flag Conditions, please refer to [Feature Flag Evaluation](https://configcat.com/docs/docs/targeting/feature-flag-evaluation/.md#evaluation-of-a-flag-condition).

## How to set a Flag Condition?[​](#how-to-set-a-flag-condition "Direct link to How to set a Flag Condition?")

You can add a Flag Condition to a feature flag by clicking the **+IF** ("Add targeting rule") button on the Dashboard.

The prerequisite flag can be any feature flag already defined in the same config on the Dashboard. In the case of a non-boolean setting (e.g. text setting or number setting), you can also set a comparison value which the prerequisite flag's value will be compared to.

![Add prerequisite](/docs/assets/targeting/targeting-rule/flag-condition/add-prerequisite_192dpi.png)

## Anatomy of a Flag Condition[​](#anatomy-of-a-flag-condition "Direct link to Anatomy of a Flag Condition")

#### Prerequisite is a feature flag (boolean setting)[​](#prerequisite-is-a-feature-flag-boolean-setting "Direct link to Prerequisite is a feature flag (boolean setting)")

![Flag condition anatomy (feature flag)](/docs/assets/targeting/targeting-rule/flag-condition/flag-condition-anatomy1_192dpi.png)

#### Prerequisite is a string, integer or double setting[​](#prerequisite-is-a-string-integer-or-double-setting "Direct link to Prerequisite is a string, integer or double setting")

![Flag condition anatomy (non-boolean setting)](/docs/assets/targeting/targeting-rule/flag-condition/flag-condition-anatomy2_192dpi.png)

A Flag Condition consists of the following:

* ***Prerequisite flag key*:** The key of the feature flag or setting on which the condition is based.
* ***Comparator*:** The comparison operator that defines the relation between the prerequisite flag's value and the comparison value. See the available comparators below.
* ***Comparison value*:** The value that the prerequisite flag's value is compared to. Available only when the prerequisite flag is a string, integer or double setting.

### Comparator[​](#comparator "Direct link to Comparator")

Different comparators are available for different types of prerequisites.

When the prerequisite is a feature flag (boolean setting), the following comparators are available:

| Comparator | Description                                  |
| ---------- | -------------------------------------------- |
| IS ON      | Checks whether the prerequisite flag is ON.  |
| IS OFF     | Checks whether the prerequisite flag is OFF. |

When the prerequisite is a string, integer or double setting, the following comparators are available:

| Comparator | Description                                                                        |
| ---------- | ---------------------------------------------------------------------------------- |
| EQUALS     | Checks whether the prerequisite flag's value is equal to the comparison value.     |
| NOT EQUALS | Checks whether the prerequisite flag's value is not equal to the comparison value. |

## Examples[​](#examples "Direct link to Examples")

### Enable feature depending on the availability of another one[​](#enable-feature-depending-on-the-availability-of-another-one "Direct link to Enable feature depending on the availability of another one")

#### Context[​](#context "Direct link to Context")

Our demo company, Whisker Co. has a mobile app, which, among other things, can show the cat-friendly cafés in the neighborhood.

The app can send notifications about the users' favorite cafés. This feature is not available to everyone though, it's enabled using the **Enable Cafe Notifications** feature flag. There is another feature that allows users to rate cafés, whose availability is controlled similarly, via the **Enable Cafe Ratings** feature flag.

#### Goal[​](#goal "Direct link to Goal")

We want to make sure that users only receive notifications about their favorite cafés if they can rate them.

#### Solution[​](#solution "Direct link to Solution")

ConfigCat offers a built-in way to solve this problem without the need of extra coding: prerequisite flags.

We can achieve our goal by adding a Targeting Rule containing a Flag Condition to **Enable Cafe Notifications**, then referencing **Enable Cafe Ratings** in the condition and setting the comparator to **IS ON**, meaning that the **Enable Cafe Notifications** feature flag will be enabled only if the **Enable Cafe Ratings** feature flag is ON.

On the Dashboard:

![Flag condition example](/docs/assets/targeting/targeting-rule/flag-condition/flag-condition-example_192dpi.png)
