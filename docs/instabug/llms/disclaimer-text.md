# Source: https://docs.instabug.com/references/bug-reporting/disclaimer-text.md

# Disclaimer Text

With the following API, you can add a disclaimer text with hyperlinked text within the bug reporting form, in case you'd like to redirect users to a different page in the event that they click on a specific text. *Example: if you'd like to hyperlink your privacy policy.*

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.setDisclaimerText("Luciq can help developers produce more quality code. [Learn more](https://www.luciq.ai) and [more](http://string-functions.com/length.aspx).")
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQBugReporting setDisclaimerText:@"Luciq can help developers produce more quality code. [Learn more](https://www.luciq.ai) and [more](http://string-functions.com/length.aspx)."];
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setDisclaimerText("Luciq can help developers produce more quality code. [Learn more](https://www.luciq.ai) and [more](http://string-functions.com/length.aspx).");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setDisclaimerText("Luciq can help developers produce more quality code. [Learn more](https://www.luciq.ai) and [more](http://string-functions.com/length.aspx).")
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.setDisclaimerText("Luciq can help developers produce more quality code. [Learn more](https://www.luciq.ai)");
```

{% endtab %}

{% tab title="Flutter" %}

```dart
BugReporting.setDisclaimerText("Luciq can help developers produce more quality code. [Learn more](https://www.luciq.ai) and [more](http://string-functions.com/length.aspx).");
```

{% endtab %}
{% endtabs %}
