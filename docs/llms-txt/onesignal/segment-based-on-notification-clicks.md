# Source: https://documentation.onesignal.com/docs/en/segment-based-on-notification-clicks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tag users with notification data

> Track and segment users based on notification clicks and topics using OneSignal Data Tags.

If you're a publisher with topic-based content or an eCommerce site tracking product interest, you can segment your users based on the *custom data* in notifications they interact with.

With OneSignal, you can do this using [Data Tags](./add-user-data-tags). By tagging users when they click a notification—based on metadata you define in the notification payload—you can create rich, behavior-driven segments.

***

## 1. Add the Code

Use OneSignal SDK's [notification event handlers](./mobile-sdk-reference) to detect when a notification is opened. In that handler, extract your custom data from the payload and use `addTag` or `addTags` to store it.

In this example, we tag the user with a `"notification_topic"` from the custom data. You can add any other fields you want—like category, product type, or campaign.

<CodeGroup>
  ````java Java theme={null}
  OneSignal.setNotificationOpenedHandler(
    new OneSignal.OSNotificationOpenedHandler() {
      @Override
      public void notificationOpened(OSNotificationOpenedResult result) {
        JSONObject data = result.getNotification().getAdditionalData();
        Log.i("OneSignalExample", "Notification Data: " + data);

        if (data != null) {
          String topic = data.optString("notification_topic", null);
          if (topic != null)
            OneSignal.User.addTag("notification_topic", topic);

          // Add more tags from custom data if needed
          String category = data.optString("category", null);
          if (category != null)
            OneSignal.User.addTag("notification_category", category);
        }
      }
    }
  );

  ```swift Swift
  let notificationOpenedBlock: OSHandleNotificationActionBlock = { result in
  let payload: OSNotificationPayload? = result?.notification.payload
  let additionalData = payload?.additionalData

  if let topic = additionalData?["notification_topic"] as? String {
    OneSignal.User.addTags(["notification_topic": topic])
  }

  if let category = additionalData?["category"] as? String {
    OneSignal.User.addTags(["notification_category": category])
  }

  // Add more tags from custom data if needed
  }
  ````

</CodeGroup>

## 2. Add custom data to your notifications

When creating a notification you simply add some [Additional Data](./push#additional-data) to the notification using our Dashboard or [API `data` parameter](/reference/push-notification).

This will be the topic of the notification and what you use to segment users. Common topics would be "news", "entertainment", "politics", "finance", "tech", etc.

<Frame caption="Adding notification topic data in dashboard">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/46305ec-Screen_Shot_2020-10-28_at_2.46.34_PM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=2829a694e36d6c607091346e8e899a86" width="623" height="209" data-path="images/docs/46305ec-Screen_Shot_2020-10-28_at_2.46.34_PM.png" />
</Frame>

## 3. Segment based on the tags

You can now [create segments](./segmentation) based on the custom data values users clicked on.

**Example**: Users who clicked a finance topic

* Key: `notification_topic`
* Condition: `equals`
* Value: `finance`

<Frame caption="Segmenting users based on topic clicked">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7197341-Screen_Shot_2020-10-28_at_3.02.23_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=254c091a979fb43c57501e4f51260bae" width="804" height="466" data-path="images/docs/7197341-Screen_Shot_2020-10-28_at_3.02.23_PM.png" />
</Frame>

## 4. Send notifications with the custom data

Now, whenever users click the notification, they will get automatically tagged with:

1. the date (unix timestamp) they clicked the notification
2. the notification's topic and how many total times that topic has been clicked

You can now [segment subscribers](./segmentation) based on this data.

***

Built with [Mintlify](https://mintlify.com).
