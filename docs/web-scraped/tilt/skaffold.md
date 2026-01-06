# Tilt Documentation
# Source: https://docs.tilt.dev/skaffold.html
# Path: skaffold.html

  * [ Getting Started ](/index.html) [ Getting Started ](/docs_nav_gettingstarted.html)
  * [ Guides ](/tiltfile_authoring.html) [ Guides ](/docs_nav_guides.html)
  * [ Tiltfile & CLI ](/api.html) [ Tiltfile & CLI ](/docs_nav_reference.html)
  * [ Tilt API ](https://api.tilt.dev) [ Tilt API ](https://api.tilt.dev)

Tiltfile

    

  * [ Writing Your First Tiltfile ](/tiltfile_authoring.html)
  * [ Tiltfile Concepts ](/tiltfile_concepts.html)
  * [ Per user Config ](/tiltfile_config.html)
  * [ Many Tiltfiles and Many Repos ](/multiple_repos.html)
  * [ Debugging File Changes ](/file_changes.html)
  * [ Resource Dependencies ](/resource_dependencies.html)
  * [ Manual Update Control ](/manual_update_control.html)
  * [ Disabling Resources new ](/disable_resources.html)

Migrating Existing Projects

    

  * [ Plain Old Static HTML ](/example_static_html.html)
  * [ Go ](/example_go.html)
  * [ Python ](/example_python.html)
  * [ NodeJS ](/example_nodejs.html)
  * [ Java ](/example_java.html)
  * [ Bazel ](/example_bazel.html)
  * [ C# ](/example_csharp.html)

Building Images

    

  * [ Getting Started with Image Builds ](/dependent_images.html)
  * [ Setting up any Image Registry ](/personal_registry.html)
  * [ Custom Image Builders ](/custom_build.html)
  * [ Bazel ](/integrating_bazel_with_tilt.html)
  * [ Skaffold ](/skaffold.html)

Kubernetes Resources

    

  * [ Modifying YAML for Dev new ](/templating.html)
  * [ Installing YAML with Helm ](/helm.html)
  * [ Port Forwards ](/accessing_resource_endpoints.html)
  * [ Custom Resource Definitions ](/custom_resource.html)
  * [ Connecting Debuggers ](/debuggers_python.html)

More Resource Types

    

  * [ Local Commands, Servers, and Tests ](/local_resource.html)
  * [ Docker Compose ](/docker_compose.html)

Live Update

    

  * [ Technical Specifications ](/live_update_reference.html)

Continuous Integration (CI)

    

  * [ Overview ](/ci.html)

Extending Tilt

    

  * [ Custom Buttons ](/buttons.html)
  * [ Tiltfile Extensions ](/extensions.html)
  * [ Contribute Extensions ](/contribute_extension.html)

Tilt with Your Team

    

  * [ Onboarding Checklist ](/onboarding_checklist.html)
  * [ Sharing Snapshots ](/snapshots.html)

#  From Skaffold to Tilt

Tilt is a great upgrade to [Skaffold](https://skaffold.dev) for local dev.
This doc compares Tilt to Skaffold and describes how to translate your
configuration, so youâll be ready to go through the [Write a Tiltfile
Guide](tiltfile_authoring.html).

## Comparison

  * Tiltâs UI shows you status at a glance, so errors canât scroll off-screen. You can navigate the UI in your terminal and dig into the logs for just one service. (Tilt also has a global log if you do want the full firehose).
  * Tiltâs configuration is [Starlark](https://github.com/bazelbuild/starlark#tour), a subset of Python. This allows simple configs to be shorter and complex configs to be possible.

## Translate Skaffold Configuration

Skaffold concepts map almost directly into Tilt. Letâs translate an example
Skaffold configuration with two deployments and two images:

    
    
    apiVersion: skaffold/v1alpha5
    kind: Config
    build:
      artifacts:
      - image: gcr.io/windmill-public-containers/servantes/snack
        context: snack
      - image: gcr.io/windmill-public-containers/servantes/spoonerisms
        context: spoonerisms
    deploy:
      kubectl:
        manifests:
          - deployments/snack.yaml
          - deployments/spoonerisms.yaml
    

The corresponding `Tiltfile` is:

    
    
    k8s_yaml(['deployments/snack.yaml', 'deployments/spoonerisms.yaml'])
    docker_build('gcr.io/windmill-public-containers/servantes/snack', 'snack')
    docker_build('gcr.io/windmill-public-containers/servantes/spoonerisms', 'spoonerisms')
    

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/skaffold.md)







### Was this doc helpful?

Yes No

