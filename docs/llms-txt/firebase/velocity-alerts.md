# Source: https://firebase.google.com/docs/crashlytics/velocity-alerts.md.txt

<br />

Use velocity alerts to notify your team when any individual issue is causing an urgent problem in your app. ForCrashlytics, an issue is a grouping of similar crashes or application not responding (ANR) events.
| **Important:** To get velocity alerts,**make sure your app uses*at minimum* the following versions of theCrashlyticsSDK:**   
| Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

## What triggers an alert?

Velocity alerts are triggered when an issue in your app crosses certain thresholds that you[configure in theFirebaseconsole](https://firebase.google.com/docs/crashlytics/velocity-alerts#configure-thresholds).

You define the threshold for velocity alerts in terms of a***percentage of users and the minimum number of users that were impacted by the crash or ANR***. You can set the percentage threshold value between 0% and 100% of sessions. The minimum users threshold can be set to any number greater than or equal to 10. By default, the velocity alert threshold is set at 1% of sessions and 25 users.

Specifically, an alert is triggered if, during a 30-minute time period,***all***the following are true:

- An issue in an app exceeds the defined percentage threshold and exceeds the minimum users set for that app.
- The app has at least 10 users in that time period.
- There was no alert previously raised for the issue in the app on that version.

## Configure velocity alert thresholds

To configure velocity alert thresholds, you must have the`firebasecrashlytics.config.update`permission. The following roles include this required permission by default:[Firebase Crashlytics Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-product#crashlytics),[Firebase Quality Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles),[Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products), or project[Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

Configure velocity alert thresholds for each of your registered apps. Each app can have a different alert threshold.

1. Sign in to theFirebaseconsole, then select your project.

2. Clicksettings, then select**Project Settings** . Select the[**Alerts**tab](https://console.firebase.google.com/project/_/settings/alerts).

3. Go to the**Crashlytics** alerts card and select the**Velocity Alerts**tab.

4. Configure the alert thresholds for the app.

## Receive alerts

### Get default alerts

By default, Firebase can sendCrashlyticsalerts using email. For velocity alerts and regressions, Firebase can also show these alerts in theFirebaseconsole.

To receiveCrashlyticsalerts using this default mechanism, you must have the`firebase.projects.update`permission. The following roles include this required permission by default:[Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products)or project[Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

By default, every project member (who has the required permissions to receive alerts) will get an email when an alert fromCrashlyticsis triggered.

#### Turn alerts on or off for your own account

For your own account, you can turnCrashlyticsalerts on or off without affecting other project members. Note that you still need the required permissions to receive alerts.

1. Sign in to theFirebaseconsole, then select your project.

2. Clicksettings, then select**Project Settings** . Select the[**Alerts**tab](https://console.firebase.google.com/project/_/settings/alerts).

3. Go to the**Crashlytics** alerts card and select the**Velocity Alerts**tab.

4. Set your account preference forCrashlyticsalerts.

### Set up basic alerting to third-party services

ForCrashlyticsalerts, Firebase offers a mechanism to send alerts to the following third-party services:[Slack](https://support.google.com/firebase/answer/9005934),[Jira](https://support.google.com/firebase/answer/9118259), or[PagerDuty](https://support.google.com/firebase/answer/9168499).

1. Set up these basic alerting options using guided workflows in the[*Integrations*tab](https://console.firebase.google.com/project/_/settings/integrations/)in yoursettings*Project settings*.

2. Select which configuration is used for individual apps and configure the destination of other alerts on theCrashlyticscard of the[*Alerts tab*](https://console.firebase.google.com/project/_/settings/alerts)in yoursettings*Project settings*.

Note that if you want more control and customization for sending alerts to any third-party service (not limited to only Slack, Jira, or PagerDuty), check out the[Set up advanced alerting to third-party services](https://firebase.google.com/docs/crashlytics/velocity-alerts#advanced-alerts-3p)section that describes advanced alerting options.

### Set up advanced alerting to third-party services

You can sendCrashlyticsalerts to your team's preferred notification channel, usingCloud Functions for Firebase. For example, you can write a function that captures an alert event for velocity alerts and posts the alert information to a third-party service, like Discord, Slack, or Jira. With this advanced alerting mechanism, you can fully customize the information sent to the third-party service; for example, you can include helpful deep-links into theFirebaseconsole or add company-specific troubleshooting information.
| **Note:** To use advanced alerting capabilities, your Firebase project needs to use the[Blaze pricing plan](https://firebase.google.com/pricing).

To set up advanced alerting capabilities usingCloud Functions for Firebase, follow these steps:

1. [Set up Cloud Functions for Firebase](https://firebase.google.com/docs/functions/get-started), which includes the following tasks:

   1. Set up a development environment for Node.js or Python.
   2. Install and sign into theFirebaseCLI.
   3. InitializeCloud Functions for Firebaseusing theFirebaseCLI.
2. [Write and deploy a function](https://firebase.google.com/docs/functions/alert-events)that captures an alert event fromCrashlyticsand handles the event payload (for example, posts the alert information in a message on Discord).

To learn about all theCrashlyticsalert events that you can capture, go to the reference documentation for[Crashlyticsalerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics).