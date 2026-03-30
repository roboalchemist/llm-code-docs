# Source: https://firebase.google.com/docs/remote-config/rollouts/get-started.md.txt

# Get started with Remote Config rollouts

<button value="android">Android</button> <button value="ios" default="">iOS+</button>   

With Remote Config rollouts, you can safely and gradually release new features and updates
to your app. With rollouts, you can control the release of new app features by
targeting specific user groups. Like A/B testing, in a rollout, the enabled
group is measured against an equal sized control group for meaningful
comparisons in the results.

## Step 1: Instrument your App with Remote Config, Crashlytics, and Google Analytics

Before you can start using Remote Config rollouts to gradually launch new features to your
users, your app should be instrumented with Firebase Remote Config,
Crashlytics, and Google Analytics.

1. Follow the instructions in [Get started with Remote
   Config](https://firebase.google.com/docs/remote-config/get-started) to add Remote Config and Analytics to your app and create a Remote Config template. You'll need to ensure that you're using Firebase BoM v32.6.0+ (Remote Config SDK v21.6.0+).
2. Follow the instructions in [Get started with
   Crashlytics](https://firebase.google.com/docs/crashlytics/get-started) to add Crashlytics to your app. Be sure to implement Firebase iOS SDK v10.24.0+.

For optimal performance, we recommend implementing [real-time Remote
Config](https://firebase.google.com/docs/remote-config/ios/real-time) in your apps to ensure that rollout
values are fetched as soon as they're published.

## Step 2: Configure a rollout in the Firebase console

After your app is instrumented with Remote Config, Crashlytics, and
Analytics, you can use the Firebase console to create a rollout.

1. In the **Firebase console** , navigate to **Remote Config** , then open [**Rollouts**](https://console.firebase.google.com/project/_/config/rollouts).
2. Click **Create rollout**.
3. In the **Parameter** field, select an existing parameter or create a new parameter to update with your rollout, then click **Next**.
4. Create or select a **Target condition** . This condition defines which
   devices will be added to the rollout-enabled and control groups. See
   [Understand rollout group
   membership](https://firebase.google.com/docs/remote-config/rollouts/about#understand-group-membership)
   for more information about how rollout-enabled and control groups are
   assigned to users.

   > [!TIP]
   > **Tip:** For successful rollout results, we recommend choosing a condition that targets a single app. This will make it easier to compare results, in both Remote Config and Crashlytics, across the Control and Enabled groups.

5. Click **Next** , and in the **Enabled value** field, add the value you want
   to release to your users.

6. In the **Random percentage** field, enter the total percentage of devices
   that should receive the enabled value. Because Firebase assigns an
   equal-sized control group to ensure an accurate comparison of results when
   measuring the performance of your enabled feature, this value must be 50% or
   less, unless you roll out to 100%. Note that this value is bound by your
   conditions: for example, if you configured a condition that only rolled out
   to version 2.0 of your app, and 30% of your user base have adopted v2.0,
   setting this value to 50% would mean that 15% of your total user base would
   get the rollout value.

7. Click **Next** and provide a **Name** and, optionally, a **Description** ,
   then click **Save**.

8. To start the rollout, click **Publish changes** , review the changed
   parameters, then click **Publish changes** again.

Your rollout should begin and you should be able to view results almost
immediately.

## Next steps

- Learn more about rollout results at [Understand rollout
  results](https://firebase.google.com/docs/remote-config/rollouts/about#understand-results).