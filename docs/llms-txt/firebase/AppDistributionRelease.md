# Source: https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistributionRelease.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease.md.txt

# AppDistributionRelease

# AppDistributionRelease


```
public interface AppDistributionRelease
```

<br />

*** ** * ** ***

The release information returned by [checkForNewRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()) when a new version is available for the signed in tester.

## Summary

|                                                                                                    ### Public methods                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[BinaryType](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType) | [getBinaryType](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#getBinaryType())`()` Returns the binary type for this build.                                  |
| `abstract @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                  | [getDisplayVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#getDisplayVersion())`()` Returns the short bundle version of this build (example: 1.0.0). |
| `abstract @`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                | [getReleaseNotes](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#getReleaseNotes())`()` Returns the release notes for this build.                            |
| `abstract long`                                                                                                                                                                                                          | [getVersionCode](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#getVersionCode())`()` Returns the version code of this build (example: 123).                 |

|                                                                                                    ### Extension functions                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `default final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[BinaryType](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType) | [FirebaseAppDistributionKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt)`.`[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component1())`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease)` receiver` `)` Destructuring declaration for [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) to provide binaryType.     |
| `default final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                  | [FirebaseAppDistributionKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt)`.`[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component2())`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease)` receiver` `)` Destructuring declaration for [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) to provide displayVersion. |
| `default final long`                                                                                                                                                                                                          | [FirebaseAppDistributionKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt)`.`[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component3())`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease)` receiver` `)` Destructuring declaration for [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) to provide versionCode.    |
| `default final `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                | [FirebaseAppDistributionKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt)`.`[component4](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component4())`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease)` receiver` `)` Destructuring declaration for [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) to provide releaseNotes.   |

## Public methods

### getBinaryType

```
abstractÂ @NonNull BinaryTypeÂ getBinaryType()
```

Returns the binary type for this build.  

### getDisplayVersion

```
abstractÂ @NonNull StringÂ getDisplayVersion()
```

Returns the short bundle version of this build (example: 1.0.0).  

### getReleaseNotes

```
abstractÂ @Nullable StringÂ getReleaseNotes()
```

Returns the release notes for this build.  

### getVersionCode

```
abstractÂ longÂ getVersionCode()
```

Returns the version code of this build (example: 123).  

## Extension functions

### FirebaseAppDistributionKt.component1

```
defaultÂ finalÂ @NonNull BinaryTypeÂ FirebaseAppDistributionKt.component1(
Â Â Â Â @NonNull AppDistributionReleaseÂ receiver
)
```

Destructuring declaration for [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) to provide binaryType.  

|                                                                                                     Returns                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[BinaryType](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType) | the binaryType of the [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) |

### FirebaseAppDistributionKt.component2

```
defaultÂ finalÂ @NonNull StringÂ FirebaseAppDistributionKt.component2(
Â Â Â Â @NonNull AppDistributionReleaseÂ receiver
)
```

Destructuring declaration for [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) to provide displayVersion.  

|                                                                                    Returns                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | the displayVersion of the [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) |

### FirebaseAppDistributionKt.component3

```
defaultÂ finalÂ longÂ FirebaseAppDistributionKt.component3(
Â Â Â Â @NonNull AppDistributionReleaseÂ receiver
)
```

Destructuring declaration for [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) to provide versionCode.  

| Returns |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the versionCode of the [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) |

### FirebaseAppDistributionKt.component4

```
defaultÂ finalÂ StringÂ FirebaseAppDistributionKt.component4(
Â Â Â Â @NonNull AppDistributionReleaseÂ receiver
)
```

Destructuring declaration for [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) to provide releaseNotes.  

|                                    Returns                                     |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html) | the releaseNotes of the [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) |