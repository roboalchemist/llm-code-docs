# Source: https://configcat.com/docs/targeting/user-object.md

# User Object

Copy page

The *User Object* represents a user in your application. It is a collection of *user attributes* that store various pieces of information about the user.

The User Object is necessary to evaluate [Targeting Rules](https://configcat.com/docs/targeting/targeting-rule/targeting-rule-overview.md) and [Percentage Options](https://configcat.com/docs/targeting/percentage-options.md). It allows you to pass the user attributes that are referenced in the rules of the feature flag to the ConfigCat SDK.

info

The User Object is essential if you'd like to use ConfigCat's [Targeting](https://configcat.com/docs/targeting/targeting-overview.md) feature.

## The relationship between the User Object and Targeting Rules[​](#the-relationship-between-the-user-object-and-targeting-rules "Direct link to The relationship between the User Object and Targeting Rules")

**As a product manager**, you can define [Targeting Rules](https://configcat.com/docs/targeting/targeting-rule/targeting-rule-overview.md) on the [ConfigCat Dashboard](https://app.configcat.com) based on the user attributes that are provided by your application.

**As a developer**, User Object allows you to pass user attributes to the ConfigCat SDK, which you (or your teammates) can reference in the [Targeting Rules](https://configcat.com/docs/targeting/targeting-rule/targeting-rule-overview.md) on the [Dashboard](https://app.configcat.com).

## Security and privacy concerns[​](#security-and-privacy-concerns "Direct link to Security and privacy concerns")

ConfigCat was designed with security and privacy in mind. The feature flag evaluation process is entirely implemented within the SDKs, meaning **your users' sensitive data never leaves your system**. The data flow is one-way – from ConfigCat CDN servers to your SDKs – and ConfigCat does not receive or store any attributes of the User Object passed to the SDKs. This design prioritizes the privacy and security of user data.

## Anatomy of the User Object[​](#anatomy-of-the-user-object "Direct link to Anatomy of the User Object")

The User Object offers the following properties to store user data:

| Attribute  | Description                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identifier | **REQUIRED.** We recommend using a user ID, email address, or session ID.                                                                                                           |
| Email      | Optional. Set this if you want to target users based on their email address. E.g.: "Turn on a feature for users with **@example.com** addresses only."                              |
| Country    | Optional. Specify this for location or country-based targeting. E.g.: "Turn on a feature for users in Canada only."                                                                 |
| Custom     | Optional. A map/dictionary that lets you set custom user attributes to target users based on any user data. E.g.: age, subscription type, user role, device type, app version, etc. |

### Code example[​](#code-example "Direct link to Code example")

```js
const userObject = {
  identifier: '#UNIQUE-USER-IDENTIFIER#', // required
  email: 'john@example.com',
  country: 'United Kingdom',
  custom: {
    SubscriptionType: 'Pro',
    UserRole: 'Admin',
  },
};

```

### Identifier attribute[​](#identifier-attribute "Direct link to Identifier attribute")

The unique identifier of a user in your application. This is a **REQUIRED** attribute. ConfigCat uses this attribute to differentiate your users from each other. By default, it is used to evaluate [Percentage Options](https://configcat.com/docs/targeting/percentage-options.md).

Our recommendation for an identifier:

* User ID - You can simply use the user ID native to your application.
* Email address - In most cases, using an email address works perfectly - as long as it is unique.
* Session ID - This is useful for targeting users who are not logged in to your application.

### Custom attributes[​](#custom-attributes "Direct link to Custom attributes")

To use custom attributes, you need to pass a User Object containing the `custom` property to the ConfigCat SDK.

info

The custom attribute's value can be of multiple types: e.g. string, number, date, array of strings, etc. Check the [SDK reference](https://configcat.com/docs/sdk-reference/overview.md) for more details.

## Examples[​](#examples "Direct link to Examples")

### Enable a feature for most valuable customers only[​](#enable-a-feature-for-most-valuable-customers-only "Direct link to Enable a feature for most valuable customers only")

#### Context[​](#context "Direct link to Context")

Our demo company, Whisker Co. developed a new feature called **Personalized Layout** to enhance the user experience of their most valuable customers.

#### Goal[​](#goal "Direct link to Goal")

We want to enable the **Personalized Layout** feature but only for customers with the **Pro** subscription.

#### Solution[​](#solution "Direct link to Solution")

To achieve this goal, we need a custom attribute named e.g. **SubscriptionType**, which stores the subscription type of the customer.

This allows us to define a Targeting Rule that turns on the feature for the customers whose **SubscriptionType** attribute is **Pro**. Finally, we need to make sure that the "To all others" value is **OFF** so the feature is turned off for the rest of the customers.

#### Dashboard[​](#dashboard "Direct link to Dashboard")

![Most valuable customers example](/docs/assets/targeting/user-object/most-valueable-customers-example_192dpi.png)

#### Code[​](#code "Direct link to Code")

Add the **SubscriptionType** custom attribute to the User Object in your application code.

```js
const userObject = {
  identifier: userId,
  custom: {
    SubscriptionType: 'Pro',
  },
};

```
