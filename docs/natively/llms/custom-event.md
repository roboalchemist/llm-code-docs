# Source: https://docs.buildnatively.com/guides/integration/custom-event.md

# Custom Event

### Prerequisites

* The Analytics feature must be enabled for your app. Follow this guide for setup: [analytics](https://docs.buildnatively.com/natively-platform/features/analytics "mention")
* Availability:
  * Bubble Plugin Version: 2.25.0 or higher
  * JavaScript SDK Version: 2.19.1 or higher

### Bubble.io Plugin

**\[Action]** Natively - Send Custom Event

* Event name - The unique identifier that will appear in your Analytics dashboard. (e.g., `user_onboarded`, `checkout_started`)
* Event data - A JSON object containing custom parameters and values you want to send with the event

#### Usage Example (Bubble Workflow)

1. In your workflow, add the action: `Natively - Send Custom Event`.
2. Provide the Event name.
3. Provide the Event data as a JSON object (must be valid JSON).  Example:&#x20;

```json
{
  "user_id": "12345",
  "screen": "home",
  "duration_seconds": 45,
  "is_premium_user": true
}
```

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FU2wHE7BWdOCeg6SxxIsx%2Fcustom_event_bubble.png?alt=media&#x26;token=3106a21b-1846-44ec-ac84-7cc349d31301" alt=""><figcaption></figcaption></figure>

#### Result:&#x20;

The event and its custom parameters will be recorded in your Analytics dashboard.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FkD3BEPbWxTlafC7qSZjX%2Fcustom_event.png?alt=media&#x26;token=fa62f065-d7f4-4f7e-abad-0b1db3acf02b" alt=""><figcaption></figcaption></figure>

### JavaScript SDK

Use the `natively.analyticsTrackEvent()` method to send the event name and a JavaScript object containing the custom data.

Example:&#x20;

```javascript
// 1. Define custom parameters using a Map
const eventData = new Map();
eventData.set('user_id', '12345');
eventData.set('screen', 'home');
eventData.set('duration_seconds', 45);
eventData.set('is_premium_user', true);

// 2. Send the event
natively.analyticsTrackEvent('button_clicked', Object.fromEntries(eventData));
```

### How to Test in AppsFlyer

1. Add the test device to your AppsFlyer account. Follow this guide: [here](https://support.appsflyer.com/hc/en-us/articles/207031996-Registering-test-devices#register-a-device-manually)
2. In the AppsFlyer dashboard, go to Settings > SDK Integration Test > Live events.<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F24X9s3Nw1u6hjTglwPr4%2Fcustom_event_test.png?alt=media&#x26;token=77624ee7-3df7-4521-af19-ec7502819d19" alt=""><figcaption></figcaption></figure>
3. Select your app and the test device, then click Continue.<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fa9VmZPJPL34x3GHrGYc9%2Fcustom_event_test_select_app_and_device.png?alt=media&#x26;token=b705bc17-6fbe-4299-b644-e3b9d7d78be6" alt=""><figcaption></figcaption></figure>
4. Start the event listener. Launch the app on the test device and trigger the custom event (e.g., click the button associated with the event).

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FkVaOUwusjp7F1fqNkx3B%2Fcustom_event_test_start.png?alt=media&#x26;token=fe716437-b365-48c9-8dcc-8f7e6952f4f5" alt=""><figcaption></figcaption></figure>

#### **Result:**&#x20;

You will see the custom event and its associated data registered in the AppsFlyer Live Events dashboard.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FkD3BEPbWxTlafC7qSZjX%2Fcustom_event.png?alt=media&#x26;token=fa62f065-d7f4-4f7e-abad-0b1db3acf02b" alt=""><figcaption></figcaption></figure>
