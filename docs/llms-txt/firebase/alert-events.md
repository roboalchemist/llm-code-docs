# Source: https://firebase.google.com/docs/functions/alert-events.md.txt

<br />

Firebase provides alerting for a wide range of project and app management events. Here are a few example events for when Firebase can send you this type of alert:

- ForCrashlytics, we can alert you if your app has a dramatic increase in crashes.
- ForPerformance Monitoring, we can alert you if your app's start-up time crosses your configured threshold.
- ForApp Distribution, we can alert you if one of your testers registers a new iOS device.

Depending on the alert and the[preferences set by the project member](https://support.google.com/firebase/answer/7276542), Firebase shows these types of alerts in theFirebaseconsole or sends them via email.

This page describes how to write functions inCloud Functions for Firebase(2nd gen) that handle alert events.

## How does it work?

You can trigger functions in response to alert events emitted by these sources:

- [Handle anApp Distributionalert event](https://firebase.google.com/docs/functions/alert-events#handle-app-distribution-alerts)
- [Handle aCrashlyticsalert event](https://firebase.google.com/docs/functions/alert-events#handle-crashlytics-alerts)
- [Handle aPerformance Monitoringalert event](https://firebase.google.com/docs/functions/alert-events#handle-performance-alerts)

In a typical lifecycle, a function triggered by an alert event does the following:

1. Listens/waits for a specific alert type to be emitted from Firebase.
2. Triggers when the alert is emitted, and receives the event payload which contains specific information about the event.
3. Invokes your function's code to handle the event payload.

## Trigger a function on alert events

Use the`firebase-functions/v2/alerts`subpackage to write a function that handles alerts events. The following product-specific examples demonstrate a workflow where a function uses a webhook to post a message to a Discord channel when an alert for that product is emitted from Firebase.
| **Important:** Each of these examples assumes that you've already[set upCloud Functions for Firebase](https://firebase.google.com/docs/functions/get-started?2nd-gen).

### Handle aCrashlyticsalert event

For the followingCrashlyticsexample, you useCloud Functions for Firebaseto handle an alert event of a new fatal crash issue. This function posts the alert information in a message to a Discord channel.

![Example crash notification in Discord](https://firebase.google.com/static/docs/functions/images/discord-functions.png)
Example notification for a new fatal crash issue

<br />

The function listens for the event corresponding to Firebase publishing a new fatal issue:  

### Node.js

    exports.postfatalissuetodiscord = onNewFatalIssuePublished(async (event) => {  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L64-L64

### Python

    @crashlytics_fn.on_new_fatal_issue_published(secrets=["DISCORD_WEBHOOK_URL"])
    def post_fatal_issue_to_discord(event: crashlytics_fn.CrashlyticsNewFatalIssueEvent) -> None:
        """Publishes a message to Discord whenever a new Crashlytics fatal issue occurs."""  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L53-L55

The function then parses the returned event object, parsing useful information from the event payload and constructing a message to post to the Discord channel:  

### Node.js

      // construct a helpful message to send to Discord
      const appId = event.appId;
      const {id, title, subtitle, appVersion} = event.data.payload.issue;
      const message = `
    ð¨ New fatal issue for ${appId} in version ${appVersion} ð¨

    **${title}**

    ${subtitle}

    id: \`${id}\`
    `;  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L67-L78

### Python

        # Construct a helpful message to send to Discord.
        app_id = event.app_id
        issue = event.data.payload.issue
        message = f"""
    ð¨ New fatal issue for {app_id} in version {issue.app_version} ð¨

    # {issue.title}

    {issue.subtitle}

    ID: `{issue.id}`
    """.strip()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L58-L69

Finally, the function sends the constructed message to Discord through an HTTP request:  

### Node.js

    const response = await postMessageToDiscord("Crashlytics Bot", message);
    if (response.ok) {
      logger.info(
          `Posted fatal Crashlytics alert ${id} for ${appId} to Discord`,
          event.data.payload,
      );
    } else {
      throw new Error(`Discord returned status code ${response.status}`);
    }  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L83-L91

### Python

    response = post_message_to_discord("Crashlytics Bot", message, DISCORD_WEBHOOK_URL.value)
    if response.ok:
        print(f"Posted fatal Crashlytics alert {issue.id} for {app_id} to Discord.")
        pprint.pp(event.data.payload)
    else:
        response.raise_for_status()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L74-L79

To learn about all theCrashlyticsalert events that you can capture, go to the reference documentation for[Crashlyticsalerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics).

### Handle aPerformance Monitoringalert event

This example exports a function that listens for performance threshold alert events:  

### Node.js

    exports.postperformancealerttodiscord = onThresholdAlertPublished(
        async (event) => {  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L149-L150

### Python

    @performance_fn.on_threshold_alert_published(secrets=["DISCORD_WEBHOOK_URL"])
    def post_performance_alert_to_discord(event: performance_fn.PerformanceThresholdAlertEvent) -> None:
        """Publishes a message to Discord whenever a performance threshold alert is fired."""  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L117-L119

The function then parses the returned event object, parsing useful information from the event payload and constructing a message to post to the Discord channel:  

### Node.js

          // construct a helpful message to send to Discord
          const appId = event.appId;
          const {
            eventName,
            metricType,
            eventType,
            numSamples,
            thresholdValue,
            thresholdUnit,
            conditionPercentile,
            appVersion,
            violationValue,
            violationUnit,
            investigateUri,
          } = event.data.payload;
          const message = `
        â ï¸ Performance Alert for ${metricType} of ${eventType}: **${eventName}** â ï¸
        
        App id: ${appId}
        Alert condition: ${thresholdValue} ${thresholdUnit}
        Percentile (if applicable): ${conditionPercentile}
        App version (if applicable): ${appVersion}
        
        Violation: ${violationValue} ${violationUnit}
        Number of samples checked: ${numSamples}
        
        **Investigate more:** ${investigateUri}
        `;  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L153-L180

### Python

        # Construct a helpful message to send to Discord.
        app_id = event.app_id
        perf = event.data.payload
        message = f"""
    â ï¸ Performance Alert for {perf.metric_type} of {perf.event_type}: **{perf.event_name}** â ï¸

    App ID: {app_id}
    Alert condition: {perf.threshold_value} {perf.threshold_unit}
    Percentile (if applicable): {perf.condition_percentile}
    App version (if applicable): {perf.app_version}

    Violation: {perf.violation_value} {perf.violation_unit}
    Number of samples checked: {perf.num_samples}

    **Investigate more:** {perf.investigate_uri}
    """.strip()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L122-L137

Finally, the function sends the constructed message to Discord through an HTTP request:  

### Node.js

    const response = await postMessageToDiscord(
        "Firebase Performance Bot", message);
    if (response.ok) {
      logger.info(
          `Posted Firebase Performance alert ${eventName} to Discord`,
          event.data.payload,
      );
    } else {
      throw new Error(`Discord returned status code ${response.status}`);
    }  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L185-L194

### Python

    response = post_message_to_discord("App Performance Bot", message,
                                       DISCORD_WEBHOOK_URL.value)
    if response.ok:
        print(f"Posted Firebase Performance alert {perf.event_name} to Discord.")
        pprint.pp(event.data.payload)
    else:
        response.raise_for_status()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L142-L148

To learn about all the performance alert events that you can capture, go to the reference documentation for[Performance Monitoringalerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance).

### Handle anApp Distributionalert event

The example in this section shows you how to write a function for new tester iOS device alerts.

In this example, the function listens for events that are sent every time a tester registers a new iOS device. When a new iOS device is registered, you need to update your provisioning profile with that device's UDID and then redistribute the app.  

### Node.js

    exports.postnewduuidtodiscord = onNewTesterIosDevicePublished(async (event) => {  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L106-L106

### Python

    @app_distribution_fn.on_new_tester_ios_device_published(secrets=["DISCORD_WEBHOOK_URL"])
    def post_new_udid_to_discord(event: app_distribution_fn.NewTesterDeviceEvent) -> None:
        """Publishes a message to Discord whenever someone registers a new iOS test device."""  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L86-L88

The function then parses the returned object, parsing useful information from the event payload and constructing a message to post to the Discord channel:  

### Node.js

      // construct a helpful message to send to Discord
      const appId = event.appId;
      const {
        testerDeviceIdentifier,
        testerDeviceModelName,
        testerEmail,
        testerName,
      } = event.data.payload;
      const message = `
    ð± New iOS device registered by ${testerName} <${testerEmail}> for ${appId}

    UDID **${testerDeviceIdentifier}** for ${testerDeviceModelName}
    `;  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L109-L121

### Python

        # Construct a helpful message to send to Discord.
        app_id = event.app_id
        app_dist = event.data.payload
        message = f"""
    ð± New iOS device registered by {app_dist.tester_name} <{app_dist.tester_email}> for {app_id}

    UDID **{app_dist.tester_device_identifier}** for {app_dist.tester_device_model_name}
    """.strip()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L91-L98

Finally, the function sends the constructed message to Discord through an HTTP request:  

### Node.js

    const response = await postMessageToDiscord("AppDistribution Bot", message);
    if (response.ok) {
      logger.info(
          `Posted iOS device registration alert for ${testerEmail} to Discord`,
      );
    } else {
      throw new Error(`Discord returned status code ${response.status}`);
    }  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/alerts-to-discord/functions/index.js#L126-L133

### Python

    response = post_message_to_discord("App Distro Bot", message, DISCORD_WEBHOOK_URL.value)
    if response.ok:
        print(f"Posted iOS device registration alert for {app_dist.tester_email} to Discord.")
        pprint.pp(event.data.payload)
    else:
        response.raise_for_status()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/alerts-to-discord/functions/main.py#L103-L108

To learn about all theApp Distributionalert events that you can capture, go to the reference documentation for[App Distributionalerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution).

To learn how to use a function triggered by an[in-app feedback Firebase alert fromApp Distribution](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload), see[Send in-app feedback to Jira](https://github.com/firebase/functions-samples/tree/main/Node/app-distribution-feedback-to-jira).