# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder.md.txt

# ActionCodeSettings.Builder

# ActionCodeSettings.Builder


```
public class ActionCodeSettings.Builder
```

<br />

*** ** * ** ***

A Builder class for `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings`. Get an instance of this Builder using `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#newBuilder()`.

## Summary

| ### Public fields |
|---|---|
| `https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#dynamicLinkDomain()` **This field is deprecated.** Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. <br /> |
| `https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#linkDomain()` |
| `https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#url()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#build()()` Builds the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` that this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` has constructed. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `[getDynamicLinkDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#getDynamicLinkDomain())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. <br /> |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#getHandleCodeInApp()()` Returns whether the out-of-band (OOB) code should be handled by the app. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#getIOSBundleId()()` Returns the bundle ID of the installed Apple platforms app. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#getLinkDomain()()` Returns the Firebase Hosting domain used to construct the action code link. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#getUrl()()` Returns the URL, which is used as a state/continueURL in the action code link. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String,boolean,java.lang.String)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html androidPackageName, boolean installIfNotAvailable, @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html minimumVersion )` Sets the Android package name and returns the current builder instance. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` | `[setDynamicLinkDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setDynamicLinkDomain(java.lang.String))(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html dynamicLinkDomain)` **This method is deprecated.** Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. <br /> |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setHandleCodeInApp(boolean)(boolean status)` The default is false. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setIOSBundleId(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html iOSBundleId)` To be used if the email link that is sent might be opened on an iOS device. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setLinkDomain(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html customDomain)` Sets the optional Firebase Hosting custom domain, overriding the default Firebase Hosting domain that would be used. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setUrl(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html url)` Sets the URL, which has different meanings in different contexts. |

## Public fields

### dynamicLinkDomain

```
public String dynamicLinkDomain
```

> [!CAUTION]
> **This field is deprecated.**   
>
> Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#linkDomain()` to set a custom domain for mobile links. Learn more in the [Dynamic Links deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq).

### linkDomain

```
public String linkDomain
```

### url

```
public String url
```

## Public methods

### build

```
public @NonNull ActionCodeSettings build()
```

Builds the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` that this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` has constructed.

### getDynamicLinkDomain

```
public @NonNull String [getDynamicLinkDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#getDynamicLinkDomain())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#getLinkDomain()`. Learn more in the [Dynamic Links deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq).

Returns the Firebase Dynamic Links domain used to construct the action code link.

### getHandleCodeInApp

```
public boolean getHandleCodeInApp()
```

Returns whether the out-of-band (OOB) code should be handled by the app. See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setHandleCodeInApp(boolean)`.

### getIOSBundleId

```
public @Nullable String getIOSBundleId()
```

Returns the bundle ID of the installed Apple platforms app. See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setIOSBundleId(java.lang.String)`.

### getLinkDomain

```
public @NonNull String getLinkDomain()
```

Returns the Firebase Hosting domain used to construct the action code link.

### getUrl

```
public @NonNull String getUrl()
```

Returns the URL, which is used as a state/continueURL in the action code link.

### setAndroidPackageName

```
public @NonNull ActionCodeSettings.Builder setAndroidPackageName(
    @NonNull String androidPackageName,
    boolean installIfNotAvailable,
    @Nullable String minimumVersion
)
```

Sets the Android package name and returns the current builder instance. If `
installIfNotAvailable` is set to `true` and the link is opened on an android device, it will try to install the app if not already available. Otherwise the web URL is used.

A minimum version string is also available. If the installed app is an older version, the user is taken to the Play Store to upgrade the app.

### setDynamicLinkDomain

```
public @NonNull ActionCodeSettings.Builder [setDynamicLinkDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setDynamicLinkDomain(java.lang.String))(@NonNull String dynamicLinkDomain)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setLinkDomain(java.lang.String)` to set a custom domain for mobile links. Learn more in the [Dynamic Links deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq).

Sets the optional FDL domain, overriding the default FDL domain that would be used. Must be one of the 5 domains configured in the Firebase console.

### setHandleCodeInApp

```
public @NonNull ActionCodeSettings.Builder setHandleCodeInApp(boolean status)
```

The default is false. When set to true, the action code link will be sent as a universal link and will be open by the app if installed. In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed.

### setIOSBundleId

```
public @NonNull ActionCodeSettings.Builder setIOSBundleId(@Nullable String iOSBundleId)
```

To be used if the email link that is sent might be opened on an iOS device.

Sets the iOS bundle Id and returns the current `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` instance.

### setLinkDomain

```
public @NonNull ActionCodeSettings.Builder setLinkDomain(@NonNull String customDomain)
```

Sets the optional Firebase Hosting custom domain, overriding the default Firebase Hosting domain that would be used.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html customDomain` | A custom domain that has been configured in Firebase Hosting and is owned by the project. This cannot be a default hosting domain (`web.app` or `firebaseapp.com`). |

### setUrl

```
public @NonNull ActionCodeSettings.Builder setUrl(@NonNull String url)
```

Sets the URL, which has different meanings in different contexts. For email actions, this is the state/continue URL. When the app is not installed, this is the web continue URL with any developer provided state appended (the continueURL query parameter). When the app is installed, this is contained in the Firebase dynamic link payload. In the case where the code is sent directly to the app and the app is installed, this is the continueURL query parameter in the dynamic link payload. Otherwise, when the code is handled by the widget itself, it is the payload itself.