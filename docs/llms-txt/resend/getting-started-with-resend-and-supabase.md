# Source: https://resend.com/docs/knowledge-base/getting-started-with-resend-and-supabase.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Started with Resend and Supabase

> A quick jumpstart to using Resend with Supabase.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

In this guide, we'll help you get started with Resend by:

* [Setting up Resend](#set-up-resend)
* [Send Auth Emails with Resend](#send-auth-emails-with-resend)
* [Send Emails with Supabase Edge Functions](#send-emails-with-supabase-edge-functions)

## Set up Resend

In order to send emails with your Supabase project, you'll need to first verify it in Resend.

Go to [the Domains page](https://resend.com/domains) and click on **Add Domain**.

1. Add your domain name (we recommend [using a subdomain](/knowledge-base/is-it-better-to-send-emails-from-a-subdomain-or-the-root-domain) like `updates.yourdomain.com`).
2. Add the DNS records to your DNS provider ([learn more about these records](/dashboard/domains/introduction)).
   <img alt="Resend Domains page" src="https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-domain-records.png?fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=24107151c9a59db661aca80c64338bfe" data-og-width="3024" width="3024" data-og-height="1900" height="1900" data-path="images/resend-domain-records.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-domain-records.png?w=280&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=494bd8f2e3988262742123605557c4d2 280w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-domain-records.png?w=560&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=aeb758a2f85e189c3dec2cb05b1b7c5e 560w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-domain-records.png?w=840&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=22696e3745cea9ed7387ef0aeebf6a09 840w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-domain-records.png?w=1100&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=d37b814b1652b485f40739eea0067b41 1100w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-domain-records.png?w=1650&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=b3c8b8823e08b00dded6ed56abfc66c9 1650w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-domain-records.png?w=2500&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=8789945dd406f89e110fcbfa02c1af83 2500w" />
3. Click on **I've added the records** to begin the verification process.
4. Wait for the verification to complete (usually takes 5–10 minutes)

<Info>
  Resend requires you own your domain (i.e., not a shared or public domain).
  Adding DNS records gives Resend the authority to send emails on your behalf
  and signals to the inbox providers that you're a legitimate sender.
</Info>

## Send Auth Emails with Resend

If you want to use Resend to send your Supabase Auth Emails, you have three options:

1. [Using the Resend Integration](#1-using-the-resend-integration): simplest, but less customizable email templates.
2. [Custom Auth Functions](#2-custom-auth-functions): more customizable email templates, but requires more setup.
3. [Self-hosted with Custom SMTP](#3-self-hosted-with-custom-smtp): only for those self-hosting Supabase.

### 1. Using the Resend Integration

Resend includes a pre-built integration with Supabase. Connecting Resend as your email provider will allow you to send your Supabase emails (i.e., password resets, email confirmations, etc.) through Resend.

<YouTube id="BkfDsGMgutk" />

1. Open the [Resend Integrations settings](https://resend.com/settings/integrations).
2. Click **Connect to Supabase** and login to your Supabase account if prompted.
   <img alt="Resend Integrations settings" src="https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-integrations-settings.png?fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=b954067bfb28d84f7d8201e05a449815" data-og-width="3024" width="3024" data-og-height="1900" height="1900" data-path="images/resend-integrations-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-integrations-settings.png?w=280&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=dc879740c1c252f05c90ebacb1cfbe03 280w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-integrations-settings.png?w=560&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=68c4e690d112c1281fb48fb05144b792 560w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-integrations-settings.png?w=840&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=c29f811c5a4fe0fa6c3faf0964a9cac1 840w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-integrations-settings.png?w=1100&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=9c3e49182d484413e4d11dcf8b66a589 1100w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-integrations-settings.png?w=1650&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=63bc8fc8295c213c29f73fe46afd9503 1650w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-integrations-settings.png?w=2500&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=c6ebebcefd3325c86f321bcea5bb4f6e 2500w" />
3. Select a project and click **Select Project**, then select your domain and click **Add API Key**. Resend will create an API key for you. Add a sender name and click **Configure SMTP Integration**.
   <img alt="Resend Integrations settings" src="https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-smtp.png?fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=e744247952bc105d6083babcc315b0a6" data-og-width="3024" width="3024" data-og-height="1900" height="1900" data-path="images/resend-supabase-setup-smtp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-smtp.png?w=280&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=a9ed6d9b5a48b3d76ed833f422908d95 280w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-smtp.png?w=560&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=a342e9288151a034f6b978b63f31657d 560w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-smtp.png?w=840&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=73dc45519ae0cfb457b3ba8fd30dbe03 840w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-smtp.png?w=1100&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=96c7b7f3db29e6b8a50a04fe97e7628a 1100w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-smtp.png?w=1650&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=8cefd2108d3d83bd10109fd50139587c 1650w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-smtp.png?w=2500&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=55fedf18ee6f5cec8a4c55912b4fb404 2500w" />

Click on **Supabase Dashboard** to confirm the integration.

<img alt="Resend Integrations settings" src="https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-confirm.png?fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=d72c13ba50f60530587107b6d7040223" data-og-width="1360" width="1360" data-og-height="150" height="150" data-path="images/resend-supabase-setup-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-confirm.png?w=280&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=7d2f46b10b7ea9ae5d11818ad5aa123f 280w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-confirm.png?w=560&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=f1cfde776e0c2b220eff47e59f49a1e6 560w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-confirm.png?w=840&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=503a094bfe2d85e61d591a5b9ce1776d 840w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-confirm.png?w=1100&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=98cbe2a79e9445c5efd3d26f4d4bf2f2 1100w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-confirm.png?w=1650&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=77b924261ff326c430e9dd7e5ec5e0b0 1650w, https://mintcdn.com/resend/_kGPo-rF0-rO9nI4/images/resend-supabase-setup-confirm.png?w=2500&fit=max&auto=format&n=_kGPo-rF0-rO9nI4&q=85&s=e7d74110ef6a1e9554e1cce5ecd89d80 2500w" />

<Info>
  Supabase has a rate limit on the number of emails you can send per hour and
  requires you to [connect a custom email provider for more than 2
  emails/hour](https://supabase.com/docs/guides/auth/rate-limits). Once you set
  Resend as your email provider, you can send additional emails (by default, 25
  emails/hour, although you can change the rate limit in your project's
  [authentication
  settings](https://supabase.com/docs/guides/deployment/going-into-prod#rate-limiting-resource-allocation--abuse-prevention)).
</Info>

### 2. Custom Auth Functions

Benefit of using custom auth functions:

* More control over the email sending process since you control the sending function.
* More control over the email template using React Email or Resend Templates.

Note that this requires enabling [Supabase Auth Hooks](https://supabase.com/docs/guides/auth/auth-hooks).

<YouTube id="tB_HcKjW8fQ" />

<Card title="Supabase Auth Hooks with Resend Templates" icon="arrow-up-right-from-square" href="https://github.com/resend/supabase-auth-hooks-with-resend-templates">
  See the full source code.
</Card>

### 3. Self-hosted with Custom SMTP

If you're self-hosting Supabase, you can use a custom SMTP server to send your emails. [Learn more here](/send-with-smtp).

## Send Emails with Supabase Edge Functions

If you're using Supabase Edge Functions, you can add email sending to your function by using the Resend Node.js SDK. You can use these functions for Auth Emails ([as shown above](#2-custom-auth-functions)) or for other emails (e.g., app notifications, account activity, etc.).

First, make sure you have the latest version of the [Supabase CLI](https://supabase.com/docs/guides/cli#installation) installed.

### 1. Create Supabase function

Create a new function locally:

```bash  theme={"theme":{"light":"github-light","dark":"vesper"}}
supabase functions new resend
```

### 2. Edit the handler function

Paste the following code into the `index.ts` file:

```js index.ts theme={"theme":{"light":"github-light","dark":"vesper"}}
import { serve } from "https://deno.land/std@0.168.0/http/server.ts";

const RESEND_API_KEY = 're_xxxxxxxxx';

const handler = async (_request: Request): Promise<Response> => {
    const res = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${RESEND_API_KEY}`
        },
        body: JSON.stringify({
            from: 'Acme <onboarding@resend.dev>',
            to: ['delivered@resend.dev'],
            subject: 'hello world',
            html: '<strong>it works!</strong>',
        })
    });

    const data = await res.json();

    return new Response(JSON.stringify(data), {
        status: 200,
        headers: {
            'Content-Type': 'application/json',
        },
    });
};

serve(handler);
```

### 3. Deploy and send email

Run function locally:

```bash  theme={"theme":{"light":"github-light","dark":"vesper"}}
supabase functions start
supabase functions serve resend --no-verify-jwt
```

Deploy function to Supabase:

```bash  theme={"theme":{"light":"github-light","dark":"vesper"}}
supabase functions deploy resend
```

Open the endpoint URL to send an email:

<img alt="Supabase Edge Functions - Deploy Function" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e28cab375d10a57f712e77ff3c888005" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/supabase-edge-functions-deploy-function.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=5ad81866f4e061b55ade5b508e8b6941 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e26ee1713f03952db5111effdd2bee4a 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=df3d94fc69f5764d13153e217e7c2982 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=d674b6064fa96011569a892cf4e9d683 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1907d607d324c5005966a03032ce5a1d 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=334c2321da6997bfdec12187653396ee 2500w" />

### 4. Try it yourself

<Card title="Supabase Edge Functions Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-supabase-edge-functions-example">
  See the full source code.
</Card>

## Happy sending!

If you have any questions, please let us know at [support@resend.com](mailto:support@resend.com).
