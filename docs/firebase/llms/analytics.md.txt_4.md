# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics.md.txt

# Firebase.Analytics Namespace

# Firebase.Analytics

## Summary

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics_1a7e8c38d3a0f973ff75897e87f0def441` | enumThe state of an app in its lifecycle. |
| `https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics_1ab87c55ec1a8727fd7a14850f2ad86e8b` | enumThe status value of the consent type. |
| `https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics_1a9bbaa83c33ea86aec075f5f666fa5935` | enumThe type of consent to set. |

| ### Classes ||
|---|---|
| [Firebase.Analytics.FirebaseAnalytics](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics) |   |
| [Firebase.Analytics.Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter) | Event parameter. |

## Enumerations

### AppLifecycleState

```c#
 AppLifecycleState
```
The state of an app in its lifecycle.

kUnknown is an invalid state that is used to capture uninitialized values. kTermination is used to indicate that the app is about to be terminated.

### ConsentStatus

```c#
 ConsentStatus
```
The status value of the consent type.

Supported statuses are ConsentStatus.Granted and ConsentStatus.Denied.

### ConsentType

```c#
 ConsentType
```
The type of consent to set.

Supported consent types are mapped to corresponding constants in the Android and iOS SDKs. Omitting a type retains its previous status.