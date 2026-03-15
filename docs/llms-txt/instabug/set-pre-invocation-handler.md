# Source: https://docs.instabug.com/references/sdk-event-handlers/set-pre-invocation-handler.md

# Set Pre-Invocation Handler

Use this handler to run any code prior to Luciq being invoked.

This block is executed on the UI thread and could be used for performing any UI changes before the SDK's UI is shown.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.willInvokeHandler = {
    someObject.setSomeState()
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.willInvokeHandler = ^{
    [someObject setSomeState];
};
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setOnInvokeCallback(new OnInvokeCallback() {
            @Override
            public void onInvoke() {
               //do something
            }
});
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setOnInvokeCallback {
                     //do something
        }
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.onInvokeHandler(function () {
    // Perform any UI changes before the SDK's UI is shown.
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
BugReporting.setOnInvokeCallback(Function function);
```

{% endtab %}
{% endtabs %}
