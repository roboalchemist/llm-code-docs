# Source: https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/cloudflare.md

# Cloudflare

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from Cloudflare.

This guide assumes your domain uses Cloudflare's nameservers (e.g., `anna.ns.cloudflare.com` or `bob.ns.cloudflare.com`). This applies whether you registered your domain directly with Cloudflare or just pointed your DNS to Cloudflare from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in Cloudflare's dashboard, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Open the **Cloudflare dashboard** and select the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FX34GISlEp6hCT3gdwXu5%2Fcloudflare-domain-dashboard.png?alt=media&#x26;token=be43139b-a9be-4307-aa26-73b91c8c0b76" alt="" width="563"></div>
{% endstep %}

{% step %}
Click on the **DNS button** in the left navigation panel. This will open DNS records.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FbqITal5uybQkArd6cTsD%2Fcloudflare-dns-menu.png?alt=media&#x26;token=e99c9153-255f-45f7-bf88-9193e20e30df" alt="" width="131"></div>
{% endstep %}

{% step %}
Click on the **Add Record** button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fswm55N6qPhld319vXmFW%2Fcloudflare-add-record-button.png?alt=media&#x26;token=c8dae520-e838-4d8b-a383-ccc7db5681e1" alt="" width="563"></div>
{% endstep %}

{% step %}
On the **Domain Verification page** in Mailtrap, you'll see the DNS records you need to add to Cloudflare. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FGwQOUF3UKuy9oM9IVSUP%2F1.png?alt=media&#x26;token=a86e347a-bf9f-4e1f-bfa1-785f5a631e8e" alt=""><figcaption></figcaption></figure>

Pay attention to the Type next to each record in Mailtrap and choose a relevant one in Cloudflare. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FjILEdX6bX0GcoJKI0Gmu%2F2.png?alt=media&#x26;token=51fa1a45-c89d-449f-9b2f-4f41d1797dd3" alt=""><figcaption></figcaption></figure>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FEXds5DPNC7IJtndLIcZy%2Fcloudflare-record-type-dropdown.png?alt=media&#x26;token=e41a106b-f48d-4e8d-be5b-25aad380d2a9" alt="DNS record type dropdown in Cloudflare" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FZwLgo6duw7mE0nndLgz3%2Fcloudflare-copy-dns-values.png?alt=media&#x26;token=a88b4350-5f1c-46ee-8474-023954498165" alt="" width="563"></div>
{% endstep %}

{% step %}
Paste the the values into Cloudflare. Remember that Cloudflare refers to the Value field as **Target** for **CNAME records** and **Content** for **TXT records**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FgA5QbsK62ivxw3AMPEmk%2Fcloudflare-paste-dns-values.png?alt=media&#x26;token=16b2cee0-8889-4c22-b311-1e3f9c9bdf3b" alt="" width="563"></div>
{% endstep %}

{% step %}
If you're not using a proxy, make sure you disable it. By default, it will be enabled.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FMSQr9P6sGH235Ko4qQmu%2Fcloudflare-disable-proxy.png?alt=media&#x26;token=46953687-bafd-43c6-a39b-cf0cdb4f64a3" alt=""></div>
{% endstep %}

{% step %}
Use the default value for **TTL**.

Click **Save** and repeat the process for all the remaining DNS records.
{% endstep %}

{% step %}
Then, **return to Mailtrap**. Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Furic1nPmhM4mz8fNHoKY%2Fcloudflare-recheck-dns-records.png?alt=media&#x26;token=7e62b12a-5021-42dc-bace-5e4d98c4da9c" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from **Missing** to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FLwRo224r3B8pXSH0KBkp%2Fcloudflare-verified-dns-records.png?alt=media&#x26;token=7e856771-bd6b-4b05-a101-71197002d559" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [Cloudflare documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) or contact us at <support@mailtrap.io>
{% endhint %}
