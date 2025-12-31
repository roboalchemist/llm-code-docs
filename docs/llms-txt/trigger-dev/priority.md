# Source: https://trigger.dev/docs/runs/priority.md

# Priority

> Specify a priority when triggering a run.

You can set a priority when you trigger a run. This allows you to prioritize some of your runs over others, so they are started sooner. This is very useful when:

* You have critical work that needs to start more quickly (and you have long queues).
* You want runs for your premium users to take priority over free users.

The value for priority is a time offset in seconds that determines the order of dequeuing.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/priority-runs.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=36b348760cb05a1c7af1b8625beddf24" alt="Priority runs" data-og-width="1243" width="1243" data-og-height="1333" height="1333" data-path="images/priority-runs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/priority-runs.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=98dd1c09b0da112db56fed9c27fb1dde 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/priority-runs.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=bd9ed1ea970f1cfa642f7c1d1c9c01ba 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/priority-runs.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=69b0bd28f1825e9fbfc3337e60355276 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/priority-runs.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=9f5fe734ac451bde5a6187f856515d30 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/priority-runs.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=756b8d9cd6835143ca95f7fefbc7f609 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/priority-runs.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c1003b28761e476969bb0b226e589ec9 2500w" />

If you specify a priority of `10` the run will dequeue before runs that were triggered with no priority 8 seconds ago, like in this example:

```ts  theme={null}
// no priority = 0
await myTask.trigger({ foo: "bar" });

//... imagine 8s pass by

// this run will start before the run above that was triggered 8s ago (with no priority)
await myTask.trigger({ foo: "bar" }, { priority: 10 });
```

If you passed a value of `3600` the run would dequeue before runs that were triggered an hour ago (with no priority).

<Note>
  Setting a high priority will not allow you to beat runs from other organizations. It will only affect the order of your own runs.
</Note>
