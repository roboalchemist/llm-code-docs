# Source: https://docs.buildnatively.com/guides/integration/open-an-external-app-url.md

# Open an external App/URL

Natively allows you to open web URL, trigger other installed applications, or direct users to their device system settings.

{% hint style="info" %}
Use the In-App Browser for web pages to keep users inside your app. Use the System Browser (device's default browser) for file downloads or third-party authentication to ensure system compatibility.
{% endhint %}

#### Why use Open an external App/URL?

* In-App Browsing: Display content (like articles or Terms of Service) in a temporary window within your app. This allows them to return to your app with a single tap.
* System Browser (Default): Hand over the URL to the device’s default browser (Safari or Chrome). Use this for file downloads, third-party authentication (OAuth), or external services that require the user's saved passwords and browser history.
* Deep Linking: Launch other installed apps directly. This is perfect for opening a specific location in Google Maps, starting a WhatsApp chat, or triggering a dialer with a pre-filled phone number.

### Open external URL

{% tabs %}
{% tab title="Bubble.io Plugin" %}
To use these features, ensure your Natively iOS & Android app builder Plugin is updated to the latest version. You can trigger these actions from any Bubble workflow.

Action **Natively - Open external url**

* URL: The destination address (e.g., `https://example.com`).
* External (yes/no):

  * **no**: Opens inside the app's browser (with a "Close" icon).

  <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fz7lk3jUR0IvUBvxL4XTP%2Fnatively_open_external_url_action_external_false.png?alt=media&#x26;token=af562462-1483-4615-9018-255595e4c2b9" alt=""><figcaption></figcaption></figure>

  <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FgA4iitjDzR8cORSyT4P6%2FAdobe%20Express%20-%20open_external_url_external_false.gif?alt=media&#x26;token=cf5a047e-e569-47e5-82ae-eb099ef9ac97" alt="" width="147"><figcaption></figcaption></figure>
* **yes**: Launches the system browser (Safari/Chrome).

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FyyMDzWNgRRFCgyZd38wx%2Fnatively_open_external_url_action_external_true.png?alt=media&#x26;token=d530cd53-0bf1-40af-aff4-26477bdc8578" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FfOvguEMdySObzlQVTD98%2FAdobe%20Express%20-%20open_external_url_external_true.gif?alt=media&#x26;token=2f997055-a133-4740-8e04-279c2edefa25" alt="" width="179"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="JavaScript SDK" %}

Ensure your Natively JS SDK is updated to the latest version. You can invoke these methods directly from your JavaScript logic.

```javascript
// Parameters: (url: string, external: boolean)
const url = "https://example.com/";
const external = true; // true = System Browser, false = In-App Browser

window.natively.openExternalURL(url, external);
```

{% hint style="warning" %}
**Critical for Social Auth:** You must set this to `true` for Social Authentication flows (e.g., Google, LinkedIn, or Facebook Login). OAuth providers specifically blocks login attempts made inside embedded webviews for security.
{% endhint %}

```javascript
const external = false; // In-App Browser
```

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FgA4iitjDzR8cORSyT4P6%2FAdobe%20Express%20-%20open_external_url_external_false.gif?alt=media&#x26;token=cf5a047e-e569-47e5-82ae-eb099ef9ac97" alt="" width="147"><figcaption></figcaption></figure>

```javascript
const external = true; // System Browser
```

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FfOvguEMdySObzlQVTD98%2FAdobe%20Express%20-%20open_external_url_external_true.gif?alt=media&#x26;token=2f997055-a133-4740-8e04-279c2edefa25" alt="" width="179"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### Open external App

Opens another application using a URL scheme.

* **Critical Setup:** To use an app scheme in your app, you must whitelist it in your Natively Dashboard > Settings > External App Schemes. Because this change modifies the app's code, you must create a new build after adding a new scheme for the changes to take effect.

{% hint style="info" %}
**How to add app schemes**: For a walkthrough on configuring these in your dashboard, please refer to our [Settings Guide](https://docs.buildnatively.com/natively-platform/settings#external-app-schemes).
{% endhint %}

{% tabs %}
{% tab title="Bubble.io Plugin" %}
To use these features, ensure your Natively iOS & Android app builder Plugin is updated to the latest version. You can trigger these actions from any Bubble workflow.

Action **Natively - Open external app**

* App url: The app's unique scheme (e.g., `whatsapp://`).
* Check this [comprehensive list](https://medium.com/@contact.jmeyers/complete-list-of-ios-url-schemes-for-apple-apps-and-services-always-updated-800c64f450f) for common iOS/Android schemes.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FWxAsF0jBojBcEMnqadJO%2Fnatively_open_external_app_action.png?alt=media&#x26;token=a96cff8f-356c-4a49-9eb5-4c5d4e5ada45" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FRKgB22acn836OFnHyWPN%2Fopen_external_app.gif?alt=media&#x26;token=5152b6f5-2248-439e-98a9-fffc9e085f00" alt="" width="223"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="JavaScript SDK" %}
Ensure your Natively JS SDK is updated to the latest version. You can invoke these methods directly from your JavaScript logic.

```javascript
const scheme = "whatsapp://send?phone=000000000&text=Hi!"; // Example to open the Whatsapp
window.natively.openExternalApp(scheme);
```

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FRKgB22acn836OFnHyWPN%2Fopen_external_app.gif?alt=media&#x26;token=5152b6f5-2248-439e-98a9-fffc9e085f00" alt="" width="223"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### Troubleshooting

**Missing URL Protocol**

Ensure your URLs always start with the protocol. For example, `example.com` will fail, while `https://example.com` will work. For app schemes, ensure you include the `://` suffix. For example, `whatsapp` will fail, while `whatsapp://` will work.

**App Not Installed**

When using `Open External App`, the native system will only respond if the target application is actually installed on the user's device. If the app is missing, the command will be ignored by the OS.
