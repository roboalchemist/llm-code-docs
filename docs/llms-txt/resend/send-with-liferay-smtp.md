# Source: https://resend.com/docs/send-with-liferay-smtp.md

# Send emails using Liferay with SMTP

> Learn how to integrate Liferay with Resend SMTP.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Get the Resend SMTP credentials

When configuring your SMTP integration, you'll need to use the following credentials:

* **Host**: `smtp.resend.com`
* **Port**: `465`
* **Username**: `resend`
* **Password**: `YOUR_API_KEY`

## 2. Integrate with Liferay

After logging into your Liferay instance as the admin user, you'll need to enable the SMTP integration.

1. Navigate to **Control Panel** → **Server Administration** → **Mail**.

<img alt="Liferay - SMTP" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/liferay-smtp-1.jpg?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=94e43af6a43bc9fa8ce8cc486eeb4f05" data-og-width="1600" width="1600" data-og-height="865" height="865" data-path="images/liferay-smtp-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/liferay-smtp-1.jpg?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=9995edfac8b98dc11358bc33e11c73f9 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/liferay-smtp-1.jpg?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=db2e237220df2531b1385e006c3eba8e 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/liferay-smtp-1.jpg?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=ad816fc70adf3b3d0654063565f12826 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/liferay-smtp-1.jpg?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=209fb4bba0fb7f3fa5a83f5f776c3197 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/liferay-smtp-1.jpg?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=dfb738e79143296b153b83955c632d63 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/liferay-smtp-1.jpg?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=99ffcafc285c62d6450d43256fdeb12d 2500w" />

2. Copy-and-paste the SMTP credentials from Resend to Liferay.

* **Outgoing SMTP Server**: `smtp.resend.com`
* **Outgoing Port**: `465`
* **Enable StartTLS**: `True`
* **User Name**: `resend`
* **Password**: `YOUR_API_KEY`

Make sure to replace `YOUR_API_KEY` with an existing key or create a new [API Key](https://resend.com/api-keys).

For the additional JavaMail properties, you can use:

```
mail.smtp.auth=true
mail.smtp.starttls.enable=true
mail.smtp.starttls.required=true
```
