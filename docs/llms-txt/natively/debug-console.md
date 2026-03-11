# Source: https://docs.buildnatively.com/guides/integration/debug-console.md

# Debug Console

The Natively Debug Console is a built-in inspector that allows you to monitor the communication between your web application and the native mobile environment. It is the most powerful tool for identifying issues with native features.

{% hint style="info" %}
When submitting a support ticket regarding a native feature not working, please always attach a screenshot of the Debug Console. This provides us with the raw logs needed to skip the "guessing" phase and move straight to a resolution.
{% endhint %}

### Why use the Debug Console?

* Instantly see if a native SDK (OneSignal for  Push Notifications or RevenueCat for In-app Purchases) is receiving data from your web app.
* Monitor logs and API responses directly on your physical device.
* Attaching a screenshot from the Debug Console to your support ticket allows our team to identify and fix your issue significantly faster.

### Implementation

{% tabs %}
{% tab title="Bubble.io Plugin" %}
To trigger the console, ensure you are using Natively iOS & Android app builder Plugin is updated to the latest version.You simply call the action from any workflow (such as a button click).

**1. Add the Action**

In your Bubble Editor, create a new workflow (e.g., *When Button 'Open Debug' is clicked*).

**2. Select the Natively Action**

Search for the following action in the workflow selector:

`Natively - Open Debug Console`

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FgfTeNXXuTa8LfykfVlqQ%2Fopen_debug_console.png?alt=media&#x26;token=99a47bb0-64d5-4ee0-a89b-a73c0210afbc" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="JavaScript SDK" %}
To trigger the console, ensure you are using JS SDK is updated to the latest version. You can call the console via a button click or a specific debug workflow in your app.

Use the global natively object to trigger the console from any JavaScript function.

```javascript
// Open the debug console
window.natively.openConsole();
```

{% endtab %}

{% tab title="React/Next.js" %}
To trigger the console, ensure you are using JS SDK is updated to the latest version. You can call the console via a button click or a specific debug workflow in your app.

You can call the function directly from the `useNatively` hook.

```javascript
import { useNatively } from 'natively';

const MyComponent = () => {
  const natively = useNatively();

  return (
    <button onClick={() => natively.openConsole()}>
      Open Debug Console
    </button>
  );
};
```

{% endtab %}
{% endtabs %}

**Preview & Test**

Once the feature is triggered in your app, the console will slide up over it, showing logs.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fbcex3lA66AhW9Jvo9mDL%2Fnatively_debug_console_example.png?alt=media&#x26;token=67164457-9faa-4465-a4af-dbfb59d1d739" alt="" width="188"><figcaption></figcaption></figure>

### Troubleshooting

If you trigger the Natively Debug Console feature and nothing happens, check these two common blockers:

#### 1. Environment Mismatch

The Debug Console is a native feature.

* It will not work in standard mobile browsers (Safari, Chrome), or wrappers created by other services.
* It will work in your own builds created with Natively.

#### 2. Missing JS SDK Integration

The `openConsole` command is a message sent from your website to the native app. If the Natively JS SDK isn't properly installed in your web app's header, the message is never sent.

* How to fix: Ensure you have added the Natively script tag to your site's `<head>` or installed the `natively` package.
* Check: Open your web browser's inspector (on desktop) and type `window.natively`. If it returns `undefined`, the SDK is not integrated correctly. Please follow this guide to integrate the Natively JS SDK: [#javascript-sdk](https://docs.buildnatively.com/guides/how-to-get-started#javascript-sdk "mention")
