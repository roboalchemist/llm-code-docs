# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-in-app-surveys/in-app-surveys-event-handlers.md

# In-App Surveys Event Handlers

You can execute code in a handler that gets called before a survey is shown and after it has been dismissed. You can use this for things like pausing and resuming a game, for example.

## Before showing the survey

Use `Surveys.setOnShowHandler` to run code right before the survey appears.

{% code title="JavaScript" %}

```javascript
Surveys.setOnShowHandler(() => {
  // Perform any changes before the survey appears.
});
```

{% endcode %}

## After the survey has been dismissed

Use `Surveys.setOnDismissHandler` to run code when the survey is dismissed.

{% code title="JavaScript" %}

```javascript
Surveys.setOnDismissHandler(() => {
  // Perform any changes before the survey disappears.
});
```

{% endcode %}
