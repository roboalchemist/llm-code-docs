# Source: https://skaffold.dev/docs/lifecycle-hooks/

Title: Lifecycle Hooks

URL Source: https://skaffold.dev/docs/lifecycle-hooks/

Published Time: Thu, 13 Nov 2025 20:49:27 GMT

Markdown Content:
Lifecycle Hooks | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/lifecycle-hooks/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

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

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/lifecycle-hooks.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Lifecycle%20Hooks)

**Maturity**[`beta`](https://skaffold.dev/docs/references/deprecation)
**Applicable**[`dev`](https://skaffold.dev/docs/references/cli#skaffold-dev)[`debug`](https://skaffold.dev/docs/references/cli#skaffold-debug)[`run`](https://skaffold.dev/docs/references/cli#skaffold-run)[`build`](https://skaffold.dev/docs/references/cli#skaffold-build)[`deploy`](https://skaffold.dev/docs/references/cli#skaffold-deploy)
**Not applicable**[`test`](https://skaffold.dev/docs/references/cli#skaffold-test)[`render`](https://skaffold.dev/docs/references/cli#skaffold-render)
**Code Samples**[`hooks`](https://github.com/GoogleContainerTools/skaffold/tree/main/examples/lifecycle-hooks)

*   [Overview](https://skaffold.dev/docs/lifecycle-hooks/#overview)
*   [Host hooks](https://skaffold.dev/docs/lifecycle-hooks/#host-hooks)
    *   [`before-build` and `after-build`](https://skaffold.dev/docs/lifecycle-hooks/#before-build-and-after-build)
    *   [`before-sync` and `after-sync`](https://skaffold.dev/docs/lifecycle-hooks/#before-sync-and-after-sync)
    *   [`before-deploy` and `after-deploy`](https://skaffold.dev/docs/lifecycle-hooks/#before-deploy-and-after-deploy)
    *   [Environment variables](https://skaffold.dev/docs/lifecycle-hooks/#environment-variables)

*   [Container hooks](https://skaffold.dev/docs/lifecycle-hooks/#container-hooks)
    *   [`before-sync` and `after-sync`](https://skaffold.dev/docs/lifecycle-hooks/#before-sync-and-after-sync-1)
    *   [`before-deploy` and `after-deploy`](https://skaffold.dev/docs/lifecycle-hooks/#before-deploy-and-after-deploy-1)

1.   [Documentation](https://skaffold.dev/docs/)
2.   Lifecycle Hooks

Lifecycle Hooks beta
====================

This page describes how to use the lifecycle hook framework to run code triggered by different events during the skaffold process lifecycle.

Overview
--------

We identify three distinct phases in skaffold - `build`, `sync` and `deploy`. Skaffold can trigger a hook `before` or `after` executing each phase. There are two types of `hooks` that can be defined - `host` hooks and `container` hooks.

Host hooks
----------

Host hooks are executed on the runner and can be defined for the following phases:

### `before-build` and `after-build`

Build hooks are executed before and after each artifact is built. If an artifact is not built, such as happens when the image was found in the Skaffold image cache, then the build hooks will not be executed. To force the build hooks, run Skaffold with `--cache-artifacts=false` option.

Example: _skaffold.yaml_ snippet

```yaml
build:
  artifacts:
  - image: hooks-example
    hooks:
      before:
        - command: ["sh", "-c", "./hook.sh"]
          os: [darwin, linux]
        - command: ["cmd.exe", "/C", "hook.bat"]
          os: [windows]
      after:
        - command: ["sh", "-c", "./hook.sh"]
          os: [darwin, linux]
        - command: ["cmd.exe", "/C", "hook.bat"]
          os: [windows]
```

This config snippet defines that `hook.sh` (for `darwin` or `linux` OS) or `hook.bat` (for `windows` OS) will be executed `before` and `after` each build for artifact `hooks-example`.

### `before-sync` and `after-sync`

Example: _skaffold.yaml_ snippet

```yaml
build:
  artifacts:
  - image: hooks-example
    sync: 
      auto: {}
      hooks:
        before:
          - host:
              command: ["sh", "-c", "./hook.sh"]
              os: [darwin, linux]
          - host:
              command: ["cmd.exe", "/C", "hook.bat"]
              os: [windows]
        after:
          - host:
              command: ["sh", "-c", "./hook.sh"]
              os: [darwin, linux]
          - host:
              command: ["cmd.exe", "/C", "hook.bat"]
              os: [windows]
```

This config snippet defines that `hook.sh` (for `darwin` or `linux` OS) or `hook.bat` (for `windows` OS) will be executed `before` and `after` each file sync operation for artifact `hooks-example`.

### `before-deploy` and `after-deploy`

Example: _skaffold.yaml_ snippet

```yaml
deploy:
  kubectl:
    manifests:
      - deployment.yaml
    hooks:
      before:
        - host:
            command: ["sh", "-c", "echo pre-deploy host hook running on $(hostname)!"]
            os: [darwin, linux]
      after:
        - host:
            command: ["sh", "-c", "echo post-deploy host hook running on $(hostname)!"]
```

This config snippet defines a simple `echo` command to run before and after each `kubectl` deploy.

### Environment variables

The following environment variables will be available for the corresponding phase host hooks, that can be resolved in both inline commands or scripts.

| Environment variable | Description | Availability |
| --- | --- | --- |
| $SKAFFOLD_IMAGE | The fully qualified image name. For example, “gcr.io/image1:tag” | Build, Sync |
| $SKAFFOLD_PUSH_IMAGE | Set to true if the image in $IMAGE is expected to exist in a remote registry. Set to false if the image is expected to exist locally. | Build |
| $SKAFFOLD_IMAGE_REPO | The image repo. For example, “gcr.io/image1” | Build |
| $SKAFFOLD_IMAGE_TAG | The image tag. For example, “tag” | Build |
| $SKAFFOLD_BUILD_CONTEXT | An absolute path to the directory this artifact is meant to be built from. Specified by artifact context in the skaffold.yaml. | Build |
| $SKAFFOLD_FILES_ADDED_OR_MODIFIED | Semi-colon delimited list of absolute path to all files synced or to be synced in current dev loop that have been added or modified | Sync |
| $SKAFFOLD_FILES_DELETED | Semi-colon delimited list of absolute path to all files synced or to be synced in current dev loop that have been deleted | Sync |
| $SKAFFOLD_RUN_ID | Run specific UUID label for deployed or to be deployed resources | Deploy |
| $SKAFFOLD_DEFAULT_REPO | The resolved default repository | All |
| $SKAFFOLD_RPC_PORT | TCP port to expose event API | All |
| $SKAFFOLD_HTTP_PORT | TCP port to expose event REST API over HTTP | All |
| $SKAFFOLD_KUBE_CONTEXT | The resolved Kubernetes context | Sync, Deploy |
| $SKAFFOLD_MULTI_LEVEL_REPO | The multi-level support of the repository | All |
| $SKAFFOLD_NAMESPACES | Comma separated list of Kubernetes namespaces | Sync, Deploy |
| $SKAFFOLD_WORK_DIR | The workspace root directory | All |
| Local environment variables | The current state of the local environment (e.g. $HOST, $PATH). Determined by the golang os.Environ function. | All |

Container hooks
---------------

Container hooks are executed on a target container and can be defined on the following phases:

### `before-sync` and `after-sync`

Example: _skaffold.yaml_ snippet

```yaml
build:
  artifacts:
  - image: hooks-example
    sync: 
      auto: {}
      hooks:
        before:
          - container:
              command: ["sh", "-c", "echo before sync hook"]
        after:
          - container:
              command: ["sh", "-c", "echo after sync hook"]
```

This config snippet defines a command to run inside the container corresponding to the artifact `hooks-example` image, `before` and `after` each file sync operation.

### `before-deploy` and `after-deploy`

Example: _skaffold.yaml_ snippet

```yaml
deploy:
  kubectl:
    manifests:
      - deployment.yaml
    hooks:
      before:
        - container:
            # this will only run when there's a matching container from a previous deploy iteration like in `skaffold dev` 
            command: ["sh", "-c", "echo pre-deploy container hook running on $(hostname)!"]
            containerName: hooks-example*
            podName: hooks-example-deployment*
      after:
        - container:
            command: ["sh", "-c", "echo post-deploy container hook running on $(hostname)!"]
            containerName: hooks-example* # use a glob pattern to prefix-match the container name and pod name for deployments, stateful-sets, etc.
            podName: hooks-example-deployment*
```

This config snippet defines a simple `echo` command to run inside the containers that match `podName` and `containerName`, before and after each `kubectl` deploy. The `after` container commands are only run after the [deployment status checks](https://skaffold.dev/docs/status-check/) on the deployment are complete. Also, unlike the `sync` container hooks, skaffold cannot determine the target container from just the config definition, and needs the `podName` and `containerName`.

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
