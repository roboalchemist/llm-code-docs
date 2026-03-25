# Source: https://documentation.onesignal.com/docs/en/hubspot.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HubSpot

> Automate push notifications, emails, SMS, and in-app messaging from HubSpot Workflows using the native OneSignal integration.

## Overview

The OneSignal HubSpot integration connects your HubSpot CRM to OneSignal through native workflow actions — no third-party middleware required. You can:

* **Send messages** — trigger push notifications, emails, and SMS from HubSpot Workflows
* **Create users** — sync HubSpot contacts to OneSignal with email and SMS subscriptions
* **Manage tags** — set or delete OneSignal [Tags](./add-user-data-tags) based on HubSpot contact properties
* **Target in-app messages** — use tags set by HubSpot to build segments that control in-app message delivery

For capabilities like A/B testing, intelligent delivery, throttling, and retargeting, use the OneSignal dashboard or API directly alongside HubSpot.

<Tip>
  Read [Four Ways to Use the OneSignal Integration with HubSpot](https://onesignal.com/blog/four-ways-to-use-the-onesignal-integration-with-hubspot-to-boost-engagement-across-channels/) for real-world examples.
</Tip>

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/SiGsvdAD6w8?si=8_WPdcNV2COIpaGM" title="OneSignal HubSpot integration overview" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

***

## Prerequisites

* HubSpot Super Admin role or [App Marketplace Permissions](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#admin)
* A [paid OneSignal plan](https://onesignal.com/pricing) (not available on free plans)

<Info>
  HubSpot deprecated the original third-party OneSignal app in December 2024. OneSignal now provides its own HubSpot app with expanded functionality. If you used the previous integration, see the migration steps below.
</Info>

<Accordion title="Migrating from the legacy HubSpot integration">
  **Install the new integration**

  Activate the HubSpot integration from the OneSignal dashboard under **Data > Integrations** as described in [Connect HubSpot to OneSignal](#connect-hubspot-to-onesignal) below.

  **Migrate your workflows**

  We recommend creating a new workflow to test the new integration before replacing actions in your existing workflows.

  1. **Clone your workflow** — On the HubSpot **Workflows** page, click **Clone** next to your existing workflow.
  2. **Remove triggers** — In the cloned workflow, remove all enrollment triggers so it does not fire automatically when published.
  3. **Replace legacy actions** — Remove each legacy OneSignal action and replace it with the new version. If both apps are installed, the legacy app shows "Built by HubSpot" — use the one that does not.

  <Frame caption="When both apps are installed, use the OneSignal action that does not say 'Built by HubSpot'.">
    <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a4e1a11d8c343bee5850147e5809d4c94c9966248433ab0ba59e5dce79a5a8b2-image.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=9563ae1d3706dfdbe7f89b4f432a4ae7" width="920" height="1166" data-path="images/docs/a4e1a11d8c343bee5850147e5809d4c94c9966248433ab0ba59e5dce79a5a8b2-image.png" />
  </Frame>

  1. **Test with a single contact** — Save and publish the workflow, then manually enroll one test contact. Check the enrollment history to verify actions completed successfully.

  <Frame caption="Example migrated HubSpot workflow.">
    <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/687f1408480774304c930f72d62a82381c1ea11a9c66a8ce6595f568a3dd3b17-image.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=e963ea94239c19696851e6edc4f18c92" width="1482" height="487" data-path="images/docs/687f1408480774304c930f72d62a82381c1ea11a9c66a8ce6595f568a3dd3b17-image.png" />
  </Frame>

  1. **Replace or update** — After confirming the workflow works correctly, either replace the original workflow with the clone or apply the same changes to the original.

  If you encounter errors during migration, contact `support@onesignal.com`.
</Accordion>

***

## Connect HubSpot to OneSignal

### Activate the integration

In OneSignal, go to **Data > Integrations > Catalog** and select **HubSpot**.

<Frame caption="The HubSpot integration card on the OneSignal Integrations page.">
  <img src="https://mintcdn.com/onesignal/yCAJt5-6hubcDKe8/images/integrations/catalog-hubspot.png?fit=max&auto=format&n=yCAJt5-6hubcDKe8&q=85&s=91266c81fdf4cea8962c73761cc0c374" width="2902" height="1806" data-path="images/integrations/catalog-hubspot.png" />
</Frame>

Click **Settings > Authenticate**, then select your HubSpot account and log in.

<Warning>
  You can only connect one HubSpot account to each OneSignal app. If you have a testing environment, you can setup another OneSignal app for testing.
</Warning>

<Frame caption="Select which HubSpot account to connect to this OneSignal app.">
  <img src="https://mintcdn.com/onesignal/yCAJt5-6hubcDKe8/images/integrations/hubspot-settings.png?fit=max&auto=format&n=yCAJt5-6hubcDKe8&q=85&s=7faf6812bc71b1fd629c963de34e9efb" width="2902" height="1806" data-path="images/integrations/hubspot-settings.png" />
</Frame>

After agreeing to the terms and selecting **Connect app**, you are redirected to OneSignal. Open the newly connected HubSpot account to confirm the connection.

### Match users with External ID

To link HubSpot contacts to OneSignal users, set the [External ID](./users) in OneSignal to a value that matches a unique property in HubSpot (e.g., a user ID or email address).

Set External ID using the SDK `login` method in your app or website. Choose a property that is readily available in both your app and HubSpot so matching is reliable.

<Info>
  See [Users](./users) and [Subscriptions](./subscriptions) for details on identity and subscription management.
</Info>

### Create a HubSpot workflow

In HubSpot, go to **Automation > Workflows** and click **Create workflow**. Select **Contact-based** and configure your enrollment triggers.

To add a OneSignal action, click **+** in the workflow editor and search for "OneSignal."

<Frame caption="OneSignal workflow actions in HubSpot.">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7857e4e4ce869bb57dfbce033baf2239054ba81e207a81565a62fe5618fb373b-Screenshot_2025-01-23_at_1.16.10_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=ea5f0eb7187127a9f4fef2e338ac5a2c" width="1866" height="1340" data-path="images/docs/7857e4e4ce869bb57dfbce033baf2239054ba81e207a81565a62fe5618fb373b-Screenshot_2025-01-23_at_1.16.10_PM.png" />
</Frame>

Every OneSignal action requires two fields:

<Frame caption="Setting the OneSignal App and External ID in a workflow action.">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a9f3c793693436c0f9ef5c421f600b21ae241310e672303cb2f95fb7f0f8d103-Screenshot_2025-01-31_at_1.40.32_PM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=162b4cc4654129a4c029d4f0fa5041b8" width="828" height="550" data-path="images/docs/a9f3c793693436c0f9ef5c421f600b21ae241310e672303cb2f95fb7f0f8d103-Screenshot_2025-01-31_at_1.40.32_PM.png" />
</Frame>

* **OneSignal App** — the app you connected during setup
* **External ID** — the HubSpot contact property that matches the External ID in OneSignal

***

## OneSignal actions

### Create OneSignal users from HubSpot

The **Create User** action creates a [User](./users) in OneSignal when a contact passes through the workflow. Use this to keep OneSignal and HubSpot in sync as new contacts are added.

If the following HubSpot properties are set, OneSignal automatically creates corresponding [Subscriptions](./subscriptions):

* **Email** → creates an email subscription in OneSignal
* **Phone number** → creates an SMS subscription in OneSignal

You can also set the External ID and tags within the Create User node.

<Frame caption="OneSignal Create User node in a HubSpot workflow.">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/544e379b13eab1fdddfdaf646a879152ea6251f1833870f5ed2671e0e2558506-Screenshot_2025-03-10_at_4.34.19_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=c12475968bf18c8353ef576882855d03" width="1030" height="817" data-path="images/docs/544e379b13eab1fdddfdaf646a879152ea6251f1833870f5ed2671e0e2558506-Screenshot_2025-03-10_at_4.34.19_PM.png" />
</Frame>

<Warning>
  If your OneSignal app has [Double Opt-in](./sms-opt-in-and-collection#promotional-double-opt-in-form) enabled, new SMS subscriptions automatically receive an opt-in message. You can disable this in the Create User node — the SMS subscription will be created but the user will not be subscribed until they opt in separately.
</Warning>

***

### Edit OneSignal tags from HubSpot

The **Edit Tags** action sets or deletes [Tags](./add-user-data-tags) on the matched OneSignal user. Tags enable [Message Personalization](./message-personalization) and [Segmentation](./segmentation), and are the mechanism for [targeting in-app messages from HubSpot](#send-in-app-messages-with-hubspot).

#### Set tags

Enter a JSON object in the Tags field:

```json  theme={null}
{ "welcome": "1", "name": "<First Name property>" }
```

You can inject any HubSpot contact property as a tag value by using HubSpot's property token inserter in the workflow editor. For example, adding a user's first name as a tag so you can personalize messages in OneSignal.

#### Delete tags

Set the value to an empty string to remove a tag:

```json  theme={null}
{ "old_tag": "" }
```

If the tag does not exist on the user, it is ignored.

<Frame caption="Setting two tags ('welcome' and 'name') and deleting one ('key') in the Edit Tags action.">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/bb4ff8e3b5c8bf3742d721f94791f2e97137b89f58f3e862ff650b2c58d1e43a-Screenshot_2025-01-23_at_1.46.35_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=6df8727cc9c5dd212c0c4ac62aeae71a" width="1866" height="1340" data-path="images/docs/bb4ff8e3b5c8bf3742d721f94791f2e97137b89f58f3e862ff650b2c58d1e43a-Screenshot_2025-01-23_at_1.46.35_PM.png" />
</Frame>

***

### Send messages from HubSpot workflows

The **Send Notification** action delivers a push notification, email, or SMS to the matched OneSignal user.

<Tip>
  Match users by **OneSignal External ID** rather than email. Email matching is a legacy option for customers who set email using the `addEmail` SDK method.
</Tip>

<Frame caption="Configuring the Send OneSignal Notification action.">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c240529d9ab770443b90a8eb61db498edde6fdacc2c4a8efc8e1eb6c26582955-Screenshot_2025-01-23_at_2.19.19_PM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=bf5975fd590611d5aedc7f297d4262d2" width="1866" height="1340" data-path="images/docs/c240529d9ab770443b90a8eb61db498edde6fdacc2c4a8efc8e1eb6c26582955-Screenshot_2025-01-23_at_2.19.19_PM.png" />
</Frame>

**Using a template**

Select a predefined [Template](./templates) created in the OneSignal dashboard or API. Templates support push notifications, email, and SMS.

**Using form fields**

If you do not select a template, you can compose a push notification directly in the workflow action using the Title, Subtitle, Message, Image URL, and Launch URL fields. Email and SMS are only available via templates.

The form fields option allows you to inject HubSpot contact properties (e.g., `First Name`) to personalize the notification content.

***

#### Send in-app messages with HubSpot

In-app messages cannot be sent directly from a HubSpot workflow. Instead, use HubSpot to tag users, then target those users with a segment-based in-app message in OneSignal.

<Steps>
  <Step title="Tag users from HubSpot">
    In your HubSpot workflow, use the [Edit Tags](#edit-onesignal-tags-from-hubspot) action to set a tag on contacts. For example: `{ "hubspot_campaign": "spring_promo" }`.
  </Step>

  <Step title="Create a segment in OneSignal">
    In the OneSignal dashboard, go to **Audience > Segments** and click **New Segment**. Add a **User Tag** filter matching the tag key and value set by HubSpot (e.g., `hubspot_campaign` is `spring_promo`).
  </Step>

  <Step title="Create the in-app message">
    Go to **Messages > In-App** and create a new in-app message. Under **Audience**, select **Show to Particular Segment(s)** and choose the segment you created.

    As users pass through the HubSpot workflow and receive the tag, they are added to the segment immediately.
  </Step>

  <Step title="Configure the trigger">
    Tags do not trigger in-app messages on their own. If the tag is set while the user is actively using the app, the in-app message does not display until the next session (a new session starts after the app is in the background for 30+ seconds).

    Available triggers:

    * **On app open** — displays the next time the user opens the app
    * **Session duration** — displays after a set number of seconds in-session
    * **Time since last in-app message** — prevents back-to-back messages
    * **Programmatic** — trigger from your app code using the OneSignal SDK

    See [In-App Message Triggers](./iam-triggers) for details on combining triggers with AND/OR operators.
  </Step>
</Steps>

***

## Common workflow patterns

HubSpot workflows combine **enrollment triggers** (the event that starts the workflow) with **OneSignal actions** (what happens to the user in OneSignal). Below are recommended patterns for common use cases.

<Info>
  Every workflow pattern below assumes you have already [connected HubSpot to OneSignal](#connect-hubspot-to-onesignal) and are [matching users via External ID](#match-users-with-external-id).
</Info>

### Welcome and onboarding

Send a welcome message when a new user signs up, and tag them for onboarding in-app messages.

| Step                   | Type                         | Configuration                                                                                                          |
| ---------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Enrollment trigger** | HubSpot                      | Contact property `Became a customer date` is known                                                                     |
| **Action 1**           | OneSignal: Create User       | Set External ID to the HubSpot contact property that matches your app (e.g., a user ID or email address)               |
| **Action 2**           | OneSignal: Edit Tags         | `{ "onboarding": "active", "name": "<First Name>" }` — insert the HubSpot First Name property token for the name value |
| **Action 3**           | OneSignal: Send Notification | Use a welcome push template, or compose inline with a personalized greeting                                            |

<Tip>
  Pair this with an [in-app message](#send-in-app-messages-with-hubspot) that targets the `onboarding` = `active` segment to guide new users through your app on first launch.
</Tip>

### Re-engagement

Reach out to users who have not visited your app recently.

| Step                   | Type                         | Configuration                                                               |
| ---------------------- | ---------------------------- | --------------------------------------------------------------------------- |
| **Enrollment trigger** | HubSpot                      | Contact property `Last activity date` is more than 14 days ago              |
| **Action 1**           | OneSignal: Send Notification | Use a re-engagement push template (e.g., "We miss you — here's what's new") |
| **Delay**              | HubSpot: Wait 3 days         | —                                                                           |
| **If/then branch**     | HubSpot                      | Check if contact has visited your site since enrollment                     |
| **Yes branch**         | OneSignal: Edit Tags         | `{ "reengaged": "true" }`                                                   |
| **No branch**          | OneSignal: Send Notification | Use an email template with a stronger incentive                             |

### Lifecycle stage change

Sync lifecycle stage changes in HubSpot with OneSignal tags so you can target different user segments.

| Step                   | Type                         | Configuration                                                                                                  |
| ---------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Enrollment trigger** | HubSpot                      | Contact property `Lifecycle stage` changes to any value                                                        |
| **Action 1**           | OneSignal: Edit Tags         | `{ "lifecycle_stage": "<Lifecycle Stage>" }` — insert the HubSpot Lifecycle Stage property token for the value |
| **If/then branch**     | HubSpot                      | Check if lifecycle stage = `Customer`                                                                          |
| **Yes branch**         | OneSignal: Send Notification | Use a "Welcome to the family" push or email template                                                           |

### Deal closed / post-purchase

Trigger a thank-you message and tag users for upsell campaigns after a deal closes.

| Step                   | Type                         | Configuration                                                                                                    |
| ---------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Enrollment trigger** | HubSpot                      | Deal property `Deal stage` = `Closed Won`                                                                        |
| **Action 1**           | OneSignal: Edit Tags         | `{ "customer": "true", "deal_value": "<Amount>" }` — insert the HubSpot Deal Amount property token for the value |
| **Action 2**           | OneSignal: Send Notification | Use a thank-you email template                                                                                   |
| **Delay**              | HubSpot: Wait 7 days         | —                                                                                                                |
| **Action 3**           | OneSignal: Send Notification | Use an upsell/cross-sell push template                                                                           |

<Note>
  Deal-based workflows require a **Deal-based** workflow type in HubSpot. Use the associated contact's External ID to match the OneSignal user.
</Note>

### Promotional campaign via in-app message

Target a specific audience with an in-app message triggered by a HubSpot list or form.

| Step                   | Type                 | Configuration                                                                      |
| ---------------------- | -------------------- | ---------------------------------------------------------------------------------- |
| **Enrollment trigger** | HubSpot              | Contact becomes a member of a static or active list (e.g., "Spring Sale Eligible") |
| **Action 1**           | OneSignal: Edit Tags | `{ "promo": "spring_2025" }`                                                       |

Then follow the [Send in-app messages with HubSpot](#send-in-app-messages-with-hubspot) steps to create a OneSignal segment matching `promo` = `spring_2025` and configure an in-app message for that segment.

To remove users from the campaign after it ends, create a second workflow that deletes the tag:

| Step                   | Type                 | Configuration                            |
| ---------------------- | -------------------- | ---------------------------------------- |
| **Enrollment trigger** | HubSpot              | Date-based, set to the campaign end date |
| **Action 1**           | OneSignal: Edit Tags | `{ "promo": "" }`                        |

***

## Troubleshooting

### Workflow action shows "Failed" in HubSpot

1. **Check the error message** — Expand the failed action in the HubSpot workflow enrollment history. The error message often indicates the cause (e.g., "User not found," "Invalid app ID").
2. **Verify the External ID** — Confirm the HubSpot contact property used as the External ID matches a user in OneSignal. Check the user's profile in **OneSignal > Audience > Users** and search by External ID.
3. **Confirm the integration is active** — Go to **OneSignal > Data > Integrations > HubSpot** and verify the connection status is active.

### Message sent but user did not receive it

1. **Check subscriptions** — The user must have an active subscription for the channel you're sending on (push, email, or SMS). Verify this in the user's profile in OneSignal under **Subscriptions**.
2. **Check segment membership** — If you're using a template with segment targeting, confirm the user belongs to the targeted segment.
3. **Review message reports** — In the OneSignal dashboard, go to **Messages**, find the message, and check its delivery report to see if the message was delivered, dropped, or errored.

### Tags not appearing on the OneSignal user

1. **Verify External ID matching** — If the External ID in the workflow does not match an existing OneSignal user, the Edit Tags action silently fails. Use the **Create User** action before Edit Tags to ensure the user exists.
2. **Check JSON format** — Tags must be a valid JSON object. Common mistakes include missing quotes around keys or values, trailing commas, or using single quotes instead of double quotes.
3. **Check for empty values** — Setting a tag value to `""` deletes the tag. Verify that HubSpot contact properties being injected are not blank.

### In-app message not displaying

See [Why didn't my in-app message display after the tag was set?](#why-didnt-my-in-app-message-display-after-the-tag-was-set) in the FAQ below.

***

## FAQ

### What data is shared between HubSpot and OneSignal?

| HubSpot            | Direction | OneSignal         | Description                                                                                                            |
| ------------------ | --------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Contact properties | →         | External ID, Tags | HubSpot contact data matches and enriches OneSignal users via [External ID](./users) and [Tags](./add-user-data-tags). |
| Workflows          | ←         | Message Templates | OneSignal [Templates](./templates) are available for selection in HubSpot workflow actions.                            |

The integration does not sync HubSpot lists, deals, or company records to OneSignal automatically. Use workflow actions to explicitly pass the data you need.

### What happens if the External ID doesn't match a OneSignal user?

The **Send Notification** and **Edit Tags** actions silently fail — no message is sent and no tags are set. Always place a **Create User** action before other OneSignal actions in your workflow to ensure the user exists in OneSignal.

### Can I use HubSpot lists to target OneSignal segments?

Not directly. HubSpot lists and OneSignal segments are independent systems. To bridge them, create a workflow that enrolls contacts from a HubSpot list and uses the **Edit Tags** action to set a tag. Then build a OneSignal segment based on that tag. See [Promotional campaign via in-app message](#promotional-campaign-via-in-app-message) for a worked example.

### Which OneSignal channels can I send from HubSpot?

Push notifications can be sent using templates or form fields. Email and SMS can only be sent using [Templates](./templates) created in OneSignal. In-app messages cannot be sent from HubSpot workflows — use the [tag-and-segment pattern](#send-in-app-messages-with-hubspot) instead.

### Why didn't my in-app message display after the tag was set?

Tags alone do not trigger in-app messages. The tag adds the user to a segment, but the in-app message still requires a **trigger** to display. If the tag is set while the user is actively using the app, the message will not appear until the next session (30+ seconds in background). Set the in-app message trigger to **On app open** for the most reliable behavior. See [In-App Message Triggers](./iam-triggers) for all trigger options.

### Can I use HubSpot webhooks to call the OneSignal API directly?

Yes. HubSpot's **Custom Code** workflow action lets you make HTTP requests to external APIs. You can call the [OneSignal REST API](/reference/create-notification) to send messages, create users, or update tags outside the native integration. This is useful for use cases the native actions do not cover, such as sending to a segment rather than an individual user.

### Can I send OneSignal message events back to HubSpot?

Yes. Use [Event Streams](./event-streams) to export OneSignal message events (sent, clicked, etc.) to a webhook endpoint. You can route these events to HubSpot's [Custom Events API](https://developers.hubspot.com/docs/api/analytics/events) or use a middleware service to update HubSpot contact properties based on OneSignal engagement data.

### Can I trigger a OneSignal Journey from HubSpot?

There are two options for getting HubSpot users into a OneSignal [Journey](./journeys-overview):

1. **Tags** — Use the [Edit Tags](#edit-onesignal-tags-from-hubspot) action to set a tag on the user. Create a segment in OneSignal based on that tag and use the segment as a Journey entry condition.
2. **Custom Events** — Use HubSpot's **Custom Code** action to call the [OneSignal Custom Events API](/reference/create-custom-events), which can serve as a Journey entry trigger.

### Can I send custom events from HubSpot to OneSignal?

Not through the native workflow actions. The native integration supports Create User, Edit Tags, and Send Notification. To send custom events, use HubSpot's **Custom Code** action to call the [OneSignal Custom Events API](/reference/create-custom-events) directly.

### What HubSpot enrollment triggers work with OneSignal?

Any HubSpot enrollment trigger works — the OneSignal actions are standard workflow actions that execute regardless of how the contact was enrolled. Common triggers include:

* **Contact property changes** (lifecycle stage, lead status, last activity date)
* **Form submissions** (signup forms, demo requests, event registrations)
* **List membership** (added to a static or active list)
* **Deal stage changes** (pipeline progression, closed won/lost)
* **Date-based** (scheduled campaigns, time since an event)
* **Manual enrollment** (for one-off sends or testing)

### How do I test a workflow before going live?

1. Create the workflow and remove all automatic enrollment triggers
2. Save and publish the workflow
3. Manually enroll a single test contact
4. Check the enrollment history in HubSpot for action success/failure
5. Verify the user, tags, or message in the OneSignal dashboard
6. Once confirmed, add your enrollment triggers and re-publish

***

<Columns cols={3}>
  <Card title="Tags" icon="tag" href="./add-user-data-tags">
    Add custom properties to users for personalization and segmentation.
  </Card>

  <Card title="Templates" icon="file-lines" href="./templates">
    Create reusable message templates for push, email, and SMS.
  </Card>

  <Card title="Journeys" icon="route" href="./journeys-overview">
    Build automated multichannel messaging flows triggered by user behavior.
  </Card>

  <Card title="Event Streams" icon="bolt" href="./event-streams">
    Export real-time message events to external platforms via webhooks.
  </Card>

  <Card title="Segmentation" icon="users" href="./segmentation">
    Build audience segments based on tags, behavior, and user properties.
  </Card>

  <Card title="In-App Message Triggers" icon="bell" href="./iam-triggers">
    Control when and how in-app messages display to users.
  </Card>
</Columns>

Built with [Mintlify](https://mintlify.com).
