# Source: https://firebase.google.com/docs/cloud-messaging/manage-tokens.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/manage-tokens.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/manage-tokens.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/manage-tokens.md.txt

# Best practices for FCM registration token management

<br />

If you use FCM APIs to build send requests programmatically, you may
find that, over time, you are wasting resources by sending messages to inactive
devices with stale registration tokens. This situation can affect the message
delivery data reported in the Firebase console or data exported to BigQuery,
showing up as a dramatic (but not actually valid) drop in delivery rates. This
guide discusses some measures you can take to help ensure efficient message
targeting and valid delivery reporting.

## Stale and expired registration tokens

Stale registration tokens are tokens associated with inactive devices that have
not connected to FCM for over a month. As time passes, it becomes less
and less likely for the device to ever connect to FCM again. Message
sends and topic fanouts for these stale tokens are unlikely to ever be
delivered.

There are several reasons why a token can become stale. For example, the device
the token is associated with may be lost, destroyed, or put into storage and
forgotten.

When stale tokens reach 270 days of inactivity, FCM will consider them
**expired tokens** . Once a token expires, FCM marks it as invalid and
rejects sends to it. However, FCM issues a new token for the app
instance in the rare case that the device connects again and the app is opened.

## Basic best practices

There are some fundamental practices you should follow in any app that uses
FCM APIs to build send requests programmatically. The main best
practices are:

- **Retrieve registration tokens from FCM and store them on your
  server.** An important role for the server is to keep track of each client's token and keep an updated list of active tokens. We strongly recommend implementing a token timestamp in your code and your servers, and updating this timestamp at regular intervals.
- **Maintain token freshness and remove stale tokens.** In addition to removing tokens that FCM no longer considers valid, you may want to monitor other signs that tokens have become stale and remove them proactively. This guide discusses some of your options for achieving this.

## Retrieve and store registration tokens

On initial startup of your app, the FCM SDK generates a registration
token for the client app instance. This is the token that you must include in
targeted send requests from the API, or add to topic subscriptions for targeting
topics.

**We strongly recommend your app retrieve this token at initial startup and save
it to your app server alongside a timestamp** . This timestamp must be
implemented by your code and your servers, as it is not provided for you by
FCM SDKs.

Also, it's important to save the token to the server and update the timestamp
whenever it changes, such as when:

- The app is restored on a new device
- The user uninstalls or re-installs the app
- The user clears app data
- The app becomes active again after FCM has expired its existing token

### Example: store tokens and timestamps in Cloud Firestore

For example, you could use Cloud Firestore to store tokens in a collection
called `fcmTokens`. Each document ID in the collection corresponds to
a user ID, and the document stores the current registration token and its
last-updated timestamp. Use the `set` function as shown in this Kotlin example:  

        /**
         * Persist token to third-party servers.
         *
         * Modify this method to associate the user's FCM registration token with any server-side account
         * maintained by your application.
         *
         * @param token The new token.
         */
        private fun sendTokenToServer(token: String?) {
            // If you're running your own server, call API to send token and today's date for the user

            // Example shown below with Firestore
            // Add token and timestamp to Firestore for this user
            val deviceToken = hashMapOf(
                "token" to token,
                "timestamp" to FieldValue.serverTimestamp(),
            )
            // Get user ID from Firebase Auth or your own server
            Firebase.firestore.collection("fcmTokens").document("myuserid")
                .set(deviceToken)
        }  
    https://github.com/firebase/quickstart-android/blob/0b77e46545ef38b040d140f360cfe3f75b54e15d/messaging/app/src/main/java/com/google/firebase/quickstart/fcm/kotlin/MyFirebaseMessagingService.kt#L105-L125

Whenever a token is retrieved, it is stored in Cloud Firestore by calling
`sendTokenToServer`:  

        /**
         * Called if the FCM registration token is updated. This may occur if the security of
         * the previous token had been compromised. Note that this is called when the
         * FCM registration token is initially generated so this is where you would retrieve the token.
         */
        override fun onNewToken(token: String) {
            Log.d(TAG, "Refreshed token: $token")

            // If you want to send messages to this application instance or
            // manage this apps subscriptions on the server side, send the
            // FCM registration token to your app server.
            sendTokenToServer(token)
        }  
    https://github.com/firebase/quickstart-android/blob/0b77e46545ef38b040d140f360cfe3f75b54e15d/messaging/app/src/main/java/com/google/firebase/quickstart/fcm/kotlin/MyFirebaseMessagingService.kt#L72-L84

            var token = Firebase.messaging.token.await()

            // Check whether the retrieved token matches the one on your server for this user's device
            val preferences = this.getPreferences(Context.MODE_PRIVATE)
            val tokenStored = preferences.getString("deviceToken", "")
            lifecycleScope.launch {
                if (tokenStored == "" || tokenStored != token)
                {
                    // If you have your own server, call API to send the above token and Date() for this user's device

                    // Example shown below with Firestore
                    // Add token and timestamp to Firestore for this user
                    val deviceToken = hashMapOf(
                        "token" to token,
                        "timestamp" to FieldValue.serverTimestamp(),
                    )

                    // Get user ID from Firebase Auth or your own server
                    Firebase.firestore.collection("fcmTokens").document("myuserid")
                        .set(deviceToken).await()
                }
            }  
    https://github.com/firebase/quickstart-android/blob/0b77e46545ef38b040d140f360cfe3f75b54e15d/messaging/app/src/main/java/com/google/firebase/quickstart/fcm/kotlin/MainActivity.kt#L131-L153

## Maintain token freshness and remove stale tokens

Determining whether a token is fresh or stale is not always straightforward. To
cover all cases, you should adopt a threshold for when you consider tokens
stale. By default, FCM considers a token to be stale if its app
instance hasn't connected for a month. Any token older than one month is likely
to be an inactive device; an active device would have otherwise refreshed its
token.

Depending on your use case, one month may be too short or too long, so it is up
to you to determine the criteria that works for you.

### Detect invalid token responses from the FCM backend

Make sure to detect invalid token responses from FCM and respond by
deleting from your system any registration tokens that are known to be invalid
or have expired. With the HTTP v1 API, these error messages may indicate that
your send request targeted invalid or expired tokens:

- `UNREGISTERED` (HTTP 404)
- `INVALID_ARGUMENT` (HTTP 400)

| **Note:** `INVALID_ARGUMENT` can also be returned in cases of issues in the message payload, so it signals an invalid token only if the payload is completely valid. See [ErrorCodes](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode) for more information.

If you are certain that the message payload is valid and you receive either of
these responses for a targeted token, it is safe to delete your record of this
token, since it will never again be valid. For example, to delete invalid tokens
from Cloud Firestore, you could deploy and run a function like the following:  

        // Registration token comes from the client FCM SDKs
        const registrationToken = 'YOUR_REGISTRATION_TOKEN';

        const message = {
        data: {
            // Information you want to send inside of notification
        },
        token: registrationToken
        };

        // Send message to device with provided registration token
        getMessaging().send(message)
        .then((response) => {
            // Response is a message ID string.
        })
        .catch((error) => {
            // Delete token for user if error code is UNREGISTERED or INVALID_ARGUMENT.
            if (error.errorCode == "messaging/registration-token-not-registered") {
                // If you're running your own server, call API to delete the
                token for the user

                // Example shown below with Firestore
                // Get user ID from Firebase Auth or your own server
                Firebase.firestore.collection("fcmTokens").document(user.uid).delete()
            }
        });

FCM will only return an invalid token response if a token expired
after 270 days or if a client explicitly unregistered. If you need to more
accurately track staleness according to your own definitions, you can
proactively [remove stale registration tokens](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/manage-tokens#remove-stale-tokens).

### Update tokens on a regular basis

We recommend that you periodically retrieve and update all registration tokens
on your server. This requires you to:

- Add app logic in your client app to retrieve the current token using the appropriate API call (such as [`token(completion):`](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging) for Apple platforms or [`getToken()`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#getToken()) for Android) and then send the current token to your app server for storage (with a timestamp). This could be a monthly job configured to cover all clients or tokens.
- Add server logic to update the token's timestamp at regular intervals, regardless of whether or not the token has changed.

For an example of Android logic for updating tokens using
[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager),
see
[Managing Cloud Messaging Tokens](https://firebase.blog/posts/2023/04/managing-cloud-messaging-tokens/#updating-registration-tokens)
on the Firebase blog.

Whatever timing pattern you follow, make sure to update tokens periodically. An
update frequency of once per month strikes a good balance between battery impact
and detecting inactive registration tokens. By doing this refresh, you also
ensure that any device which goes inactive will refresh its registration when it
becomes active again. There is no benefit to doing the refresh more frequently
than weekly.

### Remove stale registration tokens

Before sending messages to a device, ensure that the timestamp of the device's
registration token is within your staleness window period. For example, you
could implement Cloud Functions for Firebase to run a daily check to ensure that the
timestamp is within a defined staleness window period such as `const
EXPIRATION_TIME = 1000 * 60 * 60 * 24 * 30;` and then remove stale tokens:  

    exports.pruneTokens = functions.pubsub.schedule('every 24 hours').onRun(async (context) => {
      // Get all documents where the timestamp exceeds is not within the past month
      const staleTokensResult = await admin.firestore().collection('fcmTokens')
          .where("timestamp", "<", Date.now() - EXPIRATION_TIME)
          .get();
      // Delete devices with stale tokens
      staleTokensResult.forEach(function(doc) { doc.ref.delete(); });
    });  
    https://github.com/firebase/quickstart-android/blob/0b77e46545ef38b040d140f360cfe3f75b54e15d/messaging/functions/index.js#L18-L25

### Unsubscribe stale tokens from topics

If you use topics, you may also want to unregister stale tokens from the topics
to which they are subscribed. This involves two steps:

1. Your app should resubscribe to topics once per month and whenever the registration token changes. This forms a self-healing solution, where the subscriptions reappear automatically when an app becomes active again.
2. If an app instance is idle for one month (or your own staleness window) you should unsubscribe it from topics using the [Firebase Admin SDK](https://firebase.google.com/docs/cloud-messaging/manage-topics#unsubscribe) to delete the token to topic mapping from the FCM backend.

The benefit of these two steps is that your fanouts will occur faster since
there are fewer stale tokens to fan out to, and your stale app instances will
automatically resubscribe once they are active again.

## Measure delivery success

To get the most accurate picture of message delivery, it is best to only send
messages to actively used app instances. This is especially important if you
regularly send messages to topics with large numbers of subscribers; if a
portion of those subscribers are actually inactive, the impact on your delivery
statistics can be significant over time.

Before targeting messages to a token, consider:

- Do Google Analytics, data captured in BigQuery, or other tracking signals indicate the token is active?
- Have previous delivery attempts failed consistently over a period of time?
- Has the registration token been updated on your servers in the past month?
- For Android devices, does the [FCM Data API](https://firebase.google.com/docs/reference/fcmdata/rest) report a high percentage of message delivery failures due to [`droppedDeviceInactive`](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#messageoutcomepercents)?

For more information about delivery, see
[Understanding message delivery](https://firebase.google.com/docs/cloud-messaging/understand-delivery).