
# Adjust config of a sandbox

Source: https://docs.sandboxes.cloud/docs/adjust-config.md

This page described how to adjust config of an existing sandbox. No matter your sandbox is from a single repo in a single workspace, or created from a well-defined template. You can adjust its config dynamically.

Crafting allows config changes to be made to a sandbox after it's already created. You can do smaller changes such as adjusting environment variables, port-forwarding, to significant changes such as changing snapshots, adding workspaces, containers, endpoints, or dependencies. After making changes, you can also choose to save the sandbox configuration as a template to make the changes persisted.

For a sandbox created from a template, editing the configuration will disassociate the sandbox from the template. To allow editing, you can click `EDIT` button in the action menu, see below. After confirming, the sandbox will be editable as a [standalone sandbox](https://docs.sandboxes.cloud/docs/standalone-sandbox).

<Image align="center" className="border" border={true} src="https://files.readme.io/6bd624b-image.png" />

For a sandbox not associated withy any template, a.k.a., [standalone sandbox](https://docs.sandboxes.cloud/docs/standalone-sandbox), you can directly edit the config by clicking the `Edit` button on the top-right corner and get into the editing view, as shown below.

<Image align="center" className="border" border={true} src="https://files.readme.io/7206ad9-image.png" />

After getting into the editing view, you can adjust all configurations from the UI by directly clicking each card or edit the whole config as YAML file by clicking `Edit in YAML`.

<Image align="center" className="border" border={true} src="https://files.readme.io/68d255e-image.png" />

After editing, you can click `Apply` to apply the change to the sandbox. You can also test how the new configuration works for a brand new sandbox by `Try with New Sandbox` or save the config as a template by `Save as Template`.

This is a great way to try any new configs safely because your modification in the configuration here will only affect this particular sandbox, and your other sandboxes or your teammate's sandboxes won't be affected.

Details on how to adjust configurations can be found [here](https://docs.sandboxes.cloud/docs/standalone-sandbox).

If you prefer you can also edit a sandbox from command-line using Crafting CLI

```shell
cs sandbox edit

```text
