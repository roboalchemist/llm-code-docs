# Source: https://documentation.onesignal.com/docs/en/device-user-model-web-sdk-mapping.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web SDK Mapping

> Compare OneSignal Web SDK methods between the legacy Player Model and the new User Model. Learn how to migrate your implementation with TypeScript-based code examples and updated method references.

<Warning>
  OneSignal has updated from a device-centric model (Player ID) to a user-centric model (OneSignal ID). For migration guidance, refer to the [User Model Migration Guide](./user-model-migration-guide).

  For documentation on legacy device-centric implementations, see [Version 9](/v9.0/docs/web-push-sdk).
</Warning>

## Overview

This document maps the methods, properties, and events from OneSignal's legacy **Player Model Web SDK** to the newer **User Model** SDK. Each section includes matching TypeScript code examples, clearly demonstrating how to update your integration.

All examples are simplified for demonstration purposes. For complete and up-to-date implementations, refer to the documentation links provided under each method or event.

## OneSignal Service Worker

Update the import in your `OneSignalSDKWorker.js` file:

**Player Model:**

```javascript  theme={null}
importScripts('https://cdn.onesignal.com/sdks/OneSignalSDKWorker.js');
```

**User Model:**

```javascript  theme={null}
importScripts("https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.sw.js");
```

Keep the file path the same. Just update the `importScripts` URL.

See [OneSignal Service Worker](./onesignal-service-worker) for more information.

## Initialization

### `init()`

**Player Model:** [Docs](/v9.0/docs/web-push-sdk)

```html  theme={null}
<script src="https://cdn.onesignal.com/sdks/OneSignalSDK.js" async></script>
<script>
window.OneSignal = window.OneSignal || [];
OneSignal.push(function() {
  OneSignal.init({
    appId: "YOUR_APP_ID"
  });
});
</script>
```

**User Model:** [Docs](./mobile-sdk-reference#initialize)

```html  theme={null}
<script src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js" defer></script>
<script>
window.OneSignalDeferred = window.OneSignalDeferred || [];
OneSignalDeferred.push(async function(OneSignal) {
  await OneSignal.init({
    appId: "YOUR_APP_ID",
  });
});
</script>
```

### `provideUserConsent()`

**Player Model:** [Docs](/v9.0/docs/web-push-sdk)

```typescript  theme={null}
OneSignal.provideUserConsent(true)
```

**User Model:** [Docs](./mobile-sdk-reference#setconsentgiven)

```typescript  theme={null}
OneSignal.setConsentGiven(true)
```

## Registering for push

### `showNativePrompt()`

**Player Model:**

```typescript  theme={null}
OneSignal.showNativePrompt()
```

**User Model:** [Docs](./mobile-sdk-reference#requestpermission-fallbacktosettings-push)

```typescript  theme={null}
OneSignal.Notifications.requestPermission()
```

### `registerForPushNotifications()` — Dropped in User Model

```typescript  theme={null}
OneSignal.registerForPushNotifications()
```

### `#permissionPromptDisplay`

**Player Model:**

```typescript  theme={null}
OneSignal.on('permissionPromptDisplay', () => ...)
```

**User Model:** [Docs](./web-sdk-reference#addeventlistener-push-notification)

```typescript  theme={null}
OneSignal.Notifications.addEventListener('permissionPromptDisplay', event => { ... })
```

### `showSlidedownPrompt()`

**Player Model:**

```typescript  theme={null}
OneSignal.showSlidedownPrompt()
```

**User Model:** [Docs](./web-sdk-reference#promptpush)

```typescript  theme={null}
OneSignal.Slidedown.promptPush()
```

### `showHttpPrompt()` — Dropped in User Model

```typescript  theme={null}
OneSignal.showHttpPrompt()
```

### `showCategorySlidedown()`

**Player Model:**

```typescript  theme={null}
OneSignal.showCategorySlidedown()
```

**User Model:** [Docs](./web-sdk-reference#promptpushcategories)

```typescript  theme={null}
OneSignal.Slidedown.promptPushCategories()
```

### `#getNotificationPermission`

**Player Model:**

```typescript  theme={null}
OneSignal.on('getNotificationPermission', (permission) => ...)
```

**User Model:** [Docs](./web-sdk-reference#addeventlistener-push-subscription)

```typescript  theme={null}
OneSignal.User.PushSubscription.addEventListener('change', ({ optedIn }) => { ... })
```

### `isPushNotificationsSupported()`

**Player Model:**

```typescript  theme={null}
OneSignal.isPushNotificationsSupported()
```

**User Model:** [Docs](./web-sdk-reference#ispushsupported)

```typescript  theme={null}
OneSignal.Notifications.isPushSupported()
```

### `isPushNotificationsEnabled()`

**Player Model:**

```typescript  theme={null}
await OneSignal.isPushNotificationsEnabled()
```

**User Model:** [Docs](./web-sdk-reference#optedin)

```typescript  theme={null}
OneSignal.User.PushSubscription.optedIn
```

### `#subscriptionChange`

**Player Model:**

```typescript  theme={null}
OneSignal.on('subscriptionChange', (subscribed) => ...)
```

**User Model:**

```typescript  theme={null}
OneSignal.User.PushSubscription.addEventListener('change', ({ token }) => { ... })
```

## Analytics

### `#notificationPermissionChange`

**Player Model:**

```typescript  theme={null}
OneSignal.on('notificationPermissionChange', ({ to }) => ...)
```

**User Model:** [Docs](./web-sdk-reference#permissionchange)

```typescript  theme={null}
OneSignal.Notifications.addEventListener('permissionChange', permission => { ... })
```

### `#popoverShown`

**Player Model:**

```typescript  theme={null}
OneSignal.on('popoverShown', () => ...)
```

**User Model:** [Docs](./web-sdk-reference#addeventlistener-slidedown)

```typescript  theme={null}
OneSignal.Slidedown.addEventListener('slidedownShown', presented => { ... })
```

### `#customPromptClick`

**Player Model:**

```typescript  theme={null}
OneSignal.on('customPromptClick', ({ result }) => ...)
```

**User Model:** [Docs](./web-sdk-reference#click)

```typescript  theme={null}
OneSignal.Notifications.addEventListener('click', ({notification, result}) => { ... })
```

## User IDs

### `getUserId()`

**Player Model:**

```typescript  theme={null}
OneSignal.getUserId()
```

**User Model:** [Docs](./web-sdk-reference#id)

```typescript  theme={null}
OneSignal.User.PushSubscription.id;
```

### `setExternalUserId()`

**Player Model:** [Docs](./users)

```typescript  theme={null}
OneSignal.setExternalUserId("external id")
```

**User Model:** [Docs](./web-sdk-reference#login-external-id)

```typescript  theme={null}
OneSignal.login("external id")
```

### `removeExternalUserId()`

**Player Model:**

```typescript  theme={null}
OneSignal.removeExternalUserId()
```

**User Model:** [Docs](./web-sdk-reference#logout)

```typescript  theme={null}
OneSignal.logout()
```

### `getExternalUserId()`

**Player Model:**

```typescript  theme={null}
await OneSignal.getExternalUserId()
```

**User Model:** [Docs](./web-sdk-reference#externalid)

```typescript  theme={null}
OneSignal.User.externalId
```

## Tags

### `sendTag()`

**Player Model:**

```typescript  theme={null}
OneSignal.sendTag("key", "value")
```

**User Model:**

```typescript  theme={null}
OneSignal.User.addTag("key", "value")
```

**User Model** [doc](./web-sdk-reference#addtag-%2C-addtags)

### `sendTags()`

**Player Model:**

```typescript  theme={null}
OneSignal.sendTags({ key1: 'value1', key2: 'value2' })
```

**User Model:**

```typescript  theme={null}
OneSignal.User.addTags({ key1: 'value1', key2: 'value2' })
```

### `getTags()`

**Player Model:**

```typescript  theme={null}
await OneSignal.getTags()
```

**User Model:**

```typescript  theme={null}
OneSignal.User.getTags()
```

### `deleteTag()`

**Player Model:**

```typescript  theme={null}
OneSignal.deleteTag("key")
```

**User Model:**

```typescript  theme={null}
OneSignal.User.removeTag("key")
```

### `deleteTags()`

**Player Model:**

```typescript  theme={null}
OneSignal.deleteTags(["key1", "key2"])
```

**User Model:**

```typescript  theme={null}
OneSignal.User.removeTags(["key1", "key2"])
```

## Push Notifications

### `sendSelfNotification()` — Dropped in User Model

```typescript  theme={null}
OneSignal.sendSelfNotification('title', 'message', 'url')
```

### `setSubscription()`

**Player Model:**

```typescript  theme={null}
OneSignal.setSubscription(false)
```

**User Model:**

```typescript  theme={null}
OneSignal.Notifications.permission = false
```

## Receiving Notifications

### `#notificationDisplay`

**Player Model:**

```typescript  theme={null}
OneSignal.on('notificationDisplay', (event) => { ... })
```

**User Model:**

```typescript  theme={null}
OneSignal.Notifications.addEventListener('foregroundWillDisplay', ({ notification }) => { ... })
```

### `#notificationDismiss`

**Player Model:**

```typescript  theme={null}
OneSignal.on('notificationDismiss', (event) => { ... })
```

**User Model:**

```typescript  theme={null}
OneSignal.Notifications.addEventListener('dismiss', ({ notification }) => { ... })
```

### `#addListenerForNotificationOpened`

**Player Model:**

```typescript  theme={null}
OneSignal.on('addListenerForNotificationOpened', (event) => { ... })
```

## Email

### `setEmail()`

**User Model** [doc](./web-sdk-reference#addemail-%2C-removeemail)

**Player Model:**

```typescript  theme={null}
OneSignal.setEmail('email@example.com')
```

**User Model:**

```typescript  theme={null}
OneSignal.User.addEmail('email@example.com')
```

### `logoutEmail()`

**Player Model:**

```typescript  theme={null}
OneSignal.logoutEmail()
```

**User Model:**

```typescript  theme={null}
OneSignal.User.removeEmail('email@example.com')
```

### `getEmailId()` — Dropped in User Model

## SMS

### `setSMSNumber()`

**Player Model:**

```typescript  theme={null}
OneSignal.setSMSNumber('+11234567890')
```

**User Model:**

```typescript  theme={null}
OneSignal.User.addSms('+11234567890')
```

### `logoutSMSNumber()`

**Player Model:**

```typescript  theme={null}
OneSignal.logoutSMS()
```

**User Model:**

```typescript  theme={null}
OneSignal.User.removeSms('+11234567890')
```

***

Built with [Mintlify](https://mintlify.com).
