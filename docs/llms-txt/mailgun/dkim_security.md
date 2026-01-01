# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/domains/dkim_security.md

# DKIM Security

DKIM (DomainKeys Identified Mail) security involves regularly updating the cryptographic keys used for signing emails to maintain security and protect against key compromise. Like passwords, your DKIM key is vulnerable to compromise. Best practices recommend rotating your DKIM key at least every 6 months and immediately if your key is compromised.

When you set up an authenticated domain, Mailgun provides two methods for key rotation:

- **Automatic rotation** using Mailgun's Automatic Sender Security feature
- **Manual rotation** on your preferred schedule


## Automatic Sender Security

Mailgun's Automatic Sender Security feature simplifies email authentication by handling the technical setup and configuration automatically. This eliminates the need for manual key generation and DNS record adjustments, reducing errors and ensuring proper email authentication.

### How CNAME Records Enable Automated Key Management

The feature works by adding two CNAME records to your domain's DNS settings. A CNAME (Canonical Name) record creates an alias that points from your domain to another location. Instead of storing the actual DKIM public key directly in your DNS as a TXT record, the CNAME records point to Mailgun's infrastructure where the keys are hosted.

This delegation is what enables Mailgun to manage your DKIM keys automatically. When an email provider needs to verify your email signature, it queries your domain's DNS for the DKIM public key. The CNAME record redirects this query to Mailgun's servers, which return the current active public key. Because the key is hosted on Mailgun's infrastructure rather than directly in your DNS, Mailgun can update and rotate the keys without requiring any action from you.

When rotation occurs, Mailgun generates a new key pair and updates the public key on their servers. Because your DNS simply points to Mailgun's location via the CNAME record, the change takes effect immediately without any DNS updates on your end. This seamless process ensures continuous email authentication while maintaining the highest security standards through regular key rotation.

### DNS Configuration

The host or name you provide to your DNS provider will look similar to `pdk1._domainkey.my.domain.com` and `pdk2._domainkey.my.domain.com`, while the target pointing back to Mailgun will resemble `pdk1._domainkey.9d876.dkim1.mailgun.com` and `pdk2._domainkey.9d876.dkim1.mailgun.com`.

Two CNAME records are used to enable smooth key transitions during rotation. This dual key approach allows Mailgun to introduce a new key while the old key remains active, ensuring there's no interruption in email authentication. Email providers may cache DNS records, so having both keys active during the transition period ensures that emails are successfully verified regardless of which key information a receiving server has cached. Once the new key is fully propagated and the old key is no longer needed, the system maintains two active keys ready for the next rotation cycle.

Automatic Sender Security generates two 2048 bit DKIM selector records via TXT records, which are automatically rotated every 120 days by default. You can adjust the rotation period as needed. The minimum interval for rotation is 5 days.

### New Sending Domains

When adding a new domain, you will have the option to enable Automatic Sender Security during the setup process.

### Existing Sending Domains

If you have an existing sending domain currently utilizing DKIM via a TXT record and wish to switch to Automatic Sender Security, you can do so from the DNS records page in the Mailgun application.

## Manual DKIM Rotation

You have the option to manually rotate your DKIM keys on your own schedule. Mailgun supports signing messages with up to 3 DKIM keys. When multiple active keys are present on a sending domain, we use a round robin method to determine which key signs each message.

There are two methods for adding a new DKIM key. In both cases, you must choose a unique selector (unique to the sending domain):

- **Allow Mailgun to generate a DKIM key** (most common method)
- **Import an existing key** via a valid PEM file (advanced method)


### Allowing Mailgun to Generate the DKIM Key

You can choose to allow Mailgun to generate the DKIM key. Most users select this method. You can choose the DKIM key length: either 1024 bit or 2048 bit. The 2048 bit option is more secure but can be more complex to set up because the record length is significantly longer, and some DNS providers require you to split the record into two parts.

When rotating keys or upgrading from a 1024 bit key to a 2048 bit key, we recommend sending a test message to yourself to verify that messages are being signed with the new key. You may need to send several test messages before confirming. Once verified, you can delete the old key.

## Additional Resources

Learn more about [DKIM key rotation](https://help.mailgun.com/hc/en-us/articles/16956951504539)

View our [Domain Security API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/openapi-final/tag/DKIM-Security/)

View our [Domain Keys API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/openapi-final/tag/Domain-Keys/)