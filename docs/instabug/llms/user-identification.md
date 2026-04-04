# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/custom-settings/user-identification.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/custom-settings/user-identification.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/custom-settings/user-identification.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/identify-users/user-identification.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/custom-settings/user-identification.md

# User identification

Luciq helps you better identify the bug reports or feedback you get by associating a user's identity to them.

### User Email and Name

If you already have a user's name and email, you can pre-fill the email field in the bug, feedback, and question reporting flow. The user will then be identified in all reports (bugs, improvements, questions), crashes, surveys, and feature requests.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FBbrP2kQjB76E63PlRHil%2Fimage.png?alt=media&#x26;token=2abcd3b1-8382-48b0-b1b5-44146688670d" alt=""><figcaption><p><br><em>An example of a pre-filled email field in the bug reporting form.</em></p></figcaption></figure>

Ideally, this API should be called as soon as a user logs into your app.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.identifyUser(withID: "2374927027", email: "john.appleseed@apple.com", name: "John Appleseed")
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq identifyUserWithID:@"2374927027" email:@"john.appleseed@apple.com" name:@"John Appleseed"];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="warning" %}

### Null Values

If both the email and ID parameters are empty or null, the user will not be identified, and the SDK will through an error.
{% endhint %}

### User Data

You can also add additional data about your users. This API is best used for dumping large amounts of data. Each call to this method overrides the user data to be attached. The maximum length of the string is 1,000 characters.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let profileDetails = user.allProfileDetails()
let profileDetailsString = "\(profileDetails)"
Luciq.userData = profileDetailsString
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSDictionary *profileDetails = [user allProfileDetails];
NSString *profileDetailsString = [NSString stringWithFormat:@"%@", profileDetails];
Luciq.userData = profileDetailsString;
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Logout

When a user logs out, the following API should be called. Calling `logOut` will reset the value of the email and name previously set. It will also remove any currently set user attributes, user events, user chats, and user data.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.logOut()
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq logOut];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="warning" %}

### Logout only when user is identified

Please note that if the user is currently not identified using the `identifyUser` API, the `logOut` method will have no effect.
{% endhint %}
