# Source: https://docs.sandboxes.cloud/docs/containers-dependencies-setup.md

# Setup containers and dependencies

This page talks about how to setup built-in dependencies such as `Postgres`, `Redis`, `ElasticSearch`, etc., and custom containers to support your services running in `workspaces`, specifically:

* [Configure a dependency](#configure-a-dependency)
* [Configure a container](#configure-a-container)
  * [Container setup options](#container-setup-options)
  * [Volumes & data snapshots](#volumes--data-snapshots)
  * [Volume sharing](#volume-sharing)
  * [Debug a container](#debug-a-container)
  * [Build your own image](#build-your-own-image)

To add a dependency or container, from the editing view of a [Standalone sandbox](https://docs.sandboxes.cloud/docs/standalone-sandbox), we can click `Add Component` from the editing view, as highlighted below, and select `Dependencies` or `Containers` in the dialog, respectively.

<Image align="center" className="border" border={true} src="https://files.readme.io/581ee14-image.png" />

### Configure a dependency

To configure the newly added dependency, we can click into its detailed view.

<Image align="center" className="border" border={true} src="https://files.readme.io/145f4de-image.png" />

As shown above, we can edit the following info:

* **Name of the dependency** (will be used as hostname)
* **Type and version of the dependency** Commonly used services and versions are supported here, for a detailed list of what's supported, please see [https://sandboxes.cloud/dependencies](https://sandboxes.cloud/dependencies)
* **Property values** Many containers support a list of properties that users can customize to the values they want. For example, for `postgres`, you can customize a pre-registered user with `username` and `password`, and a pre-created database with `database`
* **Default snapshot**  We can optionally specify a snapshot of state we want to apply to this dependency in all newly created sandboxes. See [Save and load data snapshots](https://docs.sandboxes.cloud/docs/data-snapshots) for how to create such a snapshot.

### Configure a container

Sometimes in addition to the commonly used built-in dependencies, we need more custom containers to run alongside our services in the same sandbox. Crafting system supports running a workload directly using a container image from a public container registry, (or private registries for Crafting Self-hosted), in order to provide more flexibility to developers in case the current dependency services are not sufficient, such as:

* Need a supporting service that Crafting doesn't have as a built-in dependency.
* Need a specific version of a supporting service that Crafting doesn't have in the built-in list
* Need to add certain customization, e.g. a special config file in the supporting service.

In addition, introducing additional containers is a great way to add dev tools that make the dev environment more convenient, e.g. adding SQL Pad as UI for querying database in sandbox.

Next, we will use SQL Pad as an example to walk about how to config containers

#### Container setup options

The dependency `mysql` helps running my service, it will be great if there's a simple UI to access the database. We can use the [sqlpad container](https://hub.docker.com/r/sqlpad/sqlpad/) to provide an experience that it's ready to use when a new sandbox is created.

<Image align="center" className="border" border={true} src="https://files.readme.io/e54f7ac-image.png" />

As shown above, we can edit many options for the container we want to add, from image of the container to ports, ENVs, and overrides for entrypoints, arguments, working directory, etc. The schema follows most of the docker container image configuration. Properties `entrypoint`, `args`, `cwd` corresponds to [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint), [CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [WORKDIR](https://docs.docker.com/engine/reference/builder/#workdir) in a Dockerfile. For the full definition, please checkout [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition#containers).

Note that it's important to declare the exposed ports in the containers. It's NOT inferred from the container image.

The example YAML for the SQL pad config is shown below

```yaml
# My workspaces
workspaces:
- name: myapp
  checkouts:
  - path: src
    repo: git@github.com:examples/myapp
  ports:
  - name: http
    port: 8000
    protocol: HTTP/TCP
# myapp needs mysql
dependencies:
- name: mysql
  service_type: mysql
  properties:
    database: myapp
    username: myapp
# Add sqlpad for the team
containers:
- name: sqlpad
  image: sqlpad/sqlpad:latest
  env:
  - SQLPAD_AUTH_DISABLED=true
  - SQLPAD_AUTH_DISABLED_DEFAULT_ROLE=admin
  - SQLPAD_CONNECTIONS__myapp__name=myapp
  - SQLPAD_CONNECTIONS__myapp__driver=mysql2
  - SQLPAD_CONNECTIONS__myapp__host=mysql
  - SQLPAD_CONNECTIONS__myapp__database=myapp
  - SQLPAD_CONNECTIONS__myapp__username=myapp
  - SQLPAD_DEFAULT_CONNECTION_ID=myapp
  ports:
  - name: web
    port: 3000
    protocol: HTTP/TCP
# Exposed endpoints
endpoints:
- name: app
  http:
    routes:
    - path_prefix: /
      backend:
        target: myapp
        port: http
- name: sqlpad
  http:
    routes:
    - path_prefix: /
      backend:
        target: sqlpad
        port: web
```

With the above Sandbox Definition, the *sqlpad* can be accessed using a URL like [https://sqlpad--sandbox-myorg.sandboxes.cloud](https://sqlpad--sandbox-myorg.sandboxes.cloud). By default, it's authenticated.

#### Volumes & data snapshots

The container in Crafting handles volumes differently from a container run in docker or Kubernetes. In a sandbox, the filesystem of a container workload is always persisted. Restarting a container will have all files preserved. Because of this, it's not necessary to explicitly specify volume mounts to persist data folders as usually people do with docker or docker compose. A volume is only needed when it's being shared with multiple containers (read and write), or special content (config, secret etc.) should be mounted into the container.

To add a volume, click the `Add Component` in the editing view (shown above) and choose `volumes`

Like dependencies, we can take data snapshots for containers as well. Note that the snapshot for containers requires a pre-defined volume and only includes the data in that volume. Please make sure the data file for the service running in the container is on the defined volume.

Please refer to [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition#volumes) for the details of types of volumes and how to define them.

#### Volume sharing

Specifically, when a [regular volume](https://docs.sandboxes.cloud/docs/app-definition#regular-volume) is shared by more then one containers, the volume is mounted for reading and writing. This usage may imply a co-location of these container on the same host, and thus the scalability may be impacted.

Here's an example of two [filebrowser container](https://hub.docker.com/r/filebrowser/filebrowser) sharing the same volume:

```yaml
containers:
- name: files1
  image: filebrowser/filebrowser:latest
  ports:
  - name: web
    port: 80
    protocol: HTTP/TCP
  volume_mounts:
  - name: files
    path: /srv
- name: files2
  image: filebrowser/filebrowser:latest
  ports:
  - name: web
    port: 80
    protocol: HTTP/TCP  
  volume_mounts:
  - name: files
    path: /srv
volumes:
- name: files
endpoints:
- name: files1
  http:
    routes:
    - path_prefix: /
      backend:
        target: files1
        port: web
- name: files2
  http:
    routes:
    - path_prefix: /
      backend:
        target: files2
        port: web
```

#### Debug a container

The logs of a container workload can be viewed the same way as a workspace or a dependency. Additionally, the `cs exec` (see [reference](https://docs.sandboxes.cloud/docs/command-line-tool#exec) for details) can be used to run a command inside the container. However, the executable must exist on the filesystem inside the container.

Port-forwarding is supported the same way as a workspace, use `cs port-forward`

#### Build your own image

For your convenience, Crafting system provides a private container registry for each organization using Crafting SaaS. It can be accessed with prefix: `cr.sandboxes.cloud/ORG/`. And a docker wrapper command `cs docker` provided for pushing the image.

Here are the push steps:

* Build your image using a Dockerfile, with `docker build ...` command;
* Tag the image with sandbox private container: `docker tag LOCAL-IMAGE cr.sandboxes.cloud/ORG/NAME:TAG`
* Push the image using `cs docker -- push cr.sandboxes.cloud/ORG/NAME:TAG`

Here's an example, assuming organization is `myorg`:

```shell
docker build -t cr.sandboxes.cloud/myorg/shared/myservice:latest src/myservice/docker
cs docker -- push cr.sandboxes.cloud/myorg/shared/myservice:latest
```

And use that image in a container workload:

```yaml
containers:
- name: myservice
  image: cr.sandboxes.cloud/myorg/shared/myservice:latest
```