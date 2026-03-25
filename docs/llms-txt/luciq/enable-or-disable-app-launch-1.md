# Source: https://docs.luciq.ai/references/application-performance-monitoring/app-launch/enable-or-disable-app-launch-1.md

# Enable or Disable App Launch

Luciq collects data about your app launch time by default. You can use the following APIs to alter that.

{% tabs fullWidth="true" %}
{% tab title="RN" %}

```javascript
// Enable
APM.setAppLaunchEnabled(true);

// Disable
APM.setAppLaunchEnabled(false);
```

{% endtab %}

{% tab title="Flutter" %}

```javascript
// Enable Cold App Launch
APM.setColdAppLaunchEnabled(true);

// Disable Cold App Launch
APM.setColdAppLaunchEnabled(false);
```

{% endtab %}
{% endtabs %}
