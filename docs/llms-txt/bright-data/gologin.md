# Source: https://docs.brightdata.com/integrations/gologin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With GoLogin

> Boost your web scraping and multi-account management with GoLogin and Bright Data, offering robust anti-detection and flexible proxy control.

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

## What is GoLogin?

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .<br />

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

GoLogin is a powerful tool designed to make managing multiple accounts easy and secure. It allows you to create separate browser profiles, each with its own unique fingerprints, IPs, and cookies—making each profile appear like an individual user. This is perfect for marketers, e-commerce businesses, and anyone managing several accounts on platforms that track user behavior.

With GoLogin, you can integrate proxies, automate tasks, and switch between profiles seamlessly, all while keeping each account completely anonymous. It’s a flexible solution that helps ensure account safety, and with its collaboration features, teams can securely share profiles. Whether you’re focused on digital marketing, data scraping, or keeping accounts safe, GoLogin is a fantastic choice.

## GoLogin Proxy Integration

Follow these steps to integrate Bright Data proxies with GoLogin:

<Steps>
  <Step title="Install GoLogin">
    Download and install GoLogin from the [GoLogin website](https://gologin.com/).
  </Step>

  <Step title="Create an Account">
    Log in to GoLogin to get started with the setup.
  </Step>

  <Step title="Create a New Profile">
    Click **+Add profile** and enter the basic details for your new browser profile.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/gologin1.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=b142960b092b89d5f61d6a89a378e6bc" alt="" width="1164" height="126" data-path="images/integrations/gologin1.png" />
    </Frame>
  </Step>

  <Step title="Configure Proxy Settings">
    Enter your Bright Data proxy details:

    * **Proxy Type**: Choose from `HTTP`, `HTTPS`, or `SOCKS5` (based on your proxy type).
    * **Host**: Enter `http://brd.superproxy.io/`.
    * **Port**: Use the port number provided in your [Bright Data dashboard](https://brightdata.com/cp/zones).
    * **Login**: Enter your Bright Data proxy `username`.
    * **Password**: Enter your Bright Data proxy `password`.

    <Info>
      **You can also specify a country for your proxy. For instance, entering `your-username-country-US` will give you a US-based exit node.**
    </Info>

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/gologin2.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=fcd7af845beb2dc590d5032a2ae31207" alt="" width="687" height="633" data-path="images/integrations/gologin2.png" />
    </Frame>
  </Step>

  <Step title="Test the Proxy">
    Click **Check Proxy** to make sure everything is working as expected.
  </Step>

  <Step title="Save and Launch">
    Click **Create Profile** to save your settings, and then hit **Run** to open your new profile with secure browsing.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/gologin3.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=6fdf117e71376f73a05b2e037c031662" alt="" width="640" height="109" data-path="images/integrations/gologin3.png" />
    </Frame>
  </Step>
</Steps>

**And that's it!** You've now successfully integrated Bright Data proxies with GoLogin.
