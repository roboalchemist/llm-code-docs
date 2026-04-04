# Source: https://jam.dev/docs/jam-for-customer-support/send-recording-links-from-your-own-domain-and-collect-console-logs.md

# Send Recording Links from your own domain and collect console logs

{% hint style="info" %}
You'll need write permissions to your website to complete these three steps:

1. **Register one or more Recording URLs** with Jam\
   \&#xNAN;*(so we can generate links to your site)*
2. **Set up Jam's Recorder & Capture Scripts** on your site\
   \&#xNAN;*(so your users can start recording & capturing page context)*
3. **Modify your Content-Security-Policy** if necessary\
   \&#xNAN;*(so Jam assets can execute on your page)*
   {% endhint %}

## 1. Register one or more Recording URLs

{% hint style="info" %}
Hosted Recording Links bring users directly to your pages. You may show them content before and after the recording begins. Each base Recording URL must be registered before use.
{% endhint %}

Navigate to your Jam team's settings page, and click the "Recording Links" tab. [Here's a quick link to get there.](https://jam.dev/s/settings/recording-links)

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FPNIrkNM5bnWEGwcyHy4p%2FRecording_Links_Settings_Setup_GIF.gif?alt=media&#x26;token=9145afd7-ff60-4008-89f9-e6c0417edf6b" alt=""><figcaption></figcaption></figure>

Under Recording URLs: add, install, and verify the installation of one or more valid URLs. These will later be available to select when creating a Recording Link.

If your application redirects users from your Recording URL—for example, redirecting unauthorized users to a login page—you will need to persist Jam's querystring parameters through the redirect. Most important is `jam-recording=...`, but all `jam-` parameters should be persisted.

{% hint style="warning" %}
You will need at least one Recording URL for each domain you wish to record on. Recordings have access only to debug data from capture scripts on pages on the same domain that initiated the recording.\
\
In most cases, a recoder installed on the root domain will also be able to capture events from subdomains. The exception is Safari, where events will only be captured if recorder and capture script are on the same subdomain.&#x20;

**For example:** a recorder installed on `example.com/recorder` can see events from pages on `sub.example.com` (and vice-versa) except on Safari.
{% endhint %}

## 2. Set up Jam's Recorder & Capture Scripts

{% hint style="info" %}
To properly associate your users' recordings with the logs we collect, Jam's Recorder and Capture scripts need to be served under the *same origin* \[[MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)] as your site or application.
{% endhint %}

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FRHAmQjgqe5mSJuuwhjjs%2FRecording_Links_Team_ID_GIF.gif?alt=media&#x26;token=03634380-f754-45c4-ae58-92301040064b" alt=""><figcaption></figcaption></figure>

Use Jam.js' Recorder and Capture scripts to initialize a recorder on your page and associate captured events.

```html
<html>
  <head>
    <!-- Lets users record their screen from your site -->
    <meta name="jam:team" content="my-team-id-from-dashboard" />
    <script type="module" src="https://js.jam.dev/recorder.js"></script>

    <!-- Captures user events and developer logs -->
    <script type="module" src="https://js.jam.dev/capture.js"></script>
  </head>
</html>
```

The Recorder script will cause our Recorder UX to pop up over your page when users open your Recording Links. If the user dismisses the Recorder UX before starting a recording, they must re-click your Recording Link to try again.

The Capture script will capture events—such as console logs, network events, clicks, and keypresses—on your pages when recordings are in progress. These will be associated and saved with your users' recordings, and otherwise ignored.

Once the recording is complete, Jam will confirm that the user would like to discard their recording if they try to close the Recorder UX before the Jam has been submitted.

Once the Jam has been submitted, the Recorder UX will close automatically, restoring control to your page.

{% hint style="success" %}
To verify this is working: create a Recording Link, then navigate to it. Does the Recorder UX pop up?\
\&#xNAN;*(For not-yet-deployed sites, you must replace the Recording Link URL's host with your localhost equivalent)*
{% endhint %}

We aggressively cache Jam.js assets to minimize load time—especially the Capture script!—prioritizing only critical code and deferring the rest to ensure your page continues to load and run rapidly.

{% hint style="warning" %}
Note: Jam.js' Capture script can only capture console and network requests made after it initializes.

The `<script>` tag should be placed as early as possible on the page, and should only use a lazy-loaded `import` when explicitly trading accuracy for un-cached load performance (e.g. on SEO-optimized pages).
{% endhint %}

## 3. Modify your Content-Security-Policy

*(If your site does not specify CSP directives, you can skip this step.)*

Some sites specify Content-Security-Policy \[[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)] directives via either a header or meta tag. A `frame-src` or `script-src` directive that doesn't include `*.jam.dev` will block Jam.js from including console logs with your user's Jams.

To fix this, modify your CSP header or meta tag to allow `*.jam.dev` as both. For example:

```
<meta
  http-equiv="Content-Security-Policy"
  content="frame-src 'self' *.jam.dev; script-src 'self' *.jam.dev;"
/>
```

## Verify logs are captured

Congratulations! You should now be able to capture logs on your domain. To verify your install is working correctly, simply click the Verify link in your Recording URL settings:

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FSeOf4D2aZ7kkvA6ulQru%2FRecording_Links_Verify_GIF.gif?alt=media&#x26;token=bc802795-d5db-4d3a-8d7d-7cc15cec8b6a" alt=""><figcaption></figcaption></figure>

This will open your Recording URL to a special "verify" UI. If you see this, it means you've successfully installed the Recorder script. If you have a tab open with the Capture tab successfully installed on it, the test will succeed; otherwise you'll have to open a tab to such a page or revisit that installation step.

{% hint style="warning" %}
If you are testing not-yet-deployed code, try replacing the URL we open with your localhost equivalent
{% endhint %}

{% hint style="info" %}
If your code calls `window.jam.recorder.open(...)` manually, simply provide "verify" as the `recordingId`.
{% endhint %}

## **Jam.Metadata**

With one additional function call, `jam.metadata()`, you can ensure that every Jam submitted from your website includes the metadata you need to debug the bug. You can log anything in Jam.Metadata: simple static values like User ID, to any data like redux or react state. Whatever you need to debug, just send it to Jam.Metadata so it's always there for you in any ticket. More information can be found [here](https://jam.dev/docs/debug-a-jam/devtools/jam.metadata).

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F9Fd2qIxw5wGWUoaevn85%2Fimage.png?alt=media&#x26;token=67f16468-3c13-4485-a5f5-62bc1bb8f0bc" alt=""><figcaption></figcaption></figure>

## FAQs

* **Q: Can I put the Recorder and Capture scripts on different pages?**\
  A: Yes! There is no danger in doing so. If you do, the `<meta name="jam:team" ...>` element must be included on pages with the recorder script, and may be omitted from ones with only the capture script.
* **Q: Can I programmatically create Recording Links directly on my page?**\
  A: Not at this time; an upcoming release will expose an API you can use to create Recording Links from anywhere—Slack, Zendesk, or directly on your site (or app).
* **Q: Can I customize the Recorder UI?**\
  A: Not at this time—but we'd like to make this more customizable. Please let us know what you'd like to do!
* **Q: Can I associate Jam data with recordings we manage?**\
  A: No; due to browser storage + message partitioning controls, Jam's Recording Links scripts only work when used together.

## **Current limitations**

* Log capture is fully-supported in Chrome (including Incognito Windows) and Firefox (including Private Windows), and supported in most Safari windows. Log capture from Safari Private Windows is not currently supported.
* If the Capture script is installed within an iframe, the top level logs will not get captured, e.g. capturing logs in embedded Shopify apps.
* When using the `async` and `defer` script attributes or lazy-loaded `import(...)` calls with Jam's Capture script, we cannot guarantee it will run early enough to capture *every* console log, network request, or other capturable event.
