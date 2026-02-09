# Source: https://trigger.dev/docs/tags.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tags

> Tags allow you to easily filter runs in the dashboard and when using the SDK.

## What are tags?

We support up to 10 tags per run. Each one must be a string between 1 and 128 characters long.

We recommend prefixing your tags with their type and then an underscore or colon. For example, `user_123456` or `video:123`.

<Info>
  Many great APIs, like Stripe, already prefix their IDs with the type and an underscore. Like
  `cus_123456` for a customer.
</Info>

We don't enforce prefixes but if you use them you'll find it easier to filter and it will be clearer what the tag represents.

## How to add tags

There are two ways to add tags to a run:

1. When triggering the run.
2. Inside the `run` function, using `tags.add()`.

### 1. Adding tags when triggering the run

You can add tags when triggering a run using the `tags` option. All the different [trigger](/triggering) methods support this.

<CodeGroup>
  ```ts trigger theme={"theme":"css-variables"}
  const handle = await myTask.trigger(
    { message: "hello world" },
    { tags: ["user_123456", "org_abcdefg"] }
  );
  ```

  ```ts batchTrigger theme={"theme":"css-variables"}
  const batch = await myTask.batchTrigger([
    {
      payload: { message: "foo" },
      options: { tags: "product_123456" },
    },
    {
      payload: { message: "bar" },
      options: { tags: ["user_123456", "product_3456789"] },
    },
  ]);
  ```
</CodeGroup>

This will create a run with the tags `user_123456` and `org_abcdefg`. They look like this in the runs table:

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-org-user.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=95300055e21df2ac777716ee826b14a2" alt="How tags appear in the dashboard" data-og-width="500" width="500" data-og-height="213" height="213" data-path="images/tags-org-user.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-org-user.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4ee5ab06962f5838750401973f4b7fd4 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-org-user.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=934bb9dbccef3a395b8fc2b67b6bb627 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-org-user.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=b9f05a20db53d7f1ac1528fd24691440 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-org-user.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=aa50ecbbe7a15241f30cbcfc46a86fca 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-org-user.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=05e1b709d6f044b5fdd41060fc6429a6 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-org-user.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=a1103011e76a5348c37d7ad32d38b4f1 2500w" />

### 2. Adding tags inside the `run` function

Use the `tags.add()` function to add tags to a run from inside the `run` function. This will add the tag `product_1234567` to the run:

```ts  theme={"theme":"css-variables"}
import { task, tags } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }, { ctx }) => {
    // Get the tags from when the run was triggered using the context
    // This is not updated if you add tags during the run
    logger.log("Tags from the run context", { tags: ctx.run.tags });

    // Add tags during the run (a single string or array of strings)
    await tags.add("product_1234567");
  },
});
```

Reminder: you can only have up to 10 tags per run. If you call `tags.add()` and the total number of tags will be more than 10 we log an error and ignore the new tags. That includes tags from triggering and from inside the run function.

### Propagating tags to child runs

Tags do not propagate to child runs automatically. By default runs have no tags and you have to set them explicitly.

It's easy to propagate tags if you want:

```ts  theme={"theme":"css-variables"}
export const myTask = task({
  id: "my-task",
  run: async (payload: Payload, { ctx }) => {
    // Pass the tags from ctx into the child run
    const { id } = await otherTask.trigger(
      { message: "triggered from myTask" },
      { tags: ctx.run.tags }
    );
  },
});
```

## Filtering runs by tags

You can filter runs by tags in the dashboard and in the SDK.

### In the dashboard

On the Runs page open the filter menu, choose "Tags" and then start typing in the name of the tag you want to filter by. You can select it and it will restrict the results to only runs with that tag. You can add multiple tags to filter by more than one.

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-filtering.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=100b923c8d382ca830344a29cccd30ae" alt="Filter by tags" data-og-width="3162" width="3162" data-og-height="1874" height="1874" data-path="images/tags-filtering.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-filtering.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=cf5c3088aa5f5d500830a95352e2a613 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-filtering.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=5ad94f3537cf19214750398d8da82761 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-filtering.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=31f469bf812eeb4fe3e4255db8159702 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-filtering.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=bbb2f501b0fde07252bbc1756251cf18 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-filtering.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=f56770191e9f191911d61a041b052413 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/tags-filtering.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=ac42f439de4fb4d28c09e68185c21f8b 2500w" />

### Using `runs.list()`

You can provide filters to the `runs.list` SDK function, including an array of tags.

```ts  theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

// Loop through all runs with the tag "user_123456" that have completed
for await (const run of runs.list({ tag: "user_123456", status: ["COMPLETED"] })) {
  console.log(run.id, run.taskIdentifier, run.finishedAt, run.tags);
}
```
