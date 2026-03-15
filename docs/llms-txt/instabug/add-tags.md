# Source: https://docs.instabug.com/references/report-data/tags/add-tags.md

# Add Tags

To add a tag to the upcoming report, you can use this method and pass to it any number of strings, each denoting a unique tag.

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.appendTags(["Design", "Flow"])
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[Luciq appendTags:@[@"Design", @"Flow"]];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.addTags("Tag one", "Tag two", "Tag three");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.addTags("Tag one", "Tag two", "Tag three");
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.appendTags(["Tag 1", "Tag 2"]);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.appendTags(["Tag 1", "Tag 2"]);
```

{% endtab %}
{% endtabs %}
