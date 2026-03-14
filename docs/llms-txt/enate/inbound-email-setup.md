# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/setting-up-your-email-infrastucture/inbound-email-setup.md

# Inbound Email Setup

### Protocol Support

Enate can support the following protocols for incoming email:

* POP3/SPOP3
* IMAP4/IMAPS4
* GraphAPI (Office365)

POP3 and IMAP4 can be configured in Enate on any port, so firewall requirements are dependent upon the mail server team and their configuration of these protocols. When using POP3 and IMAP4, Enate requires that these use an external DNS name and have a publicly trusted certificate that matches on the DNS name.

For example, a POP3 server with the external DNS name pop3-mail.enate.net should have a publicly trusted certificate that either matches the full name pop3-mail.enate.net or should have a wildcard certificate for \*.enate.net. Enate requires certificates be publicly trusted and cannot accommodate internal DNS names or self-signed certificates. GraphAPI operates over HTTPS directly from Office365 and requires no additional ports to be open.&#x20;

{% hint style="info" %}
Note: There is some additional configuration to be done in Office365, which can be found [here](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/microsoft-office-365-email-integration-with-enate-via-graph-api-model).&#x20;
{% endhint %}

### Enate Message Handling

Regardless of the protocol that is used for incoming email, the behaviour is always the same within the mailbox: When Enate polls a mailbox to retrieve messages, these messages will be downloaded and processed by Enate and then be deleted from the mailbox.

### Mailbox Types

Email Integration is possible for Normal User Mailboxes as well as Shared Mailboxes. Since the Shared Mailbox doesn’t have a password but an account with permissions to access the shared mailbox, when configuring your Connector you should first enter the username and password for the primary account via which you can access the shared mailbox, then you set the 'Access Another Mailbox' option to ON, and provide the name of the shared mailbox to be used.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Miugtww3EA80WPDsZu_%2F-Miul501gI-OlQ3mhGx-%2Fimage.png?alt=media\&token=60211396-8602-490d-82e8-03e3a1079082)

### Aliasing and Forwarding

#### Aliases

Enate can support multiple aliases on a single mailbox to simplify the configuration and number of accounts required on the mail server side.

Enate mailbox matching logic is always performed on the "To" address received in the message body that was downloaded from the server. Depending on the mail server in use this can present issues when handling email internally for the same domain as the mailbox that Enate connects to. Exchange Server and Office365 will modify the "To" field to be the Primary SMTP address configured for the receiving mailbox if the email has been sent within the same domain. This can cause issues with email routes not correctly matching.

**Example:**

If <enate.sales@example.com> were configured as an alias of <enate.production@example.com> another user sending to <enate.sales@example.com> from an @example.com email address would result in the "To" field within Enate appearing as <enate.production@example.com> rather than the <enate.sales@example.com> address the email was sent to.

#### Forwarding

Forwarding between different mailboxes is sometimes used to achieve an archive of emails processed within Enate. These can be done successfully in most systems however care should be taken to avoid modification to the "To" field. This behaviour is typically highly specific to individual mail systems depending on how it is being done and so should be tested as to avoid affecting email messages.
