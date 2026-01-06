# Tilt Documentation
# Source: https://docs.tilt.dev/local_resource.html
# Path: local_resource.html

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

#  Setting up Local Commands, Servers, and Tests

Each entry in your Tilt sidebar is a **resource** âa unit of work managed by
Tilt.

The most common type of Tilt resource is one that represents a deployed
service, and is made up of some combination of image build instructions and
Kubernetes YAML.

A **local resource** works like any other resource in your sidebar; it
represents a unit of work, and executes either automatically in response to
file changes, or [manually](https://docs.tilt.dev/manual_update_control.html)
on signal from the user. For your resource `MyGreatService`, when one of its
file dependencies changes, its work is to build a Docker image and deploy some
k8s yaml; for a local resource, itâs to execute an arbitrary command on your
local filesystem.

You can define a local resource in your Tiltfile as follows:

    
    
    local_resource('yarn', cmd='yarn install', deps=['package.json'])
    

See the [`local_resource` API spec](api.html#api.local_resource) for more
details.

## File dependencies

The `deps` argument allows you to specify file dependencies for your local
resourceâeither as a string (filepath) or a list of strings (list of
filepaths).

When Tilt detects a change to any of a resourceâs `deps`, the resource will
execute (unless the resource is in `TRIGGER_MODE_MANUAL`, in which case the
resource will not execute, but youâll see the âpending changesâ
indicator next to your resource in the sidebar).

Specifying `deps` is optional. By default, a local resource without `deps`
runs only once: on `tilt up` (and any time you change its definition in your
`Tiltfile`). You can always manually trigger a local resource (or any
resource) with the [âforce updateâ
button](https://blog.tilt.dev/2019/11/14/force-update.html):

!["force update" button](assets/img/force-update-button.png)

You might use this pattern to, for instance, define a local resource that
refreshes tokens/credentials needed by your appâyou want to do it once on
`tilt up`, and every now and then as needed, but not in response to any
particular file changes.

As with `docker_build` and `custom_build`, you can specify files/directories
to be ignored [with the `ignore`
argument](http://blog.tilt.dev/2019/06/07/better-monorepo-container-builds-
with-context-filters.html).

## Resource dependencies

The `resource_deps` argument allows you to specify the order that resource
deps initialize.

A common pattern is to use `local_resource` to run database initialization
after your database comes up in Kubernetes.

See the [Resource Dependencies guide](resource_dependencies.html) for more.

## Parallelism

Local resources can read and write to the local filesystem freely.

Tilt will run local resource build commands in serial with other commands.
This prevents race conditions: if your local resources are writing files at
the same time as other resources are trying to read them, your build could get
into weird and unpredictable states (especially when writes are only partially
completed).

But you can explicitly specify that itâs ok to run resources in parallel
with:

    
    
    local_resource(name, cmd, allow_parallel=True)
    

Teams sometimes use this to run linters or unit tests that only read local
files but do not write.

## auto_init

By default, a local resource will run on startup. To disable this behavior,
specify `auto_init=False`:

    
    
    local_resource('reset-db', cmd='reset_db.sh', auto_init=False)
    

You can combine this with `trigger_mode=TRIGGER_MODE_MANUAL` (so the resource
only runs when explicitly triggered) or `trigger_mode=TRIGGER_MODE_AUTO` (so
that the resource does not run on âtilt upâ but will run if any of its
file dependencies are changed â this can be useful for tests, for example).

For more on trigger mode, [see the
docs](https://docs.tilt.dev/manual_update_control.html).

## serve_cmd

`local_resource`âs `serve_cmd` argument allows a local resource to function
as a persistent process, so you can use it for things like running services
locally instead of in k8s, or `tail -f`.

This is named `serve_cmd` because its main intent is to allow the
specification of a command to start a process that runs a server, but it can
be used for any long-running process.

Without `serve_cmd`, a local resource functions as a sort of batch job. Tilt
runs the command and expects it to terminate. While the command is running,
itâs âin progressâ, and when it finishes, itâs red or green based on
the processâs exit code.

With `serve_cmd`, when the resource updates:

  1. Tilt will first run the resourceâs `cmd`, if it is non-empty. 
     1. While you can just put this into your `serve_cmd`, it can be useful to separate your âbuildâ step (e.g., `go build ./main.go`) from your ârunâ step.
     2. When updating a resource, Tilt will not kill the resourceâs previously running process until itâs successfully executed `cmd`.
  2. If `cmd` succeeds, Tilt will run the resourceâs `serve_cmd`. 
     1. As soon as the `serve_cmd` starts, Tilt will consider the resource updated and ârunningâ.
     2. If the `serve_cmd` exits, with any exit code, Tilt will consider it an error and turn it red.

Some examples:

#### build and run a server locally

`local_resource('local-server', cmd='go build ./cmd/myserver',
serve_cmd='./myserver --port=8001', deps=['cmd/myserver'])`

#### keep a port forward open to a service not deployed by Tilt

`local_resource('kube-port-forward', serve_cmd='kubectl port-forward -n
openfaas svc/gateway 8080:8080')`

#### show the k8s api serverâs logs

`local_resource('kube-logs', serve_cmd='kubectl logs -f -n kube-system kube-
apiserver-docker-desktop')`

#### custom environment

    
    
    # will override any values for this key currently in the env
    update_env={'CGO_ENABLED': '0'}
    # if $PORT set, use that value, else use '8001'}
    serve_env={'PORT': os.getenv('PORT', default='8001')}
    local_resource('custom-env',
                   cmd='go build ./cmd/myserver', env=update_env,
                   serve_cmd='./myserver', serve_env=serve_env,
                   deps=['cmd/myserver'])
    

## readiness_probe

Probes for local resources determine whether the `serve_cmd` is considered
ready. In addition to providing more accurate resource visibility in the Tilt
UI, this ensures that Tilt waits for the probe to be successful before
starting any dependent resources for the first time. Readiness probes are
optional; local resources without one are considered ready as soon as the
process is started.

Local resource probes behave very similarly to Kubernetes readiness probes and
support similar parameters to adjust the probing period, failure threshold,
and more. See the [`probe` API spec](api.html#api.probe) for all available
options.

Probes can be an HTTP GET request
([`http_get_action`](api.html#api.http_get_action)), a TCP socket connection
([`tcp_socket_action`](api.html#api.tcp_socket_action)), or a custom
program/script ([`exec_action`](api.html#api.exec_action)). The API reference
includes details about the specific criteria that determine success for each
probe type.

You can configure a `local_resource` with an HTTP GET readiness probe for the
`serve_cmd` as follows:

    
    
    local_resource(
       "probe-example",
       serve_cmd="./myserver --port=8001",
       readiness_probe=probe(
          period_secs=15,
          http_get=http_get_action(port=8001, path="/health")
       )
    )
    

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/local_resource.md)







### Was this doc helpful?

Yes No

