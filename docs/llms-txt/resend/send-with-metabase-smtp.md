# Source: https://resend.com/docs/send-with-metabase-smtp.md

# Send emails using Metabase with SMTP

> Learn how to integrate Metabase with Resend SMTP.

### Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Get the Resend SMTP credentials

When configuring your SMTP integration, you'll need to use the following credentials:

* **Host**: `smtp.resend.com`
* **Port**: `465`
* **Username**: `resend`
* **Password**: `YOUR_API_KEY`

## 2. Integrate with Metabase SMTP

After logging into your [Metabase Cloud](https://www.metabase.com/cloud/login) account, you’ll need to enable the SMTP integration.

1. From your Metabase Cloud Admin Panel, go to **Settings > Email** in the left menu. You should see the form below.

<img alt="Metabse Cloud SMTP" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-1.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=b11a45255f8f9058f03cebbd604eb4e5" data-og-width="1488" width="1488" data-og-height="1352" height="1352" data-path="images/metabase-smtp-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-1.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=52e44d8a6b355bd6d4f9073e565d9bd6 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-1.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=0092205568cb73595485f109514b9ab1 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-1.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=b883b10ee66006d11554b5ac1c8dc499 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-1.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=50ce85961e9dc5a6ad7910af18b8ca08 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-1.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=a7e7bc6f9a81978e06bdec9687132cb8 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-1.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=9af06df6027518e060c04d3f8a37ab47 2500w" />

2. Copy-and-paste the SMTP credentials from Resend to Metabase Cloud. Finally, click the **Save** button and all of your emails will be sent through Resend.

<img alt="Metabse Cloud SMTP" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-2.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=ca2550e6061a992cc3c9a345eacd4c39" data-og-width="3600" width="3600" data-og-height="2250" height="2250" data-path="images/metabase-smtp-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-2.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=b49b01b6110dbc62bf113f11d06c94ad 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-2.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=f8a40a0c63be85703c5621498efae4f2 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-2.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=a604f67aa691e23a42bf67fa57648b52 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-2.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=fa64c995ef817d701835967394bc167a 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-2.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=4fb560d82c8ede648b2b27b5aa37438f 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/metabase-smtp-2.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=5a4ed7aadf369ade8b7acf53fb4605bb 2500w" />
