# Source: https://documentation.onesignal.com/docs/en/data-questions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data collection & security FAQs

> Learn how OneSignal protects your data, maintains compliance, and supports privacy regulations.

OneSignal is committed to protecting the privacy and security of all data stored on our platform. We maintain rigorous security controls, adhere to leading compliance frameworks, and continuously monitor and improve our systems to ensure your data remains safe.

This page answers common questions about OneSignal’s data handling, security practices, and compliance certifications.

***

## Data Protection & Compliance

### Hide Email Addresses and Phone Numbers

You can prevent user email addresses and phone numbers from appearing in the OneSignal Dashboard or data exports. See [Handling Personal Data](./handling-personal-data#masking-personally-identifiable-information-pii) for setup instructions.

### SOC 2 Type II & ISO Certifications

OneSignal maintains the following independent security certifications:

* [SOC 2 Type II](./soc-2-type-ii)
* [ISO 27001 & ISO 27701](./iso27001)

These audits validate that OneSignal’s internal controls and privacy management systems meet the highest standards for data security and operational integrity.

### HIPAA

OneSignal complies with HIPAA requirements for customers who manage protected health information (PHI).\
Learn more in our [HIPAA documentation](./hipaa).

### GDPR

OneSignal complies with the EU General Data Protection Regulation (GDPR) and helps customers uphold their GDPR responsibilities. Our primary data centers are located in the European Union.\
See [GDPR & Individual Rights](./gdpr-compliance) for details.

### Data Privacy Framework

OneSignal is certified under the **EU–U.S. Data Privacy Framework** for lawful data transfers between the EU and the U.S.

***

## Security Practices

### Independent Assessments & Vulnerability Scans

We conduct an **annual third-party security assessment** and perform **quarterly vulnerability and penetration scans**. All critical and high-severity findings are remediated promptly.

### Workstation Security

All employee workstations include:

* Firewall and endpoint protection
* Full disk encryption
* Automatic patch management

### Incident Response

We maintain a robust **incident response program** to rapidly detect, contain, and remediate security incidents.

### Dedicated Security Organization

OneSignal’s **Security Team** continuously monitors, triages, and responds to security-related events.

### Encryption

All customer data is encrypted using **industry-standard algorithms**, both **in transit** (TLS 1.2+) and **at rest** (AES-256).

### Single Sign-On (SSO)

OneSignal supports **SSO** through WorkOS, enabling integration with major identity providers. See [Single Sign-On](./sso).

### Two-Factor Authentication (2FA)

Organization administrators can enforce **2-Step Authentication (2FA)** for all team members.\
See [2-Step Authentication](./2-step-authentication).

### Personnel Security

All employees undergo background checks and regular **security awareness training**.

***

## Data Governance & Retention

OneSignal acts as a **data processor**, while customers remain the **data controller**.

* **Message data** (sent via API or Journeys): retained for 30 days before deletion.
* **Dashboard messages**: retained until deleted manually.
* **User data**:
  * Retained indefinitely on paid plans until deleted.
  * Retained for 18 months of inactivity on free plans.

### Data Export

OneSignal provides tools to easily export user and message data. See [Exporting Data](./exporting-data).

***

## FAQs

### How can I or my users opt-out of push notifications?

Users can disable push notifications in the device Notifications settings. For web push notifications, see [Unsubscribe from Notifications](./browser-behavior-and-unsubscribes). For more details, see [Subscriptions](./subscriptions).

### What data is collected by the OneSignal SDK?

See [Data Collected by the OneSignal SDK](./data-collected-by-the-onesignal-sdk).

### Does OneSignal use cookies?

OneSignal’s Web SDK does **not** use cookies. It uses **Local Storage** and **IndexedDB** for storing client data.

You may see a Cloudflare cookie named `__cf_bm`. This cookie is:

* Set by Cloudflare (not OneSignal)
* Used to protect against bots
* Classified as a *Strictly Necessary* cookie that does not require consent under the EU Cookie Law

For more details, see Cloudflare’s [cookie policy](https://www.cloudflare.com/en-gb/cookie-policy/) and [GDPR explainer](https://gdpr.eu/cookies/).

### How should I handle user data in OneSignal?

Follow our best practices in [Handling Personal Data](./handling-personal-data).

### Is OneSignal COPPA Compliant?

OneSignal is certified under the **Families Ads Program** (as of January 10, 2022).

While COPPA compliance is the publisher’s responsibility, OneSignal provides tools to help you collect user consent before data collection or push prompts. See [Getting User Consent](./handling-personal-data#collecting-and-enforcing-user-consent) and [this COPPA guide](https://www.superawesome.com/blog/how-to-implement-coppa-compliant-push-notifications-in-kid-directed-apps/).

### How Can I Secure My OneSignal Account?

Follow these security best practices:

1. Enable [2-Step Authentication](./2-step-authentication) and/or [Single Sign-On](./sso).
2. Remove unnecessary [Team Members](./manage-team-members).
3. Avoid shared logins; each person should have their own OneSignal account.
4. Regularly rotate or delete API keys. See [Keys & IDs](./keys-and-ids).
5. Reset your password as needed. See [Account Management](./apps-organizations).

<Warning>
  Never expose your REST API Keys or App Keys in public repositories or client-side code.
</Warning>

### What are the password rules and policies?

* Passwords need to have 8 characters minimum and cannot appear in a database of exposed passwords.
* There are no predefined expiration or rotation policies for passwords.

### What if my REST API key is compromised?

Immediately **delete and rotate** your API key. See [Keys & IDs](./keys-and-ids) for instructions.

### What if My App ID Is Exposed?

Your App ID is **public** and safe to share—it can only be used to create new user records. However, users cannot receive messages unless they’ve subscribed through valid means. For added protection, enable [Identity Verification](./identity-verification).

### What if a Subscription ID Is Exposed?

A user’s own `subscription_id` is safe to expose to that user—it can only modify their own data. However, **never share other users’ subscription IDs**, as these can be used to send notifications to specific devices. To prevent impersonation, use [Identity Verification](./identity-verification).

***

Built with [Mintlify](https://mintlify.com).
