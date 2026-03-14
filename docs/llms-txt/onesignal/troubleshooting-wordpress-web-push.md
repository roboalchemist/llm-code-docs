# Source: https://documentation.onesignal.com/docs/en/troubleshooting-wordpress-web-push.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# WordPress troubleshooting

> Comprehensive guide for troubleshooting common setup issues with OneSignal Web Push Notifications on WordPress, including browser compatibility (Chrome, Firefox, Safari), plugin integration, and resolving CDN or caching conflicts.

## Common setup issues

### Verify your OneSignal dashboard setup

Make sure you’ve completed each step in the [WordPress setup guide](./wordpress):

* Select the **WordPress Plugin** option when creating your OneSignal app
* Your Site URL must exactly match the browser URL
  * For example, `https://example.com` is **not** the same as `https://www.example.com`. Use one version consistently.
  * Only one site origin is supported for push. See [Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy).
* Make sure you've added at least one permission prompt.

### Do not add the OneSignal code manually

The OneSignal WordPress plugin **automatically** includes the initialization script and Service Worker.

✅ This means:

* You should **not** manually add OneSignal JavaScript code in your theme, footer, or other plugins.

❌ If you want to use [Custom Code Setup](./web-push-custom-code-setup), uninstall the WordPress plugin first to avoid conflicts.

***

## How to troubleshoot your site

<Steps>
  <Step title="Verify plugin is active and open developer tools">
    Load your site in a normal (non-incognito) browser window with the plugin enabled.

    <Frame caption="Right-click your site, click Inspect, and open the Console tab.">
      <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/28c27ab14a40621fbcc2c4168d49a2bf72088536a669be59c160b7a30a7fcd95-Screenshot_2025-02-27_at_10.39.27_AM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=38d793be0784bcfd8acee745e3757dcf" width="1814" height="1024" data-path="images/docs/28c27ab14a40621fbcc2c4168d49a2bf72088536a669be59c160b7a30a7fcd95-Screenshot_2025-02-27_at_10.39.27_AM.png" />
    </Frame>
  </Step>

  <Step title="Check the console for OneSignal errors">
    Open the **Console** tab, refresh the page, and look for any red or yellow OneSignal-related errors.
    See [Common OneSignal Console errors](#common-onesignal-console-errors) for help.
  </Step>

  <Step title="Check subscription status in the browser">
    Paste this in the console:

    ```js  theme={null}
    OneSignal.User.PushSubscription.id
    ```

    If subscribed, it returns a string (your Subscription ID).

    <Frame caption="Find your OneSignal Subscription ID in the console.">
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/96cdeebdc8888b5c49b6466bf6975a75fb9497f7e54d34f7da3d6c25b35250ae-Screenshot_2025-02-27_at_11.15.16_AM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=f396b737c9cd56257c59d6515086aec6" width="1258" height="448" data-path="images/docs/96cdeebdc8888b5c49b6466bf6975a75fb9497f7e54d34f7da3d6c25b35250ae-Screenshot_2025-02-27_at_11.15.16_AM.png" />
    </Frame>
  </Step>

  <Step title="Verify Subscription ID in OneSignal dashboard">
    Go to **OneSignal.com > Audience > Subscriptions** and search for the ID returned above.

    <Frame caption="Search your OneSignal dashboard for the Subscription ID.">
      <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e3907be9912e3ed3a934c6968f2e6f9354af519b8c670d1f7de07f32e71a8a80-Screenshot_2025-02-27_at_11.18.06_AM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=76657b84cf0f8f29fa03a776f26cf66c" width="2726" height="780" data-path="images/docs/e3907be9912e3ed3a934c6968f2e6f9354af519b8c670d1f7de07f32e71a8a80-Screenshot_2025-02-27_at_11.18.06_AM.png" />
    </Frame>
  </Step>

  <Step title="Send a test push notification">
    If the subscription exists and status is **Subscribed**, follow the [Push guide](./push) to send a notification.
    If nothing appears, see [Notifications not shown](./notifications-not-shown-web-push) for browser-specific fixes.
  </Step>
</Steps>

***

## Common OneSignal console errors

### <Warning>SdkInitError: OneSignal: This web push config can only be used on ... Your current origin is ...</Warning>

<Frame caption="Site URL mismatch error.">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/334686c64af6155f95d674d0cfd28a5b92739f3cae57382073365ec9206b7e7c-Screenshot_2025-02-27_at_11.35.59_AM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=2d8d0656875180f0b77dd88795a4bced" width="2090" height="192" data-path="images/docs/334686c64af6155f95d674d0cfd28a5b92739f3cae57382073365ec9206b7e7c-Screenshot_2025-02-27_at_11.35.59_AM.png" />
</Frame>

Your site URL in the OneSignal dashboard doesn’t match your actual domain.
Make sure it exactly matches the domain you see in the browser.

### <Warning>PushPermissionNotGrantedError: The user dismissed the permission prompt.</Warning>

The visitor declined the browser prompt. It won’t appear again until a cooldown period expires.
See [Web permission prompts](./permission-requests) for browser rules or clear site data to retry immediately.

### <Warning>The OneSignal web SDK can only be initialized once.</Warning>

<Frame caption="Duplicate OneSignal initialization error.">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/e88d53c6c92a546f188c06e14e1776da8ad63c658c64044b6a674802ce2a2277-Screenshot_2025-02-27_at_2.40.32_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=cc2d3a0773b894f423f0d6db598a37a1" width="2164" height="182" data-path="images/docs/e88d53c6c92a546f188c06e14e1776da8ad63c658c64044b6a674802ce2a2277-Screenshot_2025-02-27_at_2.40.32_PM.png" />
</Frame>

You're loading OneSignal twice. Remove manually added OneSignal code if you're using the plugin.

### <Warning>Installing service worker failed.. 403 or 404 error</Warning>

<Frame caption="Service Worker file missing (403/404).">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/990e505-Screen_Shot_2020-02-01_at_9.31.44_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=0d719e6b826477612901d07e1d505f15" width="3364" height="200" data-path="images/docs/990e505-Screen_Shot_2020-02-01_at_9.31.44_PM.png" />
</Frame>

Make sure this file is accessible:
`https://your-site.com/wp-content/plugins/onesignal-free-web-push-notifications/sdk_files/OneSignalSDKWorker.js`

If not, see [Common plugin support](#common-plugin-support) to fix CDN or caching issues.

***

## Common plugin support

CDNs and caching plugins can block OneSignal’s required files. Use these plugin-specific settings:

### Autoptimize

In **Excluded scripts**, add:

```
wp-content/plugins/onesignal-free-web-push-notifications/sdk_files/(.*)
```

### WP Rocket

Under **CDN > Exclude Files From CDN**, add:

```
(.*)/onesignal-free-web-push-notifications/sdk_files/(.*)
```

### LiteSpeed Cache

Under **CDN > Exclude Path**, add:

```
(.*)/onesignal-free-web-push-notifications/sdk_files/(.*)
```

Then press save.

### WP Super Cache

1. Go to **Settings > WP Super Cache > CDN**
2. In **Exclude if substring**, include: `onesignal-free-web-push-notifications`
3. Click **Contents** > **Delete Cache**

### WP Engine

In WP Engine **plugin > General Settings > HTML Post-Processing**, add these, replacing `YOURSITEHERE`:

```text text theme={null}
#https?://(www\.)?(YOURSITEHERE\.com|mywpenginehandleHere.wpengine.com|wpengineCDNpathHere.wpengine.netdna-(ssl|cdn).com)/wp-(content|includes)#
=> https://wpengineCDNpathHere-wpengine.netdna-ssl.com/wp-$4
#https://wpengineCDNpathHere-wpengine.netdna-ssl.com/plugins/onesignal-free-web-push-notifications/#
=> https://mywebsiteHere.com/wp-content/plugins/onesignal-free-web-push-notifications/
#https://wpengineCDNpathHere-wpengine.netdna-ssl.com/wp-content/plugins/onesignal-free-web-push-notifications/#
=> https://mywebsiteHere.com/wp-content/plugins/onesignal-free-web-push-notifications/
```

### W3 Total Cache

1. Go to **Performance > CDN**
2. Under **Rejected files**, add:

```
{plugins_dir}/onesignal-free-web-push-notifications/sdk_files/*
```

<Frame caption="W3 Total Cache exclusion settings.">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/64ad121-Screen_Shot_2020-03-02_at_7.36.18_PM.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=1b7d1eb06d32c8beef4026a70111dcdb" width="1071" height="494" data-path="images/docs/64ad121-Screen_Shot_2020-03-02_at_7.36.18_PM.png" />
</Frame>

### BunnyCDN

Exclude *onesignal* in the plugin's CDN Excluded Paths.

<Frame caption="BunnyCDN exclusion example.">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/025f46c1159398106997c97a61ad26ffe4ecd6f7a068dcd6e3f743762e6e697b-Screenshot_2024-11-19_at_9.34.35_AM.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=d893359f9da931a9db313391a58cf1ca" width="1830" height="518" data-path="images/docs/025f46c1159398106997c97a61ad26ffe4ecd6f7a068dcd6e3f743762e6e697b-Screenshot_2024-11-19_at_9.34.35_AM.png" />
</Frame>

### CDN Enabler

In Settings > CDN Enabler, add this to "Exclusions":

```
onesignal-free-web-push-notifications
```

### PressCDN

In Exclude Directories, add:

```
/wp-content/plugins/onesignal-free-web-push-notifications/
```

### Breeze

In **Settings > CDN > Exclude Content**, add:

```
/onesignal-free-web-push-notifications/sdk_files/
```

<Frame caption="Breeze exclusion example.">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e0ea4ad-Screen_Shot_2020-06-30_at_7.59.26_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=c12fed5c62e460beec878171e940928d" width="1219" height="552" data-path="images/docs/e0ea4ad-Screen_Shot_2020-06-30_at_7.59.26_PM.png" />
</Frame>

### Hummingbird Pro

Go to **Asset Optimization**, find the OneSignal SDK file, and remove it from optimization.

<Frame caption="Hummingbird Pro Asset Optimization.">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a888a91-PastedGraphic-4_3.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=e376446d64ec7fa8a8067ac7e8e551ba" width="476" height="90" data-path="images/docs/a888a91-PastedGraphic-4_3.png" />
</Frame>

### Sucuri

Follow [Sucuri's Whitelist guide](https://kb.sucuri.net/firewall/Whitelist+and+Blacklist/whitelist-file-folder) to allow OneSignal files.

### iThemes Security plugin

Disable the "Disable PHP in Plugins" option under System Tweaks.

<Frame caption="iThemes PHP plugin setting.">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f78a21b-php-in-plugins.jpg?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=ee27f7a8662e6f8e2b001056b22aa904" width="818" height="188" data-path="images/docs/f78a21b-php-in-plugins.jpg" />
</Frame>

### Defender Security plugin

Do not enable "Prevent PHP execution".
Go to Defender Plugin > Security Tweaks and verify the setting is disabled.

### Example .htaccess for Service Worker access

```html html theme={null}
<Files *.php>
Order allow,deny
Deny from all
</Files>
<Files OneSignalSDKWorker.js.php>
Allow from all
ForceType 'application/javascript; charset=UTF-8'
</Files>
<Files OneSignalSDKWorker.js>
Allow from all
ForceType 'application/javascript; charset=UTF-8'
</Files>
```

***

## Server slowdowns or site unreachable after sending notifications

If your server experiences slowdowns or becomes unreachable after sending notifications, it is often due to increased load from notification assets or limited server resources.

### Do not host your own notification icons

Avoid self-hosting images used in notifications. When you host your own notification icons or images, your server may become overloaded as every recipient’s browser attempts to fetch the image at the same time a notification is sent.
To reduce server strain, use image hosting solutions or CDN services optimized for high-concurrency access.

### Consider upgrading hosting resources

If server issues persist, you may need to:

* **Upgrade your hosting plan:** Higher bandwidth or more powerful hosting may be necessary to handle large-scale notification sends.
* **Consult your hosting provider:** Your provider can offer insights or optimizations specific to your hosting environment.

***

Built with [Mintlify](https://mintlify.com).
