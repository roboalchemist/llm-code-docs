# Source: https://trigger.dev/docs/how-to-reduce-your-spend.md

# How to reduce your spend

> Tips and best practices to reduce your costs on Trigger.dev

## Check out your usage page regularly

Monitor your usage dashboard to understand your spending patterns. You can see:

* Your most expensive tasks
* Your total duration by task
* Number of runs by task
* Spikes in your daily usage

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/usage-dashboard.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=0117c432cfbb809afbcc5698314dc97d" alt="Usage dashboard" data-og-width="1586" width="1586" data-og-height="1068" height="1068" data-path="images/usage-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/usage-dashboard.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=8bfe7c067705696a1d1c4185cb42e0b4 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/usage-dashboard.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=b9059cd16ffc6ecce13077378646f956 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/usage-dashboard.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=aa9acbd91ba5192e66f7718c16b3dbdd 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/usage-dashboard.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=0922aa95ad5d3a175c560700a869f4e2 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/usage-dashboard.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4d6c19d83cbf2a21928c9c1393b01749 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/usage-dashboard.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=e98f6e2d5bfd4e6350b622b3ade51afe 2500w" />

You can view your usage page by clicking the "Organization" menu in the top left of the dashboard and then clicking "Usage".

## Create billing alerts

Configure billing alerts in your dashboard to get notified when you approach spending thresholds. This helps you:

* Catch unexpected cost increases early
* Identify runaway tasks before they become expensive

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/billing-alerts-ui.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=cc2a66d8aab0d8941f81dd70bc7fb61f" alt="Billing alerts" data-og-width="925" width="925" data-og-height="757" height="757" data-path="images/billing-alerts-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/billing-alerts-ui.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=1239c92296178c20b1fa90beb3a516f2 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/billing-alerts-ui.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=bbadf36f5ec87cac2007f8f6075974ca 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/billing-alerts-ui.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c741c8297876d7cfadedba38ed28853f 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/billing-alerts-ui.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=594b1eec851cd8d5199d47a6b35a6b40 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/billing-alerts-ui.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=692aebc1193500cc97c275f0bd5ddb0c 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/billing-alerts-ui.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=813b55e61d9c1bffd376f06acd7f7d3f 2500w" />

You can view your billing alerts page by clicking the "Organization" menu in the top left of the dashboard and then clicking "Settings".

## Reduce your machine sizes

The larger the machine, the more it costs per second. [View the machine pricing](https://trigger.dev/pricing#computePricing).

Start with the smallest machine that works, then scale up only if needed:

```ts  theme={null}
// Default: small-1x (0.5 vCPU, 0.5 GB RAM)
export const lightTask = task({
  id: "light-task",
  // No machine config needed - uses small-1x by default
  run: async (payload) => {
    // Simple operations
  },
});

// Only use larger machines when necessary
export const heavyTask = task({
  id: "heavy-task",
  machine: "medium-1x", // 1 vCPU, 2 GB RAM
  run: async (payload) => {
    // CPU/memory intensive operations
  },
});
```

You can also override machine size when triggering if you know certain payloads need more resources. [Read more about machine sizes](/machines).

## Avoid duplicate work using idempotencyKey

Idempotency keys prevent expensive duplicate work by ensuring the same operation isn't performed multiple times. This is especially valuable during task retries or when the same trigger might fire multiple times.

When you use an idempotency key, Trigger.dev remembers the result and skips re-execution, saving you compute costs:

```ts  theme={null}
export const expensiveApiCall = task({
  id: "expensive-api-call",
  run: async (payload: { userId: string }) => {
    // This expensive operation will only run once per user
    await wait.for(
      { seconds: 30 },
      {
        idempotencyKey: `user-processing-${payload.userId}`,
        idempotencyKeyTTL: "1h",
      }
    );

    const result = await processUserData(payload.userId);
    return result;
  },
});
```

You can use idempotency keys with various wait functions:

```ts  theme={null}
// Skip waits during retries
const token = await wait.createToken({
  idempotencyKey: `daily-report-${new Date().toDateString()}`,
  idempotencyKeyTTL: "24h",
});

// Prevent duplicate child task execution
await childTask.triggerAndWait(
  { data: payload },
  {
    idempotencyKey: `process-${payload.id}`,
    idempotencyKeyTTL: "1h",
  }
);
```

The `idempotencyKeyTTL` controls how long the result is cached. Use shorter TTLs (like "1h") for time-sensitive operations, or longer ones (up to 30 days default) for expensive operations that rarely need re-execution. This prevents both unnecessary duplicate work and stale data issues.

## Do more work in parallel in a single task

Sometimes it's more efficient to do more work in a single task than split across many. This is particularly true when you're doing lots of async work such as API calls – most of the time is spent waiting, so it's an ideal candidate for doing calls in parallel inside the same task.

```ts  theme={null}
export const processItems = task({
  id: "process-items",
  run: async (payload: { items: string[] }) => {
    // Process all items in parallel
    const promises = payload.items.map((item) => processItem(item));
    // This works very well for API calls
    await Promise.all(promises);
  },
});
```

## Don't needlessly retry

When an error is thrown in a task, your run will be automatically reattempted based on your [retry settings](/tasks/overview#retry-options).

Try setting lower `maxAttempts` for less critical tasks:

```ts  theme={null}
export const apiTask = task({
  id: "api-task",
  retry: {
    maxAttempts: 2, // Don't retry forever
  },
  run: async (payload) => {
    // API calls that might fail
  },
});
```

This is very useful for intermittent errors, but if there's a permanent error you don't want to retry because you will just keep failing and waste compute. Use [AbortTaskRunError](/errors-retrying#using-aborttaskrunerror) to prevent a retry:

```ts  theme={null}
import { task, AbortTaskRunError } from "@trigger.dev/sdk";

export const someTask = task({
  id: "some-task",
  run: async (payload) => {
    const result = await doSomething(payload);

    if (!result.success) {
      // This is a known permanent error, so don't retry
      throw new AbortTaskRunError(result.error);
    }

    return result;
  },
});
```

## Use appropriate maxDuration settings

Set realistic maxDurations to prevent runs from executing for too long:

```ts  theme={null}
export const boundedTask = task({
  id: "bounded-task",
  maxDuration: 300, // 5 minutes max
  run: async (payload) => {
    // Task will be terminated after 5 minutes
  },
});
```
