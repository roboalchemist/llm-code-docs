# Source: https://console.groq.com/docs/billing-faqs

---
description: Frequently asked questions about Groq&#x27;s billing model, progressive billing, spending monitoring, invoices, and common billing issues.
title: Billing FAQs - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Billing FAQs

## [Upgrading to Developer Tier](#upgrading-to-developer-tier)

### [What happens when I upgrade to the Developer tier?](#what-happens-when-i-upgrade-to-the-developer-tier)

When you upgrade, **there's no immediate charge** \- you'll be billed for tokens at month-end or when you reach progressive billing thresholds (see below for details).

To upgrade from the Free tier to the Developer tier, you'll need to provide a valid payment method (credit card, US bank account, or SEPA debit account).

Your upgrade takes effect immediately, but billing only occurs at the end of your monthly billing cycle or when you cross progressive thresholds ($1, $10, $100, $500, $1,000; see below for details).

### [What are the benefits of upgrading?](#what-are-the-benefits-of-upgrading)

The Developer tier is designed for developers and companies who want increased capacity and more features with pay-as-you-go pricing. Immediately after upgrading, you unlock several benefits:

**Core Features:**

* **Higher Token Limits:** Significantly increased rate limits for production workloads
* **Chat Support:** Direct access to our support team via chat
* **[Flex Service Tier](https://console.groq.com/docs/flex-processing):** Flexible processing options for your workloads
* **[Batch Processing](https://console.groq.com/docs/batch):** Submit and process large batches of requests efficiently
* **[Spend Limits](https://console.groq.com/docs/spend-limits):** Set automated spending limits and receive budget alerts

### [Can I downgrade back to the Free tier after I upgrade?](#can-i-downgrade-back-to-the-free-tier-after-i-upgrade)

Yes, you can downgrade to the Free tier at any time from your account Settings under [**Billing**](https://console.groq.com/settings/billing).

> **Note:** When you downgrade, we will issue a final invoice for any outstanding usage that has not yet been billed. You'll need to pay this final invoice before the downgrade is complete.

After downgrading:

* Your account returns to Free tier rate limits and restrictions
* You'll lose access to Developer tier benefits (priority support, unlimited requests, etc.)
* Any usage-based charges stop immediately
* You can upgrade again at any time if you need more capacity

## [Understanding Groq's Billing Model](#understanding-groqs-billing-model)

### [How does Groq's billing cycle work?](#how-does-groqs-billing-cycle-work)

Groq uses a monthly billing cycle, where you receive an invoice in arrears for usage. However, for new users, we also apply progressive billing thresholds to help ease you into pay-as-you-go usage.

### [How does progressive billing work?](#how-does-progressive-billing-work)

When you first start using Groq on the Developer plan, your billing follows a progressive billing model. In this model, an invoice is automatically triggered and payment is deducted when your cumulative usage reaches specific thresholds: $1, $10, $100, $500, and $1,000.

  
**Special billing for customers in India:** Customers with a billing address in India have different progressive billing thresholds. For India customers, the thresholds are only $1, $10, and then $100 recurring. The $500 and $1,000 thresholds do not apply to India customers. Instead, after reaching the initial $1 and $10 thresholds, billing will continue to trigger every time usage reaches another $100 increment.

  
This helps you monitor early usage and ensures you're not surprised by a large first bill. These are one-time thresholds for most customers. Once you cross the $1,000 lifetime usage threshold, only monthly billing continues (this does not apply to India customers who continue with recurring $100 billing).

### [What if I don't reach the next threshold?](#what-if-i-dont-reach-the-next-threshold)

If you don't reach the next threshold, your usage will be billed on your regular end-of-month invoice.

  
**Example:**

* You cross $1 → you're charged immediately.
* You then use $2 more for the entire month (lifetime usage = $3, still below $10).
* That $2 will be invoiced at the end of your monthly billing cycle, not immediately.

This ensures you're not repeatedly charged for small amounts and are charged only when hitting a lifetime cumulative threshold or when your billing period ends.

  
Once your lifetime usage crosses the $1,000 threshold, the progressive thresholds no longer apply. From this point forward, your account is billed solely on a monthly cycle. All future usage is accrued and billed once per month, with payment automatically deducted when the invoice is issued.

### [When is payment withdrawn from my account?](#when-is-payment-withdrawn-from-my-account)

Payment is withdrawn automatically from your connected payment method each time an invoice is issued. This can happen in two cases:

* **Progressive billing phase:** When your usage first crosses the $1, $10, $100, $500, or $1,000 thresholds. For customers in India, payment is withdrawn at $1, $10, and then every $100 thereafter (the $500 and $1,000 thresholds do not apply).
* **Monthly billing phase:** At the end of each monthly billing cycle.

> **Note:** We only bill you once your usage has reached at least $0.50\. If you see a total charge of < $0.50 or you get an invoice for < $0.50, there is no action required on your end.

## [Monitoring Your Spending & Usage](#monitoring-your-spending--usage)

### [How can I view my current usage and spending in real time?](#how-can-i-view-my-current-usage-and-spending-in-real-time)

You can monitor your usage and charges in near real-time directly within your Groq Cloud dashboard. Simply navigate to [**Dashboard** → **Usage**](https://console.groq.com/dashboard/usage)

This dashboard allows you to:

* Track your current usage across models
* Understand how your consumption aligns with pricing per model

### [Can I set spending limits or receive budget alerts?](#can-i-set-spending-limits-or-receive-budget-alerts)

Yes, Groq provides Spend Limits to help you control your API costs. You can set automated spending limits and receive proactive usage alerts as you approach your defined budget thresholds. [**More details here**](https://console.groq.com/docs/spend-limits)

## [Invoices, Billing Info & Credits](#invoices-billing-info--credits)

### [Where can I find my past invoices and payment history?](#where-can-i-find-my-past-invoices-and-payment-history)

You can view and download all your invoices and receipts in the Groq Console:[**Settings** → **Billing** → **Manage Billing**](https://console.groq.com/settings/billing/manage)

### [Can I change my billing info and payment method?](#can-i-change-my-billing-info-and-payment-method)

You can update your billing details anytime from the Groq Console:[**Settings** → **Billing** → **Manage Billing**](https://console.groq.com/settings/billing/manage)

### [What payment methods do you accept?](#what-payment-methods-do-you-accept)

Groq accepts credit cards (Visa, MasterCard, American Express, Discover), United States bank accounts, and SEPA debit accounts as payment methods.

### [Are there promotional credits, or trial offers?](#are-there-promotional-credits-or-trial-offers)

Yes! We occasionally offer promotional credits, such as during hackathons and special events. We encourage you to visit our [**Groq Community**](https://community.groq.com/) page to learn more and stay updated on announcements.

  
If you're building a startup, you may be eligible for the [**Groq for Startups**](https://groq.com/groq-for-startups) program, which unlocks $10,000 in credits to help you scale faster.

## [Common Billing Questions & Troubleshooting](#common-billing-questions--troubleshooting)

### [How are refunds handled, if applicable?](#how-are-refunds-handled-if-applicable)

Refunds are handled on a case-by-case basis. Due to the specific circumstances involved in each situation, we recommend reaching out directly to our customer support team at **[\[email protected\]](/cdn-cgi/l/email-protection#3e4d4b4e4e514c4a7e594c514f105d5153)** for assistance. They will review your case and provide guidance.

### [What if a user believes there's an error in their bill?](#what-if-a-user-believes-theres-an-error-in-their-bill)

Check your console's Usage and Billing tab first. If you still believe there's an issue:

Please contact our customer support team immediately at **[\[email protected\]](/cdn-cgi/l/email-protection#93e0e6e3e3fce1e7d3f4e1fce2bdf0fcfe)**. They will investigate the specific circumstances of your billing dispute and guide you through the resolution process.

### [Under what conditions can my account be suspended due to billing issues?](#under-what-conditions-can-my-account-be-suspended-due-to-billing-issues)

Account suspension or restriction due to billing issues typically occurs when there's a prolonged period of non-payment or consistently failed payment attempts. However, the exact conditions and resolution process are handled on a case-by-case basis. If your account is impacted, or if you have concerns, please reach out to our customer support team directly at **[\[email protected\]](/cdn-cgi/l/email-protection#e695939696899492a681948997c885898b)** for specific guidance regarding your account status.

### [What happens if my payment fails? Why did my payment fail?](#what-happens-if-my-payment-fails-why-did-my-payment-fail)

You may attempt to retry the payment up to two times. Before doing so, we recommend updating your payment method to ensure successful processing. If the issue persists, please contact our support team at [\[email protected\]](/cdn-cgi/l/email-protection#52212722223d20261235203d237c313d3f) for further assistance. Failed payments may result in service suspension. We will email you to remind you of your unpaid invoice.

### [What should I do if my billing question isn't answered in the FAQ?](#what-should-i-do-if-my-billing-question-isnt-answered-in-the-faq)

Feel free to contact **[\[email protected\]](/cdn-cgi/l/email-protection#0a797f7a7a65787e4a6d78657b24696567)**

  
---

  
Need help? Contact our support team at **[\[email protected\]](/cdn-cgi/l/email-protection#4d3e383d3d223f390d2a3f223c632e2220)** with details about your billing questions.