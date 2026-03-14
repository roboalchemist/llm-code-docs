# Source: https://skaffold.dev/docs/environment/profiles/

Title: Profiles

URL Source: https://skaffold.dev/docs/environment/profiles/

Markdown Content:
Skaffold profiles allow you to define build, test and deployment configurations for different contexts. Different contexts are typically different environments in your app’s lifecycle, like Production or Development.

You can create profiles in the `profiles` section of `skaffold.yaml`.

For a detailed discussion on Skaffold configuration, see [Skaffold Concepts](https://skaffold.dev/docs/design/config/) and [skaffold.yaml References](https://skaffold.dev/docs/references/yaml/).

Profiles (`profiles`)
---------------------

Each profile has six parts:

*   Name (`name`): The name of the profile
*   Build configuration (`build`)
*   Test configuration (`test`)
*   Deploy configuration (`deploy`)
*   Patches (`patches`)
*   Activation (`activation`)

Once a profile is activated, the specified `build`, `test` and `deploy` configuration in it will be laid onto, but won’t completely replace, the `build`, `test` and `deploy` sections declared in the main section of `skaffold.yaml`. The `build`, `test` and `deploy` configuration in the `profiles` section use the same syntax as the `build`, `test` and `deploy` sections of `skaffold.yaml`; for more information, see [Builders](https://skaffold.dev/docs/builders/), [Testers](https://skaffold.dev/docs/testers), [Deployers](https://skaffold.dev/docs/deployers/) and you can always refer to [skaffold.yaml reference](https://skaffold.dev/docs/references/yaml/) for an overview of the syntax. Alternatively, you can override the main configuration with finer grained control using `patches`.

### Activation

You can activate a profile two ways: CLI flag or skaffold.yaml activations.

**CLI flag**: You can activate profiles with the `-p` (`--profile`) parameter in the `skaffold dev` and `skaffold run` commands.

```
skaffold run -p [PROFILE]
```

**Activations in skaffold.yaml**: You can auto-activate a profile based on

*   kubecontext (could be either a string or a regexp: prefixing with `!` will negate the match)
*   environment variable value
*   skaffold command (dev/run/build/deploy)

A profile is auto-activated if any one of the activations under it are triggered. An activation is triggered if all of the criteria (`env`, `kubeContext`, `command`) are triggered.

In the example below:

*   `profile1` is activated if `MAGIC_VAR` is 42
*   `profile2` is activated if `MAGIC_VAR` is 1337 or we are running `skaffold dev` while kubecontext is set to `minikube`.

```
build:
  artifacts:
  - image: gcr.io/k8s-skaffold/skaffold-example
manifests:
  rawYaml:
  - k8s-pod
profiles:
- name: profile1
  activation:
    - env: MAGIC_VAR=42
- name: profile2
  activation:
    - env: MAGIC_VAR=1337
    - kubeContext: minikube
      command: dev
```

### Override via replacement

The `build`, `test` and `deploy` sections defined in the profile will be laid onto the main configuration. The default values are the same in profiles as in the main config.

The following example showcases a `skaffold.yaml` with one profile named `gcb`, for building with Google Cloud Build:

```
build:
  artifacts:
  - image: gcr.io/k8s-skaffold/skaffold-example
manifests:
  rawYaml:
  - k8s-pod
profiles:
- name: gcb
  build:
    googleCloudBuild:
      projectId: k8s-skaffold
```

With no profile activated, Skaffold will build the artifact `gcr.io/k8s-skaffold/skaffold-example` using local Docker daemon and deploy it with `kubectl`.

However, if you run Skaffold with the following command:

```
skaffold dev -p gcb
```

Skaffold will switch to Google Cloud Build for building artifacts.

Note that since the `gcb` profile does not specify a deploy configuration, Skaffold will continue using `kubectl` for deployments.

### Override via patches

Patches are a more verbose way of overriding your config, but they provide a powerful, fine-grained way to override individual values in your yaml config. They are based on [JSON Patch](http://jsonpatch.com/) under the hood.

In the example below instead of overriding the whole `build` section, the `dev` profile specifically defines a different Dockerfile to use for the first artifact.

```
build:
  artifacts:
    - image: gcr.io/k8s-skaffold/skaffold-example
      docker:
        dockerfile: Dockerfile
    - image: gcr.io/k8s-skaffold/skaffold2
    - image: gcr.io/k8s-skaffold/skaffold3
manifests:
  rawYaml:
  - k8s-pod
profiles:
  - name: dev
    patches:
      - op: replace
        path: /build/artifacts/0/docker/dockerfile
        value: Dockerfile_dev
```

### Activating multiple profiles at the same time

Multiple profiles can be specified either by using the `-p` flag multiple times or by comma separated profiles.

```
skaffold dev -p hello,world
```

Skaffold will activate both profiles, `hello` and `world`. This is e.g. useful when combined with patches to provide a composable development setup where `hello` and `world` can be added on demand.

### Deactivating Profiles

Profiles can also be manually deactivated by prefixing the profile name with `-` like so:

```
skaffold dev -p hello,-world
```

Skaffold will activate the `hello` profile, and deactivate the `world` profile, even if it had otherwise been activated through the configuration.
