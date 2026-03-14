# Source: https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/namecheap.md

# Namecheap

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from Namecheap.

This guide assumes your domain uses Namecheap's nameservers (e.g., `dns1.registrar-servers.com` or `dns2.registrar-servers.com`). This applies whether you registered your domain directly with Namecheap or just pointed your DNS to Namecheap from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the Namecheap dashboard, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Go to Namecheap, locate the domain you've added to Mailtrap on the dashboard, and click **Manage**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FBqoAkP7QizsTG9tMiNJf%2Fnamecheap-domain-dashboard.png?alt=media&#x26;token=f935c9fa-07b9-49ca-a0cf-95ae433aeec9" alt="" width="563"></div>
{% endstep %}

{% step %}
Navigate to the **Advanced DNS** tab.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FRnNUAdv0cxefuUKEz8cG%2Fnamecheap-advanced-dns-tab.png?alt=media&#x26;token=231fbd1c-4a96-49e2-86da-02f895860992" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Add New Record**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FWJvru1WCVEGyti4E7Du1%2Fnamecheap-add-new-record-button.png?alt=media&#x26;token=424d01bd-62c5-4781-90af-e94647430545" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to Namecheap. These are Domain Verification, DKIM, DMARC, and Domain Tracking. You'll need the values under Type, Name, and Value.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fkhch8E7OiMUoshdmr6Gd%2F1.png?alt=media&#x26;token=50ff1280-1fb3-404f-bc81-18e5fb1348dc" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in Namecheap. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FS8XlNVrj8Y7upIOU7zMP%2F2.png?alt=media&#x26;token=7c4c0452-c6d6-4962-8484-3d35e6896967" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FPdyyks2i6mSTQRDEAYU5%2Fmailtrap-dns-records-copy.png?alt=media&#x26;token=7eaa8210-7e6b-451c-a1a9-a4ea64cb6a32" alt="" width="563"></div>
{% endstep %}

{% step %}
And paste the values into Namecheap. Remember that Namecheap refers to the **Name** **field** as **Host**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F9LeXD9EjyIOuU6vjJGT9%2Fnamecheap-paste-host-value.png?alt=media&#x26;token=1f38354b-3d32-4d12-9102-d372e9b42406" alt="" width="563"></div>
{% endstep %}

{% step %}
Use the **default** value for TTL.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fuw1wRhjTWFsIEoNBIOYH%2Fnamecheap-ttl-default.png?alt=media&#x26;token=d6dd6543-5a92-4e6e-9b62-065ebe33e7d5" alt="" width="375"></div>
{% endstep %}

{% step %}
Repeat the process of copying, pasting, and clicking **Add New Record** for each record until you've added all the Mailtrap DNS records to Namecheap. Click **Save All Changes**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTMPRobkoji0ZnebCs3p8%2Fnamecheap-save-all-changes.png?alt=media&#x26;token=d02f1c5b-4ce9-4a35-8493-6b869816f35f" alt="" width="375"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FAJo4OwRGaiDH9Ug6Smf5%2Fnamecheap-recheck-dns-records.png?alt=media&#x26;token=9255ea93-967d-41ab-b05e-32d5edcdd3bb" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from **Missing** to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FvoLvu6K12jnOfutIV0AM%2Fmailtrap-verified-dns-records.png?alt=media&#x26;token=7fdb4ea8-9a6d-4002-a301-4630f89c52d7" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [Namecheap documentation](https://www.namecheap.com/support/knowledgebase/article.aspx/434/2237/how-do-i-set-up-host-records-for-a-domain/) or contact us at <support@mailtrap.io>.
{% endhint %}
