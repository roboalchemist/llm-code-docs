# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-06-23-auto-privs-app-spec.md

# Jun 23, 2025: Snowflake Native App Framework updates

The Snowflake Native App Framework now includes the following features that make it easier for providers
to develop an app to create objects in a consumer account. These features also
make it easier for consumers to configure an app during installation and upgrade.

For general information on these features, see [Create and access objects in a consumer account](../../../developer-guide/native-apps/requesting-about.md).

## Automated granting of privileges (*Preview*)

This feature allows providers to specify in the manifest file the privileges required by an app.
When a consumer installs or upgrades an app, Snowflake grants these privileges to the app. For
more information, see [Configure the privileges required by an app](../../../developer-guide/native-apps/requesting-auto-privs.md).

Consumers can use feature policies to override the automatic grants for an app. For more
information, see [Use feature policies to limit the objects an app can create](../../../developer-guide/native-apps/ui-consumer-feature-policies.md).

## App specifications (*Preview*)

App specifications allow providers to request permission from the consumer to allow connections
outside Snowflake that use external access integrations or security integrations. Consumers must
approve the app specification for these objects when configuring the app after installation or
upgrade.

For more information, see [Overview of app specifications](../../../developer-guide/native-apps/requesting-app-specs.md).
