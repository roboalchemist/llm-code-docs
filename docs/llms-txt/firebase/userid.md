# Source: https://firebase.google.com/docs/analytics/userid.md.txt

Google Analyticshas a`setUserID`call, which allows you to store a user ID for the individual using your app. This call is optional, and is generally used by organizations that want to useAnalyticsin conjunction with BigQuery to associate analytics data for the same user across multiple apps, multiple devices, or multiple analytics providers.
| **Note:** You are responsible for ensuring that your use of the user ID is in accordance with the[Google AnalyticsTerms of Service](https://www.google.com/analytics/terms/). This includes avoiding the use of impermissible personally identifiable information, and providing appropriate notice of your use of identifiers in your Privacy Policy. Your user ID must not contain information that a third party could use to determine the identity of an individual user. For example, you cannot use a user's email address or social security number as a user ID.

There are many ways you can construct valid user IDs. One approach is to use an identifier you assign and only you can track back to an individual user. For one possible example, consider a hypothetical mobile game developer, AwesomeGameCompany, that has their own internal`AwesomeGameCompanyID`that they create for every user. If it isn't possible for an outside organization to track that`AwesomeGameCompanyID`back to the original user, they might consider using that`AwesomeGameCompanyID`--- or, better yet, a hashed version of`AwesomeGameCompanyID`--- as the user ID value forAnalytics. This would then allow them to calculate values such as a user's total spend across all of their games.

Setting a user ID is never required forAnalyticsto work correctly. If you're only interested in finding events belonging to the same user for the same app on a single device, you can use the`user_pseudo_id`. This value is generated automatically byAnalyticsand is stored within BigQuery for each event.

## Setting the user ID

You can set a user ID with the following method:  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
Analytics.setUserID("123456")
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
[FIRAnalytics setUserID:@"123456"]
```

### Android

```java
mFirebaseAnalytics.setUserId("123456");
```

### Web

```java
import { getAnalytics, setUserId } from "firebase/analytics";

const analytics = getAnalytics();
setUserId(analytics, "123456");
```

### Web

```java
firebase.analytics().setUserId("123456");
```

### Dart

```dart
await FirebaseAnalytics.instance.setUserId(id: '123456');
```

### Unity

```c#
Firebase.Analytics.FirebaseAnalytics.SetUserID("123456");
```

### C++

```c++
analytics::SetUserId("123456");
```

After setting a user ID, all future events will be automatically tagged with this value, and you can access it by querying for the`user_id`value in BigQuery. Adding a user ID will not affect any events previously recorded byGoogle Analytics.

To find out more about accessingAnalyticsdata in BigQuery, please see this[development guide](https://cloud.google.com/solutions/mobile/mobile-firebase-analytics-big-query).