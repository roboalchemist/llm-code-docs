# Source: https://docs.brightdata.com/integrations/webscraper.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Webscraper.io Proxy Integration

> Learn how to Integrate Webscraper.io with Bright Data proxies.

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

Webscraper.io extension and Webscraper.io Cloud can be your perfect tool for data extraction. With an easy point-and-click interface scraper gather website data in a few minutes.

With Webscraper.io Cloud, automate scraping tasks completely with scheduler, API, data parser, data export, and more.

## Getting started with Webscraper.io

1. Install Web Scraper browser extension via [Chrome Store](https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn?hl=en)

2. Sign up for [Webscraper.io Cloud](https://cloud.webscraper.io/register?luminati)

3. Subscribe to [Scale](https://cloud.webscraper.io/subscription-manager?luminati) plan

4. Open “Proxy Manager” on the left-side toolbar

<Frame>
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/webscraperio_integration6.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=0d2741a5f35432fd269ecd13ecd96ab8" alt="webscraperio_integration6.png" width="237" height="480" data-path="images/integrations/webscraperio_integration6.png" />
</Frame>

## Create a proxy in Bright Data

1. Go to your [Bright Data Dashboard](https://brightdata.com/cp/zones) and click **Add Zone**

2. Select a network type and press **Add Zone**

3. Back in your Bright Data dashboard, click a Zone name

4. Take note of your Zone username and password

5. Switch back to the Web Scraper Cloud Proxy Manager

6. Choose **Bright Data Proxy** as the designated Proxy Server

<Frame>
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/webscraperio_integration7.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=107a6619e23e303ad7a309838de97daa" alt="webscraperio_integration7.png" width="1154" height="107" data-path="images/integrations/webscraperio_integration7.png" />
</Frame>

7. Input a custom name, the username, and password form Bright Data created zone.
   If needed, limit your proxy region by selecting a country in the drop-down menu.

<Frame>
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/webscraperio_integration5.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=a9ca20a0fc41e436091c501919478084" alt="webscraperio_integration5.png" width="1154" height="502" data-path="images/integrations/webscraperio_integration5.png" />
</Frame>

8. Click **Add Proxy**

9. The custom proxy will now be listed down below

<Frame>
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/webscraperio_integration1.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=933eaabb95745a520372dd19f72f02c6" alt="webscraperio_integration1.png" width="987" height="171" data-path="images/integrations/webscraperio_integration1.png" />
</Frame>

10. To use a proxy for a scraping job, go to “My Sitemaps” from the menu on the left side

<Frame>
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/webscraperio_integration4.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=acfada3ca07ab657bd62318fb66f8537" alt="webscraperio_integration4.png" width="232" height="500" data-path="images/integrations/webscraperio_integration4.png" />
</Frame>

11. Click **Details Page** next to the sitemap you want to scrape

<Frame>
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/webscraperio_integration2.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=34a4d177335bf7ca356a397bf45d7726" alt="webscraperio_integration2.png" width="1506" height="168" data-path="images/integrations/webscraperio_integration2.png" />
</Frame>

12. From the **Proxy** drop-down menu select the created proxy and click **Scrape**

<Frame>
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/webscraperio_integration3.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=20f62632d3248853f291018c04504d65" alt="webscraperio_integration3.png" width="1574" height="397" data-path="images/integrations/webscraperio_integration3.png" />
</Frame>

There you have it - Webscraper.io Cloud will run your scraper via Bright Data Proxy.
As easy as that!

### Webscraper.io is Not A Bright Data Product

Note: the webscraper.io is not Bright Data Web Scraper API utility - this article refers to the external Webscraper.io integration.&#x20;
