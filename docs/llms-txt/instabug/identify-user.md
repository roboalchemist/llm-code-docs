# Source: https://docs.instabug.com/references/user-identification-data/identify-user.md

# Identify User

This API is primarily used to identify your user, sort of like a log in kind of method. The API takes two strings, the user's email being the first, and the user's name for the second.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.identifyUser(withID: "1", email: "john.appleseed@apple.com", name: "John Appleseed")
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[Luciq identifyUserWithID:@"1" email:@"john.appleseed@apple.com" name:@"John Appleseed"];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.identifyUser("user name", "email");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.identifyUser("user name", "email")
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.identifyUser("john.appleseed@apple.com", "John Appleseed");
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.identifyUserWithEmail(String email, [String name]);
```

{% endtab %}
{% endtabs %}

{% hint style="danger" %}

#### IMPORTANT:  `userID` Must Be Unique

The `userID` you provide is the primary identifier for a user within the Luciq. You **must** ensure that this ID is unique for each of your users.

Providing a generic, non-unique ID (e.g., "`guest`" or "`unknown_user`") for multiple users will cause their data to be incorrectly merged. This will lead to critical data integrity and privacy issues, such as **different users being able to see and reply to each other's private chat conversations**.

If a user is anonymous, **do not call** the `identifyUser` API. The SDK will automatically handle a unique anonymous identity for you.
{% endhint %}
