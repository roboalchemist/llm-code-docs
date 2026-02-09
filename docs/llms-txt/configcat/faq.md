# Source: https://configcat.com/docs/faq.md

# FAQ - Frequently Asked Questions

Copy page

A collection of frequently asked questions.

## General[​](#general "Direct link to General")

### Learning how ConfigCat can work with your product[​](#learning-how-configcat-can-work-with-your-product "Direct link to Learning how ConfigCat can work with your product")

You can book a free demo session [here](https://calendly.com/configcat/demo), where we'll show you how to use ConfigCat and answer any questions you have.

## Billing, Payments & Subscriptions[​](#billing-payments--subscriptions "Direct link to Billing, Payments & Subscriptions")

### What if I exceed the [config JSON download](https://configcat.com/docs/requests.md) limit of my plan?[​](#what-if-i-exceed-the-config-json-download-limit-of-my-plan "Direct link to what-if-i-exceed-the-config-json-download-limit-of-my-plan")

Don't worry, we will keep serving your data and feature flags. Someone from our team will contact you to discuss your options. You can always check your Usage & Quota [here](https://app.configcat.com/organization/usage).

### Where can I find and download my invoices?[​](#where-can-i-find-and-download-my-invoices "Direct link to Where can I find and download my invoices?")

All the invoices we've issued are available for download from the [Billing & Invoices page](https://app.configcat.com/organization/billing). You need to have the [Billing Manager](https://configcat.com/docs/organization.md#billing-manager-role) role to access the Billing & Invoices page.

### Is it possible to pay via wire transfer?[​](#is-it-possible-to-pay-via-wire-transfer "Direct link to Is it possible to pay via wire transfer?")

Using a credit card via the ConfigCat Dashboard is the preferred way of payment, but a wire transfer is also an option for larger subscription plans. [Contact us](https://configcat.com/support/) directly for more details.

### How do I upgrade / downgrade my billing plan?[​](#how-do-i-upgrade--downgrade-my-billing-plan "Direct link to How do I upgrade / downgrade my billing plan?")

You can change your billing plan on the [Plans](https://app.configcat.com/organization/plans) page. You need to have the [Billing Manager](https://configcat.com/docs/organization.md#billing-manager-role) role to access the Plans page.

### Can I get a discounted rate?[​](#can-i-get-a-discounted-rate "Direct link to Can I get a discounted rate?")

Discounts are available through our partnership program. [Contact us](https://configcat.com/support/) directly for more information.

### Can I change the email address associated with my account?[​](#can-i-change-the-email-address-associated-with-my-account "Direct link to Can I change the email address associated with my account?")

Currently, there's no direct way to change the email address of an account. However, you can:

1. Invite the new email to join your ConfigCat organization; this will create a fresh ConfigCat account.
2. Grant all the necessary permissions to the new account.
3. Proceed with deleting your old account from [here](https://app.configcat.com/my-account).

If you don't have the required permissions, contact your organization admin or a team member who has "Team members and permission groups" permissions.

Please note: Switching emails means you'll lose preferences from your old account, such as permissions, API keys, and Zombie flag settings. Transfer essential settings first.

### How do I change the billing email address where I receive my invoices?[​](#how-do-i-change-the-billing-email-address-where-i-receive-my-invoices "Direct link to How do I change the billing email address where I receive my invoices?")

Go to the [Billing & Invoices page](https://app.configcat.com/organization/billing) and click the `Update billing details` link. You need to have the [Billing Manager](https://configcat.com/docs/organization.md#billing-manager-role) role to access the Billing & Invoices page.

### How do I change my payment method or billing information?[​](#how-do-i-change-my-payment-method-or-billing-information "Direct link to How do I change my payment method or billing information?")

Go to the [Billing & Invoices page.](https://app.configcat.com/organization/billing) and click the `Update billing details` link. You need to have a [Billing Manager](https://configcat.com/docs/organization.md#billing-manager-role) role to access the Billing & Invoices page.

### The ChargeBee payment gets stuck | Throws an error[​](#the-chargebee-payment-gets-stuck--throws-an-error "Direct link to The ChargeBee payment gets stuck | Throws an error")

If you're using Firefox, try switching to a Chromium-based browser that has extensions turned off. If this doesn't work, [contact us](https://configcat.com/support/) for help.

### How do I cancel my account?[​](#how-do-i-cancel-my-account "Direct link to How do I cancel my account?")

Go to the [Plans](https://app.configcat.com/organization/plans) page and click the `Switch Plan` button under the Free plan. You need to have a [Billing Manager](https://configcat.com/docs/organization.md#billing-manager-role) role to access the Plans page.

### How do I change my currency?[​](#how-do-i-change-my-currency "Direct link to How do I change my currency?")

Go to the [Plans](https://app.configcat.com/organization/plans) page and use the currency toggle to switch between USD and EUR. You need to have a [Billing Manager](https://configcat.com/docs/organization.md#billing-manager-role) role to access the Plans page.

## Security[​](#security "Direct link to Security")

### Are you ISO certified?[​](#are-you-iso-certified "Direct link to Are you ISO certified?")

Yes, ConfigCat complies with the ISO/IEC 27001:2022 standard for Information Security Management Systems (ISMS). Click [here](https://configcat.com/iso/) to learn more.

### I'm setting up my firewall, which addresses should I whitelist?[​](#im-setting-up-my-firewall-which-addresses-should-i-whitelist "Direct link to I'm setting up my firewall, which addresses should I whitelist?")

If possible, you can allow the whole "configcat.com" domain. Alternatively, you can manually whitelist the following addresses:

* Global CDN: `https://cdn-global.configcat.com`
* EU CDN: `https://cdn-eu.configcat.com`
* The Public Management API: <https://api.configcat.com>
* The Dashboard URL: <https://app.configcat.com>

### I can't log in to ConfigCat using two-factor authentication (2FA).[​](#i-cant-log-in-to-configcat-using-two-factor-authentication-2fa "Direct link to I can't log in to ConfigCat using two-factor authentication (2FA).")

*Solution 1:* There might be an authenticator app on your phone that you can use to log in to ConfigCat.

*Solution 2:* Use your recovery codes that you received when you first set your 2FA up.

*Solution 3:* Contact your `Organization Admin`, and ask them to disable 2FA for your account until you set it up again. `Organization Admins` can disable 2FA on the [Members & Roles](https://app.configcat.com/organization/members) page. After you re-enable the 2FA, new recovery codes will also be (re)generated. It might be a good idea to save them to avoid such issues in the future.

### The Audit log doesn't show old operations[​](#the-audit-log-doesnt-show-old-operations "Direct link to The Audit log doesn't show old operations")

The Free plan includes a 7-day retention period. The Pro and Smart plans offer a 35-day retention, while the Enterprise and Dedicated plans provide a 2-year retention.

### Is there a way to allow a group access to only one config rather than all of them?[​](#is-there-a-way-to-allow-a-group-access-to-only-one-config-rather-than-all-of-them "Direct link to Is there a way to allow a group access to only one config rather than all of them?")

You can't set config-level access in one product. Instead, split your configs into multiple products with the appropriate permission settings.

### I cannot access my account using Google sign-in.[​](#i-cannot-access-my-account-using-google-sign-in "Direct link to I cannot access my account using Google sign-in.")

Browser extensions may interfere. Please disable all browser extensions and try again.

## Privacy[​](#privacy "Direct link to Privacy")

### How can I be sure that my data is safe?[​](#how-can-i-be-sure-that-my-data-is-safe "Direct link to How can I be sure that my data is safe?")

ConfigCat SDKs evaluate feature flags locally, in your application. They send no user data to the ConfigCat servers.

See our architecture explained [here](https://configcat.com/architecture/).

### Can we sign a data processing agreement with you?[​](#can-we-sign-a-data-processing-agreement-with-you "Direct link to Can we sign a data processing agreement with you?")

Yes. You can review our DPA through our [Trust Center](https://configcat.com/trust-center/) page, or [contact us](https://configcat.com/support/?prefilled=dpa-sign-request) and we'll send it to you for signing.

### Does ConfigCat collect browser data when serving feature flag data download requests?[​](#does-configcat-collect-browser-data-when-serving-feature-flag-data-download-requests "Direct link to Does ConfigCat collect browser data when serving feature flag data download requests?")

No. ConfigCat doesn't collect, store or process any user or browser fingerprinting data.

The data flow is one directional - the SDKs are only downloading the config JSON files and the feature flag evaluation happens in the SDKs.

ConfigCat doesn't collect any information about the customer's users.

### Is data hosted only within the EU?[​](#is-data-hosted-only-within-the-eu "Direct link to Is data hosted only within the EU?")

Our main infrastructure and database is in the EU, but CDN servers are located both in the EU and globally. You can set where you want us to keep your data, so its always within reach for your needs.

You can read more [here](https://configcat.com/docs/advanced/data-governance.md).

### Is it possible to export the feature flags?[​](#is-it-possible-to-export-the-feature-flags "Direct link to Is it possible to export the feature flags?")

Yes! You can export and download your current product as a standard JSON file anytime you want. The export will include:

* All feature flags and settings together with their values, Targeting Rules, Percentage Options, segments, tags
* All configs
* All environments
* All tags
* All segments

### How long does ConfigCat keep my data?[​](#how-long-does-configcat-keep-my-data "Direct link to How long does ConfigCat keep my data?")

We keep organization data as long as we see activity in that organization. After several months of inactivity, we send you a series of email notifications about or plans to delete your organization and all associated data. We consider an organization inactive if it meets all of the following criteria:

* no audit log events are generated in the organization,
* no valid calls are made to the organization via the Public Management API,
* config JSONs aren't downloaded from the ConfigCat CDN,
* the organization does not have an active paid subscription.

## A/B Testing & Targeting[​](#ab-testing--targeting "Direct link to A/B Testing & Targeting")

### Can I use AND operators in my Targeting Rules?[​](#can-i-use-and-operators-in-my-targeting-rules "Direct link to Can I use AND operators in my Targeting Rules?")

Yes, you can use AND operators in your Targeting Rules. (Only available in [Config V2](https://configcat.com/docs/advanced/config-v2.md) and later)

### Are Percentage Options sticky?[​](#are-percentage-options-sticky "Direct link to Are Percentage Options sticky?")

Yes. The percentage-based targeting is sticky by design and consistent across all SDKs.

Also, consider the following:

* All SDKs evaluate the rules in the exact same way. (10% is the same 10% in all SDKs)
* The percentage rules are sticky by feature flag. (10% is a different 10% for each feature flag)

More on [stickiness](https://configcat.com/docs/targeting/percentage-options.md#stickiness) and [consistency](https://configcat.com/docs/targeting/percentage-options.md#consistency)

### How to use Targeting Rules based on sensitive data?[​](#how-to-use-targeting-rules-based-on-sensitive-data "Direct link to How to use Targeting Rules based on sensitive data?")

If you want to use Targeting Rules based on email address, phone number, or other sensitive data, you can use the [Confidential text comparators](https://configcat.com/docs/targeting/targeting-rule/user-condition.md#confidential-text-comparators).

## Technical Debt[​](#technical-debt "Direct link to Technical Debt")

### What are Zombie (Stale) Flags?[​](#what-are-zombie-stale-flags "Direct link to What are Zombie (Stale) Flags?")

![Zombie cat](/docs/assets/faq/zombie.svg)

Zombie (Stale) flags are feature flags that are not changed in the last (configurable) number of days. Most of the time if a feature flag isn't changed for a long time it means it is time to be removed from your source code and from the [ConfigCat Dashboard](https://app.configcat.com/) as well to avoid technical debt.

### What is the Zombie (Stale) Flags Report?[​](#what-is-the-zombie-stale-flags-report "Direct link to What is the Zombie (Stale) Flags Report?")

The [Zombie (Stale) Flags Report](https://app.configcat.com/my-account/zombie-flags-report) is a list of all feature flags that are not changed in the last (configurable) number of days. You can use this report to identify and remove stale feature flags from your source code. This report is weekly emailed to you. You can set your [email preferences here](https://app.configcat.com/my-account/zombie-flags-report).

### I am not getting the Zombie Feature Flag email report. What am I doing wrong?[​](#i-am-not-getting-the-zombie-feature-flag-email-report-what-am-i-doing-wrong "Direct link to I am not getting the Zombie Feature Flag email report. What am I doing wrong?")

You can change the frequency, criteria and scope of the Zombie Feature Flag report on the Dashboard.

**Note:** Please be aware that feature flags are only treated as zombie flags if they haven't been modified (with save & publish) in the past given timeframe. It currently doesn't have any connection with your real usage in your code.

### How to avoid technical debt caused by feature flags?[​](#how-to-avoid-technical-debt-caused-by-feature-flags "Direct link to How to avoid technical debt caused by feature flags?")

The [ConfigCat CLI](https://configcat.com/docs/advanced/code-references/overview.md) can scan your code, upload code references to the [ConfigCat Dashboard](https://app.configcat.com/) and notify you about stale feature flags.

![Code references screenshot](/docs/assets/cli/code-refs.png)

### Is there a way to compare flag statuses between two or more environments?[​](#is-there-a-way-to-compare-flag-statuses-between-two-or-more-environments "Direct link to Is there a way to compare flag statuses between two or more environments?")

Yes, you can see the state of all your Feature Flags across all your environments in our simplified [overview](https://app.configcat.com/overview).

## Joining an Organization[​](#joining-an-organization "Direct link to Joining an Organization")

### Is there an expiration date for sent invitations?[​](#is-there-an-expiration-date-for-sent-invitations "Direct link to Is there an expiration date for sent invitations?")

Invitations are valid for 14 days by default, but you can re-send them anytime to extend their expiration.

### I can't see the organization that I just joined[​](#i-cant-see-the-organization-that-i-just-joined "Direct link to I can't see the organization that I just joined")

If you created a new account before joining an organization via an invite (like the one sent by your company via email), then it is likely that a duplicate organization is created for you by ConfigCat.

Once you find the proper organization where you are supposed to be, we recommend deleting the duplicate from [here](https://app.configcat.com/organization/preferences), but please make sure that you don't accidentally delete the one that you want to keep.

## Technical Ones[​](#technical-ones "Direct link to Technical Ones")

### Is it possible to rename a product or config?[​](#is-it-possible-to-rename-a-product-or-config "Direct link to Is it possible to rename a product or config?")

Yes, you can rename almost everything within ConfigCat. Organizations, products, configs, environments, tags and feature flags can all be renamed. What you can't rename is feature flag keys, as that could cause a tsunami of reference error messages in your applications.

### Can I change my Feature Flag based on a date?[​](#can-i-change-my-feature-flag-based-on-a-date "Direct link to Can I change my Feature Flag based on a date?")

You can pass the current date as a [custom User Object attribute](https://configcat.com/docs/targeting/targeting-rule/user-condition.md#comparison-attribute) to the ConfigCat SDK attribute when evaluating the feature flag, and you can use that attribute with our [Date and Time comparators](https://configcat.com/docs/targeting/targeting-rule/user-condition.md#date-and-time-comparators) in your targeting rules to target specific dates.

### Does ConfigCat guarantee percentage distribution?[​](#does-configcat-guarantee-percentage-distribution "Direct link to Does ConfigCat guarantee percentage distribution?")

ConfigCat guarantees percentage distribution across all SDKs, and it guarantees that each user will receive the same experience every time.

### Is it possible to set up A/B/C test (33%/33%/33%) distribution with ConfigCat?[​](#is-it-possible-to-set-up-abc-test-333333-distribution-with-configcat "Direct link to Is it possible to set up A/B/C test (33%/33%/33%) distribution with ConfigCat?")

Yes, it is possible. All you have to do is to create a text setting and apply the percentage rules. With a normal feature flag you have only two options - true or false, but with a text setting you can apply as many A/B/n options as you want with the percentages.

### Is there a way to create feature flags via the API?[​](#is-there-a-way-to-create-feature-flags-via-the-api "Direct link to Is there a way to create feature flags via the API?")

Yes there is. We have a public management API at <https://api.configcat.com>.

### How to resolve Domain verification issues?[​](#how-to-resolve-domain-verification-issues "Direct link to How to resolve Domain verification issues?")

**Txt record-based verification**

**Solution 1:** Check the 'Host' field in your DNS settings. One common cause of verification failure is an incorrectly set 'Host' field. Make sure that it is set to '@' or left empty. To check this setting, you will need to log into your domain provider's management console.

**Solution 2:** After you've added the TXT record to your DNS settings, it may take some time for the changes to propagate through the DNS system. If you have recently added or updated the TXT record, it's possible that the verification hasn't been completed due to DNS caching. Sometimes you even need to wait a few hours before trying to verify the domain again.

**File-Based verification**

If you're having trouble verifying your domain with the file-based verification method, make sure you've uploaded the file to the proper directory, and you can download it from under your domain.
