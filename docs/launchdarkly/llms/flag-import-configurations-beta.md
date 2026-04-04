# Source: https://launchdarkly.com/docs/api/flag-import-configurations-beta.md

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

Flag import configurations allow you to import feature flags from another feature management system.

Use the flag import configuration endpoints to create, delete, and manage flag import configurations. You can import flags from other feature management tools into LaunchDarkly. For example, you can import flags from Split.io.

Several of the endpoints in the flag import configuration API require an integration ID. The integration ID is returned as part of the [Create a flag import configuration](https://launchdarkly.com/docs/api/flag-import-configurations-beta/create-flag-import-configuration) response, in the `_id` field. It is also returned as part of the [List all flag import configurations](https://launchdarkly.com/docs/api/flag-import-configurations-beta/get-flag-import-configurations) response, in the `_id` field of each element in the `items` array.

To learn more about flag import configurations, read [Import flags](https://launchdarkly.com/docs/home/flags/import).
