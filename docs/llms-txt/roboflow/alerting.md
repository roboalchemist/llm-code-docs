# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/model-monitoring/alerting.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/model-monitoring/alerting.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/model-monitoring/alerting.md

# Source: https://docs.roboflow.com/deploy/model-monitoring/alerting.md

# Alerting

The Model Monitoring dashboard allows you to set up notifications for anomaly detection. To create an alert, first navigate to the model monitoring dashboard.

Click the "Create New Alert" button just above the list of models.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-e622ffa5e7b2a4d2ba378d1d61593edae5b02201%2FScreenshot%202024-05-23%20at%2021.22.44.png?alt=media" alt=""><figcaption><p>Create new alerts by clicking the Create New Alert button</p></figcaption></figure>

1. **Name your alert.** Give your alert a name. This is optional but highly recommended so that you can quickly identify your alert later
2. **Configure a Rule**. First, choose the model that you would like to create an alert for. Note that only models with a trained version will appear in the dropdown. Furthermore, if your workspace has SSO rules configured, then only models that you have access to will appear.
3. **Choose a version**. Then choose a version of that model. If no version is selected, then all inferences to all of the selected model's versions will be in scope.
4. **Choose a class**. Select a class that you would like to target for your alert.
5. **Choose a metric.** Now you can select a metric and a threshold. Anytime your inferences reach the threshold level, they will trigger an alert.
6. **Choose an alert window**. You can define an alert window. The alert window is a group of inference results that are used to determine whether or not to trigger an alert. For example, if you choose a window of "30 minutes", then only inference results made in the last 30 minutes (on a rolling basis) would be used to determine if the threshold for triggering the alert has been reached.
7.

```
<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 at 21.23.31.png" alt=""><figcaption><p>Create alert configuration</p></figcaption></figure>
```

8. **Choose alert recipients**. Now you can configure a list of team members in your workspace to send the alert to. By default, the alert will only be sent to you.
9. **Choose notification limits**. Now choose the maxium number of alerts that we should send by hour and by day. Regardless of how many times the alert is triggered, you will only receive a notification the maximum number of times hourly or daily that you set here.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-58a72f6a6cc975d18c4b02d649d5c2b3f155a533%2FScreenshot%202024-05-23%20at%2021.23.46.png?alt=media" alt=""><figcaption><p>Choose recipients and notification limits</p></figcaption></figure>

Click submit and your alert will be created. To see a list of active alerts that you have configured, you can click the "Manage Active Alerts" button. From here, you can edit and delete existing alerts.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c8b708744a90a889f25ae5634b083c4fbced6e24%2FScreenshot%202024-05-23%20at%2021.24.02.png?alt=media" alt=""><figcaption><p>View active alerts</p></figcaption></figure>
