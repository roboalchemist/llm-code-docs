# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/phishing-reporter-page-view-failure-due-to-deprecated-exchange-online-tokens.md

# Phishing Reporter Page View Failure Due to Deprecated Exchange Online Tokens

The **Phishing** **Reporter** **Page** **View** feature fails due to Microsoft's deprecation of legacy Exchange Online tokens earlier than expected date, June 2025.

## **Affected Systems**

* **Microsoft** **365** **users** utilizing the **Phishing** **Reporter** **Page** **View** feature.

## **Symptoms**

If you are using the **Phishing** **Reporter** **Page** **View** version, it may fail with the following empty message:

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F3Z3dMtVRlQN8ohMSdkdC%2FScreenshot%202025-03-26%20at%2016.48.23.png?alt=media&#x26;token=2f3f28fd-dac8-4776-abbb-dccbec1ed181" alt="Empty message shown when Phishing Reporter Page View fails due to deprecated Exchange Online tokens." width="320"><figcaption><p>Empty message shown when Phishing Reporter Page View fails due to deprecated Exchange Online tokens.</p></figcaption></figure>

## **Root Cause**

**Microsoft** has deprecated legacy **Exchange** **Online** **tokens**, which the **Phishing** **Reporter** previously relied upon for **authentication** **and** **access**.

## Short Term Solution

Admins can re-enable legacy Exchange Online tokens for their tenant by using **Exchange Online PowerShell** and the **Set-AuthenticationPolicy** command. For the deprecation timeline, token behavior, and migration guidance (NAA/MSAL), see Microsoft's [Nested app authentication FAQ - Legacy tokens](https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/faq-nested-app-auth-outlook-legacy-tokens).

**See also:** [Regarding deprecation of exchange tokens](https://learn.microsoft.com/en-us/answers/questions/4756209/regarding-deprecation-of-exchange-tokens) (Microsoft Q\&A) for community discussion and admin re-enable options.

{% hint style="warning" %}
It can take up to 24 hours before all requests from Outlook add-ins for legacy tokens are allowed.
{% endhint %}

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FlNIIMftCEoC9dUvyrgYd%2FScreenshot%202025-03-26%20153928.png?alt=media&#x26;token=167d0701-337b-42c8-a8ae-ab73104e4ed6" alt="Exchange Online PowerShell — Allow Legacy Token sample."><figcaption><p>Picture 1: Exchange Online Powershell - Allow Legacy Token Sample</p></figcaption></figure>

## Long-Term Solution

A more permanent solution, we highly recommend using **Microsoft** **Ribbon** **Phishing** **Reporter** that utilises **Graph** **API** and no dependency on Exchange Online tokens.

## FAQ:

### Q: Why is it happening now?

A: Legacy tokens turned off for all tenants before the scheduled date before June.

<table><thead><tr><th width="111.53125">Date</th><th>Legacy tokens status</th></tr></thead><tbody><tr><td>Feb 17th, 2025</td><td>Legacy tokens turned off for all tenants. Admins can reenable legacy tokens via PowerShell.</td></tr><tr><td>Jun 2025</td><td>Legacy tokens turned off for all tenants. Admins can no longer reenable legacy tokens via PowerShell and must contact Microsoft for any exception.</td></tr><tr><td>Oct 2025</td><td>Legacy tokens turned off for all tenants. Exceptions are no longer allowed.</td></tr></tbody></table>

<https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/faq-nested-app-auth-outlook-legacy-tokens>
