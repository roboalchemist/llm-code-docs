# Source: https://resend.com/docs/send-with-wordpress-smtp.md

# Send emails using WordPress with SMTP

> Learn how to send your first email using Wordpress.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install a plugin

First, you'll need to install and activate the [WP Mail SMTP](https://wordpress.org/plugins/wp-mail-smtp/) plugin. Once the plugin is activated you will see the setup wizard. You can skip this step as we'll guide you through how to configure the plugin for Resend. Just click on **Go to the Dashboard** at the bottom of the screen to exit the setup wizard.

<img alt="WP Mail SMTP - Setup Wizard" src="https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-setup-wizard.png?fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=034e82ed82a43c1cc25e9119995ac558" data-og-width="2880" width="2880" data-og-height="1462" height="1462" data-path="images/wordpress-setup-wizard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-setup-wizard.png?w=280&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=6b3e5d61f920bcee0f6935f6f762730e 280w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-setup-wizard.png?w=560&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=86da0fb49fbc2fa225a25b332f44255b 560w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-setup-wizard.png?w=840&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=d1fd29774b3f7d793b1e4a14ccd84e59 840w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-setup-wizard.png?w=1100&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=0a52661387ca6787f7b8933a68d9d470 1100w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-setup-wizard.png?w=1650&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=05b6d3c49f842c966fac12f2e50d9581 1650w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-setup-wizard.png?w=2500&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=b80e84913e35bc7460343a41e4a62399 2500w" />

## 2. Configuration

From your admin dashboard, visit the **WP Mail SMTP > Settings** page to configure the plugin. Firstly, configure your **From Email**, **From Name**, and **Return Path**. Next, we'll configure the SMTP settings for Resend. Select **Other SMTP** in the **Mailer** section.

<img alt="WP Mail SMTP - Settings" src="https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-configure.png?fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=12cb502dcffbc76cad7f6bbef00a7f43" data-og-width="2880" width="2880" data-og-height="1462" height="1462" data-path="images/wordpress-configure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-configure.png?w=280&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=501e4b9c2ecdafcb5d45de3c5475ba35 280w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-configure.png?w=560&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=56784d22779a54e5baadf1872acac90c 560w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-configure.png?w=840&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=3c5db16a12a39a94990c0be53a1c5f9d 840w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-configure.png?w=1100&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=fd4b2c0c06678f81bf5fdda1084f65dc 1100w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-configure.png?w=1650&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=939eb356981246d7f83e4cd0da5a8793 1650w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-configure.png?w=2500&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=f2debaa483536161ffbd7ce35914f2e3 2500w" />

In the **Other SMTP** section, configure the following settings:

* **SMTP Host**: `smtp.resend.com`
* **Encryption**: `SSL`
* **SMTP Port**: `465`
* **Auto TLS**: `ON`
* **Authentication**: `ON`
* **SMTP Username**: `resend`
* **SMTP Password**: `YOUR_API_KEY`

Make sure to replace `YOUR_API_KEY` with an existing key or create a new [API Key](https://resend.com/api-keys).

## 3. Sending a test email

From your admin dashboard, visit the **WP Mail SMTP > Tools** page to send a test email.

<img alt="WP Mail SMTP - Send a Test Email" src="https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-test-email.png?fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=bffb755f5673f14a03d84d36a4b361ca" data-og-width="2880" width="2880" data-og-height="1462" height="1462" data-path="images/wordpress-test-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-test-email.png?w=280&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=b6174c2d84f53d9d1f6e3b4002bf9304 280w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-test-email.png?w=560&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=ba4322c50484c467bf17cc7c20449580 560w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-test-email.png?w=840&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=47856c68dcec0393db239a3ce473ff25 840w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-test-email.png?w=1100&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=98b16e71a85dcbf01c7cec285bc2a65b 1100w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-test-email.png?w=1650&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=aa09d93ae06d5c635f58b7d73ebb8d5d 1650w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/wordpress-test-email.png?w=2500&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=78af8a485bc4f82848621c36391619b3 2500w" />
