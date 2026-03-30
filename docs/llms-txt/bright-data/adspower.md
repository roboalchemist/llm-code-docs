# Source: https://docs.brightdata.com/integrations/adspower.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With AdsPower

> Boost your web scraping and multi-account management with Bright Data and AdsPower. Stay secure and undetectable as you manage multiple accounts effortlessly.

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

## What is AdsPower?

Take control of your multi-account management with AdsPower! This versatile browser is perfect for marketers, e-commerce businesses, and social media managers who need a secure, efficient way to handle multiple accounts at once. Each profile runs in its own isolated environment, keeping your activities discreet and safe from account suspensions or flags.

With AdsPower, you get unique digital fingerprints for every profile—things like IP address, device type, and user agent—ensuring your actions stay under the radar. Whether you’re scaling your e-commerce business, running social media campaigns, or working with affiliate marketing, AdsPower makes managing multiple accounts smooth and secure.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## AdsPower Proxy Integration

Integrating Bright Data proxies with AdsPower is quick and easy. Let’s set you up in a few simple steps:

Step 1. **Download AdsPower**. Head over to the [AdsPower website](https://www.adspower.com/download) to download and install the app.

Step 2. **Create a New Profile.** Once the app is installed, open it and click **New Profile** to create your first browser profile.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/adspower1.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=084f51b96a7e5cfe0da51239c05dd3a1" alt="" width="1016" height="508" data-path="images/integrations/adspower1.png" />
</Frame>

Step 3. **Configure Your Proxies**. Now, let’s set up your Bright Data proxy. Follow these simple steps:

* **Proxy Type**: Choose from`HTTP`,`HTTPS`, or`SOCKS5`(based on your proxy type).

* **Proxy Host**: Enter[`http://brd.superproxy.io/`.](http://brd.superproxy.io/.)

* **Proxy Port**: 33335

* **Proxy Username**: Enter your Bright Data proxy zone`username`.

* **Proxy Password**: Enter your Bright Data proxy zone`password`.

Step 4: Click **Check Proxy** to ensure everything is working.

<Note>
  Some versions of AdsPower use `google.com` as their default test site. Bright data proxies are blocking `google.com`. Validate this is not a search engine website.
</Note>

<Note>
  If you chose either Residential or Mobile proxies you must install Bright Data SSL certificate to secure your end to end communication. **Otherwise you will encounter Errors**.
  SSL installation instructions can be found [here](https://docs.brightdata.com/general/account/ssl-certificate#ssl-certificate)
  Alternatively, you can ignore SSL verification on AdsPower: Go to advanced settings when setting up a profile and paste: `--ignore-certificate-errors` in launch args.
</Note>

<Info>
  **For country-specific proxies, you can enter a format like `your-username-country-us` to receive a United States exit node.**
</Info>

Once everything is in place, click **OK** to save your settings.

Step 5. **Launch the Browser**.\
Click **Open** under **Tags** to launch your browser with the configured proxy.

<Frame as="div">
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/adspower4.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=1e5d2f8418d60b32f943bf863c4719ae" alt="" width="1310" height="273" data-path="images/integrations/adspower4.png" />
</Frame>

That’s it! You’ve successfully integrated Bright Data proxies with AdsPower, and you’re ready to go.
