# Tilt Documentation
# Source: https://docs.tilt.dev/example_bazel.html
# Path: example_bazel.html

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

#  Example: Bazel

The best indicator of a healthy development workflow is a short feedback loop.

Kubernetes is a huge wrench in the works.

Letâs fix this.

In this example, weâre going to look at a project that uses Bazel to build
images and Kubernetes resources. Weâll show you how to use Tilt to speed up
iterative development. Our simple server uses Go templates to serve HTML.

Weâll use Tilt to:

  * Run the server on Kubernetes
  * Measure the time from a code change to a new process
  * Optimize that time for faster feedback

All the code is in this repo:

[tilt-example-bazel](https://github.com/tilt-dev/tilt-example-bazel)

To skip straight to the fully optimized setup, go to this Tiltfile:

[Recommended Setup](https://github.com/tilt-dev/tilt-example-
bazel/blob/main/3-recommended/Tiltfile)

For now, weâve posted the code so that teams can copy it and adapt it to
their own Bazel builds.

Weâre workshopping this approach with partner teams and tweaking it to make
sure it works well. Weâll add a longer write-up to the doc on how it works
once weâre happy with it.

Stay tuned!

## Further Reading

### CI

Once youâre done configuring your project, set up a CI test to ensure your
setup doesnât break! In the example repo, CircleCI uses
[`ctlptl`](https://github.com/tilt-dev/ctlptl) to create a single-use
Kubernetes cluster. The test script invokes `tilt ci`. The `tilt ci` command
deploys all services in a Tiltfile and exits successfully if theyâre
healthy.

  * [CircleCI config](https://github.com/tilt-dev/tilt-example-bazel/blob/master/.circleci/config.yml)
  * [Test script](https://github.com/tilt-dev/tilt-example-bazel/blob/master/test/test.sh)

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/example_bazel.md)







### Was this doc helpful?

Yes No

