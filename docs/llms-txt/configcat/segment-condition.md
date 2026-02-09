# Source: https://configcat.com/docs/targeting/targeting-rule/segment-condition.md

# Segment Condition

Copy page

## What is a Segment Condition? What is a segment?[​](#what-is-a-segment-condition-what-is-a-segment "Direct link to What is a Segment Condition? What is a segment?")

A *Segment Condition* is a condition that is based on the evaluation of a segment. A *segment* is approximately a reusable, predefined [User Condition](https://configcat.com/docs/targeting/targeting-rule/user-condition.md).

Segments allow you to define user groups based on any user attribute. You can reference segments in Targeting Rules. When you update a segment definition, the changes will be reflected automatically in all the Targeting Rules that reference it.

For example, you can define a segment called **Beta Testers** and use that segment for all features you want to be available to beta testers.

One segment belongs to one product and can be used in multiple feature flags within the same product.

## How does the Segment Condition work?[​](#how-does-the-segment-condition-work "Direct link to How does the Segment Condition work?")

The segment is evaluated with the [User Object](https://configcat.com/docs/targeting/user-object.md). Then the result is checked against the comparator you set on the Dashboard:

* For **IS IN SEGMENT**, the result of the Segment Condition will be the same as the result of the segment itself.
* For **IS NOT IN SEGMENT**, the result will be negated (i.e. it will be the opposite of the result of the segment).

For more details on the evaluation of Segment Conditions, please refer to [Feature Flag Evaluation](https://configcat.com/docs/targeting/feature-flag-evaluation.md#evaluation-of-a-segment-condition).

## How to set a Segment Condition?[​](#how-to-set-a-segment-condition "Direct link to How to set a Segment Condition?")

You can add a Segment Condition to a feature flag by clicking the **+IF** ("Add targeting rule") button on the Dashboard.

![Target a segment](/docs/assets/targeting/targeting-rule/segment-condition/target-segment_192dpi.png)

## Where can I define segments?[​](#where-can-i-define-segments "Direct link to Where can I define segments?")

You can define your segments on the ConfigCat Dashboard, on the [Segments page](https://app.configcat.com/product/segments).

![Add segment](/docs/assets/targeting/targeting-rule/segment-condition/add-segment_192dpi.png)

## Anatomy of a Segment Condition[​](#anatomy-of-a-segment-condition "Direct link to Anatomy of a Segment Condition")

![Segment condition](/docs/assets/targeting/targeting-rule/segment-condition/segment-condition-anatomy_192dpi.png)

A Segment Condition consists of two parts:

* ***Segment comparator*:** The comparison operator defines the relation between the user and the segment. See the available comparators below.
* ***Segment*:** The segment that the condition is based on.

### Segment comparator[​](#segment-comparator "Direct link to Segment comparator")

| Comparator        | Description                                             |
| ----------------- | ------------------------------------------------------- |
| IS IN SEGMENT     | Checks whether the user is in the selected segment.     |
| IS NOT IN SEGMENT | Checks whether the user is not in the selected segment. |

## Anatomy of a Segment[​](#anatomy-of-a-segment "Direct link to Anatomy of a Segment")

| Field                | Purpose                                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                 | The name of the segment.                                                                                                                           |
| Description          | The description of the segment. It's a good idea to add a hint that helps you remember what the segment is for.                                    |
| Comparison attribute | The attribute that the segment is based on. Can be **Identifier** (user ID), **Email**, **Country**, or any custom attribute.                      |
| Comparator           | The comparison operator. Defines the relation between the comparison attribute and the comparison value.                                           |
| Comparison value     | The value that the attribute is compared to. Can be a string, a number, a semantic version or a comma-separated list, depending on the comparator. |

### Comparison attribute[​](#comparison-attribute "Direct link to Comparison attribute")

A property of your user (e.g. email address, geographic location). Your application should pass the attribute values (e.g. `'jane@example.com'`, `'Europe'`) to the ConfigCat SDK as a [User Object](https://configcat.com/docs/targeting/user-object.md).

There are 3 predefined attributes. Additionally, you can define your custom attributes as well:

| Comparison attribute name | Description                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| Identifier                | Usually, it is a unique user identifier in your application.                                        |
| Email                     | The e-mail address of your user.                                                                    |
| Country                   | The location of your user. Might be useful for testing a new feature in specific countries only.    |
| Custom                    | Any additional attribute (e.g. **OS version**). Can be defined by typing its name into the textbox. |

### Comparison value[​](#comparison-value "Direct link to Comparison value")

Any string, number, or comma-separated list. Will be compared to the selected comparison attribute using the comparator. **Max. length: 65535 characters.**

### Comparator[​](#comparator "Direct link to Comparator")

#### Confidential text comparators[​](#confidential-text-comparators "Direct link to Confidential text comparators")

We recommend using confidential text comparators when targeting users based on their sensitive data (like email address, name, etc.) In this case, the feature flag evaluation is performed using the SHA256 hashes of the values to ensure that the comparison values are not exposed. This can cause an increase in the size of the config JSON file and the overall network traffic. Yet it is not recommended to use the cleartext version of the confidential comparators unless the increased network traffic becomes an issue.

The following comparators expect the comparison attribute to be a string value and the comparison value to be a string or a list of strings. The comparison is case-sensitive.

| Comparator             | Description                                                                                                                                        |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| IS ONE OF (hashed)     | Checks whether the comparison attribute is equal to any of the comparison values. (Comparison value is interpreted as a comma-separated list.)     |
| IS NOT ONE OF (hashed) | Checks whether the comparison attribute is not equal to any of the comparison values. (Comparison value is interpreted as a comma-separated list.) |

#### Text comparators[​](#text-comparators "Direct link to Text comparators")

The following comparators expect the comparison attribute to be a string value and the comparison value to be a string or a list of strings. The comparison is case-sensitive.

info

Consider using confidential text comparators if you plan to target users based on their sensitive data, e.g. email address or company domain.

| Comparator                   | Description                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONTAINS (cleartext)         | Checks whether the comparison attribute contains the comparison value as a substring.                                                              |
| DOES NOT CONTAIN (cleartext) | Checks whether the comparison attribute does not contain the comparison value as a substring.                                                      |
| IS ONE OF (cleartext)        | Checks whether the comparison attribute is equal to any of the comparison values. (Comparison value is interpreted as a comma-separated list.)     |
| IS NOT ONE OF (cleartext)    | Checks whether the comparison attribute is not equal to any of the comparison values. (Comparison value is interpreted as a comma-separated list.) |

#### Semantic version comparators[​](#semantic-version-comparators "Direct link to Semantic version comparators")

The following comparators expect the comparison attribute to be a string containing a valid semantic version and the comparison value to be a semantic version or a list of semantic versions.

Comparison is performed according to the [Semantic Versioning specification](https://semver.org/).

| Comparator             | Description                                                                                                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IS ONE OF (semver)     | Checks whether the comparison attribute interpreted as a semantic version is equal to any of the comparison values. (Comparison value is interpreted as a comma-separated list of semantic versions.)     |
| IS NOT ONE OF (semver) | Checks whether the comparison attribute interpreted as a semantic version is not equal to any of the comparison values. (Comparison value is interpreted as a comma-separated list of semantic versions.) |
| < (semver)             | Checks whether the comparison attribute interpreted as a semantic version is less than the comparison value.                                                                                              |
| <= (semver)            | Checks whether the comparison attribute interpreted as a semantic version is less than or equal to the comparison value.                                                                                  |
| > (semver)             | Checks whether the comparison attribute interpreted as a semantic version is greater than the comparison value.                                                                                           |
| >= (semver)            | Checks whether the comparison attribute interpreted as a semantic version is greater than or equal to the comparison value.                                                                               |

#### Number comparators[​](#number-comparators "Direct link to Number comparators")

The following comparators expect the comparison attribute and the comparison value to be numbers.

| Comparator  | Description                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| = (number)  | Checks whether the comparison attribute interpreted as a decimal number is equal to the comparison value.                 |
| <> (number) | Checks whether the comparison attribute interpreted as a decimal number is not equal to the comparison value.             |
| < (number)  | Checks whether the comparison attribute interpreted as a decimal number is less than the comparison value.                |
| <= (number) | Checks whether the comparison attribute interpreted as a decimal number is less than or equal to the comparison value.    |
| > (number)  | Checks whether the comparison attribute interpreted as a decimal number is greater than the comparison value.             |
| >= (number) | Checks whether the comparison attribute interpreted as a decimal number is greater than or equal to the comparison value. |

## Examples[​](#examples "Direct link to Examples")

### Beta testing scenario[​](#beta-testing-scenario "Direct link to Beta testing scenario")

#### Context[​](#context "Direct link to Context")

The developers at our demo company, Whisker Co. just finished implementing a nice new feature which allows users to personalize the layout of the webshop. It's time for a beta test.

#### Goal[​](#goal "Direct link to Goal")

We want to make the **Personalized Layout** feature of the webshop available to the beta testers.

#### Solution[​](#solution "Direct link to Solution")

We could simply achieve our goal using a Targeting Rule with a User Condition. However, **Personalized Layout** is certainly not the last feature developed at Whisker Co., so it's a good idea to create a segment named e.g. **Beta Testers** for our beta testers. This makes it easier for us to release further features for beta testing in the future.

After creating the segment, we can complete our task by adding a Targeting Rule containing a Segment Condition to **Enable Personalized Layout**, then referencing the **Beta Testers** segment in the condition and setting the comparator to **IS IN SEGMENT**.

On the Dashboard:

![Beta testing example](/docs/assets/targeting/targeting-rule/segment-condition/beta-testing-example_192dpi.png)
