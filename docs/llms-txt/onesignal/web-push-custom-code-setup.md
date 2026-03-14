# Source: https://documentation.onesignal.com/docs/en/web-push-custom-code-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Code Setup

> Complete guide for setting up OneSignal Web Push notifications using custom code integration. Configure JavaScript SDK, service workers, and Safari certificates for Chrome, Firefox, Safari, and other web browsers.

<Warning>
  Only use this Custom Code setup if you need advanced configuration or programmatic control. For most users, we recommend the:

* [Typical Web Push Setup](./web-push-setup)
* [WordPress Setup](./wordpress)
</Warning>

## Prerequisites

* A [OneSignal account](https://onesignal.com)
* A website with HTTPS (required for web push notifications)
* Access to modify your website's HTML and upload files to your server
* Basic understanding of JavaScript (helpful but not required)

***

## Creating Your OneSignal App

If this is not your first app with OneSignal, click **New App/Website**. Otherwise, you'll proceed directly to the setup.

<Frame caption="OneSignal dashboard showing the initial app creation screen">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a8f47fc-Screenshot_2023-08-10_at_4.19.23_PM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=f32205d306d2b0076d5bb4fdd932f628" width="1974" height="824" data-path="images/docs/a8f47fc-Screenshot_2023-08-10_at_4.19.23_PM.png" />
</Frame>

Name your app something descriptive (matching your website name is recommended), then select **Web** from the platform list. Click **Next: Configure Your Platform**.

**Note:** You can add additional platforms (iOS, Android, etc.) later in your app's settings.

<Frame caption="Platform selection screen showing Web option highlighted">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2776cfd-Screenshot_2023-08-10_at_4.20.50_PM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=5621c05d1e28c02d91b3b10b645f400c" width="1944" height="1860" data-path="images/docs/2776cfd-Screenshot_2023-08-10_at_4.20.50_PM.png" />
</Frame>

### 1. Choose Integration

Select **Custom Code**. This enables full programmatic control over prompts, timing, and other settings using our JavaScript SDK.

**When to choose Custom Code:**

* Need to customize notification prompts
* Want to control when users are prompted
* Require advanced segmentation or targeting
* Building a single-page application (SPA)

<Frame caption="Web configuration options with Custom Code selected">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/93a0d8d-Screenshot_2023-08-22_at_12.33.35_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=435ba806df44e6dcf2c33677933fe41c" width="1914" height="984" data-path="images/docs/93a0d8d-Screenshot_2023-08-22_at_12.33.35_PM.png" />
</Frame>

### 2. Site Setup

Configure your basic site information. These settings affect how notifications appear to users.

<Frame caption="Site setup form with required fields highlighted">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/544a7d3-Screenshot_2023-08-10_at_4.46.39_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=534e513b3a5622516349a8c5f56ac7dd" width="1914" height="836" data-path="images/docs/544a7d3-Screenshot_2023-08-10_at_4.46.39_PM.png" />
</Frame>

| Field                | Description                                | Requirements                                                         |
| -------------------- | ------------------------------------------ | -------------------------------------------------------------------- |
| **SITE NAME**        | Display name shown in push notifications   | Keep it concise and recognizable                                     |
| **SITE URL**         | Your complete website URL                  | Must include `https://` and match exactly (include `www` if used)    |
| **AUTO RESUBSCRIBE** | Automatically resubscribes returning users | **Recommended:** Helps maintain subscriber count                     |
| **DEFAULT ICON URL** | Icon for prompts and notifications         | Square `256x256` pixels, `.png/.jpg/.gif` format, HTTPS URL required |

**Common Gotchas:**

* Site URL must match exactly (with or without `www`)
* Icons must be served over HTTPS
* For local testing, see [Local Testing Setup](./web-push-options#local-testing)

### 3. Advanced Push Settings

#### Safari Web Push Certificate (Optional)

OneSignal provides Safari certificates automatically at no cost. Only enable this if you have existing Safari Web Push certificates you need to use.

<Frame caption="Safari certificate upload option for existing certificates">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5471d0e-Screenshot_2023-08-22_at_12.39.41_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=ea3ca6bceae15f880f875c71f0f7a898" width="1876" height="882" data-path="images/docs/5471d0e-Screenshot_2023-08-22_at_12.39.41_PM.png" />
</Frame>

If enabled, upload your `Safari Web .p12 Push Certificate` and enter the password.

Click **Save** to continue.

### 4. Upload Service Worker Files

The OneSignal Service Worker is required for push notifications to function. You have two options:

<Steps>
  <Step title="Option 1: Create File Manually (Recommended)">
    1. **Create** a new file named `OneSignalSDKWorker.js`
    2. **Add** this single line of code:
       ```javascript  theme={null}
       importScripts("https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.sw.js");
       ```
    3. **Upload** the file to your website's root directory
  </Step>

  <Step title="Option 2: Download and Upload">
    1. **Download** the [OneSignal SDK files](https://github.com/OneSignal/OneSignal-Website-SDK/files/11480764/OneSignalSDK-v16-ServiceWorker.zip)
    2. **Unzip** the download
    3. **Upload** `OneSignalSDKWorker.js` to your server
  </Step>
</Steps>

#### File Hosting Requirements

**Default Location:** The service worker must be accessible at `https://yoursite.com/OneSignalSDKWorker.js`

**Custom Location:** If you need to place the file in a subfolder, see our [OneSignal Service Worker Guide](./onesignal-service-worker) for detailed instructions.

<Info>
  **Need a custom location?** For subfolder placement or migrating from another push provider, follow our [OneSignal Service Worker Guide](./onesignal-service-worker).
</Info>

<Frame caption="Service worker file download interface">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b617def-Screenshot_2023-08-10_at_4.57.47_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=4d83f553d13d3f33231345aa5dfa6a2b" width="1900" height="532" data-path="images/docs/b617def-Screenshot_2023-08-10_at_4.57.47_PM.png" />
</Frame>

<Warning>
  **Legacy Setup Alert:** If your site was set up before November 22, 2021, and you're currently using two service worker files (`OneSignalSDKWorker.js` and `OneSignalSDKUpdaterWorker.js`), continue hosting both files to prevent service worker issues.

  New setups only require the single `OneSignalSDKWorker.js` file.
</Warning>

### 5. Add Code to Your Website

#### Basic Implementation

Add this code to your website's `<head>` section. Replace `YOUR_ONESIGNAL_APP_ID` with your actual App ID from the OneSignal dashboard.

```javascript  theme={null}
<script src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js" defer></script>
<script>
  window.OneSignalDeferred = window.OneSignalDeferred || [];
  OneSignalDeferred.push(function(OneSignal) {
    OneSignal.init({
      appId: "YOUR_ONESIGNAL_APP_ID",
      safari_web_id: "YOUR_SAFARI_WEB_ID", // Only needed if using custom Safari certificate
      notifyButton: {
        enable: true, // Shows the OneSignal bell icon
      },
    });
  });
</script>
```

#### Framework-Specific Setup

If you're using a JavaScript framework, follow these specialized guides:

* [Angular Setup](./angular-setup)
* [React JS Setup](./react-js-setup)
* [Vue JS Setup](./vue-js-setup)

***

## Next Steps After Code Installation

1. **Initialize the SDK:** The code above handles basic initialization
2. **Configure Prompting:** Set up when and how users are prompted - see [Permission Requests](./permission-requests)
3. **Add Custom Logic:** Use the [Web SDK Reference](./web-sdk-reference) for advanced features

**Common Integration Points:**

* Custom prompt timing based on user behavior
* Segmentation and user tagging
* Event tracking and analytics
* A/B testing different notification strategies

### Test Your Setup

#### Verify Installation

1. **Visit your website** - you should see the OneSignal bell icon (if enabled)
2. **Click the bell** to trigger the browser's native permission prompt
3. **Subscribe** to notifications
4. **Check browser console** for any JavaScript errors

#### Send Test Notification

1. **Find your test subscription:** Follow [Find & Set Test Subscriptions](./find-set-test-subscriptions)
2. **Send a test push:** Use our guide to [send yourself a Push Notification](./push)
3. **Verify delivery** across different browsers and devices

***

## Troubleshooting Common Issues

**Service Worker Problems:**

* Ensure `OneSignalSDKWorker.js` is accessible at the correct URL
* Check that the file contains the correct import statement
* Verify HTTPS is working properly

**No Bell Icon Appearing:**

* Confirm the JavaScript code is in the `<head>` section
* Check browser console for errors
* Verify your App ID is correct

**Notifications Not Received:**

* Test in an incognito/private browser window
* Ensure notifications are enabled in browser settings
* Check that your site is served over HTTPS

<Check>
  **Need Help?** If you encounter issues, check our [Web Push Troubleshooting Guide](./troubleshooting-web-push) or contact `support@onesignal.com` for assistance.
</Check>

## What's Next

After successful setup, consider these advanced features:

* [Audience Segmentation](./segmentation) for targeted messaging
* [A/B Testing](./ab-testing) your notification strategies
* [Analytics and Insights](./analytics-overview) to track performance

***

Built with [Mintlify](https://mintlify.com).
