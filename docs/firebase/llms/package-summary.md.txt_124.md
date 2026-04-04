# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary.md.txt

# com.google.firebase.appdistribution

# com.google.firebase.appdistribution

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` | The release information returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` when a new version is available for the signed in tester. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution` | The Firebase App Distribution API provides methods to update the app to the most recent pre-release build. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/OnProgressListener` | A listener that is called periodically during execution of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` | Represents a progress update or a final state from updating an app. |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` | Represents an asynchronous operation to update an app. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException` | The class for all Exceptions thrown by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution`. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType` | Enum of Android app binary types, used in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` | Enum for potential error statuses that caused the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel` | An enum specifying the level of interruption of a notification when it is created. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus` | Enum for possible states during Update, used in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress`. |

## Extension functions summary

|---|---|
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary#(com.google.firebase.appdistribution.AppDistributionRelease).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide binaryType. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary#(com.google.firebase.appdistribution.UpdateProgress).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide apkBytesDownloaded. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary#(com.google.firebase.appdistribution.AppDistributionRelease).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide displayVersion. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary#(com.google.firebase.appdistribution.UpdateProgress).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide apkFileTotalBytes. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary#(com.google.firebase.appdistribution.AppDistributionRelease).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide versionCode. |
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary#(com.google.firebase.appdistribution.UpdateProgress).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide updateStatus. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary#(com.google.firebase.appdistribution.AppDistributionRelease).component4()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide releaseNotes. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/package-summary#(com.google.firebase.Firebase).appDistribution()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Extension functions

### component1

```
operator fun AppDistributionRelease.component1(): BinaryType
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide binaryType.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType` | the binaryType of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` |

### component1

```
operator fun UpdateProgress.component1(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide apkBytesDownloaded.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the apkBytesDownloaded of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` |

### component2

```
operator fun AppDistributionRelease.component2(): String
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide displayVersion.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the displayVersion of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` |

### component2

```
operator fun UpdateProgress.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide apkFileTotalBytes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the apkFileTotalBytes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` |

### component3

```
operator fun AppDistributionRelease.component3(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide versionCode.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the versionCode of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` |

### component3

```
operator fun UpdateProgress.component3(): UpdateStatus
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide updateStatus.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus` | the updateStatus of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` |

### component4

```
operator fun AppDistributionRelease.component4(): String?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide releaseNotes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the releaseNotes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` |

## Extension properties

### appDistribution

```
val Firebase.appDistribution: FirebaseAppDistribution
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.