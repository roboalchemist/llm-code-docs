# Source: https://loops.so/docs/integrations/clerk.md

# Clerk

> Sync contacts and send emails triggered by events in Clerk.

<Info>
  Our Clerk integration lets you:

  * Create and update contacts
  * Send events to trigger loops
</Info>

Our Clerk integration is built on top of our [Incoming webhooks](/integrations/incoming-webhooks) feature. This system lets you send webhooks from supported platforms directly to Loops so you can easily sync users and customers as well as send automated emails.

[Please read our guide about incoming webhooks](/integrations/incoming-webhooks)

With Clerk, you can keep your user data synced to Loops so you can send emails to your userbase.

## Supported events

We accept the following events:

* `user.created`
* `user.deleted`
* `user.updated`
* `waitlistEntry.created`
* `waitlistEntry.updated`

[Clerk webhook docs](https://clerk.com/docs/webhooks/overview)

If you send other events, they will be ignored.

<Info>
  If you would like to see more events supported, please let us know by sending
  an email to [help@loops.so](mailto:help@loops.so). Please keep in mind only
  events that contain an email address are able to be processed.
</Info>

## Synced data

For `user.created` or `user.updated` events, we sync the following Clerk data to your Loops contacts:

* User ID
* Email address
* First name (optional)
* Last name (optional)

We use the IDs of Clerk users to match contacts in your Loops audience. If the user ID is not found in Loops, we will create a new contact.

The `user.deleted` event can be used to delete or unsubscribe your Clerk users from your Loops audience.

For `waitlistEntry.*` events, we sync:

* Email address

There is no user ID available for waitlist events. When a user graduates from your waitlist to being a user (i.e. you accept them and they complete their account), their user ID will be added to your contact in Loops.

## Create a webhook endpoint in Loops

[Follow the instructions here](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops) to create a new webhook endpoint, which will allow you to send webhook events directly to Loops.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-clerk.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=21c2650c2d23f306f4c9bedf1c04f34d" alt="Endpoint form" data-og-width="2280" width="2280" data-og-height="1556" height="1556" data-path="images/create-endpoint-clerk.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-clerk.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f731f551ee6cdaf3bfec87bf5a530067 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-clerk.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=02f5edbb10ae23f238d26dacc3a2b4ae 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-clerk.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6016e70afb776aac079b2a2e49893e2b 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-clerk.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=986f5fa3146d7c03fee1833b08a114a7 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-clerk.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=481758146e08b3328b93e23a545842ff 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-clerk.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=074bf2ce4753211b4951935a34580582 2500w" />

## Create a webhook in Clerk

Next, you need to set up webhooks in Clerk.

Inside a project in Clerk, go to **Configure -> Webhooks** and click **+ Add Endpoint**. Paste in the endpoint URL from Loops, then select the event(s) you want to send (see our [supported events](#supported-events) above).

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-webhook.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=72ff9f5552ea8207c8abe68852d739e8" alt="Adding a webhook in Clerk" data-og-width="2280" width="2280" data-og-height="2658" height="2658" data-path="images/clerk-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-webhook.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d65104dbf1b074eb8c6273a48c04b7c5 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-webhook.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=35990666e84175604f133e25fe654e24 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-webhook.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6473574282eb19e5558337e0f4ce9f47 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-webhook.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0ea75a829087873c35b5ee94084ee430 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-webhook.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=2e90c84722f530de3009df436a87dd3a 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-webhook.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=4bc2fb2c94445556b774da56fa56606f 2500w" />

Click **Create** to finish.

The last step is to copy the signing secret into Loops. On the webhook page in Clerk, click the eye icon on the right to show the secret in the page. Copy the secret and paste it into the **Signing Secret** field in Loops.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-secret.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=3bfcb09969cb7717a3b3190baacba8bc" alt="Reveal Clerk secret" data-og-width="2280" width="2280" data-og-height="1076" height="1076" data-path="images/clerk-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-secret.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=229ec8daf9c2184a3a8a5b6f90198517 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-secret.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=8f6b1fbb8b6fe37abb6f2f0c40920a4f 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-secret.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=81c1cb1f573bd7f021fc48873dd505cf 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-secret.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e81396c537449f8846f774b62b4831a6 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-secret.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6010b8de9653689d602d809f3eb2adca 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clerk-secret.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6bd7a20395dbec282dfd15136186b34a 2500w" />

Now you're all set up.

## Testing Clerk webhooks

Clerk offers a nice way to test webhooks. Click through to the webhook you created and then the **Testing** tab.

Select `user.created` or `user.updated` from the **Send event** dropdown, tweak the example data that's shown, then click **Send Example**.

This will send real data to your Loops account.

You can also test your webhook by creating and editing users in the **Users** page in Clerk, or by signing up in your application.

You can see all sent webhooks by going to **Webhooks**, clicking on the webhook and scrolling down to the **Message Attempts** section.

On Loops' end, you will see new contacts appear in your [Audience](https://app.loops.so/audience) page, and triggered events in the [Events](https://app.loops.so/settings?page=events) page.

## Examples

Here are some examples of how you can send data from Clerk to Loops to sync contacts and trigger useful emails to your customers.

### Syncing users to Loops

Create or update contacts in your Loops audience when a user is created or updated in Clerk.

1. Create a new Clerk webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
2. In Clerk, create a new webhook ([instructions above](#create-a-webhook-in-clerk)) for the `user.created` and `user.updated` events and paste in your endpoint's URL.
3. In Loops, make sure `user.created` and `user.updated` are toggled on on the Clerk settings page.

### Syncing waitlist signups to Loops

Create or update contacts in your Loops audience when someone joins your waitlist in Clerk.

1. Create a new Clerk webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
2. In Clerk, create a new webhook ([instructions above](#create-a-webhook-in-clerk)) for the `waitlistEntry.created` event and paste in your endpoint's URL.
3. In Loops, make sure `waitlistEntry.created` is toggled on on the Clerk settings page.
4. To keep track of waitlist users you can use the **Assign a user group** option. Enter something like "Waitlist" into field.

### Send an email to all new Clerk users

Send an email from Loops when a new user is created in Clerk.

1. Create a new loop in Loops using our **Onboarding drip** template.
2. For the loop trigger, select **Event received** and enter `newClerkUser` (or something similar).
3. Set up your Clerk webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
4. In Clerk, create a new webhook ([instructions above](#create-a-webhook-in-clerk)) for the `user.created` event and paste in your endpoint's URL.
5. In Loops, make sure `user.created` is toggled on, and select the event name you chose in Step 2 from the **Trigger an event** field.

### Enter all new Clerk users into an onboarding email sequence

Send an email from Loops when a new customer is created in Clerk.

1. Complete Steps 1–5 from "Send an email to all new Clerk users" above.
2. Add more emails and timers into the loop to complete your email sequence.

### Send an email to a deleted Clerk user

Send an email from Loops when a user is deleted in Clerk.

1. Create a new loop in Loops.
2. For the loop trigger, select **Event received** and enter `deletedClerkUser` (or something similar).
3. Set up your Clerk webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
4. In Clerk, create a new webhook ([instructions above](#create-a-webhook-in-clerk)) for the `user.deleted` event and paste in your endpoint's URL.
5. In Loops, make sure `user.deleted` is toggled on, and select the event name you chose in Step 2 from the **Trigger an event** field.
6. You can optionally delete or unsubscribe the user from your audience from the same settings. Note that both options will stop that contact from receiving future emails from Loops.
