# Source: https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder/mail-configurations/google-workspace.md

# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/3.-email-deliverability/google-workspace.md

# Google Workspace

It is essential that your employees are able to open all emails sent via Keepnet platform for you to accurately measure how your employees behave when faced with evolving social engineering threats.

**To ensure emails are delivered in Google Workspace, you have 2 options:**

​[Direct Email Creation](https://doc.keepnetlabs.com/next-generation-product/getting-started/3.-email-deliverability/google-workspace/google-direct-email-creation) (recommended)

​[Allow Listing](https://doc.keepnetlabs.com/next-generation-product/getting-started/3.-email-deliverability/google-workspace/google-allow-listing)​

{% hint style="success" %}
You only need to do one of these options. Customers do not need to complete both.
{% endhint %}

## **Direct Email Creation** <a href="#direct-email-creation" id="direct-email-creation"></a>

**Direct Email Creation (DEC)** is a feature that connects to your O365 or Google Workspace with a few required API permissions. This feature creates the phishing simulation email directly in the user’s inbox instead of sending the emails over SMTP protocol.

**Key Benefits:**

1. Remove false positives that allow listing tools cause when analyzing links
2. Eradicate maintenance and challenges of allow listing for the purpose of email delivery (you may need to allow list in your URL protection solutions such as Defender or ZScaler)
3. Very simple and quick setup (can be completed in a couple of minutes!)

## Allow Listing <a href="#whitelisting" id="whitelisting"></a>

**Allow Listing** is common practise for ensuring emails from specific domains are delivered successfully to the inboxes of your employees. Allow Listing is a method used by many organisations to ensure emails are successfully delivered.

The **key challenge** our customers face with allow listing is email analysis tools often open links within emails to check for maliciousness, impacting the accuracy of your reporting data. For example, it may show that your employees have opened the phishing link when they have not. This will directly influence who receives the behavioural-based training.
