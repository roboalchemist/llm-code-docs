# Source: https://docs.brightdata.com/integrations/windows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data on Windows

> Set up Bright Data proxies on Windows 10 or 11 to improve privacy, access geo-restricted content, and securely route your traffic. This guide walks you through the configuration step by step.

<Accordion title="Expand to get your Bright Data Proxy Access Information">
  ### Your proxy access information

  Bright Data proxies are grouped in "Proxy zones". Each zone holds the configuration for the proxies it holds.

  To get access to the proxy zone:

  1. Login to Bright Data control panel
  2. Select the proxy zone or setup a new one
  3. Click on the new zone name, and select the **Overview** tab.
  4. In the overview tab, under **Access details** you can find the proxy access details, and copy them to clipboard on click.
  5. You will need: Proxy Host, Proxy Port, Proxy Zone username and Proxy Zone password.
  6. Click on the copy icons to copy the text to your clipboard and paste in your tool's proxy configuration.

  ### Access Details Section Example

    <img src="https://mintcdn.com/brightdata/fC1f9RYBP6dv7X6V/snippets/accessdetails.png?fit=max&auto=format&n=fC1f9RYBP6dv7X6V&q=85&s=dfffcbfd5b7b4f07481f534159e6f710" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### Residential proxy access

  To access Bright Data's **Residential Proxies** you will need to either get verified by our compliance team, or install a certificate. [Read more...](https://docs.brightdata.com/proxy-networks/residential/network-access)

  ### Targeting search engines?

  If you target a search engine like google, bing or yandex, you need a special Search Engine Results Page (**SERP**) proxy API. Use Bright Data SERP API to target search engines.
  [Click here to read more about Bright Data SERP proxy API.](https://docs.brightdata.com/scraping-automation/serp-api/introduction)

  ### Correct setup of proxy test to avoid "PROXY ERROR"

  In many tools you will see a "test proxy" function, which performs a conncectivity test to your proxy, and some add a geolocation test as well, to identify the location of the proxy.
  To correctly test your proxy you should target those search queries to:
  `https://geo.brdtest.com/welcome.txt` .

  Some tools use popular search engines (like google.com) as a default test target. Bright Data will block those requests and you tool will show **proxy error** although your proxy is perfectly fine.

  If your proxy test fails, this is probably the reason. Make sure that your test domain is not a search engine (this is done in the tool configuration, and not controlled by Bright Data).
</Accordion>

<Tip>
  Maintain a consistent IP throughout your browsing session by using the `-session` parameter in your username. Bright Data proxies rotate IPs by default.\
  [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session)

  New users should begin with **ISP or Data Center proxies**, as residential proxies are incompatible with browser integration in Immediate-Access mode.

  For **account management use cases**, use a consistent static dedicated IP per account. Dedicated ISP proxies are recommended.
</Tip>

## Why Use Bright Data on Windows?

Configuring Bright Data on Windows allows you to:

* **Protect Your Privacy**: Mask your real IP address across browsers and applications
* **Access Geo-Restricted Content**: Route traffic through different countries or regions
* **System-Wide Proxy Support**: Apply proxy settings to all apps that follow Windows network configuration
* **Stable, Secure Connections**: Reduce detection risks during browsing or automation tasks

***

## Setting Up Bright Data Proxies on Windows

The proxy setup process is the same for **Windows 10 and Windows 11**. Follow the steps below to configure Bright Data at the system level.

### Step 1. Open Network & Internet Settings

1. Press **Windows + I** to open **Settings**.
2. Navigate to **Network & Internet**.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/windows1.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=6ea2c531b8cc390ab1b94b4f54ae6504" alt="" width="1920" height="1020" data-path="images/integrations/windows1.png" />
</Frame>

***

### Step 2. Enable Automatic Detection

1. Select **Proxy** from the left-hand menu.
2. Under **Automatic proxy setup**, turn **Automatically detect settings** **On**.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/windows2.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=838256cab6af7218727263786a030906" alt="" width="1920" height="1020" data-path="images/integrations/windows2.png" />
</Frame>

***

### Step 3. Configure Manual Proxy Settings

1. Scroll down to **Manual proxy setup**.
2. Toggle **Use a proxy server** to **On**.
3. Enter the following values:

* **Address**: `brd.superproxy.io`
* **Port**: Use the port provided in your Bright Data dashboard

4. Click **Save** to apply the settings.

<Note>
  Windows does not store proxy usernames and passwords in system settings.\
  When prompted by a browser or application, enter your Bright Data **Username** and **Password** to authenticate.

  To maintain IP consistency or enable geo-targeting, append parameters to your username (for example, `-session-1` or `-country-US`).
</Note>

***

## Verify the Proxy Connection

After saving the settings:

1. Open a browser on your Windows device.
2. Visit:

[http://httpbin.org/ip](http://httpbin.org/ip)

3. Confirm that the displayed IP matches your Bright Data proxy.

***

## Best Practices

* Use **ISP or Datacenter proxies** for better stability on Windows
* Avoid frequently toggling proxy settings during active sessions
* Use one dedicated proxy per account for account-based workflows
* Keep Bright Data credentials secure
* Recheck proxy settings after Windows updates

***

## Conclusion

You’ve successfully configured **Bright Data on Windows**. Your system traffic is now routed through secure, anonymous proxy connections, enabling private browsing and geo-flexible access across applications. With Bright Data in place, you can work, browse, and automate confidently on Windows.
