# Source: https://loops.so/docs/integrations/rudderstack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# RudderStack

> Connect Loops to hundreds of apps to manage contacts and send emails.

<Info>
  Our RudderStack integration lets you:

  * Create and update contacts
  * Send events to trigger loops
</Info>

## Configuring the destination

In RudderStack, go to [Destinations](https://app.rudderstack.com/destinations) and click **New destination**. Search for "Loops" and select it.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-add.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2ca6bcb528520950b2a699349899c1d3" alt="Adding Loops in RudderStack" data-og-width="2280" width="2280" data-og-height="1520" height="1520" data-path="images/rudderstack-add.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-add.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ebc09686293424447a348e419158b6ce 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-add.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=8f95e3e1556eebd4b320323f9d9bbcac 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-add.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=8ca77b65f024b7a334de5d8215e69abb 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-add.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=694a47d2699f266a66aa3405e42b8ebc 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-add.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e0d02bbafebbd1c22b7b8afbb5c4c964 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-add.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e3b0386c5bce87243d479382ff106315 2500w" />

Select the source you want to connect Loops to.

On the next page you need to add a Loops API key. You can generate a new one on the [Loops API Settings page](https://app.loops.so/settings?page=api) and paste it into the **API Key** field.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-configure.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ceb627402bd0b4c93a7a93c34f319ab1" alt="Configuring the destination" data-og-width="2280" width="2280" data-og-height="1520" height="1520" data-path="images/rudderstack-configure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-configure.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=3201dc6e503a1c79710a086b56d6ca1d 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-configure.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c89541ad20f55b7109d549cdce9d8db2 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-configure.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=79df9de74771d5b4232d8838c5e70c02 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-configure.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=d20c3934b92552aa4b5b66ee6589db3c 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-configure.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=660d8e32e3a75a58497e9191254a76a1 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-configure.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=232da4bd4480fd24358740ee510db11b 2500w" />

Click **Continue** at the bottom of the page to finish the setup.

## Create or update a contact

To send contact data to Loops, use RudderStack's [`identify` call](https://www.rudderstack.com/docs/event-spec/standard-events/identify/).

Identify users with a unique user ID from your source. You can include contact properties in the traits object, like `firstName` and `lastName` in this example.

<Warning>
  For new contacts, make sure to include an email address, otherwise the call will fail. If the contact has already been sent to Loops with its user ID, you can omit the email address unless you want to update that value. In general, we recommend to always include an email address.
</Warning>

```javascript  theme={"dark"}
rudderanalytics.identify(userId, {
  email: "test@test.com",
  firstName: "Adrian",
  lastName: "Brown"
});
```

To manage [mailing list](/contacts/mailing-lists) subscriptions, add a `mailingLists` object to the traits object. The key is the ID of the mailing list and the value is a boolean indicating whether the contact should be subscribed or unsubscribed.

```javascript  theme={"dark"}
rudderanalytics.identify(userId, {
  email: "test@test.com",
  firstName: "Adrian",
  lastName: "Brown",
  mailingLists: {
    cly2xnjqn002z0mmn68uog1wk: true,
  },
});
```

## Send an event

You can trigger emails from RudderStack by triggering [events](/events) via [`track` calls](https://www.rudderstack.com/docs/event-spec/standard-events/track/).

You should add and define your events in [Settings -> Events](https://app.loops.so/settings?page=events) including any expected [event properties](/events/properties).

The event name in your `track` call must match the name of the event in Loops. Data sent in the properties object will be sent as event properties to Loops, for use in your emails.

<Warning>
  Make sure to call `identify` before `track` so the event is associated with a specific contact.
</Warning>

```javascript  theme={"dark"}
rudderanalytics.track("newUser", {
  plan: "Pro Annual",
  accountType: "Facebook"
});
```

## Testing

### In RudderStack

RudderStack includes features to help you test your integration.

First of all you can see all `identify` and `track` calls coming in from your sources. Click on a source and select the **Events tab**.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/rudderstack-source.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=d40af9f050e9ee6e98bde724bcaa80e6" alt="Source events chart" data-og-width="2280" width="2280" data-og-height="2547" height="2547" data-path="images/rudderstack-source.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/rudderstack-source.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=1ce68f978fd5219e57e3524dc1d36422 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/rudderstack-source.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=1c5427fab777413d6992401b6ec1fcb6 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/rudderstack-source.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=3c9cf92e88047d9f5df18b350de35804 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/rudderstack-source.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=3eb4bda719fcc2eac7d10f7d3d9ba4ec 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/rudderstack-source.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=0a06a81e1ce4086ea4ea4128b0f5bcdb 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/rudderstack-source.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=9c16f94f72b976c42230ac9163b7c127 2500w" />

Click on the **Live events** button in the top right to view details of events as they come in.

You can also see all of the calls being sent from RudderStack to your destinations. Click on a destination and then the **Events** tab. At the bottom of this page you will see a table showing events. Click on these to see any errors that have occurred when sending data to Loops.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-destination.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=db7e43f2bdf0c2920517e5df3644ecb8" alt="Destination events" data-og-width="2280" width="2280" data-og-height="2154" height="2154" data-path="images/rudderstack-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-destination.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=a705052b9455ad25287b2796bb44cfca 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-destination.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=feec44baee3a17dd15ccfb417eb41042 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-destination.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=50d3f54d80897b63d77ddd8189888176 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-destination.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=8125fc10614b1fbdd3662c75226a4971 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-destination.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=0540c644f80078c8a0ffa6f8096c8b90 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/rudderstack-destination.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=53262e8fd712e91b221fd978e3fa26be 2500w" />

### In Loops

You can verify contact updates have happened in Loops from the [Audience page](https://app.loops.so/audience), and you can see all incoming events from the [Events page](https://app.loops.so/settings?page=events).

Click on individual events in the **Event Log** table to view the payload that Loops processed.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/events-page.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=61b360ae384ca9fcffdbe2bc193d509a" alt="Events page" data-og-width="2280" width="2280" data-og-height="1520" height="1520" data-path="images/events-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/events-page.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=862d8aa9d6f61ad95962c3e5c7f6a08a 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/events-page.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=f778c1771683ce6fe72dfc6628e835aa 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/events-page.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=26c3a7ecb8f6374640d498b3389508eb 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/events-page.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=167f6583dc35f52bfdca267dde756a12 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/events-page.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=902a7c9255941900394cdc60ad2019c3 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/events-page.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=19de67f0a14dbf8d9e12c1de7fcf29ee 2500w" />
