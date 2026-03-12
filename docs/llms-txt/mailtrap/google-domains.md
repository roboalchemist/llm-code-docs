# Source: https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/google-domains.md

# Google Domains

To add and verify a sending domain in Mailtrap, you need access to your domain's DNS records and your domain provider account.

<a class="button secondary">Sending Domain Setup</a> check it for more details on setting up your sending domain. Continue reading to learn how to add Mailtrap DNS records to Google Domain.

{% hint style="info" %}
Note: On September 7, 2023, Squarespace acquired all domain registrations and related customer accounts from Google Domains. This means that Google Domains is now in the process of migrating account and domain data to Squarespace. Until the migration is completed, you can still manage your domains in Google Domains. After the migration, you'll need to manage your domain in Squarespace.

This guide assumes that your domain is either registered with Google Domains and uses its nameservers or isn't registered with Google Domains but uses its nameservers.
{% endhint %}

{% stepper %}
{% step %}
Go to Google Domains and select the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fn8m9pbQlbNuRxybArIO5%2Fgoogle-domains-select-domain.png?alt=media&#x26;token=60319616-6454-4a4c-8729-1e5257f1502e" alt="" width="563"></div>
{% endstep %}

{% step %}
In the left-side navigation panel, click **DNS**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FrvAw8dVDX8iXocnhu8gN%2Fgoogle-domains-click-dns.png?alt=media&#x26;token=756b6162-cb0e-4985-820c-525bf040ff1c" alt="" width="188"></div>
{% endstep %}

{% step %}
Under **Custom records** in the **Resource** **records** section, choose **Manage custom records**. In case you don't have any resource records, click **Custom records** directly.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FiAj90YvBSY3uMoUVEEgt%2Fgoogle-domains-manage-custom-records.png?alt=media&#x26;token=36e9a606-88b6-433d-bf47-ac126dcceeb6" alt="" width="563"></div>
{% endstep %}

{% step %}
Scroll down at the bottom of the records and click **Create new record**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FcOkl9pUBwsuZ83lwAuwO%2Fgoogle-domains-create-new-record.png?alt=media&#x26;token=1cdf55f6-5019-4435-b9a6-d99cedd9c63d" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to Google Domains. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FWuaJG1KKC95SKGOlNcA5%2F1.png?alt=media&#x26;token=bb2cdb5d-c035-48e0-9ec1-dab04ecf38ec" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in Google Domains. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FCbYGL0u9AEGgLtzgqO6C%2F2.png?alt=media&#x26;token=20b7980f-4b19-42c5-b508-d3e0925b1604" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTY9xq92EMTDoX50aTrh6%2Fgoogle-domains-copy-name-value.png?alt=media&#x26;token=4fb04b68-b3c3-4cb3-ad6e-0bb1af7493e8" alt="" width="563"></div>
{% endstep %}

{% step %}
**Paste the values into Google Domains**. Remember that Google Domains refers to the Name field as the **Host name** and the **Value field** as either the **Domain name** (for CNAME-type records) or **Text** (for TXT-type records).

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F04K0RFkHyCxWovek3Ugz%2Fgoogle-domains-paste-values.png?alt=media&#x26;token=9d623582-c72e-43bb-ac49-d27edbc8234b" alt="" width="563"></div>
{% endstep %}

{% step %}
Use the **default** value for TTL.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FJX5Qb7tJcISLSCvks1bR%2Fgoogle-domains-ttl-default.png?alt=media&#x26;token=b0bc0958-0e54-48bc-a068-84e547de49ca" alt="" width="563"></div>
{% endstep %}

{% step %}
Repeat the process of copying, pasting, and clicking **Create new record** for each record until you've added all the Mailtrap DNS records to Google Domains. **Click Save**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FMOf7S7m2nYxm776SmVL0%2Fgoogle-domains-save-records.png?alt=media&#x26;token=db251b8f-cd42-41ae-8c04-3278493489fd" alt="" width="563"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FSWwZlpBRD4M8BSBrOpxT%2Fgoogle-domains-recheck-dns.png?alt=media&#x26;token=4c22a985-42c5-40c5-999d-1ef66e6e02de" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from **Missing** to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FUBrtvYPBZS0hlfJWb21t%2Fgoogle-domains-verified-status.png?alt=media&#x26;token=4c7535b7-2484-4dc3-806c-5c8eafe6ca92" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the [official Google Domains documentation](https://support.google.com/domains/answer/3290350?hl=en) or contact us at <support@mailtrap.io>.
{% endhint %}
