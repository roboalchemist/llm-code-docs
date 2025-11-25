# Source: https://resend.com/docs/send-with-supabase-edge-functions.md

# Send emails with Supabase Edge Functions

> Learn how to send your first email using Supabase Edge Functions.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

Make sure you have the latest version of the [Supabase CLI](https://supabase.com/docs/guides/cli#installation) installed.

## 1. Create Supabase function

Create a new function locally:

```bash  theme={null}
supabase functions new resend
```

## 2. Edit the handler function

Paste the following code into the `index.ts` file:

```ts index.ts theme={null}
const RESEND_API_KEY = Deno.env.get('RESEND_API_KEY');

const handler = async (_request: Request): Promise<Response> => {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${RESEND_API_KEY}`,
    },
    body: JSON.stringify({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'hello world',
      html: '<strong>it works!</strong>',
    }),
  });

  const data = await res.json();

  return new Response(JSON.stringify(data), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
    },
  });
};

Deno.serve(handler);
```

## 3. Deploy and send email

Run function locally:

```bash  theme={null}
supabase functions start
supabase functions serve resend --no-verify-jwt
```

Deploy function to Supabase:

```bash  theme={null}
supabase functions deploy resend
```

Open the endpoint URL to send an email:

<img alt="Supabase Edge Functions - Deploy Function" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e28cab375d10a57f712e77ff3c888005" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/supabase-edge-functions-deploy-function.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=5ad81866f4e061b55ade5b508e8b6941 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e26ee1713f03952db5111effdd2bee4a 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=df3d94fc69f5764d13153e217e7c2982 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=d674b6064fa96011569a892cf4e9d683 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1907d607d324c5005966a03032ce5a1d 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/supabase-edge-functions-deploy-function.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=334c2321da6997bfdec12187653396ee 2500w" />

## 4. Try it yourself

<Card title="Supabase Edge Functions Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-supabase-edge-functions-example">
  See the full source code.
</Card>
