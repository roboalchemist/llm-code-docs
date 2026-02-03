# Source: https://loops.so/docs/integrations/bubble.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bubble

> Integrate the Loops API into your Bubble app with our plugin.

<Info>
  Our Bubble plugin lets you:

  * Add, find, update and delete contacts
  * Send events to trigger loops
  * Send transactional email
</Info>

<Tip>
  Our Bubble plugin is unfortunately limited to what it can do because of how
  Bubble works. If you want more flexibility—for example, syncing more contact
  data to Loops—check out our [tutorial for using Bubble's API
  Connector](/guides/bubble-api-connector).
</Tip>

## Install the plugin

Go to the [Loops plugin](https://bubble.io/plugin/loops-1704117562175x705056703666192400) and select your app from the "Install in an application..." dropdown.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-install.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=483997518a64ef37bd317a40e68c40e7" alt="" data-og-width="2280" width="2280" data-og-height="1271" height="1271" data-path="images/bubble-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-install.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=541e07b9f58d506cc0e2a9d594ee0c17 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-install.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=50d82f7b3815f17c76597480be513483 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-install.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=540afd85bda06426aa7ed72fc4db76ca 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-install.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d2d8bce009ca63c81f93f7f1e219226e 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-install.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e1dca1511c625d09a231142122f1a2ce 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-install.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=22cee607a031a6d2d3428d8da2f27d36 2500w" />

Alternatively, go to the Plugins page in your Bubble admin, click "Add plugins" in the top right, and search for "Loops".

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=50e241751474a0af4a1043b593ea2908" alt="" data-og-width="2280" width="2280" data-og-height="1191" height="1191" data-path="images/bubble-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=26d6eabd730e075249e9f45c1e0aec95 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e94c5ddccbefc62935f9d2013fd24917 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=949237141268769bd901b19ed95dcc4a 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1dbf49a8af7bf66e250dc0f1ea4a0dc9 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=fa2e88eef96b96a1f55e3dacf4799bff 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1524ba7ef557098a039a857fcc6ce0dc 2500w" />

## Set up the plugin

To use the plugin you will need to add a Loops API key into Bubble.

First, go to your [Loops API settings page](https://app.loops.so/settings?page=api) and copy an API key. You may need to create a key first.

Then go to the the Plugins page in Bubble, select the Loops plugin and paste your API key into the "API key" field, prepended with the word "Bearer" and a space.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-api-key.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e9e128029e352898bd5b8a247db9fe9d" alt="" data-og-width="2280" width="2280" data-og-height="1229" height="1229" data-path="images/bubble-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-api-key.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=2487cfed8e7c6a506646372bce665d51 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-api-key.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=6d22022a7c8067b28540ea0d68baacaf 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-api-key.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=6e74b88f6245a0503144c764359381bd 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-api-key.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=117cdcb07686114d95a83aee80ff14c1 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-api-key.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=4b9d6756d73ea897cc197331e6d0d297 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-api-key.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=447718f409ba410abefb97be34165a35 2500w" />

## Using the plugin actions

To use the plugin actions in a workflow, select "Plugins" in the menu and you will see the options show up (prefaced with "Loops - ").

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-action.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=58ebbff82c1eb4c24039222709a842c8" alt="" data-og-width="2280" width="2280" data-og-height="1889" height="1889" data-path="images/bubble-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-action.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ae0d00d8c76ca940d61d420dbdf6e274 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-action.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=8dc29447318fd1f728f4dda5c5b2ba1b 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-action.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f10232d427436b9f5cbee4df65979372 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-action.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=10b33ff3aeb5bb7a70687d9c8d73d8bc 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-action.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=bee4c75745f8046f5f6080986786ab44 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-action.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=fcc4c79a0c0346c0d6cf3bea7c059438 2500w" />

Here's a simple example of using the Bubble plugin to add all new users to your Loops audience.

After your sign up action, add a new "Loops - Create a contact" action.

In the form, add your user email into the "Email" field and user ID into the "User ID" field.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5672216926ae06edd874fa375dd7a9d0" alt="" data-og-width="2280" width="2280" data-og-height="1529" height="1529" data-path="images/bubble-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=4a471bbd0b476b9596d931b858832b3e 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=09239df293d8386bcec8b26ff15f9c36 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=a84b13e3cc0154cb8abf049953bc70c4 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=57f23466474a19c1e123b8bea69fe3c2 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=41d576916d18570317f59e0c271179a0 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7de2a22fc10b7f2a5fa1ecebfe712651 2500w" />

And that's it!

## Actions

The plugin contains actions that replicate what's possible with the [Loops API](/api-reference).

### Create a contact

The **Create a contact** action will create new contacts in Loops using the email address and user ID that you send from Bubble.

If you want to "create or update" users, use the [Update a contact](#update-a-contact) action instead.

You need to provide both email and user ID values, otherwise the underlying API request from Bubble will fail.

The **Create a contact with name** action lets you also send a first and last name to Loops.

[API documentation](/api-reference/create-contact)

### Find a contact

The **Find contact by email** action will find a Loops contact based on the provided email address. This can be used to see if one of your user already exists in your Loops audience.

Similarly the **Find contact by user ID** action will find a contact by their ID.

[API documentation](/api-reference/find-contact)

### Update a contact

This action will update the email address of a Loops contact who has the provided user ID.

This action can also be used to "update or create" contacts. If a contact doesn't already exist with the provided email or user ID, a contact will be created.

The **Update a contact with name** action lets you also send a first and last name to Loops.

[API documentation](/api-reference/update-contact)

### Delete a contact

The actions **Delete a contact by email** and **Delete a contact bu user ID** will delete a contact from Loops.

This is useful for when a user closes their account in your application and therefore you no longer want to email them from Loops.

[API documentation](/api-reference/delete-contact)

### Send an event

The send event actions can be used to [trigger Loops](/loop-builder) from your application. For example, you may have a welcome loop which sends an email drip campaign to new users.

For the Send an event action, you need to provide an "Event name" value and the user's ID or email address.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5672216926ae06edd874fa375dd7a9d0" alt="" data-og-width="2280" width="2280" data-og-height="1529" height="1529" data-path="images/bubble-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=4a471bbd0b476b9596d931b858832b3e 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=09239df293d8386bcec8b26ff15f9c36 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=a84b13e3cc0154cb8abf049953bc70c4 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=57f23466474a19c1e123b8bea69fe3c2 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=41d576916d18570317f59e0c271179a0 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-form.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7de2a22fc10b7f2a5fa1ecebfe712651 2500w" />

[API documentation](/api-reference/send-event)

### Send transactional email

Transactional emails are one-time emails like password resets sent by apps to users based on an action.

To send transactional emails, you will first need to [create the email in Loops](/transactional#compose-your-email).

Once you have written the email and added data variables, you can click **Next** to see the example payload for the API.

Note the names of the `dataVariables` (which you added in the email) because you need these in Bubble.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-transactional.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=2bff907ec71e15b99f248a27a60f665f" alt="" data-og-width="2280" width="2280" data-og-height="1325" height="1325" data-path="images/bubble-transactional.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-transactional.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b8b1e76939da58e6c0da4962dc5356dd 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-transactional.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=95a5dc39a4357477ef7b5291bf96ae9e 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-transactional.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=532e5267bb9205b21c41ba99311ce89c 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-transactional.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=256b2dc2154d164698e92222efdfbddb 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-transactional.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=bb3a3db85abb4cd015b83b58924649c8 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-transactional.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=47f63004c2aa5a33abe552ff517af635 2500w" />

Once you create the action in Bubble, you will see the three fields in the form.

Here is an example API payload for the Loops API:

```json  theme={"dark"}
{
  "transactionalId": "clomzp89u635xl30px7wrl0ri",
  "email": "name@email.com",
  "dataVariables": {
    "lastLoggedIn": "20240214T10:01:29Z",
    "plan": "Pro"
  }
}
```

To get the same effect in Bubble, we need to enter the following into the "Data variables" field:

`"lastLoggedIn": "20240214T10:01:29Z", "plan": "Pro"`

To add user data into this field, place your cursor and select **Insert dynamic data** (see image above).

[API documentation](/api-reference/send-transactional-email)
