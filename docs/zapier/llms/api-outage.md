# Source: https://docs.zapier.com/platform/manage/api-outage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

> Zapier recognizes that temporary unavailability is sometimes inevitable for your API.

# null

To accommodate these situations, we recommend configuring [custom error response handling](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#general-errors) to:

* Present a meaningful, user-friendly message to users
* Refrain from disabling Zaps due to error-ratios
* Potentially reattempt the action after a given delay window

## 1. Default behavior

Zap runs that encounter a 5xx error from your API throw an exception and receive the “Stopped / Errored” status. This will [display an error message to the user](https://help.zapier.com/hc/en-us/articles/20505304170637-Review-Zap-run-statuses); allowing them to replay the Run.

If the user has [Autoreplay](https://help.zapier.com/hc/en-us/articles/8496241726989-Replay-failed-Zap-runs#how-autoreplay-works-0-4) enabled, then the errored steps will be retried on [a defined schedule](https://help.zapier.com/hc/en-us/articles/8496241726989-Replay-failed-Zap-runs#how-autoreplay-works-0-4). Only when all Autoreplay attempts have also failed will the Zap Run be assigned the “Stopped / Errored” status.

If [95% of a Zap's runs in the last 7 days are assigned the “Stopped / Errored” status](https://help.zapier.com/hc/en-us/articles/8496037690637-Troubleshoot-errors-in-Zapier#500-series-error-codes-0-3), the Zap will be paused automatically. The Zap will not run again until the user manually enables it.

## 2. Avoid automatic Zap disablement

### Platform CLI

When building in the [CLI](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md), you can [make use of HTTP middleware](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#using-http-middleware) to implement [custom error response handling](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#error-handling).

This allows you to write a single script that applies across the entire integration to detect a specific error from the API, and act accordingly. For example, if the API's outage duration is known, you could catch 503 responses during the `afterResponse` middleware and throw a [`ThrottledError`](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#handling-throttled-requests) like this:

```js  theme={null}
const yourAfterResponse = (resp) => {
  if (resp.status === 503) {
    throw new z.errors.ThrottledError(
      "Service is temporarily unavailable. Retrying in 60 seconds.",
      60,
    ); // Zapier will retry in 60 seconds
  }
  return resp;
};
```

> **Note:** You need to set [`skipThrowForStatus`](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#http-response-object) to `true` when invoking `z.request()`.

### Platform UI

When building in the [UI](https://developer.zapier.com/), custom error handling needs to be added to each individual element of the integration (authentication, triggers, actions) using [Code Mode](/platform/build/code-mode).

For example:

```js  theme={null}
const options = {
  url: `https://example.app/api/endpoint`,
  skipThrowForStatus: true,
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  params: {},
  body: {},
};

return z.request(options).then((response) => {
  if (response.status === 503) {
    throw new z.errors.ThrottledError(
      "Service is temporarily unavailable. Retrying in 60 seconds.",
      60,
    ); // Zapier will retry in 60 seconds
  }
  const results = response.json;
  return results;
});
```

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9f04386f19f0e9f7f107ea8d0d6e3b7.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=5c6af7c1711d92128de8834271dc7903" data-og-width="1570" width="1570" data-og-height="903" height="903" data-path="images/f9f04386f19f0e9f7f107ea8d0d6e3b7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9f04386f19f0e9f7f107ea8d0d6e3b7.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=e7db02b07260c4c08925e9c8b60d7a84 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9f04386f19f0e9f7f107ea8d0d6e3b7.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=774d28d3e2bc27f98b4fcd0c863436af 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9f04386f19f0e9f7f107ea8d0d6e3b7.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=8fb7b6e0cc991b9d3dfe4bf537947dd0 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9f04386f19f0e9f7f107ea8d0d6e3b7.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=2aa8f1fca7a3777e6e438fc360a69aa4 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9f04386f19f0e9f7f107ea8d0d6e3b7.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=3d06e1c8ff53e821ad714dae44547208 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/f9f04386f19f0e9f7f107ea8d0d6e3b7.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=a2d0fa394fc65c1ade48dd032ad9a2c9 2500w" />
</Frame>

> **Note:** Integrations built with the Zapier Platform UI can enable the *skipThrowForStatus* toggle under [Advanced/Settings](/platform/build/errors) to On to use [`skipThrowForStatus:true`](https://cdn.zappy.app/8ac6af91f6b27c4a473d566f1534b27e.png) on every request

## 3. Specify how long Zapier should wait before retrying

The `ThrottledError(message,delay)` method accepts two input parameters; a custom error message (string) and a delay expressed in seconds (integer).

Include a Retry-After header with responses provided by your API during downtime, to specify the amount of time until the service is expected to be back online and Zapier should retry the request. Your [custom error handling script](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#error-response-handling) can read this header and pass it to the delay parameter for `ThrottledError()`, like this:

```js  theme={null}
if (response.status === 503) {
  const delay = response.getHeader("retry-after");
  const message = `Service is temporarily unavailable. Retrying in ${delay} seconds.`;
  throw new z.errors.ThrottledError(message, delay);
}
```

## 4. Scheduled API maintenance

For periods of scheduled maintenance, a status of an app (API) as “unhealthy” can be set between a specific start and end time on request. A “Scheduled Maintenance” message will then be posted to our [status page](https://status.zapier.com) for [example](https://status.zapier.com/incidents/njgw7lrhn5hs).

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ae85a1cd6d00981ed30af8eede5938b.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=e0ba135b569542bd15a8fbc9e6c989f1" data-og-width="1556" width="1556" data-og-height="308" height="308" data-path="images/2ae85a1cd6d00981ed30af8eede5938b.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ae85a1cd6d00981ed30af8eede5938b.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=36b6c52d6329c8141ff78a4e22646103 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ae85a1cd6d00981ed30af8eede5938b.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=7be26de353598f9479c90ba96787b726 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ae85a1cd6d00981ed30af8eede5938b.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=f2708da7a22acfd774cc99f978d48b2b 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ae85a1cd6d00981ed30af8eede5938b.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=23709ed46b71f9a54a1dceacc5964bbb 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ae85a1cd6d00981ed30af8eede5938b.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=a36c2ebaac1b22edfa493386af0bdd1d 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/2ae85a1cd6d00981ed30af8eede5938b.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=bd59717eea6756f2463dca23da460de4 2500w" />
</Frame>

The app will also have a status of “unhealthy” on the [*App Status* tab.](https://status.zapier.com/#app-status)

During a set maintenance window, Zaps impacted by the downtime will be affected as follows:

**Actions/Searches:** Zap runs with affected actions/searches will have the status of “Playing” in the Zap History page. The action/search will be delayed until the incident resolves, or up to five times. On the fifth time, Zapier will attempt it regardless of the app status. If it fails, Zap runs will error and [normal manual replay mechanisms](https://help.zapier.com/hc/en-us/articles/8496241726989-Replay-failed-Zap-runs) can be used to try to replay any affected Zap runs.

**Triggers:** *most* Zaps with affected (polling) triggers won't run and so (for the most part) there will be no Zap runs in [Zap History](https://help.zapier.com/hc/en-us/articles/8496291148685-View-and-manage-your-Zap-history).

In more detail, Zapier will “skip” 90% of polls, allowing 10% through, so typically *some* runs will occur for *some* Zaps. After 15 minutes, all polling is re-enabled to check if the API is healthy again. If not, Zapier will again “skip” 90% of polls. This will be repeated until the API is healthy. Once the API is healthy, Zaps will be triggered and “catch up” on missed data, subject to normal polling limitations such as [pagination](/platform/build/trigger#how-to-use-pagination).

If Zap runs error users will be notified via email based on their [notification settings](https://help.zapier.com/hc/en-us/articles/8496289225229-Manage-notifications-when-errors-occur-in-Zaps).

If you would like to schedule a maintenance window for your app, please send across the following information to [Developer Support](https://developer.zapier.com/contact)

* Start date and time (in UTC)
* End date and time (in UTC)
* Further details about how the API will respond during the downtime if called; eg. will it return an [HTTP 503](https://www.webfx.com/web-development/glossary/http-status-codes/what-is-a-503-status-code/) “Service Unavailable” status code or not respond at all.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
