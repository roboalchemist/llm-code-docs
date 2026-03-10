# Source: https://www.inngest.com/docs-markdown/reference/typescript/v4/functions/step-sleep-until

# Sleep until `step.sleepUntil()`

Use `step.sleepUntil()` to pause your function's execution until a specific date and time. This is useful when you need to wait until a known point in time, such as the end of a trial period or a scheduled deadline.

## `step.sleepUntil(id, datetime): Promise`

- `id` (string): The ID of the step. This will be what appears in your function's logs and is used to memoize step state across function versions.

* `datetime` (Date | string | Temporal.Instant | Temporal.ZonedDateTime): The datetime at which to continue execution of your function. This can be:A Date objectAny date time string in the format accepted by the Date object, i.e. YYYY-MM-DDTHH:mm:ss.sssZ or simplified forms like YYYY-MM-DD or YYYY-MM-DDHH:mm:ssTemporal.InstantTemporal.ZonedDateTime

```ts
// Sleep until the new year
await step.sleepUntil("happy-new-year", "2024-01-01");

// Sleep until September ends
await step.sleepUntil("wake-me-up", "2023-09-30T11:59:59");

// Sleep until the end of the this week
const date = dayjs().endOf("week").toDate();
await step.sleepUntil("wait-for-end-of-the-week", date);

// Sleep until tea time in London
const teaTime = Temporal.ZonedDateTime.from("2025-05-01T16:00:00+01:00[Europe/London]");
await step.sleepUntil("british-tea-time", teaTime);

// Sleep until the end of the day
const now = Temporal.Now.instant();
const endOfDay = now.round({ smallestUnit: "day", roundingMode: "ceil" });
await step.sleepUntil("done-for-today", endOfDay);
```

> **Callout:** step.sleepUntil() must be called using await or some other Promise handler to ensure your function sleeps correctly.