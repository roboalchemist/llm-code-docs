# Source: https://docs.instabug.com/references/user-interface-design/set-floating-button-position.md

# Set Floating Button Position

If you're using the floating button as your primary invocation method, you can set a position for it to show up by default.

There are two variables here that can be manipulated:

* `floatingButtonEdge`: Which edge of the screen to show the button
* `floatingButtonTopOffset`: The position of the button on the y-axis

**Edge**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.floatingButtonEdge = .maxXEdge
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.floatingButtonEdge = CGRectMaxXEdge;
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setFloatingButtonEdge(LuciqFloatingButtonEdge.RIGHT);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setFloatingButtonEdge(LuciqFloatingButtonEdge.RIGHT)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.setFloatingButtonEdge(Luciq.floatingButtonEdge.right, 250);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
BugReporting.setFloatingButtonEdge(FloatingButtonEdge.right, 250);
```

{% endtab %}
{% endtabs %}

**Top Offset**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.floatingButtonTopOffset = 48
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.floatingButtonTopOffset = 48;
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setFloatingButtonOffset(50);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setFloatingButtonOffset(50)
```

{% endtab %}
{% endtabs %}
