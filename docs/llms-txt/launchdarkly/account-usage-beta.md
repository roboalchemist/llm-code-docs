# Source: https://launchdarkly.com/docs/api/account-usage-beta.md

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

The account usage API lets you query for metrics about how your account is using LaunchDarkly. To learn more, read [Account usage metrics](https://launchdarkly.com/docs/home/account/metrics).

Each endpoint returns time-series data in the form of an array of data points with timestamps. Each one contains data for that time from one or more series. It also includes a metadata array describing what each of the series is.
