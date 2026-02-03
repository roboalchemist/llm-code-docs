# Source: https://resend.com/docs/send-with-retool-smtp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails using Retool with SMTP

> Learn how to integrate Retool with Resend SMTP.

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

## 2. Integrate with Retool SMTP

Log into your [Retool](https://retool.com) account and create a new SMTP Resource.

1. Go to **Resources** and click **Create New**

<img alt="Retool SMTP - Create new Resources" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-1.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c6edda6c2512e895bfec5b7e47627d96" data-og-width="3025" width="3025" data-og-height="1892" height="1892" data-path="images/retool-smtp-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-1.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=b81ff63bfdbf7936c5ab264e2af38451 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-1.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=7def2c6a0c5b37eb7dd975975ae1e313 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-1.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1d29434863b0e61e8cde6b3c3b27ddeb 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-1.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=cbdd47996188825d1878074aed3e8908 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-1.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=d26a4cb5a99846984e526a4153215497 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-1.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=bc0d60220f7700bb5380a7aeeba9eede 2500w" />

2. Search for **SMTP** and select it

<img alt="Retool SMTP - Search for SMTP" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-2.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=b95716d79754f6d2f8cedd6522d8e8f8" data-og-width="3025" width="3025" data-og-height="1891" height="1891" data-path="images/retool-smtp-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-2.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=d998af6e513bc8763a182094d9cc9af9 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-2.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=839481d79c8669a965eca472bc6f724c 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-2.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=f143239107f3ca8d50bde5c682f4b729 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-2.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=8bc98e797eab8853f7f8249bc8487b0e 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-2.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=2db7c2887f0debfd4b49538fb2c1cfa6 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-2.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c9e6b4f6b754fc952f6d5e1a699a1caf 2500w" />

3. Add name and SMTP credentials

<img alt="Retool SMTP - Add SMTP credentials" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-3.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=cbd6221e4b03dfc909f00f966afc4a2a" data-og-width="3025" width="3025" data-og-height="1892" height="1892" data-path="images/retool-smtp-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-3.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c665553c9963f9c7d7d7c0b2f4f941b0 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-3.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=314a64062c5d492d46da510bf3803fe6 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-3.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c65f64784fafd90efb7d01dd37c4ed5b 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-3.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=5571a320bfbbf608d98948f14b2f7d1d 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-3.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=5e624e1f2202d425e9f689e8010dc349 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/retool-smtp-3.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=bebb774022ea1650a66af0bdb436b9b4 2500w" />
