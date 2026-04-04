# Source: https://docs.upsun.com/environments/cancel-activity.md

# Cancel an activity

If you have a stuck activity or you pushed a change you know doesn't work,
you can cancel a running or pending activity on an environment.
This works for activities such as builds, cron jobs, and source operations.

You can cancel activities using the [CLI](https://docs.upsun.com../administration/cli.md)
or in the [Console](https://docs.upsun.com../administration/web.md).

If you have more than one running or pending activity, choose which activity to cancel.
You can also cancel a specific activity by specifying its ID:

```bash {}
upsun activity:cancel <ACTIVITY_ID>
```

Get the ID from the [activity log](https://docs.upsun.com/increase-observability/logs/access-logs.md#activity-logs).

 - Open the environment where you want to cancel an activity.
 - In the [activity log](https://docs.upsun.com/increase-observability/logs/access-logs.md#activity-logs),
click More **More** next to the activity you want to cancel.
 - Click **Cancel**.

## Non-cancellable activities

An activity can finish in between when you load the Console and when you click **Cancel**.
For example, when the activity is a [source operation](https://docs.upsun.com../create-apps/source-operations.md)
and the related build hook has already completed.
In such cases, you get a message that the activity can't be cancelled.

