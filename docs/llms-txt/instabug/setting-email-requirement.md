# Source: https://docs.instabug.com/references/in-app-feature-requests/setting-email-requirement.md

# Setting Email Requirement

When a user creates a new feature request or adds a comment, they are asked to enter their email. You can use this method to set whether this email is required or not. This method takes a boolean for its first argument (whether the requirement is true or false) and enums for the second argument (for comment or new feature). More than one enum can be passed.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
FeatureRequests.setEmailFieldRequired(true, for: [.requestNewFeature, .addCommentToFeature])
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQFeatureRequests setEmailFieldRequired:YES forAction: LCQActionRequestNewFeature | LCQActionAddCommentToFeature]
```

{% endtab %}

{% tab title="And - Java" %}

```java
FeatureRequests.setEmailFieldRequired(boolean, ActionType.REQUEST_NEW_FEATURE);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
FeatureRequests.setEmailFieldRequired(boolean, ActionType.REQUEST_NEW_FEATURE)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Import Luciq, { ActionType } from '@luciq/react-native';

//The first field determines whether the email field is required or not
//The second field is for whether this is for adding comments, for requesting new features, or both
FeatureRequests.setEmailFieldRequired(true, [ActionType.requestNewFeature]);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
FeatureRequests.setEmailFieldRequired(false, [ActionType.requestNewFeature]);
```

{% endtab %}
{% endtabs %}

**Email Parameters:**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//New Feature
.requestNewFeature
//New Comment
.addCommentToFeature
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//New Feature
LCQActionRequestNewFeature
//New Comment
LCQActionAddCommentToFeature
```

{% endtab %}

{% tab title="And - Java" %}

```java
//New Feature
ActionType.REQUEST_NEW_FEATURE 
//New Comment
ActionType.ADD_COMMENT_TO_FEATURE
```

{% endtab %}

{% tab title="RN" %}

```csharp
//New Feature
ActionType.requestNewFeature
//New Comment
ActionType.addCommentToFeature
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//New Feature
ActionType.requestNewFeature
//New Comment
ActionType.addCommentToFeature
```

{% endtab %}
{% endtabs %}
