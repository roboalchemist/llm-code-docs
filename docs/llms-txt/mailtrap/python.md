# Source: https://docs.mailtrap.io/guides/sdk/python.md

# Python

<a href="https://github.com/mailtrap/mailtrap-python" class="button primary">Mailtrap Python SDK on GitHub</a>

### Overview

Mailtrap can be integrated with Python apps and projects for email sending purposes.

### Email API/SMTP for Python

#### SDK Integration

The [Mailtrap Python SDK](https://github.com/mailtrap/mailtrap-python) is a Pythonic library for sending transactional and bulk emails with full type hints support. The SDK supports:

* Transactional email sending
* Batch email sending
* Template management
* Contact management
* Sandbox testing
* Account management
* Type hints for better IDE support

### Installation

Install the SDK using pip:

{% code title="pip" %}

```bash
pip install mailtrap
```

{% endcode %}

### Minimal Example

Here's a minimal example to send your first email:

{% code title="send\_email.py" %}

```python
import mailtrap as mt

API_TOKEN = "<YOUR_API_TOKEN>"  # your API key here https://mailtrap.io/api-tokens

client = mt.MailtrapClient(token=API_TOKEN)

# Create mail object
mail = mt.Mail(
    sender=mt.Address(email="sender@example.com", name="John Smith"),
    to=[mt.Address(email="recipient@example.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
)

client.send(mail)
```

{% endcode %}

{% hint style="info" %}
Get your API token from your Mailtrap account under **Settings → API Tokens**.
{% endhint %}

#### SMTP Integration

To integrate SMTP with your Python app, navigate to the **Integrations** tab, choose the desired Python framework, and copy-paste the credentials or ready-made code snippets.

{% hint style="info" %}
SMTP integration is compatible with any Python framework or library that sends emails using SMTP.
{% endhint %}

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-424e66e21f0e3d1480887fab6b411cbe8faf92ba%2Fmailtrap-python-smtp-integration.png?alt=media" alt=""></div>

For more information read the [SMTP Integration article](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/smtp-integration).

#### RESTful API Integration

To integrate Mailtrap using RESTful API, use the configuration available among **Code samples** under the API section.

API integration can be used with any Python framework or library that supports HTTP requests. For more details, refer to the [API documentation](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/5tjdeg9545058-mailtrap-api).

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-87a9d5c126fc6cb857dd1905d7a48bfc17b3ffed%2Fmailtrap-python-api-integration.png?alt=media" alt=""></div>

Read more about API integration in the [dedicated article](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/api-integration).
