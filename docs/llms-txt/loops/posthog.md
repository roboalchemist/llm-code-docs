# Source: https://loops.so/docs/integrations/posthog.md

# PostHog

> Send events and contacts data to Loops from PostHog.

PostHog's Loops integration lets you send events from your project to Loops, as well as add users to your Loops audience.

<Info>
  PostHog's [data pipelines](https://posthog.com/cdp) add-on or a self-hosted version of PostHog is required for this integration to work.
</Info>

Here's how to set up a Loops destination in PostHog.

## Create a Loops destinations

In your PostHog dashboard go to **Date pipelines**, click **+ New destination** and search for "Loops".

You will see two options:

* Send events to Loops.so (use this to trigger [loops](/loop-builder))
* Update contacts in Loops.so (this will *create or update* contacts in your Loops audience)

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-search.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2cf888fbc6283536ce181249800e028a" alt="Search for Loops in PostHog" data-og-width="2280" width="2280" data-og-height="1098" height="1098" data-path="images/posthog-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-search.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b9144fcf5ab7ca7f3f41c11db40030d5 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-search.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=80e88fecc5040e099f46071df52cfb74 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-search.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b321eb83feb397b80a8f3836faded6df 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-search.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2f89cb969df7eb0bdb77f1a0fe3280ef 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-search.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=78481cb8681aa470aabf5f0a7121e609 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-search.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=4f504e67b436be228355d393d7d29726 2500w" />

Choose the one you want and click **+ Create**.

## Add your API key

You need to add a Loops API to each destination so that PostHog can send data to your Loops account.

In Loops, go to [Settings -> API](https://app.loops.so/settings?page=api) and generate or copy an API key.

Back in PostHog, paste the API key in the **Loops API Key** field.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-api-key.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=9ec505733ccfb58dd01047f8a392f19b" alt="Add Loops API key" data-og-width="2280" width="2280" data-og-height="1050" height="1050" data-path="images/posthog-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-api-key.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=906436dfd084910d8bab5c2860eea25f 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-api-key.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=84d22843b235103ea66cf1ebf40da3d5 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-api-key.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=47fd4066468bb07722b3389001eb49f4 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-api-key.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f1fcb313621d74af0f5e0af9bb83dfee 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-api-key.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=cff6c922f08d9d9390083041f9b56e96 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-api-key.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c67b41d82cd63042904dc3099bf02cba 2500w" />

## Customize the destination

There are a few options available to customize the data that is sent to Loops for both destination types. This helps make sure that you're sending the correct data for your events and contacts.

### Send events

In the **Send event to Loops.so** destination, you can filter which events are sent to Loops from the **Filters** section. The default is "Pageview" (which is sent with the event name "\$pageview" to Loops).

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-event-destination.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=64c419abae18051750d93f01fb174547" alt="Send events destination" data-og-width="2280" width="2280" data-og-height="1875" height="1875" data-path="images/posthog-event-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-event-destination.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f7d1c761bad2227e9710765118ac0124 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-event-destination.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=a76e61b926ff9a27bea2fbd520743e2c 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-event-destination.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=82cf1613f135dd9a8c8e51d056e8766b 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-event-destination.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=081897557b46924fda194881c9fd1234 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-event-destination.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=28e25c42afb8c4af36a38c2c3f63e65f 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-event-destination.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=a2f2d2cd2f00676e00265d3032cb92b2 2500w" />

By default `pathname` is sent with the event as an [event property](/events/properties), making it available in all emails triggered by the event.

If you want to add more event properties you can use the **Property mapping** option.

If you check the **Include all properties as attributes** option, all properties from the event will be sent to Loops.

### Update contacts

The **Update contacts in Loops.so** destination lets you sync users to Loops. If a matching contact doesn't already exist in Loops, one will be created.

In this destination you can filter which events are sent to Loops from the **Filters** section. The defaults are "Identify" and "Set person properties".

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-contact-destination.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f33527bd8f9619387b111d8a73c66888" alt="Update contacts destination" data-og-width="2280" width="2280" data-og-height="1991" height="1991" data-path="images/posthog-contact-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-contact-destination.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=d9518f1ba86562e480e50c31e2de841e 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-contact-destination.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=355a41813612dcf09c65a0172b069a5c 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-contact-destination.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=8b1492bcd56c157d9167e9501fe9db22 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-contact-destination.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=561876ab390d94ee4a8d0a1dc0bd5865 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-contact-destination.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=9462830e71ecfb8a2b48585ea7f6b800 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-contact-destination.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b3a297ab13cb4fb579b3fdca0db7a355 2500w" />

By default `email`, `userId`, `firstName` and `lastName` are synced to Loops. To add more contact properties you can use the **Property mapping** option, which allows you to map specific person data to contact properties in Loops. You can see all available contact properties in your account from [Settings -> API](https://app.loops.so/settings?page=api). Make sure to use the "API name" when mapping values in PostHog.

If you check the **Include all properties as attributes** option, all properties from the person record in PostHog will be added to contacts in Loops. This may create a lot of custom contac properties in Loops, so we suggest running a mock test (see below) first to see which data would be sent.

### Mailing lists

To add contacts to your Loops [mailing lists](/contacts/mailing-lists), you need to make a quick code change to the destination.

Click **Edit source code** on your destination's page.

For the **updating contacts** destination, edit lines 6–9 and add a new `mailingLists` section. Here, add your mailing list ID(s) and `true` (to subscribe the contact) or `false` (to unsubscribe).

```javascript {4-6} theme={"dark"}
let payload := {
  'email': inputs.email,
  'userId': person.id,
  'mailingLists': {
    '<your_list_id>': true
  }
}
```

<CardGroup>
  <Card title="Update contacts" href="/api-reference/update-contact" icon="user-pen">
    Read the API documentation for updating contacts in Loops.
  </Card>
</CardGroup>

For the send events destination, edit lines 6–11 and add a new `mailingLists` section. Here, add your mailing list ID(s) and `true` (to subscribe the contact) or `false` (to unsubscribe).

```javascript {6-8} theme={"dark"}
let payload := {
  'email': inputs.email,
  'userId': person.id,
  'eventName': event.event,
  'eventProperties': {},
  'mailingLists': {
    '<your_list_id>': true
  }
}
```

<CardGroup>
  <Card title="Send events" href="/api-reference/send-event" icon="bolt">
    Read the API documentation for sending events to Loops.
  </Card>
</CardGroup>

## Testing

To test if your configuration is working as expected, expand the **Testing** section at the bottom of the page.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-testing.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c3bb8a50e1e155adb1acf206015ca1c6" alt="Testing the integration" data-og-width="2280" width="2280" data-og-height="1854" height="1854" data-path="images/posthog-testing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-testing.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=10909e3d49ec02135891458a8809641d 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-testing.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=31c08444aed2af10ad68fb37c1649d50 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-testing.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=d1f428bd2b84d9e30aeae45cd2479102 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-testing.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=3c2b4cefc74e399aa11f13b5686bc5ba 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-testing.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c3abf8564ed950fc2afde28710660661 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/posthog-testing.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=9c9b5ec889a153939f0f9ee91a895e87 2500w" />

You can send real test events to Loops by clicking **Test function**. Check [Settings -> Events](https://app.loops.so/settings?page=events) and your [Audience](https://app.loops.so/audience) pages in Loops to see if data is coming across as you expect.

If you'd rather not send actual data to Loops during testing, select the **Mock out HTTP requests** option. This will show the expected request data (including all contact and event properties) rather than send a request to Loops.
