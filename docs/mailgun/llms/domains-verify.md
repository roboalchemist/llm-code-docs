# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/domains/domains-verify.md

# Domain Verification

![verifydomain](/assets/mailgunsendverify.4a4aa76ee8b52d005794cf5f4392627c00f8ad17c205a7fdb850171cde0eb732.05e97c23.png)

### Five reasons why you need to verify your domain:

- To prove you are an authorized sender for the domain
- Verified domains are not subject to a sending limit of 300 emails per day
- No more "sent via Mailgun.org" message in your emails
- Establishes a positive email reputation for your own domain
- Mailgun is less suspicious of traffic that is being sent on verified domains and that reduces the likelihood of being disabled


The basic steps to verify a domain are:

1. Get the DNS records (Via [API](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domains/get-v4-domains--name-) or Control Panel)
2. Open your DNS provider and add the provided DNS records:


| Type | Required | Purpose | Value |
|  --- | --- | --- | --- |
| TXT | â | SPF (Sender Policy Framework): Sending server IP validation. This is used by most email providers. | v=spf1 include:mailgun.org ~all |
| TXT | â | DKIM (DomainKeys Identified Email): Like SPF, but uses cryptographic validation. | *Find this record in the "Domain Verification & DNS" section of the Mailgun control panel for your domain.* |
| CNAME | â | Required for Mailgun to track clicks, opens, and unsubscribes. | mailgun.org |
| MX | â | Required for Mailgun to receive and route/store messages addressed to the domain. | 10 mxa.mailgun.org   10 mxb.mailgun.org |


Once you've added the supplied records, and they've propagated over the internet (can take 24-48 hours for DNS changes to fully propagate), your domain is now able to be verified.

1. You can either wait for Mailgun's system to check the domain and automatically verify it for you, or if you don't want to wait you can click Verify DNS settings in the Domain Settings section of the Control Panel, or call the [Verify API](/docs/mailgun/api-reference/send/mailgun/domains/put-v4-domains--name--verify)


Verified domains will show up on the Mailgun Control Panel with a green Verified badge next to it!

For more information and help related to verifying domains check out these articles:

-  How Do I Verify My Domain? and Other DNS Question
-  Domain Verification Walkthrough


## Common DNS Providers Documentation

If you'd like more detailed instructions on how to add DNS records for your domain, please refer to the documentation provided by your DNS provider. Below is a list of common DNS providers and links to their documentation:

| Provider | Link to Documentation |
|  --- | --- |
| Go Daddy | [MX](https://www.godaddy.com/help/add-an-mx-record-19234)[CNAME](https://www.godaddy.com/help/add-a-cname-record-19236)[TXT](https://www.godaddy.com/help/add-a-txt-record-19232) |
| NameCheap | [All Records](https://www.namecheap.com/support/knowledgebase/subcategory/10/dns-questions/) |
| Network Solutions | MXCNAMETXT |
| Rackspace Email & Apps | [All Records](https://status.apps.rackspace.com/) |
| Rackspace Cloud DNS | [Developers Guide](https://docs.rackspace.com/support/how-to/set-up-dns-records-for-cloud-office-email/) |
| Amazon Route 53 | [Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/setting-up-route-53.html) |