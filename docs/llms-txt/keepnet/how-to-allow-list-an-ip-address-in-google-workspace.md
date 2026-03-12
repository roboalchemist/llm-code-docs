# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-an-ip-address-in-google-workspace.md

# How to Allow List an IP Address in Google Workspace

## Google Workspace IP Bypass

The below instructions will show you how to allow list the emails such as notification, training, or [phishing simulation](https://keepnetlabs.com/products/phishing-simulator) emails that will be sent from the platform to users by allow listing **Sender** **IPs** in the Google Workspace environment.

{% hint style="warning" %}
To complete this procedure, you must have security administrator privileges with Google Workspace.
{% endhint %}

1. Note the [IP addresses](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) to be allowed.
2. Sign in to [Google Admin.](https://admin.google.com/)
3. Select **Apps > Google Workspace > Gmail** from the left sidebar menu.
4. Go to the **Spam, Phishing, and Malware** page.
5. Select the **Email allowlist** tab and click the **Edit** button.
6. Add the IP addresses that are listed here.
7. Click the **Save** button.
8. Go back to the **Spam, Phishing, and Malware** page.
9. Select the **Inbound Gateway** option and click **Enable**, if not enabled.
10. Add the IP addresses and click **Save**.
11. Select **Automatically detect external IP** if not already selected.
12. <mark style="color:red;">**WARNING:**</mark> Leave the option of **Reject all mail not from gateway IPs** unchecked.
    1. This option must be 'unchecked'. **Do not enable this option!**
13. Select the option of **Require TLS for connections from the email gateways listed above**.
14. Click **Save** to complete the process.

## Video Tutorial

{% embed url="<https://youtu.be/gsX6r_3gD8U>" %}
