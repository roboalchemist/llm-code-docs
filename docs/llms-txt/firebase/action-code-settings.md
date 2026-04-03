# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings.md.txt

# FirebaseAdmin.Auth.ActionCodeSettings Class Reference

# FirebaseAdmin.Auth.ActionCodeSettings

Defines the required continue/state URL with optional Android and iOS settings.

## Summary

Used when invoking the email action link generation APIs in [FirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth#class_firebase_admin_1_1_auth_1_1_firebase_auth).

|                                                                                                                                                                                                      ### Properties                                                                                                                                                                                                      ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AndroidInstallApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings_1a049296dd40c0c6dd0d7c2c7bca3c31b2)     | `bool` Gets or sets a value indicating whether to install the Android app if the device supports it and the app is not already installed.                                                     |
| [AndroidMinimumVersion](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings_1ac421e9f8beae0137ecedb15c512c7aca) | `string` Gets or sets the minimum version for the Android app.                                                                                                                                |
| [AndroidPackageName](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings_1a15382173bd1df2fd2b40891ea6a4ea98)    | `string` Gets or sets the Android package name of the app where the link should be handled if the Android app is installed.                                                                   |
| [DynamicLinkDomain](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings_1a474449d9aa9bcd9f2fea21166cbad8ff)     | `string` Gets or sets the dynamic link domain to use for the current link if it is to be opened using Firebase Dynamic Links, as multiple dynamic link domains can be configured per project. |
| [HandleCodeInApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings_1aa386758bbb695dcf5b2da829d08f5c57)       | `bool` Gets or sets a value indicating whether to open the link via a mobile app or a browser.                                                                                                |
| [IosBundleId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings_1a179139d6b0c51b34542c91da38329b6b)           | `string` Gets or sets the bundle ID of the iOS app where the link should be handled if the application is already installed on the device.                                                    |
| [LinkDomain](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings_1a2811a51065d5204ab235b970ab572316)            | `string` Gets or sets the hosting link domain to use for the current link if it is to be opened using `handleCodeInApp`, as multiple hosting link domains can be configured per project.      |
| [Url](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/action-code-settings#class_firebase_admin_1_1_auth_1_1_action_code_settings_1a558e06b2990b2c3fc1ccb972f03e87cd)                   | `string` Gets or sets the continue/state URL.                                                                                                                                                 |

## Properties

### AndroidInstallApp

```text
bool AndroidInstallApp
```  
Gets or sets a value indicating whether to install the Android app if the device supports it and the app is not already installed.  

### AndroidMinimumVersion

```text
string AndroidMinimumVersion
```  
Gets or sets the minimum version for the Android app.

If the installed app is an older version, the user is taken to the Play Store to upgrade the app.  

### AndroidPackageName

```text
string AndroidPackageName
```  
Gets or sets the Android package name of the app where the link should be handled if the Android app is installed.

Must be specified when setting other Android-specific settings.  

### DynamicLinkDomain

```text
string DynamicLinkDomain
```  
Gets or sets the dynamic link domain to use for the current link if it is to be opened using Firebase Dynamic Links, as multiple dynamic link domains can be configured per project.

This setting provides the ability to explicitly choose one. If none is provided, the oldest domain is used by default.  

### HandleCodeInApp

```text
bool HandleCodeInApp
```  
Gets or sets a value indicating whether to open the link via a mobile app or a browser.

The default is false. When set to true, the action code link is sent as a Universal Link or an Android App Link and is opened by the app if installed. In the false case, the code is sent to the web widget first and then redirects to the app if installed.  

### IosBundleId

```text
string IosBundleId
```  
Gets or sets the bundle ID of the iOS app where the link should be handled if the application is already installed on the device.  

### LinkDomain

```text
string LinkDomain
```  
Gets or sets the hosting link domain to use for the current link if it is to be opened using `handleCodeInApp`, as multiple hosting link domains can be configured per project.

This setting provides the ability to explicitly choose one. If none is provided, the default hosting domain is used.  

### Url

```text
string Url
```  
Gets or sets the continue/state URL.

This property has different meanings in different contexts.

- When the link is handled in the web action widgets, this is the deep link in the `continueUrl` query parameter.
- When the link is handled in the app directly, this is the `continueUrl` query parameter in the deep link of the Dynamic Link.

This property is required.

<br />