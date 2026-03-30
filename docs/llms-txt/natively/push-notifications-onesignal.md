# Source: https://docs.buildnatively.com/guides/integration/push-notifications-onesignal.md

# Push Notifications - OneSignal

Natively uses the [OneSignal](https://onesignal.com/) service to provide robust Push Notification support inside your mobile application. Notifications can deliver timely and important information to your users, whether their device is locked or actively in use.

{% embed url="<https://youtu.be/C2wyJIFsKYc>" %}

{% hint style="warning" %}
We do not currently support Rich Push Notifications (notifications containing action buttons or images). This feature will be added soon.
{% endhint %}

## Prerequisites

{% tabs %}
{% tab title="Android Configuration" %}
To send push notifications to Android devices through the Google Play Store, OneSignal requires Firebase Cloud Messaging (FCM) credentials.

**Requirements:**&#x20;

* A [Firebase account](https://firebase.google.com/) (free)

**Create or open your Firebase Project**

Go to the [Firebase console](https://console.firebase.google.com/).

* If you don’t have a project yet, click **Add project** and complete the setup.
* If you already have a project, **select it**.

<figure><img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/af78883-Screenshot_2024-06-27_at_9.56.53_AM.png?w=1100&#x26;fit=max&#x26;auto=format&#x26;n=RWtLFPeffHrC81wI&#x26;q=85&#x26;s=472234463516aefd9c99ba9cfaffc19f" alt=""><figcaption></figcaption></figure>

**Enable Firebase Cloud Messaging API v1**

* In Firebase, click the **gear icon** next to **Project Overview > Project settings**.

<figure><img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/85fe0ac-Screenshot_2024-06-27_at_9.59.24_AM.png?fit=max&#x26;auto=format&#x26;n=0qspEXXeJ8zJbkJ-&#x26;q=85&#x26;s=6365da65ac84db166637d06f74675a29" alt=""><figcaption></figcaption></figure>

* If **Firebase Cloud Messaging API (V1)** is **disabled**, click the **3-dot menu > Open in Cloud Console**.

<figure><img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/04dd9fc-Screenshot_2024-06-27_at_10.01.20_AM.png?fit=max&#x26;auto=format&#x26;n=ciRrThfP6xMpI7GY&#x26;q=85&#x26;s=00a205057d79bdf4d7a274d759f8976c" alt=""><figcaption></figcaption></figure>

* In the Google Cloud Console, click **Enable**. Wait a few minutes for the change to reflect in Firebase.

<figure><img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/386f283-Screenshot_2024-06-27_at_10.05.57_AM.png?fit=max&#x26;auto=format&#x26;n=_KaXe4GQkxsEfa17&#x26;q=85&#x26;s=c68e7e50bbc83ec0f1fe7c006dbb717c" alt=""><figcaption></figcaption></figure>

**Generate a Service Account JSON file**

* Return to Project Settings > Service Accounts
* At the bottom, click **Generate new private key**.

<figure><img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/88fc0c0-Screenshot_2024-06-27_at_10.12.07_AM.png?fit=max&#x26;auto=format&#x26;n=0qspEXXeJ8zJbkJ-&#x26;q=85&#x26;s=79080960dc590694c0782faaea44ea13" alt=""><figcaption></figcaption></figure>

* Confirm by clicking **Generate key** in the popup.

{% hint style="warning" %}
Required Service Account permissions:

* `cloudmessaging.messages.create`
* `firebase.projects.get`

These are included by default. If you’re using a custom Service Account, ensure it has:

* `roles/firebasemessaging.admin`
* `roles/firebase.viewer`
  {% endhint %}

<figure><img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f84ae62-Screenshot_2024-06-27_at_10.20.49_AM.png?w=1100&#x26;fit=max&#x26;auto=format&#x26;n=KSCNwSpBCNSQ8xdF&#x26;q=85&#x26;s=0d279f0b9af30daedae76b3e5fcace7d" alt=""><figcaption></figcaption></figure>

* Save the `.json` file in a secure location. You will need it shortly.
  {% endtab %}

{% tab title="iOS Configuration" %}
Before building app's logic or configuring Natively, you must authorize your Apple Developer account to send push notifications.

**Enable App Capabilities**

* Navigate to your Apple Developer account and go to Certificates, Identifiers & Profiles.
* Click on Identifiers and locate your app's Bundle ID.
* Scroll down the capabilities list and check the box for Push Notifications.
* Click Save.

<figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FndgqqyPjbNL0ctHoni9s%252Fimage.png%3Falt%3Dmedia%26token%3D2395942f-0dae-4b31-b8ea-658a2c9b4b4a&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=2a23790b&#x26;sv=2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FzcVMfwH5Ve6UplsGFPFi%252Fimage.png%3Falt%3Dmedia%26token%3D9e2aeb31-475d-40b8-86fd-557c0c91c784&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=485741d&#x26;sv=2" alt=""><figcaption></figcaption></figure>

**Generate a .p8 Push Key**

* In the Apple Developer portal, go to Keys and click the + button to register a new key.
* Name your key and select the Apple Push Notifications service (APNs) checkbox.
* Click Continue, then Register.
* Download your `.p8` key. Note: You can only download this file once, so save it securely. Apple only allows a maximum of two `.p8` keys per account.

<figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2Ffiles.readme.io%2F1e2ff6e-Apple_Key_Page.jpg&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=aacfa621&#x26;sv=2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2Ffiles.readme.io%2F312d551-Apple_Key_Page_-_Register.jpg&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=76a70453&#x26;sv=2" alt=""><figcaption></figcaption></figure>

Gather your **Key ID**, **Team ID**, and **Bundle ID** to input into OneSignal.

<figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FyXdQUMQ77GY6vK6NfjN9%252Fimage.png%3Falt%3Dmedia%26token%3D71de39b6-1e72-4cbb-8bc6-991c3208d5ee&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=93f7339e&#x26;sv=2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FHZzzbtWquP1FH2dTDjHo%252Fimage.png%3Falt%3Dmedia%26token%3D4f9b69c6-6821-4a80-890a-cf693617a5bb&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=d195182a&#x26;sv=2" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## OneSignal configuration

#### Requirements:

* A [OneSignal](https://onesignal.com/) account (free)

#### Create App

* Navigate to your [OneSginal](https://app.onesignal.com/apps) dashboard
* Click **New App/Website**
* Enter your application's name in the **OneSignal App Name** field.
* Select the option to create a new organization and enter its name.
* Choose either the **Apple iOS (APNs)** or **Google Android (FCM)** channel.
* Click **Next**.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fls2KdM2EA7yWmm33HOVI%2Fonesignal_create_app.png?alt=media&#x26;token=e34dfe30-45ec-46e5-93d7-4347efb3a5c7" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you have both an iOS and Android app for one website, you only need one OneSignal application with both platforms enabled.
{% endhint %}

{% hint style="info" %}
You can set up an additional platform later by navigating to Settings > Push & In-App.
{% endhint %}

{% tabs %}
{% tab title="Android Configuration" %}

* Upload the `.json` file under **Service Account JSON** by clicking **Select file**.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fue9RsJSKZTGwuS3PRSZE%2Fonesignal_setup_android.png?alt=media&#x26;token=a72f486d-d7cd-4dff-bca9-83e4ff382c0d" alt=""><figcaption></figcaption></figure>

* Click **Save & Continue.**
* Select the SDK: **Android Native**
* Click **Save & Continue.**
* Copy your App ID and click **Done**.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FPUuqsnTbT6bFHeIQsTGT%2Fonesignal_setup_ios_copy_id.png?alt=media&#x26;token=fbedc090-6110-420b-a3a7-1ff28cdfe95a" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="iOS Configuration" %}

* Choose **.p8 Auth Key (Recommended)** as the authentication method.
* Provide the following:
  * **`.p8 File`** – The private key file you downloaded from your Apple Developer account.
  * **`Key ID`** – Located in the [Keys section](https://developer.apple.com/account/resources/authkeys) of your Apple Developer account. Make sure it matches the downloaded .p8 file.
  * **`Team ID`** – Found in the top-right corner of your [Apple Developer account](https://developer.apple.com/account/).
  * **`App Bundle ID`** – You can find this in the [Identifiers section](https://developer.apple.com/account/resources/identifiers/list).

<figure><img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c8d0207041e7c277f7e4ca49a3f6100280ddcbf970fce9b720fddfbda6683bb6-p8.png?fit=max&#x26;auto=format&#x26;n=9_Q1FZLh6C0BFLq-&#x26;q=85&#x26;s=fc9c689b0880bda69813428ee7fdbe5f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FqWB851rOpT9CIj2xiB8D%2Fonesignal_setup_ios.png?alt=media&#x26;token=d161c8cb-16e8-4da4-939d-687b311ab24e" alt=""><figcaption></figcaption></figure>

* Click **Save & Continue.**
* Select the SDK: **Native iOS.**

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FAu8Kmj0s8X8fe95o0fQO%2Fonesignal_setup_ios_select_sdk.png?alt=media&#x26;token=4e36f314-5962-4f46-a89b-aa038f95ec4a" alt=""><figcaption></figcaption></figure>

* Click **Save & Continue**
* Copy your App ID and click **Done**.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FPUuqsnTbT6bFHeIQsTGT%2Fonesignal_setup_ios_copy_id.png?alt=media&#x26;token=fbedc090-6110-420b-a3a7-1ff28cdfe95a" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## Natively Dashboard Setup

Once OneSignal is set up, you must link it to your Natively app.&#x20;

* Navigate to Features > Notifications > OneSignal in your app's dashboard.

{% hint style="info" %}
Optionally: Enable the "Automatically request push permission on app launch" checkbox to automatically trigger the system permission prompt immediately after the user launches the app.
{% endhint %}

{% hint style="warning" %}
Requirement: Enter a clear description explaining to the user exactly why your app needs push permission to avoid app rejection.
{% endhint %}

* Enable OneSignal Notifications and enter the **App ID** from your OneSignal account.
* Click **Save**.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FFrOOMMuTUmtbMNUAZeAG%2Fonesignal_dashboard.png?alt=media&#x26;token=e8b5e72e-df99-487a-8ff0-0c761fd91c9a" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
You must rebuild your application for these changes to take effect.
{% endhint %}

## Implementation

Choose your integration method below: **Bubble.io Plugin** (No-Code) or **JavaScript SDK** (Code).

### Initialization

{% tabs %}
{% tab title="Bubble.io Plugin" %}
**Check Plugin**

Before starting, verify if the Natively plugin is already installed in your Bubble project.

1. Open your Bubble editor and navigate to the Plugins tab in the left sidebar.
2. **Check Installed Plugins:** Look through your list of installed plugins for "Natively iOS & Android app builder".
   * If it IS installed: Check the version number. If an update is available (e.g., you see a button saying "Update"), click it to ensure you have the latest features and bug fixes.

<figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FmfnSUug82IdnxOAoBrak%252Fnatively_app_builder_bubble_plugin_update.png%3Falt%3Dmedia%26token%3Dc193f69f-b03b-4be4-b80b-f34ba37ac212&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=a89e4510&#x26;sv=2" alt=""><figcaption></figcaption></figure>

* If it is NOT installed: Click the + Add plugins button , search for "Natively", and click Install.

<figure><img src="https://docs.buildnatively.com/~gitbook/image?url=https%3A%2F%2F3352617162-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F90tV7pYflEQdiAr2VfWu%252Fuploads%252FC5rA42yQHcN1uGKFbzmF%252Fnatively_app_builder_bubble_plugin.png%3Falt%3Dmedia%26token%3Dd9706d9b-dbe8-459b-b9b3-5667648aa4b7&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=9aae2297&#x26;sv=2" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="JavaScript SDK" %}
**Check SDK**

Before writing any logic, ensure the Natively SDK is correctly installed and up-to-date in your codebase.

1. Open your project's main HTML file (or header settings) and look for the Natively script tag inside the `<head>` section.
2. Install/Update: If missing or outdated, add the following code. You can specify the SDK version in the URL (e.g., `@2.20.0`) .

```javascript
<head>
  <script async onload="nativelyOnLoad()" src="https://cdn.jsdelivr.net/npm/natively@2.20.0/natively-frontend.min.js"></script>
</head>
```

{% endtab %}
{% endtabs %}

### &#x20;Setup logic

{% tabs %}
{% tab title="Bubble.io Plugin" %}
**Drag the Natively - Banner element onto your page.**

{% hint style="warning" %}
This element must be set to Visible on page load to initialize correctly. It should be placed directly on the page root and not inside hidden containers, such as Popups, Floating Groups, Group Focus elements, or Repeating Groups. To hide the element from your UI, you may set its dimensions to 0x0 px.
{% endhint %}

**Element Logic (Events, States, & Actions)**

Use the following data points to build your ad logic.

* Events:
  * OneSignal Player ID Updated: Fires whenever the Player ID is successfully retrieved or from OneSignal.
  * Permissions Authorized: Triggered when the user taps Allow on the native system permission dialog.
  * Permissions Denied: Triggered when the user taps Don't Allow on the native system permission dialog.
  * Permission Status Updated: Fires whenever the device's notification settings change.
  * External ID Updated: Triggered after an External ID is successfully set, updated, or removed.
  * External ID Error: Fires if an operation involving an External ID fails.
* States:
  * `Permission Status` (Yes/No): Returns `Yes` if the user has granted notification permissions.
  * `OneSignal PlayerId` (Text): The unique identifier for the current device, used to target this specific user.
  * `OneSignal ExternalId` (Text): The unique identifier for the current user, used to target this specific user.
  * `Error message` (Text): Returns the text of the error encountered during a failed operation. This state is updated if an action (such as an Set the user's External ID) fails.

{% hint style="info" %}
The OneSignal Player ID is equivalent to the Subscription ID. You can locate this value within your OneSignal dashboard by navigating to Audience → Subscriptions.
{% endhint %}

* Actions:
  * Request the user's push notification permission: Triggers the native system dialog using the "Permission description" defined in your dashboard. \
    Open Settings: If permission was previously denied, this displays a native alert offering to take the user directly to the system settings to enable notifications.
  * Get the user's OneSignal PlayerId: Manually refreshes the `OneSignal Player ID` state. Useful if you need to ensure the ID is current before a specific workflow.
  * Get the user's push notification permission status: Re-checks the device's notification settings and updates the `Permission Status` state (Yes/No).
  * Get the user's External ID: Fetches the custom ID currently associated with this Player ID in OneSignal.
  * Set the user's External ID: Links a custom ID to this OneSignal Player ID.
  * Remove the user's External ID: Unlinks the custom ID from the current Player ID.
    {% endtab %}

{% tab title="JavaScript SDK" %}

```javascript
// ============================================================================
// NATIVELY NOTIFICATIONS (ONESIGNAL) - DOCUMENTATION & EXAMPLES
// ============================================================================

// Initialize
const notifications = new NativelyNotifications();

// ============================================================================
// ALL AVAILABLE METHODS
// ============================================================================
// notifications.getPermissionStatus(callback); 
//   - Checks if the user has currently granted push notification permissions.
//
// notifications.requestPermission(fallbackToSettings, callback); 
//   - Prompts the native OS permission dialog. 
//   - If fallbackToSettings is true, prompts the user to open OS settings if previously denied.
//
// notifications.getOneSignalId(callback); 
//   - Retrieves the unique OneSignal Player ID for this specific device.
//   - In the OneSignal dashboard, the PlayerId is labeled as the Subscription ID.
//
// notifications.getExternalId(callback);
//   - Fetches the custom External ID you have linked to this Player ID in OneSignal.
//
// notifications.setExternalId({ externalId: string }, callback);
//   - Links a custom ID (like your database User ID) to this specific Player ID in OneSignal.
//
// notifications.removeExternalId(callback);
//   - Unlinks the current custom External ID from this Player ID.


// --- Push Notifications. Quick Start (Permissions & IDs). Start ---

// 1. DEFINE CALLBACKS
const permissionCheckHandler = function(resp) {
    // Returns boolean: true if allowed, false if denied/undetermined
    console.log("Current Permission Status:", resp.status); 
};

const permissionRequestHandler = function(resp) {
    // Returns boolean: true if the user just clicked 'Allow', false if 'Don't allow'
    console.log("Permission Granted:", resp.status); 
};

const playerIdHandler = function(resp) {
    // Returns string: The unique device identifier from OneSignal
    console.log("OneSignal Player ID:", resp.playerId); // e.g., "a301a5b5-ac6e-..."
};

// 2. CONFIGURATION
// Set to true to show a custom alert asking the user to open OS settings if they previously denied push notification permissions
const fallbackToSettings = false; 

// 3. CORE FLOW
// Check current status, request access if needed, and fetch the device ID.
notifications.getPermissionStatus(permissionCheckHandler);
notifications.requestPermission(fallbackToSettings, permissionRequestHandler);
notifications.getOneSignalId(playerIdHandler);

// --- Push Notifications. Quick Start (Permissions & IDs). End ---


// --- Advanced Usage: OneSignal External ID Management. Start ---
// Use these methods to tie a OneSignal Player ID to your own database's User IDs.

// 1. GET CURRENT EXTERNAL ID
notifications.getExternalId((resp) => {
    // Safely extract the response (handles array wrapping if present)
    const res = (Array.isArray(resp) && resp.length > 0) ? resp[0] : null;
    
    if (res && res.externalId) {
        // SUCCESS: Found an active External ID
        console.log("Current External ID:", res.externalId);
    } else {
        // FAILURE/EMPTY: Check for error messages or assume no ID exists
        const errorMessage = (res && res.error) || (res && res.message) || "No External ID found.";
        console.warn(errorMessage);
    }
});

// 2. SET NEW EXTERNAL ID (e.g., upon User Login)
const newExternalIdData = { externalId: "user_db_id_12345" };

notifications.setExternalId(newExternalIdData, (resp) => {
    if (resp && resp.externalId) {
        // SUCCESS: The ID was successfully registered with OneSignal
        console.log("External ID set successfully to:", resp.externalId);
    } else {
        // FAILURE: Log the exact error
        const errorMessage = (resp && resp.error) || (resp && resp.message) || "Failed to set External ID.";
        console.error("Set Error:", errorMessage);
    }
});

// 3. REMOVE EXTERNAL ID (e.g., upon User Logout)
notifications.removeExternalId((resp) => {
    if (resp && (resp.error || resp.message)) {
        // FAILURE: An error prevented removal
        const errorMessage = resp.error || resp.message;
        console.error("Failed to remove External ID:", errorMessage);
    } else {
        // SUCCESS: A null/empty response indicates the ID was successfully wiped
        console.log("External ID removed successfully. Device is now anonymous.");
    }
});

// --- Advanced Usage: OneSignal External ID Management. End ---
```

{% endtab %}
{% endtabs %}

### How to use

{% hint style="warning" %}
While you can trigger push notifications directly from the client side for rapid testing within the Natively Preview app, we strongly recommend migrating all production logic to Backend Workflows (server side).
{% endhint %}

{% hint style="warning" %}
If a user grants permission during their current session, the updated status will be reflected in OneSignal on the subsequent (second) app launch.
{% endhint %}

#### Implementation Best Practices

Avoid overwhelming users with a permission prompt the moment the app opens. Instead, request push notification access at a "high-value" moment in the user journey - such as during onboarding or immediately after a user opts into a feature that requires alerts (e.g., "Notify me when my order ships").

To ensure your users receive notifications reliably across all their devices, follow this login synchronization flow:

* Verify Player ID on Login: Every time a user authenticates, retrieve their current device's Player ID. Compare this against the ID stored in your database for that user.
* Register New Devices: If the current Player ID is not found in your database, the user is likely on a new device. Use this opportunity to request push permissions and register the device.
* Sync via External ID: Once the device is registered, call `Set External ID` using your internal User ID. This informs OneSignal that this device belongs to your specific user.
* Maintain Your Database: Always save the latest Player ID to your user record. It's possible storing these as a list to support users with multiple active devices (e.g., iPhone and iPad).
* Send Notifications: Use your stored Player IDs or External IDs to trigger targeted push notifications via backend workflows.

{% tabs %}
{% tab title="Bubble Plugin" %}
{% hint style="warning" %}
To authorize push notifications from your Bubble workflows, navigate to the Plugin Settings tab and enter your OneSignal REST API Key into the onesignal\_apiKey field and the App ID into the onesignal\_appId field.
{% endhint %}

Detailed instructions on creating and managing your API keys can be found in the [OneSignal Documentation](https://documentation.onesignal.com/docs/accounts-and-keys).

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FgVN9pqnSO7MEGVIFsMNz%2Fonesignal_plugin_setup.png?alt=media&#x26;token=2cbb1021-00b4-4a56-8495-ef2fefa0094d" alt=""><figcaption></figcaption></figure>

**Requesting Permissions**

Trigger the permission request when a user explicitly opts in to receive notifications (e.g., flipping a "Enable Notifications" toggle).

* Existing Permissions: If the user has already granted access, the system popup will not reappear. Instead, the element will silently refresh the `OneSignal PlayerId` state.
* Handling Denials (Open Settings): If the Open Settings option is enabled and the user previously denied permissions, a dialog will appear. This prompt invites the user to navigate to their device settings to manually re-enable notifications for your app.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FQ7XyfCIRmYiN4m4ZtKsH%2Fonesignal_bubble_request_permissions.png?alt=media&#x26;token=177f9bf1-f2ae-44f1-adf2-06a177175e12" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FaISg7L1V284vP9eIPkEf%2Fnotifications_open_settings.png?alt=media&#x26;token=0647c021-2465-4460-bc02-452ee6e66cc5" alt=""><figcaption></figcaption></figure>

**Capturing the Player ID**

To send targeted notifications, you must map the device's unique identifier to your user records.

* Create a workflow for the event **Notification permission authorized**. Within this workflow, trigger the action **Get the user's OneSignal Player Id**. This ensures that as soon as a user grants access, the app actively fetches their new identifier.
* Listen for the **OneSignal Player Id updated** event. This event fires automatically once the identifier is successfully received from the OneSignal servers.
* Within the "Updated" event workflow, save the `OneSignal Player Id` state's value to the Current User in your database.

Think of the Player ID as the "digital address" for the device. Without saving this address to your database, your backend workflows will not know where to deliver the notification.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F7scz8O6xuAgZzz5b8JeI%2Fonesignal_bubble_get_player_id.png?alt=media&#x26;token=d9b93664-02f9-46af-9c56-9d42e8717ab8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FU2dBOMMiN00tvcoSeK5r%2Fonesignal_bubble_player_id_updated.png?alt=media&#x26;token=febb2295-9561-4b0f-921b-f4ca737edbde" alt=""><figcaption></figcaption></figure>

**Sending a Notification**

In this scenario, we will schedule an automated push notification to be sent three days after a customer orders a product, informing them that their order is on its way.

1\. The Trigger (Client-Side) When a customer completes a purchase (e.g., `new_order_placed`), trigger a Backend Workflow to run with a 3-day delay. You must pass the user's Player ID and the Order Details to this backend workflow.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FVmhdqYcmP7P7KNTlLLNa%2Fonesignal_bubble_example_1.png?alt=media&#x26;token=f455ded1-15d4-4b67-aaa2-dea4eba6b694" alt=""><figcaption></figcaption></figure>

2\. The Execution (Backend Workflow) Create a backend workflow (e.g., `send_delivery_update`) that uses the OneSignal - User Single PlayerId - Send Push action.

Configure the following parameters:

* Player ID: The unique identifier retrieved from your database.
* Title & Message: "Your order is on its way!"
* Redirect URL: The specific internal page link (e.g., `https://example.com/orders/123`) that the app will open when the user taps the notification. This parameter is optional. If not provided, the app will open the App URL.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FXEZHJejSDc5pItvhDpUv%2Fonesignal_bubble_send_push_example.png?alt=media&#x26;token=4f5c612c-0a63-48af-b63b-582857b89462" alt="" width="181"><figcaption></figcaption></figure>

3\. The Result: Deep Linking When the user receives and taps the notification, the app intercepts the Redirect URL and automatically opens that specific page within the app, rather than just the home screen.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FocywJ9uut2SA51of3YTS%2Ftap_push_notification.gif?alt=media&#x26;token=c587d3a8-1b89-42d2-82fe-6355a76c8991" alt="" width="180"><figcaption></figcaption></figure>

**Using OneSignal Templates**

If you have pre-defined layouts in your OneSignal dashboard, you can trigger them by providing a Template ID.

* The Override Rule: When a Template ID is provided, it takes precedence over the Title, Subtitle, Message, and Redirect URL fields. Any content entered into those individual fields will be ignored in favor of the template's settings.
* Setup: Simply paste your Template ID (found in the OneSignal Dashboard under Messages → Templates) into the designated field in the OneSignal - User Single PlayerId - Send Push action.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FU55m9A0GpyIakVG8A4CX%2Fonesignal_bubble_send_push_template.png?alt=media&#x26;token=d56e74e1-1409-4771-a3cc-845b1e678b05" alt="" width="176"><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fv9LzizHXFaPGyFMS2Sdj%2Fonesignal_send_template.jpg?alt=media&#x26;token=b270aea3-26ee-41a3-a820-21e2dea84901" alt="" width="188"><figcaption></figcaption></figure>

**Targeting by OneSignal Segments**

Use segments to broadcast messages to specific groups of users based on their behavior, location, or custom tags. Use the **OneSignal - Segments - Send Push** action in your backend workflows to reach large audiences simultaneously.

* Included Segments: Enter the exact names of the segments you wish to target (e.g., `Active Users` or `Free Tier`). To reach your entire audience, use the default OneSignal segment name: `Total Subscriptions`.
* Excluded Segments: (Optional) Specify segments that should *not* receive the notification. For example, you can target `All Users` but exclude `Premium Subscribers` to send a specific upgrade promotion.
* Important: Segment names must match the spelling and capitalization used in your OneSignal dashboard exactly.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F0AfbB2mzQ8pJCLlHyfHn%2Fonesignal_bubble_send_push_segments.png?alt=media&#x26;token=388a784f-1969-4522-8b63-ac6a1ad5baf6" alt="" width="177"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Other Options" %}
For a comprehensive overview of the delivery methods supported by OneSignal, refer to the following resources:

* [Mobile Push Setup](https://documentation.onesignal.com/docs/en/mobile-push-setup)
* [REST API](https://documentation.onesignal.com/reference/push-notification)
  {% endtab %}
  {% endtabs %}

#### Custom Sound

Be sure to create sound files according to the following rules. If the device cannot find the file in question, or if the file is not in a supported format, it will fall back to the default system notification sound.

* Filename must be `natively.wav`.
* Recommended length less than 30 seconds. Keep file size small, large files may not play on some devices.

**Natively Dashboard Configuration**

* In your Natively dashboard, navigate to Features → Notifications → OneSignal.
* Locate the Custom Notification Sound section and click Click to upload file.
* Upload your audio file.
* Rebuild your app to apply changes.

{% tabs %}
{% tab title="Android Configuration" %}

* In your OneSignal Dashboard, go to Settings → Push & In-App Settings → Android Notification Channels.
* Click Add Group.&#x20;

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FaVE1LTEXL3ht5hkTY9wb%2Fonesignal_dashboard_create_android_channel.png?alt=media&#x26;token=9504d166-1b91-48c1-9950-894431060efd" alt=""><figcaption></figcaption></figure>

* Name the new group and click Submit.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FPph6minjtanQpNS6cgDi%2Fonesignal_dashboard_add_android_channel.png?alt=media&#x26;token=81fa82b8-cb53-4957-beee-65718605ca8b" alt=""><figcaption></figcaption></figure>

* Set the Sound field to exactly `natively`.
  * Set Importance to Urgent or High (required for the sound to trigger).

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FGIEfhoGGyhCIwqMhmf5S%2Fonesignal_dashboard_add_android_channel_settings.png?alt=media&#x26;token=185d589c-edbd-426e-ad48-2203fe40bc51" alt=""><figcaption></figcaption></figure>

* Create the channel and copy the generated Channel ID.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FHpT1e0L0RIWdJSsfuhI6%2Fonesignal_dashboard_select_android_channel.png?alt=media&#x26;token=12f2f69a-3d05-4922-909b-c27080a83eef" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FEunlJ4NEGY0xbRwzaXJz%2Fonesignal_dashboard_copy_android_channel_id.png?alt=media&#x26;token=81b34d8e-22ab-4c34-931c-773a735948b8" alt=""><figcaption></figcaption></figure>

* Paste this ID into your Bubble Plugin or OneSignal API payload.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FeNKc286b61zj6YWO5uhh%2Fnotifications_android_custom_sound.png?alt=media&#x26;token=09209135-d9b3-44bc-ad4b-780b38db05b7" alt="" width="178"><figcaption></figcaption></figure>

{% hint style="warning" %}
Because Android "locks" channel settings, you must reinstall your app on your device for the new sound settings to take effect.
{% endhint %}
{% endtab %}

{% tab title="iOS Configuration" %}
To trigger a custom sound from your Bubble workflows, navigate to the Custom Sound section of your Send Push action. In the iOS Sound field, enter exactly `natively.wav`.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fso8z8Ca2qeiv1NvloZFo%2Fnotifications_ios_custom_sound.png?alt=media&#x26;token=03f5eaa2-826c-4b4c-b70d-d52f3a7d6612" alt="" width="176"><figcaption></figcaption></figure>

To trigger a custom sound via the OneSignal REST API, you must include the `ios_sound` parameter in your JSON payload.

* Parameter: `ios_sound`
* Value: `natively.wav`
  {% endtab %}
  {% endtabs %}

## Troubleshooting

If your notifications are not appearing as expected, follow this tiered checklist to identify and resolve the issue.

**Essential Configuration**

* App Rebuild Required: Any changes made to the configuration in the Natively Dashboard require a new build of your application to take effect.
* The "Preview" Tag: If you are testing using the Natively Preview App, you must set the tag to `preview` in your Bubble plugin settings.
  * For your own build, this field must be left blank.
* Natively Dashboard: Verify that the OneSignal feature is toggled ON and that your OneSignal App ID is pasted correctly.

**Delivery & Targeting**

* Player ID Validation: Ensure you are targeting the correct Player ID (Subscription ID). Check your OneSignal Dashboard → Audience to verify the device is active.
* Bubble Workflow Logic: Double-check that your "Send Push" action is actually firing. Use the Bubble Debugger to confirm that the Player ID is not empty at the moment the action runs.
* Network Connectivity: Confirm the test device is on a stable internet connection. Some corporate firewalls or VPNs may block the ports used by APNs (Apple) or FCM (Google).

**Platform-Specific Fixes**

* iOS: Certificate Refresh: If iOS notifications fail while Android works, your Push Certificate may have expired or been misconfigured. Try re-generating your `.p8` or `.p12` certificate in the Apple Developer Portal and re-uploading it to OneSignal.
* Android: The Reinstall Rule: During development, Android "locks" notification channels upon the first launch. If you have changed the sound or category settings, you must uninstall and reinstall the app to force the OS to register the new configuration.
  * *Note: This behavior is only for development/testing and does not affect users once the app is live in the Play Store.*

**Device-Level Obstacles**

* App Permissions: Verify that the user has actually granted permission. Check the system settings on the device: Settings → \[Your App] → Notifications.
* Focus Modes: Ensure the device is not in Do Not Disturb or a specific Focus Mode (Work, Sleep, etc.).
* Low Power Mode: Some devices disable background data and push synchronization when Low Power Mode is active to conserve battery.
