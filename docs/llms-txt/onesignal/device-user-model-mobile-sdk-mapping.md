# Source: https://documentation.onesignal.com/docs/en/device-user-model-mobile-sdk-mapping.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mobile SDK Mapping

> Compare method and property names between OneSignal's legacy Player Model (v3 & v4) and the modern User Model (v5+), with side-by-side Swift code examples for easier migration.

<Warning>
  OneSignal has updated from a device-centric model (Player ID) to a user-centric model (OneSignal ID). For migration guidance, refer to the [User Model Migration Guide](./user-model-migration-guide).

  For documentation on legacy device-centric implementations, see [Version 9](/v9.0/docs/sdk-reference).
</Warning>

This page maps method and property names between OneSignal's Player Model and User Model SDKs. It mirrors the layout of the original [Player Model Client SDK Reference](/v9.0/docs/sdk-reference) for familiarity. Swift examples illustrate the API changes, but these are not always complete working samples. Refer to the linked documentation for examples in other languages and full implementation details.

## Initializing OneSignal

### `initWithLaunchOptions()`

**Player Model** [Reference](/v9.0/docs/sdk-reference)

```swift  theme={null}
OneSignal.initWithLaunchOptions(launchOptions)
OneSignal.setAppId("ONESIGNAL_APP_ID")
```

**User Model** [Reference](./mobile-sdk-reference#initialize)

```swift  theme={null}
OneSignal.initialize("YOUR_ONESIGNAL_APP_ID", withLaunchOptions: launchOptions)
```

***

## Debugging

### `setLogLevel()`

**Player Model** [Reference](/v9.0/docs/sdk-reference)

```swift  theme={null}
OneSignal.setLogLevel(.LL_VERBOSE, visualLevel: .LL_NONE)
```

**User Model** [Reference](./mobile-sdk-reference#debugging)

```swift  theme={null}
OneSignal.Debug.setLogLevel(.LL_VERBOSE)
```

***

## External user IDs

### `setExternalId()`

**Player Model** [Reference](/v9.0/docs/sdk-reference)

```swift  theme={null}
OneSignal.setExternalId("EXTERNAL_USER_ID")
```

**User Model** [Reference](./mobile-sdk-reference#debugging)

```swift  theme={null}
OneSignal.login("EXTERNAL_USER_ID")
```

### `removeExternalUserId()`

**Player Model** [Reference](/v9.0/docs/sdk-reference)

```swift  theme={null}
OneSignal.removeExternalUserId({ results in ... })
```

**User Model** [Reference](./mobile-sdk-reference#log-out-a-user)

```swift  theme={null}
OneSignal.logout()
```

***

## Tags

### `sendTag()`

**Player Model** [Reference](./add-user-data-tags)

```swift  theme={null}
OneSignal.sendTag("key", value: "value")
```

**User Model** [Reference](./mobile-sdk-reference)

```swift  theme={null}
OneSignal.User.addTag(key: "key", value: "value")
```

### `sendTags()`

```swift  theme={null}
OneSignal.sendTags(["key1": "value1", "key2": "value2"])
```

```swift  theme={null}
OneSignal.User.addTags(["key1": "value1", "key2": "value2"])
```

### `getTags()`

```swift  theme={null}
OneSignal.getTags({ tags in ..., onFailure: { error in ... })
```

```swift  theme={null}
let tags = OneSignal.User.getTags()
```

### `deleteTag()`

```swift  theme={null}
OneSignal.deleteTag("key")
```

```swift  theme={null}
OneSignal.User.removeTag("key")
```

### `deleteTags()`

```swift  theme={null}
OneSignal.deleteTags(["key1", "key2"])
```

```swift  theme={null}
OneSignal.User.removeTags(["key1", "key2"])
```

***

## User data

### `notificationPermissionStatus`

```swift  theme={null}
OneSignal.getDeviceState().notificationPermissionStatus
```

```swift  theme={null}
OneSignal.Notifications.permissionNative
```

### `userId`

```swift  theme={null}
OneSignal.getDeviceState().userId
```

```swift  theme={null}
OneSignal.User.pushSubscription.id
```

### `hasNotificationPermission()` / `areNotificationsEnabled`

```swift  theme={null}
OneSignal.getDeviceState().areNotificationsEnabled()
```

```swift  theme={null}
OneSignal.Notifications.permission
```

### `pushToken`

```swift  theme={null}
OneSignal.getDeviceState().pushToken
```

```swift  theme={null}
OneSignal.User.pushSubscription.token
```

### `hasNotificationPermission`

```swift  theme={null}
OneSignal.getDeviceState().hasNotificationPermission
```

```swift  theme={null}
OneSignal.User.pushSubscription.optedIn
```

### `isSubscribed` \[Dropped]

```swift  theme={null}
OneSignal.getDeviceState().isSubscribed
```

**User Model**: N/A

### `isPushDisabled` \[Dropped]

```swift  theme={null}
OneSignal.getDeviceState().isPushDisabled
```

**User Model**: N/A

### `setLanguage()`

```swift  theme={null}
OneSignal.setLanguage("es")
```

```swift  theme={null}
OneSignal.User.setLanguage("en")
```

***

## Privacy

### `setRequiresUserPrivacyConsent()`

```swift  theme={null}
OneSignal.setRequiresUserPrivacyConsent(true)
```

```swift  theme={null}
OneSignal.setConsentRequired(true)
```

### `consentGranted()`

```swift  theme={null}
OneSignal.consentGranted(true)
```

```swift  theme={null}
OneSignal.setConsentGiven(true)
```

***

## Location

### `setLocationShared()`

```swift  theme={null}
OneSignal.setLocationShared(false)
```

```swift  theme={null}
OneSignal.Location.isShared = false
```

### `isLocationShared()`

```swift  theme={null}
OneSignal.isLocationShared()
```

```swift  theme={null}
OneSignal.Location.isShared
```

### `promptLocation()`

```swift  theme={null}
OneSignal.promptLocation()
```

```swift  theme={null}
OneSignal.Location.requestPermission()
```

***

## Subscription observers

### `addSubscriptionObserver()`

```swift  theme={null}
OneSignal.addSubscriptionObserver(subscriptionObserver)
```

```swift  theme={null}
OneSignal.User.pushSubscription.addObserver(pushSubscriptionObserver)
```

### `removeSubscriptionObserver()`

```swift  theme={null}
OneSignal.removeSubscriptionObserver(subscriptionObserver)
```

```swift  theme={null}
OneSignal.User.pushSubscription.removeObserver(pushSubscriptionObserver)
```

***

## Push notifications

### `promptForPushNotifications()`

```swift  theme={null}
OneSignal.promptForPushNotifications()
```

```swift  theme={null}
OneSignal.Notifications.requestPermission()
```

### `postNotification()` \[Dropped]

```swift  theme={null}
OneSignal.postNotification()
```

**User Model**: N/A

### `clearOneSignalNotifications()`

```swift  theme={null}
OneSignal.clearOneSignalNotifications()
```

```swift  theme={null}
OneSignal.Notifications.clearAll()
```

### `disablePush()`

```swift  theme={null}
OneSignal.disablePush(true)
```

```swift  theme={null}
OneSignal.User.pushSubscription.optOut()
```

### `unsubscribeWhenNotificationsAreDisabled()` \[Dropped]

```swift  theme={null}
OneSignal.unsubscribeWhenNotificationsAreDisabled(false)
```

**User Model**: N/A

### `setLaunchURLsInApp()` \[Dropped]

```swift  theme={null}
OneSignal.setLaunchURLsInApp(true)
```

**User Model**: N/A

### `registerForProvisionalAuthorization()`

```swift  theme={null}
OneSignal.registerForProvisionalAuthorization({userResponse in ...})
```

```swift  theme={null}
OneSignal.Notifications.registerForProvisionalAuthorization({ userReponse in ... })
```

### `setNotificationWillShowInForegroundHandler()`

```swift  theme={null}
OneSignal.setNotificationWillShowInForegroundHandler(foregroundHandler)
```

```swift  theme={null}
OneSignal.Notifications.addForegroundLifecycleListener(notificationLifecyleHandler)
```

### `setNotificationOpenedHandler()`

```swift  theme={null}
OneSignal.setNotificationOpenedHandler(notificationOpenHandler)
```

```swift  theme={null}
OneSignal.Notifications.addClickListener(notificationClickListener)
```

### `addPermissionObserver()`

```swift  theme={null}
OneSignal.addPermissionObserver(self as OSPermissionObserver)
```

```swift  theme={null}
OneSignal.Notifications.addPermissionObserver(notificationPermissionObserver)
```

### `removePermissionObserver()`

```swift  theme={null}
OneSignal.removePermissionObserver()
```

```swift  theme={null}
OneSignal.Notifications.removePermissionObserver(notificationPermissionObserver)
```

***

## Live activities

### `enterLiveActivity()`

```swift  theme={null}
OneSignal.enterLiveActivity("my_activity_id", withToken: myToken)
```

```swift  theme={null}
OneSignal.LiveActivities.enter("my_activity_id", withToken: "TOKEN")
```

### `exit()`

```swift  theme={null}
OneSignal.exitLiveActivity("my_activity_id")
```

```swift  theme={null}
OneSignal.LiveActivities.exit("my_activity_id")
```

***

## In-app messages

### `addTrigger()`

```swift  theme={null}
OneSignal.addTrigger("prompt_ios", withValue: "true");
```

```swift  theme={null}
OneSignal.InAppMessages.addTrigger("KEY", withValue: "VALUE")
```

### `addTriggers()`

```swift  theme={null}
OneSignal.addTriggers(["trigger_key_1": "1", "trigger_key_2": "some_other_value"])
```

```swift  theme={null}
OneSignal.InAppMessages.addTriggers(["trigger_key_1": "1", "trigger_key_2": "some_other_value"])
```

### `removeTriggerForKey()`

```swift  theme={null}
OneSignal.removeTriggerForKey("trigger_key_1");
```

```swift  theme={null}
OneSignal.InAppMessages.removeTrigger("trigger_key_1")
```

### `removeTriggerForKeys()`

```swift  theme={null}
OneSignal.removeTriggerForKeys(["trigger_key_1", "trigger_key_2"])
```

```swift  theme={null}
OneSignal.InAppMessages.removeTriggers(["trigger_key_1", "trigger_key_2"])
```

### `getTriggerValueForKey()` \[Dropped]

```swift  theme={null}
OneSignal.getTriggerValueForKey("trigger_key");
```

**User Model**: N/A

### `inAppMessagesArePaused`

```swift  theme={null}
OneSignal.inAppMessagesArePaused = true
```

```swift  theme={null}
OneSignal.InAppMessages.paused = true
```

### `setInAppMessageLifecycleHandler()`

```swift  theme={null}
OneSignal.setInAppMessageLifecycleHandler(handler)
```

```swift  theme={null}
OneSignal.InAppMessages.addLifecycleListener(listener)
```

### `setInAppMessageClickHandler()`

```swift  theme={null}
OneSignal.setInAppMessageClickHandler(clickHandler)
```

```swift  theme={null}
OneSignal.InAppMessages.addClickListener(clickListener)
```

***

## Email

### `setEmail()`

**User Model** [doc](./mobile-sdk-reference#addemail-%2C-removeemail)

```swift  theme={null}
OneSignal.setEmail("email@example.com")
```

```swift  theme={null}
OneSignal.User.addEmail("email@example.com")
```

### `logoutEmail()`

```swift  theme={null}
OneSignal.logoutEmail()
```

```swift  theme={null}
OneSignal.User.removeEmail("email@example.com")
```

***

## SMS

### `setSMSNumber()`

```swift  theme={null}
OneSignal.setSMSNumber("+11234567890")
```

```swift  theme={null}
OneSignal.User.addSms("+11234567890")
```

### `logoutSMSNumber()`

```swift  theme={null}
OneSignal.logoutSMSNumber()
```

```swift  theme={null}
OneSignal.User.removeSms("+11234567890")
```

### `addSMSSubscriptionObserver()` \[Dropped]

```swift  theme={null}
OneSignal.add(subscriptionObserver)
```

**User Model**: N/A

### `getSMSId()` \[Dropped]

```csharp  theme={null}
OneSignal.Default.SMSSubscriptionState.smsUserId
```

**User Model**: N/A

***

## Outcomes

### `sendOutcome()`

```swift  theme={null}
OneSignal.sendOutcome("Purchase")
```

```swift  theme={null}
OneSignal.Session.addOutcome("Purchase")
```

### `sendOutcomeWithValue()`

```swift  theme={null}
OneSignal.sendOutcomeWithValue(withValue: "Purchase", value: 18.76)
```

```swift  theme={null}
OneSignal.Session.addOutcome("Purchase", 18.76)
```

### `sendUniqueOutcome()`

```swift  theme={null}
OneSignal.sendUniqueOutcome("Swipe")
```

```swift  theme={null}
OneSignal.Session.addUniqueOutcome("Swipe")
```

***

Built with [Mintlify](https://mintlify.com).
