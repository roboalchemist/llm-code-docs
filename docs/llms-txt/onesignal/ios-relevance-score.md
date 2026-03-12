# Source: https://documentation.onesignal.com/docs/en/ios-relevance-score.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS: Relevance score

> How you can set a relevance score

<Frame caption="Image showing selection of relevance score into Morning Summary">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b016c19-ios15-relevance-score--1.jpeg?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=847eafa58c2ed2736a448073fce1964f" width="1000" height="562" data-path="images/docs/b016c19-ios15-relevance-score--1.jpeg" />
</Frame>

Apple’s Relevance Score allows you to indicate the importance of each push notification or Live Activity update. This score helps iOS determine how prominently to display your notifications in the Notification Summary (for push) or Dynamic Island/Lock Screen (for Live Activities).

<Frame caption="Image. Showing user settings on an iPhone for their Daily Summary">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7bb9b21-image_7.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=3b3d0d266acc3d6c6b71bcf021573e8c" width="4000" height="2000" data-path="images/docs/7bb9b21-image_7.png" />
</Frame>

***

## Relevance Score for push notifications

The relevance score is a value from `0.0` to `1.0` that signals to the system the importance of a notification. Notifications with higher relevance scores are shown more prominently in the user’s Notification Summary, which you can configure for scheduled delivery times.

1. Make sure you followed our [Mobile SDK setup](./mobile-sdk-setup) docs for iOS that implement the Notification Service Extension. This extension allows you to customize payloads, including relevance score.

2. When creating a [Push](./push) message, under iOS options, specify the **Relevance Score** from 0.0 (least important) to 1.0 (most important).

<Warning>
  Reserve a score of `1.0` for the most critical messages. Overusing high scores will cause the system to ignore the distinction, making them all blend together in summary.
</Warning>

Example use cases:

* New Direct Messages set to `1.0`
* Promotional alerts set to `0.2`
* Daily reminders set to `0.6`

<Tabs>
  <Tab title="Dashboard">
    When creating a message from the dashboard, you can select the **Relevance Score** under the Apple iOS platform settings:

    <Frame caption="Example setting the Relevance Score via the OneSignal dashboard.">
      <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/496ae2be333a38d8d276b9edc2bb34e49131afc62585fa3ac5f37bd1778bc2d6-Screenshot_2025-04-24_at_5.39.58_PM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=e856c8437f0f103af71e692f08d0c3ad" width="1544" height="1592" data-path="images/docs/496ae2be333a38d8d276b9edc2bb34e49131afc62585fa3ac5f37bd1778bc2d6-Screenshot_2025-04-24_at_5.39.58_PM.png" />
    </Frame>
  </Tab>

  <Tab title="API">
    <ParamField path="ios_relevance_score" type="double">
      [ios\_relevance\_score](/reference/push-notification#body-ios-relevance-score) is a value between 0 and 1, to sort the notifications from your app. The highest score gets featured in the notification summary.
    </ParamField>

    ```bash Request theme={null}
    curl --request POST \
     --url 'https://api.onesignal.com/notifications?c=push' \
     --header 'Authorization: <authorization>' \
     --header 'Content-Type: application/json' \
     --data '{
         "app_id": "YOUR_APP_ID",
             "include_aliases": {
                 "external_id": ["EXTERNAL_ID"],
             },
             "contents": {
                 "en": "English Message"
             },
             "ios_relevance_score": 0.5
     }'
    ```
  </Tab>
</Tabs>

***

## Relevance Score for Live Activities

If your app starts multiple Live Activities, the one with the highest relevanceScore is prioritized for display in the Dynamic Island. If two or more Live Activities share the same score, the system will show the earliest-started activity. On the Lock Screen, the relevanceScore also determines the display order of your app's Live Activities.

When using our [Update Live Activity API](/reference/update-live-activity-api), set the `ios_relevance_score` to any *`double`* data type value between `0.0` and `1.0`.

***

Built with [Mintlify](https://mintlify.com).
