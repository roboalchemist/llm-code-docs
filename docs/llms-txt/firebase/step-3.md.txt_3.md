# Source: https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-3.md.txt

# Tutorial: Optimize AdMob ad frequency

## Step 3: Handle Remote Config parameter values in your app's code

<br />

|---|
| Introduction: [Optimize AdMob ad frequency using Firebase](https://firebase.google.com/docs/tutorials/optimize-ad-frequency) |
| Step 1: [Use AdMob to create new ad unit variants for testing](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-1) |
| Step 2: [Set up an A/B test in the Firebase console](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2) |
| **Step 3: Handle Remote Config parameter values in your app's code** <br /> |
| Step 4: [Start the A/B test and review the test results in the Firebase console](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-4) |
| Step 5: [Decide whether to roll out the new ad format](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-5) |

<br />

At the end of the last step, you created a Remote Config parameter
(`INTERSTITIAL_AD_KEY`). In this step, you'll add the logic to your app's code
for what your app should display based on the value of that parameter.

### **Add the required SDKs**

Before using Remote Config in your application code, add both the
Remote Config SDK and the Firebase SDK for Google Analytics to
your project build files.

### Swift

Add and install the following pods in your podfile:

    pod 'Google-Mobile-Ads-SDK'
    pod 'Firebase/Analytics'
    pod 'Firebase/RemoteConfig'

### Objective-C

Add and install the following pods in your podfile:

    pod 'Google-Mobile-Ads-SDK'
    pod 'Firebase/Analytics'
    pod 'Firebase/RemoteConfig'

### Android

Add the following library dependencies to your `build.gradle` file:

    implementation 'com.google.android.gms:play-services-ads:25.0.0'
    implementation 'com.google.firebase:firebase-analytics:23.0.0'
    implementation 'com.google.firebase:firebase-config:23.0.1'

### Unity

Download and install the Firebase Unity SDK, then add the following Unity
packages to your project:

- `FirebaseAnalytics.unitypackage`
- `FirebaseRemoteConfig.unitypackage`

### **Configure Remote Config instance**

To use the Remote Config parameter values, configure the
Remote Config instance so that it's set up to fetch new values for the
client app instance.

In this example, Remote Config is configured to check for new parameter
values once every hour.

### Swift

    remoteConfig = RemoteConfig.remoteConfig()
    let settings = RemoteConfigSettings()
    settings.minimumFetchInterval = 3600
    remoteConfig.configSettings = settings

### Objective-C

    self.remoteConfig = [FIRRemoteConfig remoteConfig];
    FIRRemoteConfigSettings *remoteConfigSettings = [[FIRRemoteConfigSettings alloc] init];
    remoteConfigSettings.minimumFetchInterval = 3600;
    self.remoteConfig.configSettings = remoteConfigSettings;

### Java

    mFirebaseRemoteConfig = FirebaseRemoteConfig.getInstance();
    FirebaseRemoteConfigSettings configSettings = new FirebaseRemoteConfigSettings.Builder()
            .setMinimumFetchIntervalInSeconds(3600)
            .build();
    mFirebaseRemoteConfig.setConfigSettingsAsync(configSettings);

### Kotlin

    remoteConfig = Firebase.remoteConfig
    val configSettings = remoteConfigSettings {
        minimumFetchIntervalInSeconds = 3600
    }
    remoteConfig.setConfigSettingsAsync(configSettings)

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

Fetch and activate the Remote Config parameters so that it can start using
the new parameter values.

You'll want to make this call as early as possible in your app's loading phase
because this call is asynchronous and you'll need the Remote Config value
pre-fetched so that your app knows which ad to show.

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

### Objective-C

    [self.remoteConfig fetchWithCompletionHandler:^(FIRRemoteConfigFetchStatus status, NSError *error) {
        if (status == FIRRemoteConfigFetchStatusSuccess) {
            NSLog(@"Config fetched!");
          [self.remoteConfig activateWithCompletion:^(BOOL changed, NSError * _Nullable error) {
            // ...
          }];
        } else {
            NSLog(@"Config not fetched");
            NSLog(@"Error %@", error.localizedDescription);
        }
        [self loadAdUnit];
    }];

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

### Unity

    remoteConfig.FetchAndActivateAsync().ContinueWithOnMainThread(task => {
      if (task.IsFaulted) {
        Debug.LogWarning("Config params failed to update");
      } else {
        Debug.Log("Config params updated: " + task.Result);
      }
      LoadAdUnit();
    });

Your app is now ready to handle the Remote Config parameter that you created
during the A/B test set up earlier in this tutorial.

### **Use the Remote Config parameter value**

Use the pre-fetched Remote Config value in the `loadAdUnit()` function to
determine which ad frequency variant should be shown for this app instance.

### Swift

    private func loadAdUnit() {
      let adUnitId = remoteConfig["INTERSTITIAL_AD_KEY"].stringValue;
      let request = GADRequest()
      GADInterstitialAd.load(withAdUnitID: adUnitId,
                                   request: request,
                         completionHandler: { [self] ad, error in
                           if let error = error {
                             print("Failed to load: \(error.localizedDescription)")
                             return
                           }
                           interstitial = ad
                           // Register for callbacks.
                         }
      )
    }

    // Register for callbacks.

### Objective-C

    - (void)loadAdUnit {
        NSString *adUnitId =
          self.remoteConfig[@"INTERSTITIAL_AD_KEY"].stringValue;

      GADRequest *request = [GADRequest request];
      [GADInterstitialAd loadAdWithAdUnitId:adUnitId
                             request:request
                             completionHandler:^(GADInterstitialAd *ad,
                                 NSError *error) {
        if (error) {
          NSLog(@"Failed to load interstitial ad with error: %@",
            [error localizedDescription]);
          return;
        }

        self.interstitial = ad;
      }];
    }

### Java

    private void loadAdUnit() {
        String adUnitId =
          mFirebaseRemoteConfig.getString("INTERSTITIAL_AD_KEY");

        // Load Interstitial Ad (assume adUnitId not null)
        AdRequest adRequest = new AdRequest.Builder().build();

        InterstitialAd.load(this, adUnitId, adRequest, new
            InterstitialAdLoadCallback() {
              @Override
              public void onAdLoaded(@NonNull InterstitialAd intertitialAd) {
                mInterstitialAd = interstitialAd;
              }

              @Override
              public void onAdFailedToLoad(@NonNull LoadAdError loadAdError) {
                mInterstitialAd = null;
              }
        });
    }

### Kotlin

    private fun loadAdUnit() {
      String adUnitId = remoteConfig.getString("INTERSTITIAL_AD_KEY")
      var adRequest = AdRequestBuilder.Builder().build()

      AdRequestBuilder.load(this, adUnitId, adRequest, object :
        InterstitialAdLoadCallback() {
          override fun onAdFailedToLoad(adError: LoadAdError) {
            mInterstitialAd = null
          }

          override fun onAdLoaded(interstitialAd: InterstitialAd) {
            mInterstitialAd = interstitialAd
          }
        })
    }

### Unity

    void LoadAdUnit() {

      // Note that you may want to encode and parse two sets of ad unit IDs for
      // Android / iOS in the Unity implementation.
      String adUnitId = remoteConfig.GetValue("INTERSTITIAL_AD_KEY").StringValue;
      this.interstitial = new InterstitialAd(adUnitId);
    }

> [!NOTE]
> **Note:** In production code, you should also add a type and null check on retrieved Remote Config parameter values.

### **Add other checks for the parameter value**

There are other areas in your application code where you'll need to check the
value of this Remote Config parameter to dictate which ad experience will be
loaded. For example, you can decide whether to reload an ad after the user has
finished viewing the current one.

The fetch and activate calls should be made first to get any parameter value
changes --- for example, if you decide to end or create a new experiment.

From there, you can always check the value for the parameter using the
following calls:

### Swift

    remoteConfig["INTERSTITIAL_AD_KEY"].stringValue

### Objective-C

    self.remoteConfig[@"INTERSTITIAL_AD_KEY"].stringValue;

### Java

    mFirebaseRemoteConfig.getString(INTERSTITIAL_AD_KEY)

### Kotlin

    remoteConfig.getString(INTERSTITIAL_AD_KEY)

### Unity

    remoteConfig.GetValue("INTERSTITIAL_AD_KEY").StringValue

These calls will always return the same value for an app instance depending on
whether it was placed in the control group or one of the new ad variant groups,
unless any changes were made in the Firebase console that were fetched and
activated in the previous calls.

<br />

*** ** * ** ***

<br />

[**Step 2** : Set up an A/B test in the Firebase console](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-2)
[**Step 4** : Start the A/B test \& review test results](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/step-4)

<br />

*** ** * ** ***