# Source: https://docs.instabug.com/android/set-up-luciq-for-android/setup-push-notifications.md

# Setup Push Notifications

### Push Notifications

You can enable Luciq to send your users push notifications each time you send them a new message.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FJ9yYDe12I6tuuDTLyBKv%2Fimage.png?alt=media&#x26;token=4ce893bd-dff5-45ac-8f64-39dc7d1fca2d" alt=""><figcaption></figcaption></figure>

#### Push Notification Key

Follow the steps below to upload your push certificate to your Luciq dashboard.

1. Go to the **Push Notifications** page on your Luciq dashboard and add you `API_KEY`.
2. Make sure to select whether the `API_KEY` you're adding is for development or production.

#### Setting Your App to Handle Luciq Notifications

Pass the push notification registration token you get to Luciq.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.setPushNotificationRegistrationToken("PUSH_NOTIFICATION_TOKEN")
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.setPushNotificationRegistrationToken("PUSH_NOTIFICATION_TOKEN");
```

{% endcode %}
{% endtab %}
{% endtabs %}

When you receive a notification, check if it's an Luciq notification, then pass it to Luciq if necessary.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
if(Replies.isLuciqNotification(data)){
  //Shown notification related to Luciq
  Replies.showNotification(data)
}
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
if(Replies.isLuciqNotification(data)){
  //Shown notification related to Luciq
  Replies.showNotification(data);
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Notification Channel ID

You can use channels to group the incoming Luciq notifications into a manageable group. To do this, you simply need to pass the channel ID to the below API.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.setPushNotificationChannelId(String pushNotificationChannelId)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.setPushNotificationChannelId(String pushNotificationChannelId);
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Notification Icon

The icon that is shown with each push notification can be changed to match your application's icon. The API below can be used to change this icon.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.setNotificationIcon(@DrawableRes int notificationIcon)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.setNotificationIcon(@DrawableRes int notificationIcon);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Disabling Push Notifications

Push notifications are enabled by default if you upload a push certificate to your Luciq dashboard. To disable them, modify your builder method as in the following example.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.setPushNotificationState(Feature.State.DISABLED)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.setPushNotificationState(Feature.State.DISABLED);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### In-App Notifications

By default, a notification will be shown on top of your app's UI when a new message is received.

{% hint style="info" %}

#### Email Notifications

If your user doesn't view the new message within 10 minutes, they will be sent an email notification as well.
{% endhint %}

#### Disabling In-App Notifications

Use the following method to disable notifications that appear in-app.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.setReplyNotificationEnabled(false)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.setInAppNotificationEnabled(false);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### In-App Notification Sound

When your app users receive an in-app notification through Luciq, sound is enabled by default. However, you can disable it by using the following method.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.setInAppNotificationEnabled(false)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.setInAppNotificationSound(false);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### System Notification Sound

System notification sound is disabled by default. You can enable it by adding the following method to Luciq builder.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.setSystemReplyNotificationSoundEnabled(true)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.setSystemReplyNotificationSoundEnabled(true);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Conversation Sound

When your app users receive a new in-app chat in a conversation with you, sound is also enabled by default. You can disable it by adding the following method to Luciq builder.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.setShouldPlayConversationSounds(false)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.setShouldPlayConversationSounds(false);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Get Unread Messages Count

You can use the following method to get the number of messages the user has yet to read.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Replies.getUnreadRepliesCount();
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Replies.getUnreadRepliesCount()
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Upload Service Account File

Google has announced the deprecation of the old FCM APIs that are used for Push Notifications. To ensure better performance and user experience, it is imperative to migrate to the HTTPv1 APIs.

{% hint style="warning" %}
This upgrade will also involve a change in the method of authorization, shifting from using api\_key to using a service-account.json file. The steps below provide a detailed guide on how to perform this migration to avoid any service interruption.
{% endhint %}

#### Prepare the service-account.json from Firebase

1. Go to your Firebase Projects Page by navigating to the [Firebase Console](https://console.firebase.google.com/).

2. Select your project from the Firebase console landing page, then select the project you want to update.

3. Access your project settings by clicking on the gear icon next to the project name to open Project Settings.

   ![](https://files.readme.io/0ae7a47-image.png)

4. Generate a new private key by doing the following:

   1. Go to the **Service Accounts** tab
   2. Click on the **Generate new private key** button

   ![](https://files.readme.io/22e0e06-image.png)

{% hint style="info" %}

#### Confirming your action

A file named \<your-project>-firebase-adminsdk-\<first-numbers-of-your-key>.json will be downloaded. This is your service-account.json file.
{% endhint %}

#### Configure Push Notifications in Luciq Dashboard

1. Select the App and Environment you need to configure push notifications for.

2. Navigate to Settings by clicking on Settings in the left sidebar.

   <figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FBwWR0cGaSnH2QNUn7UOy%2Fimage.png?alt=media&#x26;token=b42351e1-8caa-4059-9bc1-4a4f8d749a6d" alt=""><figcaption></figcaption></figure>

3. Under the settings menu, select Push Notification Settings.

4. Upload the service-account.json file you obtained from Firebase in the previous steps.<br>

   <figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FEO0epHwNcmBBBlDbdS8b%2Fimage.png?alt=media&#x26;token=9d11b538-0b6f-40dc-8638-92131d3acac7" alt=""><figcaption></figcaption></figure>

5. Update to the latest Luciq SDK version to leverage the new push notification features.
