# Source: https://launchdarkly.com/docs/api/users-beta.md

> ### Contexts are now available
>
> After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should use [Contexts](https://launchdarkly.com/docs/api/contexts) instead of these endpoints. To learn more, read [Contexts](https://launchdarkly.com/docs/home/observability/contexts).

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

LaunchDarkly creates a record for each user passed in to `variation` calls. This record powers the autocomplete functionality on the feature flag dashboard, as well as the Users page. To learn more, read [Contexts](https://launchdarkly.com/docs/home/observability/contexts)

LaunchDarkly also offers an API that lets you access this data. You can use the users API to see what user data is available to LaunchDarkly, as well as determine which flag values a user will receive. You can also explicitly set which flag value a user will receive with this API.

Users are always scoped within both a project and an environment. Each environment has its own set of user records.
