# Source: https://skaffold.dev/docs/tutorials/skaffold-resource-selector/

Title: Manage CRDs w/ Skaffold - Configuring Which K8s Resources & Fields Skaffold Manages

URL Source: https://skaffold.dev/docs/tutorials/skaffold-resource-selector/

Published Time: Thu, 13 Nov 2025 20:49:27 GMT

Markdown Content:
Manage CRDs w/ Skaffold - Configuring Which K8s Resources & Fields Skaffold Manages | Skaffold
===============
[Skaffold](https://skaffold.dev/)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [Documentation](https://skaffold.dev/docs/)
*   [skaffold.yaml](https://skaffold.dev/docs/references/yaml/)
*   [Versions](https://skaffold.dev/docs/tutorials/skaffold-resource-selector/#)[v1.0](https://skaffold-v1.web.app/)[v2.0](https://skaffold-v2.web.app/) 

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

[Edit this page](https://github.com/GoogleContainerTools/skaffold/edit/main/docs-v2/content/en/docs/tutorials/skaffold-resource-selector.md)[Create documentation issue](https://github.com/GoogleContainerTools/skaffold/issues/new?title=Manage%20CRDs%20w/%20Skaffold%20-%20Configuring%20Which%20K8s%20Resources%20&%20Fields%20Skaffold%20Manages)

**Applicable**
**Not applicable**[`dev`](https://skaffold.dev/docs/references/cli#skaffold-dev)[`debug`](https://skaffold.dev/docs/references/cli#skaffold-debug)[`run`](https://skaffold.dev/docs/references/cli#skaffold-run)[`build`](https://skaffold.dev/docs/references/cli#skaffold-build)[`test`](https://skaffold.dev/docs/references/cli#skaffold-test)[`deploy`](https://skaffold.dev/docs/references/cli#skaffold-deploy)[`render`](https://skaffold.dev/docs/references/cli#skaffold-render)

1.   [Documentation](https://skaffold.dev/docs/)
2.   [Tutorials](https://skaffold.dev/docs/tutorials/)
3.   Manage CRDs w/ Skaffold - Configuring Which K8s Resources & Fields Skaffold Manages

Manage CRDs w/ Skaffold - Configuring Which K8s Resources & Fields Skaffold Manages
===================================================================================

Common Use Cases This Page Helps Resolve:

*   Users who want skaffold to properly manage the rendering and deployment of their custom CRDs (as skaffold does with K8s objects like Pod, Deployment.apps, etc.) 
    *   Additionally users w/ a CRD that uses a different field name for `image:` (eg: `foo:`) and want skaffold to properly modify the value to instead have the image label for the image skaffold recently built

*   Users who are seeing issues with skaffold’s default resource field overwriting for a given resource - eg: skaffold errors as it tries to mutate immutable config on re-deployment

Currently skaffold modifies the manifests it renders and deploys for the following functionality:

*   status checking - done by mutating the manifest/K8s-Object by adding a label - skaffold/dev/run-id. Skaffold uses this run-id to identify the deployments Skaffold manages with it’s status checking.
*   image label overwriting - done by mutating the manifest/K8s-Object by substituting the `image:$ORIGINAL_IMAGE_TAG` value(s) in a manifest with `image:$RECENT_SKAFFOLD_BUILT_IMAGE`

Skaffold has by default the following resources set for management via field “labels:” and “image:” overwriting:

_The below list is derived from the values defined [here](https://github.com/GoogleContainerTools/skaffold/blob/main/pkg/skaffold/kubernetes/manifest/visitor.go)_

*   Pod
*   DaemonSet.apps
*   Deployment.apps
*   ReplicaSet.apps
*   StatefulSet.apps (with the exception of `.spec.volumeClaimTemplates.*.metadata.labels` field(s))
*   CronJob.batch
*   Job.batch
*   DaemonSet.extensions
*   Deployment.extensions
*   ReplicaSet.extension
*   Service.serving.knative.dev
*   Fleet.agones.dev
*   GameServer.agones.dev
*   Rollout.argoproj.io
*   Workflow.argoproj.io
*   CronWorkflow.argoproj.io
*   WorkflowTemplate.argoproj.io
*   ClusterWorkflowTemplate.argoproj.io
*   *.cnrm.cloud.google.com

_This default overwriting modifies all JSON Paths for those GroupKinds of the form:_

*   _*.metadata.labels (skaffold appends a `run-id` label to existing labels or adds a `labels`field with a `run-id` entry if it didn’t exist prior)_
*   _*.image (changes `image:` value to be the skaffold built image ONLY IF skaffold manages the original `image:` value)_

The GroupKind’s that Skaffold manages (via resource field overwriting) are user configurable via the `resourceSelector:` top level configuration.

 The `resourceSelector` configuration allows users to modify and extend which resources and what fields of those resources skaffold modifies.

 Currently skaffold only supports `label:` and `.metadata.labels` related modifications.

`resourceSelector` spec (from `pkg/skaffold/schema/latest/config.go`)

```go
// ResourceSelector describes user defined filters describing how skaffold should treat objects/fields during rendering.
ResourceSelector ResourceSelectorConfig `yaml:"resourceSelector,omitempty"`
```

```go
// ResourceSelectorConfig contains all the configuration needed by the deploy steps.
type ResourceSelectorConfig struct {
	// Allow configures an allowlist for transforming manifests.
	Allow []ResourceFilter `yaml:"allow,omitempty"`
	// Deny configures an allowlist for transforming manifests.
	Deny []ResourceFilter `yaml:"deny,omitempty"`
}
```

```go
// ResourceFilter contains definition to filter which resource to transform.
type ResourceFilter struct {
	// GroupKind is the compact format of a resource type.
	GroupKind string `yaml:"groupKind" yamltags:"required"`
	// Image is an optional slice of JSON-path-like paths of where to rewrite images.
	Image []string `yaml:"image,omitempty"`
	// Labels is an optional slice of JSON-path-like paths of where to add a labels block if missing.
	Labels []string `yaml:"labels,omitempty"`
	// PodSpec is an optional slice of JSON-path-like paths of where pod spec properties can be overwritten.
	PodSpec []string `yaml:"podSpec,omitempty"`
}
```

The values for `Image` and `Labels` support a JSON Path style string which designates a path to a field in the speified GroupKind.

 Additionally there is a special `.*` value that can be used which means that skaffold will attempt to overwrite all relevant labels following the below rules:

*   image: [".*"] -> replace all fields which follow `*.image:` where the value is an image that skaffold manages/builds
*   labels: [".*"] -> append-to or create a field named `*.metadata.labels` if a field `*.metadata` is found

Some example use cases and motivations for the `resourceSelector` are shown below:

*   Skaffold Management of Custom CRD - The below snippet using `resourceSelector` allows a user to configure skaffold to manage a custom CRD (eg: CustomDeployment.skaffold.dev) they’ve created for their application in a skaffold.

_Without this snippet, skaffold would apply the yaml but would not properly wait for child resources or replace the `image:` values with skaffold built images_

```yaml
apiVersion: skaffold/v3alpha1
kind: Config
build:
  artifacts:
    - image: my-image
      context: my-image
manifests:
  rawYaml:
  - my-manifests-*
resourceSelector:
  allow:
    - groupKind: "CustomDeployment.skaffold.dev"
      image: [".*"]
      labels: [".*"]
```

Using the above configuation, skaffold will properly update any `*.image` field and `*.metadata.labels` field allowing it to work as expected (similar to Pod, Deployment.apps, etc.)

*   Fix Issue With Skaffold Overwriting Immutable Field - The below snippet using `resourceSelector` shows a user configuring skaffold to change it’s behaviour to NOT overwrite a resource’s field to prevent K8s errors related to overwriting an immutable field:

_The below configuration is actually a part of skaffold’s default configuration, just made into a snippet to use as an example_

```yaml
apiVersion: skaffold/v3alpha1
kind: Config
build:
  artifacts:
    - image: my-image
      context: my-image
manifests:
  rawYaml:
  - my-manifests-*
resourceSelector:
  allow:
    - groupKind: "StatefulSet.apps"
      image: [".*"]
      labels: [".*"]
  deny:
    - groupKind: "StatefulSet.apps"
      labels: [".spec.volumeClaimTemplates.*.metadata.labels"]
```

*   Allow `image:` Overwriting For Differently Named Image Field(s) - The below snippet using `resourceSelector` shows a user configuring skaffold to change it’s behaviour to overwrite a resource’s `foo:`field with skaffold built images.

 This allows skaffold to properly support the images skaffold builds this resources which uses `foo:` instead of `image:` for an image value:

```yaml
apiVersion: skaffold/v3alpha1
kind: Config
build:
  artifacts:
    - image: my-image
      context: my-image
manifests:
  rawYaml:
  - my-manifests-*
resourceSelector:
  allow:
    - groupKind: "CloudBuildTrigger.cloudbuild.cnrm.cloud.google.com"
      image: [".*", ".spec.build.step.*.name"]
      labels: [".*"]
```

 Last modified November 13, 2025: [chore: Skaffold 2.17 release (#9912) (561ce51e)](https://github.com/GoogleContainerTools/skaffold/commit/561ce51e1e2c4174b375e694a676585cea7c2b65)

*   [](https://github.com/GoogleContainerTools/skaffold)
*   [](https://skaffold.dev/docs/resources/#community)
*   [](https://groups.google.com/forum/#!forum/skaffold-users)
*   [](https://forms.gle/BMTbGQXLWSdn7vEs6)

© 2025 Skaffold Authors All Rights Reserved

[Privacy Policy](https://policies.google.com/privacy)
