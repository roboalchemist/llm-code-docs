# Source: https://docs.brightdata.com/integrations/insomniac.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Insomniac

> Using Bright Data proxies with Insomniac boosts your automation efforts by providing secure, anonymous connections, reducing the risk of detection and ensuring smoother operations.

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

## What is Insomniac?

Insomniac is an online purchasing tool allowing you to hide your digital footprint through its multi-session browser. Insomniac browser allows you to apply one proxy per tab and hide your online footprint by applying a different IP address for every tab you open.

<Tip>
  Maintain a consistent IP throughout your browser session by using the `-session` parameter in your username. This is essential because BrightData proxies default to rotating IPs with each request. [Learn more](https://docs.brightdata.com/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session)

  New users should begin with ISP or Data Center proxies, as residential proxies are incompatible with browser integration in [Immediate-Access mode](https://docs.brightdata.com/proxy-networks/residential/network-access#immediate-access) .

  For use-cases related to **account management**, use a consistent static dedicated IP for each account you are managing. dedicated [ISP proxies](https://docs.brightdata.com/proxy-networks/isp/introduction) should be used for this.
</Tip>

## How to setup Insomniac with Bright Data proxies

### Using the same proxy repeatedly or rotating with new proxy every time?

Bright data offers access to two main kinds of proxies:

1. A rotating pool of proxies
2. A set of fixed proxies (shared with others or dedicated to you)

When choosing a proxy pool like our Datacenter, ISP or Residential shared pools, your isomniac browser does not need to handle the rotation as Bright Data will assign a new proxy for you in every session.

When you need a set of fixed proxies, like for managing social media accounts, you can load all your proxies to insomniac, and it will rotate along them, as you configure it.

## Set-up for Insomniac browser

* Download and install the Insomniac browser
* Open **Insomniac browser**
* Click on "Global sess." :

<Frame>
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/Insomniac_setup_1.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=a8a5905d90046dd1b1800d837a467843" alt="Insomniac_setup_1.png" width="1615" height="651" data-path="images/integrations/Insomniac_setup_1.png" />
</Frame>

* Click on "Proxy List"

<Frame>
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/Insomniac_setup_2.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=31b59c1a99055063cfd1397e7550c740" alt="Insomniac_setup_2.png" width="1389" height="652" data-path="images/integrations/Insomniac_setup_2.png" />
</Frame>

* This setup window will open, requiring you to paste your proxy configuration here.

<Frame>
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/Insomniac_setup_3.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=4b4a6c67c098128b3ed9b2c4a5aea035" alt="Insomniac_setup_3.png" width="1404" height="829" data-path="images/integrations/Insomniac_setup_3.png" />
</Frame>

The format required is **comma separated** proxy configuration: `host,port,user,password` .

## Integrating Insomniac with Bright Data Proxies

* Go to your Bright Data Dashboard and click **Create a Zone**
* Choose your configuration
* Click **Save**
* The zone now includes your proxy setup and in the access details you have the connection information.

If you want to use Bright Data's rotation and use a different proxy for every session, copy and paste this setup from Bright Data's control panel into insomniac.

<Frame>
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/Insomniac_setup_4.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=d486b35850c956cebb6b66b6c2df1243" alt="Insomniac_setup_4.png" width="1444" height="690" data-path="images/integrations/Insomniac_setup_4.png" />
</Frame>

If you wish to load a specific proxies (with distinguished IPs) of Datacenter or ISP, open the zone Overview tab in Bright Data control panel, and click "Download" to download the proxy list. A popup window will open with 3 formats. Insomniac needs comma separates format whch will be available soon in Bright Data. So choose colon seprated as shown here:

<Frame>
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/Insomniac_setup_5_brd_dc_iplistdwnld.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=7440620332b165a40b6f4f0bba63fa18" alt="Insomniac_setup_5_brd_dc_iplistdwnld.png" width="1513" height="838" data-path="images/integrations/Insomniac_setup_5_brd_dc_iplistdwnld.png" />
</Frame>

Open the file with a text editor, and using "Search and Replace" replace all colons with commas. Example in notepad (use `Ctrl+H` to open the Search and replace function):

<Frame>
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/Insomniac_setup_7_proxylist_notepad.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=a22068d563665d7103c5a3eebfc21c87" alt="insomniac_setup_7_proxylist_notepad.png" width="1423" height="723" data-path="images/integrations/Insomniac_setup_7_proxylist_notepad.png" />
</Frame>

After you copy and paste the list, you will have multiple entries of proxies in insomniac which you can order insomniac to rotate on per your desired logic.

## Integrating Multiple Proxy Manager ports with Insomniac

* Download [Proxy Manager](https://brightdata.com/products/proxy-manager)
* Click **Add new Proxy** to create a new port
* Select the new port (24XXX)
* Go to the **General** tab in the port settings
* In the **Multiply proxy port** field select the number of proxy ports to create. This will create multiple proxy ports with the same settings
* Your Spreadsheet Contains the following columns:
  * Custom Name: Add a name for each proxy
  * Host: 127.0.0.1
  * Port: 24XXX
  * Username, Password, and Tags: leave EMPTY(the Proxy Manager has already been authenticated with the Super Proxy)
* Save the file as a **CSV** and not as an XLS or XLSX
* In Insomniac **Proxy per tab** extension select **Manage Proxy list**, and select **Add bulk proxies**
* Select **Import proxy list** and upload the CSV file

<Warning>
  **Important note**:

  If you are using Bright Data’s Residential Proxies, Unlocker API or SERP API, you need to install an SSL certificate to enable end-to-end secure connections to your target website(s).

  This is a simple process, see [this guide](https://docs.brightdata.com/general/account/ssl-certificate#installation-of-the-ssl-certificate) for instructions.
</Warning>
