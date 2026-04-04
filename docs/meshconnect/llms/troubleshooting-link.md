# Source: https://docs.meshconnect.com/testing/troubleshooting-link.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# null

## Link UI is not displaying in your webpage

**Symptoms:**

* When initializing the Link UI, you see a grey box instead of the Link UI
* An error in the browser's console that says `Refused to frame 'https://web.meshconnect.com/' because an ancestor violates the following Content Security Policy directive...`

![CORS Error](https://files.readme.io/c063393-cors_error.png)

**Causes:**

* When using the Link Web SDK in your page, Mesh SDK loads the Link UI using an iFrame component. Due to security reasons, we allow loading the Link UI only on a predefined set of URLs.
* If you are using a Content Security Policy (CSP) directives on your website, they might block loading an external iFrame into your page.

**Troubleshooting:**

* [ ] &#x20;Add your website's URL to the list of **Allowed Link URLs** in our [dashboard](https://dashboard.meshconnect.com/company/keys).
* [ ] &#x20;Add the following CSP directives to your site:\
  `frame-src: *.meshconnect.com`

# Unable to connect an OAuth integration

**Symptoms:**

* When authenticating on a third party integration's side (e.g., Coinbase or Gemini), the user gets stuck on a page displaying a loading spinner

**Causes:**

* Ad-blocking software is not officially supported with Link UI, and some ad-blockers have been known to cause issues with Link.
* Some browsers have built-in ad-blocking service (Brave Browser) which prevents Link UI from using the browser's storage.

**Troubleshooting:**

* [ ] &#x20;Disable all ad-blockers in your browser
