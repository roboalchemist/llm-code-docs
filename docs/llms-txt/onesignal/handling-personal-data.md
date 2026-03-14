# Source: https://documentation.onesignal.com/docs/en/handling-personal-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Handling personal data

> How OneSignal handles personal data and how you can meet GDPR, CCPA, and privacy requirements.

## Overview

OneSignal is designed to help you meet global privacy and data protection requirements, including GDPR and CCPA, across all plans, including Free.

This guide explains:

* What data OneSignal collects
* How to minimize or avoid sending personal data
* How to collect and enforce user consent
* How to mask, restrict, or delete data when required

If you require a Data Processing Addendum (DPA) or Standard Contractual Clauses, see our [Paid Plans](https://onesignal.com/pricing) for details.

***

## How OneSignal collects data

The OneSignal SDK begins collecting data after it is initialized in your app or website. For a full list of fields collected automatically by the SDK, see [Data Collected by the OneSignal SDK](./data-collected-by-the-onesignal-sdk).

Most collected data is not considered PII (Personally Identifiable Information). However, some fields may be considered personal data depending on your region or use case. This guide focuses on how to use OneSignal without sending personal user data, or how to control it when required.

### IP address collection

In some regions, including the EU and UK, IP addresses may be considered personal data.

* **Default behavior:** OneSignal will automatically not collect IP Addresses from Users within the EU and UK.
* **Optional:** Disable IP collection globally
  * If you want to prevent IP address storage for all users, including non-EU/UK users, contact `support@onesignal.com`

<Warning> Disabling IP collection is permanent per app and cannot be selectively re-enabled later. </Warning>

### Masking personally identifiable information (PII)

<Frame caption="PII masked in the OneSignal dashboard">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/ab65582ecd658a3b1eb5aa46422d3c66d929ce021c8fc0bbd67a53ac115dc3ce-PII_masking.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=4d5615414c234f1619e1688f09fdcd6a" alt="Emails and phone numbers masked in the OneSignal dashboard" width="1600" height="255" data-path="images/docs/ab65582ecd658a3b1eb5aa46422d3c66d929ce021c8fc0bbd67a53ac115dc3ce-PII_masking.png" />
</Frame>

PII masking helps protect user privacy while allowing teams to safely view and analyze data.

**What gets masked**

* Email addresses
* Phone numbers

Masking applies to:

* The OneSignal dashboard
* Data exported directly from the dashboard

**What is not masked**

PII masking does not currently apply to:

* REST API responses
* External IDs
* Data tags

**Availability**

PII masking is available to:

* Enterprise plans
* Professional or Growth plans with the Security & Legal package

To enable PII masking, contact `support@onesignal.com` or your Account Manager.

<Note> PII masking is a **display-level control**. The underlying data is still stored securely by OneSignal. </Note>

### Personal information sent as tags or other fields

You are responsible for ensuring that you have appropriate consent for any data you send to OneSignal, including:

* Email addresses
* Phone numbers
* Names
* Any personal attributes

For example, if you send an email address as a tag, you must ensure the user has consented to that data being shared and processed.

<Note>
  Some fields are collected automatically by the SDK. You can selectively disable or override many of these fields using SDK configuration options.

  See [Data Collected by the OneSignal SDK](./data-collected-by-the-onesignal-sdk).
</Note>

### Collecting and enforcing user consent

To support GDPR and similar regulations, OneSignal provides consent gating methods that allow you to delay all data collection until the user explicitly agrees.

**Consent vs. Message Opt-in**

* Consent refers to a User-level permission that allows you to delay all data collection until the user explicitly agrees.
* Message opt-in or permission is a Subscription-level permission granted by the user to receive messages for a specific message channel.
  * [Prompt for Push Permissions](./prompt-for-push-permissions)
  * [Email opt-in best practices](./email-reputation-best-practices)
  * [SMS opt-in requirements](./sms-registration-requirements)

**How consent gating works**

* You enable consent requirements before initializing our SDK.
* Our SDK does not collect or send any data until consent is granted via our SDK consent methods.
* Any SDK methods calls made before consent is granted are safely ignored.
* Consent state is persisted across sessions. You only need to collect consent once per user.

<Warning>
  If a user has previously accepted push permissions and has since revoked consent, they can still receive push notifications. To prevent them from receiving push notifications, you can programmatically call our SDK `optOut` method *before* revoking consent, or the user can either:

* Disable push permissions in their devices notification settings
* Uninstall the app
</Warning>

**SDK references**

<Note>
  If the user has accepted push permissions previously and has since revoked consent, you can still send push notifications to them as long as they have not unsubscribed from your notifications entirely. To fully opt a user out of receiving notifications you would use optOut() method for [mobile SDKs](./mobile-sdk-reference#optout-%2C-optin-%2C-optedin) or [web](./web-sdk-reference#optout-%2C-optin-%2C-optedin), before revoking consent.
</Note>

<Columns cols={2}>
  <Card title="Mobile SDKs" href="./mobile-sdk-reference#privacy">
    <Icon icon="mobile" /> More details on the mobile SDK privacy methods.
  </Card>

  <Card title="Web SDKs" href="./web-sdk-reference#privacy">
    <Icon icon="computer" /> More details on the web SDK privacy methods.
  </Card>
</Columns>

### Location sharing

OneSignal provides a method to disable Location sharing within each mobile SDK.

<Columns cols={2}>
  <Card title="Mobile SDKs" href="./mobile-sdk-reference#location">
    <Icon icon="location-pin" /> More details on the mobile SDK location methods.
  </Card>

  <Card title="Web SDKs">
    <Icon icon="check" /> Our web SDK does not collect or send location data.
  </Card>
</Columns>

### Push tokens

Push tokens are generally not considered PII because:

* They cannot be reused outside the originating app
* They do not reveal user identity or personal attributes

However, you should still disclose in your privacy policy that you use a third-party service (like OneSignal) to deliver personalized or targeted notifications.

***

## Deleting data

OneSignal provides multiple ways to delete or retain data depending on the data type.

* **User data**: See the [Delete Users](./delete-users) guide for deleting user profiles, Subscriptions, and associated data.
* **Message data**: Messages sent from the dashboard are stored indefinitely unless deleted manually or the app is deleted.
  * Messages sent via the API are typically deleted **\~30 days** after delivery.
* **Other data**: Most remaining data is stored until your OneSignal app is deleted. See [Managing your OneSignal account](./apps-organizations) for details.

***

Built with [Mintlify](https://mintlify.com).
