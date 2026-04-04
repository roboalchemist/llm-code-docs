# Source: https://upstash.com/docs/workflow/features/parallel-steps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Parallel Steps

Upstash Workflow supports executing multiple steps in parallel.

Since each step returns a `Promise`, you can execute multiple steps concurrently by using `Promise.all()`.
This behavior works out of the box. No additional configuration is required.

```typescript app/api/workflow/route.ts theme={"system"}
import { serve } from "@upstash/workflow/nextjs";
import { checkInventory, brewCoffee, printReceipt } from "@/utils";

export const { POST } = serve(async (context) => {

  // 👇 Execute steps in parallel
  const [coffeeBeansAvailable, cupsAvailable, milkAvailable] =
    await Promise.all([
      context.run("check-coffee-beans", () => checkInventory("coffee-beans")),
      context.run("check-cups", () => checkInventory("cups")),
      context.run("check-milk", () => checkInventory("milk")),
    ]);

});
```

The results of the parallel steps are available as usual once awaited.

The dashboard visualizes parallel execution as shown below:

<Frame caption="The workflow executes three steps in parallel">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallel_steps.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=e7e8c68861f76152c98ca015fc3c0913" data-og-width="2620" width="2620" data-og-height="1992" height="1992" data-path="img/workflow/parallel_steps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallel_steps.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=4edfaaa0a9df3933dcee3df2e7c4db31 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallel_steps.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=7e558fba7f0c775fde3cc6ee6ff1dee0 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallel_steps.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=d9951af9065135f6c7da313637b8d345 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallel_steps.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=5fc4cbb09d7180979eabce86fb5a7b1a 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallel_steps.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=6bbed50a4f2307529f7dc82e07b15169 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallel_steps.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=35b85844e807fd61a79d796c46649653 2500w" />
</Frame>

You can also await different step types together. For example, you can run a `context.call()` and a `context.run()` in parallel.

<Warning>
  Whether executing sequentially or in parallel, you should always
  <code>await</code> all promises in a workflow.
  Leaving promises unawaited may cause unexpected behavior.
</Warning>
