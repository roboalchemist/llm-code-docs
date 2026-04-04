# Source: https://www.inngest.com/docs-markdown/guides/delayed-functions

# Delayed Functions

You can easily run functions in the future with Inngest. There are three ways to delay function execution:

- [**Sleep for a duration**](#sleep-for-a-duration) — Pause mid-function for a set amount of time using `step.sleep()`
- [**Sleep until a specific time**](#sleep-until-a-specific-time) — Pause mid-function until a date/time using `step.sleepUntil()`
- [**Schedule a function for later**](#schedule-a-function-for-later) — Delay when a function is first invoked by setting the event's `ts` field

Delays can be up to a year (up to seven days on the free plan). There are some benefits to delaying functions using Inngest:

- It works across any provider or platform
- Delays are durable and work across server restarts, serverless functions, and redeploys
- You can schedule functions into the far future
- Serverless functions are fully supported on all platforms
- Our SDK bypasses serverless function timeouts on all platforms
- You never need to manage queues or backlogs

### Platform support

**This works across all providers and platforms**, whether you run serverless functions or use servers like express.  **It also bypasses serverless function timeouts** on all platforms, so you can sleep for a longer time than your provider supports.

## Sleep for a duration

You can pause a function for a set amount of time using the [`step.sleep()`](/docs-markdown/reference/functions/step-sleep) method:

```ts
import { Inngest } from "inngest";

const inngest = new Inngest({ id: "signup-flow" });

export const fn = inngest.createFunction(
  { id: "send-signup-email" },
  { event: "app/user.created" },
  async ({ event, step }) => {
    await step.sleep("wait-a-moment", "1 hour");
    await step.run("do-some-work-in-the-future", async () => {
      // This runs after 1 hour
    });
  }
);
```

For more information on `step.sleep()` read [the reference](/docs-markdown/reference/functions/step-sleep).

## Sleep until a specific time

You can pause a function until a specific time using the [`step.sleepUntil()`](/docs-markdown/reference/functions/step-sleep-until) method:

```ts
import { Inngest } from "inngest";

const inngest = new Inngest({ id: "signup-flow" });

export const fn = inngest.createFunction(
  { id: "send-signup-email" },
  { event: "app/user.created" },
  async ({ event, step }) => {
    await step.sleepUntil("wait-for-iso-string", "2023-04-01T12:30:00");

    // You can also sleep until a timestamp within the event data.  This lets you
    // pass in a time for you to run the job:
    await step.sleepUntil("wait-for-timestamp", event.data.run_at); // Assuming event.data.run_at is a timestamp.

    await step.run("do-some-work-in-the-future", async () => {
      // This runs at the specified time.
    });
  }
);
```

For more information on `step.sleepUntil()` [read the reference](/docs-markdown/reference/functions/step-sleep-until).

You can pause a function for a set amount of time using the [`step.Sleep()`](https://pkg.go.dev/github.com/inngest/inngestgo@v0.7.4/step#Sleep) method:

```go
import (
	"context"
	"time"

	"github.com/inngest/inngestgo"
	"github.com/inngest/inngestgo/step"
)

func loadSendSignUpEmailInngestFn(client inngestgo.Client) (inngestgo.ServableFunction, error) {
	return inngestgo.CreateFunction(
		client,
		inngestgo.FunctionOpts{
			ID: "send-signup-email",
		},
		inngestgo.EventTrigger("app/user.created", nil),
		func(ctx context.Context, input inngestgo.Input[map[string]any]) (any, error) {
			// business logic
			_, err := step.Run(ctx, "send-the-user-a-signup-email", func(ctx context.Context) (any, error) {
				return SendEmail(SendEmailInput{
					To:      input.Event.Data["user_email"].(string),
					Subject: "Welcome to Inngest!",
					Message: "...",
				})
			})
			if err != nil {
				return nil, err
			}

			step.Sleep(ctx, "wait-for-the-future", 4*time.Hour)

			_, err = step.Run(ctx, "do-some-work-in-the-future", func(ctx context.Context) (any, error) {
				// Code here runs in the future automatically.
				return nil, nil
			})
			return nil, err
		},
	)
}
```

For more information on `step.sleep()` read [the reference](https://pkg.go.dev/github.com/inngest/inngestgo@v0.7.4/step#Sleep).

You can pause a function for a set amount of time using the [`step.sleep()`](http://localhost:3001/docs-markdown/reference/python/steps/sleep) method:

```python
import inngest
from src.inngest.client import inngest_client
from datetime import timedelta

@inngest_client.create_function(
    fn_id="send-signup-email", 
    trigger=inngest.TriggerEvent(event="app/user.created")
)
async def send_signup_email(ctx: inngest.Context):
    
    await ctx.step.sleep("wait-for-the-future", timedelta(hours=4))

    async def future_work():
        # Code here runs in the future automatically
        pass

    await ctx.step.run("do-some-work-in-the-future", future_work)
```

For more information on `step.sleep()` read [the reference](/docs-markdown/reference/functions/step-sleep).

## Sleep until a specific time

You can pause a function until a specific time using the [`step.sleep_until()`](/docs-markdown/reference/python/steps/sleep-until) method:

```python
import inngest
from src.inngest.client import inngest_client

inngest_client = inngest.Inngest(
    app_id="my-app",
)

@inngest_client.create_function(
    fn_id="send-signup-email", 
    trigger=inngest.TriggerEvent(event="app/user.created")
)
async def send_signup_email(ctx: inngest.Context):
    async def send_email():
        await sesclient.send_email(
            to=ctx.event.data["user_email"],
            subject="Welcome to Inngest!",
            message="..."
        )
    
    await ctx.step.run("send-the-user-a-signup-email", send_email)
    
    await ctx.step.sleep_until("wait-for-the-future", "2023-02-01T16:30:00")

    async def future_work():
        # Code here runs in the future automatically
        pass

    await ctx.step.run("do-some-work-in-the-future", future_work)
```

For more information on `step.sleep_until()` [read the reference](/docs-markdown/reference/python/steps/sleep-until).

## Schedule a function for later

You can also delay when a function starts by setting the `ts` field in the [event payload](/docs-markdown/events#event-payload-format) to a future timestamp (milliseconds since the Unix epoch). Unlike `step.sleep()` or `step.sleepUntil()` which add delays *within* a function, the `ts` field delays the *start* of the function run itself.

For example, to schedule a function to run 5 minutes from now:

```typescript
await inngest.send({
  name: "notifications/reminder.scheduled",
  data: {
    user: { email: "johnny.utah@fbi.gov" },
    message: "Don't forget to catch the wave at 3pm",
  },
  // Include the timestamp for 5 minutes in the future:
  ts: Date.now() + 5 * 60 * 1000,
});
```

For a complete walkthrough, see the [Scheduling a one-off function](/docs-markdown/examples/scheduling-one-off-function) example.

## How it works

### `step.sleep()` and `step.sleepUntil()`

With `step.sleep()` and `step.sleepUntil()`, **the function controls when it runs**. You control the flow of your code by calling `sleep` or `sleepUntil` within your function directly, instead of using the queue to manage your code's timing. This keeps your logic together and makes your code easier to modify.

Inngest *stops the function from running* for whatever time is specified. When you call `step.sleep` or `step.sleepUntil` the function automatically stops running any future work. The function then tells the Inngest executor that it should be re-invoked at a future time. We re-call the function at the next step, skipping any previous work. This is how we bypass serverless function time limits and work across server restarts or redeploys.

### Event `ts` field

When you set the `ts` field on an event to a future Unix timestamp, Inngest delays invoking the function until that time. The function itself runs normally — the delay happens before it starts, not within it. This is useful when the delay is known at the time the event is sent and you don't need any logic to run before the wait.