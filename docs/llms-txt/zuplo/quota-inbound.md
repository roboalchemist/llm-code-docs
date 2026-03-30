# Source: https://www.zuplo.com/docs/policies/quota-inbound.md

# Quota Policy

You can use the Quota policy to limit the number of requests that are allowed to
happen in a given time period (e.g., monthly). The policy can be applied the
users or based on custom keys.

It supports `monthly`, `weekly`, `daily` and `hourly` quotas. By default a
`requests` meter is incremented by 1 for every request but you can also quota by
other arbitrary meters; more on this below.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-quota-inbound-policy",
  "policyType": "quota-inbound",
  "handler": {
    "export": "QuotaInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "allowances": {
        "requests": 10
      },
      "period": "monthly",
      "quotaBy": "user",
      "quotaOnStatusCodes": "200-399"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `quota-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `QuotaInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `period` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The period of the quota. Allowed values are `hourly`, `daily`, `weekly`, `monthly`.
- `quotaBy` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The quota by. Allowed values are `user`, `function`. Defaults to `"user"`.
- `quotaAnchorMode` <code className="text-green-600">&lt;string&gt;</code> - How the policy determines the anchor date for ongoing quota cycles - defaults to `first-api-call` which uses the first API call for this key. Allowed values are `first-api-call`, `function`. Defaults to `"first-api-call"`.
- `allowances` <code className="text-green-600">&lt;object&gt;</code> - The allowances for the quota.
- `quotaOnStatusCodes` <code className="text-green-600">&lt;undefined&gt;</code> - A list of successful status codes and ranges "200-299, 304" that should trigger a quota increment. Defaults to `"200-299"`.
- `identifier` <code className="text-green-600">&lt;object&gt;</code> - The module and functions to dynamically set the anchor date and/or the key/allowances for this request.
  - `module` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Specifies the module to load your custom functions, in the format `$import(./modules/my-module)`. Defaults to `"$import(./modules/my-module)"`.
  - `getAnchorDateExport` <code className="text-green-600">&lt;string&gt;</code> - used when quotaAnchorMode is `function`. Specifies the export to load your custom function to get the anchor date. Defaults to `"getAnchorDate"`.
  - `getQuotaDetailExport` <code className="text-green-600">&lt;string&gt;</code> - used when quotaBy is `function`. Specifies the export to load your custom function to get the quota detail. Defaults to `"getQuotaDetail"`.

## Using the Policy

The Quota policy needs to know when to anchor the quota start date so that the
Zuplo runtime can know where in the quota cycle you are. By default the runtime
uses the `"quotaAnchorMode": "first-api-call"` which checks to see if we have an
existing quota record for this user or custom quota key and, if not, sets it
based on the time of the first API call for this key.

You can customize the subscription date by setting the `getAnchorDateExport`
function, more below under **Custom Anchor Date**.

## Quota Cycles / Periods

The quota periods run from the anchor date and **time** until the next matching
cycle. For `monthly` periods, if the anchor date is `2024-01-31 04:30Z` then the
quota cycle will terminate on the same day of the next month or the last day of
that month if it is a shorter month, at the same time. In this case the quota
cycle will reset on `2024-02-29 04:30Z` (because 2024 is a leap year).

`weekly` cycles shift on the same day of the next week, at the same time.

`daily` on the next day, at the same time.

`hourly` on the same minute, of the next hour.

## Custom Meters

You can set custom meters in the allowances property of the options to include
custom meters other than `requests`. For example, here we set a monthly
allowance of 10 `bananas`.

```json
{
  "name": "my-quota-inbound-policy",
  "policyType": "quota-inbound",
  "handler": {
    "export": "QuotaInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "period": "monthly",
      "quotaBy": "user",
      "allowances": {
        "bananas": 10
      }
    }
  }
}
```

For this to work you must tell the runtime how many `bananas` to increment in a
given request/response lifecycle. This is achieved by using the `setMeters`
method on the `QuotaInboundPolicy` class:

```ts
import { QuotaInboundPolicy } from "@zuplo/runtime";

// ...

QuotaInboundPolicy.setMeters(context, { bananas: 5, oranges: 3 });
```

This is typically invoked in a custom inbound or outbound policy or a handler.s

## Dynamic Quota Allowances and Keys

Like **Dynamic Rate Limiting**, Quota Keys and allowances can also be set
dynamically in Zuplo. This is achieved by setting the `identifier` module and
`getQuotaDetailExport` in your options:

```json
{
  "name": "my-quota-inbound-policy",
  "policyType": "quota-inbound",
  "handler": {
    "export": "QuotaInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "identifier": {
        "getQuotaDetailExport": "getQuotaDetail",
        "module": "$import(./modules/my-module)"
      },
      "quotaAnchorMode": "first-api-call",
      // Note this must be 'function' when using a custom detail function
      "quotaBy": "function"
    }
  }
}
```

If you wanted to key on a property from the user metadata, like organizationId
you might have a `getQuotaDetail` implementation that looks like this.

```ts
// ./modules/my-module.ts
import { GetQuotaDetailFunction } from "@zuplo/runtime";

export const getQuotaDetail: GetQuotaDetailFunction = async (
  request,
  context,
  policyName,
) => {
  return {
    key: request.user.data.organizationId,
    allowances: {
      bananas: 100,
    },
  };
};
```

Note that this method supports async calls and could be used to load quotas from
another API, but we would recommend caching the results for performance reasons.

## Custom Anchor Date

Similarly, the Anchor Date can be set programmatically - for example you may
load the 'subscription' start date from another database or API.

```json
{
  "name": "my-quota-inbound-policy",
  "policyType": "quota-inbound",
  "handler": {
    "export": "QuotaInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "identifier": {
        "getAnchorDateExport": "getAnchorDate",
        "module": "$import(./modules/my-module)"
      },
      // Note this must be 'function' when using a custom anchor date
      "quotaAnchorMode": "function",
      "quotaBy": "user"
    }
  }
}
```

```ts
// ./modules/my-module.ts
import { GetQuotaAnchorDateFunction } from "@zuplo/runtime";

export const getAnchorDate: GetQuotaAnchorDateFunction = async (
  request,
  context,
  policyName,
) => {
  // simple example fetch call, needs error handling, auth etc.
  const response = await fetch(
    `https://my-subs-api/subs/${request.user.data.organizationId}`,
  );
  const data = await response.json();

  return new Date(data.startDate);
};
```

Similarly, if you wanted to have a daily quota policy with the Anchor Date set
to 24 hours from the UTC start of the day (instead of based on the first API
request for this bucket) you could do the following:

```json
{
  "name": "my-quota-inbound-policy",
  "policyType": "quota-inbound",
  "handler": {
    "export": "QuotaInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "identifier": {
        "getAnchorDateExport": "getAnchorDate",
        "module": "$import(./modules/my-module)"
      },
      // Note this must be 'function' when using a custom anchor date
      "quotaAnchorMode": "function",
      "quotaBy": "user",
      "period": "daily"
    }
  }
}
```

With this function to set the anchor date:

```ts
import { GetQuotaAnchorDateFunction } from "@zuplo/runtime";

export const getAnchorDate: GetQuotaAnchorDateFunction = async (
  request,
  context,
  policyName,
) => {
  const anchorDate = getStartOfDayUTC(new Date());
  return anchorDate;
};

function getStartOfDayUTC(date: Date): Date {
  const utcDate = new Date(date.getTime());
  utcDate.setUTCHours(0, 0, 0, 0);
  return utcDate;
}
```

## Get Usage

You can also programmatically access the usage counts with the `getUsage` static
function on `QuotaInboundPolicy`. This call **must** occur **after** the
Quota-Inbound policy has executed.

```ts

const usage = QuotaInboundPolicy.getUsage(context, 'quota-policy-name');
context.log.info(usage);

// This would generate the following output:

{
  anchorDate: string;
  nextResetDate: string;
  meters: Record<string, number>;
}

// example

{
  anchorDate: "2023-08-20T03:05:05.493Z",
  nextResetDate: "2024-08-20T03:05:05.493Z",
  meters: {
    requests: 1,
    bananas: 10
  }

}
```

Note that if the quota has not yet been updated for a particular meter, the
meter will be undefined in the response.

Read more about [how policies work](/articles/policies)
