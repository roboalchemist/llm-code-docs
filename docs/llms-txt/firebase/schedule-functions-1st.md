# Source: https://firebase.google.com/docs/functions/1st-gen/schedule-functions-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Schedule functions](https://firebase.google.com/docs/functions/schedule-functions).

If you want to schedule functions to run at specified times, use the`onSchedule`handler to create a[Pub/Sub](https://cloud.google.com/pubsub/)topic that uses[Cloud Scheduler](https://cloud.google.com/scheduler/)to trigger events on that topic.

## Before you begin

Though scheduled functions are billed, you can expect the overall cost to be manageable, as eachCloud Schedulerjob costs $0.10 (USD) per month, and there is an allowance of three jobs per Google account, at no charge. Use the Blaze[pricing calculator](https://firebase.google.com/pricing#blaze-calculator)to generate a cost estimate based on your projected usage.

ThePub/SubandCloud SchedulerAPIs must be enabled for your project. These should already be enabled for most Firebase projects; you can verify in the[Google Cloud console](https://console.cloud.google.com/).
| **Important:** Cloud Schedulerused to require that your project have a[GoogleApp Engineapp](https://cloud.google.com/appengine/docs/). During its setup you were prompted to select a location, and this location became your project's[*location for defaultGoogle Cloudresources*](https://firebase.google.com/docs/projects/locations#default-cloud-location)(Cloud Schedulerbeing one of these resources). This location is used for resources in your project that have an association withApp Engine, including your*default* Cloud Firestoredatabase instance and your*default* Cloud Storagebucket (specifically with the name format`*.appspot.com`).
|
| However, now thatCloud Schedulerand recently provisioned defaultCloud Storagebuckets (with the name format`*.firebasestorage.app`) no longer have a dependency onApp Engine, you only need to consider this location if you're using 1st gen scheduled functions and`*.appspot.com`buckets.

## Write a scheduled function

InCloud Functions for Firebase, scheduling logic resides in your functions code, with no special deploy-time requirements. To create a scheduled function, use`functions.pubsub.schedule('your schedule').onRun((context))`. For example, to run a function every five minutes with[App Enginecron.yaml](https://cloud.google.com/appengine/docs/standard/python/config/cronref)syntax, do something like this:  

    exports.scheduledFunction = functions.pubsub.schedule('every 5 minutes').onRun((context) => {
      console.log('This will be run every 5 minutes!');
      return null;
    });

Both Unix Crontab andApp Enginesyntax are supported byCloud Scheduler. For example, to use Crontab to select a specific timezone in which to run a scheduled function, do something like this:  

    exports.scheduledFunctionCrontab = functions.pubsub.schedule('5 11 * * *')
      .timeZone('America/New_York') // Users can choose timezone - default is America/Los_Angeles
      .onRun((context) => {
      console.log('This will be run every day at 11:05 AM Eastern!');
      return null;
    });

The value for`timeZone`must be a time zone name from the[tz database](http://en.wikipedia.org/wiki/Tz_database). See the[Cloud Schedulerreference](https://cloud.google.com/scheduler/docs/reference/rpc/google.cloud.scheduler.v1#job)for more information on supported properties.
| **Important:** Depending on how you design your scheduling logic, a function may be triggered multiple times, with the next instance running while the previous instance is still executing.

## Deploy a scheduled function

When you deploy a scheduled function, the related scheduler job and pub/sub topic are created automatically. TheFirebaseCLI echoes the topic name, and you can view the job and topic in the[Google Cloud console](https://console.cloud.google.com/project/_/cloudscheduler). The topic is named according to the following convention:

**firebase-scheduled-<var translate="no">function_name</var>-<var translate="no">region</var>**

For example:

**firebase-scheduled-scheduledFunctionCrontab-us-east1.**
| **Important:** Make sure you do not manually delete or modify the topic or scheduler job in the console. Doing this could cause errors in the execution of your scheduled function.