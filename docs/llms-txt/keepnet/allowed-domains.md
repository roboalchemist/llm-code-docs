# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/allowed-domains.md

# Allowed Domains

This section explains the functionality of **Allowed** **Domains** and provides some related use cases to assist you in creating an optimal configuration. To access the **Allowed** **Domains**, go to **Company > Company Settings > Allowed Domains**.

## What is "Allowed Domains" used for?

To use our platform, **you must verify your domain** such as example.com. In order to use our products, we need to verify that the domain belongs to you/your company.

The components of the **Allowed** **Domains** page are:

<table><thead><tr><th width="143.5"></th><th></th></tr></thead><tbody><tr><td>Domain</td><td>Shows the defined domain information.</td></tr><tr><td>Status</td><td>Indicates the verification status of the domain.</td></tr><tr><td>Verification</td><td>The verification method used to verify domains.</td></tr><tr><td>Date Created</td><td>Shows the date the domain was added.</td></tr><tr><td>Last Check</td><td>Shows the date of the most recent verification check.</td></tr><tr><td>Date Verified</td><td>Indicates the verification date of the domain. If the domain is not verified, this field appears blank.</td></tr><tr><td>Actions</td><td><p>The column contains the below actions.</p><ul><li><strong>Verify Domain</strong>: You can see instructions and verify the domain.</li><li><strong>Delete:</strong> You can delete the domain if you no longer need to use it.</li><li><strong>Mark as Verified:</strong> You can verify the domain without using formal verification steps. This feature is only available to <strong>Reseller</strong> system admins.</li></ul></td></tr></tbody></table>

## How to add a new domain?

Go to **Company > Company Settings > Allowed Domains** from the main menu. Then follow the steps below.

* Click the **+ NEW** button to add a new domain
* Enter your **domain** in the label
* Copy your **TXT** **record** value to the clipboard
* Click the **SAVE** button on the bottom right corner
* Add the **TXT** **record** to your domain’s DNS settings respective of your **DNS host provider**:
  * **All DNS host providers** – Login to your domain’s DNS or web hosting provider, and then add the TXT records containing the values that you copied or saved previously. Different providers have different procedures for updating DNS records. See the DNS/Hosting provider table following these procedures.
* Click the **verify** button on the action column

The following table contains the most used DNS host providers and external links that might assist you in creating the DNS records on your DNS provider.

<table><thead><tr><th width="147.5"></th><th></th></tr></thead><tbody><tr><td>GoDaddy</td><td><a href="https://uk.godaddy.com/help/add-a-txt-record-19232"><strong>Add a TXT record</strong></a></td></tr><tr><td>DreamHost</td><td><a href="https://help.dreamhost.com/hc/en-us/articles/360035516812"><strong>Adding custom DNS records</strong></a></td></tr><tr><td>Cloudflare</td><td><a href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records"><strong>Manage DNS records</strong></a></td></tr><tr><td>HostGator</td><td><a href="https://mailazy.com/docs/guide/dns/hostgator/"><strong>Managing DNS</strong></a></td></tr><tr><td>Namecheap</td><td><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/"><strong>How do I add TXT/SPF/DKIM/DMARC records for my domain?</strong></a></td></tr><tr><td>Names.co.uk</td><td><a href="https://www.names.co.uk/support/articles/changing-your-domains-dns-settings/"><strong>Changing your domain’s DNS settings</strong></a></td></tr><tr><td>Wix</td><td><a href="https://support.wix.com/en/article/adding-or-updating-txt-records-in-your-wix-account"><strong>Adding or Updating TXT Records in Your Wix Account</strong></a></td></tr></tbody></table>

## Verify Domain

It may take up to 72 hours for changes to DNS settings to propagate on your DNS provider. If you have updated the domain registration but the verification was not successful, you can verify again later.

## FAQ

### Q: I added a domain, but verification failed. What should I do?

A: Please try the following steps.

* Make sure you have successfully created the DNS record.
  * TXT value must contain the “domain-verification” prefix.
  * Host/Name field must be “@” or your domain name like yourdomain.tld
* DNS changes may take up to 72 hours to propagate, so try verifying again later.

### Q: Can I create more than one Domain in the system?

A: Yes. The platform offers the flexibility to use several allowed domains.

### Q: What should I do if I don't have the DNS management of the domain that I want to verify?

A: You can contact the vendor or support team to ask for assistance with verification.
