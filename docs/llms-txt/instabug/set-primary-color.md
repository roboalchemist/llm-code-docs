# Source: https://docs.instabug.com/references/user-interface-design/set-primary-color.md

# Set Primary Color

This API is used to change the color of both the text and icons to match your app color. You can pass to it any color required.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.tintColor = .lightGray

//Alternatively, you can pass a color in an RGB format
Luciq.tintColor = .init(red: 0, green: 153/255, blue: 1, alpha: 0)
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
Luciq.tintColor = UIColor.lightGrayColor;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.setPrimaryColor(Color.BLUE);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.setPrimaryColor(Color.BLUE)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.setPrimaryColor('#ff0000');
```

{% endtab %}

{% tab title="Flutter" %}

```csharp
Luciq.setPrimaryColor(Color.blue);
```

{% endtab %}
{% endtabs %}
