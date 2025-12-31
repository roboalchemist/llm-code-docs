# Source: https://firebase.google.com/docs/ab-testing/abtest-inappmessaging.md.txt

<br />

When you are reaching out to your users or starting a new marketing campaign, you want to make sure that you get it right. A/B testing can help you find the optimal wording and presentation by testing message variants on selected portions of your user base. Whether your goal is better retention or conversion on an offer, A/B testing can perform statistical analysis to determine if a message variant is outperforming the baseline for your selected objective.

To A/B test feature variants with a baseline, do the following:

1. Create your experiment.
2. Validate your experiment on a test device.
3. Manage your experiment.

| **Important:** Make sure you have the minimum SDK version forA/B Testing: Google Play Services 11.4.2 for Android and Firebase SDK for Apple platforms 4.5.0.

## Create an experiment

An experiment that usesFirebase In-App Messaginglets you evaluate multiple variants of a single in-app message.

1. Sign in to the[Firebaseconsole](https://console.firebase.google.com/project/_/settings/integrations)and verify thatGoogle Analyticsis enabled in your project so that the experiment has access toAnalyticsdata.

   If you did not enableGoogle Analyticswhen creating your project, you can enable it on the[**Integrations**](https://console.firebase.google.com/project/_/settings/integrations)tab, which you can access usingsettings**\>** **Project settings** in the[Firebaseconsole](https://console.firebase.google.com/).
2. In the**Engage** section of the[Firebaseconsole](https://console.firebase.google.com/)navigation menu, click**A/B Testing**.

3. Click**Create experiment** , and then select**In-App Messaging**when prompted for the service you want to experiment with.

4. Alternatively, on the[Firebaseconsole](https://console.firebase.google.com/)navigation menu, expand**Engage** , then click**In-App Messaging** . Then click**New experiment**.

5. Enter a**Name** and optional**Description** for your experiment, and click**Next**.

6. Fill out the**Targeting**fields, first choosing the app that uses your experiment. You can also target a subset of your users to participate in your experiment by choosing options that include the following:

   - **Version:**One or more versions of your app
   - **User audience:** Analyticsaudiences used to target users who might be included in the experiment
   - **User property:** One or moreAnalyticsuser properties for selecting users who might be included in the experiment
   - **Country/Region:**One or more countries or regions for selecting users who might be included in the experiment
   - **Device language:**One or more languages and locales used to select users who might be included in the experiment
   - **First open:**Target users based on the first time they ever opened your app
   - **Last app engagement:**Target users based on the last time they engaged with your app

   | **Note:** Experiments that targetAnalyticsuser audiences may take between 24-48 hours to accumulate data. To learn more about this and other targeting options, see[User targeting](https://firebase.google.com/docs/ab-testing/abtest-inappmessaging#user-targeting).
7. Set the**Percentage of target users:** Select the percentage of your app's user base matching the criteria set under**Target users**that you want to evenly divide between the baseline and one or more variants in your experiment. This can be any percentage between 0.01% and 100%. Percentages are randomly reassigned to users for each experiment, including duplicated experiments.

8. In the**Variants** section, configure a baseline in-app message to send to the baseline group using the[message design interface](https://firebase.google.com/docs/in-app-messaging/compose-campaign)you use for a normal in-app messaging campaign.

9. To add a variant to your experiment, click**Add Variant**. By default, experiments have one baseline and one variant.

10. (optional) Enter a more descriptive name for each variant.

11. (optional) At the top of the**Variants** section, click the**Compare variants**button to compare one more message variants side-by-side with the baseline message.

12. Define a goal metric for your experiment to use when evaluating experiment variants along with any additional metrics you want to use from the list. These metrics include built-in objectives (engagement, purchases, revenue, retention, etc.),Analyticsconversion events, and otherAnalyticsevents.

13. Configure scheduling for the experiment:

    - Set a**Start** and**End**date for the experiment.
    - Set how in-app messages are triggered across all variants.
14. Click**Review**to save your experiment.

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

| Targeting criterion |                                                Operator(s)                                                 |                                                                                                                                                                                Value(s)                                                                                                                                                                                 |                                                                                                                                                                                                                                                Note                                                                                                                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version             | contains, does not contain, matches exactly, contains regex                                                | Enter a value for one or more app versions that you want to include in the experiment.                                                                                                                                                                                                                                                                                  | When using any of the**contains** ,**does not contain** , or**matches exactly**operators, you can provide a comma-separated list of values. When using the**contains regex** operator, you can create regular expressions in[RE2](https://github.com/google/re2/wiki/Syntax)format. Your regular expression can match all or part of the target version string. You can also use the**\^** and**$**anchors to match the beginning, end, or entirety of a target string.                            |
| User audience(s)    | includes all of, includes at least one of, does not include all of, does not include at least one of       | Select one or moreAnalyticsaudiences to target users who might be included in your experiment.                                                                                                                                                                                                                                                                          | Some experiments that targetGoogle Analyticsaudiences may require a few days to accumulate data because they are subject toAnalytics[data processing latency](https://support.google.com/analytics/answer/1070983#DataProcessingLatency). You are most likely to encounter this delay with new users, who are typically enrolled into qualifying audiences 24-48 hours after creation, or for[recently-created audiences](https://support.google.com/analytics/answer/9267572#create-an-audience). |
| User property       | **For text:** contains, does not contain, exactly matches, contains regex **For numbers:** \<, â¤, =, â¥, \> | AnAnalyticsuser property is used to select users who might be included in an experiment, with a range of options for selecting user property values. On the client, you can set only string values for user properties. For conditions that use numeric operators, theRemote Configservice converts the value of the corresponding user property into an integer/float. | When using the**contains regex** operator, you can create regular expressions in[RE2](https://github.com/google/re2/wiki/Syntax)format. Your regular expression can match all or part of the target version string. You can also use the**\^** and**$**anchors to match the beginning, end, or entirety of a target string.                                                                                                                                                                        |
| Country/Region      | N/A                                                                                                        | One or more countries or regions used to select users who might be included in the experiment.                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Languages           | N/A                                                                                                        | One or more languages and locales used to select users who might be included in the experiment.                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| First open          | More than Less than Between                                                                                | Target users based on the first time they ever opened your app, specified in days.                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Last app engagement | More than Less than Between                                                                                | Target users based on the last time they engaged with your app, specified in days.                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## A/B Testingmetrics

When you create your experiment, you choose a primary, or*goal*metric, that is used to determine the winning variant. You should also track other metrics to help you better understand each experiment variant's performance and track important trends that may differ for each variant, like user retention, app stability and in-app purchase revenue. You can track up to five non-goal metrics in your experiment.
For example, say you've added new in-app purchases to your app and want to compare the effectiveness of two different "nudge" messages. In this case, you might decide to choose to set**Purchase revenue** as your goal metric because you want the winning variant to represent the notification that resulted in the highest in-app purchase revenue. And because you also want to track which variant resulted in more future conversions and retained users, you might add the following in**Other metrics to track** :

<br />

- **Estimated total revenue**to see how your combined in-app purchase and ad revenue differs between the two variants
- **Retention (1 day)** ,**Retention (2-3 days)** ,**Retention (4-7 days)**to track your daily/weekly user retention

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