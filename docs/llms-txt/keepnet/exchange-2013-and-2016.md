# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/3.-email-deliverability/exchange-2013-and-2016.md

# Exchange 2013 and 2016

{% hint style="warning" %}
To complete this procedure, you must have security administrator privileges with the Microsoft Security & Compliance Center or be a member of the Microsoft Exchange Online Organization Management administrator group.
{% endhint %}

1. Note the [IP addresses](https://app.gitbook.com/o/-LMcQ_WBbT5jibln-2Mt/s/lKFxOYqYqSykikkXpwjG/next-generation-product/getting-started/3.-ensure-email-deliverability/exchange-2013-and-2016) to be allowed.
2. Log in to your exchange admin center.
3. From the left sidebar menu, go to **Mail flow > Connectors**.
4. Click **Add a connector**.
5. Select **Partner organization** in the **Connection** from the section.
6. Give the connector a name and click **Next**.
7. In the **Authenticating sent email** window, select the option that states **By verifying that the IP address of the sending server matches one of the following IP addresses that belong to your partner organization**.
8. Enter the IP addresses and click **Next**.
9. Uncheck the TLS option stating **Reject email messages if they are not sent over**.
10. Click **Next**, then click **Save** to complete the process.

You must complete the following steps once the **connector** is defined.

1. Go to the **Mail flow > Rules** page in the left sidebar menu.
2. Click the **+ icon** on the screen and select **Bypass spam filtering**.
3. In the **New rule** window, give the rule a name and select **The sender is ... > IP address is in any of these ranges or exactly matches.**
4. Enter the IP addresses and click **OK**.
5. In the **Do the following** section, select Set the message header to this value ... > Set a message header and enter **“X-MS-Exchange-Organization-Bypass Clutter”** in the text field, and click **OK**.
6. Set the value information to **true** with the enter text option on the right.
7. Click **Save** to complete the process.

#### **🚨 If you have additional security solutions (e.g. Mimecast) please make sure to allow list in these security solutions by following these steps:**

[​Allow Listing in Security Solutions​](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/allow-listing-in-other-security-solutions)

​✅ **You have now ensured your target users will receive emails through Keepnet. Now you need to** [**Allow List Domains**](https://doc.keepnetlabs.com/next-generation-product/getting-started/recommended-add-domains-to-url-protection) **so your target users can successfully open Keepnet email links ➡️**

### Video Tutorial <a href="#video-tutorial" id="video-tutorial"></a>

The following video tutorial contains information about how to Allow List in Exchange 2013 or 2016 environment.

{% embed url="<https://youtu.be/GsSylrZqlxQ>" %}
