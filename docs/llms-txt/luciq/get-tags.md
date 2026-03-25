# Source: https://docs.luciq.ai/references/report-data/tags/get-tags.md

# Get Tags

Retrieve the tags attached to the upcoming report using this method. This method returns an array of strings.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
let tags = Luciq.getTags()
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
NSString *tags = [Luciq getTags];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.getTags();
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.getTags();
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.getTags(function (tags) {
  // `tags` is the returned values
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.getTags();
```

{% endtab %}
{% endtabs %}
