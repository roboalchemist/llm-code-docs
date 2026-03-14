# Source: https://documentation.onesignal.com/docs/en/custom-outcomes.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Outcomes

> Learn how to track user actions and revenue from push notifications and in-app messages using OneSignal Custom Outcomes. Customize attribution and measure engagement with flexible outcome types across platforms.

<Warning>
  **Custom Outcomes is being deprecated.** It is replaced by [Conversion metrics](./conversion-metrics), which provides cross-channel last-touch attribution across push, email, SMS, in-app, and RCS. If you are setting up conversion tracking for the first time, use [Conversion metrics](./conversion-metrics) instead.

  Existing Custom Outcomes data remains accessible as historical data.
</Warning>

OneSignal Custom Outcomes allow you to track meaningful user actions resulting from push notifications and in-app messages. These actions—such as purchases, signups, or app events—can be tracked with count, sum, and unique metrics, giving you insight into the impact of your messaging campaigns.

<Info> Custom Outcomes are available on the **Professional** and **Enterprise** plans. Learn more about our [pricing](https://onesignal.com/pricing). </Info>

***

## Outcome types & SDK methods

You can trigger an Outcome by adding a line of code when a user completes a specific action (e.g., taps "Add to Cart" or "Upgrade").

| Outcome Type       |                          Mobile SDK Method                          |                        Web SDK Method                        | Description                                                                                                                        |
| ------------------ | :-----------------------------------------------------------------: | :----------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Standard Count** |          [`addOutcome`](./mobile-sdk-reference#addoutcome)          |       [`sendOutcome`](./web-sdk-reference#sendoutcome)       | Increases the count by 1 every time it's called. No value tracking.                                                                |
| **Value (Sum)**    | [`addOutcomeWithValue`](./mobile-sdk-reference#addoutcomewithvalue) |       [`sendOutcome`](./web-sdk-reference#sendoutcome)       | Increases count by 1 and sum by the specified numeric value. Useful for revenue tracking.                                          |
| **Unique Count**   |    [`addUniqueOutcome`](./mobile-sdk-reference#adduniqueoutcome)    | [`sendUniqueOutcome`](./web-sdk-reference#senduniqueoutcome) | Increases count by 1, only once per attribution window. Best for binary user actions like "Started Swipe Session" or "Tapped CTA". |

<Info> Outcome events are cached locally if offline and re-attempted on the next OneSignal initialization. </Info>

***

## Count vs sum

Outcomes support two key metrics:

| Metric    | Description                                                       |
| --------- | ----------------------------------------------------------------- |
| **Count** | Number of times the outcome event was triggered                   |
| **Sum**   | Total of all numeric values sent with the outcome (if applicable) |

Outcomes with values always round to the nearest whole number.

**Example**: To track revenue from a purchase:

<CodeGroup>
  ```java java theme={null}
  // "Purchase" button pressed in the app
     ...
     OneSignal.Session.addOutcomeWithValue("Purchase", 18.76);
  ```

  ```objectivec objectivec theme={null}
  // "Purchase" button pressed in the app
     ...
     [OneSignal.Session addOutcomeWithValue:@"Purchase" value:18.76]
  ```

  ```javascript javascript theme={null}
  //Purchase Button pressed on site
  OneSignal.Session.addOutcomeWithValue("Purchase", 20.2);
  ```

  ```javascript Javascript(Web SDK) theme={null}
  //Purchase Button pressed on site
  OneSignal.Session.sendOutcome("Purchase", 20.20);
  ```

  ```swift Swift theme={null}
  let value = "20.20"//you supply the value
  OneSignal.Session.addOutcome(withValue: "Purchase", value: NSNumber(value:value), onSuccess: {outcomeSent in
    print("outcome sent: \(outcomeSent!.name) with random value: \(value)" )
  })
  ```

  ```csharp Unity(C#) theme={null}
  //Send an outcome
  OneSignal.Session.AddOutcome("outcomeName");

  //Send a unique outcome
  OneSignal.Session.AddUniqueOutcome("uniqueOutcomeName");

  //Send an outcome with a float value
  OneSignal.Session.AddOutcomeWithValue("outcomeWithVal", 4.2f);
  ```

</CodeGroup>

***

## Outcome attribution

Each Outcome is tracked with an attribution type that explains how it was generated:

* **direct** — the Outcome occurred when the user directly interacted with the message. Some Outcomes, like `os__click` and `os__confirmed_delivery`, only have direct attribution because they happen solely as a result of the message.
* **influenced** — the Outcome occurred within the attribution time window after the message was sent, but the user never directly interacted with the message.
* **unattributed** — the Outcome occurred without a direct or influenced relationship to the message.
* **total** *(default)* — the sum of **direct + influenced + unattributed**.

## Use cases

### E-commerce site

Online stores can use OneSignal push notifications to drive users back to abandoned carts, flash sales, promotions, and more. With **Outcomes**, store owners can now easily correlate push notifications to user actions such as an add-to-cart, purchase, or coupon redeemed. For purchases, outcomes go even further than simple counts and can track purchase amounts. This allows site owners to easily view the sum total of revenue generated from individual pushes.

<CodeGroup>
  ```java java theme={null}
  OneSignal.Session.addOutcomeWithValue("Purchase", 18.76);
  ```

  ```objectivec objectivec theme={null}
  [OneSignal.Session addOutcomeWithValue:@"Purchase" value:18.76]
  ```

  ```javascript javascript theme={null}
  OneSignal.Session.addOutcomeWithValue("Purchase", 18.76);
  ```

  ```Text Javascript(Web SDK) theme={null}
  OneSignal.Session.sendOutcome("Purchase", 18.76);
  ```

  ```csharp Unity(C#) theme={null}
  OneSignal.Session.AddOutcomeWithValue("Purchase", 18.76);
  ```

</CodeGroup>

### Social apps

Social apps may want to re-engage users by using a push to notify them of a match or friend request, a new like, or simply to get them swiping. By using **Outcomes**, a developer can see whether a push notification led to a user event such as initiating a chat with a match or a 34-second swipe session. These data can then be used to refine notification and targeting strategies.

In the following example, we want to track whether a user started swiping dating profiles after a push. Since we wouldn't want to count every swipe as a conversion, we use `sendUniqueOutcome`

This "Swipe" outcome will only be attributed once to the push that triggered it. Examples:

* If the user clicked the push and performed the action which called this method, it will be a direct attribution.
* If user received the push but did not click it and performed the action within in the attribution window, it will be an influenced attribution. Even if they later click the same push and performed the action again, it will still only be influenced.
* If user performs method outside of an attribution window, it will be unattributed once per session.

<CodeGroup>
  ```java Java theme={null}
  OneSignal.Session.addUniqueOutcome("Swipe");
  ```

  ```objectivec Objective-C theme={null}
  [OneSignal.Session addUniqueOutcome:@"Swipe"]
  ```

  ```javascript JavaScript theme={null}
  OneSignal.Session.addUniqueOutcome("my_outcome_event");
  ```

  ```csharp C# theme={null}
  OneSignal.Session.AddUniqueOutcome("swipe");
  ```

</CodeGroup>

### Pushes clicked by language

Within the Notification Opened/Clicked listener methods of our SDK, you can setup Outcomes to increment how many devices clicked a push by their set language. This will require some native code to detect the language of the device, but you can then pass that language into the Outcome like so:

<CodeGroup>
  ```java Java theme={null}
    public void notificationOpened(OSNotificationOpenResult result) {
      String languageCode = Locale.getDefault().getLanguage();
      System.out.println("languageCode " + languageCode);
      OneSignal.Session.addOutcome(languageCode);
    }
  ```

  ```swift Swift theme={null}
  let notificationOpenedBlock: OSHandleNotificationActionBlock = { result in
    // This block gets called when the user reacts to a notification received
    if let languageCode = Locale.current.languageCode {
        print ("languageCode: " + languageCode);
        OneSignal.Session.addOutcome(languageCode);
    }
  }
  ```

  ```javascript JavaScript theme={null}
  var language = navigator.language;
  OneSignal.Session.addOutcome(language);
  ```

</CodeGroup>

### Pushes clicked by operating system and browser

Within the Notification Opened/Clicked listener methods of our SDK, you can setup Outcomes to increment which platform's specifically were clicked. This is generic for iOS and Android as you can set `OneSignal.addOutcome("iOS")` or `OneSignal.addOutcome("Android")` in your mobile app's click handler, but if you want to track web push platforms as well, you can use this for example:

<CodeGroup>
  ```javascript Javascript(Web SDK) theme={null}
  // Example taken from Stackoverflow: https://stackoverflow.com/questions/11219582/how-to-detect-my-browser-version-and-operating-system-using-javascript
  var os = "Unknown OS";
  if (navigator.userAgent.indexOf("Win") != -1) os = "Windows";
  if (navigator.userAgent.indexOf("Mac") != -1) os = "Macintosh";
  if (navigator.userAgent.indexOf("Linux") != -1) os = "Linux";
  if (navigator.userAgent.indexOf("Android") != -1) os = "Android";
  if (navigator.userAgent.indexOf("like Mac") != -1) os = "iOS";
  console.log('Your os: ' + os);

  var browserType = "Unknown Browser Type";
  if (navigator.userAgent.indexOf("Safari") != -1) browserType = "Safari";
  if (navigator.userAgent.indexOf("Chrome") != -1) browserType = "Chrome";
  if (navigator.userAgent.indexOf("OPR") != -1) browserType = "Opera";
  if (navigator.userAgent.indexOf("Firefox") != -1) browserType = "Firefox";
  console.log('Your Browser: ' + browserType);

  OneSignal.push(["addListenerForNotificationOpened", function(data) {
  OneSignal.Session.sendOutcome(os);
  OneSignal.Session.sendOutcome(browserType);
  }]);

  ```
</CodeGroup>

***

## Disable Outcome tracking

Disable specific Outcomes from being tracked in the dashboard **Settings > Push & In-App > Outcomes Tracking**.

From here, you can click the **Stop Tracking** button to select an outcome to stop tracking in the dashboard. Once you have stopped tracking outcomes, you will see them listed here and can start tracking them again by clicking the **Start Tracking** link.

***

## FAQ

### How long is Outcome data stored?

* Notifications sent from the dashboard keep their Outcome data forever.
* Notifications sent via the API have a 30-day retention of outcomes before being purged.

### What channels support custom outcomes?

Currently custom outcomes be added to actions on Push and In-App Messages only.

Outcomes sent through In-App messages will show as "Unattributed" and will set a tag on the device in format: `outcome name : true`.

### Can I export Outcomes?

You can export a set of outcomes or all outcomes as a CSV. We also provide API access to outcomes for an [individual notification](/reference/view-message) or for [all the notifications](/reference/view-outcomes).

### Can I store strings as values in Custom Outcomes?

This is not supported.

### What happens if a device is offline?

Data for fired outcomes are queued to be sent to OneSignal once the device is online again.

### If a user backgrounds the app after clicking a notification and then comes back to it, firing an Outcome, is it counted direct or influenced?

As long as the user returns to the app within 30 seconds after backgrounding it, the session will still be considered the original session and will get direct attribution.

### When does the new Attribution Window take affect?

If you change the attribution window from 24 hours to 1 hour for example, then the 1 hour window will take affect on a per-device basis once each device opens the app from a brand new session. This new session is created after 30 seconds of being outside the app.

### Why do sessions not match with other analytics?

OneSignal only counts a session after the user has left the app for over 30 seconds. If you close the app or website and return to it within 30 seconds, it will not be a new session.

For instance, Apple's analytics tracks the session as the number of times the app has been used for at least two seconds. If the app is in the background and is later used again, that counts as another session.

***


Built with [Mintlify](https://mintlify.com).
