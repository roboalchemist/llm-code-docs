# Source: https://documentation.onesignal.com/docs/en/clearing-cache-and-resetting-push-permissions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Clearing cache and resetting push permissions

> Learn how to reset browser push permissions, service workers, and site data across Chrome, Firefox, and Safari to ensure clean test environments and resolve web push notification issues.

Residual data from outdated or misconfigured notification settings can prevent push notifications from working properly—even when your current implementation is correct. Use the instructions below to fully reset your browser’s notification permissions, unregister service workers, and clear site data for a clean testing state.

<Tabs>
  <Tab title="Chrome desktop">
    1. Click the **View Site Information** (lock or info) icon next to the URL bar.
    2. Under **Notifications**, click **Reset permission**.
    3. Open [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open) (`F12` on PC or `fn + F12` on Mac).
    4. In the **Application tab > Storage**, click **Clear Site Data**.
    5. When prompted, click **Reload** to refresh the page.

    <Frame caption="Resetting notification permissions and clearing the site's data on Chrome">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/04d0c60-cache_clear.gif?s=d81ea2bdd30c3e4ca2520d15973e7dbd" width="1497" height="878" data-path="images/docs/04d0c60-cache_clear.gif" />
    </Frame>

    If you have [Prompting](./permission-requests) configured, a new permission request should appear. **Do not subscribe just yet.**

    **Optional:**
    To manually unregister background workers:

    * Visit [chrome://serviceworker-internals](chrome://serviceworker-internals) in a new tab.
    * Find entries under “Scopes” containing your domain.
    * Click **Stop** and **Unregister**.

    <Info>If these buttons are disabled, ensure all tabs for your site are closed.</Info>

    <Frame caption="ServiceWorker Internals Page">
      <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/66CdwknESjeKzX6E2Iim_chrome-reset-4.jpg?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=326254b21fd54428ddbeabee6518eb4d" width="1628" height="1004" data-path="images/docs/66CdwknESjeKzX6E2Iim_chrome-reset-4.jpg" />
    </Frame>

    <Check>Open a *new* tab to your site and try it out!</Check>
  </Tab>

  <Tab title="Chrome Android">
    If you still see a push notification from your site:

    1. Tap the **gear icon > Site Settings**

    <Frame caption="gear icon to settings page">
      <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/MDW3i3T4iktcqQ4APO2w_android-reset-1.jpg?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=20cc54a047131421dd9ee5182d3e4e69" width="1106" height="696" data-path="images/docs/MDW3i3T4iktcqQ4APO2w_android-reset-1.jpg" />
    </Frame>

    2. Tap **Clear & Reset**

    <Frame caption="Settings Page">
      <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/docs/ze8bkPtQKuCY1Ge7fpoW_android-reset-2.jpg?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=81df7e92adf693b7dafdcb0f43b7adda" width="1106" height="1334" data-path="images/docs/ze8bkPtQKuCY1Ge7fpoW_android-reset-2.jpg" />
    </Frame>

    If no notification is visible:

    * Open Chrome, then the **3-dot menu > Settings**
    * Scroll to **Site Settings >Notifications**
    * Ensure it is set to *Ask before sending (recommended)*
    * Find your site in the list, tap it, then tap **Clear & Reset**

    <Check>Open a *new* tab to your site and try it out!</Check>
  </Tab>

  <Tab title="Firefox desktop">
    1. Click the **i** or **lock** icon next to your site’s URL.
    2. Under **Permissions**, next to **Receive Notifications**, click the **X** to remove permission.

    <Frame>
      <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/051cb63-Screen_Shot_2018-12-05_at_11.29.42_AM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=2b72ba582e2c717b98b6ee9758e36cd8" width="690" height="369" data-path="images/docs/051cb63-Screen_Shot_2018-12-05_at_11.29.42_AM.png" />
    </Frame>

    3. In the same dialog, scroll to the bottom and click **Clear Cookies and Site Data...**

    <Frame>
      <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/ed69259-Screen_Shot_2018-12-05_at_11.30.14_AM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=d902816a5851fdeefb8b2bb52283be3e" width="417" height="341" data-path="images/docs/ed69259-Screen_Shot_2018-12-05_at_11.30.14_AM.png" />
    </Frame>

    4. On the popup dialog, click **OK**

    <Frame>
      <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0fa754a-Screen_Shot_2018-12-05_at_11.30.22_AM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=d2cdcf2ffcf657fbbafa102845845d93" width="522" height="402" data-path="images/docs/0fa754a-Screen_Shot_2018-12-05_at_11.30.22_AM.png" />
    </Frame>
  </Tab>

  <Tab title="Firefox Android">
    Refer to [Firefox's official guide](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) to clear browsing data on Android.
  </Tab>

  <Tab title="Safari macOS">
    <Info>
      Apple does not support Web Push in Safari on Windows.
    </Info>

    To reset notification permissions and cache:

    1. From the menu bar, go to: **Safari > Settings > Websites > Notifications**
    2. Find your site and click **Remove**

    <Frame>
            <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6a12291-Screenshot_2023-01-19_at_6.11.08_PM.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=75dfbd00a3ecb9ba7e9fcd269375aa8d" alt="" width="2124" height="1096" data-path="images/docs/6a12291-Screenshot_2023-01-19_at_6.11.08_PM.png" />
    </Frame>

    3. Navigate to **Privacy > Manage Website Data...**

    <Frame>
            <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/523e40e-Screenshot_2023-01-19_at_6.13.42_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=21f7ccf686633cebd08520fb7f9668f0" alt="" width="1772" height="1082" data-path="images/docs/523e40e-Screenshot_2023-01-19_at_6.13.42_PM.png" />
    </Frame>

    <br />

    4. Search for your domain, select it, and click **Remove** or **Remove All**

    <Frame>
            <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6bacb76-Screenshot_2023-01-19_at_6.15.38_PM.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=fd4620e4f5952c5e9a969591ddefe499" alt="" width="1772" height="1224" data-path="images/docs/6bacb76-Screenshot_2023-01-19_at_6.15.38_PM.png" />
    </Frame>

    5. Click **Done**

    <Check>
      Return to your site and refresh. It should behave like a first-time visit.
    </Check>
  </Tab>
</Tabs>

***

Built with [Mintlify](https://mintlify.com).
