# Source: https://docs.brightdata.com/integrations/helium-scraper.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Helium Scraper

> Integrate Bright Data with Helium Scraper for secure, efficient, and anonymous web scraping with flexible proxy management.

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

## What is Helium Scraper?

Helium Scraper is an intuitive, desktop-based web scraping tool designed to help you extract data from websites without needing any coding skills. Its visual interface makes it easy to select, extract, and organize data—perfect for both beginners and experienced users alike.

Helium Scraper is ideal for small to medium-scale scraping projects. Whether you're a freelancer, marketer, or business professional, it provides an efficient and straightforward way to collect and structure web data without the complexity of programming.

## Helium Scraper Proxy Integration

Follow these simple steps to set up Bright Data proxies with Helium Scraper:

<Steps>
  <Step title="Install Helium Scraper">
    1. [Download Helium Scraper](https://www.heliumscraper.com/eng/download.php) and install it on your computer.
    2. Launch the tool once the installation is complete.
  </Step>

  <Step title="Access the Proxy List">
    In Helium Scraper, click on **File > Proxy List** to open the proxy configuration panel.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/helium-scraper1.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=7b623918aa9f083b1e96d204ac687a2d" alt="" width="200" height="248" data-path="images/integrations/helium-scraper1.png" />
    </Frame>
  </Step>

  <Step title="Configure Your Bright Data Proxy">
    Add your Bright Data proxy details to the fields provided:

    * **Host**: Enter `http://brd.superproxy.io/`.
    * **Port**: Use the port number provided in your [Bright Data dashboard](https://brightdata.com/cp/zones).
    * **Username**: Enter your Bright Data proxy `username`.
    * **Password**: Enter your Bright Data proxy `password`.

    Click **OK** to store your proxy settings.

    <Info>
      **For country-specific proxies, you can enter a format like `your-username-country-US` to receive a US exit node.**
    </Info>
  </Step>

  <Step title="Enable Proxies for Your Project">
    1. Go to **Project > Settings** from the menu.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/helium-scraper2.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=8aae672241a72ff5a738306330eba7fc" alt="" width="199" height="104" data-path="images/integrations/helium-scraper2.png" />
    </Frame>

    2. In the settings window, set **Enable Proxies** to **True**.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/helium-scraper3.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=6c7c3d9bd064aca8fa74d7d1b2e7a9d3" alt="" width="350" height="554" data-path="images/integrations/helium-scraper3.png" />
    </Frame>
  </Step>

  <Step title="Verify the Proxy Setup">
    1. Open a website that displays your IP address using Helium Scraper’s built-in browser.
    2. Check if the displayed IP matches the Bright Data proxy settings to confirm the proxy integration.
  </Step>
</Steps>

**That’s it!** You've now successfully integrated Bright Data proxies with Helium Scraper.
