# Source: https://docs.sandboxes.cloud/docs/personalize.md

# Personalize your sandbox

This page describes about how to personalize your development environment in Crafting Sandbox using personal snapshot.

Crafting allows a team to pre-define standard setups for the default dev environments as [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) stored in templates. In addition, it also allows every developer to further personalize their workspaces to have their personal touch on top of the default, team-wide templates.

You can define `Personal Snapshots`, a snapshot containing personalized configurations and is applied to the home directory (`/home/owner`) for *every workspace* in new sandboxes created by you.

### Create a personal snapshot

Similar to `Home Snapshot`, a `Personal Snapshot` can be created via CLI command. To create a personal snapshot, first edit the file `~/.snapshot.personal/includes.txt` and optionally, `~/.snapshot.personal/excludes.txt`. The `includes.txt` should specify the files patterns to be included in the snapshot, and the `excludes.txt` should specify patterns for the files to be excluded. Once the `includes.txt` file is ready, use the command to create the snapshot.

```shell
$ cs snapshot create --personal NAME --set-personal-default
```

### Set default snapshot

As the name suggests, a `Personal Snapshot` is personal to one user (the owner). It's visible and accessible to the owner only. The name shares a different namespace from other snapshots in the org. Hence, it can have the same name as other kinds of snapshots in the same organization.

The sub-command `set-default` can be used to explicitly set a personal snapshot as the `Default Personal Snapshot`, which will be applied automatically to all new workspaces created later. If there are no existing personal snapshots, the first one will become default automatically. If there is more than one personal snapshot, the default one can be selected in web console, under `Resources->Snapshots`

<Image align="center" className="border" border={true} src="https://files.readme.io/fed53e2-image.png" />

We can also select a personal snapshot via CLI command:

```shell
$ cs snapshot personal get-default
$ cs snapshot personal set-default NAME
```

To unset the `Default Personal Snapshot` so that no personal snapshots will be applied to new workspaces:

```shell
$ cs snapshot personal set-default NONE
```

### What to put in personal snapshot and avoid conflicts

Since a `Personal Snapshot` is applied the same way as a [Home Snapshot](https://docs.sandboxes.cloud/docs/workspaces-setup#home-snapshots) that directly extracts the snapshot into the home folder. it's recommended that there's no file overlapping between a personal snapshot and a home snapshot since a home snapshot can be updated later with updated content in an overlapped file which will be reverted once the personal snapshot is applied, and it may contain an old version of the file compared to the latest home snapshot.\
To avoid that, for example, adding personal environment variables, the best way is to add the following in `~/.bashrc`:

```shell
if [[ -f ~/.bashrc.me ]]; then
  . ~/.bashrc.me
fi
```

And add `~/.bashrc` in a shared home snapshot, and `~/.bashrc.me` in personal snapshot. File `~/.snapshot.personal/includes.txt` contains

```text
.bashrc.me
```