# Source: https://docs.brightdata.com/integrations/ios.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Use Bright Data on iOS

> Learn how to set up Bright Data proxies on your iOS device to enjoy secure, private, and unrestricted browsing. This guide walks you through the complete configuration process for a smooth and reliable connection.

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

## Why Use Bright Data on iOS?

Using Bright Data proxies on your iOS device allows you to:

* **Protect Your Privacy**: Hide your real IP address and browse securely.
* **Access Geo-Restricted Content**: Route traffic through different countries and regions.
* **Improve Connection Reliability**: Reduce detection risks and maintain stable, anonymous connections while browsing, shopping, or managing accounts.

***

## Prerequisites

Before you begin, ensure you have:

* **Bright Data Proxy Credentials**\
  Log in to your [Bright Data dashboard](https://brightdata.com/cp/zones) and note your **Host**, **Port**, **Username**, and **Password**.

* **An iPhone or iPad running iOS 10 or later**\
  The steps below apply to most modern iOS versions.

***

## Configuring a Proxy for a Wi-Fi Network

<Steps>
  <Step title="Open Wi-Fi Settings">
    1. Open **Settings** on your iOS device.
    2. Tap **Wi-Fi**, then select the **ⓘ (Info)** icon next to your connected network.

    <Frame as="div" style={{ width: "50%", height: "auto" }}>
      <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/iphone1.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=7db8a4ce8077adc663be348defc998c4" alt="" width="1170" height="1049" data-path="images/integrations/iphone1.png" />
      <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/iphone2.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=499175c990f30ebdf106654b703d68c8" alt="" width="1170" height="569" data-path="images/integrations/iphone2.png" />
    </Frame>
  </Step>

  <Step title="Change Proxy Settings to Manual">
    1. Scroll down to **HTTP Proxy**.
    2. Switch the setting from **Off** or **Automatic** to **Manual**.
    3. Toggle **Authentication** **On**.

    <Frame as="div" style={{ width: "50%", height: "auto" }}>
      <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/iphone3.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=6a9aa54dd89b464e65f5840928986a44" alt="" width="1170" height="1043" data-path="images/integrations/iphone3.png" />
      <img src="https://mintcdn.com/brightdata/mDnOYJMdf2BWnkdI/images/integrations/iphone4.png?fit=max&auto=format&n=mDnOYJMdf2BWnkdI&q=85&s=c6a304dbfe67723fa78a321736d1b86d" alt="" width="1170" height="1168" data-path="images/integrations/iphone4.png" />
    </Frame>
  </Step>

  <Step title="Enter Bright Data Proxy Credentials">
    Fill in the following details:

    * **Server**: `brd.superproxy.io`
    * **Port**: Use the port provided in your Bright Data dashboard
    * **Username**: Your Bright Data proxy username
    * **Password**: Your Bright Data proxy password

    Ensure all values are correct, then tap **Save** to apply the configuration.
  </Step>

  <Step title="Verify the Connection">
    1. Open **Safari** or any browser on your device.
    2. Visit:

    [http://httpbin.org/ip](http://httpbin.org/ip)

    3. Confirm that the displayed IP matches your Bright Data proxy IP.
  </Step>
</Steps>

***

## Best Practices

* Use **ISP or Datacenter proxies** for better stability on mobile devices
* Avoid switching Wi-Fi networks frequently when using proxies
* Keep your Bright Data credentials secure
* Re-check proxy settings after iOS updates

***

## Conclusion

You have successfully configured **Bright Data on iOS**. Your Wi-Fi traffic is now routed through secure and anonymous proxy connections, enabling private browsing and access to geo-restricted content. Enjoy a safer, more flexible browsing experience with Bright Data wherever you go.
