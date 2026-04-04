Source: https://docs.slack.dev/tools/deno-slack-sdk/guides/utilizing-slack-and-custom-data-types

# Utilizing Slack & custom data types

Workflow apps require a paid plan

Join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

When building workflow apps, you can use a handful of Slack types. You can also [define your own custom type](/tools/deno-slack-sdk/guides/creating-a-custom-type).

## Slack types {#slack}

Slack types are used in two ways: as input and output parameters of [Slack functions](/tools/deno-slack-sdk/guides/creating-slack-functions) & [custom functions](/tools/deno-slack-sdk/guides/creating-custom-functions), as well as attributes of [datastores](/tools/deno-slack-sdk/guides/using-datastores).

All manifests can be written in JSON; however, declaring types in an app using the Deno Slack SDK is done differently, requiring a reference to the `Schema.slack` package for non-primitive types. The examples in the reference show both how would they appear in Typescript as they would appear in a Deno Slack SDK app and in JSON as they would be defined in a manifest.

➡️ [View the full Slack types reference catalog here](/tools/deno-slack-sdk/reference/slack-types)

## Custom types {#custom}

Custom types provide a way to introduce reusable, sharable types to your workflow apps. Once registered in your manifest, you can use custom types as input or output parameters in any of your app's [functions](/tools/deno-slack-sdk/guides/creating-slack-functions), [workflows](/tools/deno-slack-sdk/guides/creating-workflows), or [datastores](/tools/deno-slack-sdk/guides/using-datastores). The possibilities are endless!

➡️ To learn how to create your own custom type, read our [Creating a custom type](/tools/deno-slack-sdk/guides/creating-a-custom-type) guide.
