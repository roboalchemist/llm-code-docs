# Source: https://docs.buildnatively.com/guides/integration/geolocation.md

# Source: https://docs.buildnatively.com/natively-platform/features/geolocation.md

# Geolocation

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FFbEAQBcf2tLQ5LS0KGkb%2Fnatively_location_feature.png?alt=media&#x26;token=f0758281-4cab-4562-85b4-730d0acbb2af" alt=""><figcaption></figcaption></figure>

### How to set up geolocation?

Turn on the **Location** feature:

* **Permission description** - The permission description text should explain to the user why your app needs that permission. Refer to [**Apple's guidelines** ](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/)and [Google's guidelines](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en) to avoid potential **rejection**.

### How to set up background location tracking?

{% hint style="danger" %}
To start using background location tracking. You need to enable a Geolocation and fill out the Permission description for iOS (If you're planning to use iOS).
{% endhint %}

* **Permission description** - The permission description text should explain to the user why your app needs that permission. Refer to [**Apple's guidelines** ](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/)and [Google's guidelines](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en) to avoid potential **rejection**.

{% hint style="info" %}
To make background location tracking work correctly, you need to ask the user to give Always allow permission. The system will handle that for you, but make sure you specify it in the permission description for Android.\
For iOS OS will ask users to allow background tracking automatically once they collapse that app.
{% endhint %}

* **Webhook URL** - This is your endpoint URL where we will send a user's geolocation. A few requirements for an endpoint:
  * HTTPS (HTTP is not supported)
  * POST method
  * JSON in a body

```json
// JSON of what you should expect to be received from a device 
// Example
{
	"latitude": 50.000001,
	"longitude": 50.000001,
	// Identifier that will be passed later (Check Integration for more details)
	"identifier": "TEST", 
	// Error can be null or string (which will contain an error message)
	"error": null // "Data Discarded", "Timeout", "Authorization Needed", "Internal Server Error", "Parsing Error", "User Cancelled", "Invalid/Missing API Key", "Quota limit reached", "Not Found", "Reserved IP", "Not Supported", "Invalid polygon. Must be 1 or more points", "Network error: \(statusCode)"
}
```

* **Header Name & Value (Optional)** - In case you have authorization on your webhook endpoint. This header will be sent to your endpoint from a device.

### How to create a webhook with Bubble?

* [https://manual.bubble.io/core-resources/api/workflow-api](https://manual.bubble.io/help-guides/apis-connect-to-other-apps/the-bubble-api/the-workflow-api/workflow-api-endpoints)
* [How to setup Bubble's Workflow API Endpoint for your Application](https://youtu.be/6MxCxUroY4s)

### How to use geolocation?

{% content-ref url="../../guides/integration/geolocation" %}
[geolocation](https://docs.buildnatively.com/guides/integration/geolocation)
{% endcontent-ref %}

### I'm already utilizing geolocation permissions on my website. Is it necessary to implement a native geolocation API in my app?

Yes, we advise using the native geolocation API for an enhanced user experience, but the web geolocation API is also an option, albeit with repeated permission prompts each time the app is accessed.
