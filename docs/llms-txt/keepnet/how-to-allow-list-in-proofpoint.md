# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-in-proofpoint.md

# How to Allow List in Proofpoint

To ensure smooth delivery of Keepnet’s simulated phishing campaigns and awareness training notifications, you may need to allow list Keepnet in your Proofpoint environment. This guide covers configuration steps for both **Proofpoint Essentials** and **Proofpoint Enterprise**.

{% hint style="info" %}
These are third-party configurations. If you encounter any difficulties during the process, we recommend contacting Proofpoint support directly. For any questions specific to Keepnet, feel free to reach out to our support team.
{% endhint %}

## Allow List in Proofpoint Essentials

Follow the steps below to allow Keepnet’s IP addresses through **Proofpoint** **Essentials**:

1. Go to **Security Settings** > **Email** > **Sender Lists**.
2. In the **Safe Senders** section, add [Keepnet’s IP addresses](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#phishing-simulation-ip-addresses-for-whitelisting).
3. Click **Save** to apply the changes.

{% hint style="info" %}
For information about Proofpoint’s handling of email attachments, consult their documentation titled *"*[*Blocks by Default*](https://help.proofpoint.com/Proofpoint_Essentials/Email_Security/Administrator_Topics/090_filtersandsenderlists/Attachment_Types_Proofpoint_Essentials_Blocks_By_Default)*."*
{% endhint %}

## Allow List in Proofpoint Enterprise

To safelist Keepnet in your **Proofpoint** **Enterprise** environment:

1. Sign in to your **Proofpoint Enterprise Admin Console**.
2. Navigate to **Email Protection**.
3. Under the **Spam Detection** menu, select **Organizational Safe List**.
4. Click **Add** to begin a new rule.
5. In the **Global Safe List** configuration:
   * **Filter Type**: Select **Sender Hostname**.
   * **Operator**: Choose **Equals**.
   * **Value**: Enter [Keepnet’s IP addresses](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#phishing-simulation-ip-addresses-for-whitelisting).
6. Click **Save Changes**.

## URL Defense (TAP) Exemptions

To avoid disruptions by **Proofpoint Targeted Attack Protection (TAP)**, you can exclude Keepnet’s emails from **URL rewriting policies:**

1. Navigate to **Email Protection** > **Targeted Attack Protection** > **URL Defense**.
2. Select **URL Rewrite Policies**.
3. Under **Exceptions**, do the following:
   * Add [Keepnet’s IP addresses.](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#phishing-simulation-ip-addresses-for-whitelisting)
   * Add your phishing link domains.
     * To get a downloadable CSV of your phishing simulation domains, go to your **Keepnet** **dashboard** and then go to **Phishing Simulator > Settings > Domains** page.
4. Click **Save Changes**.

## Allow Listing by Simulation Domain

To allow list Keepnet by **simulation domains** in **Proofpoint**:

1. Go to **Email Firewall > Rules** in your **Proofpoint** **Admin** **Center**.
2. Enable the rule by switching **Enable** to **On**.
3. Set a descriptive name such as **'Keepnet&#x20;*****Allow Listing Simulation Domains'***
4. Under **Conditions**, click **Add Condition** and select **Sender Domain**.
5. Add the domains listed in the Keepnet platform by logging in and then going to **Phishing Simulator > Settings > Domains** page.
6. Under **Dispositions**, change **Delivery Method** to **Deliver Now**.
7. Click **Save** to apply changes.

Allow time for the rule to propagate before testing your next campaign.

## If Simulation Emails Are Going to Spam

If your simulated phishing emails land in users’ spam folders or are being quarantined, ensure **Keepnet** is on the **Organizational** **Safe** **List**:

1. In the **Proofpoint** **Admin** **Center**, go to **Email Protection** > **Spam Detection** > **Organizational Safe List**.
2. Add [**Keepnet’s IPs**](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#phishing-simulation-ip-addresses-for-whitelisting).

## Verifying Your Configuration

To confirm successful allow listing, please follow the steps below.

1. First, launch a phishing campaign to your pilot groups and confirm if the simulation emails are delivered to the inbox.
2. Second, please check the campaign report on the Keepnet platform to confirm if there are any false positives.

{% hint style="info" %}
Even after allow listing is completed, but still the emails go to spam or quarantine, please make sure you have allow listed Keepnet on your email server too. Please [check this document](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing) for more information.
{% endhint %}

If you need further help, [submit a support request](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk) — our team is here to assist.
