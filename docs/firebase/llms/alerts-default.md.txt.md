# Source: https://firebase.google.com/docs/crashlytics/alerts-default.md.txt

Firebase can send a variety of default Crashlytics alerts (see the
[alerting overview page](https://firebase.google.com/docs/crashlytics/alerts)).
Firebase can send all default Crashlytics alerts to your email.
For *regressed issues* and *increasing-velocity issues* , Firebase can also show
alerts in the Firebase console.

- Alerts for *regressed* and *trending* issues do not require any configuration
  and are ***sent by default*** when you set up Crashlytics.

- Alerts for new *non-fatals* , *fatals* , *ANRs* , and
  *increasing-velocity issues* are ***not sent by default***. To receive these
  alerts, you must (at minimum) select your preferred alerting channel.

All alert types offer some configuration. For example, you can turn alerts on
or off for your own account, and for *increasing-velocity issues* , you can set
thresholds for when alerts are sent. You can view and configure these alerts in
the
[**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts)
in the Firebase console.

> [!NOTE]
> **Note:** Alerts for increasing-velocity issues (called ***velocity alerts*** ) are a more complex type of alert. Find detailed information about [configuring velocity alerts](https://firebase.google.com/docs/crashlytics/alerts-default#velocity-alerts) later on this page.

<br />

The rest of this page describes in detail how to configure various options for
default Crashlytics alerts.

## Receive alerts by email and in-console

Only specific project members can receive alerts, and you can turn on or off
alerts for your own account.

By default, every project member (who has the required permissions to receive
alerts) will get an email for *regressed issue* alerts and an email plus an
in-console alert for *trending* alerts. All other alerts must be configured for
you to receive them by email or in-console.

### Required permissions to receive alerts

To receive Crashlytics alerts by email or in-console, you must have the
`firebase.projects.update` permission. The following roles include this required
permission by default:
[Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products) or project
[Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

### Turn alerts on or off for your own account

For your own account, you can turn Crashlytics alerts on or off without
affecting other project members. Note that you still need the required
permissions to receive alerts.

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts).

4. Go to the **Crashlytics** alerts card, and then select the alert that
   you want to configure (for example, *Velocity Alerts*).

5. Set your account preference for that alert.

## Configure alert settings

To configure the settings for an alert, you must have the
`firebasecrashlytics.config.update` permission. The following roles include
this required permission by default:
[Firebase Crashlytics Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-product#crashlytics),
[Firebase Quality Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles),
[Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products), or
project [Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings** . Select the
   [**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts).

3. Go to the **Crashlytics** alerts card, and then select the alert that
   you want to configure (for example, *Velocity Alerts*).

4. Configure the settings for that alert.

<br />

*** ** * ** ***

## Configure velocity alerts

Use velocity alerts to notify your team when any individual issue is causing an
urgent problem in your app. For Crashlytics, an issue is a grouping of
similar crashes or application not responding (ANR) events.

> [!IMPORTANT]
> **Important:** To get velocity alerts, **make sure your app uses *at minimum* the following versions of the
> Crashlytics SDK:**   
> Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoM v32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

### What triggers a velocity alert?

Velocity alerts are triggered when an issue in your app crosses certain
thresholds that you
[configure in the Firebase console](https://firebase.google.com/docs/crashlytics/alerts-default#velocity-alerts-configure-thresholds).

You define the threshold for velocity alerts in terms of a
***percentage of users and the minimum number of users that were
impacted by the crash or ANR***. You can set the percentage threshold value
between 0% and 100% of sessions. The minimum users threshold can be set to any
number greater than or equal to 10. By default, the velocity alert threshold is
set at 1% of sessions and 25 users.

Specifically, an alert is triggered if, during a 30-minute time period,
***all*** the following are true:

- An issue in an app exceeds the defined percentage threshold and exceeds the minimum users set for that app.
- The app has at least 10 users in that time period.
- There was no alert previously raised for the issue in the app on that version.

### Configure velocity alert thresholds

To configure velocity alert thresholds, you must have the
`firebasecrashlytics.config.update` permission. The following roles include
this required permission by default:
[Firebase Crashlytics Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-product#crashlytics),
[Firebase Quality Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles),
[Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products), or
project [Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

Configure velocity alert thresholds for each of your registered apps. Each app
can have a different alert threshold.

1. Sign in to the Firebase console, then select your project.

2. Click , then select
   **Project Settings**.

3. Select the
   [**Alerts** tab](https://console.firebase.google.com/project/_/settings/alerts).

4. Go to the **Crashlytics** alerts card, and then select the
   **Velocity Alerts** tab.

5. Configure the alert thresholds for the app.