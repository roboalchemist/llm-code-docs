# Tilt Documentation
# Source: https://docs.tilt.dev/manual_update_control.html
# Path: manual_update_control.html

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

#  Play and Pause Resources with Manual Update Control

By default, Tilt watches your filesystem for edits and, whenever it detects a
change affecting Resource X, triggers an update of that resource. All your
local code, synced to your cluster as you edit it! What could be better?

Well, sometimes thatâs _not_ what you want. Maybe updating Resource X takes
a long time and so you only want to run updates when youâre actually ready.
Maybe youâre about to check out a branch and donât want all the spurious
file changes to launch a lot of updates. Whatever your reason, Manual Update
Control is here to help.

The behavior described above is `TriggerMode: Auto` (Tiltâs default); that
is, updates are _automatically_ triggered whenever Tilt detects a change to a
relevant file.

Thereâs another way of doing things: `TriggerMode: Manual`. Tilt will still
monitor file changes associated with your resources, but instead of
automatically rebuilding and/or deploying every time a relevant file changes,
Tilt will simply indicate in the UI that files have changed, and give you a
button that you can use to kick off the update.

## Using TriggerMode

You can change the trigger mode(s) of your resources in your Tiltfile in two
different ways:

  1. Functions that configure resources ([`k8s_resource()`](/api.html#api.k8s_resource), [`local_resource()`](/api.html#api.local_resource), and [`dc_resource()`](/api.html#api.dc_resource)) have an optional arg, `trigger_mode`; for that specific resource, you can pass either `TRIGGER_MODE_AUTO` or `TRIGGER_MODE_MANUAL`.
  2. If you want to adjust all of your resources at once, call the top-level function [`trigger_mode()`](/api.html#api.trigger_mode) with one of those two constants. This sets the _default trigger mode for all resources_. (You can still use `k8s_resource()` to set the trigger mode for a specific resource.)

Here are some examples:

    
    
    ...
    # TriggerMode = Auto by default
    k8s_resource('snack')
    
    
    
    ...
    # TriggerMode = Manual
    k8s_resource('snack', trigger_mode=TRIGGER_MODE_MANUAL)
    
    
    
    trigger_mode(TRIGGER_MODE_MANUAL)
    ...
    # TriggerMode = Manual (default set above)
    k8s_resource('snack')
    
    # TriggerMode = Auto (can override the above default
    # for specific resources)
    k8s_resource('bar', trigger_mode=TRIGGER_MODE_AUTO)
    

![](assets/img/update-control.gif)

When you make changes to `snack`, instead of them being automatically applied,
Tilt will simply indicate unapplied changes by the asterisk to the right of
`snack` in the sidebar. It will not automatically apply those changes.
Instead, it will wait until you click the apply button to the left of `snack`.

## Auto Init

TriggerMode can be combined with the `auto_init` argument on
[`k8s_resource()`](/api.html#api.k8s_resource),
[`local_resource()`](/api.html#api.local_resource), and
[`dc_resource()`](/api.html#api.dc_resource) for even more fine-grained
control.

To configure a resource to _only_ run when explicitly triggered from the UI,
set `auto_init=False` and `trigger_mode=TRIGGER_MODE_MANUAL`. It will not run
on start nor when files are changed.

To configure a resource that does _not_ run at start, but still runs whenever
a file dependency is changed, set `auto_init=False` and
`trigger_mode=TRIGGER_MODE_AUTO`. This can be useful for tasks like linting or
executing tests automatically, for example.

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/manual_update_control.md)







### Was this doc helpful?

Yes No

