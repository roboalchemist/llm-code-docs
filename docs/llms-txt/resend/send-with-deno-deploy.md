# Source: https://resend.com/docs/send-with-deno-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Deno Deploy

> Learn how to send your first email using Deno Deploy.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Create a Deno Deploy project

Go to [dash.deno.com/projects](https://dash.deno.com/projects) and create a new playground project.

<img alt="Deno Deploy - New Project" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-new-project.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=634d342d6e542f4c82eb9c013bfcc817" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/deno-deploy-new-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-new-project.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=f92fd83b5564fdc078867d7d4cbb4262 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-new-project.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=4ca5e87dbc66643ce4cbf18d3399686d 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-new-project.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=da3c6bd27d700a1f5372ec24c807855c 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-new-project.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=6ea1fb1720e7309517a12f9bceadecfd 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-new-project.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=6849f1f611cc5b03898c8c4b5b8396dc 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-new-project.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=883f8d6f49eb27cf5c2592d45c8d2397 2500w" />

## 2. Edit the handler function

Paste the following code into the browser editor:

```ts main.ts theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'npm:resend';

const resend = new Resend('re_123456789');

Deno.serve(async () => {
  try {
    const response = await resend.emails.send({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'Hello World',
      html: '<strong>It works!</strong>',
    });

    return new Response(JSON.stringify(response), {
      status: response.error ? 500 : 200,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  } catch (error) {
    console.error(error);
    return new Response(null, {
      status: 500,
    });
  }
});
```

## 3. Deploy and send email

Click on `Save & Deploy` at the top of the screen.

<img alt="Deno Deploy - Playground" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-playground.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=fb62c969114e48e5401fecc67f5a4d76" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/deno-deploy-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-playground.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=36893350ecf4039eef7514f5c7b548aa 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-playground.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=df997f1dba4ed30bb02f78632002f0e2 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-playground.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=26bcd5520ec035f9270eed86d2809af8 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-playground.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e4d65d030da04239429ad1bcf2a10e87 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-playground.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=0b139a96b092a4776f2d87a2c1524217 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/deno-deploy-playground.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e704749e9adc3179f481bb7129c79073 2500w" />

## 4. Try it yourself

<Card title="Deno Deploy Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-deno-deploy-example">
  See the full source code.
</Card>
