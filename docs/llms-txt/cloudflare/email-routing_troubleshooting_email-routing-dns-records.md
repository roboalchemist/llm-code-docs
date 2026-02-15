# Source: https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-dns-records/index.md

---

title: Troubleshooting misconfigured DNS records · Cloudflare Email Routing docs
description: If there is a problem with your SPF records, refer to
  Troubleshooting SPF records.
lastUpdated: 2025-12-03T22:57:02.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-dns-records/
  md: https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-dns-records/index.md
---

1. In the Cloudflare dashboard, go to the **Email Routing** page.

   [Go to **Email Routing**](https://dash.cloudflare.com/?to=/:account/:zone/email/routing)

2. Go to **Settings**. Email Routing will show you the status of your DNS records, such as `Missing`.

3. Select **Enable Email Routing**.

4. The next page will show you what kind of action is needed. For example, if you are missing DNS records, select **Add records and enable**.

If there is a problem with your SPF records, refer to [Troubleshooting SPF records](https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-spf-records/).

Note

If you are not using Email Routing but notice an Email Routing DNS record in your zone that you cannot delete, you can use the [Disable Email Routing API call](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/delete/). It will remove any unexpected records, such as DKIM TXT records like `cf2024-1._domainkey.<hostname>`.
