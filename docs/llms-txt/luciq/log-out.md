# Source: https://docs.luciq.ai/references/user-identification-data/log-out.md

# Log Out

In the event of a user logging out or if you want new reports to no longer be associated with a specific user, you can use the log out API.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.logOut()
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[Luciq logOut];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.logoutUser();
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.logoutUser()
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.logOut();
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.logOut();
```

{% endtab %}
{% endtabs %}
