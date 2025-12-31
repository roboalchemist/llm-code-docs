# Source: https://trigger.dev/docs/idempotency.md

# Idempotency

> An API call or operation is “idempotent” if it has the same result when called more than once.

We currently support idempotency at the task level, meaning that if you trigger a task with the same `idempotencyKey` twice, the second request will not create a new task run.

## `idempotencyKey` option

You can provide an `idempotencyKey` to ensure that a task is only triggered once with the same key. This is useful if you are triggering a task within another task that might be retried:

```ts  theme={null}
import { idempotencyKeys, task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  retry: {
    maxAttempts: 4,
  },
  run: async (payload: any) => {
    // This idempotency key will be unique to this task run, meaning the childTask will only be triggered once across all retries
    const idempotencyKey = await idempotencyKeys.create("my-task-key");

    // childTask will only be triggered once with the same idempotency key
    await childTask.trigger({ foo: "bar" }, { idempotencyKey });

    // Do something else, that may throw an error and cause the task to be retried
    throw new Error("Something went wrong");
  },
});
```

You can use the `idempotencyKeys.create` SDK function to create an idempotency key before passing it to the `options` object.

We automatically inject the run ID when generating the idempotency key when running inside a task by default. You can turn it off by passing the `scope` option to `idempotencyKeys.create`:

```ts  theme={null}
import { idempotencyKeys, task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  retry: {
    maxAttempts: 4,
  },
  run: async (payload: any) => {
    // This idempotency key will be globally unique, meaning only a single task run will be triggered with this key
    const idempotencyKey = await idempotencyKeys.create("my-task-key", { scope: "global" });

    // childTask will only be triggered once with the same idempotency key
    await childTask.trigger({ foo: "bar" }, { idempotencyKey });
  },
});
```

If you are triggering a task from your backend code, you can use the `idempotencyKeys.create` SDK function to create an idempotency key.

```ts  theme={null}
import { idempotencyKeys, tasks } from "@trigger.dev/sdk";

// You can also pass an array of strings to create a idempotency key
const idempotencyKey = await idempotencyKeys.create([myUser.id, "my-task"]);
await tasks.trigger("my-task", { some: "data" }, { idempotencyKey });
```

You can also pass a string to the `idempotencyKey` option, without first creating it with `idempotencyKeys.create`.

```ts  theme={null}
import { myTask } from "./trigger/myTasks";

// You can also pass an array of strings to create a idempotency key
await myTask.trigger({ some: "data" }, { idempotencyKey: myUser.id });
```

<Note>Make sure you provide sufficiently unique keys to avoid collisions.</Note>

You can pass the `idempotencyKey` when calling `batchTrigger` as well:

```ts  theme={null}
import { tasks } from "@trigger.dev/sdk";

await tasks.batchTrigger("my-task", [
  {
    payload: { some: "data" },
    options: { idempotencyKey: await idempotencyKeys.create(myUser.id) },
  },
]);
```

## `idempotencyKeyTTL` option

The `idempotencyKeyTTL` option defines a time window during which a task with the same idempotency key will only run once. Here's how it works:

1. When you trigger a task with an idempotency key and set `idempotencyKeyTTL: "5m"`, it creates a 5-minute window.
2. During this window, any subsequent triggers with the same idempotency key will return the original task run instead of creating a new one.
3. Once the TTL window expires, the next trigger with that idempotency key will create a new task run and start a new time window.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/idempotency-key-ttl.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ed13a5a2782dceb10e62483dd0ad6417" alt="idempotency-key-ttl" data-og-width="939" width="939" data-og-height="924" height="924" data-path="images/idempotency-key-ttl.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/idempotency-key-ttl.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5e9e71c9b27dbd12ce2d427b6a381976 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/idempotency-key-ttl.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=27c5b4751d25d9dd76a109487b926d10 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/idempotency-key-ttl.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=28adb87d5c934a925e3a9494c23c983a 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/idempotency-key-ttl.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=234d6cc345f7e86c88627eca77503d1a 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/idempotency-key-ttl.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=fb417bbcbc46cd9ad684783313b9a91f 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/idempotency-key-ttl.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=d701231ed25ac6e732be10529e46e017 2500w" />

By default idempotency keys are stored for 30 days. You can change this by passing the `idempotencyKeyTTL` option when triggering a task:

```ts  theme={null}
import { idempotencyKeys, task, wait } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  retry: {
    maxAttempts: 4,
  },
  run: async (payload: any) => {
    const idempotencyKey = await idempotencyKeys.create("my-task-key");

    // The idempotency key will expire after 60 seconds
    await childTask.trigger({ foo: "bar" }, { idempotencyKey, idempotencyKeyTTL: "60s" });

    await wait.for({ seconds: 61 });

    // The idempotency key will have expired, so the childTask will be triggered again
    await childTask.trigger({ foo: "bar" }, { idempotencyKey });

    // Do something else, that may throw an error and cause the task to be retried
    throw new Error("Something went wrong");
  },
});
```

You can use the following units for the `idempotencyKeyTTL` option:

* `s` for seconds (e.g. `60s`)
* `m` for minutes (e.g. `5m`)
* `h` for hours (e.g. `2h`)
* `d` for days (e.g. `3d`)

## Payload-based idempotency

We don't currently support payload-based idempotency, but you can implement it yourself by hashing the payload and using the hash as the idempotency key.

```ts  theme={null}
import { idempotencyKeys, task } from "@trigger.dev/sdk";
import { createHash } from "node:crypto";

// Somewhere in your code
const idempotencyKey = await idempotencyKeys.create(hash(childPayload));
// childTask will only be triggered once with the same idempotency key
await tasks.trigger("child-task", { some: "payload" }, { idempotencyKey });

// Create a hash of the payload using Node.js crypto
// Ideally, you'd do a stable serialization of the payload before hashing, to ensure the same payload always results in the same hash
function hash(payload: any): string {
  const hash = createHash("sha256");
  hash.update(JSON.stringify(payload));
  return hash.digest("hex");
}
```

## Important notes

Idempotency keys, even the ones scoped globally, are actually scoped to the task and the environment. This means that you cannot collide with keys from other environments (e.g. dev will never collide with prod), or to other projects and orgs.

If you use the same idempotency key for triggering different tasks, the tasks will not be idempotent, and both tasks will be triggered. There's currently no way to make multiple tasks idempotent with the same key.
