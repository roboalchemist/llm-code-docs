# Source: https://firebase.google.com/docs/reference/js/analytics.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics.md.txt

# Source: https://firebase.google.com/docs/dynamic-links/analytics.md.txt

# Source: https://firebase.google.com/docs/reference/dynamic-links/analytics.md.txt

# Source: https://firebase.google.com/docs/analytics.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics.md.txt

# Source: https://firebase.google.com/docs/analytics.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics.md.txt

# Firebase.Analytics Namespace

# Firebase.Analytics

## Summary

|                                                                                                ### Enumerations                                                                                                ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| [ConsentStatus](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics_1ab87c55ec1a8727fd7a14850f2ad86e8b) | enum The status value of the consent type. |
| [ConsentType](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics_1a9bbaa83c33ea86aec075f5f666fa5935)   | enum The type of consent to set.           |

|                                                                      ### Classes                                                                       ||
|--------------------------------------------------------------------------------------------------------------------------------------|------------------|
| [Firebase.Analytics.FirebaseAnalytics](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics) |                  |
| [Firebase.Analytics.Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter)                  | Event parameter. |

## Enumerations

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