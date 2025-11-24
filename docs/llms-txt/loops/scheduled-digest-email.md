# Source: https://loops.so/docs/guides/scheduled-digest-email.md

# How to create a scheduled email with Loops

> How to send a daily, weekly or monthly email with a summary of what's happened in your app.

This email type may also be referred to as a "rollup" email or a "summary" email. The idea is to send a single email that summarizes what's happened in your app over a period of time.

These kinds of digest emails are a great way to keep your users engaged with your app.

The best way to do it today is a Loop with an [event trigger](/loop-builder/loop-triggers) set to fire “every time” with an event payload containing the updated property you’d like to send.

Then at the end of the day, week or month you can trigger a digest email with a summary of the events that happened.

## Create the loop and event

Go to the [Loops](https://app.loops.so/loops) page and create a new loop.

Choose the **Event is fired** trigger. You will enter the loop editor.

Click on the **Event received** node and type the name of your event. You can re-use an existing event or create a new one from this input.

For example, you can use a name like `sendDigest` and then click **+ Create new event**.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-trigger.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=0ed8f39465deb0ef2786cafaec05edd2" alt="Creating a trigger node" data-og-width="2280" width="2280" data-og-height="1893" height="1893" data-path="images/scheduled-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-trigger.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=1bdeced8e856aded10138075e1bb7355 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-trigger.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=17293e59e001dd643be3feb04f2ed7c6 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-trigger.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=aaca904d3ab8bd57bc6d915bd1b204d1 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-trigger.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=0a7609e747d6e103d120a9604339371e 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-trigger.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ecf7d444858270434be78cfb0c393089 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-trigger.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ce9f54298b6e572ef2b33f082f08901a 2500w" />

Next, click on the **Edit event properties** button to add [properties](/events/properties) to your event. Properties are extra pieces of data that you can attach to each event. This data is then made available in every email you send.

In the event editor overlay, click **+ Add event property** and add any properties you want to include in your digest email.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-event-properties.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ae2556a066c606f85579976b068f0d41" alt="Adding event properties" data-og-width="2280" width="2280" data-og-height="1652" height="1652" data-path="images/scheduled-event-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-event-properties.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=a7cbf6430bda3ae08d3f949099647ec4 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-event-properties.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=1b72dc2eb427fda2cc2b53fd630eb18a 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-event-properties.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=217892e1413daece337c47940b2b5e51 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-event-properties.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=3d53b6c33d397b1570787c1d59ff69bc 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-event-properties.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=4b8a8502ab2336b6b016f02ef60b4ade 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/scheduled-event-properties.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=dce6f2d12a2c650eadc062efcd59640a 2500w" />

Make sure the "Trigger frequency" dropdown in the **Event received** node has **One time** selected, as we only want to email each user once per event.

## Create your email

The next step is to create the email you send to each contact.

Click on the **Send email** node and then **Create email**. This will open the email editor, where you can [create your email](/creating-emails/editor).

When you want to add the event properties you created in the previous step, click the `⚡️` button above the editor (1) and then configure in the **Event Property** editor panel (2).

<img src="https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=fb1eb41c4043168c67219248413abf68" alt="Adding event properties in the editor" data-og-width="2280" width="2280" data-og-height="1596" height="1596" data-path="images/scheduled-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=280&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=1ef06da3b015974424b33b606fcbea9e 280w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=560&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=09f2cd64215e8a41434f9eb793ef2763 560w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=840&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=5383aa9d6e0f65363495d715799e3203 840w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=1100&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=b90362052ff0d7b02bbdf69483e8aa1a 1100w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=1650&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=8f8e5fd8e214b51792467e6fd3ab6c73 1650w, https://mintcdn.com/loops/Ghb_kmuDWgpv_ZFW/images/scheduled-editor.png?w=2500&fit=max&auto=format&n=Ghb_kmuDWgpv_ZFW&q=85&s=13502dc0a70bf1a57382741b897e1ede 2500w" />

In the right-hand panel, you will see a list allowing you to insert available event properties [into your email](/creating-emails/personalizing-emails).

Make sure to [add fallback values](/creating-emails/personalizing-emails#fallback-values) for every property; if an event doesn't have a value for a property in your email, the email will not send. Fallback values make sure that emails are sent to every contact.

When you've finished creating your email, click **Start** in the top right. This will make your loop active and you can start triggering it by sending events.

## Trigger events

To send events to Loops you can use an [integration](/integrations), an [SDK](/sdks) or [our API](/api-reference).

With the API, it's just a case of making a request to the [Send event endpoint](/api-reference/send-event) containing the contact's details, the event name and your event properties.

```json  theme={"dark"}
{
  "eventName": "sendDigest",
  "email": "user1@gmail.com",
  "eventProperties": {
    ...
  }
}
```

## Learn more

<CardGroup columns="2">
  <Card title="Loop Builder" icon="arrows-rotate" href="/loop-builder">
    Learn about creating email sequences in our loop builder.
  </Card>

  <Card title="Loop Triggers" icon="circle-play" href="/loop-builder/loop-triggers">
    Read more about triggering emails with events.
  </Card>

  <Card title="Personalizing emails" icon="crystal-ball" href="/creating-emails/personalizing-emails">
    Learn how to add dynamic data to your emails.
  </Card>

  <Card title="API Reference" icon="rectangle-terminal" href="/api-reference">
    Find out how to send events using our API.
  </Card>
</CardGroup>
