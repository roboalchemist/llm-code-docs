# Source: https://loops.so/docs/loop-builder/loop-triggers.md

# Triggering Loops

> Learn how to trigger a Loop to start sending emails.

## Loop triggers

A Loop trigger is an event, contact update or contact addition that starts a Loop. For example, if you create a Loop that sends a welcome email to new contacts, the trigger would be when a new contact is added to your audience.

## Different types of Loop triggers

There are currently four types of triggers that you can use to start a Loop: **Contact added**, **Contact updated**, **Contact added to list** and **Event received**.

### Contact added

The **Contact added** trigger will start a Loop when a contact is added to your audience. This trigger is useful for sending welcome emails to new contacts or sending a series of onboarding emails to new customers. This trigger works for contacts added via an integration, a form, or an API call. Contacts uploaded via CSV or added individually to the audience table will not be included. As long as the contact is added to your audience with an automatic method the Loop will start.

This trigger requires no additional setup. Once you create a Loop with this trigger, you can start adding contacts to your audience and contacts will enter the Loop.

### Contact updated

The **Contact updated** trigger will start a Loop when a contact is updated in your audience. This trigger is useful for sending emails to contacts based on their actions or behavior. For example, you can send a series of emails to contacts who change their subscription plan from free to paid or from paid to canceled.

You can also set the trigger to only start the Loop when a specific field is updated from a specific value to another specific value. For example, you can send a series of emails to contacts who change their subscription plan from free to paid but exclude contacts who have updated their subscription plan from paid to canceled.

### Contact added to list

The **Contact added to list** trigger will start a Loop when a contact is added to a [mailing list](/contacts/mailing-lists). It triggers every time a contact is added to a list (so if the contact is removed from a list and then re-added, it will trigger again).

<Warning>
  This trigger is tied directly to a contact's subscription to the selected mailing list. If the contact is removed from the mailing list, they will be removed from any connected loops when they reach the next node.
</Warning>

### Event received

The **Event received** trigger will start a Loop when a contact receives a specific matching event sent via API, Integrations or a form. This trigger is great for events like payment received, order placed, or a new message received. You can fire events with the [Events API](/api-reference/send-event) or an integration.

## Trigger frequency

You can choose to trigger a Loop just the first time a contact matches the trigger settings or every time the contact matches.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/trigger-frequency.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=8bb968a8827dec66291d8719da07d2ee" alt="Trigger frequency" data-og-width="2280" width="2280" data-og-height="1434" height="1434" data-path="images/trigger-frequency.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/trigger-frequency.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=34de79e540158d313fa8ed36c516f6be 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/trigger-frequency.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f307232862d8d23edd0d808688dfc341 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/trigger-frequency.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=75a131df9db194110b311ba78c740178 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/trigger-frequency.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=aa94f5611dd57651b4e773b801748517 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/trigger-frequency.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=59050a80c0dbe4895ce2fd10a973ae65 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/trigger-frequency.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=0679b0405b8792533e4af885e9d969ab 2500w" />

For example, if you want to send to a contact every time they update their subscription plan, you can choose to trigger the Loop every time the contact is updated (select "Every time").

However, if you want to send a welcome email to a contact just the first time they are added to your audience, you can choose to trigger the Loop once when the contact is added (select "One time").

## Changing the trigger type

You can change the trigger type at any time. For example, if you create a Loop with the Contact Added trigger, you can change it to the Contact Updated trigger at any time.

## Re-triggering loops

Sometimes you may want to re-trigger a loop for certain contacts, for example if you want to add an older contact to a new email sequence.

The easiest way to do this is to [download contacts in a CSV](/contacts/export-contacts) and re-upload them with the [CSV uploader](/add-users/csv-upload#trigger-loops-via-csv). Make sure to toggle "Trigger Loops" in the last upload step.
