# Usage and billing

Source: https://semgrep.dev/docs/usage-and-billing

- [](/docs/)- [Support &amp; resources](/docs/trophy-case)- Usage and billing**On this page- [Support](/docs/tags/support)- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)Usage and billing
Learn about usage computation and other aspects of your Semgrep licenses.

note
- This document is for **Semgrep AppSec Platform** users; Semgrep Community Edition (CE) does not have any usage limit. Compare [** Semgrep AppSec Platform and Semgrep CE](/docs/semgrep-pro-vs-oss).

## Usage[​](#usage)
Several Semgrep AppSec Platform products are free under the **Team** tier for **10 monthly contributors**. These products include:

- Semgrep Code
- Semgrep Supply Chain

A **contributor** is someone who has made at least **one** commit to a Semgrep-scanned **private** repository within the last 30 days, starting from the **date of license purchase** if a license was purchased, or the date of account creation, for accounts using Semgrep within usage limits.

Any type of Semgrep AppSec Platform scan counts towards the contributor total. This includes:

- Scanning with Semgrep Code or Supply Chain.
- Full scans on a repository or partial scans on a pull request or merge request.

### Multiple Semgrep organization accounts[​](#multiple-semgrep-organization-accounts)
If your company creates multiple Semgrep organizations, the ten-contributor limit applies across **all** of your organizations. For example, if your company creates three Semgrep organizations, each with the following number of contributors:

- Organization 1 has 8 contributors
- Organization 2 has 9 contributors
- Organization 3 has 10 contributors

Your company has 27 contributors across three organizations, and you are over the 10-contributor limit. You must purchase licenses for 27 contributors.

Small teams and startupsIf you are a small team, such as an **11-person team**, you may be eligible for Semgrep&#x27;s startup pricing, which provides a discounted rate. Fill out the [** Startup pricing](https://semgrep.dev/contact/contact-us-startups) form to apply.

### Usage computation[​](#usage-computation)
Contributors are calculated using `git log` over the **past 30 days** (a rolling interval), not the beginning of each month. The start date is either:

- The date of your license purchase.
- The date of account creation, if you and your team are within usage limits.

**Bots** and similar automations are excluded from this count.

### Exceeding the free usage limit[​](#exceeding-the-free-usage-limit)
Semgrep scans stop when the usage limit is exceeded. Resume scanning through:

- A one-time 30-day free trial that starts automatically when the usage limit is exceeded for the first time.
- Purchasing additional licenses.
- Waiting for the next billing cycle.

If the first scan exceeds the usage limit, Semgrep still completes the first scan and a one-time 30-day free trial automatically starts. After the trial concludes, if scans are attempted on private repositories that exceed the usage limit, scans will not run until additional licenses are purchased.

### Usage limit on public projects[​](#usage-limit-on-public-projects)
Public projects have no limits on contributors.

### Semgrep CLI commands subject to usage limits[​](#semgrep-cli-commands-subject-to-usage-limits)

- The `semgrep scan` command is subject to the usage limit only if the scan is by a logged-in contributor.
- Semgrep computes contributor counts for any logged-in scan command such as `semgrep ci` and `semgrep scan`.

## Determine your plan needs[​](#determine-your-plan-needs)
Within your team or organization, assess the number of **contributors**. Contributors are members of your organization that make commits. That determines the number of **licenses** needed for the plan purchase.

For example, if a project has 4 unique contributors who create commits during the billing period while Semgrep is scanning their repositories, only 4 licenses are required even if the organization has a total of 10 members. Contributors are counted only once even if they commit to many projects within the same organization, so no additional licenses are required.

infoSemgrep provides a special pricing program for small teams and startups. Fill out the [** Startup pricing](https://semgrep.dev/contact/contact-us-startups) form to apply.

All members of the organization, regardless of contributor (license) status, have access to paid features for the chosen tier. This means that project managers and other non-programming roles can still view the Semgrep AppSec Platform dashboard.

### Single-product purchases[​](#single-product-purchases)
You can choose to purchase a single product. Products can also be turned off from the [Settings page](https://semgrep.dev/orgs/-/settings).

### Number of licenses per product[​](#number-of-licenses-per-product)
You must purchase an **equal number of licenses** for each product you intend to use. For example, you cannot purchase 4 licenses of Semgrep Supply Chain and 9 licenses of Semgrep Code.

## Reconciliation of licenses and usage[​](#reconciliation-of-licenses-and-usage)
If your organization exceeds the number of purchased licenses for the period defined in your contract, your organization will be charged based on the number of licenses that exceeded the purchased amount. The additional charge starts the month after the use of licenses exceeds the contracted amount.

Check in with your Semgrep Account Executive every **60 days** if you need more licenses than initially purchased.

### Example of license reconciliation[​](#example-of-license-reconciliation)
On January 21, you purchased annual licenses for 50 developers of Semgrep Supply Chain’s Team tier ($40 per developer per month). The 21 of the month is the start date of the annual contract. In the following month, on February 28, the number of used developer licenses exceeded the original purchased quantity by 20 users. This requires a contract adjustment.

Contract adjustment:

- Since the organization’s use exceeded the amount of purchased licenses on February 28, the future date of March 21 is selected to align with the remaining months in the contract. There are 10 months remaining in the contract.
- The additional amount charged, the add-on cost, is $8,000 ($40 per developer per month x 10 months x 20 users).
- Resulting add-on cost: **$8,000**

## Upgrade your plan[​](#upgrade-your-plan)
To upgrade to the **Team tier** using a credit card:

- Navigate to **Settings** &gt; **Usage &amp; billing**.
- Choose the product you want to upgrade. You can upgrade Semgrep Code, Semgrep Supply Chain, or both. Click **Upgrade**.
- Review the details of your order, and ensure that the number of licenses you&#x27;re purchasing is accurate.
- Provide your payment details, and click **Subscribe**.

To purchase licenses for Semgrep Secrets, or to upgrade to the **Enterprise tier**, please contact [Semgrep Sales](mailto:sales@semgrep.com).

### Billing[​](#billing)
Team tier users who pay through a credit card are charged monthly. Enterprise tier users are charged at an agreed-upon billing cycle. For any concerns such as custom payment methods and billing cycles, send an email to the Semgrep sales team at [billing@semgrep.com](mailto:billing@semgrep.com).

## Modify or cancel your plan[​](#modify-or-cancel-your-plan)
To modify or cancel your plan, send an email to [billing@semgrep.com](mailto:billing@semgrep.com).

## Pay for your plan[​](#pay-for-your-plan)
Pay through the following methods:

Pay using your credit card.The payment will be processed through Stripe. If you need to change the credit card on file, please reach out to [billing@semgrep.com](mailto:billing@semgrep.com), and Semgrep will contact you for your updated credit card information.Pay through a purchase order or invoice.Send an email to [billing@semgrep.com](mailto:billing@semgrep.com).

## See also[​](#see-also)

- [Supported languages](/docs/supported-languages)
- [List of vulnerabilities found and fixed with Semgrep](/docs/trophy-case)
- [Frequently asked questions](/docs/faq/overview)

## Additional resources[​](#additional-resources)

- [Slack on scaling static analysis with Semgrep](https://semgrep.dev/blog/2021/slack-presents-semgrep-at-def-con-appsec-village/)
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Support](/docs/tags/support)- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/usage-and-billing.mdx)Last updated on **Nov 25, 2025**