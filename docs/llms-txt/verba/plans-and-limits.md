# Source: https://docs.verba.ink/guides/plans-and-limits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Plans and limits

> Complete plan matrix for premium features, usage limits, and API behavior.

## Premium quick answers

* API access is available on all plans (`/v1/response`, `/v1/image`).
* Full matrix (`verbs/msg-min/context/max-tokens`): Free `5/20/50/4096`, Plus `10/40/75/8192`, Pro `20/100/100/16384`, Ultra `40/unlimited/150/32768`.
* Free: `5` verbs, `20` msg/min, `50` context, `4096` max tokens.
* Plus: `10` verbs, `40` msg/min, `75` context, `8192` max tokens.
* Pro: `20` verbs, `100` msg/min, `100` context, `16384` max tokens.
* Ultra: `40` verbs, unlimited msg/min, `150` context, `32768` max tokens.
* Streaming (`stream: true`) is available on Plus/Pro/Ultra.

## Plan tiers

Verba currently supports four tiers:

* `free`
* `plus`
* `pro`
* `ultra`

Quick reference (context/tokens):

* Free: `50` / `4096`
* Plus: `75` / `8192`
* Pro: `100` / `16384`
* Ultra: `150` / `32768`

## Feature matrix

| Feature                                            | Free      | Plus        | Pro               | Ultra                     |
| -------------------------------------------------- | --------- | ----------- | ----------------- | ------------------------- |
| Monthly credit allowance                           | `0`       | `2.5`       | `5`               | `10`                      |
| Max verbs                                          | `5`       | `10`        | `20`              | `40`                      |
| Message rate limit (per minute)                    | `20`      | `40`        | `100`             | `Unlimited`               |
| Max model context                                  | `50`      | `75`        | `100`             | `150`                     |
| Max response tokens                                | `4096`    | `8192`      | `16384`           | `32768`                   |
| API access (`/v1/response`, `/v1/image`)           | Yes       | Yes         | Yes               | Yes                       |
| API streaming (`/v1/response` with `stream: true`) | No        | Yes         | Yes               | Yes                       |
| Default model tier access                          | Free      | Free + Plus | Free + Plus + Pro | Free + Plus + Pro + Ultra |
| Watermark removal                                  | No        | Yes         | Yes               | Yes                       |
| Advanced AI flag                                   | No        | No          | Yes               | Yes                       |
| Early feature access                               | No        | Yes         | Yes               | Yes                       |
| VIP support                                        | No        | No          | No                | Yes                       |
| Image generations per month                        | Unlimited | Unlimited   | Unlimited         | Unlimited                 |

<Note>
  These values are enforced by backend tier feature controls and can be updated
  over time.
</Note>

## What each limit changes

* `Max verbs`: how many verbs you can create on your account.
* `Message rate limit`: per-user server-side throttle window.
* `Max model context`: max recent-message window your verb can use.
* `Max response tokens`: cap for generated response length.
* `Monthly credit allowance`: recurring included credit amount tied to tier.

## Behavior when you exceed limits

* Verb creation over your tier cap is rejected.
* Model context above your cap is clamped or rejected depending on endpoint.
* Free tier streaming requests return a plan-upgrade error.
* Message bursts above tier limits return rate-limit responses.

## Model access and tiering

Model availability is tier-controlled. If a selected model is not available for
your current tier, the system may remap/fallback to an allowed model.

## Patreon and plan sync

Premium tier is synced from Patreon membership data. On tier changes:

* Your account tier is updated.
* Model access can be adjusted.
* Monthly allowance logic follows tier/cycle rules.

If you unlink Patreon while a premium subscription is active, disconnection may
be blocked for account safety/billing consistency.

## Related guides

* [Credits and billing](/guides/credits)
* [Billing and refunds](/guides/billing-and-refunds)
* [AI engine settings](/guides/ai-engine)
* [Troubleshooting](/guides/troubleshooting)

Built with [Mintlify](https://mintlify.com).
