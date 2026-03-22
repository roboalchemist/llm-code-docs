# Source: https://docs.brightdata.com/integrations/kameleo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Kameleo

> Integrate Bright Data with Kameleo for secure browsing and efficient management of multiple profiles, offering enhanced privacy and robust protection against detection.

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

## What is Kameleo?

Kameleo is an advanced anti-detection browser designed for users who need to manage multiple online profiles without risking detection. Whether you’re a social media manager, affiliate marketer, e-commerce operator, or web scraper, Kameleo gives you the tools to bypass IP bans, prevent device tracking, and avoid account linking.

With Kameleo, you can customize your browser fingerprints—like user agents, screen resolutions, and fonts—so each profile looks completely unique. This ensures that your activities remain undetected. Kameleo supports a variety of proxies, including residential, datacenter, and ISP proxies, letting you assign different IPs and digital identities to each profile. This makes it perfect for handling multiple accounts across social media platforms, e-commerce sites, and more—all from a single session.

On top of its strong anti-detection features, Kameleo also supports automation tools, making it a powerful choice for bulk tasks like posting or data scraping. Whether you’re managing a handful of profiles or scaling up for larger operations, Kameleo ensures your privacy and security are protected while optimizing your online activities.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## Kameleo Proxy Integration

Follow these simple steps to integrate Bright Data proxies into Kameleo:

<Steps>
  <Step title="Open Kameleo">
    Launch the [**Kameleo app**](https://kameleo.io/downloads/) and log in to your account.
  </Step>

  <Step title="Create a New Profile">
    Click on the **New Profile** option in the left navigation panel to start setting up a new browsing profile.
  </Step>

  <Step title="Configure Your Profile Preferences">
    Select the profile settings that match your preferred device type, operating system, browser, and language settings.
  </Step>

  <Step title="Configure Your Bright Data Proxy">
    Navigate to the **Connection** section in the profile settings and enter the following details to configure your Bright Data proxy:

    * **Proxy**: Choose from `HTTP`, `HTTPS`, or `SOCKS5` (based on your proxy type).
    * **Host:**  Enter `http://brd.superproxy.io/`.
    * **Port**: Use the port number provided in your [Bright Data dashboard](https://brightdata.com/cp/zones).
  </Step>

  <Step title="Enable Authentication">
    Toggle the **Authentication** button to reveal the `Username` and `Password` fields.\
    Enter your Bright Data proxy credentials here.

    To ensure everything works correctly, click the **Test Proxy** button to perform several tests for your proxy connection.

    <Info>
      **For country-specific proxies, you can enter a format like `your-username-country-US` to receive a US exit node.**
    </Info>
  </Step>

  <Step title="Save Your Settings">
    Once you’ve configured your proxy, click **OK** to save your settings.

    Alternatively, click **START** to launch the browser immediately with your configured profile.
  </Step>
</Steps>

And that’s it! You’ve successfully integrated Bright Data proxies with Kameleo.
