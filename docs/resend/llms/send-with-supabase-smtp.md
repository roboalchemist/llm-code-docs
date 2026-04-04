# Source: https://resend.com/docs/send-with-supabase-smtp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails using Supabase with SMTP

> Learn how to integrate Supabase Auth with Resend SMTP.

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

## 2. Integrate with Supabase SMTP

After logging into your Supabase account, you'll need to enable the SMTP integration.

1. Go to your Supabase project
2. Click on **Project Settings** in the left sidebar
3. Select the **Authentication** tab
4. Find the SMTP section and toggle the **Enable Custom SMTP** option
5. Add your Sender email and name (these are required fields). For example: `support@acme.com` and `ACME Support`.

<img alt="Supabase Auth - SMTP Sender email and name settings" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-sender-email-name.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1db59a322b21efb38bc298a5796d32b3" data-og-width="2080" width="2080" data-og-height="618" height="618" data-path="images/supabase-auth-smtp-sender-email-name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-sender-email-name.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=2e34806461bbb2538976e11b22abfab6 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-sender-email-name.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=a7d329ae9f31e92890088acb9a09c697 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-sender-email-name.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=5c917b24f62b074f0b557905cb428bdf 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-sender-email-name.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=6a4d7d5cc37e6e38142c54ed34976f55 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-sender-email-name.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=af95b5a5e788f1d2e9108c2c1842e6f2 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-sender-email-name.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c93aefe9daf3abb6a56cddf790437958 2500w" />

6. You can copy-and-paste the [SMTP credentials](https://resend.com/settings/smtp) from Resend to Supabase.

<img alt="Supabase Auth - SMTP Settings" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-settings.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=70c068d96e4f03c7e2f03b6e71219d4f" data-og-width="2076" width="2076" data-og-height="1536" height="1536" data-path="images/supabase-auth-smtp-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-settings.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=465dbfc732418be3aeafe1ecb3f70c60 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-settings.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=67bc5c6b4d7aa2ae1c6010c294d7fc36 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-settings.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=a2fd51db77a16bd81d5c29498906c813 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-settings.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c83fed224cbda52c16d0e5ee74fa8494 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-settings.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=666714885dfb48bbc1ccf7d175f8a468 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-auth-smtp-settings.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=755196fc8e36cf108db49b9f4d085080 2500w" />

After that, you can click the **Save** button and all of your emails will be sent through Resend.
