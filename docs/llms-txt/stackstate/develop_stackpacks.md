# Source: https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/develop_stackpacks.md

# How to create a StackPack

## When to create a StackPack

As a rule of thumb each integration should have a StackPack. Without configuration StackState doesn't process incoming topology, telemetry or trace data. Such data will be accepted by StackState, but won't automatically reflect on the 4T data model. The best way to bundle configuration is through a StackPack. StackState can also be configured using the CLI, UI or directly via the API, but then your configuration won't be protected from user changes, can't easily be upgraded and can't easily be used for configuring multiple instances of an integration.

## How to create a StackPack

Refer to:

* [Prepare a StackPack package](https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/prepare_package)
* [How to customize a StackPack](https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/how_to_customize_a_stackpack)
* [How to get a template file](https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/how_to_get_a_template_file)
* [Prepare a StackPack provisioning script](https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/prepare_stackpack_provisioning_script)
* [How to pack and upload a StackPack](https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/how_to_pack_and_upload_stackpack)
* [How to make a multi-instance StackPack](https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/how_to_make_a_multi-instance_stackpack)
