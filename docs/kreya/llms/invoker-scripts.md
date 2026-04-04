# Source: https://kreya.app/docs/scripting-and-tests/invoker-scripts.md

# Scripts [Pro / Enterprise](/pricing.md)

Kreya scripts (not to be confused with [operation scripts](/docs/scripting-and-tests/operation-scripts.md), which define scripts and tests in operations) offer a way to arbitrarily control the execution flow of operations. Among other things, it allows you to create tests and view the results of them.

![Screenshot of a script](/assets/ideal-img/invoker-script.efa0191.400.png)

This can be useful in a range of scenarios. For example, if you want to start a long-running job and wait until it is finished:

```
// Invoke an operation that starts a long running job on the server
await kreya.invokeOperation('start-long-running-job');

while (true) {
  const result = await kreya.invokeOperation('fetch-job-status');
  if (result.success) {
    break;
  }

  kreya.sleep(500);
}

// Now invoke an operation that fetches the job result and performs tests on it
await kreya.invokeOperation('fetch-job-result');
```

Another use case could be to run multiple operations concurrently:

```
// Start an operation, but do not wait for its completion (no await keyword)
const runningOperation = kreya.invokeOperation('long-running');

// Invoke some other operations in the meantime
await kreya.invokeOperation('operation1');
await kreya.invokeOperation('operation2');

// Now we wait for the long-running operation to complete
await runningOperation;
```

View all available properties and methods in the [API reference](/docs/scripting-and-tests/invoker-scripts/api-reference.md).

To create a new script, select `Script` in the new menu:

![Screenshot of the new menu focused on the script](/assets/ideal-img/invoker-script-new.80f9959.400.png)
