# Source: https://trigger.dev/docs/logging.md

# Logging and tracing

> How to use the built-in logging and tracing system.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-log.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=595580c7a9e3e5dcc0e3297f0f6fec68" alt="The run log" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/run-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-log.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8e387330e0f9ff8717932fae4d604ecf 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-log.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=fd0e82f755dd03d33b64384d10bd5969 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-log.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=6dfa64d17a661cf7715799d82ed898ca 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-log.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=7ddf07bfae2ad13b921b2051002f4ad5 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-log.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=541fa551d5361702d92e41b0dad28b50 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-log.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=cd7e639daec0374eb8c2cb6c5017f89b 2500w" />

The run log shows you exactly what happened in every run of your tasks. It is comprised of logs, traces and spans.

## Logs

You can use `console.log()`, `console.error()`, etc as normal and they will be shown in your run log. This is the standard function so you can use it as you would in any other JavaScript or TypeScript code. Logs from any functions/packages will also be shown.

### logger

We recommend that you use our `logger` object which creates structured logs. Structured logs will make it easier for you to search the logs to quickly find runs.

```ts /trigger/logging.ts theme={null}
import { task, logger } from "@trigger.dev/sdk";

export const loggingExample = task({
  id: "logging-example",
  run: async (payload: { data: Record<string, string> }) => {
    //the first parameter is the message, the second parameter must be a key-value object (Record<string, unknown>)
    logger.debug("Debug message", payload.data);
    logger.log("Log message", payload.data);
    logger.info("Info message", payload.data);
    logger.warn("You've been warned", payload.data);
    logger.error("Error message", payload.data);
  },
});
```

## Tracing and spans

Tracing is a way to follow the flow of your code. It's very useful for debugging and understanding how your code is working, especially with long-running or complex tasks.

Trigger.dev uses OpenTelemetry tracing under the hood. With automatic tracing for many things like task triggering, task attempts, HTTP requests, and more.

| Name          | Description                      |
| :------------ | :------------------------------- |
| Task triggers | Task triggers                    |
| Task attempts | Task attempts                    |
| HTTP requests | HTTP requests made by your code. |

### Adding instrumentations

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/auto-instrumentation.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c23b7b3b9b853d52af2850b732e576d7" alt="The run log" data-og-width="1442" width="1442" data-og-height="521" height="521" data-path="images/auto-instrumentation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/auto-instrumentation.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=d087748854dbe051414c3f842f183af8 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/auto-instrumentation.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c86e6cc078f69e7585836db0561eae15 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/auto-instrumentation.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c03cb732f67e320ac58efc3fd6001a66 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/auto-instrumentation.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=f91182e7070b80515e916f1401c40212 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/auto-instrumentation.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=6182199af22c75f77a02bdfb9a8d42d5 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/auto-instrumentation.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b161da0f8c3c970e234e7574c0042951 2500w" />

You can [add instrumentations](/config/config-file#instrumentations). The Prisma one above will automatically trace all Prisma queries.

### Add custom traces

If you want to add custom traces to your code, you can use the `logger.trace` function. It will create a new OTEL trace and you can set attributes on it.

```ts  theme={null}
import { logger, task } from "@trigger.dev/sdk";

export const customTrace = task({
  id: "custom-trace",
  run: async (payload) => {
    //you can wrap code in a trace, and set attributes
    const user = await logger.trace("fetch-user", async (span) => {
      span.setAttribute("user.id", "1");

      //...do stuff

      //you can return a value
      return {
        id: "1",
        name: "John Doe",
        fetchedAt: new Date(),
      };
    });

    const usersName = user.name;
  },
});
```
