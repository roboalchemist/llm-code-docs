# Source: https://www.courier.com/docs/external-integrations/email/smtp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SMTP

> Send emails via SMTP using Courier by including the recipient's email and customizing delivery using NodeMailer-compatible overrides—for message content (like attachments) or transport settings (host, port, auth credentials).

## Setup

Courier's SMTP integration uses [NodeMailer](https://nodemailer.com) under the hood. In Courier, navigate to the [SMTP Integration](https://app.courier.com/integrations/catalog/smtp) page and enter your SMTP host, username, password, and From Address, then click "Save." You can override these settings on a per-message basis using provider overrides.

<Info>
  Courier connects to your SMTP server from Courier's own IP addresses. If your server uses IP allowlisting, contact [Courier Support](mailto:support@courier.com) for the current list of egress IPs.
</Info>

## Profile Requirements

To deliver a message to a recipient over SMTP, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`:

```json icon="code" theme={null}
{
  "message": {
    "to": {
      "email": "recipient@example.com"
    }
    // ... rest of message definition
  }
}
```

## Overrides

You can override both the message content and SMTP transport configuration on a per-message basis using provider overrides in the Send API.

### Message Override

You can use a provider override to replace what we send to SMTP using NodeMailer. For example, you can add an attachment to your request:

```json icon="code" highlight={11-17} theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "smtp": {
        "override": {
          "body": {
            "attachments": [
              {
                "filename": "document.pdf",
                "content": "aGVsbG8gd29ybGQh",
                "encoding": "base64",
                "contentType": "application/pdf"
              }
            ]
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.smtp.override.body` will be merged with Courier's generated message and passed directly to NodeMailer. You can see all the available options by visiting the [NodeMailer message options documentation](https://nodemailer.com/message/).

### Transport Override

You may also override the [SMTP transport configuration](https://nodemailer.com/smtp) using values passed to `message.providers.smtp.override.config`. These settings will override your stored provider configuration for this specific message.

**Basic Example:**

```json icon="code" highlight={9-15} theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "smtp": {
        "override": {
          "config": {
            "auth": {
              "user": "username",
              "pass": "hunter2"
            },
            "host": "smtp.example.com",
            "secure": true,
            "port": 465
          }
        }
      }
    }
  }
}
```

**STARTTLS (port 587, recommended):**

```json icon="code" highlight={10-17} theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "smtp": {
        "override": {
          "config": {
            "host": "smtp.yourdomain.com",
            "port": 587,
            "secure": false,
            "requireTLS": true,
            "auth": {
              "user": "user@yourdomain.com",
              "pass": "your-password"
            }
          }
        }
      }
    }
  }
}
```

**Implicit TLS (port 465):**

```json icon="code" highlight={10-16} theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "smtp": {
        "override": {
          "config": {
            "host": "smtp.yourdomain.com",
            "port": 465,
            "secure": true,
            "auth": {
              "user": "user@yourdomain.com",
              "pass": "your-password"
            }
          }
        }
      }
    }
  }
}
```

**Common provider settings:**

| Provider              | Host                  | Port | secure | requireTLS |
| --------------------- | --------------------- | ---- | ------ | ---------- |
| Office 365            | `smtp.office365.com`  | 587  | false  | true       |
| Gmail (app password)  | `smtp.gmail.com`      | 587  | false  | true       |
| On-prem Exchange      | `mail.yourdomain.com` | 587  | false  | true       |
| Custom (implicit TLS) | varies                | 465  | true   | -          |

**Transport options reference:**

| Option              | Type    | Description                                                                       |
| ------------------- | ------- | --------------------------------------------------------------------------------- |
| `host`              | string  | SMTP server hostname                                                              |
| `port`              | number  | SMTP port (commonly 25, 465, 587)                                                 |
| `secure`            | boolean | Use SSL (true for port 465)                                                       |
| `requireTLS`        | boolean | Require STARTTLS (true for port 587)                                              |
| `auth`              | object  | Authentication credentials `{ user, pass }`                                       |
| `tls`               | object  | TLS options (see [NodeMailer TLS docs](https://nodemailer.com/smtp/#tls-options)) |
| `connectionTimeout` | number  | Connection timeout in milliseconds                                                |
| `socketTimeout`     | number  | Socket timeout in milliseconds                                                    |

**Available Options:** See the [NodeMailer SMTP transport documentation](https://nodemailer.com/smtp/) for all available `config` override options.

## Security Best Practices

<Note>
  * Use app-specific passwords for Office 365 and Gmail instead of regular account passwords.
  * Create dedicated service accounts for sending rather than using personal accounts.
  * Store credentials in Courier Studio rather than passing them in every API request.
  * Always use TLS: set `requireTLS: true` for port 587, `secure: true` for port 465.
  * For HIPAA or data residency requirements, use a direct connection to your on-premises SMTP server.
</Note>

## Troubleshooting

Courier verifies your SMTP connection before each send. If verification fails, the message is not sent and an error is returned. Connection timeouts (`ETIMEDOUT`) and temporary server unavailability are retried automatically.

<AccordionGroup>
  <Accordion title="Connection Timeouts">
    * Check that firewall rules allow outbound connections to your SMTP server
    * Verify the SMTP host and port are correct
    * Ensure your SMTP server is accessible from Courier's infrastructure
  </Accordion>

  <Accordion title="Authentication Failures">
    * Verify username and password are correct
    * For Office 365, ensure you're using an app-specific password if MFA is enabled
    * Check if your account has permission to send emails via SMTP
  </Accordion>

  <Accordion title="TLS/SSL Errors">
    * Verify your SMTP server supports the requested encryption method
    * Check certificate validity if using custom certificates
    * Ensure `secure` and `requireTLS` settings match your server configuration
  </Accordion>
</AccordionGroup>
