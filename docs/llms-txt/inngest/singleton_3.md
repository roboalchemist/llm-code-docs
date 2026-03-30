# Source: https://www.inngest.com/docs-markdown/reference/typescript/v4/functions/singleton

# Ensure exclusive execution of a function

Ensure that only a single run of a function (*or a set of specific functions, based on specific event properties*) is running at a time.

See the [Singleton Functions guide](/docs-markdown/guides/singleton) for more information about how this feature works.

```ts
export default inngest.createFunction(
  {
    id: "data-sync",
    triggers: { event: "data-sync.start" },
    singleton: {
      key: "event.data.user_id",
      mode: "skip",
    },
  },
  async ({ event }) => {
    // This function will be skipped if another run of the same function is already running for the same user
  }
);
```

## Configuration

- `singleton` (object): Options to configure exclusive execution of a function.A unique key expression to which the limit is applied. This expression is evaluated for each triggering event.Expressions are defined using the Common Expression Language (CEL) with the original event accessible using dot-notation. Read our guide to writing expressions for more info. Examples:Ensure exclusive execution of a function per customer ID: 'event.data.customer\_id'Ensure exclusive execution of a function per account and email address: 'event.data.account\_id + "-" + event.user.email'The mode to use for the singleton function:"skip": Skip the new run."cancel": Cancel the existing run and start the new one.

## Examples

### Ensure executing only upon the latest event

In this example, the active run of our `data-sync` function will be cancelled if another event with the same `user_id` is received:

```ts
// Example event payload:
// {
//   name: "data-sync.start",
//   data: {
//     user_id: "123456789",
//   }
// }
export default inngest.createFunction(
  {
    id: "data-sync",
    triggers: { event: "data-sync.start" },
    singleton: {
      key: "event.data.user_id",
      mode: "cancel",
    },
  },
  async ({ event, step }) => {
    const company = await step.run(
      "fetch-latest-data-from-source",
      async () => {
        return await client.fetchData(event.data.user_id);
      }
    );

    await step.run("update-data-in-database", async () => {
      return await database.upsert({ id: company.id }, company);
    });
  }
);
```

While similar to [Debounce](/docs-markdown/guides/debounce), Singleton Functions are designed to ensure that only a single run of a function is happening at a time, whereas Debounce ensures that only a single event is processed within a given time window.

Refer to the [Singleton Functions guide](/docs-markdown/guides/singleton) for more information about how this feature works.