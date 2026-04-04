# Source: https://docs.brightdata.com/integrations/octoparse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With Octoparse

> Boost your web scraping efficiency by integrating Bright Data with Octoparse, ensuring secure and anonymous data extraction while reducing the risk of IP blocks.

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

## What is Octoparse?

Octoparse is a user-friendly web scraping tool that allows you to collect data from websites without needing any coding knowledge. With its simple point-and-click interface, Octoparse enables you to extract information from even the most complex sites. It offers the flexibility to customize, automate, and schedule scraping tasks, saving the extracted data in formats such as CSV or Excel. Perfect for market research, price tracking, or lead generation, Octoparse makes data collection fast, easy, and efficient!

## Octoparse Proxy Integration

Follow these simple steps to integrate Bright Data proxies with Octoparse:

<Steps>
  <Step title="Install Octoparse">
    Visit the [Octoparse website](https://www.octoparse.com/download) to download and install the tool.
  </Step>

  <Step title="Create a New Task">
    Click the **+New** button in the top-left corner, then select **Custom Task**.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/octoparse1.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=1bc3b6b76cf839f6ee19a805338ca46d" alt="" width="226" height="175" data-path="images/integrations/octoparse1.png" />
    </Frame>
  </Step>

  <Step title="Enter the Target URL">
    In the **URL Input** field, enter the URL of the website you wish to scrape, then click **Save**.
  </Step>

  <Step title="Access Proxy Settings">
    Once the page loads, navigate to **Task Settings > Anti-blocking**.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/octoparse2.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=e1b2fe8f06918f65c76d9cfb9483204a" alt="" width="468" height="67" data-path="images/integrations/octoparse2.png" />
    </Frame>
  </Step>

  <Step title="Enable Proxy Usage">
    Check **Access websites via proxies** and select **Use my own proxies**. Then click **Configure**.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/octoparse3.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=cfa43161de739f2cfa327e0e2793add2" alt="" width="796" height="544" data-path="images/integrations/octoparse3.png" />
    </Frame>
  </Step>

  <Step title="Configure Your Bright Data Proxy">
    In the pop-up window, enter your Bright Data proxy details in the following format:

    ```sh  theme={null}
    IP/host:port:username:password
    ```

    * **IP/host**: Enter `http://brd.superproxy.io/`.
    * **Port**: Use the port number provided in your [Bright Data dashboard](https://brightdata.com/cp/zones/page/plans).
    * **Username**: Enter your Bright Data proxy `username`.
    * **Password**: Enter your Bright Data proxy `password`.

    <Info>
      For country-specific proxies, you can enter a format like `your-username-country-US` to receive a US exit node.
    </Info>

    If you're using rotating proxies, set the **Switch interval** to specify how often the IPs should rotate. For sticky sessions, adjust it according to your preferred session length.

    <Frame as="div">
            <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/octoparse4.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=b0157e2a28d3ae8d4eb2f218163c33cc" alt="" width="793" height="543" data-path="images/integrations/octoparse4.png" />
    </Frame>
  </Step>

  <Step title="Save Your Settings">
    Click **Confirm** to apply the changes, then click **Save**.
  </Step>
</Steps>

And that's it! You've now successfully integrated Bright Data proxies with Octoparse.
