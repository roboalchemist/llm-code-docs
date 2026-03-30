# Source: https://docs.buildnatively.com/guides/integration/admob-integration-guide.md

# AdMob Integration Guide

Natively integrates with Google AdMob to help you monetize your iOS and Android applications through high-quality advertisements. This guide covers the end-to-end process of setting up AdMob, configuring the Natively wrapper, and implementing ads via Bubble.io or the JavaScript SDK.

Currently, Natively supports **Banner** and **Interstitial** ad formats.

## Prerequisites

* A **Google AdMob** account.
* A **Natively** account with an active app project.

## Google AdMob Configuration

You must register your applications in the AdMob console to generate the necessary App IDs.

### Create App in AdMob

1. Log in to your [Google AdMob Console](https://apps.admob.com).

2. Navigate to Apps and click Add Your First App (or Add App if you have existing ones).

   <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FbghTM56fRnog5GP5VizP%252F1.png%3Falt%3Dmedia%26token%3D12006427-c50d-47cd-a92f-12691e0adb87&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=efd0417e&#x26;sv=2" alt=""><figcaption></figcaption></figure>

3. Select the Platform (iOS or Android).

   <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FFn1vu5cdBZEzUBh7rQ4z%252F2.png%3Falt%3Dmedia%26token%3D974e9819-acc6-41d7-ae08-b1443dcbf3bb&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=4cc18175&#x26;sv=2" alt=""><figcaption></figcaption></figure>

   * *Note:* If you are building for both platforms, you must repeat this process to create two separate apps in AdMob.

4. Is the app listed on a supported app store?

   * Yes: Search for your app and click Add.

   <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FfCZ7rEfHsdu26KXqdQkW%252F3.png%3Falt%3Dmedia%26token%3D35263e8b-4701-40f2-9a67-d9737093a603&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=358fe58e&#x26;sv=2" alt=""><figcaption></figcaption></figure>

   <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FnZZC7RmxDzL3IkoU1CEc%252F4.png%3Falt%3Dmedia%26token%3Dca2118ae-9e95-4644-ab2d-d4165e062521&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=a9a580c&#x26;sv=2" alt=""><figcaption></figcaption></figure>

   * No: Select No, enter your App Name, and click Add App.<br>

   <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252F971PF2yUTe2LLwda6wYJ%252F3-1.png%3Falt%3Dmedia%26token%3Dcf1c7836-e896-493e-94bd-595a322563c4&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=7680e7aa&#x26;sv=2" alt=""><figcaption></figcaption></figure>

### Retrieve App ID

Once the app is created, you need the App ID to link it with Natively.

1. Go to Apps > View All Apps.
2. Locate your newly created app.
3. Copy the App ID (it starts with `ca-app...`).<br>

   <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FN5UUXc2kAcBXfHr9DcxK%252F5.png%3Falt%3Dmedia%26token%3D3b76dd72-0439-4f6b-a4f0-8cba4c834481&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=9af11d44&#x26;sv=2" alt=""><figcaption></figcaption></figure>

View AdMob's full setup guide here: [Setup Admob App](https://support.google.com/admob/answer/9989980?hl=en)

## Natively Dashboard Setup

You must link your AdMob App IDs to your Natively project and rebuild the app.

* Open your Natively App Dashboard.
* Navigate to Features > AdMob and toggle the feature to Enabled.
* Paste the App IDs you copied in the AdMob dashboard into the respective fields:
  * iOS App ID
  * Android App ID
* Enter a Permission Description. This text explains to the user why the app requests tracking permissions (App Tracking Transparency). Failure to provide a clear description may result in App Store rejection.
* Order a new build. The AdMob SDK and keys are injected into your app bundle during the build process.

## Implementation

Choose your integration method below: **Bubble.io Plugin** (No-Code) or **JavaScript SDK** (Code).

### Inizialization

{% tabs %}
{% tab title="Bubble.io Plugin" %}
**Check Plugin**

Before starting, verify if the Natively plugin is already installed in your Bubble project.

1. Open your Bubble editor and navigate to the Plugins tab in the left sidebar.
2. **Check Installed Plugins:** Look through your list of installed plugins for "Natively iOS & Android app builder".
   * If it IS installed: Check the version number. If an update is available (e.g., you see a button saying "Update"), click it to ensure you have the latest features and bug fixes.

     <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FmfnSUug82IdnxOAoBrak%2Fnatively_app_builder_bubble_plugin_update.png?alt=media&#x26;token=c193f69f-b03b-4be4-b80b-f34ba37ac212" alt=""><figcaption></figcaption></figure>
   * If it is NOT installed: Click the + Add plugins button , search for "Natively", and click Install.

     <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FC5rA42yQHcN1uGKFbzmF%2Fnatively_app_builder_bubble_plugin.png?alt=media&#x26;token=d9706d9b-dbe8-459b-b9b3-5667648aa4b7" alt=""><figcaption></figcaption></figure>

{% endtab %}

{% tab title="JavaScript SDK" %}
**Check SDK**

Before writing any ad logic, ensure the Natively SDK is correctly installed and up-to-date in your codebase.

1. Open your project's main HTML file (or header settings) and look for the Natively script tag inside the `<head>` section.
2. Install/Update: If missing or outdated, add the following code. You can specify the SDK version in the URL (e.g., `@2.20.0`) .

```javascript
<head>
  <script async onload="nativelyOnLoad()" src="https://cdn.jsdelivr.net/npm/natively@2.20.0/natively-frontend.min.js"></script>
</head>
```

{% endtab %}
{% endtabs %}

### **Banner Ads**

{% tabs %}
{% tab title="Bubble.io Plugin" %}

1. Drag the Natively - Banner element onto your page.

{% hint style="warning" %}
This element must be set to Visible on page load to initialize correctly. It should be placed directly on the page root and not inside hidden containers, such as Popups, Floating Groups, Group Focus elements, or Repeating Groups. To hide the element from your UI, you may set its dimensions to 0x0 px.
{% endhint %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fn3538Ge19Pxm5gi0bEJ4%2Fnatively_bubble_plugin_admob_banner_element.png?alt=media&#x26;token=04bd9767-2428-4295-9bd7-bdb9ed4c0bbe" alt=""><figcaption></figcaption></figure>

1. Configure the following fields in the property editor:

   * iOS UnitId: Test unitId `'ca-app-pub-3940256099942544/2934735716'` or your own.
   * Android UnitId: Test unitId `'ca-app-pub-3940256099942544/6300978111'` or your own.
   * Position: `TOP`, `BOTTOM`.
   * Size Type: `AUTO`, `CUSTOM`.
   * Banner Width: Will be applied only when Size Type is `CUSTOM`.
   * Banner Height: Will be applied only when Size Type is `CUSTOM`.
   * Preload Ad on Initialize: Load ad on initialization.
   * Show Ad on Initialize: Display ad on initialization.

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F1FgyUFJOt0WVMIOHdTcL%2Fnatively_bubble_plugin_admob_banner_settings.png?alt=media&#x26;token=c8b6fc61-b11e-4f63-84f3-e378550be11c" alt=""><figcaption></figcaption></figure>

2. Element Logic (Events, States, & Actions)

Use the following data points to build your ad logic.

* Events:
  * Did finish setup: When the banner has finished setting up and is ready to load an ad.
  * Did load ad: When ad loading is finished and the banner is ready to be displayed (called after 'Load Ad' action).
  * Did fail to receive ad: When loading the ad failed (can occur after 'Load Ad' action).
  * Did record click: When the user clicks on the banner.
  * Did record impression: When the user sees the ad.
  * Did show banner: When the banner is successfully shown.
  * Did hide banner: When the banner is successfully hidden.
* States:
  * Banner Is Ready: (Yes/No)
  * Banner Is Visible: (Yes/No)
  * Ad Is Loaded: (Yes/No)
  * Latest Error Message: Text description of the last error.
  * Latest Event: Returns the specific event code received from the app:

    * `DID_FINISH_SETUP`
    * `DID_SHOW_BANNER`
    * `DID_HIDE_BANNER`
    * `DID_LOAD_AD`
    * `DID_RECORD_CLICK`
    * `DID_FAIL_TO_RECEIVE_AD`
    * `DID_RECORD_IMPRESSION`
    * Actions:
      * Show Banner: Displays the banner on the screen.
      * Hide Banner: Removes the banner from the screen.
      * Load Ad: Manually fetches a new ad.
      * Check Banner Visible: Refreshes the `Banner Is Visible` state.
      * Check Banner Ready: Refreshes the `Banner Is Ready` state. Checks if the banner is ready to load the ad.

    **How to Use (Workflow Logic)**\
    Automatic Setup: The Banner element sets itself up automatically on page load.

    1. Manual Loading (If 'Preload Ad' is disabled):
       * Create a workflow for the event Did finish setup.
       * Add the action Load Ad.<br>

         <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FlXiSotfBUqJQBH4vRFEP%2Fnatively_bubble_plugin_load_ad.png?alt=media&#x26;token=cee6c627-023f-4b44-8a19-a49a6582e6c9" alt=""><figcaption></figcaption></figure>
    2. Manual Showing (If 'Show Ad' is disabled):
       * Create a workflow for the event Did load ad.
       * Add the action Show Banner.<br>

         <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FWpSh8tP26RQNINPijrND%2Fnatively_bubble_plugin_show_banner.png?alt=media&#x26;token=22fac98d-a23c-4c4f-baec-0c118d45b1de" alt=""><figcaption></figcaption></figure>

{% endtab %}

{% tab title="JavaScript SDK" %}
Use the following code to configure the Banner ad. Note that setting `showAd` and `preloadAd` to `true` handles the initial display automatically.

```javascript
// for release use your own unitID
const androidUnitId = "ca-app-pub-3940256099942544/6300978111"
// for release use your own unitID
const iOSUnitId = "ca-app-pub-3940256099942544/2934735716"
const position = "BOTTOM" // or "TOP"
const sizeType = "AUTO" // or "CUSTOM"
const custom_width = 320 // used only if sizeType is "CUSTOM"
const custom_height = 50 // used only if sizeType is "CUSTOM"
const showAd = true;
const preloadAd = true;

const bannerConfig = {
    androidUnitId,
    iOSUnitId,
    position,
    sizeType,
    custom_width, // used only if sizeType is "CUSTOM"
    custom_height // used only if sizeType is "CUSTOM"
};

const bannerad_callback = function(resp) {
    const event = resp.event;
    // Possible events:
    // DID_FINISH_SETUP - when banner finished setup and is ready to load the ad
    // DID_SHOW_BANNER
    // DID_HIDE_BANNER
    // DID_LOAD_AD - when ad loading is finished and now banner is ready to be displayed (called after Load Ad action)
    // DID_RECORD_CLICK - when the user click on the banner ad
    // DID_FAIL_TO_RECEIVE_AD - when loading ad failed (can be called after Load Ad action)
    // DID_RECORD_IMPRESSION - when the user saw an ad
    console.log(event);
};

const admobBanner = new NativelyAdmobBanner(
    bannerConfig,
    bannerad_callback, // setup callback function(resp){}
    preloadAd,         // true/false (mapped from 'preloadAd' variable)
    bannerad_callback, // setup callback function(resp){}
    showAd,            // true/false (mapped from 'showAd' variable)
    bannerad_callback  // show ad callback function(resp){}
);

// All available methods
// admobBanner.loadAd(callback); - Manually fetches a new ad from the AdMob network.
// admobBanner.showBanner(callback); - Makes the banner visible on the screen.
// admobBanner.hideBanner(callback); - Hides the banner from the screen (does not destroy the instance).
// admobBanner.bannerIsReady(callback); - Checks if an ad has been successfully loaded and is ready to show.
// admobBanner.bannerIsVisible(callback); - Checks if the banner is currently visible to the user.

// How to use?
// If you disabled preloadAd or showAd in the configuration, follow this event loop to display ads manually:
// 1. Wait for Setup: Listen for the DID_FINISH_SETUP event.
// 2. Load the Ad: Call admobBanner.loadAd().
// 3. Wait for Load: Listen for the DID_LOAD_AD event (confirming the ad is ready).
// 4. Show the Ad: Call admobBanner.showBanner().

// --- Banner Ads. Quick Start (Automatic Handling) Example. Start ---
// Use this for simple implementations where you want the ad to appear immediately.
// 1. CONFIGURATION
const bannerConfig = {
    androidUnitId: "ca-app-pub-3940256099942544/6300978111", // Test ID
    iOSUnitId: "ca-app-pub-3940256099942544/2934735716",     // Test ID
    position: "BOTTOM", // or "TOP"
    sizeType: "AUTO"    // or "CUSTOM"
};

// 2. OPTIONAL LOGGING
const onBannerEvent = function(resp) {
    console.log("Banner Event:", resp.event); 
};

// 3. INITIALIZE
// Setting both booleans to 'true' handles loading and showing automatically
const banner = new NativelyAdmobBanner(
    bannerConfig,
    onBannerEvent, 
    true, // preloadAd: Auto-fetch ad from network
    onBannerEvent,
    true, // showAd: Auto-display when ready
    onBannerEvent 
);

// --- Banner Ads. Quick Start (Automatic Handling) Example. End ---

// --- Banner Ads. Advanced Usage (Manual Control) Example. Start ---

// 1. CONFIGURATION
const manualConfig = {
    androidUnitId: "ca-app-pub-3940256099942544/6300978111", // Test ID
    iOSUnitId: "ca-app-pub-3940256099942544/2934735716", // Test ID
    position: "BOTTOM", // or "TOP"
    sizeType: "AUTO" // or "CUSTOM"
};

// 2. DEFINE THE HANDLER
// We use one function to handle the entire lifecycle
const lifecycleHandler = function(resp) {
    const event = resp.event;
    console.log("Current State:", event);

    // Step 1: SDK is ready -> Load the Ad
    if (event === "DID_FINISH_SETUP") {
        console.log("Setup done. Fetching ad...");
        manualBanner.loadAd(); 
    }

    // Step 2: Ad is loaded -> Show the Ad
    if (event === "DID_LOAD_AD") {
        console.log("Ad ready. Displaying now...");
        manualBanner.showBanner();
    }
    
    // Error Handling
    if (event === "DID_FAIL_TO_RECEIVE_AD") {
        console.warn("Ad failed to load.");
    }
};

// 3. INITIALIZE MANUAL INSTANCE
// We set boolean flags to 'false' to prevent auto-loading
const manualBanner = new NativelyAdmobBanner(
    manualConfig,
    lifecycleHandler, 
    false, // preloadAd: FALSE (We will call loadAd() manually)
    lifecycleHandler,
    false, // showAd: FALSE (We will call showBanner() manually)
    lifecycleHandler 
);

// --- Banner Ads. Advanced Usage (Manual Control) Example. End ---
```

{% endtab %}
{% endtabs %}

### **Interstitial Ads**

{% tabs %}
{% tab title="Bubble.io Plugin" %}

1. Drag the Natively - Interstitial element onto your page.

{% hint style="warning" %}
This element must be set to Visible on page load to initialize correctly. It should be placed directly on the page root and not inside hidden containers, such as Popups, Floating Groups, Group Focus elements, or Repeating Groups. To hide the element from your UI, you may set its dimensions to 0x0 px.
{% endhint %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FUt5ZMxbJNJHU4lDNSUd2%2Fnatively_bubble_plugin_admob_interstitial_element.png?alt=media&#x26;token=2e81d973-0435-47a1-874f-4cf43552d9ce" alt=""><figcaption></figcaption></figure>

1. Configure the following fields in the property editor:

   * iOS UnitId: Test unitId `'ca-app-pub-3940256099942544/2934735716'` or your own.
   * Android UnitId: Test unitId `'ca-app-pub-3940256099942544/6300978111'` or your own.
   * Auto Ad Reload: Automatically load new ad after 'Did dismiss ad' event. You will be notified once it's ready with 'Did load ad' event.

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FMdEFE2fnl9cw0knYuYzu%2Fnatively_bubble_plugin_admob_interstitial_settings.png?alt=media&#x26;token=8bbf4645-081b-4e7f-8215-a51ebbd55b5c" alt=""><figcaption></figcaption></figure>
2. Element Logic (Events, States, & Actions)<br>

   Use the following data points to build your ad logic.

   * Events:
     * Did Load Ad: When the ad view has finished setup and is ready to be displayed.
     * Did record click: When the user clicks on the ad.
     * Did fail to present: When presenting the ad failed (can be fired after 'Show Ad' action).
     * Did fail to load ad: When loading the ad failed (can be fired after 'Load Ad' action).
     * Did show ad: When the ad view is displayed to the user.
     * Did dismiss ad: When the user dismisses (closes) the ad view.
     * Did record impression: When the user saw the ad.
   * States:
     * Interstitial Is Ready: When the ad view is ready to be displayed.
     * Latest Error Message
     * Latest Event: The latest event received from the app:
       * `DID_FAIL_TO_LOAD_AD`
       * `DID_LOAD_AD`
       * `DID_SHOW_AD`
       * `DID_RECORD_CLICK`
       * `DID_FAIL_TO_PRESENT`
       * `DID_DISMISS_AD`
       * `DID_RECORD_IMPRESSION`
   * Actions:
     * Show Ad: Displays the interstitial ad.
     * Load Ad: Loads a new ad manually.
     * Check Interstitial Ready: Checks if the ad view is active and can be displayed.

   \
   **How to Use (Workflow Logic)**

   The Interstitial will set up automatically on page load.

   1. Show Ad: Run the Show Ad action when you want to display it.
   2. Reloading Strategy:
      * After each time the ad is shown, a new ad must be fetched.
      * If 'Auto Ad Reload' is enabled: This happens automatically. You will be notified via the Did Load Ad event.<br>

        <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fw2lIvcUkYmdBcipqP3lE%2Fnatively_bubble_plugin_show_interstitial.png?alt=media&#x26;token=b9374360-a94c-4427-bc46-a2d70c07a015" alt=""><figcaption></figcaption></figure>
      * If 'Auto Ad Reload' is disabled: Listen to the Did dismiss ad event and call the Load Ad action manually.<br>

        <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FdL2X1MWyoUKi5rOMsVfo%2Fnatively_bubble_plugin_load_ad__interstitial.png?alt=media&#x26;token=ca842767-ecf3-462c-bb0c-585009c1350c" alt=""><figcaption></figcaption></figure>

{% endtab %}

{% tab title="JavaScript SDK" %}
Interstitial ads cover the full screen and require a strict "Load → Show → Dismiss" lifecycle. You can control this flow using the methods below.

```javascript
// for release use your own unitID
const androidUnitId = "ca-app-pub-3940256099942544/4411468910"
// for release use your own unitID
const iOSUnitId = "ca-app-pub-3940256099942544/1033173712"
const autoReloadAd = true;

const interstitialad_callback = function(resp) {
    const event = resp.event;
    // Possible events:
    // DID_LOAD_AD - when ad view finished setup & load ad and is ready to be displayed
    // DID_FAIL_TO_LOAD_AD - when loading of ad failed (can be called after 'Load Ad' action)
    // DID_SHOW_AD - ad view displayed to user
    // DID_FAIL_TO_PRESENT - when presenting of ad failed (can be called after 'Show Ad' action)
    // DID_RECORD_CLICK - when the user clicks on the ad
    // DID_DISMISS_AD - when the user clicks close ad view.
    // DID_RECORD_IMPRESSION - when the user saw an ad
    console.log(event);
};

const admobInterstitial = new NativelyAdmobInterstitial(
    iOSUnitId,
    androidUnitId,
    interstitialad_callback, // setup & load callback
    autoReloadAd,            // true/false
    interstitialad_callback  // auto reload callback
);

// All available methods
// admobInterstitial.loadAd(callback); - Manually fetches a new ad from the network.
// admobInterstitial.showInterstitialAd(callback); - Displays the ad over the current screen.
// admobInterstitial.interstitialIsReady(callback); - Checks if an ad is currently loaded and ready to be displayed.

// How to use?
// 1. Listen to DID_LOAD_AD
// 2. Call admobInterstitial.showInterstitialAd to show ad
// 3. Listen to DID_DISMISS_AD
// 4. Load new ad with admobInterstitial.loadAd
// 5. Call admobInterstitial.showInterstitialAd to show ad

// --- Interstitial Ads. Standard Usage (Auto-Reload) Example. Start ---
//The SDK automatically fetches the next ad as soon as the current one is closed, ensuring an ad is always ready.

// 1. CONFIGURATION
const autoConfig = {
    androidId: "ca-app-pub-3940256099942544/4411468910", // Test ID
    iosId: "ca-app-pub-3940256099942544/1033173712",     // Test ID
    autoReload: true // SDK handles reloading automatically
};

// 2. DEFINE LOGIC
const onInterstitialEvent = function(resp) {
    const event = resp.event;
    console.log("Interstitial Event:", event);

    if (event === "DID_LOAD_AD") {
        console.log("Ad ready! Enable your 'Show Ad' button now.");
    }

    if (event === "DID_DISMISS_AD") {
        console.log("User closed ad. Resuming app flow...");
        // No need to call loadAd() here, SDK does it automatically.
    }
};

// 3. INITIALIZE
const interstitial = new NativelyAdmobInterstitial(
    autoConfig.iosId,
    autoConfig.androidId,
    onInterstitialEvent, // Initial Setup Callback
    autoConfig.autoReload, 
    onInterstitialEvent  // Auto-Reload Callback
);

// 4. TRIGGER THE AD (Example Function)
function triggerLevelCompleteAd() {
    // Check if ready before showing to avoid errors
    interstitial.interstitialIsReady(function(status) {
        if (status.result) {
            interstitial.showInterstitialAd();
        } else {
            console.log("Ad not ready yet, skipping...");
        }
    });
}

// --- Interstitial Ads. Standard Usage (Auto-Reload) Example. End ---

// --- Interstitial Ads. Advanced Usage (Manual Control) Example. Start ---
// Use this if you need strict control over network usage and want to load ads only at specific moments.

// 1. CONFIGURATION
const manualConfig = {
    androidId: "ca-app-pub-3940256099942544/4411468910", // Test ID
    iosId: "ca-app-pub-3940256099942544/1033173712", // Test ID
    autoReload: false // We will load manually
};

// 2. DEFINE LOGIC
const manualHandler = function(resp) {
    const event = resp.event;

    // A. Ad is loaded and waiting
    if (event === "DID_LOAD_AD") {
        console.log("Manual Ad Loaded. Ready to show.");
    }

    // B. User closed the ad
    if (event === "DID_DISMISS_AD") {
        console.log("Ad closed.");
        // OPTIONAL: Load the next one immediately
        // manualInterstitial.loadAd(); 
    }
};

// 3. INITIALIZE
const manualInterstitial = new NativelyAdmobInterstitial(
    manualConfig.iosId,
    manualConfig.androidId,
    manualHandler,
    manualConfig.autoReload, 
    manualHandler
);

// 4. MANUAL LOAD TRIGGER
// Call this early (e.g., when a level starts) so the ad is ready by the end
function prepareAd() {
    console.log("Pre-loading ad...");
    manualInterstitial.loadAd();
}

// --- Interstitial Ads. Advanced Usage (Manual Control) Example. End ---
```

{% endtab %}
{% endtabs %}

## Testing & Release

#### Testing with Test Devices

Never click your own live ads, as this violates AdMob policy. Always use Test Devices and Test Unit IDs during development.

1. Add Test Device:

   * Go to AdMob Settings > Test devices.

   * Click Add Test Device.<br>

     <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FPbHn3rdwJJ1XuQsfqQ18%252Ftesting-1.png%3Falt%3Dmedia%26token%3D0ac51312-5567-4b8c-8bbe-a225a4f69cd3&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=918d8072&#x26;sv=2" alt=""><figcaption></figcaption></figure>

   * Enter your device name and [Advertising ID/IDFA](https://support.google.com/admob/answer/9691433?hl=en#ID)<br>

     <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FJScTyUEhmY8Cf1lBS3Y8%252Ftesting-2.png%3Falt%3Dmedia%26token%3D91770901-c594-41c3-ab02-6390c32de47d&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=5620ef44&#x26;sv=2" alt=""><figcaption></figcaption></figure>
2. Use Test Unit IDs: Google provides dedicated test IDs that always return test ads:
   * iOS Test Unit ID: `ca-app-pub-3940256099942544/2934735716`
   * Android Test Unit ID: `ca-app-pub-3940256099942544/6300978111`

View AdMob's full app testing guide here:

* [For iOS](https://developers.google.com/admob/android/test-ads)
* [For Android](https://developers.google.com/admob/ios/test-ads)

#### Moving to Production

1. Create real Ad Units in your AdMob Console.
2. Replace the Test Unit IDs in your Bubble plugin or JavaScript code with your real Unit IDs.
3. Submit your app to the App Store and Google Play.
4. Once approved, go to Apps > Your App > App Settings in AdMob and click Add Store to link the live app stores to AdMob. This process takes \~1 day for review.

   <figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FClJBqizoXseptHyMr1uM%252Fimage.png%3Falt%3Dmedia%26token%3Df22d9adc-3baa-4ba7-9e56-aaa22e5bcead&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=b101fc79&#x26;sv=2" alt=""><figcaption></figcaption></figure>

## Troubleshooting

If you have more questions, please read the Admob FAQ page: [Google Admob Help](https://support.google.com/admob/?hl=en\&sjid=11000667129848669269-EU#topic=9757996)
