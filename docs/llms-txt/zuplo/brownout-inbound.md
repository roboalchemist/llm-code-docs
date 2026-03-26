# Source: https://www.zuplo.com/docs/policies/brownout-inbound.md

# Brown Out Policy

The brownout policy allows performing scheduled downtime on your API. This can
be useful for helping notify clients of an impending deprecation or for
scheduling maintenance.

This policy uses [cron schedules](https://crontab.guru) to check if a request
should experience a brownout or not. When a request falls into a scheduled
brownout an error response will be return. The error response can be customized
by setting the `problem` properties.

For more information using brownouts to alert clients on impending API
changes/deprecations see our blog post
[How to version an API](https://zuplo.com/blog/2022/05/17/how-to-version-an-api)

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-brownout-inbound-policy",
  "policyType": "brownout-inbound",
  "handler": {
    "export": "BrownoutInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "cronSchedule": "* 2 * * *",
      "problem": {
        "type": "https://example.com/problems/deprecation-announcement",
        "title": "Deprecation Test",
        "detail": "This is a temporary brownout every day between 02:00-03:00 to alert of an upcoming deprecation.",
        "status": 400
      }
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `brownout-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `BrownoutInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `cronSchedule` **(required)** <code className="text-green-600">&lt;undefined&gt;</code> - The cron schedule for when this policy is enabled. This can be a single cron string or an array of multiple cron strings.
- `problem` <code className="text-green-600">&lt;object&gt;</code> - The problem that is returned in the response body when this policy is enabled.
  - `type` <code className="text-green-600">&lt;string&gt;</code> - The type of problem.
  - `title` <code className="text-green-600">&lt;string&gt;</code> - The title of problem.
  - `detail` <code className="text-green-600">&lt;string&gt;</code> - The detail of problem.
  - `status` <code className="text-green-600">&lt;number&gt;</code> - Http status code of the problem.

## Using the Policy

## Cron Schedules

This policy accepts a single cron schedule or an array of cron schedules. Any
time a requests falls withing that schedule the brownout response will be set.

Example schedules could be:

**Every Day between 2am and 3am**

```json
"cronSchedule": "* 2 * * *"
```

**Every Hour on the hour, and the 15th, 30th, and 45th minutes**

```json
"cronSchedule": ["0 * * * *", "15 * * * *", "30 * * * *", "45 * * * *"]
```

This can also be written as:

```json
"cronSchedule": ["0/15 * * * *"]
```

## Cron Expression Format

This policy uses the
[linux cron syntax](https://man7.org/linux/man-pages/man5/crontab.5.html) with
the addition that you can optionally specify seconds by prepending the minute
field with another field.

```txt
┌───────────── second (0 - 59, optional)
│ ┌───────────── minute (0 - 59)
│ │ ┌───────────── hour (0 - 23)
│ │ │ ┌───────────── day of month (1 - 31)
│ │ │ │ ┌───────────── month (1 - 12)
│ │ │ │ │ ┌───────────── weekday (0 - 7)
* * * * * *
```

All linux cron features are supported, including

- lists
- ranges
- ranges in lists
- step values
- month names (jan,feb,... - case insensitive)
- weekday names (mon,tue,... - case insensitive)
- time nicknames (@yearly, @annually, @monthly, @weekly, @daily, @hourly - case
  insensitive)

To test out cron patterns try using a tool like
[crontab.guru](https://crontab.guru/).

Read more about [how policies work](/articles/policies)
