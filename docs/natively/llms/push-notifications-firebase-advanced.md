# Source: https://docs.buildnatively.com/guides/integration/push-notifications-firebase-advanced.md

# Push Notifications - Firebase (Advanced)

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)
* [Recommendations](#recommendations)

We are using [Firebase](https://firebase.google.com/products/cloud-messaging) Service to provide a Push Notification functionality.

### 🧋 Bubble.io Plugin

#### \[Element] Natively - Push Notifications (Firebase)

#### Initialization:

On initialization, the element will try to get the current notification permission status. (No need to call it on the Page Is Load event)

#### Element Events:

* **Firebase FMC Token Updated** - get called when [FMC token](https://firebase.google.com/docs/cloud-messaging/manage-tokens) was updated.
* **Firebase APNS Token Updated** - get called when [APNS token](https://firebase.google.com/docs/cloud-messaging/ios/client) was updated.
* **Notification permissions authorized** - get called when the user clicks Allow on permission alert.
* **Notification permissions denied** - get called when the user clicks Decline on permission alert.
* **Notification permissions status updated** - get called when permission status was updated because of the user's action.
* **Topic subscription status** - get called when topic subscription status was updated because of the user's action: subscribe/unsubscribe.

#### Element States:

* **Permission Status** - Yes or No.
* **Firebase FCM Token** -  [FMC token](https://firebase.google.com/docs/cloud-messaging/manage-tokens)'s text value.
* **Firebase APNS Token -** [APNS token](https://firebase.google.com/docs/cloud-messaging/ios/client)'s text value
* **Topic subscription status** - 'SUCCESS' if the 'subscribe' action was successful
* **Topic unsubscribe status** - 'SUCCESS' if the 'unsubscribe' action was successful

{% hint style="info" %}
You will need the **FMC token** value to send a push notification. Take this value on the user's login and store it in a database. (For example, you can add a property to the user named fmc\_token)
{% endhint %}

{% hint style="info" %}
You will need the **APNS token** value to send a push notification to iOS device. Take this value on the user's login and store it in a database. (For example, you can add a property to the user named apns\_token)
{% endhint %}

#### Element Actions:

* **Request the user's push notification permission** - displays a systems popup with your Notification Permissions Text
* **Get the user's Firebase APNS Token** - Reload the user's Firebase APNS  token
* **Get the user's Firebase FCM Token** - Reload the user's Firebase FCM  token
* **Get the user's push notification permission status**
* **Subscribe to topic**&#x20;
  * Topic ID - the [FCM topic](https://firebase.google.com/docs/cloud-messaging/android/topic-messaging) name
* **Unsubscribe from topic**&#x20;
  * Topic ID - the [FCM topic](https://firebase.google.com/docs/cloud-messaging/android/topic-messaging) name&#x20;

#### How to send Push Notifications with Firebase?

1. **Firebase Console**\
   \- [Firebase Console Docs](https://firebase.google.com/docs/cloud-messaging/android/send-with-console)
2. **Topic messaging**\
   \- [Firebase Topic Messaging Docs](https://firebase.google.com/docs/cloud-messaging/android/topic-messaging)
3. Cloud Messaging REST API

To a topic subscribers

```
curl -X POST \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
https://fcm.googleapis.com/v1/projects/YOUR_PROJECT_ID/messages:send \
-d '{
"message": {
"notification": {
"title": "Notification to All App Users",
"body": "This is for all users of the app."
},
"data": {
"url": "{YOUR_URL_TO_OPEN_INSIDE_OF_THE_APP}",
},
"topic": "all"
}
}'
```

To a single user

```
curl -X POST \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
https://fcm.googleapis.com/v1/projects/YOUR_PROJECT_ID/messages:send \
-d '{
"message": {
"notification": {
"title": "Notification to a Single App Users",
"body": "This is for a single user of the app."
},
"data": {
"url": "{YOUR_URL_TO_OPEN_INSIDE_OF_THE_APP}",
},
"token": "{FCM_TOKEN}"
}
}'
```

### **Bubble - Setup example**

{% hint style="info" %}
These steps provide a general guide. You can adapt them to fit the specific needs and logic of your application.
{% endhint %}

1. **Request Push Notification permission whenever you need it.**<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F7LmxLRVp2aX5kl2KFacU%2FScreenshot%20from%202024-11-29%2010-34-43.png?alt=media&#x26;token=1088168c-d0c8-48be-a0d9-449a362afabe" alt=""><figcaption></figcaption></figure>
2. **Save APNS token to your user model (only for iOS)**

   <div><figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FarYlPIdTVv9uGQMsefkw%2FScreenshot%20from%202024-11-29%2010-43-46.png?alt=media&#x26;token=17157fb7-f2ae-4c02-b51d-acd9d4eb84d1" alt=""><figcaption></figcaption></figure> <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FYFdMnbNCj3Scxq0OIPBg%2FScreenshot%20from%202024-11-29%2010-50-29.png?alt=media&#x26;token=0aaa2f39-347a-45e2-a450-9d07abb14de0" alt=""><figcaption></figcaption></figure></div>
3. **Save FCM token to your user model**

   <div><figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FbdbWOdQ5Iwv7Ft4Pi96X%2FScreenshot%20from%202024-11-29%2010-46-58.png?alt=media&#x26;token=055ee45b-54e4-46ce-b036-a28a1e6ca7e4" alt=""><figcaption></figcaption></figure> <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fnym9tHGkR5tg75zu1R2u%2FScreenshot%20from%202024-11-29%2010-47-48.png?alt=media&#x26;token=b85fd85c-acf0-447d-8052-5ed97b35e8ee" alt=""><figcaption></figcaption></figure></div>

### 🛠 JavaScript SDK

#### NativelyNotifications

<pre class="language-javascript" data-overflow="wrap" data-line-numbers><code class="lang-javascript">const notifications = new NativelyFirebaseNotifications()
const apns_token_callback = function (resp) {
        console.log(resp.token); // string
};
const token_callback = function (resp) {
        console.log(resp.token); // string
};
const topic = "FCM topic name" // string
const subscribe_callback = function (resp) {
        console.log(resp.status); // string
        console.log(resp.message); // string. error message if any
<strong>};  
</strong><strong>const unsubscribe_callback = function (resp) {
</strong>        console.log(resp.status); // string
        console.log(resp.message); // string. error message if any
};  
<strong>const permission_callback = function (resp) {
</strong>        console.log(resp.status); // true/false
<strong>};
</strong><strong>const permission_status_callback = (instance) => (resp) => {
</strong><strong>        console.log(resp.status); // true/false
</strong><strong>};
</strong>notifications.firebase_get_apns_token(apns_token_callback);
<strong>notifications.firebase_get_token(token_callback);
</strong>notifications.firebase_subscribe_to_topic(topic, token_callback);
notifications.firebase_unsubscribe_from_topic(topic, unsubscribe_callback);
<strong>notifications.firebase_has_permission(permission_status_callback);
</strong><strong>notifications.firebase_request_permission(permission_callback);
</strong></code></pre>

**How to set up?**

1. Make sure you've [prepared](https://docs.buildnatively.com/natively-platform/features/notifications/firebase-notifications-advanced) your app and Firebase for Push Notifications.
2. call **firebase\_request\_permission** **(required for both iOS & Android).**
3. call **firebase\_get\_apns\_token (will return the APNS token for iOS).**
4. call **firebase\_get\_token (will return the FCM token).**
5. Save FMC token and the APNS token (for iOS) somewhere (for example, save them in the user's ***fcm\_token*** property and ***apns\_token*** property).

### Recommendations

* Request the user's notification permission. You can do that in any necessary place. For example: show a popup that explains to the user's why your app needs it (so, it can be a better experience when just displaying a system popup)
* Identify a user by using FCM token.
* Check the fcm\_token value on each login (It can be [changed](https://firebase.google.com/docs/cloud-messaging/manage-tokens#stale-and-expired-tokens))
