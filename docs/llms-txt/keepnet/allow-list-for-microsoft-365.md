# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/recommended-add-domains-to-url-protection/allow-list-for-microsoft-365.md

# Allow List for Microsoft 365

## How to Allow List Using the Safe Links Feature in Office 365 <a href="#how-to-whitelist-using-the-safe-links-feature-in-office-365" id="how-to-whitelist-using-the-safe-links-feature-in-office-365"></a>

The below instructions will show you how to allow list the emails such as notification, training, or phishing simulation emails that will be sent from the platform to users by allow listing **Domains** in the O365 environment in the **Safe** **Links** feature.

{% hint style="danger" %}
This step is suggested to prevent any false clicks on training or phishing reports.
{% endhint %}

{% hint style="info" %}
To complete this procedure, you must have security administrator privileges with the Microsoft Security & Compliance Center or be a member of the Microsoft Exchange Online Organization Management administrator group.
{% endhint %}

1. Find the list of the [phishing simulator](https://keepnetlabs.com/products/phishing-simulator) domains in **Phishing Simulator > Settings > Domains**.
2. Sign into the **Microsoft Security & Compliance** Center.
3. Click **Policies and rules** from the left sidebar menu, click **Threat** **Policies** and select **Safe Links**.
4. Click **Create**.
5. Add a name and description for your safe links policy and click **Next**.
6. Select your company domain to be included in this policy and click **Next**.
7. Deselect the **Track user clicks** option.
8. Add the **phishing domains** by using **\*.domain.com/\*** wildcard syntax to the **Do not rewrite the following URLs** section.
9. Click the **Next** button and select **Submit** to complete the process.

✅ **You have now Allow List Domains so your target users can successfully open Keepnet email links. Please also Allow List in your security solutions if you haven't already.**

**Next step is to** [**Setup your Phishing Reporter**](https://github.com/ucarozan/keepnet-docs/blob/main/next-generation-product/getting-started/6.-setup-phishing-reporter) **➡️**
