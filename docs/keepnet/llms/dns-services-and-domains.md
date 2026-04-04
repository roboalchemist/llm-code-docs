# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/settings/dns-services-and-domains.md

# DNS Services and Domains

This page explains the capabilities available to create and use **Domains** and **DNS Services** in the [phishing simulator.](https://keepnetlabs.com/products/phishing-simulator) You can integrate your DNS service provider if the platform supports it already and then you will be able to create phishing domains on the platform to use them in the phishing campaigns.

The platform supports Cloudflare as a DNS provider by default. Cloudflare provides instant subdomains for the main domains and it is easy to manage phishing domains and subdomains with Cloudflare and also able to use on-the-fly free SSL certificates.

## Domains

Previously created domains are listed in the **Phishing Simulator > Settings > Domains** menu on the left sidebar of the platform The table below provides details of the content on this page.

<table><thead><tr><th width="150"></th><th width="581.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Domain</td><td>The name of the domain</td><td></td></tr><tr><td>DNS Name</td><td>The name of the integrated DNS service</td><td></td></tr><tr><td>DNS Record</td><td>The destination IP address or hostname information of the domain</td><td></td></tr><tr><td>Created By</td><td><p>Indication that the domain definition was created by the platform (system) or the company (custom).</p><p><strong>System</strong> type domains on the platform cannot be edited or deleted.</p></td><td></td></tr><tr><td>Status</td><td>The system checks if there is an access problem on the domain every 24 hours.</td><td></td></tr><tr><td>Date Created</td><td>The date and time that the domain address was created</td><td></td></tr><tr><td>Action</td><td><strong>Edit</strong> the details of the selected domain or <strong>Delete</strong> the selected domain.</td><td></td></tr></tbody></table>

## DNS Services

Previously created DNS Services are displayed in the **Phishing Simulator > Settings > DNS Services** menu on the left sidebar of the platform. The table below provides details of the content on this page.

{% hint style="warning" %}
The system supports Cloudflare for the customers to manage phishing domains and add/use them on the platform. These steps are only available to customers who can use Cloudflare for phishing domains.
{% endhint %}

<table><thead><tr><th width="156.20164126611957"></th><th width="581.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>DNS Name</td><td>The name of the DNS service</td><td></td></tr><tr><td>Service Type</td><td>A list of integrated DNS services that are ready to use</td><td></td></tr><tr><td>Status</td><td>The system checks if there is an access problem on the domain service every 24 hours.</td><td></td></tr><tr><td>Created By</td><td><p>Indication that the domain service definition was created by the platform (system) or the company (custom)</p><p><strong>System</strong> type domains on the platform cannot be edited or deleted.</p></td><td></td></tr><tr><td>Date Created</td><td>The date and time that the DNS service was created</td><td></td></tr><tr><td>Action</td><td><strong>Edit</strong> the details of the selected DNS service or <strong>Delete</strong> the selected DNS service.</td><td></td></tr></tbody></table>

## Create a New DNS Service

From the left sidebar menu of the platform, go to **Phishing Simulator > Settings > DNS Services** and click on the **“+ NEW”** button. You will be asked to complete some mandatory fields to integrate a new DNS service.

<table><thead><tr><th width="156.20164126611957"></th><th width="581.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>DNS Name</td><td>The name of the created DNS service</td><td></td></tr><tr><td>Service Type</td><td>A list of integrated DNS Services that are ready to use</td><td></td></tr><tr><td>Email Address</td><td>The e-mail address registered with your DNS service provider</td><td></td></tr><tr><td>API Key</td><td>The API key provided by your DNS service provider</td><td></td></tr><tr><td>Make Available for</td><td><p>Select companies or company groups with which you wish to share the DNS service</p><p>This option is only available to <strong>Reseller</strong> users</p></td><td></td></tr><tr><td>Test Connection</td><td>Check the settings of the DNS service</td><td></td></tr></tbody></table>

## Create a New Domain

From the left sidebar menu of the platform, go to **Phishing Simulator > Settings > Domains** and click on the **“+ NEW”** button. You will be asked to complete some mandatory fields to create a new domain to be used in phishing campaigns.

<table><thead><tr><th width="156.20164126611957"></th><th width="581.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Domain</td><td>The domain address (e.g example.com).</td><td></td></tr><tr><td>DNS Service</td><td>Select the DNS service that is already integrated on the platform.</td><td></td></tr><tr><td>Customize DNS Record</td><td><p>Choose the DNS record type.</p><ul><li>Record type "A" requires that you enter IP address information.</li><li>Record type "CNAME" requires that you enter hostname information.</li></ul><p>The Support Team can provide CNAME or A record information after requested via ticket.</p></td><td></td></tr><tr><td>Proxy Status</td><td><ul><li><strong>Proxied</strong> <strong>=</strong> Traffic between the user and the DNS service provider is provided through a reverse-proxy server. The traffic between the user and DNS is encrypted and the real IP address of the server is masked.</li><li><strong>DNS</strong> <strong>Only</strong> <strong>=</strong> The traffic between the user and the DNS service provider is provided directly. The company is responsible for encrypting the traffic and the real server's IP address is not masked.</li></ul><p>If the <strong>DNS</strong> <strong>Only</strong> status is enabled, the <strong>Schema</strong> option is not available.</p></td><td></td></tr><tr><td>Schema</td><td>Select the HTTP, HTTPS, or use of both protocols for the domain address.</td><td></td></tr><tr><td>Zone ID</td><td>Enter the unique Zone ID provided by Cloudflare. The information is at the bottom of the Dashboard page in Cloudflare.</td><td></td></tr><tr><td>Make Available for</td><td><p>Select which companies or company groups with whom you wish to share the DNS service.</p><p>This option is only available to <strong>Reseller</strong> users.</p></td><td></td></tr><tr><td>Test Connection</td><td>Check the settings of the domain</td><td></td></tr></tbody></table>

## **FAQ**

### Q: Can I use a DNS service other than Cloudflare?

A: Integration is only possible with the DNS services listed on the platform.

### Q: Can I use SSL certificate domains in phishing scenarios?

A: The platform offers this feature If you use a Cloudflare domain address.
