# Source: https://gitbook.com/docs/help-center/published-documentation/custom-domains/my-custom-subdomain-isnt-working.md

# My custom subdomain isn't working

Custom domain issues are usually DNS-related. Here's how to troubleshoot:

### Check your DNS configuration:

1. Verify you created a **CNAME record** (not an A record) pointing to the value GitBook provided.&#x20;
2. Ensure you're using the subdomain format (`docs.yoursite.com` or `www.yoursite.com`
3. If using Cloudflare, **disable the orange cloud (proxy)** - it must be set to "DNS only"

#### Common DNS issues:

* **Conflicting records**: Remove any existing A, AAAA, or other records for the same subdomain
* **TTL delays**: DNS changes can take up to 48 hours to propagate globally
* <mark style="background-color:$warning;">CAA records: If you have CAA records, add</mark> <mark style="background-color:$warning;"></mark><mark style="background-color:$warning;">`0 issue "pki.goog"`</mark> <mark style="background-color:$warning;"></mark><mark style="background-color:$warning;">to allow GitBook's SSL certificate</mark><mark style="color:$warning;">s</mark>

### **How to test your setup?**

&#x20;Use a DNS lookup tool like [WhatsMyDNS.net](https://www.whatsmydns.net/#CNAME) to verify your CNAME record is pointing to the correct GitBook address.

If you continue having issues after 48 hours, [contact support](https://www.gitbook.com/contact) with your domain name and the CNAME value GitBook provided.
