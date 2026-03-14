# Source: https://launchdarkly.com/docs/api/integration-delivery-configurations-beta.md


> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

The integration delivery configurations API allow you to create, modify, validate, and delete delivery configurations.

Several of the endpoints require a delivery configuration ID. The delivery configuration ID is returned as part of the [Create delivery configuration](https://launchdarkly.com/docs/api/integration-delivery-configurations-beta/create-integration-delivery-configuration) and [List all delivery configurations](https://launchdarkly.com/docs/api/integration-delivery-configurations-beta/get-integration-delivery-configurations) responses. It is the `_id` field, or the `_id` field of each element in the `items` array.
