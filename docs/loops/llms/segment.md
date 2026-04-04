# Source: https://loops.so/docs/integrations/segment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment

> Utilize our official Segment integration to manage contacts and send email.

<Info>
  Our Segment integration lets you:

  * Create and update contacts
  * Send events to trigger loops
</Info>

Visit our [Segment integration](https://segment.com/catalog/integrations/actions-loops/) to learn more and follow the steps below.

## Configuring the destination

After opening the link above, click **Configure Loops (Actions)**.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-loops.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=5e5f327e220492cc8291ec29cdd5b32e" alt="Adding Loops in Segment" data-og-width="2280" width="2280" data-og-height="1125" height="1125" data-path="images/segment-configure-loops.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-loops.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=00f46841325b8c4964bc02f05b88ee8c 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-loops.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=10e0cad92a1bddccd4ba6eb4afc24ac9 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-loops.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=5673468baad8bba40ca92212368167d4 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-loops.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f361c822fb36b8b1acda60a77bf92916 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-loops.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=13bff59eec45fb7a602ff4ecd8d5bf6e 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-loops.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=05c702d7be6fb2047c8493efcbb25346 2500w" />

Select your data source, give the destination a name, and click **Create destination**.

Next, you’ll need an API key. You can generate a new one for Segment on the [Loops API Settings page](https://app.loops.so/settings?page=api).

Enter the API key on your Segment destination settings:

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-api-key.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=60e2cf5103c1d17da42db3cf97827d4f" alt="Add an API key" data-og-width="2280" width="2280" data-og-height="1647" height="1647" data-path="images/segment-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-api-key.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=18a391ff2737057c5675a748f963ad9e 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-api-key.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c20b5d117ad2fe1a8ddf2eca322e6c98 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-api-key.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=afb471c9ab6314092df80aa5854af609 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-api-key.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=b94342acddf3f7b42bf74c22ec6752ca 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-api-key.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=70967bc3287ceeb442e11c9caad93bc6 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-api-key.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=4afd84d7398bede1f6be7b3283c593f5 2500w" />

Enable the destination and click **Save Changes**. Note that no data will start flowing until you create specific mappings for Loops.

## Mappings

Segment action destinations require that you map specific fields from your source to your destination (in this case Loops). You can set this up by clicking into the **Mappings** tab and adding a new mapping. Currently we support updating contacts in Loops and sending events into Loops.

### Create or update contact

First, select which events to map. Typically for contact creation and updates, the most useful event to map will be "Identify".

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-select-events.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=62e7f1763ee87d83d5f3df9fb503b357" alt="Map contact properties" data-og-width="2280" width="2280" data-og-height="947" height="947" data-path="images/segment-select-events.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-select-events.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=8099e92d7a3a6be0eddbb74f5d3a66ae 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-select-events.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=6c12e0022338bd4ce26ae2812bb4f832 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-select-events.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=5b13fb1ac2c06f1108181429bdffe147 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-select-events.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=1a550744bb798c75d8ffdbe674e6be93 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-select-events.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c483930d856b1063b3c5eb8bcca6f41b 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-select-events.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=e4281d081884efb1dee5599ab0ab8dbe 2500w" />

The next step is to load a sample event to help you map fields appropriately.

Contact properties are found in the `traits` object.

For this example, we’ll be using this test event:

```json  theme={"dark"}
{
  "messageId": "segment-test-message-gt3ds8",
  "timestamp": "2023-05-24T17:58:30.352Z",
  "type": "identify",
  "email": "adam@loops.so",
  "traits": {
    "firstName": "Adam",
    "favoriteColor": "blue",
    "favoriteNumber": 42
  },
  "userId": "test-user-a5h7xb"
}
```

<Warning>
  When sending a contact's details to Loops, you must include an Email and a User ID.
</Warning>

We've provided some defaults for the mappings, which will show up in the third step, but it is important you review them:

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-default-mapping.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=deee73f5d70f77a3de8596f9120285e8" alt="Default contact mappings" data-og-width="2280" width="2280" data-og-height="2436" height="2436" data-path="images/segment-default-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-default-mapping.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f654fdbf78b0a5907e53b4c530b3f242 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-default-mapping.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=3dec93e963c5f1f17c0438f533d592a2 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-default-mapping.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ab5a2fea99d579c101d14333805eded6 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-default-mapping.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=91d6d37daa06f513963a5c9cf624f138 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-default-mapping.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=a64e0c5bd2717f58b2079a4a8e54ecce 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-default-mapping.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=b9db81ba765cb844a3ba1edc8db63261 2500w" />

#### Custom contact properties

Segment does not provide an interface to provide the names and types for [custom contact properties](/contacts/properties#custom-contact-properties) that you might be using with Loops. In our example, those fields are `favoriteColor` and `favoriteNumber`.

You can pass contact properties as a dictionary in the **Custom Contact Attributes** field.

<Warning>
  Ensure that the keys and values you provide match the schema you’ve created in your [Contact properties settings](https://app.loops.so/settings?page=api).
</Warning>

Click **Edit Object** to specify the custom fields you want to send to Loops individually:

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-edit-defaults.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ef6b0be2f2a214f4699c26496563da1d" alt="Mapping custom contact properties" data-og-width="2280" width="2280" data-og-height="858" height="858" data-path="images/segment-edit-defaults.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-edit-defaults.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=bc793f8c6cbb75de1b6c0d6b0a348942 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-edit-defaults.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=3b86f9872b6ef0e4310f5e2e18dfa4e0 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-edit-defaults.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=9b6b4ee90c1e640b0659d082c78dfb7d 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-edit-defaults.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f2fe5e211309fb6dbec3beda174b8aba 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-edit-defaults.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ce09628a202c6f04a3824747f1306465 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-edit-defaults.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=366f98b3cf0541b2528928bbd8ed8bca 2500w" />

#### Subscribed

In most cases, you want to leave the **Subscribed** field as the default (deselected). Setting this to `true` will re-subscribe contacts who had previously unsubscribed, and setting it to `false` will unsubscribe contacts from receiving email. Leaving it deselected will default new users as subscribed to email and not update the email preference for existing contacts.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-subscribed-field.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=fbe6333a7ba93f350372adaf073d9ded" alt="Subscribed field" data-og-width="2280" width="2280" data-og-height="858" height="858" data-path="images/segment-subscribed-field.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-subscribed-field.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=eb6ee90f79c3436657cc724330a8fb72 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-subscribed-field.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f4c6bf60be472a172830e2a1b581765e 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-subscribed-field.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f7ad833c1684a2eb2f2a006f1976fb5d 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-subscribed-field.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=66be8a2b10cd65b482ac1311f3f963c0 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-subscribed-field.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=93113500240cdfc3c7ee038d4929d244 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-subscribed-field.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=e2d48b15d86e109c652398809fc9df29 2500w" />

#### Mailing lists

To subscribe contacts to [mailing lists](/contacts/mailing-lists) there are two options.

The first method is to manually edit the **Mailing Lists** data. This will allow you to enter list ID values that are the same for every contact.

Click the **Edit Object** option, then the **+ Add Mapping Field** button. In the **Select event variable** field enter "true" or "false" (to subscribe or unsubscribe) and in the **Enter key name** field enter your list ID(s).

You can add multiple lists by clicking on the **+ Add Mapping Field** button again. Make sure the data shown below the fields has the same structure as in the image below.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mapping-lists.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=13d71019be25d37f92a6dd6060f38025" alt="Adding list IDs in the mapping UI" data-og-width="2280" width="2280" data-og-height="978" height="978" data-path="images/segment-mapping-lists.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mapping-lists.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=00cfeb409efaccbc81c1239f1098ab7b 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mapping-lists.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=e0dad271977e674f96128848769abe2d 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mapping-lists.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ef7f22083a8c3f5f93dd30d91bf55bfc 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mapping-lists.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f16d405c07ffc730cb9326ba8c093c73 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mapping-lists.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=0ac4d8cf9ce308094d57867550c6f538 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mapping-lists.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=11588c459e7719e2cc3675faf8a52353 2500w" />

Another option is to add mailing list data to your Identify call, which will let you dd more dynamic data for each contact. You can test this by adding a `mailingLists` object to `traits` in your test event with list IDs as keys and `true` (to subscribe) or `false` (to unsubscribe) as values.

```json  theme={"dark"}
{
  "messageId": "segment-test-message-gt3ds8",
  "timestamp": "2023-05-24T17:58:30.352Z",
  "type": "identify",
  "email": "adam@loops.so",
  "traits": {
    "firstName": "Adam",
    "favoriteColor": "blue",
    "favoriteNumber": 42,
    "mailingLists": {
      "cm06f5v0e45nf0ml5754o9cix": true,
      "cm16k73gq014h0mmj5b6jdi9r": true,
    }
  },
  "userId": "test-user-a5h7xb"
}
```

Then you need to map the data. Click the **Select Object** option, then search for `traits.mailingLists` from the Event Variables options.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mailinglists-object.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=0bdad2f709ce49e3cedbfb4a2db4dde9" alt="Selecting the mailing list data from traits" data-og-width="2280" width="2280" data-og-height="1098" height="1098" data-path="images/segment-mailinglists-object.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mailinglists-object.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=bc4f4d1c296686e0a41240250f906784 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mailinglists-object.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c1825a5ed66e718247bd2d35034aeec1 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mailinglists-object.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=dc1323eab0a1c95547b8f027870f6227 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mailinglists-object.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=549a0707ef3ac3fa97eca853bc0c4666 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mailinglists-object.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=a188c4ddfb63d2709a43804419103be3 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-mailinglists-object.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=2e2243376ac4e6e18f403c9ebd5e5c2e 2500w" />

#### Testing

After the mappings are configured you can preview the data that will be sent.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-preview.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=235a79d1658e48758004f91a7ebd461f" alt="Event data preview" data-og-width="2280" width="2280" data-og-height="1653" height="1653" data-path="images/segment-test-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-preview.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=62b1972f6b669ae32a033e1ed9276db7 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-preview.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=30171b0d15e8e4ad5cf1318e215b9e56 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-preview.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=57fcf7777837a6b0f4499921ad150a71 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-preview.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=d2e0b1a56d3cab1845c2bf6bc37659f7 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-preview.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=0b67b28e16dab163755b644b2b53cf30 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-preview.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=b73d74e5f270590392a59022c83e87ed 2500w" />

You can also send a test event to Loops to verify everything is working (this will send actual data to your Loops account). If it works, you will get a successful response:

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-event.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=6497b1f7b5ecd4328992b4786ad977aa" alt="Successful response" data-og-width="2280" width="2280" data-og-height="1289" height="1289" data-path="images/segment-test-event.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-event.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c0c70abb1f6acf7359134028e8cdb613 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-event.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=407a6f9824b6ea6f3de539b393be4c05 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-event.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=66d301ef702d901c0257231165f4f220 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-event.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=6d60cfbc86c21b41f92d6e10bc16f2b2 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-event.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=08c307e0dde029e58780048d01260fb0 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-event.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=90cebc746a267a7534e67eeb7746811d 2500w" />

Check your [Loops audience page](https://app.loops.so/audience) to ensure the contact was created or updated as intended.

<Warning>
  Sending another test event with the same User ID or Email will update the existing contact instead of creating a new contact.
</Warning>

### Send event

You can send events to trigger [loops](/loop-builder).

First, select which event(s) to map. Typically for sending an event, the most useful event to map will be "Track".

We recommend that you filter the events down to only ones that you plan on using within Loops using the **Event Name** filter:

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-send-event.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=eb07702265a9c324bbe9f9537e4123e0" alt="Sent event in Segment" data-og-width="2280" width="2280" data-og-height="1002" height="1002" data-path="images/segment-send-event.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-send-event.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=bf24efb32607fdf76daab715a18b16a8 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-send-event.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ceb464ff7c5a9e749e5f98d65d55f00e 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-send-event.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=2942933231e131d7e34c0612959c6267 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-send-event.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=163ff5854086168f9266dbc8c3a38a3e 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-send-event.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=d67b16a4ba877f3fd5141919f823278f 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-send-event.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=8b2e039dbad9d16212fa055c1d423d94 2500w" />

Then after defining or loading a sample event in step 2, configure the mapping.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-mappings.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=e41dfcd28513825e37576838c31c6f84" alt="Sent event in Segment" data-og-width="2280" width="2280" data-og-height="1511" height="1511" data-path="images/segment-configure-mappings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-mappings.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=4e6141db050b5030c0b99ef99fa7d84c 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-mappings.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=cfb7cc71c3500283776f714eb93ba32e 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-mappings.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=d7e5ae6f2e519a3bf01090caab00b6ad 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-mappings.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=93dca6dfd73eeb445a94ab4260effec3 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-mappings.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=9ea2f3fc59e4d8f4dd588c26b1bcccd3 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-configure-mappings.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=a968ef68e60ace87e2a356fd95653f2e 2500w" />

#### Required fields

The **User ID** field is required. If a contact already exists in your Loops audience, the **Contact Email** field is optional; if the contact does not exist in Loops you need to include an email address so that a contact can be created and an email can be sent (we recommend always including an email address).

#### Event properties

If you want to add [event properties](/events/properties), you can pass them as a dictionary to the **Event Properties** field. These properties can be included in emails triggered by your event.

You can choose to select the `properties` object to send all data from the track call. Or if you click **Edit Object** you can select individual properties. Make sure to enter the correct contact property name from Loops in the **Enter key name** field.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-properties.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=6d55f7bd6e8b9dce0413525e5ea54ed8" alt="Configure event mappings" data-og-width="2280" width="2280" data-og-height="1142" height="1142" data-path="images/segment-event-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-properties.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=fd9e4d425ee5492b7fdc534c1660d091 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-properties.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=10582d54c9cb9616d80b61d2dd11fb59 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-properties.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c670670b0ef31ad3aadadc44cc22cedd 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-properties.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=5888d70dc8d8ba56d55dd55e4e1585fe 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-properties.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c26762bdc42aac96f6b0b80db15745c3 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-properties.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=8ef3cf83728ba93d9fe66e02a034f23a 2500w" />

#### Contact properties

You can update contacts at the same time as sending an event with the **Contact Properties** field.

Click **Edit Object** and specify the properties and values you want to update on your contacts.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-contact-properties.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=db06fb438c39251da7ab9c3845273e0f" alt="Mapping custom contact properties" data-og-width="2280" width="2280" data-og-height="1142" height="1142" data-path="images/segment-event-contact-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-contact-properties.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=7cc7bd972a5bc9e758cd9ad005cdaa8e 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-contact-properties.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=7d2d2743adb370fdd6cf42619058e239 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-contact-properties.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=e22083cdb659b4a8fd9649ff0f1e9f33 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-contact-properties.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=0dc6569640009e3902eee6bbb02c1cdd 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-contact-properties.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=30d0fff9a0ec7aa68c97d1d6c1797d17 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-contact-properties.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=2d0323c77d3012e9567659c985acf3ef 2500w" />

<Warning>
  Ensure that the keys and values you provide match the schema you’ve created in your [Contact properties settings](https://app.loops.so/settings?page=api), otherwise some data may not be captured by Loops.
</Warning>

You can choose to add a contact's email address in the **Contact Email** field or in the **Contact Properties** object.

#### Testing

After configuring the mapping, you can send a test event at the bottom of the page (this will send actual data to your Loops account). You can preview the data that will be sent.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-preview.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c0276874863e39d5b5bdd9055a8bf2f0" alt="Send event preview" data-og-width="2280" width="2280" data-og-height="1350" height="1350" data-path="images/segment-event-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-preview.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=a09b1615a3366e26e870f77efdd0305e 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-preview.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=61aa355acc2d9afca2eb28a8d5c60c72 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-preview.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=d58518ebe853871c7d1ce4ae0fa2c204 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-preview.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=7a254deeb0376123fae1d8c9e5149738 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-preview.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=36d39daed04ee187567c353c263223f5 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-event-preview.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=00262de2ed9db641620156129fb7f9bd 2500w" />

The response should indicate success:

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-mappings.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=2ad0e04c0c800d4db9c2ccb703c27066" alt="Success message" data-og-width="2280" width="2280" data-og-height="1215" height="1215" data-path="images/segment-test-mappings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-mappings.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=7c78740adcbc9a2a45a5fca0b346c577 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-mappings.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=cdb9c10f81f3fe1c3d4f502aa29722db 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-mappings.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c4370ab5a41915f4b867212f9108beca 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-mappings.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=9889063a67cfc68d3285a26067d9a6a8 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-mappings.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=7c05c2b72b22baa4f20e66ecbf73d510 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/segment-test-mappings.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=95508db44a80e70e28236ae9822b1222 2500w" />

You can verify the event was received on your [Events page](https://app.loops.so/settings?page=events) in Loops.

## Sending data to Segment

The following examples show how you can send data from your application to Segment for the two Loops actions.

The examples use Segment's [Analytics.js library](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/), but the premise is similar for other libraries.

### Create or update contact

For this action you should send a `identify()` event. Add contact properties (including any [custom properties](/contacts/properties#custom-contact-properties)) in the traits object:

```javascript  theme={"dark"}
analytics.identify("97980cfea0067", {
  email: "peter@example.com",
  plan: "premium",
  logins: 5
});
```

If you're mapping a `mailingLists` object from `traits` ([read more above](#mailing-lists)) add it like this:

```javascript  theme={"dark"}
analytics.identify("97980cfea0067", {
  email: "peter@example.com",
  plan: "premium",
  logins: 5,
  mailingLists: {
    "cm06f5v0e45nf0ml5754o9cix": true,
    "cm16k73gq014h0mmj5b6jdi9r": true,
  }
});
```

### Send event

For this action send a `track()` event. Data sent in the properties object will be sent as [event properties](/events/properties) to Loops. Make sure that you have added these event properties in your [Events Settings](https://app.loops.so/settings?page=events) in Loops before sending the event to Segment.

```javascript  theme={"dark"}
analytics.track("User Registered", {
  plan: "Pro Annual",
  accountType: "Facebook",
  firstName: "Phil"
});
```

You can update a contact's properties when sending events (for example, `firstName`) by mapping values in your properties within the **Contact Properties** object ([see above](#contact-properties)).
