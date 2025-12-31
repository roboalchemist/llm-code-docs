# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder.md.txt

# ActionCodeSettings.Builder

public static final class **ActionCodeSettings.Builder** extends Object  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#build())() Builds a new [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings).                                                                                                                                              |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) | [setAndroidInstallApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidInstallApp(boolean))(boolean androidInstallApp) Specifies whether to install the Android app if the device supports it and the app is not already installed.                                                                                                                   |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) | [setAndroidMinimumVersion](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidMinimumVersion(java.lang.String))(String androidMinimumVersion) Sets the minimum version for Android app.                                                                                                                                                                  |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) | [setAndroidPackageName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String))(String androidPackageName) Sets the Android package name of the app where the link should be handled if the Android app is installed.                                                                                                          |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) | [setDynamicLinkDomain](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setDynamicLinkDomain(java.lang.String))(String dynamicLinkDomain) *This method is deprecated. Use [setLinkDomain(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setLinkDomain(java.lang.String)) instead.* |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) | [setHandleCodeInApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setHandleCodeInApp(boolean))(boolean handleCodeInApp) Specifies whether to open the link via a mobile app or a browser.                                                                                                                                                                    |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) | [setIosBundleId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setIosBundleId(java.lang.String))(String iosBundleId) Sets the bundle ID of the iOS app where the link should be handled if the application is already installed on the device.                                                                                                                |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) | [setLinkDomain](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setLinkDomain(java.lang.String))(String linkDomain) Sets the link domain to use for the current link if it is to be opened using `handleCodeInApp`, as multiple link domains can be configured per project.                                                                                     |
| [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder) | [setUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setUrl(java.lang.String))(String url) Sets the link continue/state URL.                                                                                                                                                                                                                                |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Methods

#### public [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings)
**build**
()

Builds a new [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings).  

##### Returns

- A non-null [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings).  

#### public [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder)
**setAndroidInstallApp**
(boolean androidInstallApp)

Specifies whether to install the Android app if the device supports it and the app is not
already installed.  

##### Parameters

| androidInstallApp | true to install the app, and false otherwise. |
|-------------------|-----------------------------------------------|

##### Returns

- This builder.  

#### public [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder)
**setAndroidMinimumVersion**
(String androidMinimumVersion)

Sets the minimum version for Android app. If the installed app is an older version, the user
is taken to the Play Store to upgrade the app.  

##### Parameters

| androidMinimumVersion | Minimum version string. |
|-----------------------|-------------------------|

##### Returns

- This builder.  

#### public [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder)
**setAndroidPackageName**
(String androidPackageName)

Sets the Android package name of the app where the link should be handled if the
Android app is installed. Must be specified when setting other Android-specific settings.  

##### Parameters

| androidPackageName | Package name string. Must be specified, and must not be null or empty. |
|--------------------|------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder)
**setDynamicLinkDomain**
(String dynamicLinkDomain)


**This method is deprecated.**   
Use [setLinkDomain(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder#setLinkDomain(java.lang.String)) instead.

Sets the dynamic link domain to use for the current link if it is to be opened using
Firebase Dynamic Links, as multiple dynamic link domains can be configured per project. This
setting provides the ability to explicitly choose one. If none is provided, the oldest
domain is used by default.  

##### Parameters

| dynamicLinkDomain | Firebase Dynamic Link domain string. |
|-------------------|--------------------------------------|

##### Returns

- This builder.  

#### public [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder)
**setHandleCodeInApp**
(boolean handleCodeInApp)

Specifies whether to open the link via a mobile app or a browser. The default is false.
When set to true, the action code link is sent as a Universal Link or an Android App Link
and is opened by the app if installed. In the false case, the code is sent to the web widget
first and then redirects to the app if installed.  

##### Parameters

| handleCodeInApp | true to open the link in the app, and false otherwise. |
|-----------------|--------------------------------------------------------|

##### Returns

- This builder.  

#### public [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder)
**setIosBundleId**
(String iosBundleId)

Sets the bundle ID of the iOS app where the link should be handled if the
application is already installed on the device.  

##### Parameters

| iosBundleId | The iOS bundle ID string. |
|-------------|---------------------------|

#### public [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder)
**setLinkDomain**
(String linkDomain)

Sets the link domain to use for the current link if it is to be opened using
`handleCodeInApp`, as multiple link domains can be configured per project. This
setting provides the ability to explicitly choose one. If none is provided, the default
Firebase Hosting domain will be used.  

##### Parameters

| linkDomain | Link domain string. |
|------------|---------------------|

##### Returns

- This builder.  

#### public [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.Builder)
**setUrl**
(String url)

Sets the link continue/state URL.

This parameter has different meanings in different contexts:

- When the link is handled in the web action widgets, this is the deep link in the `continueUrl` query parameter.
- When the link is handled in the app directly, this is the `continueUrl` query parameter in the deep link of the Dynamic Link.

This parameter must be specified when creating a new [ActionCodeSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings) instance.  

##### Parameters

| url | Continue/state URL string. |
|-----|----------------------------|

##### Returns

- This builder.