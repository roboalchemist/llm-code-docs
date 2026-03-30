# Source: https://docs.vast.ai/documentation/instances/connect/instance-portal.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Instance Portal

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Vast.ai Instance Portal",
  "description": "Understanding the Vast.ai Instance Portal - a web interface for accessing instances loaded with Vast.ai Docker images, featuring secure Cloudflare tunnels, application management, tunnel configuration, logs viewing, and PORTAL_CONFIG customization.",
  "author": {
    "@type": "Organization",
    "name": "Vast.ai"
  },
  "articleSection": "Instances Documentation",
  "keywords": ["Instance Portal", "Cloudflare tunnels", "web interface", "application access", "configuration", "vast.ai"]
})
}}
/>

## What is the Instance Portal?

The Instance Portal is the first application you will see after clicking the 'Open' button to access an instance that has been loaded with a [Vast.ai Docker image](https://github.com/vast-ai/base-image/). Many of our recommended templates include the Instance Portal.

<Frame caption="Instance card interface shows the open button">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=7cb467e126f32ad43c444158ac07989d" alt="Instance card interface shows the open button" data-og-width="953" width="953" data-og-height="354" height="354" data-path="images/console-templates-instance-portal.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=4cc8bc6e36401701f55ba1777fd3cb0c 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=99b92664c4c8290c92609596d3dcc4d8 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=0fbd4bee39954fce83a86696db9634f2 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=3a3180da81f2deefa823cfc6b19b65b8 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=cee266735b35f64dada7a52a7a4e2f28 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=132709a8bedfbcd95e963bb57c247f81 2500w" />
</Frame>

## Loading Process

Upon opening the Instance Portal you will see a loading indicator for a short time.&#x20;

<Frame caption="Loading Indicator">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-2.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=cd0bb1186ee7794bb0c5954f7da1ec64" alt="Loading Indicator" data-og-width="800" width="800" data-og-height="570" height="570" data-path="images/console-templates-instance-portal-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-2.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=82d98db57d332fa5330a52ef02dce73b 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-2.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f726a81aa99378a37d4af6e5a623ad24 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-2.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=1728e0fdf6a4253cefbabf423a4f3458 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-2.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=459950cfdc1e18502ccbefde36e538f3 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-2.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e454d71dd3bb3940e6695f8d0e594826 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-2.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f8058ca973df1a967082fc22b21b1f96 2500w" />
</Frame>

During this loading phase, a secure Cloudflare tunnel will be created for each of your instance's open ports and the browser will test whether these tunnel links are accessible.

The secure tunnel link will be formatted like this:

[https://four-randomly-selected-words.trycloudflare.com](https://four-randomly-selected-words.trycloudflare.com)

When the secure tunnel for port `1111` becomes accessible, the instance Portal will redirect to this link before revealing the full interface.

If it is taking too long for the tunnels to be ready, you will see the Instance Portal interface revealed at `http://ip_address:port_1111`

If you would like the default application URLs to be **https\://** rather than **http\://** you can add the following environment variable to your [account level environment variables](https://cloud.vast.ai/account/):

<Frame caption="Enable HTTPS Variable">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-3.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=96b23ffcbd961ef44c3a6ce8a93d95f0" alt="Enable HTTPS Variable" data-og-width="1280" width="1280" data-og-height="296" height="296" data-path="images/console-templates-instance-portal-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-3.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=d7112fc8470e70a42c7048388d604704 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-3.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9dd8d15847c80ada98cab8a781a85c11 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-3.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=41e1a8a9294eee2279666e1819965e42 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-3.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f7f64b732a2de16d679a9fa6b9356b11 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-3.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=65fa0aa53c12536fa18efe03ed99c758 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-3.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e91816df735bc82267ccba5574ff8d43 2500w" />
</Frame>

If you set this variable, it is important to add the Vast.ai Jupyter certificate  to your local system to avoid browser warnings.  See [this page](/documentation/instances/jupyter#1SmCz) for more information about installing the certificate.

## Landing Page

The instance Portal has a simple interface to help you access other web applications that may be running in the instance. See the configuration section of this document for further details on application startup.

<Frame caption="Landing Page">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-4.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=6f10480de3430c01d1aa6a9086ee7498" alt="Landing Page" data-og-width="1280" width="1280" data-og-height="621" height="621" data-path="images/console-templates-instance-portal-4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-4.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=cb4ec0fa4630eb433d5120cebc3401fd 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-4.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=3f8bc2c49890ac251216a39ac5129663 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-4.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=041ac9f65a7b7009285c310761a1c407 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-4.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ea8826ae5fb17c1a223f9b5222109e1f 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-4.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=c685d186e36a1983b0177ec135aefffb 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-4.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=6fed7bf60dcc1e5e97511a2d0569e205 2500w" />
</Frame>

The large blue 'Launch Application' buttons will open your running applications in a new browser tab. &#x20;

If a secure tunnel is available, the button will open the 'trycloudflare.com' link.  If a tunnel is not yet available then the button will open the direct IP address link.

In both cases, a secure token is appended to the link to prevent unauthorised access to your applications.

You can also click the 'Advanced Connection Options' link to see all available connection methods.

## Tunnels Page

Use this page to manage existing secure tunnels and add new tunnels to get access to ports that have not directly been opened in the instance

<Frame caption="Tunnels Page">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-5.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=6dab1170d5581a5c86727c0237b05269" alt="Tunnels Page" data-og-width="1280" width="1280" data-og-height="619" height="619" data-path="images/console-templates-instance-portal-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-5.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=b79b4a0bcc915d6acaadf711ec9ee565 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-5.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e3d9ab43b367a2469b005c24000df9fb 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-5.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=cd3bda8319e3d23eb4cf61953f526e14 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-5.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e673a490a1cf735c841bc23835c0c459 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-5.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=8ad316357160fe20ba5aa47e9310608d 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-5.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=0c08a5608535233360dbe3ff980f1fef 2500w" />
</Frame>

Use this interface to create links to applications you have started after configuring your instance. For example:

If you started an instance but later decide that you want to install some new software that listens on port `7860`, it will not be available directly if you did not configure the port when creating or editing the template.

Simply enter `http://localhost:7860` in the top input box and click the blue 'Create New Tunnel' button.  A tunnel will be created for this port. It may take a moment to be available after creation.&#x20;

You can use the 'Manage' buttons to stop existing tunnels or to refresh them if you want a new URL.

If you would like to link your own domain name to the instance then please see 'Named Tunnels' in the configuration section of this document.

## Instance Logs Page

The logs page will show a live stream of entries added to any `.log` files in the `/var/log/portal/` directory.

Use the 'Copy Logs' button to copy the currently displayed logging output to your clipboard.  You can also use the 'Download Logs' button to download a zip file containing all files and directories in the `/var/log/` directory of your instance.

<Frame caption="Instance Portal logs interface">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-6.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=969f9449473336fa10be1581d9611aa6" alt="Logs Page" data-og-width="1280" width="1280" data-og-height="614" height="614" data-path="images/console-templates-instance-portal-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-6.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=87d0493c517d7d7e57eaaa599c26b306 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-6.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=2497d0dfaf2750c66a7652c3ba629ac0 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-6.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9e5ab0fcbd2051d6954f1aa1b3133d51 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-6.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=a81d208c6dd437b914eacf2ec7763acb 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-6.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=11b572d3fd3b8390791ba8db31984840 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-6.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=1d7d097c2277c896ec16b6dea9f2fb8b 2500w" />
</Frame>

## Tools & Help Page

This page links to useful pages in the Vast.ai documentation to help you get the most from your instance.

<Frame caption="Instance Portal tools and help page">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-7.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f1a8b5607e17dfd8beac31fede839221" alt="Instance Portal tools and help page" data-og-width="1280" width="1280" data-og-height="617" height="617" data-path="images/console-templates-instance-portal-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-7.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=4bd169a47e1c38b42eade331db5044b9 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-7.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=77246a11201fe8431d1b967828ad4d88 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-7.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f5e740b54703db18614472d31d0a9bd0 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-7.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=8cfbe55fb68d7d51ab30278b54e180aa 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-7.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=37f519fb5036ec73dc60b7a6856e91da 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-7.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=571dfe29e9df3a190d6c347b9e2827e9 2500w" />
</Frame>

## Configuration

Initial configuration of the Instance Portal is via the `PORTAL_CONFIG` enviroment variable.  The default value looks like this:

```bash Bash theme={null}
localhost:1111:11111:/:Instance Portal|localhost:8080:18080:/:Jupyter|localhost:8080:8080:/terminals/1:Jupyter Terminal|localhost:8384:18384:/:Syncthing|localhost:6006:16006:/:Tensorboard
```

Each application is separated by a pipe (`|`) character, and each application option is separated by a colon (`:`)&#x20;

For each application, we provide the following configuration options

* Interface to bind the application (currently always `localhost`)
* External port to proxy the application. This must have been added to the template. Eg. `-p 1111:1111`)
* Internal port where the running application will be bound
* URL path for links to open (often `/`)
* Application Name

Where the external port and internal port **are not equal**, a reverse proxy (Caddy) will make your application available on the external port.

Where the external port and internal port **are equal** the application will not be proxied to the external port but secure tunnel application links will be created.

### In Place Configuration

On first boot the configuration variable will be processed and is used to create the configuration file `/etc/portal.yaml`

You can edit this file in a running instance to add or remove applications from the interface.

Any applications you have added after the instance has started will not initially be reachable so you will need to reboot the instance.

### Disable Default Applictions

The startup scripts we use for the default applications we provide will read this configuration and will not start if they are not specified in the configuration file.

### Named Tunnels

While the default behavior of the Instance Portal is to create 'quick' tunnels with a randomly assigned subdomain of 'trycloudflare.com', it is also possible to assign a pre-configured subdomain of your own domain name.

To do this you will need a free [Cloudflare Zero Trust](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) account and a domain name linked to that account.

Here's an example of how your tunnel configuration might look in the Cloudflare dashboard:

<img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-8.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=019e511e85452b7b487a567e1a760812" alt="Example named tunnel configuration" data-og-width="1280" width="1280" data-og-height="486" height="486" data-path="images/console-templates-instance-portal-8.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-8.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=3907ef2d71bbc6f03abb0934d3829d90 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-8.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=3bb42307d2051c5a5b21c587c90165ab 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-8.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=5b87589d4fcdf074146b0904fb71acec 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-8.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=8befe20571c1b6080e994458246df4e0 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-8.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ba63a5d456878bac116e949dd3d7b00d 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-instance-portal-8.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e36a48d17fee7afa222b8c44e416c70c 2500w" />

Once you have created your named tunnel, you can link it to your instance by providing the token associated with your tunnel as the value of environment variable `CF_TUNNEL_TOKEN`. You can save this in the 'Environment Variables' section in your [account settings](https://cloud.vast.ai/account/) or directly in the template if you are saving it privately.

If the instance is already running you can provide then token in the `/etc/environment` file and reboot the instance.

Named tunnels are generally more reliable than quick tunnels and will provide consistent URLs you can use to access applications running in an instance.

When named tunnels are configured, the 'Launch Application' button will direct to the named tunnel rather than the quick tunnel.

**Important:&#x20;**&#x55;sing the same tunnel token for multiple running instances is not possible and will cause broken links.  If you need several instances then you will need a separate tunnel token for each of them.
