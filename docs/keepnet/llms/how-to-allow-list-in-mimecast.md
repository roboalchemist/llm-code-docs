# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-in-mimecast.md

# How to Allow List in Mimecast

Ensure that important emails from trusted sources, like training notifications or [phishing simulation](https://keepnetlabs.com/products/phishing-simulator) emails, bypass Mimecast's usual filtering processes by following these steps. This document guides you through setting up various policies within Mimecast to improve the deliverability and reliability of these critical communications.

## **Impersonation Protection Bypass Policy**

To prevent Mimecast from blocking emails from known and safe sources due to impersonation protection rules, set up an Impersonation Protection Bypass Policy.

1. Note the [IP addresses](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) to be allowed.
2. **Log in to your Mimecast Administration Console.**
3. Navigate to **Administration > Gateway | Policies**.
4. Choose **Impersonation Protection Bypass** from the policies list and click **New Policy**.
5. Configure the policy:
   * **Applies From**: Everyone (using IP addresses/Hostnames as the source)
   * **Applies To**: Everyone
6. Enter the specific IP addresses under [**Source IP Ranges**](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow).
7. Save the policy settings.

For more information on these settings, see Mimecast's[ Configuring an Impersonation Protection Bypass Policy](https://community.mimecast.com/docs/DOC-1909) article.

## **Anti-Spoofing Policy**

Set up an Anti-Spoofing Policy to allow emails that appear to be coming from your domain.

1. Note the [IP addresses](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) to be allowed.
2. Access **Gateway | Policies** via the **Administration** tab.
3. Select **Anti-Spoofing**, then **New Policy**.
4. Define the policy:
   * **Emails From**: Everyone (utilizing IP addresses)
   * **Emails To**: Everyone
5. Add the Keepnet IP addresses in the [**Source IP Ranges**](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow).
6. Commit the changes to ensure that emails are recognized as legitimate. Configure Anti-Spoofing

For more information see Mimecast's[ Configuring an Anti-Spoofing Policy](https://community.mimecast.com/docs/DOC-1419#jive_content_id_Configuring_an_AntiSpoofing_Policy) article.

## **Permitted Senders Policy**

To allowlist emails specifically for training and phishing simulation:

1. Note the [IP addresses](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow) to be allowed.
2. Go to **Gateway | Policies** and select **Permitted Senders**.
3. Click **New Policy** and set the parameters:
   * **Emails From**: Everyone (with specified IPs)
   * **Emails To**: Everyone
4. Include the relevant IP addresses in [**Source IP Ranges**](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow).
5. Finalize the settings by saving the policy.

For more information on these settings see Mimecast's[ Configuring a Permitted Senders Policy](https://community.mimecast.com/docs/DOC-1427#jive_content_id_Configuring_aPermitted_Senders_Policy) article.

## **URL Protection Bypass Policy**

For accurate phishing test results, exclude certain URLs from Mimecast's URL Protection.

{% hint style="info" %}
You can find the phishing simulation domains by logging into the platform and then going to **Phishing Simulator > Settings > Domains** page.
{% endhint %}

1. Under **Gateway | Policies**, select **URL Protection Bypass** and then **New Policy**.
2. Adjust the policy settings:
   * **Applies From**: Everyone (IP addresses/hostnames as the source)
   * **Applies To**: Everyone
3. Input the applicable IP ranges in [**Source IP Ranges**](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/..#ip-addresses-and-domains-to-allow).
4. Save your changes to activate the policy.

For more information on these settings, see Mimecast's[ Configuring a URL Protection Bypass Policy](https://community.mimecast.com/docs/DOC-1030#jive_content_id_Configuring_a_URL_Protection_Bypass_Policy) article

## Final Steps

After setting up these policies, conduct a small-scale test to ensure everything functions as intended before rolling out to your entire organization. This verification step is crucial to prevent disruptions and ensure that all settings are correctly applied.
