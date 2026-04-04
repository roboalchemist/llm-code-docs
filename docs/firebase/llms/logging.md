# Source: https://firebase.google.com/docs/app-hosting/logging.md.txt

<br />

Logging and metrics are important tools for debugging and monitoring code.App Hostingprovides quick access to view logs and metrics for the Google Cloud services powering your web app:Cloud Run,Cloud Buildand Cloud CDN.

Using standard logging syntax like Node.js'`console.log`, you can write log entries toCloud Logging.

## View usage in the console

Each backend has an**Overview**tab, with a summary of your app's traffic (request count) and error rate over the past seven days.

Each backend also has a**Usage**tab with several usage graphs for activity and usage of your app. The data represented includes CDN bandwidth and requests, Cloud Run CPU and memory utilization, and more.

You can find additional utilization metrics for Cloud Run (such as CPU utilization and Memory utilization), in the Google Cloud console.

## View logs in the console

From theFirebaseconsole context menu (a 3-dot menu at upper right) for a rollout, you can get quick access to view theCloud Runrevision details and errors as well as build logs.

These logs contain helpful information for debugging yourApp Hostingdeployments. For example, theCloud Runlog notes when`package.json`is not found.

The build log displays your build output, allowing you to triage whether errors occurred in configuration in your framework, or inApp Hostingconfiguration. It also displays your basic`runConfig`settings, and indicates when settings are missing or when`apphosting.yaml`does not exist:  

    > next build

       â² Next.js 14.1.4
       -   Environments: .env

       ...

    Route (app)                              Size     First Load JS
    â Î» /                                    4.79 kB         214 kB
    â Î» /_not-found                          882 B          85.3 kB
    â Î» /restaurant/[id]                     5.28 kB         207 kB
    +   First Load JS shared by all            84.4 kB
      â chunks/69-6678c81190a8fe82.js        29 kB
      â chunks/fd9d1056-51920e345d2966e8.js  53.4 kB
      â other shared chunks (total)          1.98 kB

## Write logs toCloud Logging

If you want to log custom events, you can write toCloud LoggingfromCloud Run, where your server-rendered code runs. Use standard JavaScript logging calls such as`console.log`and`console.error`. For example, to write a custom entry from code for a[Next.js route handler](https://www.google.com/url?q=https://nextjs.org/docs/app/building-your-application/routing/route-handlers), you would do something like this:

- `console.log()`commands have the**INFO**log level.
- `console.info()`commands have the**INFO**log level.
- `console.warn()`commands have the**ERROR**log level.
- `console.error()`commands have the**ERROR**log level.
- Internal system messages have the**DEBUG**log level.

Note that`console.log`pipes through toCloud Loggingin the*server-rendered* code for your app. Events related to static rendering are sent toCloud Buildlogs, while server rendering are sent toCloud Runlogs.

## View server errors

[Cloud Error Reporting](https://www.google.com/url?q=https://cloud.google.com/error-reporting/docs/grouping-errors)consolidates errors from yourApp HostingCloud Runinstance. You can optionally configure Cloud Error Reporting to[notify you when new errors arise](https://cloud.google.com/error-reporting/docs/notifications).