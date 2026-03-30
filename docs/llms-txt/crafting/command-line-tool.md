
# Command Line Tool

Source: https://docs.sandboxes.cloud/docs/command-line-tool.md

## One CLI

The only CLI `cs` can be used outside the Crafting Sandbox system (e.g. your laptop, local machine) or inside a workspace, where the CLI is already installed.

Type `cs` or `cs help` to view the list of sub-commands and flags. Use `cs COMMAND --help` (or `cs help COMMAND`) to get help of a specific command.

## Output and Interactive Mode

Based on the terminal, the CLI will automatically determine whether to support colored output and enable interactive mode.

The CLI outputs all human-readable sentences on *STDERR* as well as error messages.
It reserves *STDOUT* for structured data output, like JSON or YAML.
So when piping the output, make sure the output is in JSON or YAML (some commands always output JSON or YAML, e.g. `cs template show --def`).
Colored output can be turned off by setting environment variable `CLI_NO_COLOR` to a non-empty value, regardless of the actual value.

When interactive mode is enabled, some command line arguments can be omitted or incomplete.
The CLI will interactively prompt the user to select or enter required information.
And text editor (used by `cs template create`, `cs template edit` etc) will only be launched in interactive mode.

The interactive mode is disabled in any of the following cases:

* The terminal is not a TTY;
* *STDIN* is closed;
* Environment variable `CLI_SCRIPT` is not empty, regardless of the value;
* Command line flag `--output-format` (or `-o`) is specified. Note: this will disable interactive mode and assume the CLI is used by a script for piping input/output.

## Commands

## Login

Create an authenticated session for the CLI and other clients.

```shell
cs login

█████████████████████████████████████████
█████████████████████████████████████████
████ ▄▄▄▄▄ █▀█ █▄▄█▀ ▀▀▄▀▀█▄▀█ ▄▄▄▄▄ ████
████ █   █ █▀▀▀█ ▀▀ ▀███▄▄████ █   █ ████
████ █▄▄▄█ █▀ █▀▀█▄▀▄█ ▄▀█▀▄██ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄▀ ▀▄█▄█▄█▄▀▄▀ █▄█▄▄▄▄▄▄▄████
████     █▄▄▄▄▀▄▀▄▄▄ ▄▀▀▀█▄▀█▄▀▄█▄▀ ▀████
█████▄▀█  ▄███▄█▀█   ▄▄█  ▄█▀ █ ▀▄▀▄█████
█████▄▄▀▄█▄ ▀ ▄█▄▄ █▀▄▄ ▄█▄▀▄ ▀█▄▄█▀▀████
████▄  ▀ █▄ ▀   ▄█   ▄██ ▀ ▀█▀▀█ █▀▄█████
████▄ ▄ ▄█▄ █▄▄▄▀ ▄▄ ▄▄▀▀▀▄  █▀▄▄▀█ ▀████
████▄▄█ ▀ ▄ ▀███▀█ ▄▄▄▀█▀▀ █▄▄  ▄▄▀▄█████
████▀▄██ ▀▄█ █▄█▄▄▄▄▄▄█▀ █▄▀▄▄▀▄▄▀█ ▀████
████ ██▄▄▄▄ ▄▀█ ▄▄  ▀▄▀█▄ ▀██▀▀▄█ ▀▄█████
████▄█▄██▄▄▄ █▄▄▀▀█▄▄▄█▀▀█▄▀ ▄▄▄ ▄▀█ ████
████ ▄▄▄▄▄ █▄▄ █▀ ▄ ▄███▀▀▄  █▄█  ▀ █████
████ █   █ █ ▄▄█▄█▄▄  ▀▀ █▀▀▄ ▄  █▀██████
████ █▄▄▄█ █ ▄▄ ▄█▀ ▀█ ▀▄▀ ▄█▀ ▀▀  ▄█████
████▄▄▄▄▄▄▄█▄▄█▄███▄▄▄██▄█▄▄▄███▄██▄█████
█████████████████████████████████████████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Login with: https://sandboxes.cloud/auth/login?state=c%3Ac76vuhtq43umrqhpeumg

```text

It will print the login URL (and a QRCode if you want to scan and login from a phone). Visit the URL in browser to complete login process.

##### Flags

* `-t`: followed by a login token to login with it. See [Service Account and Login Token](#service-account-and-login-token) for more details. Remember that if you are using self-hosted Crafting, please specify first `CRAFTING_SANDBOX_SERVER_URL=https://your.site.address`

## Info

Display detailed information about the current client.

```shell
cs info

USER Demo Me
  Email: demo.me@crafting.dev
  AUTHORIZED SSH KEYS
    FINGERPINT                                         COMMENT      CURRENT
    SHA256:M0JDLwPWPnuIixDDIRbxDCwoTgRmbj1YAZqbFZQLqyI dev          *      
SECRET default-ssh-0
Version: 16aa9d024b577309
OwnedBy: demo.me@crafting.dev
UpdatedAt: 03 Nov 12:47:19
CreatedAt: 03 Nov 12:47:19
CreatedBy: demo.me@crafting.dev
Type: SSHKey
State: READY
SSH Authorized Key
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDOLsrOAKpIIP/yDQhks70RbPmmsdPFz/czxD99vnHLuybY4koRecq3N9mpC9zj67kla0bX0yjqJSaUAkeb+sPzC+2VNdvpjnUhOqEmSDwflyVDz+3Q6h+5M4gSIbr6L79KK/UrG728lp8EZwWQW1RPNvzjAs26y+yZ7oOT420FISSNT2KBvQYJSVI5X1tQOexHtfwtdcmzpCgr96lq0H0T7dQ6ZjuTggw9ScEDPtR+XYr/16KoD5Bf8TVcqbRi1ACxob2yCm8raxtJl7b/VEY2HNl1AOT42zzacVkP/IrsTYoeMjlteipQ/LAq3i5SX8vGCK4bU83GIoE1jjoMkOKA+UlfI4dUeUhQisTvRFM3rvFGDCmGECbrf/w1auD+fmRcYbZMj/+BicvAS1SkeHFgJz4yDoIYJPx48jT5pmGMVlMSolg78FP07pwg36k3yzIW5k4NFRCztsY9gbHWqFoOGaM5f1lJbjp09ul0GvYtk60WqyvwLcaNQT80RI/QVtM=

Fingerprint: SHA256:DSF5PZ+LDK7G4M3gFlp1RpTPDs02GNoPmJmZc8aqoc4

```text

The `AUTHORIZED SSH KEYS` lists SSH authorized keys that can be used to access a workspace. The marker `*` indicate the authorized key used by the current client.

The section `SECRET default-ssh-0` provides the public key information of the generated and managed SSH keypair by the Crafting Sandbox system for the current user. This will be used to checkout (and push) code if SSH protocol is specified for a git repository (like `git@...`). If that's the case, this public key must be added to the git source control system (for GitHub, follow the [doc](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)).

## Org

List and show the organization information.

```shell
cs org list
cs org show

```text

## Template

List, show and manipulate Templates.

#### Create

Create a new Template from [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition).

```shell
cs template create NAME DEFINITION-FILE.(json|yaml)|-

```text

The [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) is read from a JSON or YAML file or from *STDIN* (when `-` is specified for `DEFINITION-FILE`).
If read from *STDIN*, the format must be explicitly specified using `--format` (or `-f`).
If no arguments are specified, and [interactive mode](#output-and-interactive-mode) is enabled, the CLI will ask for the name
and launch an editor (from env `EDITOR` or `editor` command) to edit the definition.

##### Flags

* `--format`, `-f`: The format of `DEFINITION-FILE`: `json` or `yaml`. Default is to guess from file extension if `DEFINITION-FILE` is a file.

##### Examples

```shell
cs template create dev1 def1.yaml
cs template create dev1 - --format=yaml <def1.yaml
cat def1.json | cs template create dev1 - -f json
cs template create # This will ask for name and launch an editor.

```text

#### List

List Templates.

```text
cs template list

NAME VERSION          UPDATED_AT      CREATED_AT      CREATED_BY            #W #EP
demo 16be90c0ca3b18b1 07 Dec 19:47:52 07 Dec 18:56:40 demo.me@crafting.dev  5  2

```text

The list shows Template's `NAME`, `VERSION`, `UPDATED_AT`, `CREATED_AT`, `CREATED_BY` and number of workloads (including workspaces and dependencies) and number of endpoints. The time shown in the list is local time, in the shortest form (date will be suppressed if on the same day). The `VERSION` will change when the Template is updated.

##### Flags

* `--columns`, `-c`: Select columns: `+COLUMN` makes `COLUMN` visible, and `-COLUMN` hides `COLUMN`. Example: `-c +UPDATED_AT,-CREATED_AT`.

#### Show

Show the details of the Template.

```shell
cs template show NAME

```text

If name is not specified, and [interactive mode](#output-and-interactive-mode) is enabled, it will prompt for selection an Template.

##### Flags

* `--def`, `-d`: Print [Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) (default in YAML, can be overridden by `--format` (or `-f`)) instead of the details of the Template. The output can be used for `cs template create` or `cs template update`.

#### Update

Update the [Definition](https://docs.sandboxes.cloud/docs/sandbox-definition).

```shell
cs template update NAME DEFINITION-FILE.(json|yaml)|-

```text

The [Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) is read from a JSON or YAML file or from *STDIN* (when `-` is specified for `DEFINITION-FILE`).
If read from *STDIN*, the format must be explicitly specified using `--format` (or `-f`).
If no arguments are specified, and [interactive mode](#output-and-interactive-mode) is enabled, the CLI will ask for the name
and launch an editor (from env `EDITOR` or `editor` command) to edit the definition.

##### Flags

* `--format`, `-f`: The format of `DEFINITION-FILE`: `json` or `yaml`. Default is to guess from file extension if `DEFINITION-FILE` is a file.

#### Remove

Remove a Template.

```shell
cs template remove NAME

```text

The sandboxes created using this App will not be affected, however they can no longer be updated.

##### Flags

* `--force`, `-f`: Force remove without confirmation.

## Sandbox

List, show and manipulate sandboxes.

#### Create

Create a new sandbox.

```shell
cs sandbox create NAME

```text

Use the flags to specify the details.

##### <a name="sandbox-create-flags" />Flags

* `--template`, `-t`: The name of Template used for creating the sandbox;
* `--auto`, `-A`: The name of a workspace to run in *AUTO* mode. Use `*` to put all workspaces in *AUTO* mode;
* `--override`, `-D`: Specify override rules: `WORKLOAD/rule=value`, see [rules](#sandbox-override-rules);
* `--auth-proxy`, `-p`: Specify [auth proxy](https://docs.sandboxes.cloud/docs/sandbox-definition#http-endpoint) config: `ENDPOINT_NAME=[Y|N][[:A|R PATTERN]...]`:
  * `Y|N` specified whether auth proxy is enabled or disabled;
  * Each rule starts with `:` and `A|R` specifies `ACCEPT` or `REJECT`, and `PATTERN` matches email.
* `--if-exists=skip`: Do nothing if a sandbox with the same name already exists and exit without failure.
* `--wait`: Wait for the sandbox becoming ready. This is default, specify `--wait=false` to not wait.
* `--wait-timeout=DUR`: Wait for the sandbox until it's ready or reached `DUR` and ignore errors.

##### <a name="sandbox-create-examples" />Examples

```shell
# Create a sandbox using demo Template
cs sandbox create demo1 -t demo

# Create a sandbox for preview purpose, leave all workspaces in AUTO mode
cs sandbox create demo1 -t demo -A '*'

# Create a sandbox for checkout an alternative branch and change the home snapshot
cs sandbox create demo1 -t demo \
    -D 'dev/checkout[src/demo].version=preview1' \
    -D 'dev/home=home/preview'

# Create a sandbox using a old version of package
cs sandbox create demo1 -t demo -D 'dev/package[golang]=1.16.2'

# Create a sandbox with a different mysql database name
cs sandbox create demo1 -t demo -D 'mysql/property.database=previewdb'

# Create a sandbox with mysql pre-populated from a snapshot
cs sandbox create demo1 -t demo -D 'mysql/snapshot=mysql/preview/20211105'

# Create a sandbox with auth proxy OFF
cs sandbox create demo1 -t demo --auth-proxy 'app=N'

# Create a sandbox allowing external visitors to access the endpoint
cs sandbox create demo1 -t demo --auth-proxy 'app=Y:A v*@guests.com'

```text

#### Update

Update a sandbox.

```shell
cs sandbox update NAME

```text

Without additional flags, the sandbox is synchronized with the changes of the current Template. It does nothing if Template hasn't been changed since the creation (or last update) of the sandbox.
With flags, the update may alter certain overrides. See below.

##### Flags

* `--override`, `-D`: Specify override: `WORKLOAD/rule=value`, see [rules](#sandbox-override-rules);
* `--mode`, `-m`: Change workspace mode: `WORKSPACE-NAME=AUTO|MANUAL` (or `a|m`);
* `--auth-proxy`, `-p`: Specify [auth proxy](https://docs.sandboxes.cloud/docs/sandbox-definition#http-endpoint) config, see [sandbox creation flags](#sandbox-create-flags);
* `--set-all`, `-A`: Ignore existing overrides, and create overrides and workspace modes completely from the command line;
* `--no-sync`: when only `--mode` (or `-m`) is specified, do not synchronize the changes from the App, only change the modes.
* `--wait`: Wait for the sandbox becoming ready. This is default, specify `--wait=false` to not wait.
* `--wait-timeout=DUR`: Wait for the sandbox until it's ready or reached `DUR` and ignore errors.

##### Examples

```shell
# Sync the sandbox with it's Template
cs sandbox update demo1

# Only change workspace mode to MANUAL
cs sandbox update demo1 -m dev=MANUAL --no-sync

# Disable auth proxy
cs sandbox update demo1 --auth-proxy app=N

```text

#### List

List sandboxes.

```text
cs sandbox list

NAME  STATE TEMPLATE OWNER                 UPDATED_AT      CREATED_AT      CREATED_BY           #W #EP
demo1 Ready demo     demo.me@crafting.dev  01 Dec 04:35:36 01 Dec 04:35:36 demo.me@crafting.dev 5  2

```text

The `STATE` of a sandbox may show up with the following values:

* `SettingUp`: some of the workspaces and dependencies are still being configured, setting up (including code checkout and build);
* `Ready`: all workspaces and dependencies are working (code checked out, and built, processes launched);
* `Problematic`: at least one of the workspaces or dependencies encountered some errors which can be:
  * Failures during setup, including code checkout, and build;
  * Some processes are not running;
  * Readiness probes yield negative results.
* `Failed`: this indicates serious problem that the sandbox can't be up. Contact support if you see this;
* `Suspended`: the sandbox was suspended (either manually or automatically), use `cs sandbox resume` to resume it.

##### Flags

* `--columns`, `-c`: Select columns: `+COLUMN` makes `COLUMN` visible, and `-COLUMN` hides `COLUMN`. Example: `-c +UPDATED_AT,-CREATED_AT`.
* `--watch`: Incrementally watch the sandbox updates and refresh the list. It can be used with `-o` to incrementally print changed sandboxes on `STDOUT`.  Sandboxes no long shown on the list (e.g. deleted) are printed in the schema like `{ "absent": ["id1", "id2", ...] }`.

#### Show

Show the details of a sandbox.

```shell
cs sandbox show NAME

```text

#### Suspend

Suspend a sandbox manually.

```shell
cs sandbox suspend NAME

```text

Suspend will immediately change the sandbox `STATE` to be `Suspended`. However it may take a while for the workspaces and dependencies to freeze.

#### Resume

Resume a suspended sandbox.

```shell
cs sandbox resume NAME

```text

Some commands will automatically resume a sandbox if it's suspended. Use this command to manually resume a sandbox.

##### Flags

* `--wait`: Wait for the sandbox becoming ready. This is default, specify `--wait=false` to not wait.
* `--wait-timeout=DUR`: Wait for the sandbox until it's ready or reached `DUR` and ignore errors.

#### Edit

Edit the [Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) of the sandbox. If the sandbox is created from a Template, it is detached from the template. That means the sandbox owns its definition and will no longer be able to sync changes from that Template. Also the sandbox will not be able to attach to any Template.

```shell
cs sandbox edit NAME

```text

##### Flags

* `--from`: read the new definition from the specified file (`-` for reading from STDIN), rather than launching an interactive editor;
* `--keep`: if the sandbox was created with additional configurations (workspace AUTO mode, extra environment variables), keep those when applying the new definition. By default they will be discarded;
* `--wait`: Wait for the sandbox becoming ready after applying the new definition;
* `--wait-timeout=DUR`: Wait for the sandbox until it's ready or reached `DUR` and ignore errors.
* `--force`: always continue without confirmation.

#### Remove

Delete a sandbox.

```shell
cs sandbox remove NAME

```text

**WARNING**: Sandbox removal is permanent. All data in workspaces and dependencies will be lost and is **UNRECOVERABLE**.

##### Flags

* `--force`, `-f`: Force remove without confirmation.

#### Sandbox Override Rules

These are the rules used by `cs sandbox create` or `cs sandbox update` to override the settings in the [Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) used by the sandbox. The format is `WORKLOAD-NAME/rule=VALUE`.
The rules are:

* For workspaces:
  * `checkout[PATH].PROPERTY=VALUE` (alias `co`): override a [checkout](https://docs.sandboxes.cloud/docs/sandbox-definition#checkouts) property:
    * `repo`: `VALUE` is a string, in the format of `SCHEME:URI`, where `SCHEME` can be `git` or `github`. A list of examples:
      * `git:git@github.com:org/repo`
      * `git:<https://github.com/org/repo`>
      * `github:org/repo`
    * `version_spec` (alias `version`): the value can be one of
      * a branch name
      * a tag name
      * a commit hash
  * `package[NAME]=VERSION` (alias `pkg`): override the version of a [package](https://docs.sandboxes.cloud/docs/sandbox-definition#packages) to be used;
  * `portforward[LOCAL]=HOST:PORT` (alias `pf`): override the [local port forwarding](https://docs.sandboxes.cloud/docs/sandbox-definition#local-port-forwarding) rule;
  * `base=SNAPSHOT_NAME`: override the [base snapshot](https://docs.sandboxes.cloud/docs/sandbox-definition#snapshots);
  * `home=SNAPSHOT_NAME`: override the [home snapshot](https://docs.sandboxes.cloud/docs/sandbox-definition#snapshots);
  * `env[KEY]=VAL`: inject/override the environment variable.
* For dependencies:
  * `version=VERSION`: override the [dependency service version](https://docs.sandboxes.cloud/docs/sandbox-definition#dependencies);
  * `snapshot=SNAPSHOT_NAME`: override the [dependency service snapshot](https://docs.sandboxes.cloud/docs/sandbox-definition#dependencies);
  * `property.NAME=VALUE` (alias `prop` or `p`): override the named [dependency service property](https://docs.sandboxes.cloud/docs/sandbox-definition#dependencies);
* For containers:
  * `snapshot=SNAPSHOT_NAME`: override the [container snapshot](https://docs.sandboxes.cloud/docs/sandbox-definition#container-snapshot);
  * `env[KEY]=VAL`: inject/override the environment variable.

See [examples](#sandbox-create-examples) above.

#### Pin/Unpin

Pin a sandbox to be always running (without being automatically suspended). This is useful when a sandbox is used for demo purpose (mostly with AUTO mode on).

```shell
cs sandbox pin NAME   # Keep sandbox running
cs sandbox unpin NAME # Sandbox can be auto-suspended

```text

#### Access Control

Specify/View the access level of a sandbox.

```shell
cs sandbox access private # Set to private mode
cs sandbox access shared  # Set to shared mode (the default)
cs sandbox access show    # Show the current setting.

```text

Please read [Sandbox Access Control](https://docs.sandboxes.cloud/docs/sandbox-access-control) for more details.

#### Workspace Restricted Mode

Request the workspace to exit the [restricted mode](https://docs.sandboxes.cloud/docs/cloud-resources-setup#restrict-access-to-workspaces-and-secrets) .

```shell
cs sandbox restriction disable WORKSPACE-NAME

```text

#### Lifecycle Related

Resolve lifecycle hook failures.

```shell
cs sandbox lifecycle resolve -S SANDBOX -a ACTION [TARGET[:ACTION]]...

```text

Resolve all or specified lifecycle hook failures using the specified `ACTION`. If no `TARGET` is specified, all failures are resolved. If any `TARGET` is specified, only failures on those targets (workspace name, or resource name) are resolved. A `TARGET` can be suffixed with `:ACTION` to resolve using this specific action.

An `ACTION` can be one of:

* `retry`: run the lifecycle hook again, this is the default;
* `skip`: ignore the failure, assume the hook has completed successfully and move the lifecycle transition to the next state;
* `abort`: only used for a running lifecycle hook (effectively not a resolution), to abort the execution, and mark the hook as failed due to abort.

## Snapshot

Snapshot related commands.

#### Create

Create a snapshot.

```shell
cs snapshot create NAME

```text

This command is able to create a workspace base snapshot, home snapshot or dependency service snapshot. See flags below to determine which kind of snapshot is being created.
When using this command, the target must be a workspace, or a dependency which supports snapshots.

**NOTE**: during dependency snapshot creation, the dependency service will be stopped temporarily. And it will be resumed after snapshot is created. For base/home snapshots, the workspace is still accessible, however please try to avoid writing files to the file system during that procedure. Otherwise, some incomplete files may be included in the snapshot.

All snapshots share the same namespace regardless of the type, so it's recommended defining a naming convention to avoid conflicts. One proposal is using a format like `TYPE-NAME-REV`, where `TYPE` is the snapshot type, e.g. `base`, `home`, `mysql` etc. and `NAME` indicates the purpose of the snapshot, while `REV` reflects the revision which can be a date like `YYYYMMDD` or a monotonic version number. For example (not necessary to follow):

* Base snapshots are named as `base-NAME-REV`, like `base-backend-r1`;
* Home snapshots are named as `home-NAME-REV`, like `home-frontend-20221010`;
* Dependency snapshots are named as `SERVICE-TYPE-NAME-REV`, like `mysql-test-2`.

Additional prefixes can be added to further separate among sub-teams or persons:

* Base snapshots used by a team: `team1-base-frontend-3`
* Personal home snapshot: `alan-home-frontend-1`

##### Flags

* `--workload`, `-W`: Specify the workload name in the format of `SANDBOX/WORKLOAD`. If the target is a dependency, a dependency snapshot is created. Otherwise, based on `--home` flag to determine if it's a home snapshot or base snapshot;
* `--home`: Create a home snapshot. The target must be a workspace;
* `--personal`: Create a [Personal Snapshot](https://docs.sandboxes.cloud/docs/personalize#create-a-personal-snapshot);
* `--set-personal-default`: Only valid with `--personal` to set the current snapshot as the *Default Personal Snapshot*;
* `--force`, `-f`: Overwrite an existing snapshot (if `NAME` already exists) without confirmation.

#### List

List snapshots.

```shell
cs snapshot list

```text

##### Flags

* `--columns`, `-c`: Select columns: `+COLUMN` makes `COLUMN` visible, and `-COLUMN` hides `COLUMN`. Example: `-c +UPDATED_AT,-CREATED_AT`.

#### Show

Show the details of a snapshot.

```shell
cs snapshot show NAME

```text

#### Restore

Restore a dependency snapshot.

```shell
cs snapshot restore NAME

```text

Only a dependency supporting snapshots can be restored from a snapshot. Base and home snapshots for workspaces are only applied during the workspace creation time, and can't be changed later.
**NOTE**: during snapshot restoring, the dependency service will be stopped temporarily. And it will be resumed after snapshot is restored.

##### Flags

* `--workload`, `-W`: Specify the workload name in the format of `SANDBOX/WORKLOAD`. The target must be a dependency which supports snapshots.

#### Remove

Remove a snapshot.

```shell
cs snapshot remove NAME

```text

**WARNING**: Snapshot removal is permanent. The data in the snapshot is **UNRECOVERABLE**.
The workspaces and dependencies with snapshot already applied won't be affected. However new sandboxes may fail to be created if the App/Sandbox is referencing a *deleted* snapshot.

##### Flags

* `--force`, `-f`: Force remove without confirmation.

#### Personal

Personal snapshot related.

```shell
cs snapshot personal get-default      # Get the current default personal snapshot
cs snapshot personal set-default NAME # Set the specified personal snapshot as default.
cs snapshot personal set-default NONE # Do not use a personal snapshot.

```text

## Secret

Secret related commands.

A *Secret* operated by this command is a small piece (a few KB) of opaque data provided by the user. It's not necessary to be sensitive information. And the data is encrypted at storage.
A *Secret* has a scope. It's one of:

* Personal: belonging to a user, regardless of the orgs;
* Private in org: belonging to a member in org. The user can only access own secrets in the context of that org and the secrets can't be accessed by others;
* Shared in org: belonging to an org (not a user), and all members in the org has the access to that secret.

#### Create

Create a secret.

```shell
cs secret create NAME

```text

A secret is created with *private in org* scope by default unless `--shared` flags is specified. *Personal* secrets can't be created from the CLI.

##### Flags

* `--shared`: Create a shared secret in the current org;
* `--from`, `-f`: Read content from a `FILE` or `-` (*STDIN*). This flag is required;
* `--restricted`: Set the access restriction to *Admin Only* so this secret can only be mounted in workspaces which are running in [Restricted mode](https://docs.sandboxes.cloud/docs/cloud-resources-setup#restrict-access-to-workspaces-and-secrets) .

#### List

List secrets.

```shell
cs secret list

```text

This command lists all the secrets the user has access to, including:

* Personal secrets;
* Private secrets in the current org;
* Shared secrets in the current org.

##### Flags

* `--user`, `-u`: List personal secrets rather than org scoped secrets;
* `--columns`, `-c`: Select columns: `+COLUMN` makes `COLUMN` visible, and `-COLUMN` hides `COLUMN`. Example: `-c +UPDATED_AT,-CREATED_AT`.

#### Show

Show the details of a secret, without revealing the content.

```shell
cs secret show NAME

```text

#### Remove

Remove a secret.

```shell
cs secret remove NAME

```text

Only a secret in the current org is to be removed by default, unless `--user` flag is specified.
Some secrets (e.g. generated and managed by the system) can't be removed.

##### Flags

* `--user`, `-u`: Remove a personal secret rather than the one in the current org;
* `--force`, `-f`: Force remove without confirmation.

#### Access Restriction

Update the access restriction.

```shell
cs secret restrict NAME -a MODE

```text

Where `MODE` can be one of the values:

* `default`: regular secret, shared in org and any member is able to access;
* `admin-only`: the access is restricted to admin only, so the secret is only mounted in workspaces which are running in [Restricted mode](https://docs.sandboxes.cloud/docs/cloud-resources-setup#restrict-access-to-workspaces-and-secrets) .

## Dependency Service

Retrieve information about dependency services.

```shell
cs dependency-service list
cs dependency-service show NAME

```text

When creating a [Definition](https://docs.sandboxes.cloud/docs/sandbox-definition), it's important to inspect the details of a dependency service using `cs dependency-service show` to figure out:

* Exposed ports of the service (name, port number and protocol);
* Properties
* Available versions

## Tool Packages

List available tool packages.

```shell
cs package list

```text

## Mode

This is a shortcut for setting workspace mode: `AUTO` or `MANUAL`.

```shell
cs mode auto
cs mode manual

```text

##### Flags

* `--workspace`, `-W`: Specify the workspace in the format of `SANDBOX/WORKSPACE`. If unspecified, it will target the current workspace (if the CLI runs inside a workspace), or prompt for a selection.

## SSH

Start an SSH session to a workspace.

```shell
cs ssh

```text

When passing flags to `ssh`, put them after `--`. For example:

```shell
cs ssh -- /myscript --script-flag
cs ssh -- -t -L 8080:localhost:8080 /myapp

```text

##### Flags

* `--workspace`, `-W`: Specify the workspace in the format of `SANDBOX/WORKSPACE`. If unspecified, it will prompt for a selection.

## SCP

Run `scp` to copy files to/from a workspace.

```shell
cs scp LOCAL-PATH SANDBOX/WORKSPACE:REMOTE-PATH
cs scp SANDBOX/WORKSPACE:REMOTE-PATH LOCAL-PATH

```text

Similar to `ssh` command, flags passing to `scp` should be placed after `--`, for example:

```shell
cs scp -- -r LOCAL-PATH SANDBOX/WORKSPACE:REMOTE-PATH

```text

## RSYNC

Run `rsync` between a local folder and a folder in a workspace.

```shell
cs rsync LOCAL-PATH SANDBOX/WORKSPACE:REMOTE-PATH
cs rsync SANDBOX/WORKSPACE:REMOTE-PATH LOCAL-PATH

```text

Flags passed to `rsync` should be placed after `--`.

## SSHFS

Mount a path in a workspace to a local directory using `sshfs` which must be installed on the system the CLI runs.

```shell
cs sshfs SANDBOX/WORKSPACE:REMOTE-PATH LOCAL-PATH

```text

## Mutagen

Run `mutagen` for a two-way sync session between a local directory and one in a workspace. [Mutagen](https://github.com/mutagen-io/mutagen) must be installed on the system the CLI runs.

```shell
cs mutagen LOCAL-PATH SANDBOX/WORKSPACE:REMOTE-PATH

```text

This command will run in the foreground until the sync session is over. Stop the command (using Ctrl-C) will also stop the sync session.

## IDE

Launch WebIDE in browser.

```shell
cs ide [PATH|.|~]

```text

Launch WebIDE in browser and opens a [checkout](https://docs.sandboxes.cloud/docs/sandbox-definition#checkouts) or home directory if `.` or `~` is specified as the argument.

##### Flags

* `--workspace`, `-W`: Specify the workspace in the format of `SANDBOX/WORKSPACE`. If unspecified, it will prompt for a selection.

## VSCode

Launch a local-installed VSCode to connect to a workspace using SSH remote development extension.

```shell
cs vscode [PATH|.|~]

```text

Launch a local-installed VSCode and opens a [checkout](https://docs.sandboxes.cloud/docs/sandbox-definition#checkouts) or home directory if `.` or `~` is specified as the argument.

##### Flags

* `--workspace`, `-W`: Specify the workspace in the format of `SANDBOX/WORKSPACE`. If unspecified, it will prompt for a selection.

## JetBrains IDE

Currently remote development is supported using JetBrains Gateway:

```shell
cs jetbrains

```text

This command will automatically download JetBrains Gateway, install Crafting plugin and launch the IDE connected to a remote workspace.

##### Flags

* `--ide=TYPE`: Select an IDE type. Default is `IntelliJ`, other options are `GoLand`, `RubyMine`, `PyCharm`, `CLion` and `WebStorm`;
* `--gateway`: Launch JetBrains Gateway UI, do not connect automatically.

## Daemon Management

Manage [daemons](https://docs.sandboxes.cloud/docs/repo-manifest#daemons) inside a workspace. A daemon process must be defined in [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest).

```shell
cs ps
cs up [DAEMON-NAME...]
cs down [DAEMON-NAME...]
cs restart [DAEMON-NAME...]

```text

When running inside a workspace, without additional flags (`--workspace` or `-W`), the CLI targets the current workspace.

##### Flags

* `--workspace`, `-W`: Specify the workspace in the format of `SANDBOX/WORKSPACE`. If unspecified, it will prompt for a selection.

## Job Management

Manage [jobs](https://docs.sandboxes.cloud/docs/repo-manifest#jobs) inside a workspace.

```shell
cs job enable [JOB-NAME...]
cs job disable [JOB-NAME...]

```text

When running inside a workspace, without additional flags (`--workspace` or `-W`), the CLI targets the current workspace.

##### Flags

* `--workspace`, `-W`: Specify the workspace in the format of `SANDBOX/WORKSPACE`. If unspecified, it will prompt for a selection.

## Log

View tail logs of daemons, setup actions etc.

```shell
cs log NAME

```text

The CLI will try to match the best target based on `NAME` for fetching logs. It may prompt for a selection if multiple matches are available. With flags, the scopes can be further narrowed.

##### Flags

* `--workspace`, `-W`: Specify the workspace in the format of `SANDBOX/WORKSPACE`. If unspecified, it will target the current workspace if running inside it, or prompt for a selection;
* `--action`, `-a`: Match `NAME` against the action names in a task (specified by `--task`);
* `--task`, `-t`: Specify task name, only used when `--action` is in use;
* `--kind`, `-k`: Match specific process type (exclusive from `--action`), one of:
  * `daemon` or `d`: for daemons;
  * `job` or `j`: for jobs.
* `--path`, `-p`: Specify the [checkout](doc:sandbox-definition:#checkouts) path for matching the process;
* `--lines`, `-n`: Number of lines to print from the tail log, default is the same as `tail` command;
* `--follow`, `-f`: Watch and follow new logs.

##### Examples

```shell
# Show the only daemon log or select one
cs log
# Show Build log during setup
cs log -a build
# Follow daemon log
cs log -f server
# Tail more lines and follow
cs log -n 1000 -f server

```text

## Port Forward

Bi-directional port-forwarding between local and a workspace.

```shell
cs port-forward

```text

By default, this command will establish port forwarding between local machine (where the CLI runs) and a workspace (usually specified by `--workspace` flag):

* All ports defined in the workspace are forwarded from workspace to local machine (`localhost`) with the same destination port numbers;
* All rules defined in [port\_forward\_rules](https://docs.sandboxes.cloud/docs/sandbox-definition#local-port-forwarding) are forwarded from local machine to the workspace. The CLI tries to listen on the *local* ports as specified by `port_forward_rules`, however it may fail if the port is already in-use, and the CLI will skip that rule and keep others running.

The default behavior can be overridden by flags.

##### Flags

* `--workspace`, `-W`: Specify the workspace in the format of `SANDBOX/WORKSPACE`. If unspecified, it will prompt for a selection;
* `--skip-exposed-ports`, `-P`: Skip all *exposed* ports on the workspace;
* `--skip-forward-rules`, `-F`: Skip all rules in `port_forward_rules`;
* `--reverse`, `-R`: Specify an explicit incoming forwarding rule, in the format of `REMOTE-PORT:LOCAL-HOST:LOCAL-PORT`, where
  * `REMOTE-PORT`: a port number on the workspace and it is not necessary one of the exposed ports;
  * `LOCAL-HOST`: a hostname that the traffic will be forward to, it can be `localhost` or any hostname that's reachable from the local machine;
  * `LOCAL-PORT`: a port on the host specified by `LOCAL-HOST` that a connection will be forwarded to.
* `--local`, `-L`: Specify an explicit outgoing forwarding rule, in one of the formats:
  * `LOCAL-PORT:REMOTE-PORT`: forward `localhost:LOCAL-PORT` to `REMOTE-PORT` (a port number) on the workspace;
  * `LOCAL-PORT:HOST:PORT`: forward `localhost:LOCAL-PORT` to remote, based on `HOST`:
    * `HOST` is `localhost`: `PORT` can be either a number or name of an exposed port, and the forward target is the workspace;
    * `HOST` is not `localhost`: then it's must be a workload name, and `PORT` must match an exposed port of that workload, either by port number or name. The forward target is the specified workload and port.
  * `LOCAL-ADDR:LOCAL-PORT:HOST:PORT`: same as above rule, however the local listening address is `LOCAL-ADDR:LOCAL-PORT` instead of `localhost:LOCAL-PORT`;

##### Examples

```shell
# Incoming forward only
cs port-forward -F
# Outgoing forward only
cs port-forward -P
# Add an incoming forwarding rule
cs port-forward -R 8080:localhost:8080
# Specify all rules explicitly (disable defaults)
cs port-forward -FP \      # disable the defaults
    -R 8080:localhost:8080 \ # incoming workspace port 8080 to localhost:8080
    -L 9000:9000 \           # outgoing from localhost:9000 to workspace 9000
    -L 5000:backend:api \    # outgoing from localhost:5000 to workload "backend" port "api"
    -L 5001:localhost:5001 \ # outgoing from localhost:5001 to workspace localhost:5001
    -L :5002:localhost:5001  # outgoing from *:5002 to workspace localhost:5001

```text

## Exec

Run a command inside a [container workload](https://docs.sandboxes.cloud/docs/containers).

```shell
cs exec -- command...
cs exec -W SANDBOX/WORKLOAD -- command...
cs exec --tty -- command ... # Force using TTY
cs exec -T -- command...     # Force disabling TTY

```text

##### Flags

* `--tty`, `-t`: Force using TTY;
* `--disable-tty`, `-T`: Disable TTY;
* `--uid`, `-U`: Run as the specified UID.

## Wait

Wait for a sandbox to become ready or a workload to become ready.

```shell
cs wait sandbox NAME     # Wait until the sandbox state becomes Ready or Problematic/Failed
cs wait service WORKLOAD # Wait for the readiness of a workload

```text

The command `cs wait service` is useful to synchronize the initialization between multiple workloads. For example, a workspace needs to seed some data into a database during the build process (e.g. automatically triggered, during setup), and it's possible the dependency (e.g. mysql) is still being started and not ready yet. In this case, the build hook script of the workspace can include `cs wait service` command, like:

```shell
#!/bin/bash

do_build
cs wait service mysql
do_seed_data

```text

##### Flags

* `--timeout`: Maximum duration to wait. If unspecified (or zero value), it will wait indefinitely. The value is suffixed by a unit of `h` (hour), `m` (minute), `s` (second) or `ms` (millisecond). For example: `1h`, `5m`, `300ms`, or `6m30s`, etc;
* `--sandbox`, `-S`: Only applies to `cs wait service` command. When used, the CLI may run outside of a workspace, or wait for a workload in a different sandbox. The value is the sandbox name.

## Docker

Run the `docker` command with credential-helper hooked. This is used when pushing an image to the org-scoped private container registry.

```shell
cs docker -- push cr.sandboxes.cloud/myorg/path/myimage:tag

```text

## Inside Workspace Only

The following command are available when the CLI is running inside a workspace.

#### Run Hook

Run a hook script defined in [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest).

```shell
cs run-hook NAME

```text

The `NAME` can be `post-checkout` or `build`. The hook script is directly run in foreground by the CLI, not by the workspace agent. This is for debugging purpose as there may be slightly difference between the CLI environment and the workspace agent.

#### Build

This is a shortcut for `cs run-hook build`.

```shell
cs build

```text

#### Banner Control

By default, a welcome banner is displayed when an interactive shell is opened (via SSH or VSCode terminal).
This can be suppressed by `mute/unmute` command.

```shell
cs banner mute   # Do not display the banner
cs banner unmute # Display the banner

```text

## Endpoint Alias

#### Create

```shell
cs endpoint-alias create ENDPOINT-ALIAS-NAME [SANDBOX-NAME ENDPOINT-NAME]

```text

It creates an *Endpoint Alias* with name specified by `ENDPOINT-ALIAS-NAME`. The final DNS is derived from that name and the org name. For example, `cs endpoint-alias create foo` in org `bar` will generate the DNS `foo-bar.sandboxes.run`.

When `SANDBOX-NAME` and `ENDPOINT-NAME` is specified, the newly created *Endpoint Alias* is assigned to that endpoint, or it's *Unassigned*.

#### List

```shell
cs endpoint-alias list

```text

It shows a list of all Endpoint Aliases.

#### Assign

```shell
cs endpoint-alias map ENDPOINT-ALIAS-NAME [SANDBOX-NAME ENDPOINT-NAME]

```text

The assignment can be changed at any time. If `SANDBOX-NAME` and `ENDPOINT-NAME` are unspecified, the Endpoint Alias becomes *Unassigned*.

#### Remove

```shell
cs endpoint-alias remove ENDPOINT-ALIAS-NAME

```text

## Service Account and Login Token

```shell
cs org service-account create NAME --display-name "DISPLAY NAME" --role ROLE
cs org service-account remove NAME
cs org login-token create ACCOUNT_EMAIL --valid-since TIME --expiry TIME \
  --redirect-path PATH --url
cs org login-token remove PARTIAL_TOKEN
cs org login-token list
cs org login-token show PARTIAL_TOKEN

```text

When create/remove a service account, only `NAME` is provided, and it will generate the account email as `NAME@org.sandbox`. `DISPLAY NAME` is optional. Additional `ROLE` can be specified with one or more `--role` flags. Current available roles are: `org-admin`.

When create a Login Token, the full `ACCOUNT_EMAIL` must be provided, e.g. `NAME@org.sandbox`. The flags `--valid-since` and `--expiry` is highly recommended. The value can be one of the following formats:

* `+DUR`: now plus a duration, e.g. `+30m`, `+4h`, `+1h20m`, etc;
* `-DUR`: now minus a duration, e.g. `-30m`, `-4h`, `-1h20m`;
* `@TIME`: at a specific time, e.g. `@12:10`, `@2022-06-07 21:30:00`

The `--redirect-path` can be specified to redirect to the specified path after login on the Web Console.
When `--url` is specified, the full login URL is printed instead of the token itself.

For *remove* and *show* commands of Login Token, a sub-string in the token can be provided as `PARTIAL_TOKEN` and the command will match the token.

A *Login Token* can be shared with a non-member of the organization to login from:

* Web Console: `<https://sandboxes.cloud/auth/token/TOKEN`>
* CLI: `cs login -t TOKEN`  Remember that if you are using self-hosted Crafting, please specify first `CRAFTING_SANDBOX_SERVER_URL=https://your.site.address`

For CLI use, a more secure practice is to put the token in a file, and use the following environment to point to the file, for example:

```shell
export CRAFTING_SANDBOX_AUTH_TOKEN_FILE=/somefolder/token
cs login

```text

Or

```shell
export CRAFTING_SANDBOX_AUTH_TOKEN=token
cs login

```text

## External Infrastructure and Kubernetes

For the details about Kubernetes support, please read [Setup for Kubernetes](https://docs.sandboxes.cloud/docs/kubernetes-setup).

#### Connect a Kubernetes Cluster

```shell
cs infra connect kubernetes [NAME]

```text

It installs the Crafting Kubernetes Agent into the current cluster and registers the cluster in the Crafting system under `NAME` which is only used on the Crafting system side for referencing the cluster and not necessary to be the exact cluster name.

##### Flags

* `--subnets`: a comma-separated CIDRs represents the subnets accessible in the cluster, and the agent will tunnel through the sandbox to access these subnets when interception is on. If unspecified, the command will try to detect the in-cluster Pod subnet and Service subnet. If failed, it will prompt for entering the CIDRs manually. Specifically for AWS EKS clusters, as they are using VPC subnets directly, the command won't be able to detect the Service subnet. In this case, simply provide the VPC CIDR;
* `--apiserver-proxy-clusterrole`: The cluster role that the API server proxy will run under. This is also the identity used for the sandboxes to access the API server. For most development usage, the default value is `cluster-admin`;
* `--disable-apiserver-proxy`: Disable the API server proxy completely. Sandboxes won't be able to access the API server through the agent. Additional setup is required (see [Setup for Kubernetes](https://docs.sandboxes.cloud/docs/kubernetes-setup)) if API server access is still desired.

#### List Connected Clusters

```shell
cs infra list

```text

#### Disconnect a Cluster

```shell
cs infra disconnect [NAME]

```text

This command will uninstall the Crafting Kubernetes agent and unregister the cluster from the Crafting system.

Before the operation, the command will perform some checks and aborts if there's any error. The flag `--ignore-check-errors` can be used to continue the operation if there're errors. However agent uninstallation will be disabled if there's any error. As a result, the cluster is unregistered with agent still running inside. With `--force-uninstall`, the uninstallation will be attempted after the cluster is unregistered.

To manually uninstall the agent, simply delete the namespace `crafting-sandbox`.

##### Flags

* `--ignore-check-errors`: continue unregistering the cluster even there were check errors;
* `--force-uninstall`: always attempt uninstalling the agent even there were check errors.

## CLI Extensions

A *CLI extension* is an executable with file name like `cs-FOO`, so the command `cs FOO` will invoke the executable `cs-FOO` with rest of the command line arguments.
An extension can be placed in any folder that can be looked up in `PATH` environment variable, or a git repository containing these files can be installed.

```shell
cs extensions install git@github.com:example/cs-ext
cs extensions install https://github.com/example/cs-ext
cs extensions install /absolute-path-to-a-local-folder
cs extensions list
cs extensions uninstall [PARTIAL-NAME]

```text

#### Install

Only two kinds of sources can be installed:

* A git repository
* A local folder

The same git repository but with different versions (branch/tag) are treated as different sources.

When looking up an extension command, the installed git repository will be updated automatically based on the default or specified version.

##### Flags

* `--version`: this is only used when a git repository is installed. Default is the `master` branch;
* `--subdir`: specify a sub directory inside the installed repository or folder for extension executables. By default, only the top-level directory is searched. The extension executables are only looked up in one level of directory, not recursively.

#### Uninstall

When uninstalling a git repository, the original repository URL and version must be matched. From the command line, partial content of the original URL can be provided, and the CLI will help to match the installed sources. If there are multiple matched, the user is asked to select one of them.
