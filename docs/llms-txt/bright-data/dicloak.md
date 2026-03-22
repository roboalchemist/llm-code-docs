# Source: https://docs.brightdata.com/integrations/dicloak.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up Bright Data With DICloak

# DICloak Proxy Integration

DICloak is a powerful anti-detect browser designed to provide secure and anonymous internet browsing. It offers dynamic fingerprinting, profile management, and robust proxy support, making it an essential tool for professionals seeking enhanced privacy and data collection capabilities.

## DICloak and Bright Data: A Powerful Integration for Secure Browsing

Integrating DICloak with Bright Data’s proxy solutions creates a robust combination for privacy-focused professionals. Here’s how Bright Data enhances DICloak:

* **Global Proxy Coverage:** Access over 72 million IPs worldwide for seamless region-specific browsing, the largest proxy network in the world.
* **Enhanced Privacy:** Secure and anonymous browsing with reliable proxy support.
* **Geo-Bypassing:** Easily access restricted content for international projects.
* **Optimized Speed:** High-performance proxies ensure fast connections.
* **Versatile Applications:** Suitable for web scraping, account management, and more.

Integrating DICloak with Bright Data's proxy services ensures optimal performance and security for your web scraping and browsing tasks. This article provides a step-by-step guide to integrate Bright Data with DICloak seamlessly.

## How to Integrate Bright Data With DICloak

<Steps>
  <Step title="Download and Install DICloak">
    1. [Download](https://dicloak.com/download) the DICloak browser suitable for your operating system.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/download-dicloak.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=7d9d2143649f4e7701ae67e7807475c4" alt="download-dicloak" width="1880" height="863" data-path="images/integrations/dicloak/download-dicloak.png" />
    </Frame>

    2. Install DICloak and launch the app.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/launch-dicloak.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=f2b2a45ab60d4b11441426cb545b65b8" alt="launch-dicloak" width="1999" height="1250" data-path="images/integrations/dicloak/launch-dicloak.png" />
    </Frame>
  </Step>

  <Step title="Create a New Profile">
    1. Click on the **+ Create Profile** button.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/create-profile.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=b17e256641e5b085a5833475eecc0838" alt="create-profile" width="1785" height="903" data-path="images/integrations/dicloak/create-profile.png" />
    </Frame>

    2. Set up the basic profile:

    * Enter a **Profile Name**.
    * Choose the browser and operating system.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/setup-basic-profile.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=2584fc18709f7bd2503d75a59ae651db" alt="setup-basic-profile" width="1999" height="1250" data-path="images/integrations/dicloak/setup-basic-profile.png" />
    </Frame>
  </Step>

  <Step title="Proxy Configuration in DICloak">
    1. Scroll down to the **Proxy** section and set proxy details:

    * From the **Proxy Type** dropdown, select `HTTP`.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/proxy-config.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=49997175da87d757007435376d97ce00" alt="proxy-config" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-config.png" />
    </Frame>

    2. Enter the following details:

       * **Host:** `brd.superproxy.io`
       * **Port:** `33335`
       * **Account Name:** Enter your Bright Data username.
       * **Password:** Enter your Bright Data password.

       <Tip>
         Learn how to find your Bright Data username and password in [this guide](/integrations/bright-data).
       </Tip>

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/proxy-connection.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=fdc2ac295a8d5ab8976329747094170c" alt="proxy-connection" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-connection.png" />
    </Frame>
  </Step>

  <Step title="Test your Proxy">
    1. Click on the **Check Proxy** button to test the connection.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/check-proxy.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=e5773e6d5ff712050da16d58353cc68d" alt="check-proxy" width="1999" height="1250" data-path="images/integrations/dicloak/check-proxy.png" />
    </Frame>

    2. Ensure the connection test is successful and confirm the settings.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/proxy-test-success.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=48296100d4c975e7cd77b64c9b5bf6eb" alt="proxy-test-success" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-test-success.png" />
    </Frame>
  </Step>

  <Step title="Start Browsing">
    1. To use the proxy, click on the **Open** button.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/open-browser.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=d6b2a4dca745723216fed42fa4dc4125" alt="open-browser" width="1999" height="1250" data-path="images/integrations/dicloak/open-browser.png" />
    </Frame>

    2. A browser will open with your preferred settings and the configured proxy.

    <Frame>
            <img src="https://mintcdn.com/brightdata/Wl7FaVrr89gzDnYW/images/integrations/dicloak/browser-open.png?fit=max&auto=format&n=Wl7FaVrr89gzDnYW&q=85&s=5b8cd7e28652cb0eaaad447559bf063e" alt="browser-open" width="1999" height="1250" data-path="images/integrations/dicloak/browser-open.png" />
    </Frame>
  </Step>
</Steps>

***

## Additional Tips

* **Session Control:** Bright Data allows session customization. Configure session persistence to maintain the same IP or rotate IPs as needed for your tasks.
* **Proxy Pooling:** Utilize Bright Data’s proxy pool for larger data collection projects.
* **DICloak Enhancements:** Leverage DICloak’s unique anti-detect features to mimic human-like browsing behavior.

By following this guide, you can effectively integrate Bright Data with DICloak for secure, efficient, and anonymous browsing and data collection.
