# Source: https://console.groq.com/docs/spend-limits

---
description: Control your API costs with automated spending limits and proactive usage alerts. Set monthly budgets, configure alert thresholds, and prevent unexpected charges with organization-wide spending controls.
title: Spend Limits - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Spend Limits

Control your API costs with automated spending limits and proactive usage alerts when approaching budget thresholds.

## [Quick Start](#quick-start)

**Set a spending limit in 3 steps:**

1. Go to [**Settings** → **Billing** → **Limits**](https://console.groq.com/settings/billing/limits)
2. Click **Add Limit** and enter your monthly budget in USD
3. Add alert thresholds at 50%, 75%, and 90% of your limit
4. Click **Save** to activate the limit

**Requirements:** Paid tier account with organization owner permissions.

## [How It Works](#how-it-works)

Spend limits automatically protect your budget by blocking API access when you reach your monthly cap. The limit applies organization-wide across all API keys, so usage from any team member or application counts toward the same shared limit. If you hit your set limit, API calls from any key in your organization will return a 400 with code `blocked_api_access`. Usage alerts notify you via email before you hit the limit, giving you time to adjust usage or increase your budget.

  
This feature offers:

* **Near real-time tracking:** Your current spend updates every 10-15 minutes
* **Automatic monthly reset:** Limits reset at the beginning of each billing cycle (1st of the month)
* **Immediate blocking:** API access is blocked when a spend update detects you've hit your limit
  
> ⚠️ **Important:** There's a 10-15 minute delay in spend tracking. This means you might exceed your limit by a small amount during high usage periods.

## [Setting Up Spending Limits](#setting-up-spending-limits)

### [Create a Spending Limit](#create-a-spending-limit)

Navigate to [**Settings** → **Billing** → **Limits**](https://console.groq.com/settings/billing/limits) and click **Add Limit**.

Example Monthly Spending Limit: $500

Your API requests will be blocked when you reach $500 in monthly usage. The limit resets automatically on the 1st of each month.

### [Add Usage Alerts](#add-usage-alerts)

Set up email notifications before you hit your limit: Alert at $250 (50% of limit) Alert at $375 (75% of limit) Alert at $450 (90% of limit)

**To add an alert:**

1. Click **Add Alert** in the Usage Alerts section
2. Enter the USD amount trigger
3. Click **Save**

Alerts appear as visual markers on your spending progress bar on Groq Console Limits page under Billing.

### [Manage Your Alerts](#manage-your-alerts)

* **Edit Limit:** Click the pencil icon next to any alert
* **Delete:** Click the trash icon to remove an alert
* **Multiple alerts:** Add as many thresholds as needed

## [Email Notifications](#email-notifications)

All spending alerts and limit notifications are sent from **[\[email protected\]](/cdn-cgi/l/email-protection#e3909693938c9197a384918c92cd808c8e)** to your billing email addresses.

**Update billing emails:**

1. Go to [**Settings** → **Billing** → **Manage**](https://console.groq.com/settings/billing)
2. Add or update email addresses
3. Return to the Limits page to confirm the changes

**Pro tip:** Add multiple team members to billing emails so important notifications don't get missed.

## [Best Practices](#best-practices)

### [Setting Effective Limits](#setting-effective-limits)

* **Start conservative:** Set your first limit 20-30% above your expected monthly usage to account for variability.
* **Monitor patterns:** Review your usage for 2-3 months, then adjust limits based on actual consumption patterns.
* **Leave buffer room:** Don't set limits exactly at your expected usage—unexpected spikes can block critical API access.
* **Use multiple thresholds:** Set alerts at 50%, 75%, and 90% of your limit to get progressive warnings.

## [Troubleshooting](#troubleshooting)

### [Can't Access the Limits Page?](#cant-access-the-limits-page)

* **Check your account tier:** Spending limits are only available on paid plans, not free tier accounts.
* **Verify permissions:** You need organization owner permissions to manage spending limits.
* **Feature availability:** Contact us via [\[email protected\]](/cdn-cgi/l/email-protection#62111712120d10162205100d134c010d0f) if you're on a paid tier but don't see the spending limits feature.

### [Not Receiving Alert Emails?](#not-receiving-alert-emails)

* **Verify email addresses:** Check that your billing emails are correct in [**Settings** → **Billing** → **Manage**](https://console.groq.com/settings/billing).
* **Check spam folders:** Billing alerts might be filtered by your email provider.
* **Test notifications:** Set a low-dollar test alert to verify email delivery is working.

### [API Access Blocked?](#api-access-blocked)

* **Check your spending status:** The [limits page](https://console.groq.com/settings/billing/limits) shows your current spend against your limit.
* **Increase your limit:** You can raise your spending limit at any time to restore immediate access if you've hit your spend limit. You can also remove it to unblock your API access immediately.
* **Wait for reset:** If you've hit your limit, API access will restore on the 1st of the next month.

## [FAQ](#faq)

**Q: Can I set different limits for different API endpoints or API keys?**

A: No, spending limits are organization-wide and apply to your total monthly usage across all API endpoints and all API keys in your organization. All team members and applications using your organization's API keys share the same spending limit.   

**Q: What happens to in-flight requests when I hit my limit?**

A: In-flight requests complete normally, but new requests are blocked immediately.   

**Q: Can I set weekly or daily spending limits?**

A: Currently, only monthly limits are supported. Limits reset on the 1st of each month.   

**Q: How accurate is the spending tracking?**

A: Spending is tracked in near real-time with a 10-15 minute delay. The delay prevents brief usage spikes from prematurely triggering limits.   

**Q: Can I temporarily disable my spending limit?**

A: Yes, you can edit or remove your spending limit at any time from the limits page.   

---

  
Need help? Contact our support team at [\[email protected\]](/cdn-cgi/l/email-protection#04777174746b76704463766b752a676b69) with details about your configuration and any error messages.