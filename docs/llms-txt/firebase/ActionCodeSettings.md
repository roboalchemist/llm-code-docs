# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ActionCodeSettings.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.md.txt

# ActionCodeSettings

# ActionCodeSettings


```
public class ActionCodeSettings implements Parcelable
```

<br />

*** ** * ** ***

Structure that contains the required continue/state URL with optional Android and iOS bundle identifiers. The stateUrl used to initialize this class is the link/deep link/fallback url used while constructing the Firebase dynamic link.

## Summary

|                                                                                                                                       ### Nested types                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public class `[ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder) A Builder class for [ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings). |

|                                                                                                               ### Constants                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `static final `[Parcelable.Creator](https://developer.android.com/reference/android/os/Parcelable.Creator.html)`<`[ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings)`>` | [CREATOR](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#CREATOR()) |

|                                                                            ### Public fields                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `final boolean`                                                                                                                                                          | [androidInstallApp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#androidInstallApp())         |
| `final @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html) | [androidMinimumVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#androidMinimumVersion()) |
| `final `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                          | [androidPackageName](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#androidPackageName())       |
| `final `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                          | [linkDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#linkDomain())                       |
| `final `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                          | [url](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#url())                                     |

|                                                                                                          ### Public methods                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `boolean`                                                                                                                                                                                                                            | [canHandleCodeInApp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#canHandleCodeInApp())`()` Returns whether the out-of-band (OOB) code should be handled by the app.                                                                                                                   |
| `boolean`                                                                                                                                                                                                                            | [getAndroidInstallApp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getAndroidInstallApp())`()` Returns the preference for whether to attempt to install the app if it is not yet installed on the device.                                                                             |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                   | [getAndroidMinimumVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getAndroidMinimumVersion())`()` Returns the minimum version of the app required to open an email link for sign-in.                                                                                             |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                   | [getAndroidPackageName](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getAndroidPackageName())`()` Returns the package name of the installed Android app.                                                                                                                               |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                   | [getIOSBundle](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getIOSBundle())`()` Returns the bundle ID of the installed Apple platforms app.                                                                                                                                            |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                     | [getLinkDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getLinkDomain())`()` Returns the Firebase Hosting domain used to construct the action code link.                                                                                                                          |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                     | [getUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getUrl())`()` Returns the URL.                                                                                                                                                                                                   |
| `static @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder) | [newBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#newBuilder())`()` Returns a new instance of [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder).                                            |
| `void`                                                                                                                                                                                                                               | [writeToParcel](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#writeToParcel(android.os.Parcel,int))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Parcel](https://developer.android.com/reference/android/os/Parcel.html)` out, int flags)` |

|                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `static final int` | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `static final int` | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                         ### Inherited methods                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |----------------|---------------------------------------------------------------------------------------------------------------| | `abstract int` | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()` | |

## Constants

### CREATOR

```
publicÂ staticÂ finalÂ Parcelable.Creator<ActionCodeSettings>Â CREATOR
```  

## Public fields

### androidInstallApp

```
publicÂ finalÂ booleanÂ androidInstallApp
```  

### androidMinimumVersion

```
publicÂ finalÂ @Nullable StringÂ androidMinimumVersion
```  

### androidPackageName

```
publicÂ finalÂ StringÂ androidPackageName
```  

### linkDomain

```
publicÂ finalÂ StringÂ linkDomain
```  

### url

```
publicÂ finalÂ StringÂ url
```  

## Public methods

### canHandleCodeInApp

```
publicÂ booleanÂ canHandleCodeInApp()
```

Returns whether the out-of-band (OOB) code should be handled by the app. See [setHandleCodeInApp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setHandleCodeInApp(boolean)).  

### getAndroidInstallApp

```
publicÂ booleanÂ getAndroidInstallApp()
```

Returns the preference for whether to attempt to install the app if it is not yet installed on the device. See [setAndroidPackageName](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String,boolean,java.lang.String)).  

### getAndroidMinimumVersion

```
publicÂ @Nullable StringÂ getAndroidMinimumVersion()
```

Returns the minimum version of the app required to open an email link for sign-in. If the app version on the device is lower than this version then the user is taken to Google Play Store to upgrade the app. See [setAndroidPackageName](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String,boolean,java.lang.String)).  

### getAndroidPackageName

```
publicÂ @Nullable StringÂ getAndroidPackageName()
```

Returns the package name of the installed Android app. See [setAndroidPackageName](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String,boolean,java.lang.String)).  

### getIOSBundle

```
publicÂ @Nullable StringÂ getIOSBundle()
```

Returns the bundle ID of the installed Apple platforms app. See [setIOSBundleId](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setIOSBundleId(java.lang.String)).  

### getLinkDomain

```
publicÂ @NonNull StringÂ getLinkDomain()
```

Returns the Firebase Hosting domain used to construct the action code link.  

### getUrl

```
publicÂ @NonNull StringÂ getUrl()
```

Returns the URL. See [setUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setUrl(java.lang.String)).  

### newBuilder

```
publicÂ staticÂ @NonNull ActionCodeSettings.BuilderÂ newBuilder()
```

Returns a new instance of [ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder).  

### writeToParcel

```
publicÂ voidÂ writeToParcel(@NonNull ParcelÂ out,Â intÂ flags)
```