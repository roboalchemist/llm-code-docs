# Source: https://launchdarkly.com/docs/api/applications-beta.md

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

The applications API lets you create, update, delete, and search for applications and application versions.

Each application includes information about the app you're creating, and a set of versions of the app that you've released. You can use applications to target particular application versions in your feature flags more easily, and to handle unsupported application versions more gracefully.

In addition to creating applications through the applications API, you can also create applications in the LaunchDarkly user interface. To learn more, read [Applications and application versions](https://launchdarkly.com/docs/home/releases/applications). LaunchDarkly also creates applications and application versions automatically when a LaunchDarkly SDK evaluates a feature flag for a context that includes application information. To learn more, read [Automatic environment attributes](https://launchdarkly.com/docs/sdk/features/environment-attributes).

You can use an application in any project in your LaunchDarkly account.

### Filtering applications and application versions

The `filter` parameter supports the following operators: `equals`, `notEquals`, `anyOf`, `startsWith`.

You can also combine filters in the following ways:

- Use a comma (`,`) as an AND operator
- Use a vertical bar (`|`) as an OR operator
- Use parentheses (`()`) to group filters

#### Supported fields and operators

You can only filter certain fields in applications when using the `filter` parameter. Additionally, you can only filter some fields with certain operators.

When you search for applications, the `filter` parameter supports the following fields and operators:

|<div style="width:120px">Field</div> |Description |Supported operators |
|---|---|---|
|`key` | The application or application version key, a unique identifier |`equals`, `notEquals`, `anyOf` |
|`name` | The application name or application version name |`equals`, `notEquals`, `anyOf`, `startsWith` |
|`autoAdded` | Whether the application or application version was automatically created because it was included in a context when a LaunchDarkly SDK evaluated a feature flag, or was created through the LaunchDarkly UI or REST API |`equals`, `notEquals` |
|`kind` | The application kind, one of `mobile`, `server`, `browser`. Only available for [Get applications](https://launchdarkly.com/docs/api/applications-beta/get-applications). |`equals`, `notEquals`, `anyOf` |
|`supported` | Whether a mobile application version is supported or unsupported. Only available for [Get application versions by application key](https://launchdarkly.com/docs/api/applications-beta/get-application-versions).|`equals`, `notEquals` |

For example, the filter `?filter=kind anyOf ["mobile", "server"]` matches applications whose `kind` is either `mobile` or `server`. The filter is not case-sensitive.

The documented values for `filter` query parameters are prior to URL encoding. For example, the `[` in `?filter=kind anyOf ["mobile", "server"]` must be encoded to `%5B`.

### Sorting applications and application versions

LaunchDarkly supports the following fields for sorting:
- `name` sorts by application name.
- `creationDate` sorts by the creation date of the application.

By default, the sort is in ascending order. Use `-` to sort in descending order. For example, `?sort=name` sorts the response by application name in ascending order, and `?sort=-name` sorts in descending order.
