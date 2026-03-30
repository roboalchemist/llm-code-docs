# Source: https://skaffold.dev/docs/custom-actions/

Title: Custom Actions

URL Source: https://skaffold.dev/docs/custom-actions/

Published Time: Thu, 13 Nov 2025 20:49:27 GMT

Markdown Content:
Custom Actions | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/custom-actions/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

*   [Documentation](https://skaffold.dev/docs/ "Skaffold 2.0 Documentation")
    *   - [x] [Installing Skaffold](https://skaffold.dev/docs/install/) 
    *   - [x] [Upgrading from Skaffold v1 to Skaffold v2 [NEW]](https://skaffold.dev/docs/upgrading/) 
    *   - [x] [Quickstart](https://skaffold.dev/docs/quickstart/) 
    *   - [x] [Guides](https://skaffold.dev/docs/workflows/) 
        *   - [x] [Getting Started With Your Project](https://skaffold.dev/docs/workflows/getting-started-with-your-project/) 
        *   - [x] [Continuous Development](https://skaffold.dev/docs/workflows/dev/ "skaffold dev") 
        *   - [x] [Debugging](https://skaffold.dev/docs/workflows/debug/ "Debugging With Skaffold") 
        *   - [x] [Continuous Delivery](https://skaffold.dev/docs/workflows/ci-cd/) 
        *   - [x] [Managing ARM workloads [NEW]](https://skaffold.dev/docs/workflows/handling-platforms/) 

    *   - [x] [Skaffold Pipeline Stages](https://skaffold.dev/docs/pipeline-stages/) 
    *   - [x] [Init](https://skaffold.dev/docs/init/) 
    *   - [x] [Build](https://skaffold.dev/docs/builders/) 
        *   - [x] [Builder types](https://skaffold.dev/docs/builders/builder-types/) 
            *   - [x] [Docker](https://skaffold.dev/docs/builders/builder-types/docker/ "Docker Build") 
            *   - [x] [Jib](https://skaffold.dev/docs/builders/builder-types/jib/ "Jib Build") 
            *   - [x] [Bazel](https://skaffold.dev/docs/builders/builder-types/bazel/) 
            *   - [x] [Custom](https://skaffold.dev/docs/builders/builder-types/custom/ "Custom Build Script") 
            *   - [x] [Buildpacks](https://skaffold.dev/docs/builders/builder-types/buildpacks/ "Cloud Native Buildpacks") 
            *   - [x] [ko](https://skaffold.dev/docs/builders/builder-types/ko/) 

        *   - [x] [Environments](https://skaffold.dev/docs/builders/build-environments/ "Build environments") 
            *   - [x] [Local build](https://skaffold.dev/docs/builders/build-environments/local/) 
            *   - [x] [In cluster](https://skaffold.dev/docs/builders/build-environments/in-cluster/ "In cluster build") 
            *   - [x] [Google Cloud Build](https://skaffold.dev/docs/builders/build-environments/cloud-build/) 

        *   - [x] [Cross/multi-platform](https://skaffold.dev/docs/builders/cross-platform/ "Cross-platform and multi-platform build support") 

    *   - [x] [Deploy [UPDATED]](https://skaffold.dev/docs/deployers/) 
        *   - [x] [Kubectl](https://skaffold.dev/docs/deployers/kubectl/) 
        *   - [x] [Kpt [UPDATED]](https://skaffold.dev/docs/deployers/kpt/) 
        *   - [x] [Helm [UPDATED]](https://skaffold.dev/docs/deployers/helm/) 
        *   - [x] [Docker](https://skaffold.dev/docs/deployers/docker/) 
        *   - [x] [Google Cloud Run [NEW]](https://skaffold.dev/docs/deployers/cloudrun/) 

    *   - [x] [Render [NEW]](https://skaffold.dev/docs/renderers/) 
        *   - [x] [Raw YAML](https://skaffold.dev/docs/renderers/rawyaml/) 
        *   - [x] [Kpt [NEW]](https://skaffold.dev/docs/renderers/kpt/) 
        *   - [x] [Kustomize](https://skaffold.dev/docs/renderers/kustomize/) 
        *   - [x] [Helm [UPDATED]](https://skaffold.dev/docs/renderers/helm/) 

    *   - [x] [Test](https://skaffold.dev/docs/testers/) 
        *   - [x] [Container Structure Test](https://skaffold.dev/docs/testers/structure/) 
        *   - [x] [Custom Test](https://skaffold.dev/docs/testers/custom/) 

    *   - [x] [Tag](https://skaffold.dev/docs/taggers/) 
    *   - [x] [File Sync](https://skaffold.dev/docs/filesync/) 
    *   - [x] [Log Tailing](https://skaffold.dev/docs/log-tailing/) 
    *   - [x] [Verify [NEW]](https://skaffold.dev/docs/verify/) 
    *   - [x] [Deploy Status Checking](https://skaffold.dev/docs/status-check/) 
    *   - [x] [Lifecycle Hooks](https://skaffold.dev/docs/lifecycle-hooks/) 
    *   - [x] [Port Forwarding](https://skaffold.dev/docs/port-forwarding/) 
    *   - [x] [Cleanup](https://skaffold.dev/docs/cleanup/) 
    *   - [x] [Custom Actions](https://skaffold.dev/docs/custom-actions/) 
    *   - [x] [Architecture and Design](https://skaffold.dev/docs/design/) 
        *   - [x] [Skaffold Pipeline](https://skaffold.dev/docs/design/config/) 
        *   - [x] [Global Configuration](https://skaffold.dev/docs/design/global-config/) 
        *   - [x] [Skaffold API](https://skaffold.dev/docs/design/api/) 

    *   - [x] [Environment Management](https://skaffold.dev/docs/environment/) 
        *   - [x] [Load ENV from a file](https://skaffold.dev/docs/environment/env-file/ "Load environment variables from a file") 
        *   - [x] [Local Cluster](https://skaffold.dev/docs/environment/local-cluster/) 
        *   - [x] [Image Repository Handling](https://skaffold.dev/docs/environment/image-registries/) 
        *   - [x] [Profiles](https://skaffold.dev/docs/environment/profiles/) 
        *   - [x] [Kube-context Activation](https://skaffold.dev/docs/environment/kube-context/) 
        *   - [x] [Templated Fields](https://skaffold.dev/docs/environment/templating/) 

    *   - [x] [Tutorials](https://skaffold.dev/docs/tutorials/) 
        *   - [x] [Build and deploy on Kubernetes](https://skaffold.dev/docs/tutorials/build-and-deploy-to-kubernetes/ "Use Skaffold to build and deploy an application on Kubernetes") 
        *   - [x] [Manage CRDs w/ Skaffold - Configuring Which K8s Resources & Fields Skaffold Manages](https://skaffold.dev/docs/tutorials/skaffold-resource-selector/) 
        *   - [x] [Build Dependencies](https://skaffold.dev/docs/tutorials/artifact-dependencies/ "Defining dependencies between artifacts") 
        *   - [x] [Config Dependencies](https://skaffold.dev/docs/tutorials/config-dependencies/ "Importing configuration as dependencies") 
        *   - [x] [Custom Build Script](https://skaffold.dev/docs/tutorials/custom-builder/ "Building Artifacts with a Custom Build Script") 
        *   - [x] [Developer Journey](https://skaffold.dev/docs/tutorials/developer-journey/ "Developer Journey with Buildpacks") 
        *   - [x] [Go integration test coverage profiles](https://skaffold.dev/docs/tutorials/go-integration-coverage/) 
        *   - [x] [Overriding the buildpacks run image](https://skaffold.dev/docs/tutorials/buildpacks-override/ "Override the run image in buildpacks builder") 
        *   - [x] [Skaffold in CI/CD](https://skaffold.dev/docs/tutorials/ci_cd/ "Using Skaffold for CI/CD with GitLab") 

    *   - [x] [References](https://skaffold.dev/docs/references/) 
        *   - [x] [CLI](https://skaffold.dev/docs/references/cli/) 
        *   - [x] [skaffold.yaml](https://skaffold.dev/docs/references/yaml/) 
        *   - [x] [API](https://skaffold.dev/docs/references/api/) 
            *   - [x] [gRPC API](https://skaffold.dev/docs/references/api/grpc/) 
            *   - [x] [HTTP API](https://skaffold.dev/docs/references/api/swagger/) 

        *   - [x] [API V2](https://skaffold.dev/docs/references/api-v2/) 
            *   - [x] [gRPC API](https://skaffold.dev/docs/references/api-v2/grpc/) 
            *   - [x] [HTTP API](https://skaffold.dev/docs/references/api-v2/swagger/) 

        *   - [x] [Privacy Settings](https://skaffold.dev/docs/references/privacy/) 
        *   - [x] [Deprecation Policy](https://skaffold.dev/docs/references/deprecation/) 

    *   - [x] [Resources](https://skaffold.dev/docs/resources/) 
        *   - [x] [Skaffold Feedback](https://skaffold.dev/docs/resources/feedback/) 
        *   - [x] [Telemetry](https://skaffold.dev/docs/resources/telemetry/) 

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/custom-actions.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Custom%20Actions)

**Applicable**
**Not applicable**[`dev`](https://skaffold.dev/docs/references/cli#skaffold-dev)[`debug`](https://skaffold.dev/docs/references/cli#skaffold-debug)[`run`](https://skaffold.dev/docs/references/cli#skaffold-run)[`build`](https://skaffold.dev/docs/references/cli#skaffold-build)[`test`](https://skaffold.dev/docs/references/cli#skaffold-test)[`deploy`](https://skaffold.dev/docs/references/cli#skaffold-deploy)[`render`](https://skaffold.dev/docs/references/cli#skaffold-render)

*   [Defining Custom Actions](https://skaffold.dev/docs/custom-actions/#defining-custom-actions)
*   [Executing Custom Actions](https://skaffold.dev/docs/custom-actions/#executing-custom-actions)
    *   [Timeouts](https://skaffold.dev/docs/custom-actions/#timeouts)
    *   [Fail strategy](https://skaffold.dev/docs/custom-actions/#fail-strategy)
    *   [Execution modes](https://skaffold.dev/docs/custom-actions/#execution-modes)

*   [Skaffold build + exec](https://skaffold.dev/docs/custom-actions/#skaffold-build--exec)

1.   [Documentation](https://skaffold.dev/docs/)
2.   Custom Actions

Custom Actions
==============

With Skaffold you can define generic actions in a declarative way using a Skaffold config file (`skaffold.yaml`), and execute them with the `skaffold exec <action-name>` command.

A generic action (a.k.a. Custom Action), defines a list of containers that will be executed in parallel when the action is invoked. A Custom Action execution is considered successful if all its containers end without errors, and considered as failed if one or more of its containers report an error.

#### Note

 Custom Actions are meant to run **specific, completable tasks**; are not meant to be use to execute your main application. 

Defining Custom Actions
-----------------------

A Skaffold config file can define one or more Custom Actions using the [`customActions` stanza](https://skaffold.dev/docs/references/yaml/#customActions). Each action and container must be identified by an unique name across modules/configurations. **NOTE:** Two different [profiles](https://skaffold.dev/docs/environment/profiles/) can have an action each, with the same name.

Therefore, a configuration for a Custom Action named `update-infra`, with two containers, `update-db-schema` and `setup-external-proxy`, will be defined like this in a `skaffold.yaml` file:

```yaml
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

```console
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

```yaml
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

```console
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

```yaml
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

```console
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

```yaml
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

```console
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

```yaml
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

```yaml
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

```yaml
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

```console
$ skaffold build --file-output=build.json
```

Skaffold will create a new `build.json` file with the necessary info. Then, using the generated file, we can run `skaffold exec`:

```console
$ skaffold exec update-infra --build-artifacts=build.json
```

That way, Skaffold will be able to run the `local-db-updater` image in the `update-infra` Custom Action.

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
