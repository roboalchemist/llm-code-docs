# Source: https://docs.buildnatively.com/guides/integration/how-to-get-started.md

# How to get started?

## Quickstart

Integrate Natively into your existing web application to unlock native mobile capabilities. Choose your integration method below to get started.

{% tabs %}
{% tab title="Bubble.io Plugin" %}
The fastest way to convert your Bubble web app into a native mobile experience.

**Installation**

* Navigate to the Plugins tab in your Bubble editor.
* Search for [Natively](https://bubble.io/plugin/natively---fast-mobile-app-wrapper-1654595882459x381599056563798000) and click Install.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FIn6GrYUzjDiDwS2kLeg6%2Fnatively_bubble_plugin.png?alt=media&#x26;token=fde581cd-173c-43f1-97bb-e01b67b69354" alt=""><figcaption></figcaption></figure>

**Configuration (Headers)**

The **mode** field in the plugin settings controls environment-specific behavior:

* `debug`: Enables detailed error alerts and console logs. Recommended during development.
* `preview`: Required for testing Push Notifications within the [Natively Preview app](https://docs.buildnatively.com/natively-platform/preview). Remove this tag before testing your own build.

**Configuration (API Keys)**

* `onesignal_appId` : Links your mobile app to your specific OneSignal project to enable device registration.
* `onesignal_apiKey`: Authorizes your Bubble web app to trigger [push notifications](https://docs.buildnatively.com/guides/integration/push-notifications-onesignal) via OneSignal.
* `revenuecat_apiKey` : Allows your Bubble web app to verify purchases and sync subscription statuses with RevenueCat ([In-app purchases](https://docs.buildnatively.com/guides/integration/in-app-purchases)).

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F6AYBdHUh4kPSRO1zgehO%2Fnatively_bubble_plugin_settings.png?alt=media&#x26;token=bc20a184-e201-495f-806d-f303975cedb3" alt=""><figcaption></figcaption></figure>

Explore our Example App to see a configuration of the Natively plugin. Use this sandbox to inspect functional workflows, element states, and API setups.

* Editor Link: [Natively QA Sandbox](https://bubble.io/page?name=index\&id=nativelyqa\&tab=tabs-1)
* Credentials: `Username: 1` / `Password: 1`

{% hint style="warning" %}
Avoid calling "Get" actions (like getting Device Info) on Page Load (or similar events). The Natively plugin needs a few milliseconds to inject into your site. Use a slight delay or trigger actions based on user interaction to ensure the plugin is active.
{% endhint %}

{% hint style="warning" %}
This plugin's elements must be set to Visible on page load to initialize correctly. It should be placed directly on the page root and not inside hidden containers, such as Popups, Floating Groups, Group Focus elements, or Repeating Groups. To hide the element from your UI, you may set its dimensions to 0x0 px.
{% endhint %}
{% endtab %}

{% tab title="JavaScript SDK" %}
Include the Natively SDK to bridge the gap between your web code and the mobile OS.

Add the following to your `<head>` tag.

```javascript
<head>

    <script 
        async 
        onload="nativelyOnLoad()" 
        src="https://cdn.jsdelivr.net/npm/natively@2.20.0/natively-frontend.min.js">
    </script>


    <script>
        function nativelyOnLoad() {
            // The SDK is now successfully injected into the global window object.
            
            // --- DEBUG MODE ---
            // Set to TRUE during development: Shows native OS alerts if an SDK error occurs.
            // Set to FALSE or not included in production: Prevents users from seeing raw error messages.
            window.natively.setDebug(true);

            console.log("✅ Natively SDK loaded successfully.");

            // Add any other automatic initializations here:
            // e.g., Check permissions, initialize analytics, or setup your audio player.
        }
    </script>

</head>
```

{% hint style="info" %}
You can target a specific SDK version by modifying the version number in the CDN URL (e.g., `2.20.0`).

* Standard Syntax: `https://cdn.jsdelivr.net/npm/natively@VERSION_NUMBER/natively-frontend.min.js`
* To ensure you are using the most up-to-date features, refer to the [Natively GitHub Repository](https://github.com/No-Code-No-Problem/natively-sdk) for the latest version number.
  {% endhint %}
  {% endtab %}

{% tab title="React/Node.js" %}
**Installation**

Install the Natively package via npm.

```bash
npm install natively@">=2.20.0"
```

**Usage & The `'use client'` Rule**

If you are using Next.js (App Router), the Natively SDK relies on the browser's `window` object. Therefore, any component interacting with Natively must be rendered on the client side. You must declare `'use client';` at the very top of your file.

```typescript
'use client'; // <--- CRITICAL: Natively cannot be executed on the server-side

import { NativelyInfo, useNatively } from 'natively';

export default function NativeDashboard() {
  // 1. Initialize the Wrapper
  // useNatively() is a safe React wrapper around the standard 'window.natively' object.
  // Use this hook instead of calling window.natively directly in React.
  const natively = useNatively(); 

  // 2. Fetch Device Info
  const info = new NativelyInfo();
  const browserInfo = info.browserInfo();

  // 3. Define Actions
  const handleOpenConsole = () => {
    // Check if we are actually inside the compiled mobile app before firing native commands
    if (browserInfo.isNativeApp) {
        natively.openConsole();
    } else {
        console.warn("Console command ignored: You are viewing this in a standard web browser.");
    }
  };

  // 4. Render UI
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h2>📱 App Environment Status</h2>
      
      <p>
        Running inside Native App: 
        <strong> {browserInfo.isNativeApp ? "✅ True" : "❌ False"}</strong>
      </p>
      
     <button 
  onClick={handleOpenConsole}
  style={{ 
    padding: '12px 24px', 
    backgroundColor: '#FD734B', 
    color: '#FFFFFF', 
    borderRadius: '8px', 
    border: 'none', 
    cursor: 'pointer',
    fontFamily: '"Inter", sans-serif',
    fontWeight: 700,
    fontSize: '16px'
  }}
>
  Open Natively Debug Console
</button>
    </div>
  );
}
```

Example project: <https://github.com/romanfurman6/nextjs-boilerplate>

{% hint style="info" %}
You can target a specific version by modifying the version number (e.g., `2.20.0`).

* Standard Syntax: `npm install natively@">=VERSION_NUMBER"`
* To ensure you are using the most up-to-date features, refer to the [Natively GitHub Repository](https://github.com/No-Code-No-Problem/natively-sdk) for the latest version number.
  {% endhint %}
  {% endtab %}
  {% endtabs %}
