# Source: https://docs.trackjs.com/data-management/ad-blockers/

Title: Dealing with Ad Blockers

URL Source: https://docs.trackjs.com/data-management/ad-blockers/

Markdown Content:
Over 25% of internet users run ad blocking software. If you’re serving technical users like we are, it could be as many as 40%. Almost all of the ad blocker software is powered by a handful of “block lists”, which often block monitoring tools like TrackJS due to vague rules and over-zealous contributors.

**TIP**: This might be a problem with your code too! Always be sure to check how your site behaves with ad blocking software. The side effects can be unexpected. [Check out our write-up on avoiding ad blocker errors](https://trackjs.com/blog/avoid-ad-blocker-errors/).

For many TrackJS users, ad blockers are not a problem. The important errors from your site are recorded from the non-blocking clients. However, if you have a tech-heavy audience, you may want to avoid these issues. We have solutions for you!

[Bundling the Agent](https://docs.trackjs.com/data-management/ad-blockers/#bundling-the-agent "Permalink Here")
---------------------------------------------------------------------------------------------------------------

The first, and easiest, thing to try is to [bundle the agent with your code](https://docs.trackjs.com/browser-agent/installation/#bundling-as-a-module). This will fetch our code from your own domain, which makes it much less likely that error requests will be blocked.

We recommend doing this for improved performance as well.

[Domain Forwarding](https://docs.trackjs.com/data-management/ad-blockers/#domain-forwarding "Permalink Here")
-------------------------------------------------------------------------------------------------------------

If you’ve bundled the agent and you’re still having problems with ad blockers rejecting error payloads, you can bypass them by CNAME’ing your domain to our proxy servers.

For example, if you have a website on `example.com`, requests going to `trackjs.com` may get stopped. But by CNAME’ing `errors.example.com` to our servers, everything belongs to your primary domain and nothing will be blocked. Our forwarding servers automatically handle error forwarding and HTTPS termination.

### [Configure Domain Forwarding](https://docs.trackjs.com/data-management/ad-blockers/#configure-domain-forwarding "Permalink Here")

**1. Point Your Domain**

 Use your DNS provider to CNAME the subdomain to `forwarder.trackjs.com`. The exact steps for this vary by provider.

**2. Configure Your Account**

 Set the forwarding domain in [Account Settings](https://my.trackjs.com/Account/organization#domain-forwarding). The forwarding domain can be any subdomain under your site’s domain (eg - errors.your_domain.com). You should see a confirmation that everything is set up and working.

**3. Configure the TrackJS Agent**

 Configure the TrackJS agent to use the new [forwarding domain](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#forwardingdomain). This is done in the agent install block.

[Global](https://docs.trackjs.com/data-management/ad-blockers/)[Module](https://docs.trackjs.com/data-management/ad-blockers/)

<script src="https://errors.your_domain.com/agent/v3/latest/t.js"></script><script> window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", forwardingDomain: "errors.your_domain.com" });</script>'

[Agent domain forwarding configuration](https://docs.trackjs.com/data-management/ad-blockers/#code-agent-domain-forwarding-configuration)

import { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN", forwardingDomain: "errors.your_domain.com"});

[Agent domain forwarding configuration](https://docs.trackjs.com/data-management/ad-blockers/#code-agent-domain-forwarding-configuration)

**4. Verify the Agent Configuration**

 Test it by loading your site and using DevTools to check that the call to _usage_ is successful. Send an error manually by calling `TrackJS.track("testing proxy")` and see the request sent. You should see the error in your account within 30 seconds.

[Self-Hosted Domain Forwarding](https://docs.trackjs.com/data-management/ad-blockers/#self-hosted-domain-forwarding "Permalink Here")
-------------------------------------------------------------------------------------------------------------------------------------

The forwarding server can also be self-hosted if you do not wish to use our hosted forwarding service. This example uses Nginx running on Linux, but any software that can run as a HTTPS reverse proxy will work.

### [Building a Proxy Server with Linux and Nginx](https://docs.trackjs.com/data-management/ad-blockers/#building-a-proxy-server-with-linux-and-nginx "Permalink Here")

This will walk you through creating a simple TrackJS error proxy using Linux and Nginx.

**1. Create a Linux server.**

 If you don’t have your own way of creating servers, we recommend a $10/mo Droplet from [DigitalOcean](https://www.digitalocean.com/). We like Ubuntu linux, and [here’s a tutorial from DigitalOcean to set it up](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04).

**2. Install Nginx.**

 Nginx is a fast webserver, and we use it a lot. [Here’s a tutorial on installing it for Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04).

**3. Point your domain.**

 Add a `A Record` to the DNS for your domain. We recommend using something generic like `errors` rather than `TrackJS`, which might get blocked by name. Point the record at the public IP Address of your server. If everything is working, you should be able to visit _http://errors.your\_domain.com/_ and see the default nginx page.

**4. Secure the server with Let’s Encrypt.**

 The proxy server will need to listen to HTTPS requests, so you’ll need a certificate. If you have a wildcard certificate for your domain already, feel free to use that. Otherwise, [follow this tutorial to install a free certificate](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/) from [Let’s Encrypt](https://letsencrypt.org/) into nginx. Once that’s done, you should be able to visit _http**s**://errors.your\_domain.com/_ and see the default nginx page.

**5. Configure Nginx to proxy to TrackJS.**

 In the previous tutorials, you probably created a server block configuration file for your domain, a file something like `/etc/nginx/sites-available/errors.your_domain.com`. If you stuck with the default server configuration file instead, that’s fine. Modify your server block to contain the following.

server { listen 80 default_server; listen [::]:80 default_server; server_name errors.your_domain.com; location /usage.gif { proxy_set_header Host $host; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-Proto $scheme; proxy_pass "https://usage.trackjs.com/usage.gif"; } location /fault.gif { proxy_set_header Host $host; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-Proto $scheme; proxy_pass "https://usage.trackjs.com/fault.gif"; } location /capture { proxy_set_header X-Forwarded-Host $host; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-Proto $scheme; proxy_pass "https://capture.trackjs.com/capture"; } # SSL configuration injected by Certbot}

[Nginx TrackJS Proxy Configuration](https://docs.trackjs.com/data-management/ad-blockers/#code-nginx-trackjs-proxy-configuration)

Once added and saved, restart nginx `sudo systemctl restart nginx`. If everything works you should be able to visit _https://errors.your\_domain.com/usage.gif_ and get an empty image response.

**6. Configure the TrackJS agent to use the proxy.**

 Now that you have an error proxy server, you need to configure the TrackJS agent to send traffic to it. This is done by setting a few _undocumented_ properties in the install block.

[Global](https://docs.trackjs.com/data-management/ad-blockers/)[Module](https://docs.trackjs.com/data-management/ad-blockers/)

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script><script> window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", forwardingDomain: "errors.your_domain.com" });</script>'

[Agent proxy configuration](https://docs.trackjs.com/data-management/ad-blockers/#code-agent-proxy-configuration)

import { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN", forwardingDomain: "errors.your_domain.com"});

[Agent proxy configuration](https://docs.trackjs.com/data-management/ad-blockers/#code-agent-proxy-configuration)

Test it by loading your site and using DevTools to check that the call to _usage_ is successful. Send an error manually by calling `TrackJS.track("testing proxy")` and see the request sent. You should see the error in your account within 30 seconds.

_Need help?_ Send our engineering team a note at [hello@trackjs.com](mailto:hello@trackjs.com).
