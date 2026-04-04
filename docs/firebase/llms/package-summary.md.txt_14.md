# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/package-summary.md.txt

# com.google.firebase.appdistribution

# com.google.firebase.appdistribution

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` | The release information returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` when a new version is available for the signed in tester. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution` | The Firebase App Distribution API provides methods to update the app to the most recent pre-release build. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/OnProgressListener` | A listener that is called periodically during execution of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` | Represents a progress update or a final state from updating an app. |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` | Represents an asynchronous operation to update an app. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType` | Enum of Android app binary types, used in `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` | Enum for potential error statuses that caused the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel` | An enum specifying the level of interruption of a notification when it is created. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus` | Enum for possible states during Update, used in `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress`. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException` | The class for all Exceptions thrown by `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution`. |