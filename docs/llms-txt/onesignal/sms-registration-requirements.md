# Source: https://documentation.onesignal.com/docs/en/sms-registration-requirements.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Toll-free / 10DLC / RCS registration requirements

> Requirements for registering Toll-free, RCS and 10DLC SMS campaigns with Twilio.

To ensure successful approval of your SMS campaigns under Twilio's **A2P 10DLC**, **RCS** or **Toll-Free** messaging systems, it's essential to meet specific compliance requirements. This guide outlines key standards—especially around opt-in forms and privacy policies—to help you get approved faster and avoid rejections.

<Info>
  Please contact `support@onesignal.com` for assistance with short codes or alpha numeric numbers.
</Info>

***

## 1. Compliant opt-in form requirements

Your "opt-in form" specifically refers to how you collect phone numbers from your users. Before submitting your registration, ensure your opt-in form meets the following standards:

1. **Unchecked Opt-In Checkbox**
   * Must be manually checked by users (off by default)

2. **Clear Opt-Out Instructions**
   * Be explicit with your opt-out keywords like: *"Reply STOP to unsubscribe."*

3. **Visible Privacy Policy & Terms Links**
   * These links must be directly accessible from the form

4. **Cost Disclosure**
   * Example: *"Message & data rates may apply."*

5. **Message Frequency Disclosure**
   * Be specific if known (e.g., "1 msg/week") or use: *"Message frequency varies."*

6. **Purpose of Messages (Use Case Disclosure)**

   * Explain what the messages are for. Example standard use cases:

     * **2FA (Two-Factor Authentication):** One-time passwords or login codes
     * **Account Notifications:** Password changes, account alerts, etc.
     * **Customer Care:** Support conversations via SMS
     * **Delivery Notifications:** Shipping and order updates
     * **Fraud Alerts:** Suspicious activity alerts
     * **Higher Education:** Messaging for students, staff, faculty
     * **Marketing:** Promotions and special offers (**requires explicit opt-in**)
     * **Polling and Voting:** Non-political surveys or votes
     * **Public Service Announcements:** Community or emergency updates
     * **Security Alerts:** Breach or issue notifications

### Example opt-in consent language

> \[ ] I agree to receive \[TYPE OF MESSAGES] from \[COMPANY NAME]. Message frequency varies. Message & data rates may apply. Reply STOP to unsubscribe. View our Privacy Policy and Terms of Service.

### Notes on submissions

* If your opt-in form isn't live or ready yet, you may submit a screenshot or mockup as a placeholder.
* If the opt-in occurs behind a login or isn't public, include screenshots to demonstrate the experience.
* Opt-in **must not** be bundled with other terms. Example: You **can not say**: *"By accepting our Terms of Use, you also agree to receive Email updates."* SMS opt-in must be **explicit** and **separate**.

<Info>
  Try this prompt in ChatGPT or your AI tool:

  *"Does my opt-in form meet 10DLC requirements?"*

  Include a screenshot or link to your form.
</Info>

***

## 2. Privacy policy requirements

Your Privacy Policy must be easy to find and contain explicit statements clearly explaining **how mobile numbers are used** and **who they are shared with**.

### Required Clauses

* **How Data is Used**

  * Describe how mobile numbers are used to send SMS alerts

* **Data Sharing Transparency**

  * Must clearly state that phone numbers are not shared with third parties for marketing.
  * Sharing with affiliates/subcontractors for support services is permissible.

* **Opt-Out Instructions**

  * Explain how users can stop receiving messages.
  * Example: *"You may opt out of receiving text messages from us at any time by replying STOP."*

* **Visibility**

  * Link to your Privacy Policy directly from the opt-in form.

### Example Privacy Policy Statement

> *"Your mobile number will only be used for \[specific purpose]. We do not share numbers with third parties for marketing or lead generation. We may share with affiliates or vendors for service-related purposes."*

<Info>
  Try this prompt in ChatGPT or your AI tool:

  *"Review the following privacy policy and provide actionable suggestions on how to make it 10DLC or toll-free compliant."*

  Include a link or copy-paste the content.
</Info>

***

## 3. Prohibited use cases (Will be rejected automatically)

Avoid these restricted content categories, which are never approved:

❌ **High-Risk Financial**

* Payday loans, short-term/high-interest loans
* Auto loans with high APR
* Third-party loan matchmakers

❌ **Debt & Credit**

* Credit repair or "get out of debt" offers
* Debt relief or forgiveness

❌ **Regulated Products**

* Cannabis, CBD, Rx drugs (regardless of state legality)
* Casinos, gambling, betting, sweepstakes, lotteries with cash prizes

❌ **Deceptive Offers**

* "Get rich quick" schemes
* Work-from-home scams
* High-yield investment pitches

❌ **Sensitive or Regulated Content**

* Adult or sexually explicit content
* Hate speech, violence
* Alcohol (without age gate)
* Firearms or weapons

❌ **Spam or Lead Generation**

* Cold outreach
* Messaging users who didn't opt in
* Selling or buying user lists

***

# Final checklist before submitting

* Opt-in form meets all checkbox, disclosure, and link requirements
* Privacy Policy clearly outlines use, sharing, and opt-out
* No restricted content or use cases are involved

<Info>
  If you haven't already, open ChatGPT and try this prompt:

  *"Review my opt-in form and privacy policy. Provide actionable suggestions on how to make it 10DLC or toll-free compliant."*

  Provide screenshots, links, or copy-paste your text into the AI tool to review.
</Info>

<Check>
  Submit your information to us via our [10DLC](https://docs.google.com/forms/d/e/1FAIpQLSe-UhgLfSIJLN_CQhjDDMIVNM5xhcMY4Xu2z7JT7tjFoLiYUA/viewform) or [Toll-free](https://docs.google.com/forms/d/e/1FAIpQLScWbnAOUzS7kJUnYybyt7ZbGSotpK6FNhisRAoNfCi473hYYA/viewform) forms and contact your Account Manager for next steps.
</Check>

***

**General Disclaimer**: The content on this page is for informational purposes only and does not constitute legal advice. We recommend consulting with a legal professional to ensure full compliance with all applicable regulations.

***

Built with [Mintlify](https://mintlify.com).
