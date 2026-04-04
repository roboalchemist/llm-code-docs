# Source: https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/how_to_pack_and_upload_stackpack.md

# Upload a StackPack file

The `.sts` file is a zip archive that contains the [StackPack file structure](https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/prepare_package). When all files are in place, archive your StackPack directory into a `.zip` file and change its extension to `.sts`.

To upload the `.sts` file to StackState use the [StackState CLI](https://archivedocs.stackstate.com/5.1/setup/cli) with the following command: \`

{% tabs %}
{% tab title="CLI: sts" %}

```
sts stackpack upload --file <PATH_TO_FILE.sts>
```

From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison#which-version-of-the-cli-am-i-running)
{% endtab %}

{% tab title="CLI: stac (deprecated)" %}

```
stac stackpack upload <PATH_TO_FILE.sts>
```

⚠️ **From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://archivedocs.stackstate.com/5.1/setup/cli/cli-sts#install-the-new-sts-cli)
* [Comparison between the CLIs](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison)
  {% endtab %}
  {% endtabs %}
