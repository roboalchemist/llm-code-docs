# Source: https://firebase.google.com/docs/admob/cpp/admob-migration.md.txt

<br />

| **DEPRECATED:** The Google Mobile Ads C++ SDK is*deprecated* as of June 17, 2024 and should not be adopted in projects that don't already use it. It will enter*End-of-Maintenance (EoM)* on June 17, 2025. Note that versions of the SDK released before the EoM date will continue to function, but no further bug fixes or changes will be released after the EoM date.
|
| Instead of the Google Mobile Ads C++ SDK, consider using the[iOS](https://firebase.google.com/docs/admob/ios/quick-start)and[Android](https://firebase.google.com/docs/admob/android/quick-start)SDKs fromAdMob. For support, reach out to the[Google Mobile Ads SDK Technical Forum](https://groups.google.com/g/google-admob-ads-sdk).

<br />

The release of theFirebaseC++SDK v9.1.0 introduces a new Google Mobile Ads C++ SDK.

The Google Mobile Ads C++ SDK is a new API surface that incorporates the major breaking changes made to the Firebase AdMob C++ SDKs for iOS and Android in 2021 and 2022, including the removal of deprecated APIs, and a new flow when working with full screen ad types.

The old Firebase AdMob C++ SDK (`firebase::admob`) has been marked deprecated and will not be receiving any updates or bug fixes moving forward.

Both the new Google Mobile Ads C++ SDK (`firebase::gma`) and the old Firebase AdMob C++ SDK (`firebase::admob`) will remain part of the build archives for theFirebaseC++SDK during the Firebase AdMob C++ SDK deprecation window.

## Legacy API removal

The following APIs have been removed from the Google Mobile Ads C++ SDK in their entirety.

### `RewardedVideoAd`

AdMob's`RewardedVideoAd`namespace has been replaced with`RewardedAd`class.`RewardedAd`behaves similarly to`InterstitialAd`but includes an additional`RewardedAdListener`to receive notification of item rewards.

### `NativeExpressAds`

AdMob's`NativeExpressAd`had already been marked as deprecated in each Firebase AdMob C++ SDK. Therefore`NativeExpressAd`is not included in the new Google Mobile Ads C++ SDK.

## SDK namespace change

The SDK has relocated to a new namespace, and it has a new directory structure:

### Namespace`firebase::gma`

The sources of the new Google Mobile Ads C++ SDK are in the`firebase::gma`namespace. The older`firebase::admob`namespace has been deprecated along with the Firebase AdMob C++ SDK.

### Directory structure

Header files have moved to a new directory inside the build archive:

| Deprecated Firebase AdMob C++ SDK | New Google Mobile Ads C++ SDK |
|-----------------------------------|-------------------------------|
| `include/firebase/admob`          | `include/firebase/gma`        |

### Library

The Firebase AdMob C++ SDK will be provided as a static library within theFirebaseC++SDK build archive:  

### iOS

| Deprecated Firebase AdMob C++ SDK | New Google Mobile Ads C++ SDK |
|-----------------------------------|-------------------------------|
| `firebase_admob.xcframework`      | `firebase_gma.xcframework`    |

### Android

| Deprecated Firebase AdMob C++ SDK | New Google Mobile Ads C++ SDK |
|-----------------------------------|-------------------------------|
| `libfirebase_admob.a`             | `libfirebase_gma.a`           |

## Class, enum, and struct migrations

The table below lists specific classes, enums, and structs that changed or have been removed. Here's a summary:

- `BannerView`is renamed to`AdView`.
- `NativeAdExpressView`is removed.
- The`RewardedVideo`namespace is replaced with a`RewardedAd`class.
- The`PresentationState`enumeration and listeners are removed and replaced with`AdListener`and`FullScreenContent`listeners.
- The following parameters are removed as per-ad configuration parameters in`AdRequests`:

  - the configuration of test device IDs
  - the targeting of advertisements based on age

  Instead, these parameters can now be configured in`RequestConfiguration`which is a global setting that will affect all subsequent ad loads.

| Deprecated`firebase::admob namespace` |                        New`firebase::gma namespace`                        |
|---------------------------------------|----------------------------------------------------------------------------|
| `AdSizeType`(enum)                    | `AdSize::Type`(enum)                                                       |
| `BannerView`                          | `AdView`                                                                   |
| `BannerView::Listener`                | `AdListener` `AdViewBoundingBoxListener` `PaidEventListener`               |
| `BannerView::Position`                | `AdView::Position`                                                         |
| `BannerView::PresentationState`       | *Removed*                                                                  |
| `ChildDirectedTreatmentState`         | `RequestConfiguration::TagForChildDirectedTreatment`                       |
| `Gender`(enum)                        | *Removed*                                                                  |
| `InterstitialAd::Listener`            | `FullScreenContentListener` `PaidEventListener`                            |
| `KeyValuePair`                        | *Removed*                                                                  |
| `NativeExpressAdView`                 | *Removed*                                                                  |
| `PollableRewardListener`              | *Removed*                                                                  |
| `RewardItem`                          | `AdReward`                                                                 |
| `RewardedVideoAd`(namespace)          | `RewardedAd`(class)                                                        |
| `RewardedVideoAd::Listener`           | `FullScreenContentListener` `PaidEventListener` `UserEarnedRewardListener` |
| `AdMobError`(enum)                    | `AdErrorCode`(enum)                                                        |
| `RewardItem`                          | `AdReward`                                                                 |

## SDK initialization

Each Google Mobile Ads C++ SDK initialization function immediately returns two status indicators:

- An optional out parameter conveys whether a dependency error occurred before the initialization process started.

- The return parameter is a reference to a`firebase::Future`. The`Future`contains the results of the asynchronous initialization of the mediation adapters on the device.

While the Google Mobile Ads C++ SDK may be invoked to loadAdMob-served ads as soon as the initialization function returns, other ad networks will not serve ads until their corresponding medation adapter has been fully initialized. This process occurs asynchronously. Therefore, if you're using ad mediation in your application, we recommend that you wait for the`Future`to resolve before attempting to load any ads.

### Before

    firebase::App* app = ::firebase::App::Create();
    firebase::InitResult result = firebase::admob::Initialize(*app, kAdMobAppID);

    if (result != kInitResultSuccess) {
      // Initialization immediately failed, most likely due to a missing dependency.
      // Check the device logs for more information.
      return;
    }

### After

    using firebase::App;
    using firebase::Future;
    using firebase::gma::AdapterInitializationStatus;

    App* app = ::firebase::App::Create();
    firebase::InitResult result;
    Future<AdapterInitializationStatus> future =
      firebase::gma::Initialize(*app, &result);

    if (result != kInitResultSuccess) {
      // Initialization immediately failed, most likely due to a missing dependency.
      // Check the device logs for more information.
      return;
    }

    // Poll the future to wait for its completion either in this
    // thread, or as part of your game loop by calling
    // firebase::gma::InitializeLastResult();
    while (future.status() == firebase::kFutureStatusPending) {
      // Initialization on-going, continue to wait.
    }

    // future.status() is either kFutureStatusComplete or there's an error

    if (future.status() == firebase::kFutureStatusComplete &&
         future.error() == firebase::gma::AdErrorCodeNone) {
      AdapterInitializationStatus* status = future.result();
      // Check status for any mediation adapters you wish to use.
      // ..
    } else {
      // Handle initialization error.
    }

## Changes to`AdSize`within`AdView`

`AdSize`now contains static members of common banner ad sizes, and supports`AnchorAdaptive`and`InlineAdaptive`ad sizes which have a dynamic height based on the given width and the screen's current orientation.

|                                    Static`AdSize`constants added to`firebase::gma::AdSize`                                     ||
|----------------------------|----------------------------------------------------------------------------------------------------|
| `AdSize::kBanner`          | Mobile Marketing Association (MMA) banner ad size (320x50 density-independent pixels)              |
| `AdSize::kFullBanner`      | Interactive Advertising Bureau (IAB) full banner ad size (468x60 density-independent pixels)       |
| `AdSize::kLargeBanner`     | Taller version of`kBanner`, typically 320x100                                                      |
| `AdSize::kLeaderboard`     | Interactive Advertising Bureau (IAB) leaderboard ad size (728x90 density-independent pixels)       |
| `AdSize::kMediumRectangle` | Interactive Advertising Bureau (IAB) medium rectangle ad size (300x250 density-independent pixels) |

|                                                                                    Static methods in`firebase::gma::AdSize`to help construct instances of`AdSize`                                                                                     ||
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GetLandscapeAnchoredAdaptiveBannerAdSize`          | Creates an`AdSize`with the given width and a Google-optimized height to create a banner ad in landscape mode                                                                                     |
| `GetPortraitAnchoredAdaptiveBannerAdSize`           | Creates an`AdSize`with the given width and a Google-optimized height to create a banner ad in portrait mode                                                                                      |
| `GetCurrentOrientationAnchoredAdaptiveBannerAdSize` | Creates an`AdSize`with the given width and a Google-optimized height to create a banner ad given the current orientation                                                                         |
| `GetInlineAdaptiveBannerAdSize`                     | Creates an`AdSize`most suitable for banner ads given a maximum height This`AdSize`allows Google servers to choose an optimal ad size with a height less than or equal to a specified max height. |
| `GetLandscapeInlineAdaptiveBannerAdSize`            | Creates an`InlineAdaptive``AdSize`with the given width and the device's landscape height                                                                                                         |
| `GetPortraitInlineAdaptiveBannerAdSize`             | Creates an`InlineAdaptive``AdSize`with the given width and the device's portrait height.                                                                                                         |
| `GetCurrentOrientationInlineAdaptiveBannerAdSize`   | A convenience method to return`InlineAdaptive``AdSize`given the current interface orientation given a specific width.                                                                            |

### Before

    firebase::admob::BannerView* banner_view = new firebase::admob::BannerView();

    firebase::admob::AdSize ad_size;
    ad_size.ad_size_type = firebase::admob::kAdSizeStandard;
    ad_size.width = 320;
    ad_size.height = 50;

    // ad_parent is a reference to an iOS UIView or an Android Activity.
    // banner_ad_unit is your ad unit id for banner ads.
    banner_view->Initialize(ad_parent, banner_ad_unit, ad_size);

### After

    firebase::gma::AdView* ad_view = new firebase::gma::AdView();

    // ad_parent is a reference to an iOS UIView or an Android Activity.
    // banner_ad_unit is your ad unit id for banner ads.
    banner_view->Initialize(ad_parent, banner_ad_unit, firebase::gma::AdSize.kBanner);

## `AdRequest`and global configuration

Test device IDs,`TagForChildDirectedTreatment`, and`TagForUnderAgeOfConsent`(previously handled by birthday) have been removed from`AdRequest`and are now part of a global`RequestConfiguration`. Applications may invoke`firebase::gma::SetRequestConfiguration()`early-on in the application's lifecycle to configure these values. All subsequent ad load operations will honor these settings once they're configured.

`firebase::gma::AdRequest`still exists as it provides contextual information for loading advertisements, including keywords and an optional content URL.

AdMob's`AdRequest`C-style struct has been replaced with a class with methods which provide a better user experience when defining and appending to the various lists of information.

Here are notable`AdRequest`changes:

- Extras are now associated with a mediation adapter class name. Extras sent to theAdMobservice should use the default class name as defined below.
- When requesting an ad, apps may pass a URL of the content they are serving. This enables keyword targeting to match the ad with other content being displayed.

### Before

    firebase::admob::AdRequest request;

    // Keywords to be used in targeting.
    const char* keywords[] = {"GMA", "C++", "Fun"};
    request.keyword_count = sizeof(keywords) / sizeof(keywords[0]);
    request.keywords = keywords;

    // "Extra" key value pairs.
    static const firebase::admob::KeyValuePair extras[] = {
          {"extra_name", "extra_value"}};
    request.extras_count = sizeof(extras) / sizeof(extras[0]);
    request.extras = kRequestExtras;

    // Devices that should be served test ads.
    const char* test_device_ids[] ={ "123", "4567", "890" };
    request.test_device_id_count =
          sizeof(test_device_ids) / sizeof(test_device_ids[0]);
    request.test_device_ids = test_device_ids;

    // Sample birthday to help determine the age of the user.
    request.birthday_day = 10;
    request.birthday_month = 11;
    request.birthday_year = 1975;

    // Load Ad with the AdRequest.

### After

    // Do once after Google Mobile Ads C++ SDK initialization.
    // These settings will affect all Ad Load operations.
    firebase::gma::RequestConfiguration configuration;
    configuration.max_ad_content_rating =
          firebase::gma::RequestConfiguration::kMaxAdContentRatingPG;
    configuration.tag_for_child_directed_treatment =
          firebase::gma::RequestConfiguration::kChildDirectedTreatmentTrue;
    configuration.tag_for_under_age_of_consent =
          firebase::gma::RequestConfiguration::kUnderAgeOfConsentFalse;
    configuration.test_device_ids.push_back("1234");
    configuration.test_device_ids.push_back("4567");
    configuration.test_device_ids.push_back("890");
    firebase::gma::SetRequestConfiguration(configuration);

    // Then, more information must be provided via an AdRequest when
    // loading individual ads.
    firebase::gma::AdRequest ad_request;

    // "Extra" key value pairs.
    ad_request.add_keyword("GMA");
    ad_request.add_keyword("C++");
    ad_request.add_keyword("Fun");

    // Content URL.
    ad_request.set_content_url("www.example.com");

    // Mediation Adapter Extras.
    #if defined(Android)
    const char* ad_network_extras_class_name =
        "com/google/ads/mediation/admob/AdMobAdapter";
    #else  // iOS
    const char* ad_network_extras_class_name = "GADExtras";
    #endif

    ad_request.add_extra(ad_network_extras_class_name, "extra_name", "extra_value");

    // Load Ad with the AdRequest. See next section.

## `AdResults`

`LoadAd`now returns a`Future`containing an`AdResult`object for all`AdView`,`InterstitialAd`, and`RewardedAd`ad types. The`AdResult::is_successful`method returns`true`if the ad request was successfully fulfilled, or`false`if not.

On failure, the`AdResult`contains an`AdError`object with service-level information about the problem, including the error code, the error message and domain strings.

### Before

    firebase::Future<AdResult> future;

    void load_ad() {
      // Assume an already created AdRequest object.
      future = ad_view->LoadAd(ad_request);
    }

    void your_game_loop() {
      if (future.status() == firebase::kFutureStatusComplete) {
        if(future.error() != firebase::admob::kAdMobErrorNone) {
          // There was either an internal SDK issue that caused the Future to
          // fail its completion, or AdMob failed to fulfill the ad request.
          // Details are unknown other than the Future's error code returned
          // from future.error().
        } else {
          // The ad loaded successfully.
        }
      }
    }

### After

    firebase::Future<AdResult> future;

    void load_ad() {
      // Assumes a previously created AdRequest object.
      // See "AdRequest and Global Configuration" above.
      future = ad_view->LoadAd(ad_request);
    }

    void your_game_loop() {
      // Check the future status in your game loop:
      if (future.status() == firebase::kFutureStatusComplete) {
        if(future.error() != firebase::admob::kAdErrorCodeNone) {
          // There was an internal SDK issue that caused the Future to fail.
        } else {
          // Future completed successfully.  Check the GMA result.
          const AdResult* ad_result = future.result();
          if ( ad_result->is_successful() != true ) {
            // GMA failed to serve an ad. Gather information about the error.
            const AdError& ad_error = ad_result->ad_error();
            AdErrorCode error_code = ad_error.code();
            const std::string error_domain = ad_error.domain();
            const std::string error_message = ad_error.message();
          } else {
            // The ad loaded successfully.
          }
        }
      }
    }

## `AdListener`events within`AdView`

AdMob's`BannerView::Listener`class has been replaced with two distinct listener classes in the Google Mobile Ads C++ SDK:

- `AdListener`tracks ad lifecycle and user interaction events.
- `AdViewBoundingBoxListener`is invoked when the`AdView`is resized or moved.

### AdMob`OnPresentationStateChanged`callbackGoogle Mobile Adsmappings

The`firebase::admob::BannerView::PresentationState`enumerated type and`OnPresentationStateChanged`listener method are not included in the new Google Mobile Ads C++ SDK.

The following are alternative ways to detect presentation state changes in the life cycle of an`AdView`:

| `firebase::admob::BannerView::Listener OnPresentationStateChanged`event |                                                                                                         `firebase::gma::AdListener`counterpart                                                                                                          |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kPresentationStateHidden`                                              | When`AdListener::OnAdClosed`is invoked, or when`AdView::Hide()`completes its asynchronous operation successfully                                                                                                                                        |
| `kPresentationStateVisibleWithoutAd`                                    | None. Attempting to invoke`AdView::Show()`an unloaded`AdView`will result in an error.                                                                                                                                                                   |
| `kPresentationStateVisibleWithAd`                                       | When`AdListener::OnAdOpened`is invoked, or when`AdView::Show()`completes its asynchronous operation successfully with an ad                                                                                                                             |
| `kPresentationStateOpenedPartialOverlay`                                | Query the bounding box after`AdListener::OnAdOpened()`has been invoked to determine the size and position of the ad being shown. Alternatively, query the`AdView`'s position and`AdSize`and/or monitor the bounding box via`AdViewBoundingBoxListener`. |
| `kPresentationStateCoveringUI`                                          | See`kPresentationStateOpenedPartialOverlay`above                                                                                                                                                                                                        |

## `RewardedAd`is now a class

The deprecated Firebase AdMob C++ SDK facilitated rewarded ads via a collection of functions in the`firebase::admob::rewarded_ad`namespace. These functions have been coalesced into a new`RewardedAd`class which serves ads with a similar API surface to`InterstitialAd`(see next section).

## `InterstitialAd`and`RewardedAd`listeners

Both interstitial ads and rewarded ads are considered full screen ads. A new`FullScreenContentListener`can be installed to listen to advertisement life cycle events for these ad types, and a separate`PaidEventListener`can be installed to track when theAdMobservice has deemed a paid event has occurred.

`RewardedAd`has an additional listener to monitor user-earned reward events.

### New full screen ad callback methods

| `FullScreenContentListener`methods  | `PaidEventListener`methods | `UserEarnedRewardListener`methods |
|-------------------------------------|----------------------------|-----------------------------------|
| `OnAdClicked`                       | `OnPaidEvent`              | `OnUserEarnedReward`              |
| `OnAdDismissedFullScreenContent`    | `OnPaidEvent`              | `OnUserEarnedReward`              |
| `OnAdFailedToShowFullScreenContent` | `OnPaidEvent`              | `OnUserEarnedReward`              |
| `OnAdImpression`                    | `OnPaidEvent`              | `OnUserEarnedReward`              |
| `OnAdShowedFullScreenContent`       | `OnPaidEvent`              | `OnUserEarnedReward`              |

## Methods changed/removed/replaced

The table below lists the specific methods changed in the new Google Mobile Ads C++ SDK. Methods with parameters listed remain but their signatures have changed.

|                    Class                    |              Firebase AdMob C++ SDK API               |                              Google Mobile Ads C++ SDK API                              |                                        Notes                                         |
|---------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `BannerView`                                | `MoveTo`                                              | `AdView::SetPosition`                                                                   |                                                                                      |
| `BannerView`                                | `presentation_state`                                  | *Removed*                                                                               | Handled by`AdViewListener`events and`AdView::Show`and`AdView::Hide`future results.   |
| `BannerView`                                | `SetListener`                                         | `AdView::SetAdListener` `AdView::SetBoundingBoxListener` `AdView::SetPaidEventListener` | The new listener design increases the fidelity of detecting`AdView`lifecycle events. |
| `BannerView`                                | `Listener::OnPresentationStateChanged`                | *Removed*                                                                               | See`BannerView::SetListener`, above.                                                 |
| `BannerView`                                | `Listener::OnBoundingBoxChanged`                      | `AdViewBoundingBoxListener::OnBoundingBoxChanged`                                       |                                                                                      |
| InterstitialAd                              | `Initialize(AdParent parent, const char* ad_unit_id)` | `Initialize(AdParent parent)`                                                           | The`ad_unit_id`parameter is now part of the`LoadAd`operation.                        |
| InterstitialAd                              | `LoadAd(const AdRequest& request)`                    | `LoadAd(const char* ad_unit_id, const AdRequest& request)`                              |                                                                                      |
| InterstitialAd                              | `presentation_state`                                  | *Removed*                                                                               | The`presentation_state`enumeration has been removed. Use`FullScreenContentListener`. |
| InterstitialAd                              | `SetListener`                                         | `SetFullScreenContentListener` `SetPaidEventListener`                                   |                                                                                      |
| InterstitialAd                              | `Destroy`                                             | *Removed*                                                                               | Cleaning up resources is now part of the`RewardedAd`destructor.                      |
| `RewardedAd` *(formally `RewardedVideoAd`)* | `Initialize`                                          | `Initialize(AdParent parent)`                                                           | `AdParent`was previously passed to`Show`, but is now part of initialization.         |
| `RewardedAd` *(formally `RewardedVideoAd`)* | `presentation_state`                                  | *Removed*                                                                               | The`presentation_state`enumeration has been removed. Use`FullScreenContentListener`. |
| `RewardedAd` *(formally `RewardedVideoAd`)* | `SetListener`                                         | `SetFullScreenContentListener` `SetPaidEventListener``Show`                             | A`UserEarnedReward`listener is also defined when showing a`RewardedAd`. See below.   |
| `RewardedAd` *(formally `RewardedVideoAd`)* | `Show(AdParent parent)`                               | `Show(UserEarnedRewardListener* listener)`                                              |                                                                                      |