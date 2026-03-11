# Source: https://docs.base44.com/developers/backend/resources/backend-functions/automations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Automations

> Schedule recurring tasks and trigger functions automatically based on database events

<div className="dev-docs-banner">
  <div className="dev-docs-banner-content">
    <div className="dev-docs-banner-title">
      You're viewing developer documentation
    </div>

    <div className="dev-docs-banner-text">
      This documentation is for developers working with the Base44 developer platform. For information about automations in the app editor, see <a href="/Building-your-app/Creating-automations">Creating automations for your app</a>.
    </div>
  </div>
</div>

Automations allow [backend functions](/developers/backend/resources/backend-functions/overview) to run automatically on a schedule or in response to database events. Use automations to process data at regular intervals, handle entity changes, or execute one-time tasks at specific times.

Each backend function can have multiple automations attached, configured in the function's `function.jsonc` file. If you only have an `entry.ts` or `entry.js` file, you'll need to add this configuration file to use automations. Automations are [deployed atomically with the function code](#deploy-automations) when you run [`deploy`](/developers/references/cli/commands/deploy) or [`functions deploy`](/developers/references/cli/commands/functions-deploy).

## Automation types

Base44 supports 3 types of automations:

* **[Scheduled automations with cron](#cron)**: Use cron expressions for precise scheduling control.
* **[Scheduled automations with simple schedules](#simple-schedule)**: Configure recurring tasks by interval without cron expressions.
* **[Entity event automations](#entity-events)**: Trigger functions when database records are created, updated, or deleted.

## Common fields

### Common fields for all automations

All automation types share the following fields:

| Field           | Type      | Required | Description                                                                                     |
| --------------- | --------- | -------- | ----------------------------------------------------------------------------------------------- |
| `type`          | `string`  | Yes      | The automation type. Possible values: `"scheduled"` or `"entity"`.                              |
| `name`          | `string`  | Yes      | Unique identifier for the automation.                                                           |
| `description`   | `string`  | No       | Human-readable description.                                                                     |
| `function_args` | `object`  | No       | Arguments passed to the function when triggered. See [Function arguments](#function-arguments). |
| `is_active`     | `boolean` | No       | Whether the automation is enabled. Default: `true`.                                             |

### Common fields for scheduled automations

Both cron and simple scheduled automations share these additional fields:

| Field              | Type     | Required    | Description                                                                                                                                                           |
| ------------------ | -------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `schedule_mode`    | `string` | Yes         | Whether the schedule repeats. Possible values: `"recurring"` or `"one-time"`.                                                                                         |
| `schedule_type`    | `string` | Yes         | Scheduling method to use. Possible values: `"cron"` or `"simple"`.                                                                                                    |
| `ends_type`        | `string` | No          | When the recurring schedule should stop. Possible values: `"never"`, `"on"`, or `"after"`. Default: `"never"`.                                                        |
| `ends_on_date`     | `string` | Conditional | Date when the recurring schedule ends, inclusive, in UTC. Required when `ends_type` is `"on"`. Format: `YYYY-MM-DDTHH:MM:SSZ`. For example, `"2026-12-31T23:59:59Z"`. |
| `ends_after_count` | `number` | Conditional | Number of executions after which the recurring schedule stops. Required when `ends_type` is `"after"`.                                                                |

## Automation configuration

Configure automations in your `function.jsonc` file using one of the following approaches. All automations use the [common fields for all automations](#common-fields-for-all-automations) listed above, plus the fields specific to each type.

### Cron

Use [common fields for all automations](#common-fields-for-all-automations) and [common fields for scheduled automations](#common-fields-for-scheduled-automations) along with the cron-specific fields listed here.

Set `type` to `"scheduled"` and `schedule_type` to `"cron"` to use cron expressions for precise scheduling control.

Cron automations use standard 5-field syntax: `minute hour day-of-month month day-of-week`. See [crontab.guru](https://crontab.guru/) for an interactive cron expression editor and syntax reference.

| Field             | Type     | Required | Description              |
| ----------------- | -------- | -------- | ------------------------ |
| `cron_expression` | `string` | Yes      | 5-field cron expression. |

#### Example

This example runs a function every day at midnight UTC:

```jsonc  theme={null}
{
  "name": "sendDailyReport",
  "entry": "entry.ts",
  "automations": [
    {
      "type": "scheduled",
      "name": "daily_midnight_report",
      "description": "Runs every day at midnight UTC",
      "function_args": { "mode": "full_sync" },
      "is_active": true,
      
      "schedule_mode": "recurring",
      "schedule_type": "cron",
      "cron_expression": "0 0 * * ?"
    }
  ]
}
```

### Simple schedule

Use [common fields for all automations](#common-fields-for-all-automations) and [common fields for scheduled automations](#common-fields-for-scheduled-automations) along with the simple schedule fields listed here.

Set `type` to `"scheduled"` and `schedule_type` to `"simple"` for straightforward scheduling needs.

Configure recurring tasks by interval such as minutes, hours, days, weeks, or months without writing cron expressions.

| Field                    | Type       | Required    | Description                                                                                                                                                                |
| ------------------------ | ---------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `one_time_date`          | `string`   | Conditional | Date and time when the automation runs once, in UTC. Required when `schedule_mode` is `"one-time"`. Format: `YYYY-MM-DDTHH:MM:SSZ`. For example, `"2026-02-15T10:00:00Z"`. |
| `repeat_unit`            | `string`   | Conditional | Time unit for recurring automations. Required when `schedule_mode` is `"recurring"`. Possible values: `"minutes"`, `"hours"`, `"days"`, `"weeks"`, or `"months"`.          |
| `repeat_interval`        | `number`   | Conditional | Interval between executions. Required when `repeat_unit` is `"minutes"`, `"hours"`, or `"days"`.                                                                           |
| `start_time`             | `string`   | Conditional | Time of day when the automation runs, in UTC. Required when `repeat_unit` is `"days"`, `"weeks"`, or `"months"`. Format: `HH:MM`.                                          |
| `repeat_on_days`         | `number[]` | Conditional | Days of the week when the automation runs. Required when `repeat_unit` is `"weeks"`. Array of weekday numbers, where `0` is Sunday and `6` is Saturday.                    |
| `repeat_on_day_of_month` | `number`   | Conditional | Day of the month when the automation runs. Required when `repeat_unit` is `"months"`. Valid values: `1`-`31`.                                                              |

#### Examples

The following examples show different ways to schedule automations with simple schedules:

<CodeGroup>
  ```jsonc Every 30 minutes theme={null}
  {
    "type": "scheduled",
    "name": "every_30_minutes",
    "description": "Runs every 30 minutes.",
    "is_active": true,
    
    "schedule_mode": "recurring",
    "schedule_type": "simple",
    "repeat_unit": "minutes",
    "repeat_interval": 30
  }
  ```

  ```jsonc Weekdays at 9am theme={null}
  {
    "type": "scheduled",
    "name": "weekday_morning_report",
    "description": "Runs at 9 AM Monday through Friday.",
    "is_active": true,
    
    "schedule_mode": "recurring",
    "schedule_type": "simple",
    "repeat_unit": "weeks",
    "repeat_interval": 1,
    "start_time": "09:00",
    "repeat_on_days": [1, 2, 3, 4, 5],
    
    "ends_type": "after",
    "ends_after_count": 52
  }
  ```

  ```jsonc One-time execution theme={null}
  {
    "type": "scheduled",
    "name": "one_time_cleanup",
    "description": "Runs once at a specific date and time.",
    "function_args": { "cleanup": true },
    "is_active": true,
    
    "schedule_mode": "one-time",
    "schedule_type": "simple",
    "one_time_date": "2026-02-15T10:00:00Z"
  }
  ```
</CodeGroup>

### Entity events

Use [common fields for all automations](#common-fields-for-all-automations) along with the entity event fields listed here.

Set `type` to `"entity"` to trigger functions automatically when database records are created, updated, or deleted.

Entity automations can listen to 1 or more event types on a specific entity.

| Field         | Type       | Required | Description                                                                                              |
| ------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------- |
| `entity_name` | `string`   | Yes      | Name of the entity to monitor.                                                                           |
| `event_types` | `string[]` | Yes      | Database events to listen for. Possible values: `"create"`, `"update"`, `"delete"`. At least 1 required. |

#### Examples

The following examples show how to trigger functions based on entity events:

<CodeGroup>
  ```jsonc All order events theme={null}
  {
    "name": "processOrders",
    "entry": "entry.ts",
    "automations": [
      {
        "type": "entity",
        "name": "on_order_changes",
        "description": "Triggered on order create, update, or delete.",
        "function_args": { "notify_slack": true },
        "is_active": true,
        
        "entity_name": "orders",
        "event_types": ["create", "update", "delete"]
      }
    ]
  }
  ```

  ```jsonc New records only theme={null}
  {
    "type": "entity",
    "name": "on_customer_create",
    "description": "Triggered when a new customer is created.",
    "is_active": true,
    
    "entity_name": "customers",
    "event_types": ["create"]
  }
  ```
</CodeGroup>

### Function arguments

Pass data to your function when it's triggered by including the `function_args` field in your automation configuration. This is useful when one function handles multiple automations with different behaviors, such as a sync function that runs incrementally every 15 minutes but does a full sync daily.

Access these arguments in your function code through the request body.

#### Example

This example shows a function that handles both incremental and full sync modes based on the automation config:

<CodeGroup>
  ```typescript Function code theme={null}
  Deno.serve(async (req) => {
    const body = await req.json();
    const args = body.args ?? {};
    
    // Use the arguments from automation config
    const mode = args.mode ?? "incremental";
    
    // Your function logic
  });
  ```

  ```jsonc Automation config theme={null}
  {
    "name": "syncData",
    "entry": "entry.ts",
    "automations": [
      {
        "type": "scheduled",
        "name": "incremental_sync",
        "description": "Runs every 15 minutes with incremental mode.",
        "function_args": { "mode": "incremental" },
        "is_active": true,
        "schedule_mode": "recurring",
        "schedule_type": "simple",
        "repeat_unit": "minutes",
        "repeat_interval": 15
      },
      {
        "type": "scheduled",
        "name": "full_sync",
        "description": "Runs daily at midnight with full sync mode.",
        "function_args": { "mode": "full" },
        "is_active": true,
        "schedule_mode": "recurring",
        "schedule_type": "cron",
        "cron_expression": "0 0 * * ?"
      }
    ]
  }
  ```
</CodeGroup>

## Deploy automations

Deploy backend functions with their automations using the CLI [`functions deploy`](/developers/references/cli/commands/functions-deploy) command or the unified [`deploy`](/developers/references/cli/commands/deploy) command.

The deployment is atomic per function. A function is only considered deployed if both the Deno deployment and all its automations succeed. If any automation fails to deploy, the entire function deployment is rolled back.

After deploying, the CLI shows which functions were successfully deployed, deleted, or had errors. Functions missing locally but existing on Base44 are removed.

## Manage automations in the dashboard

<Warning>
  Any changes made in the dashboard will be overwritten the next time you run [`functions deploy`](/developers/references/cli/commands/functions-deploy). There is no two-way sync between the dashboard and your local files. Automations defined in your local `function.jsonc` files are the source of truth.

  If you want to make changes to your automations, update your local `function.jsonc` files and redeploy. Use the dashboard for monitoring execution logs and manually triggering automations when needed.
</Warning>

View and manage your automations in the Base44 dashboard under the **Automations** tab. From the dashboard, you can:

* View execution logs and history
* Run automations manually for testing
* Monitor automation status

## See also

* [Backend Functions](/developers/backend/resources/backend-functions/overview): Learn about backend functions
* [`functions deploy`](/developers/references/cli/commands/functions-deploy): Deploy functions with automations
* [`deploy`](/developers/references/cli/commands/deploy): Deploy all resources at once
* [`logs`](/developers/references/cli/commands/logs): View function logs


Built with [Mintlify](https://mintlify.com).