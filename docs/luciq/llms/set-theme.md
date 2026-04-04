# Source: https://docs.luciq.ai/references/user-interface-design/set-theme.md

# Set Theme

By default, the Luciq SDK uses a light theme. This, however, can be changed to use a dark theme. To do this, you can use this API while passing the relevant enum to it.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.setColorTheme(.dark)
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[Luciq setColorTheme:LCQColorThemeDark];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.setColorTheme(LuciqColorTheme.LuciqColorThemeLight);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.setColorTheme(LuciqColorTheme.LuciqColorThemeLight)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.setColorTheme(Luciq.colorTheme.dark);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.setColorTheme(ColorTheme.dark);
```

{% endtab %}
{% endtabs %}

**Theme Parameters:**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//Light
.light
//Dark
.dark
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Light
LCQColorThemeLight
//Dark
LCQColorThemeDark
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Light
LCQColorThemeLight
//Dark
LCQColorThemeDark
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Light
LCQColorThemeLight
//Dark
LCQColorThemeDark
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Light
Luciq.colorTheme.light
//Dark
Luciq.colorTheme.dark
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//Light
ColorTheme.light
//Dark
ColorTheme.dark
```

{% endtab %}
{% endtabs %}
