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

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` A Builder class for `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings`. |

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#CREATOR()` |

| ### Public fields |
|---|---|
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#androidInstallApp()` |
| `final @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#androidMinimumVersion()` |
| `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#androidPackageName()` |
| `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#linkDomain()` |
| `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#url()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#canHandleCodeInApp()()` Returns whether the out-of-band (OOB) code should be handled by the app. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getAndroidInstallApp()()` Returns the preference for whether to attempt to install the app if it is not yet installed on the device. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getAndroidMinimumVersion()()` Returns the minimum version of the app required to open an email link for sign-in. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getAndroidPackageName()()` Returns the package name of the installed Android app. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getIOSBundle()()` Returns the bundle ID of the installed Apple platforms app. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getLinkDomain()()` Returns the Firebase Hosting domain used to construct the action code link. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#getUrl()()` Returns the URL. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder`. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings#writeToParcel(android.os.Parcel,int)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/os/Parcel.html out, int flags)` |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
public static final Parcelable.Creator<ActionCodeSettings> CREATOR
```

## Public fields

### androidInstallApp

```
public final boolean androidInstallApp
```

### androidMinimumVersion

```
public final @Nullable String androidMinimumVersion
```

### androidPackageName

```
public final String androidPackageName
```

### linkDomain

```
public final String linkDomain
```

### url

```
public final String url
```

## Public methods

### canHandleCodeInApp

```
public boolean canHandleCodeInApp()
```

Returns whether the out-of-band (OOB) code should be handled by the app. See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setHandleCodeInApp(boolean)`.

### getAndroidInstallApp

```
public boolean getAndroidInstallApp()
```

Returns the preference for whether to attempt to install the app if it is not yet installed on the device. See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String,boolean,java.lang.String)`.

### getAndroidMinimumVersion

```
public @Nullable String getAndroidMinimumVersion()
```

Returns the minimum version of the app required to open an email link for sign-in. If the app version on the device is lower than this version then the user is taken to Google Play Store to upgrade the app. See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String,boolean,java.lang.String)`.

### getAndroidPackageName

```
public @Nullable String getAndroidPackageName()
```

Returns the package name of the installed Android app. See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setAndroidPackageName(java.lang.String,boolean,java.lang.String)`.

### getIOSBundle

```
public @Nullable String getIOSBundle()
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

Returns the URL. See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder#setUrl(java.lang.String)`.

### newBuilder

```
public static @NonNull ActionCodeSettings.Builder newBuilder()
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder`.

### writeToParcel

```
public void writeToParcel(@NonNull Parcel out, int flags)
```