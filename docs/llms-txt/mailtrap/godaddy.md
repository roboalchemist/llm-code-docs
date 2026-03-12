# Source: https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/godaddy.md

# GoDaddy

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from GoDaddy.

This guide assumes your domain uses GoDaddy's nameservers (e.g., `ns1.domaincontrol.com` or `ns2.domaincontrol.com`). This applies whether you registered your domain directly with GoDaddy or just pointed your DNS to GoDaddy from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the GoDaddy dashboard, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Go to GoDaddy and locate the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FA0We0czQf0sdyOo6gKiC%2Fgodaddy-domain-list.png?alt=media&#x26;token=67c6c7c6-e8da-4f3e-b6ce-8957ae821348" alt="" width="375"></div>
{% endstep %}

{% step %}
Open the DNS settings and click **Add New Record**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F5WCxWMiIYgu6HdkFDKFO%2Fgodaddy-dns-settings.png?alt=media&#x26;token=994af315-6860-455a-969c-ea0300864e90" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to GoDaddy. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**. The naming of these records in Mailtrap is the same as in GoDaddy.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fm0siaM1xMYdRbyinCWx9%2F1.png?alt=media&#x26;token=9c199389-6e2a-48cd-b5d7-f6741bf7140a" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in GoDaddy. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F7RhtVtC6IiYXIdbZbkj6%2F2.png?alt=media&#x26;token=091e9e14-661e-420f-b98a-2dda217f4831" alt=""><figcaption></figcaption></figure>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FEWjqsg3rLrTV7zZ3HIIW%2Fgodaddy-dns-type-selector.png?alt=media&#x26;token=f20316cf-3859-45c2-95d5-515446d7d7a2" alt="GoDaddy DNS record type selector dropdown" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FYf5YGSWS0GzgFLZFuYyc%2Fgoogle-cloud-dns-6.png?alt=media&#x26;token=e0c487f6-cbac-453d-a924-79502ac975da" alt="" width="563"></div>
{% endstep %}

{% step %}
Paste the values into GoDaddy DNS management page.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fv1UJWwEjCESQB92EKm5M%2Fgodaddy-paste-dns-values.png?alt=media&#x26;token=79bc9a14-4ef4-49f7-a9b5-71fb1d47db72" alt="Pasting DNS values into GoDaddy record form" width="563"></div>
{% endstep %}

{% step %}
Use the default value for TTL.

Click Save after adding each record in GoDaddy.
{% endstep %}

{% step %}
Repeat the process of copying and pasting for each record until you've added all the Mailtrap DNS records to GoDaddy.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F5ET4NItKg574VPZXOJDe%2Fgodaddy-all-dns-records-added.png?alt=media&#x26;token=b1c7dca8-042f-46bf-8f25-0ac175335499" alt="" width="563"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FBhy4zE92B4b5WXKNU3FL%2Fgoogle-cloud-dns-11.png?alt=media&#x26;token=7971338b-bf0b-4e9f-96f2-e9ee91a7f37a" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from Missing to Verified, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTHdyFGVpLLtjdgD99mOW%2Fgoogle-cloud-dns-12.png?alt=media&#x26;token=f1bc9168-5e47-460a-8e79-3fbc859f9df7" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [GoDaddy documentation](https://uk.godaddy.com/help/manage-dns-records-680) or contact us at <support@mailtrap.io>.
{% endhint %}
