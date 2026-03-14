# Source: https://docs.mailtrap.io/account-and-organization/billing/setup.md

# Source: https://docs.mailtrap.io/email-sandbox/setup.md

# Source: https://docs.mailtrap.io/email-api-smtp/setup.md

# Setup & Configuration

Complete guide to setting up and configuring Mailtrap Email API/SMTP for your application. Follow these steps to start sending emails in production.

### Quick start checklist

Get up and running with this essential setup checklist:

* [ ] Create your Mailtrap account
* [ ] Verify your sending domain
* [ ] Choose integration method (API or SMTP)
* [ ] Configure authentication
* [ ] Send your first email

### Configuration steps

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Sending Domain Setup</strong></td><td><em>the foundation of email delivery. Verify your domain ownership and configure authentication records (SPF, DKIM, DMARC) for optimal deliverability.</em></td><td><a href="setup/sending-domain">sending-domain</a></td></tr><tr><td><strong>API Integration</strong></td><td><em>modern RESTful API for programmatic email sending. Best for new applications and microservices architecture.</em></td><td><a href="setup/api-integration">api-integration</a></td></tr><tr><td><strong>SMTP Integration</strong></td><td><em>traditional SMTP protocol for universal compatibility. Works with any email library or legacy system.</em></td><td><a href="setup/smtp-integration">smtp-integration</a></td></tr><tr><td><strong>Dedicated IP</strong></td><td><em>gradually build your sending reputation. Essential for high-volume senders and dedicated IPs.</em></td><td><a href="deliverability/ip-warmup">ip-warmup</a></td></tr></tbody></table>

### Choose your integration method

#### When to use API

**Best for:**

* Modern web applications
* Microservices architecture
* Cloud-native applications
* Real-time sending needs
* Advanced analytics requirements

**Advantages:**

* Faster performance
* Better error handling
* Detailed response data
* Webhook support
* Easier debugging

**Example:**

```bash
curl -X POST "https://send.api.mailtrap.io/api/send" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "from": {"email": "hello@example.com"},
    "to": [{"email": "user@example.com"}],
    "subject": "Test Email",
    "text": "This is a test email"
  }'
```

#### When to use SMTP

**Best for:**

* Legacy applications
* Email clients
* CMS platforms
* Standard libraries
* Minimal code changes

**Advantages:**

* Universal compatibility
* No code changes required
* Works with any language
* Familiar protocol
* Easy migration
