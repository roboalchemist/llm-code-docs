# Source: https://trigger.dev/docs/runs/max-duration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Max duration

> Set a maximum duration for a task to run.

The `maxDuration` parameter sets a maximum compute time limit for tasks. When a task exceeds this duration, it will be automatically stopped. This helps prevent runaway tasks and manage compute resources effectively.

You must set a default maxDuration in your `trigger.config.ts` file, which will apply to all tasks unless overridden:

```ts /config/trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "proj_gtcwttqhhtlasxgfuhxs",
  maxDuration: 60, // 60 seconds or 1 minute
});
```

<Note>
  The minimum maxDuration is 5 seconds. If you want to avoid timeouts, set this value to a very large number of seconds.
</Note>

You can set the `maxDuration` for a run in the following ways:

* Across all your tasks in the [config](/config/config-file#max-duration)
* On a specific task
* On a specific run when you [trigger a task](/triggering#maxduration)

## How it works

The `maxDuration` is set in seconds, and is compared to the CPU time elapsed since the start of a single execution (which we call [attempts](/runs#attempts)) of the task. The CPU time is the time that the task has been actively running on the CPU, and does not include time spent waiting during the following:

* `wait.for` calls
* `triggerAndWait` calls
* `batchTriggerAndWait` calls

You can inspect the CPU time of a task inside the run function with our `usage` utility:

```ts /trigger/max-duration.ts theme={"theme":"css-variables"}
import { task, usage } from "@trigger.dev/sdk";

export const maxDurationTask = task({
  id: "max-duration-task",
  maxDuration: 300, // 300 seconds or 5 minutes
  run: async (payload: any, { ctx }) => {
    let currentUsage = usage.getCurrent();

    currentUsage.attempt.durationMs; // The CPU time in milliseconds since the start of the run
  },
});
```

The above value will be compared to the `maxDuration` you set. If the task exceeds the `maxDuration`, it will be stopped with the following error:

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/runs/max-duration-error.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=fb10afcfe6aae4eff9556065464a32c7" alt="Max duration error" data-og-width="924" width="924" data-og-height="316" height="316" data-path="runs/max-duration-error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/runs/max-duration-error.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=3771ebf9e1f4eeb6a91a83deddea89a8 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/runs/max-duration-error.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=8d994f357524f61a993ac1313cd923fc 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/runs/max-duration-error.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=bbde11e079e057cb0ce80660c865df75 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/runs/max-duration-error.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=68ff4023f21611a3157356341efe9759 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/runs/max-duration-error.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=9dba8f836e6c38da8d8425a775b13d14 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/runs/max-duration-error.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=67a18c013e6fe596764caea1ef7d9cf6 2500w" />

## Configuring for a task

You can set a `maxDuration` on a specific task:

```ts /trigger/max-duration-task.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const maxDurationTask = task({
  id: "max-duration-task",
  maxDuration: 300, // 300 seconds or 5 minutes
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

This will override the default `maxDuration` set in the config file. If you have a config file with a default `maxDuration` of 60 seconds, and you set a `maxDuration` of 300 seconds on a task, the task will run for 300 seconds.

You can "turn off" the Max duration set in your config file for a specific task like so:

```ts /trigger/max-duration-task.ts theme={"theme":"css-variables"}
import { task, timeout } from "@trigger.dev/sdk";

export const maxDurationTask = task({
  id: "max-duration-task",
  maxDuration: timeout.None, // No max duration
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

## Configuring for a run

You can set a `maxDuration` on a specific run when you trigger a task:

```ts /trigger/max-duration.ts theme={"theme":"css-variables"}
import { maxDurationTask } from "./trigger/max-duration-task";

// Trigger the task with a maxDuration of 300 seconds
const run = await maxDurationTask.trigger(
  { foo: "bar" },
  {
    maxDuration: 300, // 300 seconds or 5 minutes
  }
);
```

You can also set the `maxDuration` to `timeout.None` to turn off the max duration for a specific run:

```ts /trigger/max-duration.ts theme={"theme":"css-variables"}
import { maxDurationTask } from "./trigger/max-duration-task";
import { timeout } from "@trigger.dev/sdk";

// Trigger the task with no maxDuration
const run = await maxDurationTask.trigger(
  { foo: "bar" },
  {
    maxDuration: timeout.None, // No max duration
  }
);
```

## maxDuration in run context

You can access the `maxDuration` set for a run in the run context:

```ts /trigger/max-duration-task.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const maxDurationTask = task({
  id: "max-duration-task",
  maxDuration: 300, // 300 seconds or 5 minutes
  run: async (payload: any, { ctx }) => {
    console.log(ctx.run.maxDuration); // 300
  },
});
```

## maxDuration and lifecycle functions

When a task run exceeds the `maxDuration`, the lifecycle functions `cleanup`, `onSuccess`, and `onFailure` will not be called.
