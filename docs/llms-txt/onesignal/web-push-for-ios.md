# Source: https://documentation.onesignal.com/docs/en/web-push-for-ios.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS web push setup

> Complete guide to enabling web push notifications on iOS and iPadOS devices, including manifest file setup, user onboarding strategies, and implementation best practices for Safari, Chrome, and Edge browsers.

export const SdkReleasesIframe = ({sdkFilter = undefined, viewMode = undefined, height, ...frameProps}) => {
  const baseUrl = 'https://onesignal.github.io/sdk-releases';
  const buildUrl = (theme, sdkFilter, viewMode) => {
    const url = new URL(baseUrl);
    const params = new URLSearchParams();
    if (theme) {
      params.set('theme', theme);
    }
    if (sdkFilter) {
      params.set('sdk', sdkFilter);
    }
    if (viewMode) {
      params.set('viewMode', viewMode);
    }
    if (params.toString()) {
      url.search = params.toString();
    }
    return url.toString();
  };
  const detectTheme = () => {
    if (document.documentElement.classList.contains('dark')) {
      return 'dark';
    }
    return 'light';
  };
  const [theme, setTheme] = useState('light');
  const [iframeSrc, setIframeSrc] = useState(() => {
    const initialTheme = detectTheme();
    return buildUrl(initialTheme, sdkFilter, viewMode);
  });
  useEffect(() => {
    const currentTheme = detectTheme();
    setTheme(currentTheme);
    setIframeSrc(buildUrl(currentTheme, sdkFilter, viewMode));
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    const handleThemeChange = () => {
      const newTheme = detectTheme();
      setTheme(newTheme);
      setIframeSrc(buildUrl(newTheme, sdkFilter, viewMode));
    };
    if (mediaQuery.addEventListener) {
      mediaQuery.addEventListener('change', handleThemeChange);
    } else {
      mediaQuery.addListener(handleThemeChange);
    }
    window.addEventListener('storage', handleThemeChange);
    const observer = new MutationObserver(handleThemeChange);
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class', 'data-theme']
    });
    return () => {
      if (mediaQuery.removeEventListener) {
        mediaQuery.removeEventListener('change', handleThemeChange);
      } else {
        mediaQuery.removeListener(handleThemeChange);
      }
      window.removeEventListener('storage', handleThemeChange);
      observer.disconnect();
    };
  }, [sdkFilter, viewMode]);
  const getIframeHeight = () => {
    if (viewMode === 'table') {
      return '450';
    }
    if (viewMode === 'mini') {
      return '170';
    }
    return '800';
  };
  const iframeHeight = height || getIframeHeight();
  return <Frame {...frameProps}>
      <iframe src={iframeSrc} width="100%" height={iframeHeight} frameBorder="0" style={{
    border: "none"
  }} title="SDK Releases" key={iframeSrc} />
    </Frame>;
};

<SdkReleasesIframe sdkFilter="react,vue,vue3,angular,wordpress" viewMode="table" height="380" />

Apple started suporting push notifications on iOS and iPadOS 16.4+ for web apps added to a user's home screen. This functionality works across Safari, Chrome, and Edge browsers, opening new engagement opportunities for web-first companies. This comprehensive guide covers everything you need to implement iOS web push notifications successfully.

<Frame caption="Example web push notification on mobile.">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2477862-iOS_push-doc.jpg?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=86aed6cdbed6645e568a644ac725f414" width="806" height="929" data-path="images/docs/2477862-iOS_push-doc.jpg" />
</Frame>

***

## Important updates for 2025

**Cross-Browser Support**: Web push notifications now work across all major browsers on iOS/iPadOS 16.4+ including Safari, Chrome, and Edge.

**iOS 17+ Improvements**: Enhanced implementation with relevant APIs enabled by default, making web push more accessible to users.

**Reliability Considerations**: Some developers report occasional reliability issues where iOS web push notifications may work initially but then stop unexpectedly. Monitor your notification delivery rates and have fallback engagement strategies in place.

***

## Requirements

* **iOS/iPadOS Version**: 16.4 or higher
* **HTTPS Origin**: Secure connection with responsive design
* **Web Application Manifest**: Valid `manifest.json` file with correct settings
* **Home Screen Installation**: Web app must be added to user's home screen from any supported browser
* **User-Initiated Action**: User must interact with your site before permission prompts can appear
* **OneSignal Service Worker**: Required for notification delivery

### Progressive web app (PWA) check

If your website is already a [Progressive Web App (PWA)](https://onesignal.com/blog/what-is-a-pwa/), no additional site updates are needed. Use [Lighthouse in Chrome DevTools](https://developer.chrome.com/docs/lighthouse/overview/#devtools) to audit whether your site qualifies as a PWA.

***

## Setup

### 1. Create your web application manifest

A Web Application Manifest (`manifest.json`) is a JSON file that defines how your web application appears and behaves when installed on a user's device. For iOS web push, this file is **mandatory**.

#### Required manifest fields

Your `manifest.json` must include these essential fields:

* **`$schema`** (recommended): JSON schema URL for validation and IDE support
* **`name`** (required): Full application name displayed to users
* **`display`** (required): Must be set to `"standalone"` or `"fullscreen"` for iOS compatibility
* **`start_url`** (required): Entry point URL when the application launches
* **`icons`** (required): Array of icon objects with multiple sizes
* **`id`** (recommended): Unique identifier allowing multiple app instances

#### Example manifest file

```json  theme={null}
{
  "$schema": "https://json.schemastore.org/web-manifest-combined.json",
  "name": "OneSignal Manifest Example",
  "short_name": "OS Manifest",
  "display": "standalone",
  "start_url": "/",
  "theme_color": "#E54B4D",
  "background_color": "#ffffff",
  "icons": [
    { "src": "/icon-192x192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-256x256.png", "sizes": "256x256", "type": "image/png" },
    { "src": "/icon-384x384.png", "sizes": "384x384", "type": "image/png" },
    { "src": "/icon-512x512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "id": "?homescreen=1"
}
```

#### Implementation steps

1. **File Placement**: Place `manifest.json` in your website's root directory
2. **HTML Integration**: Add this link tag to the `<head>` section of all pages:

```html  theme={null}
<link rel="manifest" href="/manifest.json"/>
```

1. **Icon Preparation**: Create high-quality PNG icons in multiple sizes (192x192, 256x256, 384x384, 512x512 pixels recommended)

<Note>
  Use tools like [SimiCart Manifest Generator](https://www.simicart.com/manifest-generator.html/) to quickly create manifest files, or validate existing ones with [Manifest Tester](https://manifesttester.com/).
</Note>

### 2. Add the OneSignal service worker

If you've already completed our [Web SDK setup](./web-sdk-setup) and can receive web push notifications on other browsers, this step is complete. See [OneSignal Service Worker](./onesignal-service-worker) documentation for detailed setup instructions.

### 3. Configure permission prompts

Existing [Web permission prompts](./permission-requests) from your [Web SDK setup](./web-sdk-setup) will work on iOS devices **only after users add your site to their home screen and open it from there**. This is Apple's design requirement.

### 4. Guide users to "Add to Home Screen"

Unlike desktop or Android devices where permission prompts appear based on your settings, iOS requires a specific user journey that you must facilitate.

#### The required user journey

Users must complete these steps to receive notifications:

1. Visit your website on Safari, Chrome, or Edge on iOS/iPadOS 16.4+
2. Click the browser's **Share** button
3. Select **Add to Home Screen** option
4. Save the app to their device
5. Open the app from the home screen (not the browser)
6. Interact with your subscribe button to trigger the native permission prompt

<Frame caption="Adding a Website to the Home Screen on iOS">
  <img src="https://mintcdn.com/onesignal/2iWYYuHf1gqm06bv/images/docs/638b3a1-ios-web-push-add-to-home-screen.jpg?fit=max&auto=format&n=2iWYYuHf1gqm06bv&q=85&s=54cb44f40d70397099b32375a3e97683" width="1346" height="736" data-path="images/docs/638b3a1-ios-web-push-add-to-home-screen.jpg" />
</Frame>

#### User onboarding strategies

Since this process isn't intuitive, implement clear guidance through:

* **Website banners**: Display banners specifically on mobile Apple devices explaining the value of notifications and providing step-by-step instructions.

* **Visual guides**: Use screenshots and arrows to show users exactly where to tap.

* **Timing**: Present the guidance after users have demonstrated engagement with your content.

#### Implementation examples

Here are effective approaches from real applications:

<Frame caption="Example banner prompting users to add to home screen">
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0b97752-image.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=bfec43a31639c25a6eab85961334a8bd" width="2055" height="1257" data-path="images/docs/0b97752-image.png" />
</Frame>

<Frame caption="Step-by-step visual guidance">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4e970c1-image.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=04aef274f934dd44f34eaa8bd7e37360" width="2055" height="1257" data-path="images/docs/4e970c1-image.png" />
</Frame>

<Frame caption="Benefits-focused messaging">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/208b123-image.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=c8bd38cfb229c68500a9260b8b6e4b33" width="2055" height="1257" data-path="images/docs/208b123-image.png" />
</Frame>

<Frame caption="Clear call-to-action with visual cues">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/7ec125a-image.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=c532cb02bcde365092a6bc001beaaf06" width="2055" height="1257" data-path="images/docs/7ec125a-image.png" />
</Frame>

#### Open source solutions

Consider implementing this popular open-source banner solution:

**GitHub Project**: [add-to-home-screen by rajatsehgal](https://github.com/rajatsehgal/add-to-home-screen)

<Frame caption="Example of an Add to Home Screen banner prompt from an open source project by rajatsehgal.">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b63b31f-GitHub_A2HS_Ex_1.jpg?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=ccc678721ffc636fa5ddb4a71efb7ed0" width="1149" height="2142" data-path="images/docs/b63b31f-GitHub_A2HS_Ex_1.jpg" />
</Frame>

Additional banner examples and best practices available at [web.dev](https://web.dev/promote-install/).

### 5. Testing and validation

#### Manifest file testing

1. **Accessibility Check**: Navigate to `https://yoursite.com/manifest.json` to ensure public accessibility
2. **Browser DevTools**:
   * Open Chrome DevTools (F12)
   * Go to Application tab → Manifest
   * Review any errors or warnings
3. **Online Validators**:
   * [Manifest Tester](https://manifesttester.com/)
   * [Redirection.io Validator](https://redirection.io/tools/web-app-manifest/validator)
   * [ValidBot Manifest Wizard](https://www.validbot.com/tools/app-manifest-wizard.php)

#### End-to-end push notification testing

1. Visit your website on iOS 16.4+ device using Safari, Chrome, or Edge
2. Click the browser's **Share** button
3. Select **Add to home screen**
4. Save the app to your device
5. Open the app from the home screen (crucial step)
6. Trigger your subscribe button - the native permission prompt should appear
7. Grant permission and test notification delivery

#### Important testing notes

**Re-testing requirements**: To test again on the same device:

* Remove the app from home screen
* Clear browser cache (Settings > Safari/Chrome/Edge > Clear cache)
* Repeat the process

**Permission denied recovery**: If permission is denied, the home screen app must be removed and re-added for the permission prompt to appear again.

**Common issues to check**:

* Ensure `display` field is `"standalone"` or `"fullscreen"`
* Verify all icon paths are accessible
* Confirm manifest serves with correct MIME type (`application/manifest+json`)
* Test for CORS errors

***

## Troubleshooting

**Manifest not loading**: Check file path, HTTPS requirement, and MIME type configuration on your server.

**Icons not displaying**: Verify icon file accessibility and correct size specifications in manifest.

**Permission prompt not appearing**: Ensure user accessed site via home screen app and clicked an interactive element first.

**Notifications not delivering**: Verify OneSignal service worker is properly installed and check browser console for errors.

***

## Next steps

<Check>
  You're now ready to send notifications! Continue to [Push](./push) documentation or use our [Create message](/reference/create-message) API to start engaging your iOS users with web push notifications.
</Check>

For ongoing success, monitor your iOS web push performance metrics and consider implementing progressive enhancement strategies that gracefully handle the additional steps required for iOS users while providing seamless experiences on other platforms.

***

Built with [Mintlify](https://mintlify.com).
