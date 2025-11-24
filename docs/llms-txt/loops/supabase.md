# Source: https://loops.so/docs/smtp/supabase.md

# Source: https://loops.so/docs/integrations/supabase.md

# Supabase

> Sync contacts and send emails triggered by events in Supabase.

<Info>
  If you are looking to send Supabase authentication emails with Loops, check out our [Supabase SMTP docs](/smtp/supabase).
</Info>

<Info>
  Our Supabase integration lets you:

  * Create and update contacts
  * Send events to trigger loops
</Info>

Our Supabase integration is built on top of our [Incoming webhooks](/integrations/incoming-webhooks) feature. This system lets you send webhooks from supported platforms directly to Loops so you can easily sync users and customers as well as send automated emails.

[Please read our guide about incoming webhooks](/integrations/incoming-webhooks)

With Supabase, you can keep your user data synced to Loops so you can send emails to your userbase.

## Supported events

We accept the following database events for the "Users" table:

* `INSERT`
* `UPDATE`
* `DELETE`

[Supabase database webhooks docs](https://supabase.com/docs/guides/database/webhooks)

Events from other tables will be ignored.

## Synced data

For `INSERT` and `UPDATE` events, we sync the following Supabase data to your Loops contacts:

* User ID
* Email address

We use the IDs of Supabase users to match contacts in your Loops audience. If the user ID is not found in Loops, we will create a new contact.

`DELETE` events can be used to delete or unsubscribe your Supabase users from your Loops audience.

## Create a webhook endpoint in Loops

[Follow the instructions here](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops) to create a new webhook endpoint, which will allow you to send webhook events directly to Loops.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-supabase.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d76efd48a5326debecce311b80dde7ce" alt="Endpoint form" data-og-width="2280" width="2280" data-og-height="1556" height="1556" data-path="images/create-endpoint-supabase.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-supabase.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=7a6a2cb668574fc8673a9a45792400d3 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-supabase.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=85a54d66e359123eff9d1d5ba26fa652 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-supabase.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6b9f0c5604e601cf026205707f9d8645 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-supabase.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=df571100daf2c9e497818c60926568fc 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-supabase.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=cb773940107dbcdf60df8ab2810ec337 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint-supabase.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5fd146b67b2c9de5353a203780ab7105 2500w" />

## Create a database hook in Supabase

Next, you need to set up database hooks in Supabase.

Inside a project in Supabase, go to [Integrations -> Database Webhooks -> Webhooks](https://supabase.com/dashboard/project/_/integrations/webhooks/webhooks) and click **Create a new hook**.

Give a name to your webhook, select "auth users" from the **Table** dropdown, and select the event(s) you want to get webhooks for.

Make sure **HTTP Request** is selected in the **Webhook configuration** section. In the **HTTP Request** section, paste in the endpoint URL from Loops into the **URL** field.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/supabase-webhook.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=802b4a0498a39577f692fe8fcfae0bb1" alt="Adding a webhook in Supabase" data-og-width="2280" width="2280" data-og-height="2658" height="2658" data-path="images/supabase-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/supabase-webhook.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=406b4a3eae3b36f47c86f5a9caad5797 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/supabase-webhook.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=547b61e97a54e3e0b81b5410c2c7edd0 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/supabase-webhook.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=4f838bf252b5ab877e7000b443ea1968 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/supabase-webhook.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=14aa37bd068d8bb52ceca9d0018f46d7 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/supabase-webhook.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=ca463579b6d55952f91c2d5012683e0a 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/supabase-webhook.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=37d82b64b12862a0b30362136dc2fa09 2500w" />

The last step is to secure requests with a header. In the **HTTP Headers** section, click **+ Add a new header**. From the **Secret header** section in Loops, paste in the **Header name** ("Loops-Secret") and **Header value** values into the form.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/supabase-header.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=08a4154f400e6cc28c8dd570d2bed97b" alt="Add header in Supabase" data-og-width="2280" width="2280" data-og-height="1326" height="1326" data-path="images/supabase-header.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/supabase-header.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=21cf2ed556315ad0de67c874209e9727 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/supabase-header.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=6150696d816a1d21697ab3d4ed461c27 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/supabase-header.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ea09ae93bb0c976f6ea89200d3e37688 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/supabase-header.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=0f0ac6266dc72982f93a7cb754324a55 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/supabase-header.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ed0e4ee56773eff5245a3e308a469850 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/supabase-header.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c0074404ef1679261bd319c446131a08 2500w" />

Click **Create webhook** to finish.

## Testing Supabase webhooks

You can test a user webhooks by creating, editing and deleting users from the [Authentication -> Users](https://supabase.com/dashboard/project/_/auth/users) page in Supabase, or by signing up in your application.

On Loops' end, you will see new contacts appear in your [Audience](https://app.loops.so/audience) page, and triggered events in the [Events](https://app.loops.so/settings?page=events) page.
