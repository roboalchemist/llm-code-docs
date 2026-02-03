# Source: https://upstash.com/docs/qstash/recipes/periodic-data-updates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Periodic Data Updates

<Note>
  * Code:
    [Repository](https://github.com/upstash/qstash-examples/tree/main/periodic-data-updates)
  * App:
    [qstash-examples-periodic-data-updates.vercel.app](https://qstash-examples-periodic-data-updates.vercel.app)
</Note>

This recipe shows how to use QStash as a trigger for a Next.js api route, that
fetches data from somewhere and stores it in your database.

For the database we will use Redis because it's very simple to setup and is not
really the main focus of this recipe.

## What will be build?

Let's assume there is a 3rd party API that provides some data. One approach
would be to just query the API whenever you or your users need it, however that
might not work well if the API is slow, unavailable or rate limited.

A better approach would be to continuously fetch fresh data from the API and
store it in your database.

Traditionally this would require a long running process, that would continuously
call the API. With QStash you can do this inside your Next.js app and you don't
need to worry about maintaining anything.

For the purpose of this recipe we will build a simple app, that scrapes the
current Bitcoin price from a public API, stores it in redis and then displays a
chart in the browser.

## Setup

If you don't have one already, create a new Next.js project with
`npx create-next-app@latest --ts`.

Then install the required packages

```bash  theme={"system"}
npm install @upstash/qstash @upstash/redis
```

You can replace `@upstash/redis` with any kind of database client you want.

## Scraping the API

Create a new serverless function in `/pages/api/cron.ts`

````ts  theme={"system"}
import { NextApiRequest, NextApiResponse } from "next";
import { Redis } from "@upstash/redis";

import { verifySignature } from "@upstash/qstash/nextjs";

/**
 * You can use any database you want, in this case we use Redis
 */
const redis = Redis.fromEnv();

/**
 * Load the current bitcoin price in USD and store it in our database at the
 * current timestamp
 */
async function handler(_req: NextApiRequest, res: NextApiResponse) {
  try {
    /**
     * The API returns something like this:
     * ```json
     * {
     *   "USD": {
     *     "last": 123
     *   },
     *   ...
     * }
     * ```
     */
    const raw = await fetch("https://blockchain.info/ticker");
    const prices = await raw.json();
    const bitcoinPrice = prices["USD"]["last"] as number;

    /**
     * After we have loaded the current bitcoin price, we can store it in the
     * database together with the current time
     */
    await redis.zadd("bitcoin-prices", {
      score: Date.now(),
      member: bitcoinPrice,
    });

    res.send("OK");
  } catch (err) {
    res.status(500).send(err);
  } finally {
    res.end();
  }
}

/**
 * Wrap your handler with `verifySignature` to automatically reject all
 * requests that are not coming from Upstash.
 */
export default verifySignature(handler);

/**
 * To verify the authenticity of the incoming request in the `verifySignature`
 * function, we need access to the raw request body.
 */
export const config = {
  api: {
    bodyParser: false,
  },
};
````

## Deploy to Vercel

That's all we need to fetch fresh data. Let's deploy our app to Vercel.

You can either push your code to a git repository and deploy it to Vercel, or
you can deploy it directly from your local machine using the
[vercel cli](https://vercel.com/docs/cli).

For a more indepth tutorial on how to deploy to Vercel, check out this
[quickstart](/qstash/quickstarts/vercel-nextjs#4-deploy-to-vercel).

After you have deployed your app, it is time to add your secrets to your
environment variables.

## Secrets

Head over to [QStash](https://console.upstash.com/qstash) and copy the
`QSTASH_CURRENT_SIGNING_KEY` and `QSTASH_NEXT_SIGNING_KEY` to vercel's
environment variables. <img src="https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel_env.png?fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=4a6b0a2d6462ad1263ca5a818d51f0c4" alt="" data-og-width="1936" width="1936" data-og-height="558" height="558" data-path="img/qstash/vercel_env.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel_env.png?w=280&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=0a70241ecf06008c91890e8006bb112d 280w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel_env.png?w=560&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=8bb5ed05bd390dc9b65c90440a2af1eb 560w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel_env.png?w=840&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=44d6710922737223fcbea2353e0ef3a7 840w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel_env.png?w=1100&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=781e9a6c1db30e1a8516eb57ab978d1d 1100w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel_env.png?w=1650&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=8415b3480935383e86ae88f9641e1be3 1650w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel_env.png?w=2500&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=9c1bed9b4627fa7e247d5ed3a82022f7 2500w" />

If you are not using a custom database, you can quickly create a new
[Redis database](https://console.upstash.com/redis). Afterwards copy the
`UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN` to vercel.

In the near future we will update our
[Vercel integration](https://vercel.com/integrations/upstash) to do this for
you.

## Redeploy

To use the environment variables, you need to redeploy your app. Either with
`npx vercel --prod` or in the UI.

## Create cron trigger in QStash

The last part is to add the trigger in QStash. Go to
[QStash](https://console.upstash.com/qstash) and create a new schedule.

<img src="https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/schedule.png?fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=d2c7fdc9aa6649d1eabc215a22b2c5d8" alt="" data-og-width="1978" width="1978" data-og-height="1268" height="1268" data-path="img/qstash/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/schedule.png?w=280&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=2b98f99aa0996910a67722f13fc7a5cc 280w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/schedule.png?w=560&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=f346055eb0a179a785dc4e7ad53893c1 560w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/schedule.png?w=840&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=2a84cda9465fecd911bd05ecde8a65c4 840w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/schedule.png?w=1100&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=311e881865a6b41e818f692e5cdab32d 1100w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/schedule.png?w=1650&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=932005b810d98335d0d956dc590caa06 1650w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/schedule.png?w=2500&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=10272ef5c53da0a67c2bc5fca78e310e 2500w" />

Now we will call your api function whenever you schedule is triggered.

## Adding frontend UI

This part is probably the least interesting and would require more dependencies
for styling etc. Check out the
[index.tsx](https://github.com/upstash/qstash-examples/blob/main/periodic-data-updates/pages/index.tsx)
file, where we load the data from the database and display it in a chart.

## Hosted example

You can find a running example of this recipe
[here](https://qstash-examples-periodic-data-updates.vercel.app/).
