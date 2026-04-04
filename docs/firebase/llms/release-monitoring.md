# Source: https://firebase.google.com/docs/release/release-monitoring.md.txt

<br />

Rolling out a new version of your mobile app to production is one of the most exciting parts of app development, but it can also be one of the most stressful! Your team needs to keep track of version uptake, new bugs and the impact of those bugs, a comparison to earlier releases, and more.

This page describes several tools offered by Firebase to monitor the data you need to feel confident about your mobile app release.

## Use the*Release Monitoring*dashboard to explore your release-related data

The[*Release Monitoring*dashboard](https://console.firebase.google.com/project/_/releasemonitoring/)in theFirebaseconsole is powered byFirebase Crashlytics. It's a single dashboard to monitor your most recent production release. The dashboard updates in near real time and gives you a high-level view of the most important release metrics, including crash-free metrics, version uptake, comparisons to previous releases, and any new issues for the release.

This new dashboard improves upon the*Latest Release* page in the console. Compared to that page, the*Release Monitoring*dashboard adds more information, displays useful data without the need for Google Analytics, and loads more quickly.
| **Important:** Before trying to use the dashboard, we recommend reviewing the FAQ["Which builds can I view on the*Release Monitoring*dashboard?"](https://firebase.google.com/docs/release/release-monitoring#which-builds-can-be-viewed). In particular,**make sure your app uses*at minimum* the following versions of theCrashlyticsSDK:**   
| Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

### Features of the dashboard

- **Real time reporting**   
  All the charts update in near real time. Shortly after you deploy your latest version, you can watch as users start engaging with that release. If some of those users happen to experience crashes, you'll know the impact immediately through[crash-free metrics](https://firebase.google.com/docs/crashlytics/crash-free-metrics)charts.

- **Comparison and benchmarking based on previous releases**   
  You can view your latest release's stability in context of your previous releases. The dashboard lets you compare the live metrics from your latest release and up to two of your previously released builds.

- **Top new issues**   
  You can view*new* crashes for your latest release as they arrive. In the*Top new issues*table, you can monitor the impact of the issues first detected in your latest release, allowing you to quickly make a decision on whether to halt or rollback the release.

### Requirements for the dashboard

To view your latest release in the*Release Monitoring*dashboard, do the following:

1. Make sure your app uses*at minimum* the following versions of theCrashlyticsSDK:  
   Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

2. Publish a new version of the app to production so that you have a[sufficient number of engaged users with your latest release](https://firebase.google.com/docs/release/release-monitoring#waiting-for-more-users-message).

### FAQs about the dashboard

<br />

##### What are the required SDK versions to use the*Release Monitoring*dashboard?

<br />

For a build to appear on the dashboard, it must use*at minimum* the following versions of theCrashlyticsSDK:  
Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

Note that these versions of the SDK are often referred to as "sessions-capable" SDK versions, since they're capable of sending sessions data toCrashlyticswhich is required for many of the new features inCrashlytics, like the*Release Monitoring*dashboard.

<br />

<br />

<br />

##### Why does the*Release Monitoring*dashboard say "Waiting for more users to engage"?

<br />

For a build to appear on the dashboard, it must meet all the following requirements:

- The build uses*at minimum* the following versions of theCrashlyticsSDK:  
  Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

- The build has a sufficient number of users within the last 3 days:

  - The build must have at least 500 unique users**OR**

  - The build has at least 1% of the total users***and***has at least 2 unique users.

<br />

<br />

<br />

##### Which builds can be viewed on the*Release Monitoring*dashboard?

<br />

The*Release Monitoring*dashboard aims to help you with your production releases, that is, builds that have a significant number of users.

For a build to appear on the dashboard, it must meet all the following requirements:

- The build uses*at minimum* the following versions of theCrashlyticsSDK:  
  Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

- The build has a sufficient number of users within the last 3 days:

  - The build must have at least 500 unique users**OR**

  - The build has at least 1% of the total users***and***has at least 2 unique users.

*(For apps distributed throughGoogle Play)* If an app has a[Google Playlink](https://firebase.google.com/docs/crashlytics/integrate-with-google-play), the dashboard shows all the builds listed in thePlayProd track, even ifCrashlyticshasn't received any sessions logs or detected active users for that build.

Note that to view data in the dashboard for comparisons or active users percentage, you need to have released*at least two builds*that meet the preceding requirements.

<br />

<br />

<br />

##### How are the values shown in the*Active users*chart determined or calculated?

<br />

First, it's helpful to understand some of the terminology involved with the*Active users*chart:

- A***session***is a continuous period of time when a user is engaged with an application. A new session starts when the app is cold-started or the app is foregrounded after at least 30 minutes of backgrounding.

- ***Active users***for a specific build are the number of users who started a session using that build, grouped by hour.

- ***Total (active) users*** are the number of users who started a session in*any build* of the app that uses a[sessions-capable SDK version](https://firebase.google.com/docs/release/release-monitoring#required-sdk-versions), grouped by hour.

In the*Active users* chart, the percentage value and count of active users that are always displayed on the chart are from the last 60 minutes (or if there haven't been any active users in the past 60 minutes, the past hour period that did have data). For example, in the example screenshot, there were 90 active users for the`6.0.0 (600)`build in the past 60 minutes, which accounts for 22.1% of the total (active) users for the app.

![screenshot of an example _Active users_ chart from the <i>Release Monitoring</i> dashboard](https://firebase.google.com/static/docs/release/images/release-monitoring_active-users-chart.png)

When you hold the mouse over the lines in the*Active users*chart, the active user percentage is calculated from the active users count from the hour period you're hovering over.

Note that to see the active users percentage, you need to have released*at least two builds* that meet the requirements described in the FAQ["Which builds can be viewed on the*Release Monitoring*dashboard?"](https://firebase.google.com/docs/release/release-monitoring#which-builds-can-be-viewed).

<br />

<br />

<br />

##### Why is my active users percentage at 0%?

<br />

The active users percentage is based on received session data not on any other data (likeGoogle Playdata or crash reports).

<br />

<br />

<br />

##### Why am I not seeing comparisons and/or active users percentage?

<br />

If this is the first time that you've released your app with a[compatibleCrashlyticsSDK version](https://firebase.google.com/docs/release/release-monitoring#required-sdk-versions), thenCrashlyticshas no previous session data to compare against.

<br />

<br />

## Set up alerts

Several Firebase products, includingCrashlytics, can send alerts for various product-specific reasons. In order to[receive alerts](https://support.google.com/firebase/answer/7276542), you must have the required permissions.

To monitor the stability of your latest release, you can set up alerts from both[Performance Monitoring](https://firebase.google.com/docs/perf-mon/alerts)andCrashlytics. ForCrashlyticsspecifically, you can set up the following alerts:

- Use[velocity alerts](https://firebase.google.com/docs/crashlytics/alerts-default#velocity-alerts)to notify your team if any individual issue in your app crosses a threshold that you define in theFirebaseconsole.

- Send alerts about new or regressed issues to your preferred notification channel:

  - Use the Firebase-console configured alert integrations for[Slack](https://firebase.google.com/docs/crashlytics/alerts-basic-integrations#slack),[Jira](https://firebase.google.com/docs/crashlytics/alerts-basic-integrations#jira), and[PagerDuty](https://firebase.google.com/docs/crashlytics/alerts-basic-integrations#pagerduty).

  - Set up[advanced alerting to third-party services](https://firebase.google.com/docs/crashlytics/alerts#advanced)usingCloud Functions for Firebase.

## Ensure a smooth release before you release

Before you release your latest version, consider using some of the following services and features to help ensure a smooth release.

### Use pre-release testing services

Firebase offers two products that can help with pre-release testing:Test LabandApp Distribution. Both these services can be integrated into your CI/CD flows.

[Firebase Test Lab](https://firebase.google.com/products/test-lab)is a cloud-based app testing infrastructure that lets you test your app on a range of devices and configurations, so you can get an early understanding of how it will perform in the hands of live users.

And when you're ready to put your latest build in the hands of trusted*human* testers, use[Firebase App Distribution](https://firebase.google.com/products/app-distribution). You can manage both your Apple platform and Android pre-release distributions from the same place.

### Use roll out and limited testing services

Use[Firebase Remote Config](https://firebase.google.com/products/remote-config)to launch new features with a[percentage rollout mechanism](https://firebase.google.com/docs/remote-config/use-cases#launch_new_features_with_the_percentage_rollout_mechanism)or test those features on a[limited testing group](https://firebase.google.com/docs/remote-config/use-cases#test_new_functionality_on_a_limited_testing_group).

Firebase also offers[A/B Testing](https://firebase.google.com/products/ab-testing)so that you can test changes to your app's UI, features, or engagement campaigns to see how they impact your key metrics (like revenue and retention) before you roll them out widely.