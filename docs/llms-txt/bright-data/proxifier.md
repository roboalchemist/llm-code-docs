# Source: https://docs.brightdata.com/integrations/proxifier.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Configure Bright Data With Proxifier

> Streamline your network management with Proxifier! By integrating Bright Data, you can securely route traffic from applications that lack native proxy support. With Proxifier's flexible rule-based system, you can customize traffic routing and enjoy seamless, anonymous browsing.

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

## What is Proxifier?

**Proxifier** is a powerful desktop application that allows programs without native proxy support to connect through HTTPS, HTTP, or SOCKS5 proxies. It’s ideal for routing traffic securely, managing application-specific connections, and providing an alternative to VPNs. Its rule-based setup lets you assign proxies to specific applications, giving you precise control over your internet usage.

## How to Integrate Bright Data With Proxifier

**Step 1. Download and Install Proxifier**

1. Visit the [Proxifier website](https://www.proxifier.com/download/) to download the application.

2. Follow the installation instructions and launch Proxifier on your system.

**Step 2. Access Proxy Settings**

1. Open Proxifier and navigate to the **Profile** menu.

2. Select **Proxy Servers** to manage your proxy configurations.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier1.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=5587873c305cfdbf089a88a54f6718d2" alt="" width="1270" height="530" data-path="images/integrations/proxifier1.png" />
</Frame>

**Step 3. Add Your Bright Data Proxy**

1. Click the **Add** button to configure a new proxy.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier2.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=6c0462c726f3c5ad0a9cee4e3ece4b7a" alt="" width="445" height="289" data-path="images/integrations/proxifier2.png" />
</Frame>

2. In the **Proxy Server** dialog, input the following details:

* **Type**: Select HTTP, HTTPS, or SOCKS5.
* **Address**: `http://brd.superproxy.io/`.
* **Port**: Enter the port from your [Bright Data dashboard](https://brightdata.com/cp/zones/page/plans).
* Enable **Authentication** and provide:
  * **Username**: Your Bright Data username.
  * **Password**: Your Bright Data password.

3. Click **OK** to save the settings. The proxy will now appear in the list.

<Note>
  **`For geo-targeted proxies, include the country code in your username (e.g., your-username-country-US for a US-based IP).`**
</Note>

**Step 4. Test the Proxy Connection**

1. In the **Proxy Servers** section, select your configured proxy.

2. Click **Check** and then **Start Testing**. Ensure the test is successful before proceeding.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier3.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=ce2bf34b95290ce73ae27084138c5f77" alt="" width="446" height="288" data-path="images/integrations/proxifier3.png" />
</Frame>

**Step 5. Create Proxy Rules for Applications**

1. Go to **Profile** > **Proxification Rules**.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier4.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=6bd6102843754c25b8dfb7d895bdfe06" alt="" width="1270" height="529" data-path="images/integrations/proxifier4.png" />
</Frame>

2. Click **Add** to set up a new rule.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier5.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=e181edf901b7503c75e96a4ffd4caad1" alt="" width="716" height="428" data-path="images/integrations/proxifier5.png" />
</Frame>

3. Name the rule for clarity.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier6.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=4fe601fd780810fc2be9a435a8d4e614" alt="" width="479" height="534" data-path="images/integrations/proxifier6.png" />
</Frame>

4. Use the **Browse** button to specify the application (e.g., Chrome, Firefox) for the rule.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier7.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=d26b35db023b6143b07a59f20d7db0ad" alt="" width="844" height="305" data-path="images/integrations/proxifier7.png" />
</Frame>

5. Choose how the traffic is routed:

* Through the proxy.
* Directly to the internet.
* Blocked entirely.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier8.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=dc41fdb511b5f3ee0803ace0260626d3" alt="" width="480" height="534" data-path="images/integrations/proxifier8.png" />
</Frame>

6. Save the rule and move it to the top of the list for priority.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxifier9.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=7d293a3c5be4ace8db3833d02915e206" alt="" width="718" height="429" data-path="images/integrations/proxifier9.png" />
</Frame>

**Step 6. Verify and Start Browsing**

1. Launch the application associated with your rule.

2. Visit an IP-checking website (e.g., [httpbin.org/ip](http://httpbin.org/ip)) to confirm that the proxy is active.

With **Bright Data** set up in **Proxifier**, you can manage your network traffic with precision, route applications through secure proxies, and ensure privacy for even the most complex workflows. Whether you need anonymity, faster connections, or app-specific routing, this setup empowers you to control your internet experience with ease.

## Why I get wrong GeoLocation or blocked with Proxifier and BrightData?

Proxifier enables you to control applications running and selectively direct them to route their traffic via Bright Data's proxy. If the application is attempting to access and IP address and not a domain name, Bright Data may either block it or route the request thru our Superproxy servers and not the Proxy peers. It means that the target domain will see this request coming from Bright Data servers and not from your assigned proxy and may block it.

Bright Data does not allow targeting IP addresses due to our compliance rules and regulations.
