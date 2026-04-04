# Source: https://render.com/docs/configure-namecheap-dns.md

# Configuring Namecheap DNS


> This guide assumes you've added your domains to the corresponding Render service. If you haven't done this yet, follow the steps to <a href="/docs/custom-domains#adding-a-custom-domain">add custom domains to your service</a>.

To configure Namecheap for custom domains, we need to create A records for root custom domains and CNAME records for non-root domains (`www` or any other subdomains). In this guide, we'll configure Namecheap for `example.com` and `www.example.com`.

> Make sure to remove any existing `AAAA` records for your domains when you update your DNS settings. `AAAA` records map a domain to a corresponding IPv6 record, but Render does not support IPv6 addresses yet. As a result, `AAAA` records can interfere with Render hosting your custom domains.

1. Log into Namecheap. You'll see your custom domain in the dashboard.

   [image: Namecheap dashboard with example.com domain]

2. Click on the *MANAGE* button on the right and select the *Advanced DNS* tab.

3. Remove any existing `A` records for `@` and click on `Add New Record`. Add an `A` record for host `@` pointing to Render's load balancer IP `216.24.57.1`.

   We recommend setting the TTL to 1 minute so we can verify the domain faster.

   [image: Namecheap root]

4. Remove any existing `CNAME` or Redirect records for `www` and click on `Add New Record`. Add a `CNAME` record for host `www` pointing to your Render subdomain which looks like `example.onrender.com`.

   Again, set the TTL to 1 minute.

   [image: Namecheap www]

   The final configuration should look something like this:

   [image: Namecheap Advanced DNS tab with A and CNAME records]

That's it! DNS changes can take a few minutes to propagate, but once they do you should be all set.