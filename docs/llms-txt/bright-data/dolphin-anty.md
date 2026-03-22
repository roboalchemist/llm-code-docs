# Source: https://docs.brightdata.com/integrations/dolphin-anty.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Dolphin Anty

> Enhance your web scraping and multi-account management with Dolphin Anty and Bright Data proxies. Enjoy secure, efficient data extraction and powerful anti-detection features.

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

## What is Dolphin Anty?

Dolphin Anty is an easy-to-use, anti-detection browser built for marketers, social media managers, and e-commerce professionals who need to manage multiple accounts without being flagged. It creates unique digital fingerprints for each profile—like IP addresses and device types—so platforms can’t link multiple accounts to the same user. With Dolphin Anty, you can securely run social media campaigns, manage affiliate marketing, and handle e-commerce tasks—all without worrying about account bans.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## Dolphin Anty Proxy Integration

Here’s a quick guide to get you started:

### Step 1. **Download Dolphin Anty.**

Visit the [Dolphin Anty website](https://dolphin-anty.com/) to download and install the software.

### Step 2. **Create and Log into Your Account.**

After installing Dolphin Anty, open the app, create your account, and log in.

### Step 3. **Create a New Profile.**

Click on **+ CREATE PROFILE** to start setting up your new browsing environment.

### Step 4. **Add a New Proxy.**

Scroll down to the **NEW PROXY** section to begin configuring your Bright Data proxy.

### Step 5. **Configure Your Bright Data Proxy.**

Follow this format for entering your proxy details: `type://host:port:username:password`

* **Type**: Choose `HTTP` or `SOCKS5` (based on your proxy type).
* **Host**: Enter [`http://brd.superproxy.io/`.](http://brd.superproxy.io/.)
* **Port**: Use the port number provided in your [Bright Data dashboard](https://brightdata.com/cp/zones).
* **Username**: Enter your Bright Data proxy `username`.
* **Password**: Enter your Bright Data proxy `password`.

Click the **⮂ Test Connection** button to verify the connection.

<Info>
  **For country-specific proxies, you can enter a format like `your-username-country-US` to receive a US exit node.**
</Info>

### Step 6. **Save Your Settings.**

Once everything is in place, click **+ CREATE** to save your profile.

***

And you're all set! You've successfully integrated Bright Data proxies with Dolphin Anty.
