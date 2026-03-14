# Source: https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/aws-route-53.md

# AWS Route 53

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from AWS Route 53.

This guide assumes your domain uses Route 53's nameservers (e.g., `ns-123.awsdns-12.com` or `ns-456.awsdns-34.net`). This applies whether you registered your domain directly with AWS or just pointed your DNS to Route 53 from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the AWS Management Console, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Go to the **AWS Management Console**, type **Route 53** in the search bar, and click on it.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fk9E6RAYQXU6kCjvQKo6l%2Faws-route53-search.png?alt=media&#x26;token=ce589f79-3d1a-4cc1-bdff-a6f6f81928b0" alt="" width="375"></div>
{% endstep %}

{% step %}
Navigate to **Hosted Zone** settings for the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FqF8mqbLrxo3wwY8lY1AF%2Faws-route53-hosted-zones.png?alt=media&#x26;token=bb48b450-01c8-46c2-9606-d0517b81a74c" alt="" width="375"></div>
{% endstep %}

{% step %}
Click the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FK1R2UizdVI9Cbh7n5TM8%2Faws-route53-domain-records.png?alt=media&#x26;token=f5cdf109-0e07-4238-b47f-e200555bb78c" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Create record** button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FNA8EYM9RYQGOUOxbjrDN%2Faws-route53-create-record-button.png?alt=media&#x26;token=2db45bca-6494-4ffb-966a-c66ca693b1cf" alt="" width="375"></div>
{% endstep %}

{% step %}
Return to Mailtrap. On the Domain Verification page, you'll see the DNS records you need to add to AWS Route 53. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FJquaSVRQBHMiM4aSbxjH%2F1.png?alt=media&#x26;token=b7f605ad-89c0-4123-94e7-c319d35148c4" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in AWS Route 53. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type records** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FjmkdQ32IwgOcpQs5HM5A%2F2.png?alt=media&#x26;token=12a1a229-b725-426f-bdd0-102611afba36" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FPdyyks2i6mSTQRDEAYU5%2Fmailtrap-dns-records-copy.png?alt=media&#x26;token=7eaa8210-7e6b-451c-a1a9-a4ea64cb6a32" alt="" width="563"></div>
{% endstep %}

{% step %}
Paste the **Name** and **Value** into AWS Route 53. The namings of the records are the same in AWS Route 53 as in Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fad42KavVGNP0bnEJeMtJ%2Faws-route53-add-record-form.png?alt=media&#x26;token=3f6c28d6-c281-49e9-a13c-3e6ae024e7d6" alt="" width="563"></div>

Use the default value for TTL as indicated in Mailtrap. Click Add another record after adding each record in AWS Route 53.
{% endstep %}

{% step %}
Repeat the process of copying and pasting for each record until you've added all the Mailtrap DNS records to AWS Route 53. Click **Create Records**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FSt3aa6mmzjjCpRdUUsMX%2Faws-route53-all-records-added.png?alt=media&#x26;token=0f4936e2-2608-4091-82ac-ac0122da33ca" alt="" width="563"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FchZAR8QZqW8HXV1qt27M%2Faws-route53-recheck-dns.png?alt=media&#x26;token=672ff691-3f18-4d33-ac8d-b905aaccf2f2" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the **Status** of DNS records will change from Missing to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FvoLvu6K12jnOfutIV0AM%2Fmailtrap-verified-dns-records.png?alt=media&#x26;token=7fdb4ea8-9a6d-4002-a301-4630f89c52d7" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, [consult AWS documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) or contact us at <support@mailtrap.io>.
{% endhint %}
