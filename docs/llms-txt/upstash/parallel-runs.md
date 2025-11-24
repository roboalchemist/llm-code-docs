# Source: https://upstash.com/docs/workflow/howto/parallel-runs.md

# Parallel Runs

<Note>
  This feature is not yet available in
  [workflow-py](https://github.com/upstash/workflow-py). See our
  [Roadmap](/workflow/roadmap) for feature parity plans and
  [Changelog](/workflow/changelog) for updates.
</Note>

Just like you can execute multiple JavaScript promises at the same time using `Promise.all`, you can run multiple workflow steps at the same time:

```typescript  theme={"system"}
const [result1, result2, result3] =
  await Promise.all([
    ctx.run("parallel-step-1", async () => { ... }),
    ctx.run("parallel-step-2", async () => { ... }),
    ctx.run("parallel-step-3", async () => { ... }),
  ])
```

In a complete code example, your workflow could look like this:

```typescript app/api/workflow/route.ts theme={"system"}
import { serve } from "@upstash/workflow/nextjs";
import { checkInventory, brewCoffee, printReceipt } from "@/utils";

export const { POST } = serve(async (ctx) => {
  const [coffeeBeansAvailable, cupsAvailable, milkAvailable] =
    await Promise.all([
      ctx.run("check-coffee-beans", () => checkInventory("coffee-beans")),
      ctx.run("check-cups", () => checkInventory("cups")),
      ctx.run("check-milk", () => checkInventory("milk")),
    ]);

  // If all ingedients available, brew coffee
  if (coffeeBeansAvailable && cupsAvailable && milkAvailable) {
    const price = await ctx.run("brew-coffee", async () => {
      return await brewCoffee({ style: "cappuccino" });
    });

    await printReceipt(price);
  }
});
```

After running your workflow, your dashboard shows each step in detail:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/parallel-workflow-runs.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8a90ffc27d343e665833d4c497d1dd9d" data-og-width="1266" width="1266" data-og-height="627" height="627" data-path="img/qstash/parallel-workflow-runs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/parallel-workflow-runs.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=014537ac125a65f39fd1e5ab5a433e0e 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/parallel-workflow-runs.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=96a6d41f1515536892a665c6a5e2561c 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/parallel-workflow-runs.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ff46f39f06c97e387370813e65f503bb 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/parallel-workflow-runs.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=dd1533e3e27e87fb0b26629690fa6284 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/parallel-workflow-runs.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2fb6bb8d641837bb2584bc894cb6dbfe 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/parallel-workflow-runs.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=47c72c728b956366d79989f9f0a2ebff 2500w" />
</Frame>
