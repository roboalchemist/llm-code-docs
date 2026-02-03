# Source: https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/qstash/quickstarts/cloudflare-workers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloudflare Workers

This is a step by step guide on how to receive webhooks from QStash in your
Cloudflare Worker.

### Project Setup

We will use **C3 (create-cloudflare-cli)** command-line tool to create our functions. You can open a new terminal window and run C3 using the prompt below.

<CodeGroup>
  ```shell npm theme={"system"}
  npm create cloudflare@latest
  ```

  ```shell yarn theme={"system"}
  yarn create cloudflare@latest
  ```
</CodeGroup>

This will install the `create-cloudflare` package, and lead you through setup. C3 will also install Wrangler in projects by default, which helps us testing and deploying the projects.

```text  theme={"system"}
➜  npm create cloudflare@latest
Need to install the following packages:
  create-cloudflare@2.52.3
Ok to proceed? (y) y

using create-cloudflare version 2.52.3

╭ Create an application with Cloudflare Step 1 of 3
│
├ In which directory do you want to create your application?
│ dir ./cloudflare_starter
│
├ What would you like to start with?
│ category Hello World example
│
├ Which template would you like to use?
│ type Worker only
│
├ Which language do you want to use?
│ lang TypeScript
│
├ Do you want to use git for version control?
│ yes git
│
╰ Application created
```

We will also install the **Upstash QStash library**.

```bash  theme={"system"}
npm install @upstash/qstash
```

### 3. Use QStash in your handler

First we import the library:

```ts src/index.ts theme={"system"}
import { Receiver } from "@upstash/qstash";
```

Then we adjust the `Env` interface to include the `QSTASH_CURRENT_SIGNING_KEY`
and `QSTASH_NEXT_SIGNING_KEY` environment variables.

```ts src/index.ts theme={"system"}
export interface Env {
  QSTASH_CURRENT_SIGNING_KEY: string;
  QSTASH_NEXT_SIGNING_KEY: string;
}
```

And then we validate the signature in the `handler` function.

First we create a new receiver and provide it with the signing keys.

```ts src/index.ts theme={"system"}
const receiver = new Receiver({
  currentSigningKey: env.QSTASH_CURRENT_SIGNING_KEY,
  nextSigningKey: env.QSTASH_NEXT_SIGNING_KEY,
});
```

Then we verify the signature.

```ts src/index.ts theme={"system"}
const body = await request.text();

const isValid = await receiver.verify({
  signature: request.headers.get("Upstash-Signature")!,
  body,
});
```

The entire file looks like this now:

```ts src/index.ts theme={"system"}
import { Receiver } from "@upstash/qstash";

export interface Env {
  QSTASH_CURRENT_SIGNING_KEY: string;
  QSTASH_NEXT_SIGNING_KEY: string;
}

export default {
  async fetch(request, env, ctx): Promise<Response> {
    const receiver = new Receiver({
      currentSigningKey: env.QSTASH_CURRENT_SIGNING_KEY,
      nextSigningKey: env.QSTASH_NEXT_SIGNING_KEY,
    });

    const body = await request.text();

    const isValid = await receiver.verify({
      signature: request.headers.get("Upstash-Signature")!,
      body,
    });

    if (!isValid) {
      return new Response("Invalid signature", { status: 401 });
    }

    // signature is valid

    return new Response("Hello World!");
  },
} satisfies ExportedHandler<Env>;
```

### Configure Credentials

There are two methods for setting up the credentials for QStash. One for worker level, the other for account level.

#### Using Cloudflare Secrets (Worker Level Secrets)

This is the common way of creating secrets for your worker, see [Workflow Secrets](https://developers.cloudflare.com/workers/configuration/secrets/)

* Navigate to [Upstash Console](https://console.upstash.com) and get your QStash credentials.

* In [Cloudflare Dashboard](https://dash.cloudflare.com/), Go to **Compute (Workers)** > **Workers & Pages**.

* Select your worker and go to **Settings** > **Variables and Secrets**.

* Add your QStash credentials as secrets here:

<Frame>
  <img src="https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets.png?fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=0fdc5a1123d5c3c3eaa083821712e887" data-og-width="1718" width="1718" data-og-height="624" height="624" data-path="img/cloudflare-integration/secrets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets.png?w=280&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=50845185131054d4d6a5a5297494386a 280w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets.png?w=560&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=8ed427e7462fcf0f234f39de7f51c39b 560w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets.png?w=840&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=edf1bdf371db5acbb1fa785d93c89347 840w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets.png?w=1100&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=e1e318665638791c5628f810b1048a2d 1100w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets.png?w=1650&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=86ede44dae15be8f5019028458507fca 1650w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets.png?w=2500&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=3dc232893357fcb259639d2b7e648b91 2500w" />
</Frame>

#### Using Cloudflare Secrets Store (Account Level Secrets)

This method requires a few modifications in the worker code, see [Access to Secret on Env Object](https://developers.cloudflare.com/secrets-store/integrations/workers/#3-access-the-secret-on-the-env-object)

```ts src/index.ts theme={"system"}
import { Receiver } from "@upstash/qstash";

export interface Env {
  QSTASH_CURRENT_SIGNING_KEY: SecretsStoreSecret;
  QSTASH_NEXT_SIGNING_KEY: SecretsStoreSecret;
}

export default {
  async fetch(request, env, ctx): Promise<Response> {
    const c = new Receiver({
      currentSigningKey: await env.QSTASH_CURRENT_SIGNING_KEY.get(),
      nextSigningKey: await env.QSTASH_NEXT_SIGNING_KEY.get(),
    });

    // Rest of the code
  },
};
```

After doing these modifications, you can deploy the worker to Cloudflare with `npx wrangler deploy`, and
follow the steps below to define the secrets:

* Navigate to [Upstash Console](https://console.upstash.com) and get your QStash credentials.

* In [Cloudflare Dashboard](https://dash.cloudflare.com/), Go to **Secrets Store** and add QStash credentials as secrets.

<Frame>
  <img src="https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets-store.png?fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=daefd6a42242541b70452ccd1071e7dd" data-og-width="1940" width="1940" data-og-height="1110" height="1110" data-path="img/cloudflare-integration/secrets-store.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets-store.png?w=280&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=4dcc1246d56ffba5f01961b68774af90 280w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets-store.png?w=560&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=8a288410ed7f8913c97e610d41ebd7c6 560w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets-store.png?w=840&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=a180068645d1f866f6ca5c6f302f7e16 840w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets-store.png?w=1100&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=8c371c37e0b4809493768fd8734c1337 1100w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets-store.png?w=1650&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=b0e40ebfe03c24b833311fb3806bb09a 1650w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/secrets-store.png?w=2500&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=a420fa6ad32aa11a9198f73e5ae7b6b1 2500w" />
</Frame>

* Under **Compute (Workers)** > **Workers & Pages**, find your worker and add these secrets as bindings.

<Frame>
  <img src="https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/add-binding.png?fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=3959adcb8a96153fbc001d35609182ad" data-og-width="1940" width="1940" data-og-height="1368" height="1368" data-path="img/cloudflare-integration/add-binding.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/add-binding.png?w=280&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=8ac52ecfe1badade3aa079ab5be91840 280w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/add-binding.png?w=560&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=8a824b1590cddb28be8ae046008d6daa 560w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/add-binding.png?w=840&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=f7ca746df30c5b0e4c9ba39c99def7d5 840w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/add-binding.png?w=1100&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=b689b92485b9c5f538ba6b7f340d84e2 1100w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/add-binding.png?w=1650&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=43d991ebc0be959c42efb31a95bac614 1650w, https://mintcdn.com/upstash/DrxIz7v3jaqUZCku/img/cloudflare-integration/add-binding.png?w=2500&fit=max&auto=format&n=DrxIz7v3jaqUZCku&q=85&s=ffb326c5cadb3044db014762bddbeddf 2500w" />
</Frame>

### Deployment

<Note>
  Newer deployments may revert the configurations you did in the dashboard.
  While worker level secrets persist, the bindings will be gone!
</Note>

Deploy your function to Cloudflare with `npx wrangler deploy`

The endpoint of the function will be provided to you, once the deployment is done.

### Publish a message

Open a different terminal and publish a message to QStash. Note the destination
url is the same that was printed in the previous deploy step.

```bash  theme={"system"}
curl --request POST "https://qstash.upstash.io/v2/publish/https://<your-worker-name>.<account-name>.workers.dev" \
     -H "Authorization: Bearer <QSTASH_TOKEN>" \
     -H "Content-Type: application/json" \
     -d "{ \"hello\": \"world\"}"
```

In the logs you should see something like this:

```bash  theme={"system"}
$ npx wrangler tail

⛅️ wrangler 4.43.0
--------------------

Successfully created tail, expires at 2025-10-16T00:25:17Z
Connected to <your-worker-name>, waiting for logs...
POST https://<your-worker-name>.<account-name>.workers.dev/ - Ok @ 10/15/2025, 10:34:55 PM
```

## Next Steps

That's it, you have successfully created a secure Cloudflare Worker, that
receives and verifies incoming webhooks from qstash.

Learn more about publishing a message to qstash [here](/qstash/howto/publishing).

You can find the source code [here](https://github.com/upstash/qstash-examples/tree/main/cloudflare-workers).
