# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-in-app-surveys/in-app-surveys-callbacks.md

# In-App Surveys Callbacks

### Flows

**When a survey is shown:**

{% code title="Kotlin" %}

```kotlin
scope.launch {
    SurveysKmp.onShow.collect {
        // Survey UI is about to be shown
    }
}
```

{% endcode %}

**When a survey is dismissed:**

{% code title="Kotlin" %}

```kotlin
scope.launch {
    SurveysKmp.onDismiss.collect {
        // Survey UI was dismissed
    }
}
```

{% endcode %}

### Handlers (convenience)

For simple callbacks on the UI thread, you can use handlers instead of collecting the flows:

{% code title="Kotlin" %}

```kotlin
SurveysKmp.setOnShowHandler {
    // Called before survey UI is presented
}
SurveysKmp.setOnDismissHandler {
    // Called after survey UI is dismissed
}
```

{% endcode %}

For more control (e.g. coroutine context), use the `onShow` and `onDismiss` flows.
