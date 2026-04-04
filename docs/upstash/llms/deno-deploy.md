# Source: https://upstash.com/docs/redis/quickstarts/deno-deploy.md

# Source: https://upstash.com/docs/qstash/quickstarts/deno-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deno Deploy

[Source Code](https://github.com/upstash/qstash-examples/tree/main/deno-deploy)

This is a step by step guide on how to receive webhooks from QStash in your Deno
deploy project.

### 1. Create a new project

Go to [https://dash.deno.com/projects](https://dash.deno.com/projects) and
create a new playground project.

### 2. Edit the handler function

Then paste the following code into the browser editor:

```ts  theme={"system"}
import { serve } from "https://deno.land/std@0.142.0/http/server.ts";
import { Receiver } from "https://deno.land/x/upstash_qstash@v0.1.4/mod.ts";

serve(async (req: Request) => {
  const r = new Receiver({
    currentSigningKey: Deno.env.get("QSTASH_CURRENT_SIGNING_KEY")!,
    nextSigningKey: Deno.env.get("QSTASH_NEXT_SIGNING_KEY")!,
  });

  const isValid = await r
    .verify({
      signature: req.headers.get("Upstash-Signature")!,
      body: await req.text(),
    })
    .catch((err: Error) => {
      console.error(err);
      return false;
    });

  if (!isValid) {
    return new Response("Invalid signature", { status: 401 });
  }

  console.log("The signature was valid");

  // do work

  return new Response("OK", { status: 200 });
});
```

### 3. Add your signing keys

Click on the `settings` button at the top of the screen and then click
`+ Add Variable`

Get your current and next signing key from
[Upstash](https://console.upstash.com/qstash) and then set them in deno deploy.

<img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/deno_deploy_env.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fcd35bafc9752ac36a93de5ff8142c18" alt="" data-og-width="3016" width="3016" data-og-height="1666" height="1666" data-path="img/qstash/deno_deploy_env.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/deno_deploy_env.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d489d42d7b134d28b4863cde8544efac 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/deno_deploy_env.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=44d5b15af4e1a47614ac4b583c79270e 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/deno_deploy_env.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=36e34a30f657a0809203e6e6bfdc87f3 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/deno_deploy_env.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3b6fb4bc9c79c2461d822890da31f2bf 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/deno_deploy_env.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ff3513e131ffdb82378f2c53abf7ba20 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/deno_deploy_env.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=65cb2066cc2ab3ee9ceda1620c354751 2500w" />

### 4. Deploy

Simply click on `Save & Deploy` at the top of the screen.

### 5. Publish a message

Make note of the url displayed in the top right. This is the public url of your
project.

```bash  theme={"system"}
curl --request POST "https://qstash.upstash.io/v2/publish/https://early-frog-33.deno.dev" \
     -H "Authorization: Bearer <QSTASH_TOKEN>" \
     -H "Content-Type: application/json" \
     -d "{ \"hello\": \"world\"}"
```

In the logs you should see something like this:

```basheurope-west3isolate start time: 2.21 ms theme={"system"}
Listening on http://localhost:8000/
The signature was valid
```

## Next Steps

That's it, you have successfully created a secure deno API, that receives and
verifies incoming webhooks from qstash.

Learn more about publishing a message to qstash [here](/qstash/howto/publishing)
