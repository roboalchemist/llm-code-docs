
# Code with JetBrains IDEs

Source: https://docs.sandboxes.cloud/docs/code-with-jetbrains-ides.md

In this page, we cover the common topics regarding using JetBrains IDEs, such as `IntelliJ`, `RubyMine`, `PyCharm`, `GoLand`, `WebStorm`, `CLion`, etc. to work on code inside the Crafting Sandbox.

## Directly edit code in sandbox using JetBrains Gateway and Client

JetBrains offers a suite of powerful and feature-rich IDEs for common programming languages. For remote development, it offers `JetBrains Gateway` on the client side to work with IDE backend running on the server. After the `Gateway` sets up IDE backend, it launches an IDE frontend `JetBrains Client` to connect with the backend via SSH.

Crafting Sandbox supports JetBrains Gateway natively with `Crafting Plugin`. It can be installed by simply run `cs jetbrains` command.

```shell
cs jetbrains
Downloading JetBrains Gateway ...
Downloading Crafting plugin
Unpacking Crafting plugin
...

```text

It will download the latest version of JetBrains Gateway, and install the Crafting Plugin into the downloaded version. After that, it will automatically connect to the workspace you selected and launch `JetBrains Client` to edit the code inside the sandbox.

In this way, the IDE backend will run on the workspace on cloud, taking the heavy-lifting work of indexing the code, build, and run tests, etc., and a generic IDE frontend (JetBrains Client) will run on your local machine providing the native editing experience with GUI.

You can select which IDE backend to launch on the workspace to match the corresponding language you want to edit, like the following, by default it would use IntelliJ

```shell
cs jetbrains --ide=IntelliJ
cs jetbrains --ide=PyCharm
cs jetbrains --ide=RubyMine
cs jetbrains --ide=GoLand
cs jetbrains --ide=WebStorm
cs jetbrains --ide=CLion

```text

Note that if the corresponding IDE backend is used first time on the workspace, it needs to be downloaded and installed, which will take a few minutes. We suggest you to pre-install the IDE into corresponding location on the workspace, i.e., under `~/.cache/JetBrains/RemoteDev/`, and include the directory into `Home Snapshot`(see [here](https://docs.sandboxes.cloud/docs/workspaces-setup#home-snapshots))  or `Personal Snapshot` (see [here](https://docs.sandboxes.cloud/docs/personalize)) so that it's loaded into any new sandbox you created.

Alternatively, you can also use a command to launch the `JetBrains Gateway` with GUI on your local machine and use the installed Crafting Plugin.

```shell
cs jetbrains --gateway

```text

This way, you can select which workspace, which IDE you want to use in the GUI. Or in the address bar, simply paste the corresponding WebIDE link and click `Connect`.

<Image align="center" width="80% " src="https://files.readme.io/d626611-image.png" />

It will also save the most recent connected workspaces in the list to help you quickly connect to them.

## Use JetBrains IDE on local codebase in hybrid mode

If you prefer using your desktop version of IDE (e.g. `IntelliJ`) directly instead of using `JetBrains Client`, Crafting supports two ways for `hybrid development` as follows:

* Code locally, build and run remotely with code sync: see [here](https://docs.sandboxes.cloud/docs/code-sync)
* Code and run one service locally, with context services on remote with port forwarding: see [here](https://docs.sandboxes.cloud/docs/port-forwarding)

## Customize JetBrains Remote Server Version

Use the `customizations` section in the Template to specify the desired version of JetBrains remote server, for example:

```yaml
workspaces:
- name: example
  ...
customizations:
- property_set:
    type: crafting.dev/sandbox/jetbrains
    properties:
      workspace: example
      ide_code: IU
      ide_version: 2024.1.1
      ide_folder: ideaIU-2024.1.1

```text

The properties are:

* `workspace`: required, name of the workspace. The version selection will only be applied to the specified workspace;
* `ide_code`: required, match the specified IDE. It uses the JetBrains defined code, some of them are like:
  * `IU`: IntelliJ
  * `PC`: PyCharm
  * `WS`: WebStorm
* `ide_folder`: optional, but recommended, the folder name of the remote server installation.

## Prelaunch JetBrains Remote Server

To reduce the start time of `cs jetbrains`, the remote server matching the specified version can be preinstalled in the base snapshot and prelaunched during workspace startup.

Start from Crafting `1.8.3`, the remote dev server can be launched easily using (inside a Crafting workspace):

```shell
cs jetbrains remote-dev-server run ${PROJECT_DIR}

```text

For older versions, the remote server can be launched (directly using `remote-dev-server.sh` may run into some race-condition that JetBrains didn't resolved well. So using `cs jetbrains remote-dev-server ...` command will apply some workarounds internally to avoid race-conditions):

```shell
BROWSER='/opt/sandboxd/sbin/wsenv open' nohup \
  ~/.cache/JetBrains/RemoteDev/dist/ideaIU-${INTELLIJ_VERSION}/bin/remote-dev-server.sh \
  run ${PROJECT_DIR} \
  --ssh-link-host ${SANDBOX_WORKSPACE}--${SANDBOX_NAME}-${SANDBOX_ORG}${SANDBOX_SYSTEM_DNS_SUFFIX} \
  > ${LOG_FILE} &

```text

Where `ideaIU-${INTELLIJ_VERSION}` matches the `ide_code`, `ide_version` and `ide_folder` in the customizations section.

To auto launch the JetBrains remote server, add that as a daemon to a checkout of the workspace, for example:

```yaml
workspaces:
- name: example
  checkouts:
  - path: src
    repo:
      ...
    manifest:
      overlays:
      - inline: |
          ...
          daemons:
              remote-dev-server:
                 run:
                    cmd: cs jetbrains remote-dev-server run

```text

Note: stopping the daemon may not stop the remote-dev-server in the background if there's any active client session connected. To forcibly stop the remote-dev-server while stopping the daemon, please add flag `--terminate-dev-server` to the command line.

## Warm-up Index

The first launching the remote server on a code repository takes a bit longer indexing the source code. This can be explicitly done during workspace startup to save time when a client connects. Starting from Crafting `1.8.3`, run the following command to warm-up the index explicitly:

```shell
cs jetbrains remote-dev-server warmup ${PROJECT_DIR}

```text

With older version, run the following command (note: it may run into race-conditions as mentioned above about prelaunch):.

```shell
~/.cache/JetBrains/RemoteDev/dist/ideaIU-${INTELLIJ_VERSION}/bin/remote-dev-server.sh warmup ${PROJECT_DIR}

```text

And this command can be added to `post-checkout` hook or run before the remote server starts as a daemon.

## Troubleshootings

#### Unable to launch IDE client (MacOS only)

When this happens, the UI may show the progress of downloading the IDE thin client (or may not if it's already downloaded), and after that, no IDE UI is being launched. From the terminal, some log may show up like:

```text
WARN - #c.i.r.d.CodeWithMeClientDownloader - Running client process failed after specified number of attempts

```text

If info level log was enabled, it will show something like `error=Error Domain=NSOSStatusErrorDomain Code=-10661`

This is caused by the `cs` CLI and/or the JetBrains Gateway for a different CPU architecture was downloaded and the gateway will download the IDE thin client for the wrong CPU architecture.

A clean fix will be:

* Remove the `cs` binary
* Run `rm -fr ~/.crafting/sandbox/cli`
* Run `rm -fr ~/.crafting/sandbox/jetbrains`
* Download and install the `cs` binary for the correct CPU architecture

Then run `cs jetbrains` again and see if the issue is resolved.
