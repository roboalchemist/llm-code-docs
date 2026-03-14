# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/recommended-add-domains-to-url-protection/allow-list-for-google-workspace.md

# Allow List for Google Workspace

## How to Allow List an IP Address in Google Workspace <a href="#how-to-whitelist-an-ip-address-in-google-workspace" id="how-to-whitelist-an-ip-address-in-google-workspace"></a>

### Google Workspace IP Bypass <a href="#google-workspace-ip-bypass" id="google-workspace-ip-bypass"></a>

The below instructions will show you how to allow list the emails such as notification, training, or phishing simulation emails that will be sent from the platform to users by allow listing **Sender** **IPs** in the Google Workspace environment.To complete this procedure, you must have security administrator privileges with Google Workspace.

1. Note the [IP addresses](https://doc.keepnetlabs.com/Next-Generation-Product/getting-started/whitelisting#ip-addresses-and-domains-to-allow) to be allowed.
2. Sign in to [Google Admin.](https://admin.google.com/)​
3. Select **Apps > Google Workspace > Gmail** from the left sidebar menu.
4. Go to the **Spam, Phishing, and Malware** page.
5. Select the **Email allowlist** tab and click the **Edit** button.
6. Add the IP addresses that are listed here.
7. Click the **Save** button.
8. Go back to the **Spam, Phishing, and Malware** page.
9. Select the **Inbound Gateway** option and click **Enable**, if not enabled.
10. Add the IP addresses and click **Save**.
11. Select **Automatically detect external IP** if not already selected.
12. **WARNING:** Leave the option of **Reject all mail not from gateway IPs** unchecked.
    1. This option must be 'unchecked'. **Do not enable this option!**
13. Select the option of **Require TLS for connections from the email gateways listed above**.
14. Click **Save** to complete the process.

✅ **You have now Allow List Domains so your target users can successfully open Keepnet email links. Please also Allow List in your security solutions if you haven't already.**

**Next step is to** [**Setup your Phishing Reporter**](https://github.com/ucarozan/keepnet-docs/blob/main/next-generation-product/getting-started/6.-setup-phishing-reporter) **➡️**
