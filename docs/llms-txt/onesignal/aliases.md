# Source: https://documentation.onesignal.com/docs/en/aliases.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Aliases

> Learn how to use custom aliases in OneSignal to identify and track users across different platforms and devices using your own unique identifiers. Aliases help unify user data across multiple sources and are essential for integrations, user data management, and transactional messaging.

Custom aliases allow you to assign custom key-value identifiers to users in OneSignal, enabling cross-platform user tracking and identification using your own internal IDs.

<Warning>
  **Important**: You must set an [External ID](./users) **before** using custom aliases.

  OneSignal uses a unique `onesignal_id` to identify users. This ID only stays consistent across [Subscriptions](./subscriptions) if they have the same `external_id`.

  Custom aliases **do not** link Subscriptions together—they rely on the `external_id` to work correctly. Without it, aliases won't associate with the same user across devices or platforms.
</Warning>

***

## What is a custom alias?

A custom alias is a `key : value` pair where:

* The `alias_label` (key) is a consistent, static identifier across all users (e.g., `facebook_id`, `firebase_id`, `crm_user_id`).
* The `alias_id` (value) is the specific user’s ID for that label (e.g., `facebook_id: 3453443`, `firebase_id: test3555`).

This allows you to link OneSignal user records to identifiers from your other platforms or databases.

***

## Why use aliases?

1. Identify users across multiple platforms and databases.
2. Send targeted transactional messages using the [Create Message REST API](/reference/create-message).
3. Fetch, update, or delete users via the User REST APIs.

***

## How to Set Aliases

You can set aliases either using the OneSignal SDK or via the REST API.

### Using the SDK

Follow these steps in your app:

1. Set the External ID
   Call `OneSignal.login(externalId)` to associate the user record.

2. Set custom aliases
   Use `OneSignal.User.addAlias(label, id)` to add a single alias, or `OneSignal.User.addAliases({ label1: id1, label2: id2 })` to set multiple.

3. Logout (optional)
   Use `OneSignal.logout()` to remove the external ID and any associated aliases for that device or session.

**Example**:

```javascript  theme={null}
OneSignal.login("user_123");

OneSignal.User.addAliases({
  facebook_id: "3453443",
  firebase_id: "test3555"
});

// Later, when the user logs out
OneSignal.logout();
```

***

### Using the REST API

To set custom aliases via the API, use the [Create Alias](/reference/create-alias) endpoint. This method is typically used in backend systems for server-side user management.

**Example Request**:

```json  theme={null}
POST /aliases
{
  "subscription_id": "abc123",
  "aliases": {
    "facebook_id": "3453443",
    "crm_user_id": "XYZ789"
  }
}
```

***

## Best practices

* Always set the `external_id` before assigning any aliases.
* Use stable, descriptive labels (e.g., `crm_user_id`, `legacy_user_id`) to avoid confusion across teams.
* Avoid using sensitive information such as email addresses or phone numbers as alias values.
* Use `logout()` to clean up aliases on device sign-out or user switch events.

***

<Check>
  Custom aliases tutorial complete!
  Next steps:

* Review our [Users](./users) and [Subscriptions](./subscriptions) documentation if you have not already.
* Explore our [REST API](/reference/create-alias) documentation for more details on using aliases via the API.
* Set up [Integrations](./integrations) to sync user data across systems.
</Check>

***

Built with [Mintlify](https://mintlify.com).
