# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing.md

# Allow Listing

This section explains allow listing and the steps needed to use the platform effectively. To ensure phishing simulation emails or training enrollments reach users' inboxes without being blocked, allow list the phishing simulation IP addresses and phishing simulation domains on your server and security solutions.

It’s strongly recommended to send a test email to a small user group to confirm successful allow listing.

## **Phishing Simulation IP Addresses for Allow Listing**

All clients must allow list the IP addresses listed below in their email server and security solutions.

* 149.72.161.59
* 149.72.42.201
* 149.72.154.87

{% hint style="info" %}
If you use [Direct Email Creation](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/direct-email-creation), allow listing isn’t required.
{% endhint %}

## Phishing Simulation Domains for Allow Listing

We strongly recommend allow listing phishing simulation domains in your email server and security solutions to enhance the effectiveness of your phishing simulation program. Phishing simulation domains vary based on customer location, language, and license type.

To find the phishing domains specific to your organization and allow list them, please navigate to **Phishing Simulator > Settings**

## Shortcuts

The shortcuts below will show you how to allow list phishing simulation IP addresses and phishing simulation domains with the most commonly used email services.

* [How to Allow List an IP Address in Office 365](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-an-ip-address-in-office-365)
* [How to Allow List an IP Address in Exchange 2013 and 2016](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-an-ip-address-in-exchange-2013-and-2016)
* [How to Allow List an IP Address in Google Workspace](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-an-ip-address-in-google-workspace)
* [Allow Listing in Security Solutions](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/allow-listing-in-other-security-solutions)
* [Why does "X" appear on Microsoft Emails in the Outlook App?](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/allow-listing-the-pictures-on-microsoft-outlook-apps)

## FAQ

### Q: Can I use Phishing Simulation on Office 365 without using Allow Listing?

A: Yes, you can. Our Direct Email Creation (DEC) feature enables you to send simulated phishing emails directly to users' inboxes, eliminating the need for Allow Listing. Discover how to leverage the DEC feature [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/direct-email-creation).

### Q: Does Allow Listing create a security weakness?

A: Allowing IP addresses or PTR Domains are owned by the platform, and only authorized admins are able to send emails to selected target users. Therefore, it does not create a security weakness for the organization.

### Q: Can I run training assignments or phishing tests without allow listing?

A: Yes, you can, but it is definitely not recommended. If allow listing is not properly done, there may be delivery difficulties. The best practice is to allow the platform IPs or PTR Domains before using the product.
