# Source: https://firebase.google.com/docs/ab-testing/abtest-config.md.txt

<br />

When you useFirebase Remote Configto deploy settings for an application with an active user base, you want to make sure you get it right. You can useA/B Testingexperiments to best determine the following:

- **The best way to implement a feature to optimize the user experience.**Too often, app developers don't learn that their users dislike a new feature or an updated user experience until their app's rating in the app store declines. A/B testing can help measure whether your users like new variants of features, or whether they prefer the app as it exists. Plus, keeping most of your users in a baseline group ensures that most of your user base can continue to use your app without experiencing any changes to its behavior or appearance until the experiment has concluded.
- **The best way to optimize the user experience for a business goal.**Sometimes you're implementing product changes to maximize a metric like revenue or retention. With A/B testing, you set your business objective, and Firebase performs the statistical analysis to determine if a variant is outperforming the baseline for your selected objective.

| **Note:** Real-timeRemote Configupdates aren't supported for A/B test parameter values. We recommend using[fetch and activate loading strategies](https://firebase.google.com/docs/remote-config/loading)forRemote Configexperiments.

To A/B test feature variants with a baseline, do the following:

1. Create your experiment.
2. Validate your experiment on a test device.
3. Manage your experiment.

| **Important:** Make sure you have the minimum SDK version forA/B Testing: Google Play Services 11.4.2 for Android and Firebase SDK for Apple platforms 4.5.0.

## Create an experiment

ARemote Configexperiment lets you evaluate multiple variants on one or more[Remote Configparameters](https://firebase.google.com/docs/remote-config/parameters).

1. Sign in to the[Firebaseconsole](https://console.firebase.google.com/project/_/settings/integrations)and verify thatGoogle Analyticsis enabled in your project so that the experiment has access toAnalyticsdata.

   If you did not enableGoogle Analyticswhen creating your project, you can enable it on the[**Integrations**](https://console.firebase.google.com/project/_/settings/integrations)tab, which you can access usingsettings**\>** **Project settings** in the[Firebaseconsole](https://console.firebase.google.com/).
2. In the**Engage** section of the[Firebaseconsole](https://console.firebase.google.com/)navigation menu, click**A/B Testing**.

3. Click**Create experiment** , and then select**Remote Config**when prompted for the service you want to experiment with.

4. Enter a**Name** and optional**Description** for your experiment, and click**Next**.

5. Fill out the**Targeting** fields, first choosing the app that uses your experiment. You can also target a subset of your users to participate in your experiment by clicking**and**, then choosing options from the following list:

   - **Version:**One or more versions of your app
   - **Build number:**The version code of the app
   - **Languages:**One or more languages and locales used to select users who might be included in the experiment
   - **Country/Region:**One or more countries or regions for selecting users who should be included in the experiment
   - **User audience:** Analyticsaudiences used to target users who might be included in the experiment
   - **User property:** One or moreAnalyticsuser properties for selecting users who might be included in the experiment
   - **First open:**Target users based on the first time they ever opened your app

     User targeting by first open time is available after you select an Android or iOS app. It is supported by the followingRemote ConfigSDK versions: Apple platforms SDK v9.0.0+ and Android SDK v21.1.1+ (Firebase BoMv30.3.0+).

     Analyticsmust also have been enabled on the client during the first open event.

   | **Note:** Due toGoogle Analytics[data processing latency](https://support.google.com/analytics/answer/1070983#DataProcessingLatency), experiments that targetAnalyticsuser audiences may require more time to accumulate data. To learn more about this and other targeting options, see[User targeting](https://firebase.google.com/docs/ab-testing/abtest-config#user-targeting).
6. Set the**Percentage of target users:** Enter the percentage of your app's user base matching the criteria set under**Target users**that you want to evenly divide between the baseline and one or more variants in your experiment. This can be any percentage between 0.01% and 100%. Users are randomly assigned to each experiment, including duplicated experiments.

7. Optionally, set an activation event to ensure that only the data from users who have first triggered someAnalyticsevent are counted in your experiment. Note that*all* users matching your targeting parameters will receiveRemote Configexperimental values, but only those who trigger an activation event will be included in your experiment results.

   To ensure a valid experiment, make sure that the event you choose occurs*after*your app activates fetched configuration values. In addition, the following events cannot be used because they always occur before fetched values are activated:
   - `app_install`
   - `app_remove`
   - `app_update`

   TheAnalyticsevent you select as the activation event must not also be used as the primary metric (or as an additional metric) in the same experiment. Doing so will trigger a validation error in the Firebase console and prevent your experiment from launching.
8. For the experiment's[**Goals**](https://firebase.google.com/docs/ab-testing/abtest-config#goal-metrics), select the primary metric to track, and add any additional metrics you want to track from the list. These include built-in objectives (purchases, revenue, retention, crash-free users, etc.),Analyticsconversion events, and otherAnalyticsevents. When finished, click**Next**.

9. In the**Variants** section, choose a baseline and at least one variant for the experiment. Use the**Choose or create new** list to add one or more parameters to experiment with. You can create a parameter that has not previously been used in theFirebaseconsole, but it must exist in your app for it to have any effect. You can repeat this step to add multiple parameters to your experiment.

10. (optional) To add more than one variant to your experiment, click**Add another variant**.

11. Change one or more parameters for specific variants. Any unchanged parameters are the same for users not included in the experiment.

12. Expand**Variant Weights** to view or change variant weight for the experiment. By default, each variant is weighted equally. Note that uneven weights may increase data collection time and**weights cannot be changed after the experiment begins**.

13. Click**Review**to save your experiment.

| **Note:** Once the experiment is running, you can check the[Parameters tab](https://console.firebase.google.com/project/_/config)of theFirebaseconsole to monitor the fetch percentage for your test variants versus the default value.

You are allowed up to 300 experiments per project, which could consist of up to 24 running experiments, with the rest as draft or completed.

## Validate your experiment on a test device

For each Firebase installation, you can retrieve the installation auth token associated with it. You can use this token to test specific experiment variants on a test device with your app installed. To validate your experiment on a test device, do the following:

1. Get the installation auth token as follows:  

   #### Swift

   ```swift
   do {
     let result = try await Installations.installations()
       .authTokenForcingRefresh(true)
     print("Installation auth token: \(result.authToken)")
   } catch {
     print("Error fetching token: \(error)")
   }
   ```

   #### Objective-C

   ```objective-c
   [[FIRInstallations installations] authTokenForcingRefresh:true
                                                  completion:^(FIRInstallationsAuthTokenResult *result, NSError *error) {
     if (error != nil) {
       NSLog(@"Error fetching Installation token %@", error);
       return;
     }
     NSLog(@"Installation auth token: %@", [result authToken]);
   }];
   ```

   ### Java

   ```java
   FirebaseInstallations.getInstance().getToken(/* forceRefresh */true)
           .addOnCompleteListener(new OnCompleteListener<InstallationTokenResult>() {
       @Override
       public void onComplete(@NonNull Task<InstallationTokenResult> task) {
           if (task.isSuccessful() && task.getResult() != null) {
               Log.d("Installations", "Installation auth token: " + task.getResult().getToken());
           } else {
               Log.e("Installations", "Unable to get Installation auth token");
           }
       }
   });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/MainActivity.java#L22-L32
   ```

   ### Kotlin

   ```kotlin
   val forceRefresh = true
   FirebaseInstallations.getInstance().getToken(forceRefresh)
       .addOnCompleteListener { task ->
           if (task.isSuccessful) {
               Log.d("Installations", "Installation auth token: " + task.result?.token)
           } else {
               Log.e("Installations", "Unable to get Installation auth token")
           }
       }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/installations/app/src/main/java/com/google/samples/snippet/kotlin/MainActivity.kt#L19-L27
   ```

   #### C++

   ```c++
   firebase::InitResult init_result;
   auto* installations_object = firebase::installations::Installations::GetInstance(
       firebase::App::GetInstance(), &init_result);
   installations_object->GetToken().OnCompletion(
       [](const firebase::Future<std::string>& future) {
         if (future.status() == kFutureStatusComplete &&
             future.error() == firebase::installations::kErrorNone) {
           printf("Installations Auth Token %s\n", future.result()->c_str());
         }
       });
   ```
   | For test device validation, the C++ API currently still uses the legacy instance ID token instead of an installation auth token.

   #### Unity

   ```c#
   Firebase.Installations.FirebaseInstallations.DefaultInstance.GetTokenAsync(forceRefresh: true).ContinueWith(
     task => {
       if (!(task.IsCanceled || task.IsFaulted) && task.IsCompleted) {
         UnityEngine.Debug.Log(System.String.Format("Installations token {0}", task.Result));
       }
     });
   ```
2. On the[Firebaseconsole](https://console.firebase.google.com/)navigation bar, click**A/B Testing**.
3. Click**Draft** (and/or**Running** for Remote Config experiments), hover over your experiment, click the context menu (*more_vert* ), and then click**Manage test devices**.
4. Enter the installation auth token for a test device and choose the experiment variant to send to that test device.
5. Run the app and confirm that the selected variant is being received on the test device.

To learn more aboutFirebaseinstallations, see[Manage Firebase installations](https://firebase.google.com/docs/projects/manage-installations).

## Manage your experiment

Whether you create an experiment withRemote Config, the Notifications composer, orFirebase In-App Messaging, you can then validate and start your experiment, monitor your experiment while it is running, and increase the number of users included in your running experiment.

When your experiment is done, you can take note of the settings used by the winning variant, and then roll out those settings to all users. Or, you can run another experiment.

### Start an experiment

1. In the**Engage** section of the[Firebaseconsole](https://console.firebase.google.com/)navigation menu, click**A/B Testing**.
2. Click**Draft**, and then click the title of your experiment.
3. To validate that your app has users who would be included in your experiment, expand the draft details and check for a number greater than**0%** in the**Targeting and distribution** section (for example,**1% of users matching the criteria**).
4. To change your experiment, click**Edit**.
5. To start your experiment, click**Start Experiment**. You can run up to 24 experiments per project at a time.

### Monitor an experiment

Once an experiment has been running for a while, you can check in on its progress and see what your results look like for the users who have participated in your experiment so far.

1. In the**Engage** section of the[Firebaseconsole](https://console.firebase.google.com/)navigation menu, click**A/B Testing**.
2. Click**Running**, and then click on, or search for, the title of your experiment. On this page, you can view various observed and modeled statistics about your running experiment, including the following:

   - **% difference from baseline**: A measure of the improvement of a metric for a given variant as compared to the baseline. Calculated by comparing the value range for the variant to the value range for the baseline.
   - **Probability to beat baseline**: The estimated probability that a given variant beats the baseline for the selected metric.
   - **<var translate="no">observed_metric</var>per user**: Based on experiment results, this is the predicted range that the metric value will fall into over time.
   - **Total<var translate="no">observed_metric</var>** : The observed cumulative value for the baseline or variant. The value is used to measure how well each experiment variant performs, and is used to calculate**Improvement** ,**Value range** ,**Probability to beat baseline** , and**Probability to be the best variant**. Depending on the metric being measured, this column may be labeled "Duration per user," "Revenue per user," "Retention rate," or "Conversion rate."
3. After your experiment has run for a while (at least 7 days forFCMandIn-App Messagingor 14 days forRemote Config), data on this page indicates which variant, if any, is the "leader." Some measurements are accompanied by a bar chart that presents the data in a visual format.

| **Tip:** You can sort by column and filter your A/B Testing experiments by name and experiment status.

### Roll out an experiment to all users

After an experiment has run long enough that you have a "leader," or winning variant, for your goal metric, you can release the experiment to 100% of users. This lets you select a variant to publish to all users moving forward. Even if your experiment has not created a clear winner, you can still choose to release a variant to all of your users.

1. In the**Engage** section of the[Firebaseconsole](https://console.firebase.google.com/)navigation menu, click**A/B Testing**.
2. Click**Completed** or**Running** , click an experiment that you want to release to all users, click the context menu (more_vert)**Roll out variant**.
3. Roll out your experiment to all users by doing one of the following:

   - For an experiment that uses**the Notifications composer** , use the**Roll out message**dialog to send the message to the remaining targeted users who were not part of the experiment.
   - For a**Remote Config** experiment, select a variant to determine whichRemote Configparameter values to update. The targeting criteria defined when creating the experiment is added as a new condition in your template, to ensure the rollout only affects users targeted by the experiment. After clicking**Review in Remote Config** to review the changes, click**Publish changes**to complete the rollout.
   - For an**In-App Messaging** experiment, use the dialog to determine which variant needs to be rolled out as a standaloneIn-App Messagingcampaign. Once selected, you are redirected to the FIAM compose screen to make any changes (if required) before publishing.

### Expand an experiment

If you find that an experiment isn't bringing in enough users forA/B Testingto declare a leader, you can increase distribution of your experiment to reach a larger percentage of the app's user base.

1. In the**Engage** section of the[Firebaseconsole](https://console.firebase.google.com/)navigation menu, click**A/B Testing**.
2. Select the running experiment that you want to edit.
3. In the**Experiment overview** , click the context menu (more_vert), and then click**Edit running experiment**.
4. The**Targeting** dialog displays an option to increase the percentage of users who are in the running experiment. Select a number greater than the current percentage and click**Publish**. The experiment will be pushed out to the percentage of users you have specified.

### Duplicate or stop an experiment

1. In the**Engage** section of the[Firebaseconsole](https://console.firebase.google.com/)navigation menu, click**A/B Testing**.
2. Click**Completed** or**Running** , hold the pointer over your experiment, click the context menu (more_vert), and then click**Duplicate experiment** or**Stop experiment**.

## User targeting

You can target the users to include in your experiment using the following user-targeting criteria.

| Targeting criterion |                                                Operator(s)                                                 |                                                                                                                                                                                          Value(s)                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                    Note                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| Version             | contains, does not contain, matches exactly, contains regex                                                | Enter a value for one or more app versions that you want to include in the experiment.                                                                                                                                                                                                                                                                                                     | When using any of the**contains** ,**does not contain** , or**matches exactly**operators, you can provide a comma-separated list of values. When using the**contains regex** operator, you can create regular expressions in[RE2](https://github.com/google/re2/wiki/Syntax)format. Your regular expression can match all or part of the target version string. You can also use the**\^** and**$**anchors to match the beginning, end, or entirety of a target string.                                                                                                                                                                                                                                                                    |
| User audience(s)    | includes all of, includes at least one of, does not include all of, does not include at least one of       | Select one or moreAnalyticsaudiences to target users who might be included in your experiment.                                                                                                                                                                                                                                                                                             | Some experiments that targetGoogle Analyticsaudiences may require a few days to accumulate data because they are subject toAnalytics[data processing latency](https://support.google.com/analytics/answer/1070983#DataProcessingLatency). You are most likely to encounter this delay with new users, who are typically enrolled into qualifying audiences 24-48 hours after creation, or for[recently-created audiences](https://support.google.com/analytics/answer/9267572#create-an-audience). ForRemote Config, this means that even if a user technically qualifies for an audience, ifAnalyticshas not yet added the user to the audience when \`fetchAndActivate()\` is executed, the user will not be included in the experiment. |
| User property       | **For text:** contains, does not contain, exactly matches, contains regex **For numbers:** \<, â¤, =, â¥, \> | AnAnalyticsuser property is used to select users who might be included in an experiment, with a range of options for selecting user property values. On the client, you can set only string values for user properties. For conditions that use numeric operators, theRemote Configservice converts the value of the corresponding user property into an integer/float.                    | When using the**contains regex** operator, you can create regular expressions in[RE2](https://github.com/google/re2/wiki/Syntax)format. Your regular expression can match all or part of the target version string. You can also use the**\^** and**$**anchors to match the beginning, end, or entirety of a target string.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Country/Region      | N/A                                                                                                        | One or more countries or regions used to select users who might be included in the experiment.                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Languages           | N/A                                                                                                        | One or more languages and locales used to select users who might be included in the experiment.                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| First open          | **Before** **After**                                                                                       | Target users based on the first time they open your app: - Select**New users**to target users who first open your app after a specified future date and time. - Select**Time range** to target users who first open your app within the range before or after the date and time you specify. Combine**Before** and**After**conditions to target users within a specific time range. <br /> | User targeting by first open is available after you select an Android or iOS app. It is currently supported by the followingRemote ConfigSDK versions: Apple platforms SDK v9.0.0+ and Android SDK v21.1.1+ (Firebase BoMv30.3.0+). Analyticsmust also have been enabled on the client during the first open event.                                                                                                                                                                                                                                                                                                                                                                                                                        |   |

## A/B Testingmetrics

When you create your experiment, you choose a primary, or*goal*metric, that is used to determine the winning variant. You should also track other metrics to help you better understand each experiment variant's performance and track important trends that may differ for each variant, like user retention, app stability and in-app purchase revenue. You can track up to five non-goal metrics in your experiment.

For example, say you're usingRemote Configto launch two different game flows in your app and want to optimize for in-app purchases and ad revenue, but you also want to track the stability and user retention of each variant. In this case, you might consider choosing**Estimated total revenue** as your goal metric because it includes in-app purchase revenue and ad revenue, and then, for**Other metrics to track**, you might add the following:

- To track your daily and weekly user retention, add**Retention (2-3 days)** and**Retention (4-7 days)**.
- To compare stability between the two game flows, add**Crash-free users**.
- To see more detailed views of each revenue type, add**Purchase revenue** and**Estimated ad revenue**.

| **Note:** Analytics events*only* appear in metrics lists if your app has triggered them. However, you can type the metric name in the**Select goal metric** field and click**Create event**to add it, and it will be used when your app triggers these events in the future.

The following tables provide details on how goal metrics and other metrics are calculated.

### Goal metrics

|         Metric          |                                                                 Description                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Crash-free users        | The percentage of users who have not encountered errors in your app that were detected by theFirebase CrashlyticsSDK during the experiment. |
| Estimated ad revenue    | Estimated ad earnings.                                                                                                                      |
| Estimated total revenue | Combined value for purchase and estimated ad revenues.                                                                                      |
| Purchase revenue        | Combined value for all`purchase`and`in_app_purchase`events.                                                                                 |
| Retention (1 day)       | The number of users who return to your app on a daily basis.                                                                                |
| Retention (2-3 days)    | The number of users who return to your app within 2-3 days.                                                                                 |
| Retention (4-7 days)    | The number of users who return to your app within 4-7 days.                                                                                 |
| Retention (8-14 days)   | The number of users who return to your app within 8-14 days.                                                                                |
| Retention (15+ days)    | The number of users who return to your app 15 or more days after they last used it.                                                         |
| first_open              | AnAnalyticsevent that triggers when a user first opens an app after installing or reinstalling it. Used as part of a conversion funnel.     |

### Other metrics

|        Metric        |                                                                                            Description                                                                                            |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| notification_dismiss | AnAnalyticsevent that triggers when a notification sent by the Notifications composer is dismissed (Android only).                                                                                |
| notification_receive | AnAnalyticsevent that triggers when a notification sent by the Notifications composer is received while the app is in the background (Android only).                                              |
| os_update            | AnAnalyticsevent that tracks when the device operating system is updated to a new version.To learn more, see[Automatically collected events](https://support.google.com/firebase/answer/6317485). |
| screen_view          | AnAnalyticsevent that tracks screens viewed within your app. To learn more, see[Track Screenviews](https://firebase.google.com/docs/analytics/screenviews).                                       |
| session_start        | AnAnalyticsevent that counts user sessions in your app. To learn more, see[Automatically collected events](https://support.google.com/firebase/answer/6317485).                                   |

<br />

## BigQuery data export

In addition to viewingA/B Testingexperiment data in theFirebaseconsole, you can inspect and analyze experiment data inBigQuery. WhileA/B Testingdoes not have a separateBigQuerytable, experiment and variant memberships are stored on everyGoogle Analyticsevent within theAnalyticsevent tables.

The user properties that contain experiment information are of the form`userProperty.key like "firebase_exp_%"`or`userProperty.key =
"firebase_exp_01"`where`01`is the experiment ID, and`userProperty.value.string_value`contains the (zero-based) index of the experiment variant.

You can use these experiment user properties to extract experiment data. This gives you the power to slice your experiment results in many different ways and independently verify the results ofA/B Testing.

To get started, complete the following as described in this guide:

1. [EnableBigQueryexport forGoogle Analyticsin the Firebase console](https://firebase.google.com/docs/ab-testing/abtest-config#enable-bigquery-export)
2. [AccessA/B Testingdata usingBigQuery](https://firebase.google.com/docs/ab-testing/abtest-config#access-abtesting-data)
3. [Explore example queries](https://firebase.google.com/docs/ab-testing/abtest-config#explore-example-queries)

### EnableBigQueryexport forGoogle Analyticsin the Firebase console

If you're on the Spark plan, you can use the[BigQuerysandbox](https://cloud.google.com/bigquery/docs/sandbox)to accessBigQueryat no cost, subject to[Sandbox limits](https://cloud.google.com/bigquery/docs/sandbox#limitations). See[Pricing and theBigQuerysandbox](https://firebase.google.com/docs/projects/bigquery-export?product=analytics#pricing)for more information.

First, make sure that you're exporting yourAnalyticsdata toBigQuery:

1. Open the[Integrations](https://console.firebase.google.com/project/_/settings/integrations)tab, which you can access usingsettings**\>** **Project settings** in the[Firebaseconsole](https://console.firebase.google.com/).
2. If you're already usingBigQuerywith other Firebase services, click**Manage** . Otherwise, click**Link**.
3. Review**About Linking Firebase toBigQuery** , then click**Next**.
4. In the**Configure integration** section, enable the**Google Analytics**toggle.
5. Select a region and choose export settings.

   | **Note:** For more information aboutGoogle AnalyticsforFirebasesettings, see[Data collection](https://support.google.com/analytics/answer/11593727).
6. Click**Link toBigQuery**.

Depending on how you chose to export data, it may take up to a day for the tables to become available. For more information about exporting project data toBigQuery, see[Export project data toBigQuery](https://firebase.google.com/docs/projects/bigquery-export?product=analytics).

### AccessA/B Testingdata inBigQuery

Before querying for data for a specific experiment, you'll want to obtain some or all of the following to use in your query:

- **Experiment ID:** You can obtain this from the URL of the**Experiment overview** page. For example, if your URL looks like`https://console.firebase.google.com/project/my_firebase_project/config/experiment/results/25`, the experiment ID is**25**.
- **Google Analyticsproperty ID** : This is your 9-digitGoogle Analyticsproperty ID. You can find this withinGoogle Analytics; it also appears inBigQuerywhen you expand your project name to show the name of yourGoogle Analyticsevent table (`project_name.analytics_000000000.events`).
- **Experiment date:** To compose a faster and more efficient query, it's good practice to limit your queries to theGoogle Analyticsdaily event table partitions that contain your experiment data---tables identified with a`YYYYMMDD`suffix. So, if your experiment ran from February 2, 2024 through May 2, 2024, you'd specify a`_TABLE_SUFFIX between
  '20240202' AND '20240502'`. For an example, see[Select a specific experiment's values](https://firebase.google.com/docs/ab-testing/abtest-config#select-a-specific-experiment).
- **Event names:** Typically, these correspond with your[goal metrics](https://firebase.google.com/docs/ab-testing/abtest-with-console#ab-testing-metrics)that you configured in the experiment. For example,`in_app_purchase`events,`ad_impression`, or`user_retention`events.

| **Tip:** If you're on the Blaze plan, Firebase can generate a sample query to extract the experiment name, variant, event name, and number of events for the experiment you select. Learn more at[Query experiment data using theFirebaseconsole's auto-generated query](https://firebase.google.com/docs/ab-testing/abtest-config#query-experiment-data-generated)

After you gather the information you need to generate your query:

1. Open[BigQuery](https://console.cloud.google.com/bigquery?project=_)in theGoogle Cloudconsole.
2. Select your project, then select**Create SQL query**.
3. Add your query. For example queries to run, see[Explore example queries](https://firebase.google.com/docs/ab-testing/abtest-config#explore-example-queries).
4. Click**Run**.

| **Tip:** While these steps describe using theGoogle Cloudconsole, you can also use the CLI or client libraries to queryBigQuery. Find out more in the[BigQuerydocumentation](https://cloud.google.com/bigquery/docs).

#### Query experiment data using the Firebase console's auto-generated query

If you're using the Blaze plan, the**Experiment overview**page provides a sample query that returns the experiment name, variants, event names, and the number of events for the experiment you're viewing.

To obtain and run the auto-generated query:

1. From theFirebaseconsole, open[**A/B Testing**](https://console.firebase.google.com/project/_/experiments/list)and select theA/B Testingexperiment you want to query to open the**Experiment overview**.
2. From the Options menu, beneath**BigQueryintegration** , select**Query experiment data** . This opens your project inBigQuerywithin theGoogle Cloudconsole console and provides a basic query you can use to query your experiment data.

The following example shows a generated query for an experiment with three variants (including the baseline) named "Winter welcome experiment." It returns the active experiment name, variant name, unique event, and event count for each event. Note that the query builder doesn't specify your project name in the table name, as it opens directly within your project.  

      /*
        This query is auto-generated by Firebase A/B Testing for your
        experiment "Winter welcome experiment".
        It demonstrates how you can get event counts for all Analytics
        events logged by each variant of this experiment's population.
      */
      SELECT
        'Winter welcome experiment' AS experimentName,
        CASE userProperty.value.string_value
          WHEN '0' THEN 'Baseline'
          WHEN '1' THEN 'Welcome message (1)'
          WHEN '2' THEN 'Welcome message (2)'
          END AS experimentVariant,
        event_name AS eventName,
        COUNT(*) AS count
      FROM
        `analytics_000000000.events_*`,
        UNNEST(user_properties) AS userProperty
      WHERE
        (_TABLE_SUFFIX BETWEEN '20240202' AND '20240502')
        AND userProperty.key = 'firebase_exp_25'
      GROUP BY
        experimentVariant, eventName

For additional query examples, proceed to[Explore example queries](https://firebase.google.com/docs/ab-testing/abtest-config#explore-example-queries).

### Explore example queries

The following sections provide examples of queries you can use to extractA/B Testingexperiment data fromGoogle Analyticsevent tables.

#### Extract purchase and experiment standard deviation values from all experiments

You can use experiment results data to independently verifyFirebase A/B Testingresults. The followingBigQuerySQL statement extracts experiment variants, the number of unique users in each variant, and sums total revenue from`in_app_purchase`and`ecommerce_purchase`events, and standard deviations for all experiments within the time range specified as the`_TABLE_SUFFIX`begin and end dates. You can use the data you obtain from this query with a statistical significance generator for one-tailed t-tests to verify that the results Firebase provides match your own analysis.

For more information about howA/B Testingcalculates inference, see[Interpret test results](https://firebase.google.com/docs/ab-testing/ab-concepts#interpreting-test-results).  

      /*
        This query returns all experiment variants, number of unique users,
        the average USD spent per user, and the standard deviation for all
        experiments within the date range specified for _TABLE_SUFFIX.
      */
      SELECT
        experimentNumber,
        experimentVariant,
        COUNT(*) AS unique_users,
        AVG(usd_value) AS usd_value_per_user,
        STDDEV(usd_value) AS std_dev
      FROM
        (
          SELECT
            userProperty.key AS experimentNumber,
            userProperty.value.string_value AS experimentVariant,
            user_pseudo_id,
            SUM(
              CASE
                WHEN event_name IN ('in_app_purchase', 'ecommerce_purchase')
                  THEN event_value_in_usd
                ELSE 0
                END) AS usd_value
          FROM `<var translate="no"><span class="devsite-syntax-n">PROJECT_NAME</span></var>.analytics_<var translate="no">ANALYTICS_ID</var>.events_*`
          CROSS JOIN UNNEST(user_properties) AS userProperty
          WHERE
            userProperty.key LIKE 'firebase_exp_%'
            AND event_name IN ('in_app_purchase', 'ecommerce_purchase')
            AND (_TABLE_SUFFIX BETWEEN '<var translate="no">YYYYMMDD</var>' AND '<var translate="no">YYYMMDD</var>')
          GROUP BY 1, 2, 3
        )
      GROUP BY 1, 2
      ORDER BY 1, 2;

#### Select a specific experiment's values

The following example query illustrates how to obtain data for a specific experiment inBigQuery. This sample query returns the experiment name, variant names (including Baseline), event names, and event counts.  

      SELECT
        '<var translate="no">EXPERIMENT_NAME</var>' AS experimentName,
        CASE userProperty.value.string_value
          WHEN '0' THEN 'Baseline'
          WHEN '1' THEN '<var translate="no">VARIANT_1_NAME</var>'
          WHEN '2' THEN '<var translate="no">VARIANT_2_NAME</var>'
          END AS experimentVariant,
        event_name AS eventName,
        COUNT(*) AS count
      FROM
        `analytics_<var translate="no">ANALYTICS_PROPERTY</var>.events_*`,
        UNNEST(user_properties) AS userProperty
      WHERE
        (_TABLE_SUFFIX BETWEEN '<var translate="no">YYYMMDD</var>' AND '<var translate="no">YYYMMDD</var>')
        AND userProperty.key = 'firebase_exp_<var translate="no">EXPERIMENT_NUMBER</var>'
      GROUP BY
        experimentVariant, eventName