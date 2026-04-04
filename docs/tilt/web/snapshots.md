# Tilt Documentation
# Source: https://docs.tilt.dev/snapshots.html
# Path: snapshots.html

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

#  Sharing Snapshots

Snapshots save your Tilt state to a file, so you (or another Tilt user) can
later load that file, and interactively explore logs and error status for that
moment in time. This can help with async debugging, and add context to bug
reports.

## Via Command Line

With a Tilt session running, run `tilt snapshot create <file>` to create a
JSON file.

Then, run `tilt snapshot view <file>` to view the Snapshot.

A header on the top of the screen shows that youâre viewing a Snapshot.

![](/assets/docimg/snapshots-header.png)

## Via Tilt Web

Create a Snapshot by clicking ![](/assets/docimg/snapshots-icon.png)on the
top-right of the screen, then clicking the âSave Snapshotâ button.

To view the downloaded Snapshot, run `tilt snapshot view <file>` in your
Terminal.

![](/assets/docimg/snapshots-menu.png)

## Deprecated: Tilt Cloud

Snapshots were once part of the Tilt Cloud, a hosted service for storing
snapshots.

Weâve found that the new file-based flow is more flexible and easier to
understand.

If you previously used Tilt Cloud and want to learn more about the
deprecation, [read this blog post](https://blog.tilt.dev/2022/05/12/offline-
snapshots.html).

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/snapshots.md)







### Was this doc helpful?

Yes No

