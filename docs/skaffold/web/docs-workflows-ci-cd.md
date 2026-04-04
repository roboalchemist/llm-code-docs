# Source: https://skaffold.dev/docs/workflows/ci-cd/

Title: Continuous Delivery

URL Source: https://skaffold.dev/docs/workflows/ci-cd/

Published Time: Thu, 13 Nov 2025 20:49:27 GMT

Markdown Content:
Continuous Delivery | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/workflows/ci-cd/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

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

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/workflows/ci-cd.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Continuous%20Delivery)

*   [Run entire pipeline end-to-end](https://skaffold.dev/docs/workflows/ci-cd/#run-entire-pipeline-end-to-end)
*   [Traditional continuous delivery](https://skaffold.dev/docs/workflows/ci-cd/#traditional-continuous-delivery)
*   [Separation of rendering and deployment](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment)
    *   [GitOps-style continuous delivery](https://skaffold.dev/docs/workflows/ci-cd/#gitops-style-continuous-delivery)
    *   [Example: Hydrate manifests then deploy/apply to cluster](https://skaffold.dev/docs/workflows/ci-cd/#example-hydrate-manifests-then-deployapply-to-cluster)

1.   [Documentation](https://skaffold.dev/docs/)
2.   [Guides](https://skaffold.dev/docs/workflows/)
3.   Continuous Delivery

Continuous Delivery
===================

#### Note

 Skaffold is used under the hood to power Google Cloud Platform’s [Cloud Deploy API](https://cloud.google.com/deploy). See the docs [here](https://cloud.google.com/deploy/docs/using-skaffold) for more information on how to use Skaffold + Cloud Deploy for CI/CD 

Skaffold provides several features and sub-command “building blocks” that make it very useful for integrating with (or creating entirely new) CI/CD pipelines. The ability to use the same `skaffold.yaml` for iterative development and continuous delivery eases handing off an application from a development team to an ops team.

Let’s start with the simplest use case: a single, full deployment of your application.

Run entire pipeline end-to-end
------------------------------

`skaffold run` is a single command for a one-off deployment. It runs through every major phase of the Skaffold lifecycle: building your application images, tagging these images (and optionally pushing them to a remote registry), deploying your application to the target cluster, and monitoring the created resources for readiness.

We recommend `skaffold run` for the simplest Continuous Delivery setup, where it is sufficient to have a single step that deploys from version control to a cluster.

For more sophisticated Continuous Delivery pipelines, Skaffold offers building blocks:

*   [status-check](https://skaffold.dev/docs/status-check/) - wait for `deployments` to stabilize and succeed only if all deployments are successful
*   [`skaffold build`](https://skaffold.dev/docs/workflows/ci-cd/#skaffold-build-skaffold-deploy) - build, tag and push artifacts to a registry
*   [`skaffold deploy`](https://skaffold.dev/docs/workflows/ci-cd/#skaffold-build-skaffold-deploy) - deploy built artifacts to a cluster
*   [`skaffold render`](https://skaffold.dev/docs/workflows/ci-cd/#skaffold-render-skaffold-apply) - export the transformed Kubernetes manifests
*   [`skaffold apply`](https://skaffold.dev/docs/workflows/ci-cd/#skaffold-render-skaffold-apply) - send hydrated Kubernetes manifests to the API server to create resources on the target cluster

Traditional continuous delivery
-------------------------------

`skaffold build` will build your project’s artifacts, and push the build images to the specified registry. If your project is already configured to run with Skaffold, `skaffold build` can be a very lightweight way of setting up builds for your CI pipeline. Passing the `--file-output` flag to Skaffold build will also write out your built artifacts in JSON format to a file on disk, which can then by passed to `skaffold deploy` later on. This is a great way of “committing” your artifacts when they have reached a state that you’re comfortable with, especially for projects with multiple artifacts for multiple services.

Example using the current git state as a unique file ID to “commit” build state:

Storing the build result in a commit specific JSON file:

```bash
export STATE=$(git rev-list -1 HEAD --abbrev-commit)
skaffold build --file-output build-$STATE.json
```

outputs the tag generation and cache output from Skaffold:

```bash
Generating tags...
 - gcr.io/k8s-skaffold/skaffold-example:v0.41.0-17-g3ad238db
Checking cache...
 - gcr.io/k8s-skaffold/skaffold-example: Found. Tagging
```

The content of the JSON file

```bash
cat build-$STATE.json
```

looks like:

```json
{"builds":[{"imageName":"gcr.io/k8s-skaffold/skaffold-example","tag":"gcr.io/k8s-skaffold/skaffold-example:v0.41.0-17-g3ad238db@sha256:eeffb639f53368c4039b02a4d337bde44e3acc728b309a84353d4857ee95c369"}]}
```

We can then use this build result file to deploy with Skaffold:

```bash
skaffold deploy -a build-$STATE.json
```

and as we’d expect, we see a bit of deploy-related output from Skaffold:

```bash
Tags used in deployment:
 - gcr.io/k8s-skaffold/skaffold-example -> gcr.io/k8s-skaffold/skaffold-example:v0.41.0-17-g3ad238db@sha256:eeffb639f53368c4039b02a4d337bde44e3acc728b309a84353d4857ee95c369
Starting deploy...
 - pod/getting-started configured
```

Separation of rendering and deployment
--------------------------------------

beta

Skaffold allows separating the generation of fully-hydrated Kubernetes manifests from the actual deployment of those manifests, using the `skaffold render` and `skaffold apply` commands.

`skaffold render` builds all application images from your artifacts, templates the newly-generated image tags into your Kubernetes manifests (based on your project’s deployment configuration), and then prints out the final hydrated manifests to a file or your terminal. This allows you to capture the full, declarative state of your application in configuration, such that _applying_ the changes to your cluster can be done as a separate step.

`skaffold apply` consumes one or more fully-hydrated Kubernetes manifests, and then sends the results directly to the Kubernetes control plane via `kubectl` to create resources on the target cluster. After creating the resources on your cluster, `skaffold apply` uses Skaffold’s built-in health checking to monitor the created resources for readiness. See [resource health checks](https://skaffold.dev/docs/status-check/) for more information on how Skaffold’s resource health checking works.

_Note: `skaffold apply` always uses `kubectl` to deploy resources to a target cluster, regardless of deployment configuration in the provided skaffold.yaml. Only a small subset of deploy configuration is honored when running `skaffold apply`:_

*   deploy.statusCheckDeadlineSeconds
*   deploy.kubeContext
*   deploy.logs.prefix
*   deploy.kubectl.flags
*   deploy.kubectl.defaultNamespace
*   deploy.kustomize.flags
*   deploy.kustomize.defaultNamespace

#### Note

`skaffold apply` attempts to honor the deployment configuration mentioned above. But when conflicting configuration is detected in a multi-configuration project, `skaffold apply` will not work. 

`skaffold apply` works with any arbitrary Kubernetes YAML, whether it was generated by Skaffold or not, making it an ideal counterpart to `skaffold render`.

### GitOps-style continuous delivery

You can use this separation of rendering and deploying to enable GitOps CD pipelines.

GitOps-based CD pipelines traditionally see fully-hydrated Kubernetes manifests committed to a configuration Git repository (separate from the application source), which triggers a deployment pipeline that applies the changes to resources on the cluster.

### Example: Hydrate manifests then deploy/apply to cluster

First, use `skaffold render` to hydrate the Kubernetes resource file with a newly-built image tag:

```code
$ skaffold render --output render.yaml
```

```yaml
# render.yaml
apiVersion: v1
kind: Pod
metadata:
  name: getting-started
  namespace: default
spec:
  containers:
  - image: gcr.io/k8s-skaffold/skaffold-example:v1.19.0-89-gdbedd2a20-dirty
    name: getting-started
```

Then, we can apply this output directly to the cluster:

```code
$ skaffold apply render.yaml

Starting deploy...
 - pod/getting-started created
Waiting for deployments to stabilize...
Deployments stabilized in 49.277055ms
```

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
