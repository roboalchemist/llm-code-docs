# Source: https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/google-cloud-dns.md

# Google Cloud DNS

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from Google Cloud DNS.

This guide assumes your domain uses Google Cloud DNS nameservers (e.g., `ns-cloud-a1.googledomains.com` or `ns-cloud-b1.googledomains.com`). This applies whether you registered your domain directly with Google or just pointed your DNS to Google Cloud DNS from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the Google Cloud Console, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Go to Google Cloud Console, type **Cloud DNS** in the search bar, and choose it from the results.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FmYbK66KbGzgbkcPOwCTk%2Fgoogle-cloud-dns-1.png?alt=media&#x26;token=bda68415-50ab-407c-aab7-ad2805886e32" alt="" width="563"></div>
{% endstep %}

{% step %}
In the Cloud DNS Zones page, open the **Zone details** for the domain you've added to Mailtrap by clicking on the **Zone name**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FGGBCde4w4LMHrJsJ96Ch%2Fgoogle-cloud-dns-2.png?alt=media&#x26;token=03a8aa03-471a-419e-9505-e8b113b0efbf" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Add Standard**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FRGFkPwWvqNCftp6I2U86%2Fgoogle-cloud-dns-3.png?alt=media&#x26;token=afd9664f-d5d8-4332-aaaa-aa54fb0f7148" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to Google Cloud DNS. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F0jgCAhBqu6m4BYgC2mqz%2F1.png?alt=media&#x26;token=8dbdf55f-1e8f-412e-98db-c35942f73831" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in Google Cloud DNS. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC). Ignore Google's SPF type record; it's deprecated.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FW90JI06Gym4eKGihPq3l%2F2.png?alt=media&#x26;token=0383b6e3-e1f9-4a5a-9ced-95802ac3f76a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FYf5YGSWS0GzgFLZFuYyc%2Fgoogle-cloud-dns-6.png?alt=media&#x26;token=e0c487f6-cbac-453d-a924-79502ac975da" alt="" width="563"></div>
{% endstep %}

{% step %}
And paste the values into Google Cloud DNS. Remember that Google Cloud DNS refers to the Name field as DNS Name and the Value field as either Canonical name (for CNAME-type records) or TXT data (for TXT-type records).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FxwFtV5zCdArLaotzijqp%2Fgoogle-cloud-dns-7.png?alt=media&#x26;token=035cb915-4406-4464-9b76-0ca2c2262b95" alt="Google Cloud DNS CNAME record form with DNS Name and Canonical name fields" width="375"><figcaption></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FfmxLtDqQusMdXFqCb1Uy%2Fgoogle-cloud-dns-8.png?alt=media&#x26;token=42a14773-0ace-4d00-9b61-f09fbd09f002" alt="Google Cloud DNS TXT record form with DNS Name and TXT data fields" width="563"><figcaption></figcaption></figure></div>

When adding TXT-type records, add double quotes in the beginning and the end of the record string in the TXT data field.
{% endstep %}

{% step %}
Use the default value for TTL.

Click **Create** after adding each record in Google Cloud DNS.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FIGyGSCq1CSZ4wZjUuzPb%2Fgoogle-cloud-dns-9.png?alt=media&#x26;token=ddf1dfea-cc5a-465e-8f70-b8bb6a4c3c7d" alt="" width="375"></div>
{% endstep %}

{% step %}
Repeat the process of copying and pasting for each record until you've added all the Mailtrap DNS records to Google Cloud DNS.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FHsPTUXl5rDKhlSzW8vdN%2Fgoogle-cloud-dns-10.png?alt=media&#x26;token=a3f30b17-0048-4e9e-ab57-2b1649c627ce" alt=""></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FBhy4zE92B4b5WXKNU3FL%2Fgoogle-cloud-dns-11.png?alt=media&#x26;token=7971338b-bf0b-4e9f-96f2-e9ee91a7f37a" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from **Missing** to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTHdyFGVpLLtjdgD99mOW%2Fgoogle-cloud-dns-12.png?alt=media&#x26;token=f1bc9168-5e47-460a-8e79-3fbc859f9df7" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [Google Cloud DNS documentation](https://cloud.google.com/dns/docs/records) or contact us at <support@mailtrap.io>.
{% endhint %}
