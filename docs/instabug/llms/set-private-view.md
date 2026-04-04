# Source: https://docs.instabug.com/references/bug-reporting/set-private-view.md

# Set Private View

You can use this API to set any particular view as private so that it is always hidden in screenshots.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
view.luciq_privateView = true
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
view.luciq_privateView = YES;
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Should be added in the activity with the view, takes any number of views
Luciq.addPrivateViews(view1, view2, view3);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Should be added in the activity with the view, takes any number of views
Luciq.addPrivateViews(view1, view2, view3)
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Add the following tag to the view you'd like to hide
<Text ref={c => this.textView = c} style={styles.welcome}>This is a private view!</Text>

//Then call the following API
Luciq.setPrivateView(this.textView);
```

{% endtab %}
{% endtabs %}

You can also remove a view from the list of private views using this API.

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
//Should be added in the activity with the view, takes any number of views
Luciq.removePrivateViews(view1, view2, view3);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Should be added in the activity with the view, takes any number of views
Luciq.removePrivateViews(view1, view2, view3)
```

{% endtab %}
{% endtabs %}
