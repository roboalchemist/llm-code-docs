# Source: https://docs.instabug.com/references/user-identification-data/user-data.md

# User Data

User data is used to add chunks of information to a user so that it's sent to the dashboard with the reports. Each call to this API overwrites the previous data added. This method takes a string argument.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
let profileDetails = user.allProfileDetails()
let profileDetailsString = "\(profileDetails)"
Luciq.userData = profileDetailsString
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
NSDictionary *profileDetails = [user allProfileDetails];
NSString *profileDetailsString = [NSString stringWithFormat:@"%@", profileDetails];
Luciq.userData = profileDetailsString;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.setUserData("User data");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.setUserData("User data")
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.setUserData("User data sample");
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.setUserData("User data sample");
```

{% endtab %}
{% endtabs %}
