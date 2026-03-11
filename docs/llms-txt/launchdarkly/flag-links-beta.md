# Source: https://launchdarkly.com/docs/api/flag-links-beta.md

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

Flag links let you view external mentions of flags from other tools and services. Links to external conversations and references to your flags allow you to collaborate more easily and quickly review relevant flag contexts. To learn more, read [Flag links](https://launchdarkly.com/docs/home/flags/links).

You can create custom flag links by associating an external URL with a feature flag. After you create a flag link, it applies across all your environments. You should use caution when you delete a flag link, because it will be deleted from all your environments.

With the flag links API, you can view, create, update, and delete links to flags.

Several of the endpoints in the flag links API require a flag link ID. The flag link ID is returned as part of the [Create flag link](https://launchdarkly.com/docs/api/flag-links-beta/create-flag-link) and [List flag links](https://launchdarkly.com/docs/api/flag-links-beta/get-flag-links) responses. It is the `_id` field, or the `_id` field of each element in the `items` array.
