# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease.md.txt

# AppDistributionRelease

# AppDistributionRelease


```
public interface AppDistributionRelease
```

<br />

*** ** * ** ***

The release information returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` when a new version is available for the signed in tester.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#getBinaryType()()` Returns the binary type for this build. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#getDisplayVersion()()` Returns the short bundle version of this build (example: 1.0.0). |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#getReleaseNotes()()` Returns the release notes for this build. |
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#getVersionCode()()` Returns the version code of this build (example: 123). |

| ### Extension functions |
|---|---|
| `default final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component1()( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease receiver )` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` to provide binaryType. |
| `default final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component2()( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease receiver )` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` to provide displayVersion. |
| `default final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component3()( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease receiver )` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` to provide versionCode. |
| `default final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component4()( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease receiver )` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` to provide releaseNotes. |

## Public methods

### getBinaryType

```
abstract @NonNull BinaryType getBinaryType()
```

Returns the binary type for this build.

### getDisplayVersion

```
abstract @NonNull String getDisplayVersion()
```

Returns the short bundle version of this build (example: 1.0.0).

### getReleaseNotes

```
abstract @Nullable String getReleaseNotes()
```

Returns the release notes for this build.

### getVersionCode

```
abstract long getVersionCode()
```

Returns the version code of this build (example: 123).

## Extension functions

### FirebaseAppDistributionKt.component1

```
default final @NonNull BinaryType FirebaseAppDistributionKt.component1(
    @NonNull AppDistributionRelease receiver
)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` to provide binaryType.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType` | the binaryType of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` |

### FirebaseAppDistributionKt.component2

```
default final @NonNull String FirebaseAppDistributionKt.component2(
    @NonNull AppDistributionRelease receiver
)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` to provide displayVersion.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the displayVersion of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` |

### FirebaseAppDistributionKt.component3

```
default final long FirebaseAppDistributionKt.component3(
    @NonNull AppDistributionRelease receiver
)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` to provide versionCode.

| Returns |
|---|---|
| `long` | the versionCode of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` |

### FirebaseAppDistributionKt.component4

```
default final String FirebaseAppDistributionKt.component4(
    @NonNull AppDistributionRelease receiver
)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` to provide releaseNotes.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | the releaseNotes of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` |