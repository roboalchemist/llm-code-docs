# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/automation-and-workflows/alerts-and-rules/predefined-alerts.md

# Predefined Alerts

Luciq creates predefined alerts for a few of the metrics that the SDK measures. These alerts are automatically enabled upon creating a new app environment and aim to give you a head start to creating your own. By default, notifications for these alerts are sent via email but this can be customizable to your preferred alerting channel like Slack or Microsoft Teams.

### Crash Free Rates

Predefined alerts are set for both the crash-free sessions and crash-free users metrics. These alerts notify you when either the crash-free sessions or crash-free users percentages drop below 99. Notifications for those alerts will be sent via email to all users on the dashboard. The alerts are refined to only the latest and top releases of your app to avoid spamming.

<figure><img src="https://files.readme.io/e8393f6-CFS2.png" alt="Crash-free sessions predefined alert"><figcaption><p><em>Crash-free sessions predefined alert</em></p></figcaption></figure>

### Crash Reporting

A default crash reporting alert is created that checks if a crash is affecting 1% of total sessions in the last 24 hours for any of the latest or top releases. When triggered, an email is sent to all users on the dashboard.

<figure><img src="https://files.readme.io/f73dafa-1percent2.png" alt="Predefined alert for a crash affecting 1% of sessions"><figcaption><p><em>Predefined alert for a crash affecting 1% of sessions</em></p></figcaption></figure>

Setting a dynamic threshold using a percentage rather than an absolute session count accounts for variations in different app sizes and user traffic fluctuations.

### Rollout Management

Luciq creates an alert to keep your dashboard admins and owners up to date on any changes that happen to the rollout status of active releases.

<figure><img src="https://files.readme.io/4cd2a65-rollout2.png" alt="Rollout status change predefined alert"><figcaption><p><em>Rollout status change predefined alert</em></p></figcaption></figure>

### Performance Metrics

Recommended alerts for performance metrics are available out of the box, so you can get started immediately after you finish integrating the Luciq SDK.

**Network Apdex**: Get notified when the network Apdex is **less than 0.7** within 1 day.

* The alert is refined to only key metrics and for APIs with a count greater than 1000.

**Network Failure Rate**: Get notified when the failure rate for a network API is **more than 10%** within 3 hours.

* The alert is refined to only key metrics and for APIs with a count greater than 1000.

**Screen Loading Apdex**: Get notified when the screen loading Apdex is **less than 0.7** within 1 day.

* The alert is refined to only key metrics and a default occurrences count greater than 100.

**UI Hangs Apdex**: Get notified when the UI hangs Apdex is **less than 0.7** within 1 day.

* The alert is refined to only key metrics and a default occurrences count greater than 100.

**App Launch Apdex**: Get notified when the app launch Apdex is **less than 0.85** within 1 day.

* The alert is refined to only key metrics and a default occurrences count greater than 100.

These alerts act as built-in examples which then can be disabled, deleted or customized to match your application performance requirements.
