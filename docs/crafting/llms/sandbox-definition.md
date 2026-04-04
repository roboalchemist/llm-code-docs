# Source: https://docs.sandboxes.cloud/docs/sandbox-definition.md

## Sandbox Definition

### Overview

A Sandbox is designed to provide an all-in-one, self-contained development environment (the on cloud potion of it, in contrast to client side, e.g., mobile app, desktop client, etc.). It contains a *definition* which defines what's inside the sandbox and how to create/run a sandbox. It's composed using a structured schema which includes:

* [overview](#overview): a markdown template to render the customized information in the sandbox details page;
* [env](#env): a list of sandbox-scope (applied to all workloads) environment variables;
* [workspaces](#workspaces): a Linux-based development environment with source code checked out, built and automatically launched as a service (often a micro service) to serve business specific functions;
* [dependencies](#dependencies): some commonly used services consumed by the `workspaces`, like MySQL, Postgres, Redis etc;
* [containers](#containers): a service launched using a container image;
* [volumes](#volumes): additional volumes to be attached to [containers](#containers);
* [endpoints](#endpoints): a DNS name exposed to the Internet and when accessed, the traffic is routed to a workspace based on the rules (e.g. HTTP routing based on path);
* [resources](#resources): a list of resources to be managed with sandbox lifecyle;
* [customizations](#customizations): additional customization capabilities for the convenience of using the sandbox.

A brief example represented in YAML:

```yaml
overview: |
  This sandbox is an example.
env:
- APP_NAME=example
- INSTANCE_TYPE=t2.micro
workspaces:            # Specifies all workspaces.
- name: frontend       # Workspace name which is also used as the hostname in a sandbox.
  checkouts:           # Specifies how to checkout source code.
  - path: src/frontend # The local path relative to $HOME to checkout source code.
    repo:
      github:          # Checkout from GitHub (GitHub integration required).
        org: sample    # GitHub org name.
        repo: frontend # Repository in the org.
  packages:            # Specifies the toolchains to be side-loaded.
  - name: nodejs
    version: '14.15.4'
  ports:               # Specifies the ports exposed by this workspace.
  - name: http
    port: 3000
    protocol: HTTP/TCP
  base_snapshot: base/frontend # The snapshot to restore the root filesystem.
  home_snapshot: home/frontend # The snapshot to restore files in home directory.
  probes:
    readiness:         # Specifies readiness probes.
    - name: http
      http_get:
        port: 3000
        path: /
- name: backend
  checkouts:
  - path: src/backend
    repo:
      github:
        org: sample
        repo: backend
  packages:
  - name: golang
    version: '1.17.2'
  ports:
  - name: api
    port: 8080
    protocol: HTTP/TCP
  base_snapshot: base/backend
  home_snapshot: home/backend
  probes:
    readiness:         # Specifies readiness probes.
    - name: http
      http_get:
        port: 8080
        path: /
  port_forward_rules:  # Forward local ports to a workspace/dependency.
  - local: "6379"      # The local port, must be a string.
    remote:
      target: redis
      port: redis
  wait_for:            # The list of workload names to wait for the readiness.
  - mysql
  system:
    daemons:
    - name: assistant
      run:
        cmd: /opt/assistant/bin/assistd
  lifecycle:
    on_create:
      run:
        cmd: ./lifecycle.sh
        dir: scripts
        env:
        - LC_FUNC=lc_$SANDBOX_LIFECYCLE
      max_retries: 3
      require_build: true
      timeout: 30m
    on_suspend:
      ... # Same schema as on_create.
    on_resume:
      ... # Same schema as on_create.
    on_delete:
      ... # Same schema as on_create.
dependencies:          # Specifies all dependencies required in the sandbox.
- name: mysql          # Dependency name which is also used as the hostname in a sandbox.
  service_type: mysql  # What kind of service the dependency provides.
  version: '8'         # The specific version of the service, optional.
  properties:
    database: app
- name: redis
  service_type: redis
containers:
- name: sqlpad
  image: sqlpad/sqlpad:latest
  env:
  - 'SQLPAD_AUTH_DISABLED=true'
  - 'SQLPAD_AUTH_DISABLED_DEFAULT_ROLE=admin'
  - 'SQLPAD_CONNECTIONS__mysql__name=mysql'
  - 'SQLPAD_CONNECTIONS__mysql__driver=mysql2'
  - 'SQLPAD_CONNECTIONS__mysql__host=mysql'
  - 'SQLPAD_CONNECTIONS__mysql__database=app'
  - 'SQLPAD_CONNECTIONS__mysql__username=root'
  - 'SQLPAD_DEFAULT_CONNECTION_ID=mysql'
  volume_mounts:
  - name: sqlpad
    path: /var/lib/sqlpad
  wait_for:
  - mysql
volumes:
- name: sqlpad
endpoints:             # The endpoints exposed to Internet.
- name: app            # Endpoint name which is used as part of the DNS name.
  http:                # This is an HTTP endpoint.
    routes:            # The HTTP routing rules.
    - path_prefix: /   # Matches all paths.
      backend:         # Route to the specified workspace and port.
        target: frontend
        port: http
resources:
- name: aws
  brief: Dev Resources on AWS
  terraform:
    workspace: dev
    dir: deploy/tf
    run:
      timeout: 600s
      vars:
        instance_type: '$INSTANCE_TYPE'
customizations:
- env:
    name: INSTANCE_TYPE
    display_name: EC2 Instance Type
    choice:
      options:
      - t2.micro
      - t3.medium
      - t3.large
- flavor:
    name: slim
    excludes:
    - sqlpad
    - aws
```

## Sections

### Template Overview

This defines an optional markdown template for rendering an informational section in the sandbox details page.

The template follows the [guide](https://handlebarsjs.com/guide/) for the syntax, with the following predefined variables:

| Variable Name                 | Description                                                                                                           | Org       | Sandbox   |
| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :-------- | :-------- |
| org.name                      | The name of current org.                                                                                              | Supported | Supported |
| user.email                    | Email of current user.                                                                                                | Supported | Supported |
| sandbox.name                  | Name of the current sandbox, if applicable.                                                                           |           | Supported |
| sandbox.createdAt             | Sandbox creation time, if applicable.                                                                                 |           | Supported |
| sandbox.updatedAt             | The last updated time of the current sandbox, if applicable.                                                          |           | Supported |
| sandbox.template              | The associated template's name of the current sandbox, if applicable.                                                 |           | Supported |
| sandbox.owner                 | The owner of current sandbox, if applicable.                                                                          |           | Supported |
| endpoints.\[endpoint-name].url | The full URL of an endpoint. If there is no endpoint named as *endpoint-name*, the variable is deemed as unknown one. |           | Supported |
| endpoints.\[endpoint-name].dns | The DNS part of an endpoint. If there is no endpoint named as *endpoint-name*, the variable is deemed as unknown one. |           | Supported |
| resources.\[name].state....    | Referencing the value of the saved state of a resource.                                                               |           | Supported |

For example, a Template with:

```yaml
overview: |
  # Sandbox Notes

  - Sandbox name: {{sandbox.name}}
  - Last updated: {{sandbox.updatedAt}}
  - Owner: {{sandbox.owner}}
  - Template: {{sandbox.template}}

  For unknown variable, we display {{unknown}}
```

will generate the following section in the sandbox details page:

```markdown
# Sandbox Notes

- Sandbox name: sandbox-name
- Last updated: 2022-01-01
- Owner: sandbox-user
- Template: example-template

For unknown variable, we display
```

### Env

A list of sandbox-scoped [environment variables](https://docs.sandboxes.cloud/docs/environment-variables) which will be applied to all workspaces.

### Workspaces

A workspace is a Linux-based development environment which runs services by automatically checking out source code, building and launching. A developer is able to access the workspace using SSH, WebIDE etc remotely and debug the service live.

A workspace is defined with the following information:

* [checkouts](#checkouts): how to checkout source code;
* [ports](#ports): the ports exposed by the workspace;
* [snapshots](#snapshots): the snapshots used to restore files;
* [probes](#probes): the readiness probes;
* [port forwarding](#local-port-forwarding): port-forwarding from the workspace to other workspaces, dependencies or containers;
* [env](#workspace-environment-variables): environment variables applied to the current workspace;
* [system](#workspace-system): system configurations, like daemons etc;
* [wait for](#wait-for): define the runtime dependencies;
* [access restriction](#access-restriction): define the workspace *Restricted* mode;
* [lifecycle](#lifecycle) : the workspace level lifecycle hooks.

#### Checkouts

A checkout defines the rule to checkout source code from one repository, with all properties shown below:

```yaml
checkouts:           # Specifies how to checkout source code.
  - path: src/frontend # The local path relative to $HOME to checkout source code.
    repo:
      # Only one of the following sources can be specified:
      
      # Using GitHub integration.
      github:
        org: sample    # GitHub org name.
        repo: frontend # Repository in the org.
 
      # Or using direct git checkout.
      # The value is a URI accepted by "git clone"
      git: git@github.com:sample/frontend
    
    # Optional version specification for checkout.
    version_spec: branch # or tag, or commit hash

    # Do not checkout submodules recursively.
    # Default is false.
    disable_recursive_checkout: true
    
    # Limit the checkout history.
    # Specify this helps significantly speed up checkout when
    # working with large repositories.
    history:
      # The history depth. This value is passed as-is to
      # git flag --depth.
      depth: 10
      # Checkout history no earlier than the specified time.
      # This value is passed as-is to git flag --shallow-since.
      since: '2022-01-01'

    # Manifest overrides.
    manifest:
      overlays:
      - name: alternate
      - file: dir/filename.yaml
      - content: |
          daemons:
            frontend:
              run:
                cmd: yarn run start-alternate
```

The local path of a working copy and remote are defined by `path` and `repo`. The value of `path` is relative to home directly (`$HOME`). The `repo` property specifies one (and only one) of the supported methods to perform the checkout operation:

* `github`: this can only be used when the org completes [GitHub Integrartion](https://docs.sandboxes.cloud/docs/github-integration), and the GitHub organization name and repository name are specified;
* `git`: use direct `git clone` to perform checkout. The value is passed to `git clone`. Based on the URI, credentials may be pre-configured (e.g. using `git@...` requires the managed public key (use CLI `cs info` to display it) of the developer to be registered in the git source control service provider.

If `version_spec` is unspecified, the code is checked out from the default branch (`master` or `main` - for GitHub). Otherwise, it can be specified using one of

* a branch name
* a tag name
* a commit hash

If the repository contains git submodules, they are automatically checked out unless `disable_recursive_checkout` is set to `true`.

The property `manifest` is used as a mechanism to skip the [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest) sits in the code base (file `.sandbox/manifest.yaml`) and use the overlays specified inline which are merged to generate a final manifest. There are 3 ways to define an overlay:

* `name`: the value specifies an alternative filename in `.sandbox` folder, so file `.sandbox/$(name).yaml` will be loaded;
* `file`: the full path of the file inside the source repo to load, so the file may sits in a folder other than `.sandbox`;
* `content`: the inline content of the [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest).

The overlays are merged using the following rules:

* `env`: environment variables are replaced by the variable name;
* `hooks`: the hook definition is replaced completely by hook name;
* `daemons` and `jobs`: the daemon/job is replaced completely by the name.

##### Manifest Override Examples

Assume in the source code, the file `.sandbox/manifest.yaml` contains:

```yaml
env:
- SERVER_NAME=dev
- BACKEND_URL=http://backend:8080

daemons:
  server:
    run:
      cmd: ./start-server.sh
      env:
      - SERVER_KEY=abc
```

1. Completely replace the manifest

In `checkout`, define the following:

```yaml
# Manifest overrides.
    manifest:
      overlays:
      - content: |
          daemons:
            frontend:
              run:
                cmd: yarn start
```

Because `manifest` is specified in `checkout`, the `.sandbox/manifest.yaml` is skipped. And the final result will be that defined in `checkout`.

1. Override environment and the daemon

In `checkout`, define the following:

```yaml
# Manifest overrides.
    manifest:
      overlays:
      - name: manifest  # Load .sandbox/manifest.yaml
      - content: |
          env:
          - BACKEND_HOST=localhost
          - BACKEND_URL=http://$BACKEND_HOST:8080
          daemons:
            server:
              run:
                cmd: ./start-server.sh --backend-as-remote
```

In the example, the first overlay loads the default manifest (it was skipped as manifest is specified. however now it's explicitly loaded), and the next overlay specifies the overrides. According to the rule, `env` are replaced by variable name, and `daemons` are replaced by name, so the result manifest is:

```yaml
env:
- SERVER_NAME=dev
- BACKEND_HOST=localhost
- BACKEND_URL=http://$BACKEND_HOST:8080

daemons:
  server:
    run:
      cmd: ./start-server.sh --backend-as-remote
```

Note: environment `SERVER_KEY` no longer exists because `daemon.server` is replaced completely.

1. Use alternative manifest file

In `checkout`, define the following:

```yaml
# Manifest overrides.
    manifest:
      overlays:
      - name: alternate  # Load .sandbox/alternate.yaml
      - name: patch1     # Load .sandbox/patch1.yaml
      - file: config/env.yaml # Load config/env.yaml
```

The above example will generate a final manifest by merge `.sandbox/alternate.yaml`, `.sandbox/patch1.yaml` and `config/env.yaml` together using the merge rules.

#### Ports

The property `ports` defines the exposed ports of the workspace. This is important information that the sandbox system will be aware of the service exposed by the workspace and how to route the traffic:

* `name`: a name to reference the port, e.g. referenced in endpoint's HTTP routes;
* `port`: the number of the port;
* `protocol`: the protocol running on the port, specified in `L7/L4` or `L4` format. The supported `L4` protocols are `TCP` and `UDP`. If `L4` is `TCP`, `L7` can be one of:
  * `HTTP`: the plain text HTTP protocol;
  * `HTTPS`: HTTP over TLS;
  * `GRPC`: the gRPC protocol over HTTP/2;
  * `H2`: the HTTP/2 protocol;
  * `H2C`: the plain text HTTP/2 protocol.

Although `protocol` is optional (default is `TCP`), it's highly recommended specifying it explicitly. Some features require a specific value of `protocol`, e.g. `HTTP/TCP`.

#### Snapshots

[Snapshots](https://docs.sandboxes.cloud/docs/snapshots) can be restored during workspace creation in two tiers, all optional:

* `base_snapshot`: when specified, the snapshot is used to restore the workspace's root filesystem, excluding `/home` and some other temporarily folders (e.g. `/tmp`); A custom container image from a *public* container registry can be used with prefix `oci://`, e.g.
  * `oci://gcr.io/example/path/image:tag` (pulled from gcr.io)
  * `oci://example/image:tag` (pulled from docker hub)
    There are requirements about building a custom container image to be used as a base snapshot. Please read [Custom Container Image as Base Snapshot](#custom-container-image) below for more details.
* `home_snapshot`: when specified, the files from that snapshot are extracted to the owner's home directory (`$HOME`, it's `/home/owner` in most cases).

Snapshots are only restored during workspace creation time. Future changes of the snapshots after a sandbox is created will not be applied to workspaces.

##### Custom Container Image

A custom container image can be used as a base snapshot, if the image is built with:

* bash
* git
* rsync
* jq
* iptables (if docker daemon will run inside the workspace)
* sudo with password-less config
* UID/GID of 1000/1000 is not used

Here is an example of a minimal Dockerfile to build a custom container image:

```dockerfile
FROM ubuntu:22.04
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata locales locales-all sudo git rsync iptables && \
    update-locale LANG=en_US.UTF-8 && \
    sed -i -r 's/^(%sudo\s).+$/\1ALL=(ALL) NOPASSWD:ALL/g' /etc/sudoers
```

##### Home Skeleton in Base Snapshot

During the initial setup of a newly created workspace, following standard, the home directory is created using the skeleton from `/etc/skel`. By leveraging the skeleton folder, the base snapshot may contain the content for home directory and thus reduce the need of a home snapshot. The sandbox system will look up the skeleton from the following folders and use the first one it found:

* `/etc/skel.sandbox`
* `/etc/skel`

If not found, an empty home folder is created.

##### Startup Scripts

After the home directory is set up, the sandbox system looks up the following scripts and execute in order (when available) every time a workspace starts up:

* `/etc/sandbox.d/setup`
* `~/.sandbox/setup`

#### Probes

Probes define extra mechanisms to determine whether the services in the workspace is ready or not, with the capability to leverage business specific logic. A probe definition requires exact one of 3 supported methods:

* `command`: a full command line (interpreted by `$SHELL -c`) run from `/` as `root` during every sampling cycle, and the success of the command (exit code 0) indicates a positive result of the probe;
* `tcp_port`: a numeric port (not necessary to be a port from the [`ports`](#ports) section) that a TCP connection will be attempted during every sampling cycle, and the success of connect indicates a positive result of the probe;
* `http_get`: `port` specifies a numeric port (not necessary to be a port from the [`ports`](#ports) section) and `path` specifies an HTTP path in the request so that an HTTP GET request will be issued during every sampling cycle. The HTTP status code 2xx indicates a positive result of the probe.

Additional properties are available to alter the parameters for sampling:

* `interval`: duration in the formation of `SSSs` where `SSS` is in seconds and suffixed by character `s` representing the unit. It specifies the interval between two sampling cycles in seconds;
* `positive_threshold`: number of consecutive positive results to turn the current state to positive;
* `negative_threshold`: number of consecutive negative results to turn the current state to negative;
* `initial_delay`: duration in the formation of `SSSs` where `SSS` is in seconds and suffixed by character `s` representing the unit. It specifies the duration the probe will not start to evaluate since the creation of the workspace;
* `initial_negative_threshold`: number of consecutive negative results to yield a negative state during initialization (specifying 0 here will use a default value which may not be 0).

Some examples of probe definitions:

```yaml
probes:
    readiness:         # Specifies readiness probes.
    - name: http
      http_get:
        port: 8080
        path: /
    - name: ok
      command: '/usr/bin/status'
      interval: 60s    # Run every minute.
    - name: port
      tcp_port:
        port: 8000
      initial_delay: 300s
      positive_threshold: 1 # as soon as the connection can be established, signal positive.
      negative_threshold: 3 # signal negative only after 3 consecutive failures.
```

Custom probes can also be used for activity detection which indicates if there's any user activities going on so the sandbox should not be auto-suspended:

```yaml Activity Probe Example
probes:
  activity:
  - name: custom-user-activity
    command: 'custom-user-activity-detect.sh'
```

Note: the exit code `0` is used to indicate on-going activities, while non-zero exit code indicates there's no on-going activities.

Also the built-in activity detectors can be explicitly disabled or enabled. Given the following example:

```yaml Built-in Activity Probes
probes:
  activity:
  - name: custom-user-activity
    command: 'custom-user-activity-detect.sh'
  activity_detection:
    disable_builtin_probes:
    - ANY
    enable_builtin_probes:
    - ENDPOINT
```

It will disable all (given the special name `ANY`) builtin probes and then enable only `ENDPOINT` probe. The available built-in probes are:

| NAME         | DESCRIPTION                                                                                                                                                                                                                                                  |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSH          | Established SSH connections will be counted as user activity. This includes all remote IDE connections over SSH.                                                                                                                                             |
| PORT\_FORWARD | Any running `cs portforward` on the client side will be counted as user activity.                                                                                                                                                                            |
| EXEC         | Any running `cs exec` sessions will be counted as user activity.                                                                                                                                                                                             |
| CLIENT       | Any background `cs` sessions (e.g. auto port-forward) launched by other `cs` commands like `cs vscode`, `cs ssh`,  `cs jetbrains` etc will be counted as user activity.                                                                                      |
| WEB\_TERMINAL | Any opened web terminal sessions will be counted as user activity.                                                                                                                                                                                           |
| WEB\_IDE      | Any connected web IDE sessions will be counted as user activity.                                                                                                                                                                                             |
| RDP          | Any connected Remote Desktop sessions, including Web based and client based, will be counted as user activity.                                                                                                                                               |
| JETBRAINS    | Any connected Jetbrains IDE sessions to the remote dev server launched by `cs jetbrains remote-dev-server run ...` will be counted as user activity. Note: the session connected directly to the Jetbrains remote dev server processes are counted as `SSH`. |
| ENDPOINT     | Any established connections to the sandbox endpoints are counted as user activity.                                                                                                                                                                           |

There's a special name `ANY` references all the built-in probes which can be used in either `disable_builtin_probes` or `enable_builtin_probes`.

#### Local Port Forwarding

Example:

```yaml
workspaces:
- name: work
  port_forward_rules:
  - local: '6379'
    remote:
      target: redis
      port: redis
  - local: '/run/backend.sock'
    remote:
      target: backend
      port: api
- name: backend
  ports:
  - name: api
    port: 8080
    protocol: HTTP/TCP
dependencies:
- name: redis
  service_type: redis
```

The property `port_forward_rules` maps a port (or a unix domain socket) on `localhost` to an exposed port on a workspace or a dependency in the same sandbox.

This feature is designed for 2 purposes:

* Provide optional information about the dependencies of the current workspace;
* Minimizing the change of code expecting a local-only environment (with dependencies configured on localhost).

However, a more cloud-native approach is using [service linking](https://docs.sandboxes.cloud/docs/port-forwarding#service-linking) and avoid accessing `localhost` with ports defined in `port_forward_rules`. When using [service linking](https://docs.sandboxes.cloud/docs/port-forwarding#service-linking), a dependency can be resolved using environment variables:

* `<NAME>_SERVICE_HOST`
* `<NAME>_SERVICE_PORT`

These environment variables are available in every workspace. In the `backend` workspace example above, the `port_forward_rules` can be avoided if the source code accesses `redis` using `$REDIS_SERVICE_HOST:$REDIS_SERVICE_PORT`.

In the extent of using `port_forward_rules`, the `local` property can be defined in one of the following forms:

* `PORT`: the port number listening ONLY on `localhost`;
* `+PORT`: the port number listening ONLY on the primary network interface (e.g. `eth0`);
* `*PORT`: the port number listening on ALL network interfaces;
* `/PATH`: the absolute path of a unix domain socket.

The `remote` property specifies the destination. `target` is the name of the destination service (name of a workspace, dependency or a container), and `port` is the name of the port exposed by the destination service. If it's a dependency, the port name can be found by `cs depsvc list` or from [https://sandboxes.cloud/dependencies](https://sandboxes.cloud/dependencies).

#### Workspace Environment Variables

A list of [environment variables](https://docs.sandboxes.cloud/docs/environment-variables) applied to the current workspace, based on the built-in and sandbox-scoped environment variables.

#### Workspace System

Configurations on the system level, like daemons and/or files.

```yaml
workspaces:
- name: example
  system:
    daemons:
    - name: foo
      run:
        cmd: /opt/foo/foo
        dir: /opt/foo
        env:
        - FOO=BAR
    files:
    - path: /etc/sandbox.d/setup
      mode: '0755'
      overwrite: true
      content: |
        #!/bin/bash
        echo "Setting up workspace"
    - path: ~/.sandbox/setup
      mode: '0755'
      overwrite: true
      content: |
        #!/bin/bash
        echo "Setting up for user"
    - path: /work/placeholder
      owner: '1000:1000'
      template: |
        SANDBOX={{env "$SANDBOX_NAME"}}
    - path: ~/.env
      symlink: /run/sandbox/fs/secrets/shared/dotenv
    - path: ~/.foo/credentials
      mode: '0600'
      secret:
        name: foo-creds
```

This defines a background process `foo` to be launched when workspace starts. This runs before any checkout/build hooks to provide support as part of the workspace system. The processes defined here will be launched and monitored. It's restarted if it stops.

The definition is equivalent to individual YAML files in the `/etc/sandbox.d/daemons` folder. For example, the above daemon can be defined in a file `/etc/sandbox.d/daemons/foo.yaml` (this can be baked into a base snapshot):

```yaml
name: foo
run:
  cmd: /opt/foo/foo
  dir: /opt/foo
  env:
  - FOO=BAR
```

The `files` section defines the injections to the workspace file system. The `path` specifies the absolution path (must be an absolute path, or starts with `~/` to indicate inside the home directory) in the workspace. When the path starts with `~/`, it's inside the home directory, and the default ownership will be `owner:owner` (or `1000:1000`) rather than `root`. The ownership can always be specified using `owner` (the value must be `UID:GID`). The content of the file can be exact one of the following:

* `content`: a plain text file;
* `template`: the content is rendered using the specified Go template. There are special functions to be used for:
  * `{{ env "STRING" }}` perform env expansion on `STRING`. For example, the `STRING` can be something like `The sandbox $SANDBOX_NAME is owned by $SANDBOX_OWNER_EMAIL` which contains multiple env expansions. Keep in mind, the `STRING` is not the env name, use `$` to expand an env in the `STRING`;
  * `{{ secret "NAME" }}` to extract the content of the specified shared secret `NAME`.
* `symlink`: `path` specifies a symbolic link, and the target is specified as the value here;
* `secret`: the content is from the shared secret.

The `mode` can be used to specify the permission of the file/directory. Please quote the value as a string, otherwise YAML will interpret it incorrectly. If `mode` is unspecified, the system will use `0755` for directories and `0644` for files.

The `overwrite` flag specifies the content of the file must match what's being specified exactly in the template. If the file/symlink exists with different content, it will be overwritten. If this flag is `false` (or unspecified), the existing file/symlink will not be touched.

#### Wait For

A list of workload names (also including resource names) to be specified that the workspace doesn't start any daemons before those are ready (depending on the readiness probes). This introduce dependencies between the workloads and resources, cyclic dependencies are not allowed.

#### Access Restriction

Specify the workspace should run in the [Restricted Mode](https://docs.sandboxes.cloud/docs/cloud-resources-setup#restrict-access-to-workspaces-and-secrets)  that only org-admin is able to access it (over SSH, Web Terminal, WebIDE, Remote Desktop etc), and secrets with access restriction set to *Admin Only* will be mounted.

```yaml
workspaces:
- name: example
  ...
  restriction:
    life_time: STARTUP
```

The `life_time` can be one of the values:

* `STARTUP`: the workspace is created in *Restricted* mode, and can exit later at any time up-on request by any user who has *Update* permission to the sandbox. Once the workspace exits the *Restricted* mode, it can never get back to *Restricted* mode again, and secrets with access restriction set to *Admin Only* will be unmounted;
* `ALWAYS`: the workspace is created in *Restricted* mode and can't exit.

The restriction setting is permanent once the workspace is created and won't be changed even the Sandbox Definition is updated.

#### Lifecycle

Add additional hooks to be executed during special sandbox lifecycle events:

* on\_create: the hook will be executed during sandbox creation, after all setup tasks (e.g. checkout, build etc) are completed;
* on\_suspend: the hook will be executed before the sandbox is being suspended. Failure of the hook will prevent the sandbox from being suspended;
* on\_resume: the hook will be executed after the sandbox is resumed;
* on\_delete: the hook will be executed before the sandbox is being deleted. Failure of the hook will prevent the sandbox from being deleted.

In the case of lifecycle hook failures, the sandbox/workload will not be able to move the next lifecycle state. In this case, the workspace is still accessible, so the owner is able to troubleshoot. After that, either use the UI or [CLI](https://docs.sandboxes.cloud/docs/command-line-tool#lifecycle-related)  to resolve the failure and let the lifecycle transition move on.

All lifecycle failures except `on_suspend` still allow sandbox auto-suspension of there's no activities. After resume the failure will be restored and requires resolution, unless `on_resume` failed, in which case, the previous failure will be replaced by `on_resume` failure.

The lifecycle hooks are executed in respect to the implicit/explicit dependency relationships between the workloads and resources. For example, workspace A has a `wait_for` including workspace B, so `A.on_create`/`A.on_resume` will be after `B.on_create`/`B.on_resume`, and `A.on_suspend`/`A.on_delete` will be before `B.on_suspend`/`B.on_delete`. Within resources, when `use_workspace` is defined, it's an implicit dependency between the resource and the workspace. The resource's `on_create/on_resume` will be after the workspace's `on_create/on_resume`, and vice versa for `on_suspend/on_delete`.

### Dependencies

The section `dependencies` lists the well-known services to be added to a sandbox and consumed by the other workloads. A *dependency* is a service managed by the sandbox system and deployed in sandboxes for development purpose (single instance, non-clustered, no HA, no backup). To get a list of currently supported dependencies, visit the [web console](https://sandboxes.cloud/dependencies) or run CLI `cs dependency-service list`.

When defining a dependency, properties `name` and `service_type` are mandatory.
The property `name` specifies the name of the dependency, and it's also used as the *hostname* inside a sandbox network to reach to the service. The environment variables for service injection will be generated per workspace using the name.
The property `service_type` specifies the actual type of the dependency (checkout from [web console](https://sandboxes.cloud/dependencies) or run CLI `cs dependency-service list`).
The property `version` specifies a version explicitly. Otherwise, a default version (defined by the dependency service) will be used.
The property `snapshot` optionally specifies the name of a snapshot to restore during the creation of the dependency, if snapshot functionality is supported.
The property `properties` optionally defines a key/value map to provide parameters for creation the dependency. The definition of key/value pairs are dependency specific. Here is a list of properties defined by the currently supported dependencies (or find out using CLI `cs dependency-service show SERVICE_TYPE`):

<HTMLBlock>
  {`
  <table style="width: 100%; border-collapse: collapse;">
  <thead>
  <tr>
    <th style="border: 1px solid #ddd; padding: 8px;">Service Type</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Property Key</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>mysql</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>root-password</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The initial password of root. Default is empty (no password required for root).</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"></td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>username</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The regular user to be created.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"></td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>password</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The password for the regular user. It&#39;s only used if <code>username</code> is specified.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"></td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>database</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The database to be created and grant access to the regular user (if <code>username</code> is specified).</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>postgres</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>username</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The regular user to be created.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"></td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>password</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The password for the regular user. It&#39;s only used if <code>username</code> is specified.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"></td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>database</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The database to be created and grant access to the regular user (if <code>username</code> is specified).</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>mongodb</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>replicaset</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The name of replicaset. If specified, the single-instance mongodb server will be configured as a single-instance replicaset.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>redis</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>persistence</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>If specified, turn on persistence. Use one of the values:  </p>
  <ul>
  <li><code>appendonly</code>: persist data using append-only file;</li>
  <li><code>rdb</code>: persist data using RDB.</li>
  </ul>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"></td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>save</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The <code>save</code> configuration, in the format of <code>SECONDS CHANGES; SECONDS CHANGES ...</code>. Example: <code>900 1; 300 10; 60 10000</code>.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"></td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>cluster</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>If the value is <code>yes</code> (or <code>y</code>), <code>true</code>  (or <code>t</code>), (note, must be a quoted string when define in YAML), configure the single-instance redis to be a single-instance redis cluster (the single instance covers all partitions).</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>rabbitmq</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>default-user</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The default username for authentication. If unspecified, guest user can access.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"></td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>default-pass</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The password for <code>default-user</code> if specified.</p>
  </td>
  </tr>
  </tbody>
  </table>
  `}
</HTMLBlock>

### Containers

The section `containers` defines the workloads created directly from container images. It provides the flexibility that a developer may bring in any services as long as there's a container image (private container registries are not supported yet).

A container is defined with the following information:

* image: the container image, following the docker image naming convention;
* entrypoint, args, cwd: corresponding to [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint), [CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [WORKDIR](https://docs.docker.com/engine/reference/builder/#workdir) in docker image configuration;
* [ports](#ports): the ports exposed by the container and the protocol;
* [env](#container-environment-variables): environment variables added to the container;
* [probes](#probes): the readiness probes;
* [volume\_mounts](#volume-mounts): additional volumes mounted into the container;
* [run\_as](#run-as): run as a specified user/group;
* [snapshot](#container-snapshot): restore snapshot during creation.

Different from containers run on other system (docker, Kubernetes etc.), all containers running in a Sandbox has the filesystem persisted. Restarting a container workload will not reset the filesystem. So in most cases, it's not necessary to specify an item in `volume_mounts` unless the volume needs to be shared across multiple containers.
If resetting the file system is needed, rebuilding the container will get everything erases: `cs sandbox rebuild -S SANDBOX WORKLOAD`.

#### Volume Mounts

Additional volumes can be mounted into the container, given:

```yaml
containers:
- name: sqlpad
  ...
  volume_mounts:
  - name: sqlpad
    path: /var/lib/sqlpad
  - name: files
    path: /etc/config/example.conf
    sub_path: example.conf
```

The `name` specifies the name of a *volume* (defined under [volumes](#volumes) section). And `path` specifies the path inside the container and it must be an absolute path without `.` or `..` in the middle. The final mountpoint can be a directory or a file based on what's mapped in the original volume. When `sub_path` is being used, it references a path under the original volume.

#### Run As

By default, the user/group specified in the container image (or root/root when unspecified) is respected. If specified, this will override that in the container image. The value can be either username/groupname or uid/gid. Example:

```yaml
# All fields are optional
containers:
- name: example1
  run_as:
    user: user1
    group: group1
- name: example2
  run_as:
    user: user
- name: example3
  run_as:
    uid: 1000
- name: example4
  run_as:
    uid: 1000
    gid: 900
```

#### Container Environment Variables

This is similar to [Workspace Environment Variables](#workspace-environment-variables). The final environment variables are generated from the sources in the order of:

* Environment variables defined in the container image;
* App/Sandbox environment variables;
* Environment variables defined in the container.

#### Container Snapshot

Snapshot can be taken from volumes of a running container. This is only supported when there are at least one `volume_mounts` defined in the container backed by a [regular persistent volume](#regular-volume). The `volume_mounts` backed by regular persistent volumes are also used as the schema of the snapshot so it can only be restored to a container with the same set of `volume_mounts`.

Similar to dependency snapshots, during snapshot creation/restoring, the container is temporarily stopped.

#### Container Wait For

Same as workspace, the container doesn't start until the workloads in the `wait_for` list become ready (relying on the readiness probe).

### Volumes

The section `volumes` defines the volumes referenced by the entries under [volume\_mounts](#volume-mounts) of [containers](#containers) section.

A *volume* can be one of the following types:

* [Regular](#regular-volume): a persistent volume shared with one or more containers;
* [Content](#content-volume): a read-only volume with predefined content;
* [Secret](#secret-volume): a volume containing the content of a [Secret](https://docs.sandboxes.cloud/docs/secrets);
* [Workspace Filesystem](#workspace-filesystem-volume): a volume exposing as a shared file system backend by a workspace.

#### Regular Volume

A volume defined with only a *name* represents a regular, persistent volume:

```yaml
volumes:
- name: data
```

A regular volume can be shared by one or more containers. When multiple containers reference the same regular volume, during runtime, these containers may be co-located on the same host under-the-hood, and the volume is shared for reading and writing.

#### Content Volume

A read-only volume with predefined content. For example:

```yaml
volumes:
- name: json_config
  content:
    text: |
      {
        "key": "value"
      }
- name: yaml_config
  content:
    text: |
      key: value
- name: config
  content:
    text: |
      some text information
      another line
- name: binary_config
  content:
    binary: !!binary "SGVsbG8gV29ybGQK"
```

A content volume is mounted as a file inside a container. Either the `text` or `binary` value is used as the content of the file as-is.

When the content is updated in the App Definition, the file inside the container will reflect the change immediately after the sandbox is in sync.

#### Secret Volume

A read-only volume with content from a *shared* secret.

```yaml
volumes:
- name: cred
  secret:
    name: shared-cred
```

A secret volume is mounted as a file inside a container.

#### Workspace Filesystem Volume

A pseudo volume exposing the root filesystem of a workspace as a shared filesystem.

```yaml
volumes:
- name: work
  workload:
    name: workspace
    prefix: /
```

The volume is mounted as a remote filesystem inside a container. By default `prefix` is `/` which will expose the full root filesystem. If `prefix` is defined, it will be prepend to every filesystem access request to construct the final path inside the workspace filesystem.

Not all paths in the workspace filesystem is exposed. Mountpoints like `/proc`, `/sys`, `/dev/shm` etc are not exposed.

### Endpoints

The section `endpoints` specifies how the application in a sandbox can be accessed from the Internet so it can be tested end-to-end, advertised as a demo, etc. Most ports exposed by workspaces and dependencies are private inside the sandbox network. An `endpoint` is used to route traffic from Internet to one of these ports. Only TCP or HTTP endpoints are supported.

#### HTTP Endpoint

An HTTP endpoint has the capability of routing HTTP requests based on matchers and optionally supports authentication using Single-Sign-On from the sandbox system. For example:

```yaml
endpoints:
- name: app
  http:
    routes:
    - path_prefix: /
      backend:
        target: frontend # workspace name
        port: http       # port name defined in the workspace
```

The property `name` defines the name of the endpoint and it will also be part of the generated DNS name over the Internet.
The property `path_prefix` defines a string prefix to literally match the request path. When matched, the request is routed to the destination specified by `backend`. If multiple rules are specified, the one matches longest wins.

As most of the sandboxes are for development purpose, it's insecure to expose an endpoint to the Internet without access control. By default, all HTTP endpoints are protected by Single-Sign-On from the sandbox system. Without further configuration, only members in the same organization are allowed to access the protected endpoints. For some cases, like the application already implements authentication (e.g. API-only endpoints), or for demo purpose, the Single-Sign-On protection can be explicitly disabled:

```yaml
endpoints:
- name: api
  http:
    auth_proxy:
      disabled: true    # Explicitly disable SSO protection.
    routes:
    - path_prefix: /
      backend:
        target: backend # workspace name
        port: api       # port name defined in the workspace
```

For some demo cases, customers not in the organization are invited to try out. An endpoint can be configured with extra policy that the Single-Sign-On protection will allow or reject based on individual identity:

```yaml
endpoints:
- name: app
  http:
    auth_proxy:
      rules:             # Custom access control policy.
      - regexp: "i.+-c@sample.com"
        action: REJECT
      - pattern: "ext@sample.com"
        action: REJECT
      - pattern: "*@sample.com"
        action: ACCEPT
    routes:
    - path_prefix: /
      backend:
        target: frontend # workspace name
        port: http       # port name defined in the workspace
```

The above example will allow all organization members and selected customer emails to access the endpoint. For certain demo only use cases, organization members can also be excluded by setting `auth_proxy.disable_defaults` to `true`, for example:

```yaml
endpoints:
- name: app
  http:
    auth_proxy:
      rules:             # Custom access control policy.
      - regexp: "i.+-c@sample.com"
        action: REJECT
      - pattern: "ext@sample.com"
        action: REJECT
      - pattern: "*@sample.com"
        action: ACCEPT
      disable_defaults: true # This will not allow organization members
    routes:
    - path_prefix: /
      backend:
        target: frontend # workspace name
        port: http       # port name defined in the workspace
```

##### Default Path

This is informational only. When specified, the URL opened by clicking the endpoint from the WebConsole will have this path instead of `/`.

```yaml
endpoints:
- name: dashboard
  http:
    routes:
    - path_prefix: /
      backend:
        target: dashboard
        port: http
    path: /dashboard
```

With above example, the endpoint URL on the WebConsole contains path `/dashboard` rather then `/`.

##### Header Injection

Custom headers can be injected, for example:

```yaml
endpoints:
- name: app
  http:
    routes:
    - path_prefix: /
      backend:
        target: dev
        port: http
    request_headers:
      X-App-Env: 'sandbox-{{.SandboxID}}'
    response_headers:
      X-App-Server: 'sandbox-{{.SandboxID}}'
```

The value can be a Go template with some variables being substituted.

| Context               | Value                                                                                                                        |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| `.Org`                | Org name                                                                                                                     |
| `.SandboxID`          | Current sandbox ID                                                                                                           |
| `.SandboxName`        | Current sandbox name                                                                                                         |
| `.EndpointDNSSuffix`  | The suffix (without endpoint name) to construct the full DNS name of an Endpoint. For example: `--sandbox-org.sandboxes.run` |
| `.EndpointBaseDomain` | The base domain of endpoint DNS, e.g. `sandboxes.run`                                                                        |
| `.EndpointName`       | The name of the current endpoint                                                                                             |
| `.EndpointDNS`        | The DNS of the current endpoint                                                                                              |
| `.SysBaseDomain`      | The base domain of Crafting system: `sandboxes.cloud`                                                                        |
| `.SysDNSSuffix`       | The suffix to construct DNS names with system base domain, e.g. `.sandboxes.cloud`                                           |
| `.AppDNSSuffix`       | The suffix to construct endpoint DNS names, e.g. `.sandboxes.run`                                                            |

##### Passthrough Mode

This is a special mode of an HTTP endpoint which provides capability of header-based (e.g. API-key) authentication when regular OAuth is not applicable (e.g. Service-to-service communication). This can be configured as:

```yaml
endpoints:
- name: api
  http:
    routes:
    - path_prefix: /
      backend:
        target: api-server
        port: http
    auth_proxy:
      mode: PASSTHROUGH
      passthrough:
        required_headers:
        - header: X-Api-Key
          regexp: '^apikey-123456$'
```

#### TCP Endpoint

A TCP endpoint forwards TCP connections to the specified backend:

```yaml
endpoints:
- name: conn
  tcp:
    backend:
      target: backend
      port: tcp
```

TLS is always required for TCP connections, and the endpoint terminates the TLS (without requiring/verifing client certificates) so the backend talks only in plaintext.

#### Internal Endpoint

An endpoint can be defined as internal which is assigned an internal DNS names and can be accessed by other sandboxes:

```yaml
endpoints:
- name: foo
  type: INTERNAL
  ...
```

Internal endpoints are assigned a DNS name like `NAME--SANDBOX-ORG.sandboxes.internal`. So the above endpoint in sandbox (assume name `sandbox1`) in org (assume name `org1`) can be accessed from other sandboxes via `foo--sandbox1-org1.sandboxes.internal`. Note, internal endpoints are exposed with TLS. It's impossible to expose an endpoint without TLS.

### Resources

A `resource` in a sandbox represents a collection of resources outside of the sandbox system but managed by the lifecycle of the sandbox. It uses the scripts provided by the user to create, suspend, resume and delete the actual resources which are opaque to the sandbox system.

A `resource` has 4 lifecycle event hooks, all optional:

* `on_create`: the hook is executed during sandbox creation;
* `on_delete`: the hook is executed before a sandbox is deleted;
* `on_suspend`: the hook is executed before a sandbox is suspended;
* `on_resume`: the hook is executed right after the sandbox is resumed.

Each hook will use a workspace to execute the script. As a common practice, the workspace checks out the repository containing the scripts and providing the environment for execution.

It can be defined as a list of `resources`, for example

```yaml
workspaces:
- name: dev
  checkouts:
  - path: src
    ...
resources:
- name: aws
  brief: Dev Resources on AWS
  details: |
    Created [resource]({{state.resource_link}})
  handlers:
    on_create:
      save_state: true
      max_retries: 3
      timeout: 600s
      use_workspace: dev
        name: dev
        require_build: true
        run:
          dir: src
          cmd: ./scripts/provision.sh
        artifacts:
        - terraform
    on_suspend:
      use_workspace: dev
        name: dev
        run:
          dir: src
          cmd: ./scripts/suspend.sh
    on_resume:
      save_state: true
      use_workspace: dev
        name: dev
        run:
          dir: src
          cmd: ./scripts/resume.sh
        artifacts:
        - terraform:tf/terrform.tfstate
    on_delete:
      use_workspace: dev
        name: dev
        run:
          dir: src
          cmd: ./scripts/unprovision.sh
```

Each resource is defined with a `name`, optional `brief` (a one sentence summary), optional `details` (a markdown template), and a list of `handlers`. Each handler specifies the workspace (via `use_workspace`) and how to run the script in the workspace (using the [Run Schema](https://docs.sandboxes.cloud/docs/repo-manifest#run-schema)). The `dir` property must specify a relative path to the current home directory (not the checkout path).

The `save_state` flag (mostly used in `on_create` and `on_resume`) indicates the output (STDOUT only) of the script is a JSON and should be persisted as the state of the resource. The values in the JSON can be used to render the markdown defined in `details`, like in the above example, with output of

```json
{"resource_link": "https://svc.awsamazon.com/something/id"}
```

Will be used in `details` to render the final markdown, like:

```markdown
Created [resource](https://svc.awsamazon.com/something/id)
```

With `save_state: true`, the output can also be accessed from the workspace file system, located at `/run/sandbox/fs/resources/NAME/state`. In the above example, `NAME` is `aws`.

Note: the most recently executed script will overwrite the state if the corresponding `save_state` is `true`. In the above example, the output of `on_resume` script will overwrite that generated by `on_create`.

Property `max_retries` specifies the maximum attempts of retries if the script fails. Specifically for `on_suspend` and `on_delete`, failure of the script will prevent the sandbox being suspended or deleted, so the user is able to get into a workspace and debug. A sandbox can be manually, forcibly deleted by ignoring the `on_delete` hook of resources.

Property `timeout` specifies the total time allowed for the script, including all retries.

While using a workspace, the script is executed after checkout completes (including the post-checkout hook defined in the [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest). With `require_build: true`, the script will be executed after a successful build instead of checkout completion.

The list of `artifacts` provides hints about additional information generated by the script. For example, the value `terraform` indicates the script involved Terraform and generated `terraform.tfstate` in the same directory, so the sandbox system will attempt to visualize the Terraform states in the WebConsole. Alternatively `terraform:dir/file` specifies an alternative path related to the working directory for the Terraform state file.

#### Terraform Support

If Terraform is used as the only tool for provisioning the resources, a simpler format can be used:

```yaml
env:
- AWS_REGION=us-west1
workspaces:
- name: dev
  checkouts:
  - path: src
  ...
resources:
- name: aws
  brief: Dev Resources on AWS
  details: |
    EC2 instance id: {{state.instance_id}}
  terraform:
    save_state: true
    workspace: dev
    # Same as above.
    require_build: false
    # The directory (relative to home dir) containing the main terraform module.
    dir: deploy/tf
    run:
      max_retries: 3
      timeout: 600s
      # command is optional, only used if the executable is not "terraform".
      command: tf
      # additional command line arguments.
      args:
      - 'arg passed to terraform directly, can use ${ENV_VAR}'
      # additional env variables.
      env:
      - CURRENT_REGION='${AWS_REGION}'
      vars:
        instance_type: 't2.micro'
        region: '${AWS_REGION}'
    # If specified, the value of the output will be used as the output of this
    # lifecycle hook. Otherwise, the full terraform output in JSON is used:
    #   terraform output -json
    output: instance
```

The system knows how to run `terraform`. With the above example, the system will run `terraform apply` for `on_create` hook and `terraform destroy` for `on_delete` hook, and uses the full terraform output in JSON (unless `output` is specified) as the state. The hooks for `on_suspend` and `on_resume` are undefined by default. To explicitly enable `on_suspend` and `on_resume` hooks, add `on_suspend` explicitly and it will also enable `on_resume` to use exactly the same config as `on_create`:

```yaml
workspaces:
- name: dev
  checkouts:
  - path: src
  ...
resources:
- name: aws
  brief: Dev Resources on AWS
  terraform:
    workspace: dev
    dir: deploy/tf
    run:
      timeout: 600s
      vars:
        instance_type: 't2.micro'
    on_suspend:
      vars:
        instance_count: '0'
```

The above example will run `terraform apply` with special variable `instance_count=0` during sandbox suspension, and `terraform apply` same as `on_create`.

By default, `on_delete` uses the same configuration as `on_create`, but runs `terraform destroy`. If special configuration is needed for `terraform destroy`, define `on_delete` explicitly:

```yaml
workspaces:
- name: dev
  checkouts:
  - path: src
  ...
resources:
- name: aws
  brief: Dev Resources on AWS
  terraform:
    workspace: dev
    dir: deploy/tf
    run:
      timeout: 600s
      vars:
        instance_type: 't2.micro'
    on_delete:
      vars:
        delete_var: special
```

More examples can be found in this [repository](https://github.com/crafting-demo/solutions).

### Customizations

The `customizations` section in the definition provides additional information for special features and extensibility.

#### UI Widget for Env

Sandbox-level environment variables can be customized to show additional UI widgets on the sandbox creation page in the WebConsole, so a user can simply select from a set of predefined values for a specific environment variable without carefully typing in which is error-prune.

```yaml
env:
- INSTANCE_TYPE=t2.micro
- APP_NAME=
...
customizations:
- env:
    name: INSTANCE_TYPE
    display_name: EC2 Instance Type
    description: The instance type for the additional EC2 VM
    choice:
      default: t2.micro
      options:
      - t2.micro
      - t3.medium
      - t3.large
- env:
    name: APP_NAME
    display_name: The name of the app
    validators:
    - regexp: '^[a-z][a-z0-9-]*[a-z0-9]$'
```

Property `name` must match the environment variable defined in `env`.

Property `display_name` must be specified in order to show the widget in the WebConsole.

##### Edit Box

Without additional config, an edit box is shown on the sandbox creation page for the environment  variable. Additional `validators` can be specified for the value entered by the user.

##### Selection

With `choice`, a dropdown selector is shown on the sandbox creation page. The default value is the first item in the `options` list unless explicitly specified.

##### Editable Selection

With `choice` and `editable: true`, for example:

```yaml
env:
- APP_TYPE=simple
...
customizations:
- env:
    name: APP_TYPE
    display_name: App type
    description: The type of the app, or enter your own
    choice:
      editable: true
      options:
      - simple
      - multiple
      - extra
    validators:
    - regexp: '^[a-z][a-z0-9-]*[a-z0-9]$'
```

It shows an editable dropdown.

#### Sandbox Flavor

A sandbox flavor is a named preset which defines the information used to create a new sandbox. With sandbox flavors defined in `customizations` section, the user can simply select one during sandbox creation instead of specifying every detail. Here's an example:

```yaml
customizations:
- flavor:
    name: Standard # The flavor name
    default: true  # If true, this flavor is selected by default on sandbox creation
    env:
    - FOO=BAR      # Environment variables appended to the sandbox-scope env list
    - FOO1=${FOO}1 # Expansion is supported
    workspaces: # Configure specific workspaces
      dev:           # This must be the name of the workspace
        auto: true   # Put the workspace in AUTO mode
        env:
        - KEY=VALUE  # Append to the workspace-scope env list
        checkouts:   # Override specified checkouts in the workspace
        - path: src  # This is used to match the defined checkout in the Template
          version_spec: develop # Override the version_spec to use develop branch
    excludes:   # Exclude the specified workloads during sandbox creation 
    - testloader
    - test-db
    
```

A flavor is able to define configurations (all optional) covering:

* Sandbox scoped environment variables
* Workspace scoped environment variables
* Put workspace in AUTO mode
* Checkout version spec
* Exclude workloads from the sandbox

##### Environment Variables

The top-level `env` specifies the sandbox-scoped environment variables. They are appended to the `env` list defined in the Template. The `env` under `workspaces` appends environment variables to the list of the workspace. Regarding how the final environment variables are generated, please read [environment variables](https://docs.sandboxes.cloud/docs/environment-variables).

##### Workspace Mode

Add `auto: true` to a workspace will put the workspace into *AUTO* mode during sandbox creation. Regarding the mode, please read [auto follow](https://docs.sandboxes.cloud/docs/auto-follow) for more information.

##### Checkout Version Spec

First define `path: PATH` to match the checkout defined in the workspace from the Template, and then use `version_spec` to specify a new [version spec](#checkouts).

##### Exclude Workloads

When a Template defines many workloads, sometimes a sandbox is created for specific tasks which only need a subset of the workloads. In this case, flavor is the most convenient way to define a sub-graph of workloads to be activated in the sandbox. List the names of workloads here to exclude those. The name can be any of the workspaces, dependencies, containers or resources. Note: sandbox creation may fail if the exclusion list breaks the dependency graph (introduced by `wait_for` property of workloads, or `use_workspace` in [resources](#resources).
