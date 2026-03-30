# Source: https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-spf-records/index.md

---

title: Troubleshooting SPF records · Cloudflare Email Routing docs
description: "Having multiple sender policy framework (SPF) records on your
  account is not allowed, and will prevent Email Routing from working properly.
  If your account has multiple SPF records, follow these steps to solve the
  issue:"
lastUpdated: 2025-12-03T22:57:02.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-spf-records/
  md: https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-spf-records/index.md
---

Having multiple [sender policy framework (SPF) records](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/) on your account is not allowed, and will prevent Email Routing from working properly. If your account has multiple SPF records, follow these steps to solve the issue:

1. In the Cloudflare dashboard, go to the **Email Routing** page. Email Routing will warn you that you have multiple SPF records.

   [Go to **Email Routing**](https://dash.cloudflare.com/?to=/:account/:zone/email/routing)

2. Under **View DNS records**, select **Fix records**.

3. Delete the incorrect SPF record.

You should now have your SPF records correctly configured. If you are unsure of which SPF record to delete:

1. In the Cloudflare dashboard, go to the **Email Routing** page. Email Routing will warn you that you have multiple SPF records.

   [Go to **Email Routing**](https://dash.cloudflare.com/?to=/:account/:zone/email/routing)

2. Under **View DNS records**, select **Fix records**.

3. Delete all SPF records.

4. Select **Add records and enable**.
