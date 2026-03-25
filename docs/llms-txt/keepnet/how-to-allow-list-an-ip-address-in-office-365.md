# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-an-ip-address-in-office-365.md

# How to Allow List an IP Address in Office 365

It's suggested to use all the methods explained in this documentation step by step for allow listing successfully. The customer may skip the related step if there is no feature in their O365 environment due to the license.

## How to Allow List Using the Third-party Phishing Simulations Feature in Office 365

The below instructions will show you how to allow list the emails such as notification, training, or phishing simulation emails that will be sent from the platform to users by allow listing **Sender** **IPs** and **Domains** in the O365 environment in the [**Phishing Simulation**](https://keepnetlabs.com/products/phishing-simulator) feature.

{% hint style="info" %}
To complete this procedure, you must have security administrator privileges with the Microsoft Security & Compliance Center or be a member of the Microsoft Exchange Online Organization Management administrator group.
{% endhint %}

1. Note the [IP addresses](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) to be allowed.
2. Sign in to the [Microsoft Security & Compliance](https://security.microsoft.com/homepage) Center.
3. Click the **Policies & rules** item on the left sidebar menu.
4. Go to **Threat policies > Advanced delivery**.
5. Click the **Phishing simulations** tab and click **Edit**.
6. Add the **IP address** to **Sending IP** section\*\*.\*\*
7. Add the **Domain** address (also known as the **MAIL** **FROM** address) used in the phishing campaign into the **Domains** section.
8. Add the **phishing domains** [here](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing-in-other-security-solutions#whitelisting-platform-addresses) by using **\*.domain.com/\*** wildcard syntax to **Simulation URLs to allow** section.
9. Click **Save** to complete the process.

## How to Allow List Using the Threat Policies Feature in Office 365

The below instructions will show you how to allow list the emails such as notification, training, or phishing simulation emails that will be sent from the platform to users by allow listing **Sender** **IPs** in the O365 environment in the **Threat Policies** feature.

{% hint style="info" %}
To complete this procedure, you must have security administrator privileges with the Microsoft Security & Compliance Center or be a member of the Microsoft Exchange Online Organization Management administrator group.
{% endhint %}

1. Note the [IP addresses](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) to be allowed.
2. Sign in to the [Microsoft Security & Compliance](https://security.microsoft.com/homepage) Center.
3. Click the **Policies and rules** > **Anti-Spam** under the **Policies.** To go directly to the Anti-spam policies page, use <https://security.microsoft.com/antispam>
4. Click the **Connection Filter Policy** and select the **Edit** **connection** **filter**.
5. Add the IP addresses to the section labeled **Always allow messages from the following IP addresses or address range**.
6. Enable the **Turn on safe** list option.
7. Click **Save** to complete the process.

## How to Allow List Using the Safe Links Feature in Office 365

The below instructions will show you how to allow list the emails such as notification, training, or phishing simulation emails that will be sent from the platform to users by allow listing **Domains** in the O365 environment in the **Safe** **Links** feature.

{% hint style="danger" %}
This step is suggested to prevent any false clicks on training or phishing reports.
{% endhint %}

{% hint style="info" %}
To complete this procedure, you must have security administrator privileges with the Microsoft Security & Compliance Center or be a member of the Microsoft Exchange Online Organization Management administrator group.
{% endhint %}

1. Please ask for the list of the [phishing simulator](https://keepnetlabs.com/products/phishing-simulator) domains from [here](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing-in-other-security-solutions#whitelisting-platform-addresses).
2. Sign into the [**Microsoft Security & Compliance**](https://security.microsoft.com/) Center.
3. Click and open the **Email & Collaboration** menu from the left.
4. Click **Policies and rules** from the left sidebar menu, click **Threat** **Policies** and select **Safe Links**.
5. Click **Create**.
6. Add a name and description for your safe links policy and click **Next**.
7. Select your company domain to be included in this policy and click **Next**.
8. Deselect the **"Track user clicks"** option and the **"Office 365 Apps"** option.
9. Add the **phishing domains** [here](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing-in-other-security-solutions#whitelisting-platform-addresses) by using **\*.domain.com/\*** wildcard syntax to the **Do not rewrite the following URLs** section.
10. Click the **Next** button and select **Submit** to complete the process.

{% hint style="warning" %}
After creating the rule, it may not effect immediately, please wait a couple of hours before you test it.
{% endhint %}

## How to Allow List Using the Spam Filter Bypass Feature in Office 365

The below instructions will show you how to allow list the emails such as notification, training, or phishing simulation emails that will be sent from the platform to users by allow listing the **Sender** **IPs** in the O365 environment in the **Bypass Spam Filter f**eature.

{% hint style="info" %}
To complete this procedure, you must have security administrator privileges with the Microsoft Security & Compliance Center or be a Microsoft Exchange Online Organization Management administrator group member.
{% endhint %}

1. Sign in to the [admin](https://admin.microsoft.com/AdminPortal/) portal.
2. Go to **Exchange > Mail flow > Rules** and click the **+ Add a rule** butto&#x6E;**.**
3. Select the **Bypass Spam Filter** option.
4. Enter a name for your allow listing rule.
5. Scroll down to the **"Apply this rule if..."** section and select "**The** **sender"** and then select **"IP address is in any of these ranges or exactly matches"**
   1. To the right you'll see **"Enter text...",** click **"Enter Words"** to bring up a new window labeled **specify** **IP** **address** **ranges,** and enter the **IPs** listed [here](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) and then click the **Save** button.
6. Scroll down to the "**Do the following"** section.
   1. Select the "**Modify the message properties"** option and then select the "**Set the spam confidence level(SCL)"** option.
   2. And then click the **Set the spam confidence level (SCL) to '-1'** option and select "**Bypass spam filtering"** and click the **Save** butto&#x6E;**.**
7. Next to the **"Do the following"** field, click **+** button to create a new rule.
   1. Select the **"Modify the message properties"** option and then select the **"set a message header"** option.
   2. Click **"Enter** **Words"** and type **"X-MS-Exchange-Organization-BypassClutter"** and then click the **Save** button.
   3. Next, click **Enter** **Words** under the **"header value"** and type **"true".**
8. We recommend leaving the rest of the rule settings the same. Once you have completed these steps, click **Save** to save your allow listing rule.
9. Make sure the allow listing rule's status is enabled. If it's disabled, click on it and **Enable** it and click the **Edit** **Rule** **Settings** button on the opened page to save it.

## How to Bypass Advanced Threat Protection (ATP) "Link" by Using IP Address in Office 365

The below instructions will show you how to allow list the emails such as notification, training, or phishing simulation emails that will be sent from the platform to users by allow listing the **Sender** **IPs** in the O365 environment with the **"SkipSafeLinksProcessing**" rule.

{% hint style="danger" %}
This step is suggested to prevent scanning phishing simulation links by O365 sent by the platform.
{% endhint %}

{% hint style="info" %}
To complete this procedure, you must have security administrator privileges with the Microsoft Security & Compliance Center or be a Microsoft Exchange Online Organization Management administrator group member.
{% endhint %}

1. Sign in to the [admin](https://admin.microsoft.com/AdminPortal/) portal.
2. Go to **Exchange > Mail flow > Rules** and click the **+ Add a rule** butto&#x6E;**.**
3. Click on the **Create a new rule** option.
4. Enter a name for your allow listing rule.
5. Scroll down to the **"Apply this rule if..."** section and select "**The** **sender"** and then select **"IP address is in any of these ranges or exactly matches"**
   1. To the right, you'll see **"Enter text...",** click **"Enter Words"** to bring up a new window labelled **specify** **IP** **address** **ranges,** and enter the **IPs** listed [here](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) and then click the **Save** button.
6. Scroll down to the **"Do the following"** section.
   1. Select the **"Modify the message properties"** option and then select the **"Set a message header"** option.
   2. Set the message header to **"X-MS-Exchange-Organization-SkipSafeLinksProcessing"** and set the value to **"1"**.
7. We recommend leaving the rest of the rule settings the same. Once you have completed these steps, click **Save** to save your allow listing rule.
8. Make sure the allow listing rule's status is enabled. If it's disabled, click on it and **Enable** it and click the **Edit** **Rule** **Settings** button on the opened page to save it.

## How to Bypass Advanced Threat Protection (ATP) "Attachment" by Using IP Address in Office 365

The below instructions will show you how to allow list the attached files in the emails that will be sent from the platform to users by allow listing the **Sender** **IPs** in the O365 environment with the **"SkipSafeAttachmentProcessing"** rule.

{% hint style="danger" %}
This step is suggested to prevent scanning phishing simulation attachment files by O365 sent by the platform.
{% endhint %}

{% hint style="info" %}
To complete this procedure, you must have security administrator privileges with the Microsoft Security & Compliance Center or be a Microsoft Exchange Online Organization Management administrator group member.
{% endhint %}

1. Sign in to the [admin](https://admin.microsoft.com/AdminPortal/) portal.
2. Go to **Exchange > Mail flow > Rules** and click the **+ Add a rule** butto&#x6E;**.**
3. Click on the **Create a new rule** option.
4. Enter a name for your allow listing rule.
5. Scroll down to the **"Apply this rule if..."** section and select "**The** **sender"** and then select **"IP address is in any of these ranges or exactly matches"**
   1. To the right, you'll see **"Enter text...",** click **"Enter Words"** to bring up a new window labelled **specify** **IP** **address** **ranges,** and enter the **IPs** listed [here](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) and then click the **Save** button.
6. Scroll down to the **"Do the following"** section.
   1. Select the **"Modify the message properties"** option and then select the **"Set a message header"** option.
   2. Set the message header to **"X-MS-Exchange-Organization-SkipSafeAttachmentProcessing"** and set the value to **"1"**.
7. We recommend leaving the rest of the rule settings the same. Once you have completed these steps, click **Save** to save your allow listing rule.
8. Make sure the allow listing rule's status is enabled. If it's disabled, click on it and **Enable** it and click the **Edit** **Rule** **Settings** button on the opened page to save it.

## Troubleshooting

If the emails sent by the platform somehow is not delivered to the user's inbox, the admin can use the following steps to see why it's not delivered and find a solution for it.

1. Sign in to the [admin](https://admin.microsoft.com/AdminPortal/) portal.
2. Go to **Exchange > Mail flow > Message Trace** and click the **+ start a trace** butto&#x6E;**.**
3. Enter the from address to the **"Senders"** field which is expected to be delivered from the platform and click the **Search** button.
4. The O365 will list the emails that is delivered from the specified email address and then you can click on the emails to see more information.
5. While on the Quarantine page, click on the email to view more details. Scroll down to the email body to check the links inside. If you notice a **Mimecast** link, it indicates that Mimecast has interfered with the email. In this case, you need to [allow list the email in Mimecast](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-in-mimecast).

## Video Tutorial

The following video playlist tutorial contains information about how to allow list in O365 environment.

{% embed url="<https://youtube.com/playlist?list=PLTfpxvprC-_w5co46z8kqxeizCFR6ty2G>" %}
