# Source: https://jam.dev/docs/record-a-jam/incognito-sessions.md

# Incognito Sessions

### Overview

Jam works seamlessly in incognito mode, giving you complete debugging capabilities while maintaining privacy. Perfect for internal testing, sensitive environments, or when you need to capture bugs without leaving traces in your regular browsing session.

### Key Benefits

**Full feature access:** All Jam tools work in private browsing mode\
**Complete bug context:** Capture instant replay, network logs, console data, and device info\
**Privacy-first testing:** Test and debug without affecting your main browser session\
**Clean environment:** Isolate testing from extensions, cookies, and cached data

### How It Works

When enabled for incognito mode, Jam provides the same comprehensive debugging toolkit you get in regular browsing:

* **Instant replay** captures the last 30 seconds of user actions
* **Screen recording** documents the full bug reproduction
* **Network logs** show API calls, failed requests, and performance data
* **Console logs** capture JavaScript errors and warnings
* **Device information** includes browser, OS, and viewport details

### Getting Started

{% tabs %}
{% tab title="Chrome" %}
![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FPOddjUP3LyAG1j72QTfO%2Fa91f85b5-124d-4374-8da5-f53095acdc1b_796x540.gif?alt=media\&token=e0e2c080-ed0f-4bfe-93a5-b5eb20a8684b)\
\
**Enable Incognito Access in Chrome**

1. Go to [chrome://extensions](chrome://extensions/) in your address bar
2. Find the Jam extension
3. Click Details
4. Toggle on Allow in incognito

You should now see the Jam extension icon in incognito windows.
{% endtab %}

{% tab title="Firefox" %}
**Enable Incognito Access in Firefox**

1. Go to <about:addons> in your address bar
2. Find the Jam extension
3. Click on the extension name
4. Under Run in Private Windows, select Allow

You should now see the Jam extension icon in private windows.
{% endtab %}

{% tab title="Edge" %}
**Enable Incognito Access in Edge**

1. Go to <edge://extensions> in your address bar
2. Find the Jam extension
3. Click Details
4. Toggle on Allow in InPrivate

You should now see the Jam extension icon in InPrivate windows.
{% endtab %}
{% endtabs %}

### FAQs

<details>

<summary>Does incognito mode affect the quality of bug reports?</summary>

No. You get the same comprehensive data collection in incognito mode, including full network logs, console output, and device information.

</details>

<details>

<summary>Can I use Jam in incognito mode without enabling this setting?</summary>

No. Browser security policies require explicit permission for extensions to run in private browsing modes.

</details>

<details>

<summary>Will my incognito browsing data be saved in Jam reports?</summary>

Jam only captures the specific page and interactions you choose to record. Your broader incognito browsing session remains private.

</details>
