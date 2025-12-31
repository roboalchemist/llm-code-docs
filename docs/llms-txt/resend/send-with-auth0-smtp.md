# Source: https://resend.com/docs/send-with-auth0-smtp.md

# Send emails using Auth0 with SMTP

> Learn how to integrate Auth0 with Resend SMTP.

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

## 2. Integrate with Auth0 SMTP

After logging into your [Auth0](https://auth0.com/) dashboard, you'll need to enable the SMTP integration.

1. From your Auth0 dashboard, go to [Branding > Email Provider](https://manage.auth0.com/#/templates/provider).
2. Enable the **Use my own email provider** toggle.
3. Select **SMTP Provider**.
4. Enter a **From** email address, and then enter the Resend SMTP server's **Host**, **Port**, **Username**, and your API key as the **Password**.

<img alt="Auth0 SMTP - Email Provider Settings" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/auth0-smtp.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=91d6c2472ae892f200787d35a3568533" data-og-width="1986" width="1986" data-og-height="2272" height="2272" data-path="images/auth0-smtp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/auth0-smtp.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=2515e6f7fc862f21549ff5f6a1f5ed5a 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/auth0-smtp.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=bee7cd1b8c96adb62a33b9b5691f4455 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/auth0-smtp.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=7e7d5041b4acf156c41733bac84bdc73 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/auth0-smtp.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=e4da247ed09adcfbcd7171762fd79e26 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/auth0-smtp.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=e8bcd9213be903f896c65d255e11e7df 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/auth0-smtp.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=2feffb26f8bcfe4993db877c337f83d4 2500w" />

## 3. Send a test email

Once you have configured the SMTP settings, click **Save**. Next send a test email using the **Send Test Email** button. If everything is configured correctly, you will receive a confirmation email. If you did not receive an email, check your [Auth0 Logs](https://manage.auth0.com/#/logs).
