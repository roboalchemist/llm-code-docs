# Source: https://skaffold.dev/docs/environment/image-registries/

Title: Image Repository Handling

URL Source: https://skaffold.dev/docs/environment/image-registries/

Markdown Content:
Image Repository Handling | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/environment/image-registries/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

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

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/environment/image-registries.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Image%20Repository%20Handling)

**Applicable**[`dev`](https://skaffold.dev/docs/references/cli#skaffold-dev)[`debug`](https://skaffold.dev/docs/references/cli#skaffold-debug)[`run`](https://skaffold.dev/docs/references/cli#skaffold-run)[`build`](https://skaffold.dev/docs/references/cli#skaffold-build)[`test`](https://skaffold.dev/docs/references/cli#skaffold-test)[`deploy`](https://skaffold.dev/docs/references/cli#skaffold-deploy)[`render`](https://skaffold.dev/docs/references/cli#skaffold-render)

*   [Insecure image registries](https://skaffold.dev/docs/environment/image-registries/#insecure-image-registries)

1.   [Documentation](https://skaffold.dev/docs/)
2.   [Environment Management](https://skaffold.dev/docs/environment/)
3.   Image Repository Handling

Image Repository Handling
=========================

Often, a Kubernetes manifest (or `skaffold.yaml`) makes references to images that push to registries that we might not have access to. Modifying these individual image names manually is tedious, so Skaffold supports automatically prefixing these image names with a registry specified by the user. Using this, any project configured with Skaffold can be run by any user with minimal configuration, and no manual YAML editing!

This is accomplished through the `default-repo` functionality, and can be used one of three ways:

1.   `--default-repo` flag

```bash
skaffold dev --default-repo <myrepo>
``` 
2.   `SKAFFOLD_DEFAULT_REPO` environment variable

```bash
SKAFFOLD_DEFAULT_REPO=<myrepo> skaffold dev
``` 
3.   Skaffold’s global config

```bash
skaffold config set default-repo <myrepo>
``` 

If no `default-repo` is provided by the user, there is no automated image name rewriting, and Skaffold will try to push the image as provided in the yaml.

The image name rewriting strategies are designed to be _conflict-free_: the full image name is rewritten on top of the default-repo so similar image names don’t collide in the base namespace (e.g.: repo1/example and repo2/example would collide in the target_namespace/example without this)

Automated image name rewriting strategies are determined based on the default-repo and the original image repository:

*   default-repo domain does not contain `gcr.io` or `-docker.pkg.dev`

    *   **strategy**: escape & concat & truncate to 256

```
original image: 	gcr.io/k8s-skaffold/skaffold-example1
 default-repo:      aws_account_id.dkr.ecr.region.amazonaws.com
 rewritten image:   aws_account_id.dkr.ecr.region.amazonaws.com/gcr_io_k8s-skaffold_skaffold-example1
```

*   default-repo contain `gcr.io` or `-docker.pkg.dev` (special cases - as GCR and AR allow for arbitrarily deep directory structure in image repo names)

    *   **strategy**: concat unless prefix matches

    *   **example1**: prefix doesn’t match:

```
original image: 	gcr.io/k8s-skaffold/skaffold-example1
  default-repo: 	gcr.io/myproject/myimage
  rewritten image:  gcr.io/myproject/myimage/gcr.io/k8s-skaffold/skaffold-example1
```
    *   **example2**: prefix matches:

```
original image: 	gcr.io/k8s-skaffold/skaffold-example1
  default-repo: 	gcr.io/k8s-skaffold
  rewritten image:  gcr.io/k8s-skaffold/skaffold-example1
```
    *   **example3**: shared prefix:

```
original image: 	gcr.io/k8s-skaffold/skaffold-example1
  default-repo: 	gcr.io/k8s-skaffold/myimage
  rewritten image:  gcr.io/k8s-skaffold/myimage/skaffold-example1
```

Insecure image registries
-------------------------

During development you may be forced to push images to a registry that does not support HTTPS. By itself, Skaffold will never try to downgrade a connection to a registry to plain HTTP. In order to access insecure registries, this has to be explicitly configured per registry name.

There are several levels of granularity to allow insecure communication with some registry:

1.   Per Skaffold run via the repeatable `--insecure-registry` flag

```bash
skaffold dev --insecure-registry insecure1.io --insecure-registry insecure2.io
``` 
2.   Per Skaffold run via `SKAFFOLD_INSECURE_REGISTRY` environment variable

```bash
SKAFFOLD_INSECURE_REGISTRY='insecure1.io,insecure2.io' skaffold dev
``` 
3.   Per project via the Skaffold pipeline config `skaffold.yaml`

```yaml
build:
    insecureRegistries:
    - insecure1.io
    - insecure2.io
``` 
4.   Per user via Skaffold’s global config

```bash
skaffold config set insecure-registries insecure1.io           # for the current kube-context
skaffold config set --global insecure-registries insecure2.io  # for any kube-context
``` 
Note that multiple set commands _add_ to the existing list of insecure registries. To clear the list, run `skaffold config unset insecure-registries`.

Skaffold will join the lists of insecure registries, if configured via multiple sources.

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
