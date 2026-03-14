# Source: https://skaffold.dev/docs/custom-actions/

Title: Custom Actions

URL Source: https://skaffold.dev/docs/custom-actions/

Markdown Content:
With Skaffold you can define generic actions in a declarative way using a Skaffold config file (`skaffold.yaml`), and execute them with the `skaffold exec <action-name>` command.

A generic action (a.k.a. Custom Action), defines a list of containers that will be executed in parallel when the action is invoked. A Custom Action execution is considered successful if all its containers end without errors, and considered as failed if one or more of its containers report an error.

Defining Custom Actions
-----------------------

A Skaffold config file can define one or more Custom Actions using the [`customActions` stanza](https://skaffold.dev/docs/references/yaml/#customActions). Each action and container must be identified by an unique name across modules/configurations. **NOTE:** Two different [profiles](https://skaffold.dev/docs/environment/profiles/) can have an action each, with the same name.

Therefore, a configuration for a Custom Action named `update-infra`, with two containers, `update-db-schema` and `setup-external-proxy`, will be defined like this in a `skaffold.yaml` file:

```
apiVersion: skaffold/v4beta5
kind: Config

customActions:
  - name: update-infra
    containers:
      - name: update-db-schema
        image: gcr.io/my-registry/db-updater:latest
      - name: setup-external-proxy
        image: gcr.io/my-registry/proxy:latest
```

Running `skaffold exec update-infra` with the previous configuration will trigger the execution of the `update-infra` action, as a [local (Docker) action](https://skaffold.dev/docs/custom-actions/#local-docker), creating and running a container for `update-db-schema` (using the `gcr.io/my-registry/db-updater:latest` image), and `setup-external-proxy` (using the `gcr.io/my-registry/proxy:latest` image). The output will look like this:

```
$ skaffold exec update-infra
Starting execution for update-infra
...
[setup-external-proxy] updating proxy version...
[setup-external-proxy] copying proxy rules...   
[setup-external-proxy] starting proxy...
[update-db-schema] starting db update...
[update-db-schema] db schema update completed
[setup-external-proxy] proxy configured
```

To check the list of available options to configure an action please refer to the [`customActions` stanza documentation](https://skaffold.dev/docs/references/yaml/#customActions).

Executing Custom Actions
------------------------

The `skaffold exec <action-name>` command executes a defined Custom Action. During execution, Skaffold streams the logs from the containers associated with the action. Upon completion, Skaffold returns an exit code: `0` for success or `1` for failure. To see the available options for the `skaffold exec` command, refer to the [CLI documentation](https://skaffold.dev/docs/references/cli/#skaffold-exec).

### Timeouts

Per default, a Custom Action does not have a timeout configured, which means, the action will run until it completes (success or fail). Using the[`customActions[].timeout`](https://skaffold.dev/docs/references/yaml/#customActions-timeout) property you can change the previous behaviour, adding a desired timeout in seconds:

```
apiVersion: skaffold/v4beta5
kind: Config

customActions:
  - name: update-infra
    timeout: 10 # <- 10 seconds timeout.
    containers:
      - name: update-db-schema
        image: gcr.io/my-registry/db-updater:latest
      - name: setup-external-proxy
        image: gcr.io/my-registry/proxy:latest
```

Running `skaffold exec update-infra` with the previous configuration will fail if the Custom Action takes more than 10 seconds to complete. If the timeout is triggered, Skaffold will stop any running container and will return a status code `1`:

```
$ skaffold exec update-infra
tarting execution for update-infra
...
[setup-external-proxy] updating proxy version...
[setup-external-proxy] copying proxy rules...
[setup-external-proxy] starting proxy...
[update-db-schema] starting db update...
context deadline exceeded
```

Skaffold will return status code `0` if all the containers associated with the given action finish their execution before the 10 seconds timeout.

### Fail strategy

A Custom Action will be run with a `fail-fast` strategy, which means, if one container associated with the action fails, Skaffold will stop any running container, and will return a status code `1`:

The following `skaffold.yaml` config:

```
apiVersion: skaffold/v4beta5
kind: Config

customActions:
  - name: update-infra
    containers:
      - name: update-db-schema
        image: gcr.io/my-registry/db-updater:latest
      - name: setup-external-proxy
        image: gcr.io/my-registry/proxy:latest
```

With an error in the `update-db-schema` container, will produce the following output:

```
$ skaffold exec update-infra
Starting execution for update-infra
...
[setup-external-proxy] updating proxy version...
[setup-external-proxy] copying proxy rules...
[setup-external-proxy] starting proxy...
[update-db-schema] starting db update...
"update-db-schema" running container image "gcr.io/my-registry/db-updater:latest" errored during run with status code: 1
```

The previous default behaviour can be change with the [`customActions[].failFast` property](https://skaffold.dev/docs/references/yaml/#customActions-failFast), changing its value to `false`:

```
apiVersion: skaffold/v4beta5
kind: Config

customActions:
  - name: update-infra
    failFast: false # <- Set to false, making it fail-safe.
    containers:
      - name: update-db-schema
        image: gcr.io/my-registry/db-updater:latest
      - name: setup-external-proxy
        image: gcr.io/my-registry/proxy:latest
```

The previous configuration indicates Skaffold to run the `update-infra` action with a `fail-safe` strategy, which means, Skaffold will not interrupt any container if one or more of them fail; all the containers will run until they finish (success or fail):

```
Starting execution for update-infra
...
[setup-external-proxy] updating proxy version...
[setup-external-proxy] copying proxy rules...
[setup-external-proxy] starting proxy...
[update-db-schema] starting db update...
[setup-external-proxy] proxy configured
1 error(s) occurred:
* "update-db-schema" running container image "gcr.io/my-registry/db-updater:latest" errored during run with status code: 1
```

### Execution modes

A Custom Action has an execution mode associated with it that indicates Skaffold in which environment and how the containers of that action should be created and executed. This execution mode can be configured with the [`customActions[].executionMode` property](https://skaffold.dev/docs/references/yaml/#customActions-executionMode). These are the available execution modes for a Custom Action:

#### Local (Docker) - default

This is the default configuration when no [`customActions[].executionMode`](https://skaffold.dev/docs/references/yaml/#customActions-executionMode) is specified. With this execution mode, Skaffold will run every container associated to a given Custom Action with a Docker daemon.

#### Remote (K8s job)

With this execution mode, Skaffold will create a K8s job for each container associated with the given action. For the following configuration:

```
apiVersion: skaffold/v4beta5
kind: Config

customActions:
  - name: update-infra
    executionMode:
      kubernetesCluster: {} # <- Indicates Skaffold to run the action with K8s jobs.
    containers:
      - name: update-db-schema
        image: gcr.io/my-registry/db-updater:latest
      - name: setup-external-proxy
        image: gcr.io/my-registry/proxy:latest
```

Skaffold will create one K8s job for `update-db-schema` and another for `setup-external-proxy`. The jobs will use the following template per default:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: # <- Container name defined in skaffold.yaml.
spec:
  template:
    spec:
      containers: # <- Only one container, the one defined in the skaffold.yaml.
      # ...
      restartPolicy: Never
  backoffLimit: 0
```

The template can be extended using the [`customActions[].executionMode.kubernetesCluster.overrides`](https://skaffold.dev/docs/references/yaml/#customActions-executionMode-kubernetesCluster-overrides) and [`customActions[].executionMode.kubernetesCluster.jobManifestPath`](https://skaffold.dev/docs/references/yaml/#customActions-executionMode-kubernetesCluster-jobManifestPath) properties.

Skaffold build + exec
---------------------

Custom Actions can be used together with [Skaffold build](https://skaffold.dev/docs/builders/) so the Custom Actions can use images build by Skaffold.

Using the following `skaffold.yaml` file:

```
apiVersion: skaffold/v4beta5
kind: Config

build:
  artifacts:
    - image: local-db-updater # <- Image build by Skaffold.
      # ...

customActions:
  - name: update-infra
    containers:
      - name: update-db-schema
        image: local-db-updater # <- Image build by Skaffold.
      - name: setup-external-proxy
        image: gcr.io/my-registry/proxy:latest
```

We trigger an Skaffold build using the `skaffold build` command:

```
$ skaffold build --file-output=build.json
```

Skaffold will create a new `build.json` file with the necessary info. Then, using the generated file, we can run `skaffold exec`:

```
$ skaffold exec update-infra --build-artifacts=build.json
```

That way, Skaffold will be able to run the `local-db-updater` image in the `update-infra` Custom Action.
