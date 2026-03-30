# Source: https://docs.buildnatively.com/guides/integration/open-app-settings.md

# Open app settings

If a user accidentally denies a permission (like Camera or Location), use the Open App Settings feature to send them directly to the system menu where they can re-toggle permissions.

### Implementation

{% tabs %}
{% tab title="Bubble.io Plugin" %}
To use this feature, ensure your Natively iOS & Android app builder Plugin is updated to the latest version. You can trigger these actions from any Bubble workflow.

A simple action that opens the user's system settings for your specific app. Highly useful for "Permission Denied" states.

Action **Natively - Open external app**

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fb2ou7ZbfsBSg4X4tnbVV%2Fnatively%20_open_app_settings_action.png?alt=media&#x26;token=8fc61d0f-8b47-4225-ac10-b5880b7f95b3" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F8rKGxD1E3vf53Hpps1AO%2Fnatively_open_settings.gif?alt=media&#x26;token=50b94d38-0a4e-4695-80be-3d4a49e05103" alt="" width="189"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="JavaScript SDK" %}
Ensure your Natively JS SDK is updated to the latest version. You can invoke these methods directly from your JavaScript logic.

```javascript
window.natively.openAppSettings();
```

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F8rKGxD1E3vf53Hpps1AO%2Fnatively_open_settings.gif?alt=media&#x26;token=50b94d38-0a4e-4695-80be-3d4a49e05103" alt="" width="189"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

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
