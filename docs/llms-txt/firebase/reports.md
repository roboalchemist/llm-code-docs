# Source: https://firebase.google.com/docs/analytics/reports.md.txt

Once you[add the Google Analytics for Firebase SDK](https://firebase.google.com/docs/analytics/get-started), you can use the*Analytics* section in theFirebaseconsole and the*Reports* section in your Google Analytics property to see your app data. The app reports in theFirebaseconsole are identical to the app reports in your Google Analytics property.

This page describes how to view your Analytics reports and what data is available in each report. To learn more about Analytics and its features, such as audiences, conversions, and remarketing, see[the Google Analytics help center](https://support.google.com/analytics).

## Get started with Analytics reports

The app reports in theFirebaseconsole and in your Google Analytics property provide comprehensive in-app behavioral and marketing analytics for web and mobile apps. You get insight into your app marketing performance and how users engage with your app. The reports also enable you create audiences and connect with third-party networks to make your insights actionable.

## View your Analytics reports

To view your reports in theFirebaseconsole, follow these steps:

1. Go to the[Firebaseconsole](https://console.firebase.google.com/).
2. Select your Firebase project.
3. In the left-side navigation menu, expand**Analytics**.
4. Click the reports you want to view, such as*Dashboard* ,*Events* , or*Audiences*.

When viewing a report in theFirebaseconsole, you can click**View more in Google Analytics**to open the report in your Google Analytics property.
| **Note:** The reports are identical in theFirebaseconsole and in your Google Analytics property. For more information about each report, refer to the applicable Google Analytics help center article (see links below).

## Learn about each Analytics report

The following table describes each report in theFirebaseconsole and where you can find the report in your Google Analytics property:

| Report in Firebaseconsole | Report in Google Analytics |                                                                                                                                                  Description                                                                                                                                                  |
|---------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Dashboard*               | *Firebase overview*        | See a summary of data about your linked apps to help you monitor engagement, see how much revenue you're generating, and evaluate the success of your app releases.[Learn more about the report.](https://support.google.com/analytics/answer/11014767)                                                       |
| *Realtime Analytics*      | *Realtime*                 | Monitor app activity in the last 30 minutes (per minute) so you can evaluate the impact of new campaigns and app changes on your traffic.[Learn more about the report.](https://support.google.com/analytics/answer/9271392)                                                                                  |
| *Events*                  | *Events*                   | See how many times each event is triggered and how many users trigger each event on your app. This data can help you make improvements to the user experience and increase conversions.[Learn more about the report.](https://support.google.com/analytics/answer/12926615)                                   |
| *Conversions*             | *Conversions*              | See how often users triggered each conversion event and how many users triggered each conversion event.[Learn more about the report.](https://support.google.com/analytics/answer/12925217)                                                                                                                   |
| *Audiences*               | *Audiences*                | Create, edit, and archive audiences to segment your users in ways that are important to your business. You can segment by dimensions, metrics, and events to include practically any subset of users.[Learn more about the report.](https://support.google.com/analytics/answer/9267572)                      |
| *Custom Definitions*      | *Custom definitions*       | Create custom dimensions and metrics using values from event parameters and user properties. This enables you to report on information about your users and how they interact with your app.[Learn more about the report.](https://support.google.com/analytics/answer/10075209)                              |
| *Latest Release*          | *Latest release*           | Report on important metrics for your app, like app adoption (for example, how many users upgrade), engagement (for example, what are people doing in the app), and stability (for example, how often does the app crash).[Learn more about the report.](https://support.google.com/analytics/answer/13386872) |
| *DebugView*               | *DebugView*                | Monitor events and user properties as they are collected by Google Analytics to ensure that you're collecting data correctly.[Learn more about the report.](https://support.google.com/analytics/answer/7201382)                                                                                              |

## Understand where Analytics data comes from

The Google Analytics for Firebase SDK collects basic app-usage data through[automatically collected events](https://support.google.com/analytics/answer/9234069)and[predefined user properties](https://support.google.com/analytics/answer/9268042). This data can help you understand basic interactions, such as how many times your app was opened, how often in-app purchases were made, and how many users were active in a chosen time period.

In addition to the basic app-usage data, you can set up[recommended events](https://support.google.com/analytics/answer/9267735),[custom events](https://support.google.com/analytics/answer/12229021), and[user properties](https://support.google.com/analytics/answer/12370404)to collect more data than what's collected by default.

## Export your data inBigQuery

In addition to seeing your data in Analytics reports, you can export your data toBigQuery.[BigQuery](https://cloud.google.com/bigquery)is a Google Cloud tool that lets you run fast queries on large datasets.

You can export all of your raw, unsampled events toBigQueryand use a SQL-like syntax to query that data. InBigQuery, you can choose to export your data to an external storage or import external data to combine it with your Analytics data.

When you export data toBigQuery, you own that data, and you can useBigQueryACLs to manage permissions on projects and datasets.

To export your data toBigQuery, you need to[link your Firebase project toBigQuery](https://support.google.com/firebase/answer/6318765).