# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-crash-reporting/crash-reporting-event-handlers.md

# Crash Reporting Event Handlers

### Before sending a report

This block is executed in the background before sending each report. It can be used for attaching logs and extra data to reports.

{% code title="JavaScript" %}

```javascript
Luciq.onReportSubmitHandler(function () {
    // Attach logs and extra data to reports.
});
```

{% endcode %}

You can also set custom data, such as a user attribute, at any time, including inside event handlers. Logging user events in the event handlers is possible as well.
