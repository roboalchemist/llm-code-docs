# Source: https://skaffold.dev/docs/design/config/

Title: Skaffold Pipeline

URL Source: https://skaffold.dev/docs/design/config/

Published Time: Thu, 13 Nov 2025 20:49:27 GMT

Markdown Content:
Skaffold Pipeline | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/design/config/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

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

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/design/config.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Skaffold%20Pipeline)

*       *   [File resolution](https://skaffold.dev/docs/design/config/#file-resolution)

*   [Multiple configuration support](https://skaffold.dev/docs/design/config/#multiple-configuration-support)
*   [Configuration dependencies](https://skaffold.dev/docs/design/config/#configuration-dependencies)
    *   [Local config dependency](https://skaffold.dev/docs/design/config/#local-config-dependency)
    *   [Remote config dependency](https://skaffold.dev/docs/design/config/#remote-config-dependency)
    *   [Profile Activation in required configs](https://skaffold.dev/docs/design/config/#profile-activation-in-required-configs)

1.   [Documentation](https://skaffold.dev/docs/)
2.   [Architecture and Design](https://skaffold.dev/docs/design/)
3.   Skaffold Pipeline

Skaffold Pipeline
=================

You can configure Skaffold with the Skaffold configuration file, `skaffold.yaml`. A single configuration consists of several different components:

| Component | Description |
| --- | --- |
| `apiVersion` | The Skaffold API version you would like to use. The current API version is skaffold/v4beta13 . |
| `kind` | The Skaffold configuration file has the kind `Config`. |
| `metadata` | Holds additional properties like the `name` of this configuration. |
| `build` | Specifies how Skaffold builds artifacts. You have control over what tool Skaffold can use, how Skaffold tags artifacts and how Skaffold pushes artifacts. Skaffold supports using local Docker daemon, Google Cloud Build, Kaniko, or Bazel to build artifacts. See [Builders](https://skaffold.dev/docs/builders) and [Taggers](https://skaffold.dev/docs/taggers/) for more information. |
| `test` | Specifies how Skaffold tests artifacts. Skaffold supports [container-structure-tests](https://github.com/GoogleContainerTools/container-structure-test) to test built artifacts and custom tests to run custom commands as part of the development pipeline. See [Testers](https://skaffold.dev/docs/testers/) for more information. |
| `deploy` | Specifies how Skaffold deploys artifacts. Skaffold supports using `kubectl`, `helm`, or `kustomize` to deploy artifacts. See [Deployers](https://skaffold.dev/docs/deployers/) for more information. |
| `profiles` | Profile is a set of settings that, when activated, overrides the current configuration. You can use Profile to override the `build`, `test` and `deploy` sections. |
| `requires` | Specifies a list of other skaffold configurations to import into the current config |

You can [learn more](https://skaffold.dev/docs/references/yaml/) about the syntax of `skaffold.yaml`.

Skaffold normally expects to find the configuration file as `skaffold.yaml` in the current directory, but the location can be overridden with the `--filename` flag.

### File resolution

The Skaffold configuration file often references other files and directories. These files and directories are resolved relative to the current directory _and not to the location of the Skaffold configuration file_. There are two important exceptions:

1.   Files referenced from a build artifact definition are resolved relative to the build artifact’s _context_ directory. When omitted, the context directory defaults to the current directory.
2.   For [configurations resolved as dependencies](https://skaffold.dev/docs/design/config/#configuration-dependencies%22), paths are always resolved relative to the directory containing the imported configuration file.

For example, consider a project with the following layout:

```
.
├── frontend
│   └── Dockerfile
├── helm
│   └── project
│       └── dev-values.yaml
└── skaffold.yaml
```

The config file might look like:

```yaml
apiVersion: skaffold/v2beta11
kind: Config
build:
  artifacts:
  - image: app
    context: frontend
    docker:
      dockerfile: "Dockerfile"
deploy:
  helm:
    releases:
    - name: project
      chartPath: helm/project
      valuesFiles:
      - "helm/project/dev-values.yaml"
```

In this example, the `Dockerfile` for building `app` is resolved relative to `app`’s context directory, whereas the the Helm chart’s location and its values-files are relative to the current directory in `helm/project`.

We generally recommend placing the configuration file in the root directory of the Skaffold project.

Multiple configuration support
------------------------------

A single `skaffold.yaml` file can define multiple skaffold configurations in the schema described above using the separator `---`. If these configuration objects define the `metadata.name` property then we consider them as `modules`, that can then be activated by name.

Consider a `skaffold.yaml` defined as:

```yaml
apiVersion: skaffold/vX
kind: Config
metadata:
  name: cfg1
build:
  # build definition
deploy:
  # deploy definition

---

apiVersion: skaffold/vX
kind: Config
metadata:
  name: cfg2
build:
  # build definition
deploy:
  # deploy definition
```

Here `cfg1` and `cfg2` are independent skaffold modules. Running `skaffold dev` for instance will execute actions from both these modules. You could also run `skaffold dev --module cfg1` to only activate the `cfg1` module and skip `cfg2`.

Configuration dependencies
--------------------------

In addition to authoring configurations in a `skaffold.yaml` file, we can also import other existing configurations as dependencies. Skaffold manages all imported and defined configurations in the same session. It also ensures all artifacts in a required config are built prior to those in current config (provided the artifacts have dependencies defined); and all deploys in required configs are applied prior to those in current config.

#### Note:

 Running `skaffold <command> --module <config-name>` will filter to the specified target module, but also include the transitive closure of all other configurations in its dependency graph. For instance, if a module `cfg1` imported another module `cfg2` as a dependency while `cfg2` imported `cfg3` and `cfg4`, then running `skaffold dev --module cfg1` would activate all of `cfg1`, `cfg2`, `cfg3` and `cfg4` and execute them in dependency order. 

### Local config dependency

Consider the same `skaffold.yaml` defined above. Modules `cfg1` and `cfg2` from the above file can be imported as dependencies in your current config definition, via:

```yaml
apiVersion: skaffold/v2beta11
kind: Config
requires:
  - configs: ["cfg1", "cfg2"]
    path: path/to/other/skaffold.yaml 
build:
  # build definition
deploy:
  # deploy definition
```

If the `configs` list isn’t defined then it imports all the configs defined in the file pointed by `path`. Additionally, if the `path` to the configuration isn’t defined it assumes that all the required configs are defined in the same file as the current config.

#### Note:

 In imported configurations, files are resolved relative to the location of imported Skaffold configuration file. 

### Remote config dependency

The required skaffold config can live in a remote git repository or in Google Cloud Storage:

```yaml
apiVersion: skaffold/v4beta7
kind: Config
requires:
  - configs: ["cfg1", "cfg2"]
    git:
      repo: http://github.com/GoogleContainerTools/skaffold.git
      path: getting-started/skaffold.yaml
      ref: main
  - configs: ["cfg3"]
    googleCloudStorage:
      source: gs://my-bucket/dir1/*
      path: config/skaffold.yaml
```

The environment variable `SKAFFOLD_REMOTE_CACHE_DIR` or flag `--remote-cache-dir` specifies the download location for all remote dependency contents. If undefined then it defaults to `~/.skaffold/remote-cache`. The remote cache directory consists of subdirectories with the contents retrieved from the remote dependency. For git dependencies the subdirectory name is a hash of the repo `uri` and the `branch/ref`. For Google Cloud Storage dependencies the subdirectory name is a hash of the `source`.

The remote config gets treated like a local config after substituting the path with the actual path in the cache directory.

### Profile Activation in required configs

Profiles specified by the `--profile` flag are also propagated to all configurations imported as dependencies, if they define them. This behavior can be disabled by setting the `--propagate-profiles` flag to `false`.

You can additionally set up more granular and conditional profile activations across dependencies through the `activeProfiles` stanza:

```yaml
apiVersion: skaffold/v2beta11
kind: Config
metadata:
    name: cfg
requires:
  - path: ./path/to/required/skaffold.yaml
    configs: [cfg1, cfg2]                 
    activeProfiles:                                     
     - name: profile1                               
       activatedBy: [profile2, profile3]
```

Here, `profile1` is a profile that needs to exist in both configs `cfg1` and `cfg2`; while `profile2` and `profile3` are profiles defined in the current config `cfg`. If the current config is activated with either `profile2` or `profile3` then the required configs `cfg1` and `cfg2` are imported with `profile1` applied. If the `activatedBy` clause is omitted then that `profile1` always gets applied for the imported configs.

#### Follow up

 Take a look at the [tutorial](https://skaffold.dev/docs/tutorials/config-dependencies/) section to see this in action. 

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
