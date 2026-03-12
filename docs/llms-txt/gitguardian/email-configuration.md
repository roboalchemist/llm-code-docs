# Source: https://docs.gitguardian.com/self-hosting/management/application-management/email-configuration.md

# Configure the email system

> Configure SMTP email settings for GitGuardian self-hosted to enable notification delivery.

In order to receive alerts from your GitGuardian instance, you need to setup an email sending system.

You can either pick a classic SMTP configuration or use [SendGrid](https://sendgrid.com/).

1. Go to the Admin area of ââyour GitGuardian instance. You must be an admin to access it.
   ![Admin area CTA](/img/self-hosting/management/application-management/admin_area_cta.png)
2. Navigate to Settings > Email > Configuration

### SMTP Configuration

You need to fill in the following information:

- Server Host
- Server Port
- Username
- Password
- SSL activation

![Email configuration SMTP](/img/self-hosting/management/application-management/email_configuration_smtp.png)

:::info
For SMTP server with a self-signed certificate, add it to the trusted list to ensure communication (refer to **[custom CA](../../security/custom-ca.md)**). The DNS name must match the certificate's name.

Alternatively, starting **2024.2.1** release, you can enable bypassing TLS verification for the SMTP server by executing the following command:

```bash
kubectl exec --namespace <namespace> deployments/webapp-internal-api -c app -- python manage.py set_preferences --email__is_bypass_tls_smtp_enabled=True
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).
:::

### SendGrid

A SendGrid API key in necessary to send emails with SendGrid. You need to generate one from the [SendGrid Website](https://app.sendgrid.com/settings/api_keys).

![Email configuration Sendgrid](/img/self-hosting/management/application-management/email_configuration_sendgrid.png)

### Checking your configuration

Once you have picked a method and saved your configuration, you can test it by pressing the `Send test email` button.

Shortly after that, you will receive an email on the address you used to set up your GitGuardian instance.
If you did not receive any mail, check the app logs for any errors and reach out to us.
