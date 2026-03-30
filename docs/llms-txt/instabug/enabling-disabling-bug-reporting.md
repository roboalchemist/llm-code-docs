# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-bug-reporting/enabling-disabling-bug-reporting.md

# Enabling/Disabling Bug Reporting

When your users [invoke the SDK](https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-bug-reporting/broken-reference), a popup appears with default [Prompt Options](https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-bug-reporting/broken-reference) for them to "Report a bug" (submit a bug), "Suggest an improvement" (send you feedback), or "Ask a question" (send you a chat).

These options can be disabled or enabled separately. When only a single option is enabled, it becomes the default [invocation mode](https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-bug-reporting/broken-reference) and the Prompt Options menu doesn't appear.

The below API completely disables all forms of bug, improvement, and question reports.

{% code title="JavaScript" %}

```javascript
BugReporting.setEnabled(false);
```

{% endcode %}

You can also specify whether to show any of the Report a bug, Suggest an improvement, Ask a question options, or all using this API:

{% code title="JavaScript" overflow="wrap" %}

```javascript
import { ReportType } from '@luciq/react-native';

BugReporting.setReportTypes([ReportType.bug, ReportType.feedback, ReportType.question]);
```

{% endcode %}

By default, all three options are enabled if they are available in your current subscription plan.

Updated 8 days ago
