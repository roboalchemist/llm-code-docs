# Source: https://docs.buildnatively.com/guides/integration/request-users-review.md

# Request User's review

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

Apple's recommendation:

Spend some time thinking about the best places within your own app to show a request for review and what conditions are appropriate to delay it. Here are some best practices:

* Try to request at a time that will not interrupt what the user is trying to achieve in your app. For example, at the end of a sequence of events that the user has successfully completed.
* Avoid showing a request for a review immediately when a user launches your app, even if it is not the first time that it launches.

Check out Apple's guidelines about [Requesting User's review](https://developer.apple.com/design/human-interface-guidelines/ios/system-capabilities/ratings-and-reviews/) for more details.

There is also one more way to request a review. You can use open **Natively - Open external app** action with this URL:

itms-apps\://itunes.apple.com/app/idXXXXXXXX?action=write-review

Where idXXXXXXXX is your AppStore id

{% hint style="info" %}
This feature will not work until you submit your app to the App Store / Google Play.
{% endhint %}

###

### 🧋 Bubble.io Plugin

#### \[Action] Natively - Request AppStore/GooglePlay review

### 🛠 JavaScript SDK

#### Request AppStore/GooglePlay review

{% code overflow="wrap" lineNumbers="true" %}

```javascript
window.natively.requestAppReview();
```

{% endcode %}
