# Source: https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-3.md.txt

# Tutorial: Optimize hybrid monetization using AdMob, Google Analytics, and Firebases

## Step 3: Set up Firebase Remote Config to show specific ads experiences

<br />

|---|
| Introduction: [Optimize hybrid monetization using AdMob, Google Analytics, and Firebase](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization) |
| Step 1: Use AdMob to create new ad units for display |
| Step 2: [Set up Google Analytics](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-2) |
| **Step 3: [Set up Firebase Remote Config to show specific ads experiences](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-3)** <br /> |

<br />

At the end of the last step, you learned about Google Analytics audiences. In
this step, you'll create a Remote Config boolean-controlled parameter
(called `ad_control_switch`) that leverages the "Purchasers" audience. You'll
then add the logic to your app's code for what your app should display based on
the value of that parameter.

### **Set up Remote Config parameters and conditions in the Firebase console**

1. In the [Firebase console](https://console.firebase.google.com/),
   open your Firebase project.

2. In the left-side pane, expand the **Engage** section, and then select
   **Remote Config**.

3. Click **Create configuration** (or **Add parameter** if you've used
   Remote Config before).

4. In the *Create parameter* panel, complete the following steps:

   1. In the *Parameter name* field, enter `ad_control_switch`.

   2. From the `Data type` dropdown menu, select **Boolean**.

   3. Click **Create new** , and then select **Create new condition**.

5. In the *Define a new condition* dialog, complete the following steps:

   1. In the *Name* field, enter `Purchasers Group` (or any other easily
      identifiable name for the condition).

   2. From the *Applies if...* dropdown menu, select **User audience(s)**.

   3. From the *Select audiences(s)* dropdown menu, select **Purchasers**.

   4. Click **Save condition**.

6. Back in the *Create parameter* panel, complete the following steps:

   1. For the *Value* of *Purchasers Group* , select **false**.

   2. For the *Default value* , select **true**.

7. Click **Save** , and then **Publish changes**.

This configuration will check if the user is in the "Purchasers" audience
(that is, they are a paying user):

- If the user is in the "Purchasers" audience, then Remote Config will
  return the value of `false` for the `ad_control_switch` parameter.

- If the user is **not** in the "Purchasers" audience, then Remote Config
  will return the value of `true` for the `ad_control_switch` parameter.

In the following steps, you will implement Remote Config in your app to
handle these parameter values.

### **Add the Remote Config SDK to your app**

Before using Remote Config in your application code, add the
Remote Config SDK to your app's codebase. Note that your app should already
have the Google Mobile Ads (AdMob) SDK and the
Google Analytics for Firebase SDK from previous steps of this tutorial.

### Swift

Add and install the Remote Config pod in your podfile:

    pod 'Firebase/RemoteConfig'

### Android

Add the Remote Config library dependency to your `build.gradle` file:

    implementation 'com.google.firebase:firebase-config:23.0.1'

### Flutter

From the root of your Flutter project, run the following command to install
the Remote Config plugin:

    flutter pub add firebase_remote_config

### Unity

Download and install the latest
[Firebase Unity SDK](https://firebase.google.com/download/unity), and then add
the Remote Config package to your project:  

`FirebaseRemoteConfig.unitypackage`

### **Configure the Remote Config instance**

So that you app can use the Remote Config parameter values, configure the
Remote Config instance so that it can fetch new values for the client app
instance.

In this example, Remote Config is configured to check for new parameter
values once every hour.

### Swift

    remoteConfig = RemoteConfig.remoteConfig()
    let settings = RemoteConfigSettings()
    settings.minimumFetchInterval = 3600
    remoteConfig.configSettings = settings

### Kotlin

    remoteConfig = Firebase.remoteConfig
    val configSettings = remoteConfigSettings {
        minimumFetchIntervalInSeconds = 3600
    }
    remoteConfig.setConfigSettingsAsync(configSettings)

### Java

    mFirebaseRemoteConfig = FirebaseRemoteConfig.getInstance();
    FirebaseRemoteConfigSettings configSettings = new FirebaseRemoteConfigSettings.Builder()
            .setMinimumFetchIntervalInSeconds(3600)
            .build();
    mFirebaseRemoteConfig.setConfigSettingsAsync(configSettings);

### Flutter

    remoteConfig = FirebaseRemoteConfig.instance;
      final configSettings = FirebaseRemoteConfigSettings(
        minimumFetchInterval: Duration(hours: 1),
      );
      await remoteConfig.setConfigSettings(configSettings);

      // Use the `onConfigUpdated` callback to listen for changes to the config settings.
      remoteConfig.onConfigUpdated.listen((_) {
        print('Config settings confirmed');
      });

### Unity

    var remoteConfig = FirebaseRemoteConfig.DefaultInstance;
    var configSettings = new ConfigSettings {
      MinimumFetchInternalInMilliseconds =
            (ulong)(new TimeSpan(1, 0, 0).TotalMilliseconds)
    };
    remoteConfig.SetConfigSettingsAsync(configSettings)
            .ContinueWithOnMainThread(task => {
              Debug.Log("Config settings confirmed");
    }

### **Fetch and activate Remote Config**

Fetch and activate the Remote Config parameter so that it can start using
the new parameter values.

You want to make this call as early as possible in your app's loading phase
because this call is asynchronous and you need the Remote Config value
pre-fetched so that your app knows whether to show an ad.

### Swift

    remoteConfig.fetch() { (status, error) -> Void in
      if status == .success {
        print("Config fetched!")
        self.remoteConfig.activate() { (changed, error) in
          // ...
        }
      } else {
        print("Config not fetched")
        print("Error: \(error?.localizedDescription ?? "No error available.")")
      }
      self.loadAdUnit()
    }

### Kotlin

    remoteConfig.fetchAndActivate()
            .addOnCompleteListener(this) { task ->
                if (task.isSuccessful) {
                    val updated = task.result
                    Log.d(TAG, "Config params updated: $updated")
                } else {
                    Log.d(TAG, "Config params failed to update")
                }
                loadAdUnit()
            }

### Java

    mFirebaseRemoteConfig.fetchAndActivate()
            .addOnCompleteListener(this, new OnCompleteListener<Boolean>() {
                @Override
                public void onComplete(@NonNull Task<Boolean> task) {
                    if (task.isSuccessful()) {
                        boolean updated = task.getResult();
                        Log.d(TAG, "Config params updated: " + updated);
                    } else {
                        Log.d(TAG, "Config params failed to update");
                    }
                    loadAdUnit();
                }
            });

### Flutter

    remoteConfig = FirebaseRemoteConfig.instance;

    // Fetch and activate the latest Remote Config values.
    final updated = await remoteConfig.fetchAndActivate();

    // Check if the config params were updated successfully.
    if (updated) {
      print('Config params updated');
    } else {
      print('Config params failed to update');
    }

    // Load the ad unit.
    _loadAdUnit();

### Unity

    remoteConfig.FetchAndActivateAsync().ContinueWithOnMainThread(task => {
      if (task.IsFaulted) {
        Debug.LogWarning("Config params failed to update");
      } else {
        Debug.Log("Config params updated: " + task.Result);
      }
      LoadAdUnit();
    });

Your app is now configured to handle the Remote Config parameter that you
created earlier in this step.

### **Use the Remote Config parameter value**

Use the pre-fetched Remote Config value in the `loadAdUnit()` function to
determine whether the app instance should do one of the following:

- The `ad_control_switch` parameter value resolves to `true`: show the
  interstitial ad (because the user is a non-paying user).

- The `ad_control_switch` parameter value resolves to `false`: do not show the
  ad (because the user is a paying user).

### Swift

    private func loadAdUnit() {
      let showAds = remoteConfig["ad_control_switch"].boolValue

      if showAds {
        // Load interstitial ad (implemented ad unit)
        // per AdMob instructions (the first step of this tutorial).
      } else {
        // Don't show ads.
      }
    }

### Kotlin

    private fun loadAdUnit() {
      var showAds = remoteConfig.getBoolean(ad_control_switch)

      if (showAds) {
          // Load interstitial ad (implemented ad unit)
          // per AdMob instructions (the first step of this tutorial).
        } else {
          // Don't show ads.
        }
    }

### Java

    private void loadAdUnit() {
        boolean showAds =
          mFirebaseRemoteConfig.getBoolean(ad_control_switch);

        if (showAds) {
          // Load interstitial ad (implemented ad unit)
          // per AdMob instructions (the first step of this tutorial).
        } else {
          // Don't show ads.
        }
    }

### Flutter

    void _loadAdUnit() {
      bool showAds = remoteConfig.getBool(ad_control_switch);

      if (showAds) {
        // Load interstitial ad (implemented ad unit)
        // per AdMob instructions (the first step of this tutorial).
      } else {
        // Don't show ads.
      }
    }

### Unity

    void LoadAdUnit() {
      bool showAds =
          remoteConfig.GetValue("ad_control_switch").BooleanValue;

      if (showAds) {
        // Load interstitial ad (implemented ad unit)
        // per AdMob instructions (the first step of this tutorial).
      } else {
        // Don't show ads.
      }
    }

> [!NOTE]
> **Note:** In production code, you should also add a type and null check on retrieved Remote Config parameter values.

### **Release your app**

Since the logic for showing the ad or not is within your codebase, you need to
release a new version of your app that contains this logic.

If you followed the steps of this tutorial, your app should immediately start
serving a customized in-app ads experience to your users. You can monitor your
ads revenue in both your AdMob account and in the Google Analytics
dashboards (either in the Firebase console or the Google Analytics UI).

<br />

And that's it! You've completed the tutorial for optimizing hybrid monetization
using AdMob, Google Analytics, and Firebase.

## Related resources

- Check out another solution guides:

  - [Test ad format adoption using Firebase](https://firebase.google.com/docs/tutorials/test-ad-format-adoption)
  - [Optimize ad frequency using Firebase](https://firebase.google.com/docs/tutorials/optimize-ad-frequency)
- Watch a video series: [Optimize your app revenue with Firebase and
  AdMob](https://www.youtube.com/watch?v=9lYjl5dz6F0&list=PLl-K7zZEsYLlNxt9KQJ0YGPPJjkoDBEy9)

<br />

*** ** * ** ***

<br />

[**Step 2**: Set up Google Analytics](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-2)

<br />

*** ** * ** ***