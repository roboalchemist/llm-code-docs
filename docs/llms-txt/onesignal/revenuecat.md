# Source: https://documentation.onesignal.com/docs/en/revenuecat.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# RevenueCat

> Sync in-app purchase and subscription data from RevenueCat to OneSignal for personalized messaging.

## Overview

RevenueCat helps you track in-app purchases and subscription lifecycles across platforms. With OneSignal, you can use this data to send personalized messages based on a user's subscription status.

This integration updates user tags in OneSignal automatically with their latest subscription info.

### Key benefits

With the RevenueCat–OneSignal integration, you can:

* Send onboarding messages to users in a free trial or who just subscribed.
* Re-engage churned users with surveys or discounts.
* Send transactional messages for purchases, billing issues, or renewals.

With accurate subscription data in OneSignal, your campaigns will be smarter and more effective.

***

## Requirements

* [RevenueCat account](https://www.revenuecat.com/docs/welcome/overview)
  * RevenueCat [*Purchases SDK*](https://www.revenuecat.com/docs/getting-started/quickstart)
  * Understand [RevenueCat-OneSignal integration](https://www.revenuecat.com/docs/integrations/third-party-integrations/onesignal)
* OneSignal account with [integrated SDK](./developers)
  * Understand [Data Tags](./add-user-data-tags), [Users](./users), and OneSignal [Subscriptions](./subscriptions)

***

## Setup

### Connect OneSignal to RevenueCat

1. In your RevenueCat dashboard, navigate to your project settings and choose 'OneSignal' from the Integrations menu.
2. Add your OneSignal App ID and OneSignal API key. See [Keys and IDs](./keys-and-ids) for more information.
3. Enter the tag names that RevenueCat should use, or choose the default tag names.

### Pass RevenueCat the OneSignal ID

RevenueCat uses the OneSignal user ID (OneSignal ID) to update user tags in OneSignal based on their RevenueCat user details.

<Warning>
  Setting the External ID in OneSignal is required for a stable identifier. If it changes mid-session, the OneSignal ID may also change, breaking the RevenueCat connection.
</Warning>

To pass the OneSignal ID to RevenueCat, you should:

<Steps>
  <Step title="Set the External ID in OneSignal">
    Set the External ID in OneSignal to your main user ID. This can be done with the SDK `login` method.

    * [Mobile SDK `login` method](./mobile-sdk-reference#login-external-id)
    * [Web SDK `login` method](./web-sdk-reference#login-external-id)
  </Step>

  <Step title="Get the OneSignal ID">
    We recommend using the user state observer method to get the OneSignal ID, but we also provide getter methods:

    * User state observers:
      * [Mobile SDK `addObserver` user state](./mobile-sdk-reference#addobserver-user-state)
      * [Web SDK `addObserver` user state](./web-sdk-reference#addeventlistener-user-state)
    * Getter methods:
      * [Mobile SDK `getOneSignalId` method](./mobile-sdk-reference#getonesignalid)
      * [Web SDK `OneSignalId` property](./web-sdk-reference#onesignal-user-onesignalid)
  </Step>

  <Step title="Pass the OneSignal ID to RevenueCat">
    Pass the OneSignal ID to RevenueCat.

    * RevenueCat property: `$onesignalUserId`
    * RevenueCat helper method: `setOneSignalUserID()` (recommended)
  </Step>
</Steps>

### Send RevenueCat events to OneSignal

Users that have a mapped OneSignal ID to RevenueCat will have their tags updated automatically.

#### Testing the integration

<Steps>
  <Step title="Make a sandbox purchase">
    Simulate a new user installing your app, and go through your app flow to complete a sandbox purchase.

    <Warning>
      Make sure the OneSignal ID is set in RevenueCat.
    </Warning>
  </Step>

  <Step title="Check that the required device data is collected">
    In RevenueCat, navigate to the Customer View for the test user that just made a purchase. Make sure that all of the required data is listed as attributes for the user.
  </Step>

  <Step title="Check that the OneSignal event delivered successfully">
    While still on the Customer View, click into the test purchase event in the Customer History and make sure that the OneSignal integration event exists and was delivered successfully.
  </Step>

  <Step title="Check that the OneSignal tags are updated">
    In OneSignal, navigate to **Audience > Users** and search for the OneSignal ID. You should see the tags that were updated by RevenueCat.
  </Step>
</Steps>

<Check>
  Integration complete! You should now see the tags in OneSignal update automatically as users make purchases or update their subscription status.
</Check>

***

## RevenueCat event tags

For every auto-renewing subscription event in RevenueCat, the following tags get added or updated on the user in OneSignal. By leaving the tag blank in the RevenueCat dashboard, you can choose to not send any value for specific tag(s).

| Tag                          | Description                                                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app_user_id`                | The RevenueCat App User Id that triggered the event                                                                                                        |
| `period_type`                | The latest period type for the purchase or renewal. Either: `TRIAL` (for free trials), `INTRO` (or introductory pricing), `NORMAL` (standard subscription) |
| `purchased_at`               | Epoch time in seconds of the latest subscription purchase or renewal                                                                                       |
| `expiration_at`              | Epoch time in seconds of the latest subscription expiration date                                                                                           |
| `store`                      | Either `APP_STORE`, `PLAY_STORE`, or `STRIPE`                                                                                                              |
| `environment`                | Either `SANDBOX` or `PRODUCTION`                                                                                                                           |
| `last_event_type`            | The latest event type from the user. Either: `INITIAL_PURCHASE`, `TRIAL_STARTED`, `TRIAL_CONVERTED`, `TRIAL_CANCELLED`, `RENEWAL`, `CANCELLATION`          |
| `product_id`                 | The latest subscription product identifier that the user has purchased or renewed                                                                          |
| `entitlement_ids`            | Comma separated string of RevenueCat Entitlement identifiers that the user unlocked                                                                        |
| `active_subscription`        | The value will be set to `true` on any purchase/renewal event, and `false` on `EXPIRATION`                                                                 |
| `subscription_status`        | See Subscription Status Attribute below                                                                                                                    |
| `grace_period_expiration_at` | If a billing issue occurs, we will send the date of the grace period expiration.                                                                           |

<Note>
  * Auto-renewing subscriptions only
  * RevenueCat only updates data tags in OneSignal in response to auto-renewing subscription events.
</Note>

### RevenueCat event examples

Provided JSON examples show the tags sent to OneSignal based on [RevenueCat Events](https://www.revenuecat.com/docs/integrations/third-party-integrations/onesignal#events).

The event is saved as the `last_event_type` tag.

<Tabs>
  <Tab title="initial_purchase">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "NORMAL",
            "purchased_at": 1600016247,
            "expiration_at": 1602608247,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "initial_purchase",
            "last_event_at": 1600016250,
            "product_id": "monthly_sub",
            "entitlement_ids": "Pro"
        }
    }
    ```
  </Tab>

  <Tab title="trial_started">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "TRIAL",
            "purchased_at": 1600031584,
            "expiration_at": 1600290784,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "trial_started",
            "last_event_at": 1600031586,
            "product_id": "three_month_sub_trial",
            "entitlement_ids": "Pro"
        }
    }
    ```
  </Tab>

  <Tab title="trial_converted">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "NORMAL",
            "purchased_at": 1602136340,
            "expiration_at": 1602741140,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "trial_converted",
            "last_event_at": 1602114850,
            "product_id": "weekly_sub_trial",
            "entitlement_ids": null
        }
    }
    ```
  </Tab>

  <Tab title="trial_cancelled">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "TRIAL",
            "purchased_at": 1602051920,
            "expiration_at": 1602311120,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "trial_cancelled",
            "last_event_at": 1602129368,
            "product_id": "weekly_sub_trial",
            "entitlement_ids": null
        }
    }
    ```
  </Tab>

  <Tab title="renewal">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "NORMAL",
            "purchased_at": 1602125078,
            "expiration_at": 1604807078,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "renewal",
            "last_event_at": 1602122793,
            "product_id": "monthly_sub",
            "entitlement_ids": "Pro"
        }
    }
    ```
  </Tab>

  <Tab title="cancellation">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "NORMAL",
            "purchased_at": 1602086660,
            "expiration_at": 1602691460,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "cancellation",
            "last_event_at": 1602118600,
            "product_id": "weekly_sub",
            "entitlement_ids": null
        }
    }
    ```
  </Tab>

  <Tab title="uncancellation">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "TRIAL",
            "purchased_at": 1663445025,
            "expiration_at": 1664049825,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "uncancellation",
            "last_event_at": 1663969096,
            "product_id": "annual_sub",
            "entitlement_ids": "Premium"
        }
    }
    ```
  </Tab>

  <Tab title="non_subscription_purchase">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "purchased_at": 1602086660,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "non_renewing_purchase",
            "last_event_at": 1602118600,
            "product_id": "one_time_purchase_product",
            "entitlement_ids": null
        }
    }
    ```
  </Tab>

  <Tab title="subscription_paused">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "NORMAL",
            "purchased_at": 1602086660,
            "expiration_at": 1602691460,
            "store": "PLAY_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "subscription_paused",
            "last_event_at": 1602118600,
            "product_id": "weekly_sub",
            "auto_resume_at": 1602119600,
            "entitlement_ids": null
        }
    }
    ```
  </Tab>

  <Tab title="expiration">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "period_type": "NORMAL",
            "purchased_at": 1652374230,
            "expiration_at": 1652979030,
            "last_event_type": "expiration",
            "last_event_at": 1652988735
        }
    }
    ```
  </Tab>

  <Tab title="billing_issue">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "TRIAL",
            "purchased_at": 1652383957,
            "expiration_at": 1654371157,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "billing_issue",
            "last_event_at": 1652988776,
            "product_id": "annual_sub",
            "entitlement_ids": "Premium"
        }
    }
    ```
  </Tab>

  <Tab title="product_change">
    ```json  theme={null}
    {
        "app_id": "12345678-1234-1234-1234-123456789012",
        "tags": {
            "app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
            "period_type": "NORMAL",
            "purchased_at": 1602086660,
            "expiration_at": 1602691460,
            "store": "APP_STORE",
            "environment": "PRODUCTION",
            "last_event_type": "product_change",
            "last_event_at": 1602118600,
            "product_id": "weekly_sub",
            "new_product_id": "monthly_sub",
            "entitlement_ids": null
        }
    }
    ```
  </Tab>
</Tabs>

### `subscription_status` tag

Whenever RevenueCat sends an event to OneSignal, a `subscription_status` tag is added or updated with any applicable changes, using one of the following values:

| Status               | Description                                                                                                           |
| :------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| active               | The customer has an active, paid subscription which is set to renew at their next renewal date.                       |
| intro                | The customer has an active, paid subscription through a paid introductory offer.                                      |
| cancelled            | The customer has a paid subscription which is set to expire at their next renewal date.                               |
| grace\_period        | The customer has a paid subscription which has entered a grace period after failing to renew successfully.            |
| trial                | The customer is in a trial period which is set to convert to paid at the end of their trial period.                   |
| cancelled\_trial     | The customer is in a trial period which is set to expire at the end of their trial period.                            |
| grace\_period\_trial | The customer was in a trial period and has now entered a grace period after failing to renew successfully.            |
| expired              | The customer's subscription has expired.                                                                              |
| promotional          | The customer has access to an entitlement through a RevenueCat                                                        |
| expired\_promotional | The customer previously had access to an entitlement through a RevenueCat Granted Entitlement that has since expired. |
| paused               | The customer has a paid subscription which has been paused and is set to resume at some future date.                  |

For customers with multiple active subscriptions, this attribute will represent the status of only the subscription for which the most recent event occurred.

***

## FAQ

### How do I know if the integration is working?

In OneSignal, navigate to **Audience > Users** and search for the OneSignal ID. You should see the tags that were updated by RevenueCat.

You can also go to **Audience > Segments** and create a segment that filters for the tags you have set via RevenueCat.

### How many tags can I set?

There is no limit to the amount of tags you can set in OneSignal, but there is a limit to how many tags each user can have at a given time.

See our [Pricing page](https://onesignal.com/pricing) for more information.

***

Built with [Mintlify](https://mintlify.com).
