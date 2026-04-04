# Source: https://docs.brightdata.com/integrations/salefreaks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With SaleFreaks

> Learn how to integrate Bright Data proxies with SaleFreaks to securely manage dropshipping automation, protect seller accounts, and reduce IP-related risks.

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

## What is SaleFreaks?

SaleFreaks is an automation platform built for dropshippers to manage online stores more efficiently. It helps automate key workflows such as product sourcing, order fulfillment, inventory synchronization, and account management. SaleFreaks commonly integrates with marketplaces like eBay and Amazon, where stable IP usage is critical to avoid account flags or suspensions.

Using Bright Data proxies with SaleFreaks improves account safety, enables geo-targeted operations, and ensures long-term automation stability.

***

## Why Use Bright Data With SaleFreaks?

* **Account Protection**: Reduce the risk of marketplace bans by using dedicated, consistent IPs
* **Geo-Targeting**: Operate seller accounts from specific countries or cities
* **High Stability**: Dedicated datacenter or ISP proxies ensure uninterrupted automation
* **Scalability**: Manage multiple seller accounts with isolated proxy identities

***

## Steps to Integrate SaleFreaks With Bright Data Proxies

### Step 1. Sign Up to Bright Data

1. Log in to your Bright Data dashboard
2. Navigate to **Proxy & Scraping Infrastructure**
3. Click **Add** to create a new proxy **Zone**

<Frame caption="Proxy management interface with active proxies and Add button">
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/add-zone-2.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=62502d2b6cee7a834075f1d4270181d9" alt="add-zone-2.png" width="1000" height="324" data-path="images/integrations/add-zone-2.png" />
</Frame>

***

### Step 2. Select Proxy Type

For SaleFreaks, **Datacenter or ISP proxies** are recommended for maximum account stability.

<Frame caption="Web interface for managing proxies and scraping infrastructure">
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/SaleFreaks-4.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=3795e293133b5129f6bc859a697246c8" alt="SaleFreaks-4.png" width="500" height="313" data-path="images/integrations/SaleFreaks-4.png" />
</Frame>

***

### Step 3. Name the Proxy Zone

Choose a clear name for your proxy zone (for example, `salefreaks-ebay-us`).

<Frame caption="Form to choose IP type, showing Dedicated option selected">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/select-ip-type.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=23bc0f28135928c9b060737f271b13d2" alt="select-ip-type.png" width="1000" height="333" data-path="images/integrations/select-ip-type.png" />
</Frame>

***

### Step 4. Select IP Count

Specify the number of IPs required.\
Best practice: **one IP per seller account**.

<Frame>
    <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/number-of-ips-1.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=87cf4921d7a857658d3a2f43b989fb9c" alt="number-of-ips-1.png" width="1000" height="164" data-path="images/integrations/number-of-ips-1.png" />
</Frame>

***

### Step 5. Country & City Selection

Select the country and city that best match your marketplace region.

<Frame caption="Geolocation targeting options for United States and New York City">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/city-ip.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=ef4c7a8441abd53a6f06cc722d6b90fd" alt="city-ip.png" width="1000" height="197" data-path="images/integrations/city-ip.png" />
</Frame>

***

### Step 6. Add the Zone

Click **Add** to create and activate the proxy zone.

<Frame>
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/click-add.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=f9442168a4a097ee04bc09c4c9d679e6" alt="click-add.png" width="1000" height="288" data-path="images/integrations/click-add.png" />
</Frame>

***

### Step 7. Zone Is Ready

Click on the zone name to view configuration details.\
You can edit settings or add more proxies from the **Configuration** page.

<Frame caption="Proxies and Scraping dashboard with various proxy options listed">
    <img src="https://mintcdn.com/brightdata/_z4zr7zjFQ35V26y/images/integrations/zone-ready.png?fit=max&auto=format&n=_z4zr7zjFQ35V26y&q=85&s=451d82ec9afe58c02ac3e98c1bc6cad8" alt="zone-ready.png" width="500" height="313" data-path="images/integrations/zone-ready.png" />
</Frame>

***

### Step 8. Add a New Proxy Password

Navigate to **Access parameters** and click **Add password** to generate a new proxy password.

<Frame caption="Interface showing proxy configuration settings">
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/adding-new-pass.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=3d2d58f8d974e8fbb42949fcf1860ded" alt="adding-new-pass.png" width="500" height="313" data-path="images/integrations/adding-new-pass.png" />
</Frame>

***

### Step 9. Open the Configuration Page

After adding a password, go back to the configuration page to manage IP access.

<Frame>
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/proxy-config.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=d1b4b48e48bd4dd84feb32c717b8f853" alt="proxy-config.png" width="500" height="313" data-path="images/integrations/proxy-config.png" />
</Frame>

***

### Step 10. Review Allocated IPs

Click **Show allocated IPs** to view your assigned IP addresses.

<Frame caption="Settings page showing IP allocation details">
    <img src="https://mintcdn.com/brightdata/klVtuyVQZ5GK3nLT/images/integrations/allocated-ips.png?fit=max&auto=format&n=klVtuyVQZ5GK3nLT&q=85&s=c7336be9db246d38f43e6c204bc61497" alt="allocated-ips.png" width="500" height="313" data-path="images/integrations/allocated-ips.png" />
</Frame>

***

### Step 11. Download the IP List

Download the allocated IPs list for use in SaleFreaks.

<Frame caption="Interface showing IP allocation options and download link">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/download-ips.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=1e15ed848b19421bc4cac5838279bf4e" alt="download-ips.png" width="500" height="313" data-path="images/integrations/download-ips.png" />
</Frame>

<Tip>
  If you added a new password, wait a few minutes before downloading the IP list to allow the password to sync correctly.
</Tip>

***

### Step 12. Open the IP File

Open the downloaded file in a text editor of your choice.

<Frame caption="Text file with proxy IP addresses on screen">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/file-editor.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=788be587b072208fa7ee60e79845a470" alt="file-editor.png" width="500" height="313" data-path="images/integrations/file-editor.png" />
</Frame>

***

### Step 13. Review Required Proxy Fields

Use the following values when configuring SaleFreaks:

* **Proxy Type**: `HTTP`
* **Proxy IP / Host**: `brd.superproxy.io`
* **Proxy Port**: `33335`
* **Proxy Username**:\
  `lum-customer-{your_customer_id}-zone-{your_zone}-ip-{allocated_ip}`
* **Proxy Password**:\
  Your generated proxy password

<Frame caption="Text file screenshot showing proxy server details">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/requried-fileds.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=a5f22761bb5909d88426c5c3adb7c532" alt="requried-fileds.png" width="500" height="313" data-path="images/integrations/requried-fileds.png" />
</Frame>

***

### Step 14. Log In to SaleFreaks

Log in to your SaleFreaks account.\
When prompted to add a marketplace account, choose **Provide my own proxy**.

<Frame caption="Dialog box for adding an eBay account on SaleFreaks">
    <img src="https://mintcdn.com/brightdata/lafG1dG0XmKZiP70/images/integrations/salefreaks-logins.png?fit=max&auto=format&n=lafG1dG0XmKZiP70&q=85&s=2e1867017fc1242e2e3ec90bafc1f6b5" alt="salefreaks-logins.png" width="500" height="313" data-path="images/integrations/salefreaks-logins.png" />
</Frame>

***

### Step 15. Enter Proxy Details in SaleFreaks

Paste the proxy details from the Bright Data IP file into the SaleFreaks proxy fields.

<Frame caption="Form for adding eBay account with proxy settings">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/fill-in-info.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=082fbb1a3c6f3057d2f78c2af5b0b035" alt="fill-in-info.png" width="500" height="313" data-path="images/integrations/fill-in-info.png" />
</Frame>

***

### Step 16. Enable Auto-Recharge (Recommended)

To avoid losing access to allocated IPs, enable **auto-recharge** in your Bright Data billing settings.

<Frame caption="Enable auto recharge confirmation pop-up on billing page">
    <img src="https://mintcdn.com/brightdata/eeH2P1gRKelS4k6h/images/integrations/autorecharge.png?fit=max&auto=format&n=eeH2P1gRKelS4k6h&q=85&s=18d30530b4dd2b3069325fbf3aeac3d4" alt="autorecharge.png" width="500" height="284" data-path="images/integrations/autorecharge.png" />
</Frame>

***

<Warning>
  **Important Note**

  If you are using Bright Data **Residential Proxies**, **Unlocker API**, or **SERP API**, you must install an SSL certificate to enable secure connections.

  Follow the instructions in this guide to complete the setup:\
  [https://docs.brightdata.com/general/account/ssl-certificate#installation-of-the-ssl-certificate](https://docs.brightdata.com/general/account/ssl-certificate#installation-of-the-ssl-certificate)
</Warning>

***

## Best Practices

* Use **one dedicated IP per seller account**
* Avoid reusing IPs across multiple marketplaces
* Monitor SaleFreaks logs for proxy-related errors
* Use ISP or Datacenter proxies for long-term account safety
* Keep auto-recharge enabled to prevent service interruptions

***

## Conclusion

By integrating Bright Data proxies with SaleFreaks, you create a stable and secure automation environment for dropshipping operations. This setup protects seller accounts, enables geo-specific workflows, and ensures reliable performance across sourcing, fulfillment, and inventory management—allowing you to scale your business with confidence.
