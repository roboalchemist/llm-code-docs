# Source: https://trigger.dev/docs/tasks/scheduled.md

# Scheduled tasks (cron)

> A task that is triggered on a recurring schedule using cron syntax.

<Note>
  Scheduled tasks are only for recurring tasks. If you want to trigger a one-off task at a future
  time, you should [use the delay option](/triggering#delay).
</Note>

## Defining a scheduled task

This task will run when any of the attached schedules trigger. They have a predefined payload with some useful properties:

```ts  theme={null}
import { schedules } from "@trigger.dev/sdk";

export const firstScheduledTask = schedules.task({
  id: "first-scheduled-task",
  run: async (payload) => {
    //when the task was scheduled to run
    //note this will be slightly different from new Date() because it takes a few ms to run the task
    console.log(payload.timestamp); //is a Date object

    //when the task was last run
    //this can be undefined if it's never been run
    console.log(payload.lastTimestamp); //is a Date object or undefined

    //the timezone the schedule was registered with, defaults to "UTC"
    //this is in IANA format, e.g. "America/New_York"
    //See the full list here: https://cloud.trigger.dev/timezones
    console.log(payload.timezone); //is a string

    //If you want to output the time in the user's timezone do this:
    const formatted = payload.timestamp.toLocaleString("en-US", {
      timeZone: payload.timezone,
    });

    //the schedule id (you can have many schedules for the same task)
    //using this you can remove the schedule, update it, etc
    console.log(payload.scheduleId); //is a string

    //you can optionally provide an external id when creating the schedule
    //usually you would set this to a userId or some other unique identifier
    //this can be undefined if you didn't provide one
    console.log(payload.externalId); //is a string or undefined

    //the next 5 dates this task is scheduled to run
    console.log(payload.upcoming); //is an array of Date objects
  },
});
```

You can see from the comments that the payload has several useful properties:

* `timestamp` - the time the task was scheduled to run, as a UTC date.
* `lastTimestamp` - the time the task was last run, as a UTC date.
* `timezone` - the timezone the schedule was registered with, defaults to "UTC". In IANA format, e.g. "America/New\_York".
* `scheduleId` - the id of the schedule that triggered the task
* `externalId` - the external id you (optionally) provided when creating the schedule
* `upcoming` - the next 5 times the task is scheduled to run

<Note>
  This task will NOT get triggered on a schedule until you attach a schedule to it. Read on for how
  to do that.
</Note>

Like all tasks they don't have timeouts, they should be placed inside a [/trigger folder](/config/config-file), and you [can configure them](/tasks/overview#defining-a-task).

## How to attach a schedule

Now that we've defined a scheduled task, we need to define when it will actually run. To do this we need to attach one or more schedules.

There are two ways of doing this:

* **Declarative:** defined on your `schedules.task`. They sync when you run the dev command or deploy.
* **Imperative:** created from the dashboard or by using the imperative SDK functions like `schedules.create()`.

<Info>
  A scheduled task can have multiple schedules attached to it, including a declarative schedule
  and/or many imperative schedules.
</Info>

### Declarative schedules

These sync when you run the [dev](/cli-dev) or [deploy](/cli-deploy) commands.

To create them you add the `cron` property to your `schedules.task()`. This property is optional and is only used if you want to add a declarative schedule to your task:

```ts  theme={null}
export const firstScheduledTask = schedules.task({
  id: "first-scheduled-task",
  //every two hours (UTC timezone)
  cron: "0 */2 * * *",
  run: async (payload, { ctx }) => {
    //do something
  },
});
```

If you use a string it will be in UTC. Alternatively, you can specify a timezone like this:

```ts  theme={null}
export const secondScheduledTask = schedules.task({
  id: "second-scheduled-task",
  cron: {
    //5am every day Tokyo time
    pattern: "0 5 * * *",
    timezone: "Asia/Tokyo",
    //optional, defaults to all environments
    //possible values are "PRODUCTION", "STAGING", "PREVIEW" and "DEVELOPMENT"
    environments: ["PRODUCTION", "STAGING"],
  },
  run: async (payload) => {},
});
```

When you run the [dev](/cli-dev) or [deploy](/cli-deploy) commands, declarative schedules will be synced. If you add, delete or edit the `cron` property it will be updated when you run these commands. You can view your schedules on the Schedules page in the dashboard.

### Imperative schedules

Alternatively you can explicitly attach schedules to a `schedules.task`. You can do this in the Schedules page in the dashboard by just pressing the "New schedule" button, or you can use the SDK to create schedules.

The advantage of imperative schedules is that they can be created dynamically, for example, you could create a schedule for each user in your database. They can also be activated, disabled, edited, and deleted without deploying new code by using the SDK or dashboard.

To use imperative schedules you need to do two things:

1. Define a task in your code using `schedules.task()`.
2. Attach 1+ schedules to the task either using the dashboard or the SDK.

## Supported cron syntax

```
*    *    *    *    *
┬    ┬    ┬    ┬    ┬
│    │    │    │    |
│    │    │    │    └ day of week (0 - 7, 1L - 7L) (0 or 7 is Sun)
│    │    │    └───── month (1 - 12)
│    │    └────────── day of month (1 - 31, L)
│    └─────────────── hour (0 - 23)
└──────────────────── minute (0 - 59)
```

"L" means the last. In the "day of week" field, 1L means the last Monday of the month. In the "day of month" field, L means the last day of the month.

We do not support seconds in the cron syntax.

## When schedules won't trigger

There are two situations when a scheduled task won't trigger:

* For Dev environments scheduled tasks will only trigger if you're running the dev CLI.
* For Staging/Production environments scheduled tasks will only trigger if the task is in the current deployment (latest version). We won't trigger tasks from previous deployments.

## Attaching schedules in the dashboard

You need to attach a schedule to a task before it will run on a schedule. You can attach static schedules in the dashboard:

<Steps>
  <Step title="Go to the Schedules page">
    In the sidebar select the "Schedules" page, then press the "New schedule" button. Or you can
    follow the onboarding and press the create in dashboard button. <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-blank.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=43eb999c7adffee996282649787537ac" alt="Blank schedules
    page" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/schedules-blank.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-blank.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=fe91c092419f97fabd87bc978b02ef70 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-blank.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=80f88b80434b611ce1c3d496563c6986 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-blank.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=366e55c6afcfd9a36a16d94ef5bb7453 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-blank.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=d3cc50242dbdd1bb6f035caeb20c91c6 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-blank.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8b38dec234ab37de05949645ac5bd3e6 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-blank.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=bc86e5670d9c0b0c85cb3db0cde6bfbe 2500w" />
  </Step>

  <Step title="Create your schedule">
    Fill in the form and press "Create schedule" when you're done. <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-create.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c958b2628029237508df655d4e893d1e" alt="Environment variables
    page" data-og-width="1600" width="1600" data-og-height="901" height="901" data-path="images/schedules-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-create.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=5ebfd52f0aa7804335db8b6cc77dd13f 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-create.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a0bddf8862294445a0c3b6d2140ddffd 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-create.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=04fa4d04c0490f38d0b243f2588e00f3 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-create.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=0895d4a4306bbd55f91173c4b365c6e2 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-create.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=21b3fc532d0bdce094542b94a20e915c 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-create.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=06ce41644450d0f6bc12745c26e8859b 2500w" />

    These are the options when creating a schedule:

    | Name              | Description                                                                                   |
    | ----------------- | --------------------------------------------------------------------------------------------- |
    | Task              | The id of the task you want to attach to.                                                     |
    | Cron pattern      | The schedule in cron format.                                                                  |
    | Timezone          | The timezone the schedule will run in. Defaults to "UTC"                                      |
    | External id       | An optional external id, usually you'd use a userId.                                          |
    | Deduplication key | An optional deduplication key. If you pass the same value, it will update rather than create. |
    | Environments      | The environments this schedule will run in.                                                   |
  </Step>
</Steps>

## Attaching schedules with the SDK

You call `schedules.create()` to create a schedule from your code. Here's the simplest possible example:

```ts  theme={null}
const createdSchedule = await schedules.create({
  //The id of the scheduled task you want to attach to.
  task: firstScheduledTask.id,
  //The schedule in cron format.
  cron: "0 0 * * *",
  //this is required, it prevents you from creating duplicate schedules. It will update the schedule if it already exists.
  deduplicationKey: "my-deduplication-key",
});
```

<Note>The `task` id must be a task that you defined using `schedules.task()`.</Note>

You can create many schedules with the same `task`, `cron`, and `externalId` but only one with the same `deduplicationKey`.

This means you can have thousands of schedules attached to a single task, but only one schedule per `deduplicationKey`. Here's an example with all the options:

```ts  theme={null}
const createdSchedule = await schedules.create({
  //The id of the scheduled task you want to attach to.
  task: firstScheduledTask.id,
  //The schedule in cron format.
  cron: "0 0 * * *",
  // Optional, it defaults to "UTC". In IANA format, e.g. "America/New_York".
  // In this case, the task will run at midnight every day in New York time.
  // If you specify a timezone it will automatically work with daylight saving time.
  timezone: "America/New_York",
  //Optionally, you can specify your own IDs (like a user ID) and then use it inside the run function of your task.
  //This allows you to have per-user cron tasks.
  externalId: "user_123456",
  //You can only create one schedule with this key.
  //If you use it twice, the second call will update the schedule.
  //This is useful because you don't want to create duplicate schedules for a user.
  deduplicationKey: "user_123456-todo_reminder",
});
```

See [the SDK reference](/management/schedules/create) for full details.

### Dynamic schedules (or multi-tenant schedules)

By using the `externalId` you can have schedules for your users. This is useful for things like reminders, where you want to have a schedule for each user.

A reminder task:

```ts /trigger/reminder.ts theme={null}
import { schedules } from "@trigger.dev/sdk";

//this task will run when any of the attached schedules trigger
export const reminderTask = schedules.task({
  id: "todo-reminder",
  run: async (payload) => {
    if (!payload.externalId) {
      throw new Error("externalId is required");
    }

    //get user using the externalId you used when creating the schedule
    const user = await db.getUser(payload.externalId);

    //send a reminder email
    await sendReminderEmail(user);
  },
});
```

Then in your backend code, you can create a schedule for each user:

```ts Next.js API route theme={null}
import { reminderTask } from "~/trigger/reminder";

//app/reminders/route.ts
export async function POST(request: Request) {
  //get the JSON from the request
  const data = await request.json();

  //create a schedule for the user
  const createdSchedule = await schedules.create({
    task: reminderTask.id,
    //8am every day
    cron: "0 8 * * *",
    //the user's timezone
    timezone: data.timezone,
    //the user id
    externalId: data.userId,
    //this makes it impossible to have two reminder schedules for the same user
    deduplicationKey: `${data.userId}-reminder`,
  });

  //return a success response with the schedule
  return Response.json(createdSchedule);
}
```

You can also retrieve, list, delete, deactivate and re-activate schedules using the SDK. More on that later.

## Testing schedules

You can test a scheduled task in the dashboard. Note that the `scheduleId` will always come through as `sched_1234` to the run.

<Steps>
  <Step title="Go to the Test page">
    In the sidebar select the "Test" page, then select a scheduled task from the list (they have a
    clock icon on them) <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=6591163dd3e4af384746705dffef6c92" alt="Test page" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/schedules-test.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=ec7027a656655d186e0ee7b8d4d858ad 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=7616d494747c8f9038be012668f3a238 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=23eb128eee342e40a3826b05c006c029 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f7fdc2ee3775b41361ae411022a37f53 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=4261839b6f2f2c8f1c2c360108c16f33 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=82ac96f5c94674e853545cb60285b38a 2500w" />
  </Step>

  <Step title="Create your schedule">
    Fill in the form \[1]. You can select from a recent run \[2] to pre-populate the fields. Press "Run
    test" when you're ready <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test-form.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=0b2a0947db2701825addb703f92748a1" alt="Schedule test form" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/schedules-test-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test-form.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=3031563444d48852d76c67b95a4f5139 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test-form.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=1455997fee472ae6934f5d96ba2e1a2e 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test-form.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=5be53628561e1c9ae50228cef28ffac6 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test-form.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=aa2f6a789d838b7afb13ad77f6305143 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test-form.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f833cb1540671e10b2a9aebda6fd0b9c 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/schedules-test-form.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8878736225374e8cc8ddd0d8227a596a 2500w" />
  </Step>
</Steps>

## Managing schedules with the SDK

### Retrieving an existing schedule

```ts  theme={null}
const retrievedSchedule = await schedules.retrieve(scheduleId);
```

See [the SDK reference](/management/schedules/retrieve) for full details.

### Listing schedules

```ts  theme={null}
const allSchedules = await schedules.list();
```

See [the SDK reference](/management/schedules/list) for full details.

### Updating a schedule

```ts  theme={null}
const updatedSchedule = await schedules.update(scheduleId, {
  task: firstScheduledTask.id,
  cron: "0 0 1 * *",
  externalId: "ext_1234444",
  deduplicationKey: "my-deduplication-key",
});
```

See [the SDK reference](/management/schedules/update) for full details.

### Deactivating a schedule

```ts  theme={null}
const deactivatedSchedule = await schedules.deactivate(scheduleId);
```

See [the SDK reference](/management/schedules/deactivate) for full details.

### Activating a schedule

```ts  theme={null}
const activatedSchedule = await schedules.activate(scheduleId);
```

See [the SDK reference](/management/schedules/activate) for full details.

### Deleting a schedule

```ts  theme={null}
const deletedSchedule = await schedules.del(scheduleId);
```

See [the SDK reference](/management/schedules/delete) for full details.

### Getting possible timezones

You might want to show a dropdown menu in your UI so your users can select their timezone. You can get a list of all possible timezones using the SDK:

```ts  theme={null}
const timezones = await schedules.timezones();
```

See [the SDK reference](/management/schedules/timezones) for full details.
