# Source: https://jam.dev/docs/jam-for-customer-support/advanced-data-protection-for-customer-support-jams-auto-blur.md

# Advanced Data Protection for  Customer Support Jams (Auto-blur)

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FVRlbi4cluvMUjt9I0Yxb%2F2025-10-29_15-16-03.gif?alt=media&#x26;token=11240334-eb29-404f-9d33-0021d81764a4" alt=""><figcaption></figcaption></figure>

## How it works

The Jam.js snippet automatically detects and blurs sensitive content during recording sessions. When a customer records their issue:

1. Sensitive elements are blurred in real time as they are recorded, and sensitive information is redacted from the console logs.
2. Only the blurred version is captured—sensitive data never reaches Jam's servers.
3. The final Jam shows blurred content exactly as the customer saw it during recording; the console logs will show \<redacted> instead of the sensitive data.

**What gets blurred:** only the elements you want

**Applies to:** Jams you request from your customers via Intercom or Recording Link

{% hint style="info" %}
By default, Jam recognizes the same privacy selectors used by popular tools like FullStory, Hotjar, LogRocket, Sentry, and others. If you're already using these tools, your existing privacy setup works automatically with Jam; if not, it's as easy as adding our selector, or providing us with your own.
{% endhint %}

***

## Setup

**Note:** Blurring is enabled by default once the snippet is installed.

{% hint style="warning" %}
**Blurred content is only supported on sites with verified Jam.js installations.**

Follow the [Recording Links setup guide](https://jam.dev/docs/jam-for-customer-support/send-recording-links-from-your-own-domain-and-collect-console-logs) \[5 mins] before proceeding.
{% endhint %}

### Quickstart

#### - Want to blur something?

Use Jam.js data attributes to opt in:

```
<span data-jam-blur>{ccNumber}</span>
```

Or tell Jam.js about your privacy selectors:

```
<meta name="jam:blur" content=".secret-stuff" />
```

Or if you're using the SDK:

```
jam.initialize({ blurSelectors: ".secret-stuff" });
```

#### - Want to unblur something?

Use Jam.js data attributes to opt out:

```
<span class="cc-number" data-jam-blur="no">{ccNumber}</span>
```

***

### What gets blurred automatically

Jam recognizes privacy selectors from popular session replay and analytics tools. If you already use any of these tools with privacy controls in place, those same elements will be automatically blurred in Jam recordings:

#### Standard selectors

* **Jam**: `[data-jam-blur]`
* **rrweb**: `.rr-block`, `.rr-mask`, `.rr-ignore`&#x20;
* **Additional selectors:**<br>

  > **Standard HTML autocomplete attributes**
  >
  > * `autocomplete="cc-number"` - credit card numbers
  > * `autocomplete="cc-exp"` - credit card expiration
  > * `autocomplete="cc-csc"` - credit card security code
  > * `autocomplete="tel"` - phone numbers
  > * `autocomplete="email"` - email addresses
  >
  > **Common name/id patterns for sensitive fields:**
  >
  > **Social Security Numbers:**
  >
  > * `ssn`, `social-security`, `social_security_number`, `tax-id`
  >
  > **Bank Account:**
  >
  > * `account-number`, `account_number`, `routing-number`, `iban`, `swift`
  >
  > **Credit Cards:**
  >
  > * `card-number`, `cardnumber`, `cc-number`, `creditcard`
  > * `cvv`, `cvc`, `security-code`, `card-code`
  >
  > **Photo IDs/Passports:**
  >
  > * `passport`, `passport-number`, `drivers-license`, `id-number`, `national-id`
  >
  > **Driver's License:**
  >
  > * `license-number`, `drivers-license`, `dl-number`

#### Session replay tools

* **FullStory**: `.fs-exclude`, `.fs-mask`, `.fs-block`, `.fs-unmask` (unblur)
* **Hotjar**: `.data-hj-suppress`, `.data-hj-masked`, `[data-hj-suppress]`, `[data-hj-masked]`
* **LogRocket**: `[data-private]`
* **Microsoft Clarity**: `[data-clarity-mask]`, `[data-clarity-unmask]` (unblur)
* **Sentry**: `.sentry-block`, `.sentry-mask`, `[data-sentry-block]`, `[data-sentry-mask]`
* **OpenReplay**: `[data-openreplay-obscured]`, `[data-openreplay-hidden]`
* **Highlight.io**: `.highlight-block`, `.highlight-mask`, `.highlight-ignore`
* **ContentSquare**: `[data-cs-mask]`, `[data-cs-encrypt]`, `[data-cs-capture]` (unblur)
* **Matomo**: `[data-matomo-mask]`

#### Analytics tools

* **Heap**: `[data-heap-redact-text]`, `[data-heap-redact-attributes]`, `[data-heap-ignore]`, `.heap-ignore`
* **Amplitude**: `[data-amp-mask]`, `[data-amp-unmask]`(unblur)

***

### Add custom selectors for your product

If you are using `@jam.dev/recording-links/sdk`: pass your custom selectors into `initialize(...)` using the `blurSelectors` key:

```
import * as jam from "@jam.dev/recording-links/sdk";

// `blurSelectors` can be a static string:
jam.initialize({ blurSelectors: ".my-custom-blur-class" });

// or an array of static strings
jam.initialize({ blurSelectors: [".blur-class-1", ".blur-class-2"] });

// or a runtime function that evaluates to either of the above
jam.initialize({
  blurSelectors: () => `.my-${Math.ceil(Math.random() * 100)-blur-class`,
});
```

If you are using `<script type="module" ...>` to embed `recorder.js` and `capture.js`: use `<meta>` tags to provide your selectors to Jam.js:

```
<html>
  <head>
    ...
    <meta name="jam:blur" content=".my-custom-blur-class" />
    <meta name="jam:blur" content=".blur-class-1,.blur-class-2" />
  </head>
  <body>
    ...
  </body>
</html>
```

***

### Opt out of blurring for specific elements

If Jam.js is blurring an element it oughtn't, you can use `[data-jam-blur="no"]` to disable blurring:

```
<div class=".rr-block" data-jam-blur="no">
  Blurred in rrweb, but not in Jam
</div>
```

**Selector priority:** Manual opt-out overrides all blurrable matches, whether from a default or custom selector.

***

### Test your setup

Before sharing Recording Links with customers, verify that blurring works correctly:

1. Create a Recording Link with your verified recording URL selected
2. Click your own link and start a recording session
3. Navigate to pages with sensitive content

**What to look for:**

* If sensitive content is blurred during the recording session, it won't appear in the final Jam ✓
* If you can see sensitive content clearly while recording, it will appear in the Jam

This real-time preview shows you exactly what will be captured.

### Limitations

* Content in iframes must be blurred altogether, or not at all—we cannot selectively blur inside an iframe
* Flashes of unblurred content may occur during captured pageloads if your UI initializes before Jam.js. If you see flashes of unblurred content when refreshing a page during a recording, try moving Jam.js initialization earlier in your page's execution, or `await`ing it before displaying sensitive data.

<br>
