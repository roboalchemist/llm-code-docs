# Source: https://docs.instabug.com/references/bug-reporting/take-screenshot-by-media-projection.md

# Take Screenshot by Media Projection

If your application uses any hardware-accelerated views, chances are that the captured screenshots will be blank for these views. In these cases, you can use this API to enable screenshots via media projection. Please note that enabling this will request permission from the users to record the screen at the beginning of the session.

> 🚧 Requires API 21
>
> In order to enable media projection, the minimum support Android SDK version is 21.

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
BugReporting.setScreenshotByMediaProjectionEnabled(true);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setScreenshotByMediaProjectionEnabled(true)
```

{% endtab %}
{% endtabs %}
