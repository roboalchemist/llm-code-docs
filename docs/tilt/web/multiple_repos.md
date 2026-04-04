# Tilt Documentation
# Source: https://docs.tilt.dev/multiple_repos.html
# Path: multiple_repos.html

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

#  Many Tiltfiles and Many Repos

Most of our example projects use a single Tiltfile. All the source files,
Dockerfiles, and Kubernetes configs are in a single folder.

But your project may be organized differently!

## How to Organize Your Project for Tilt

Tilt does not require a particular project structure. We try to provide APIs
to help you pull the services you need into your dev environment, no matter
where theyâre defined.

> > Do NOT restructure your project for Tilt. Instead, restructure your
> Tiltfiles to match your project structure!

Weâve seen many patterns, including:

  * One main Tiltfile that subincludes a subdirectory Tiltfile for each service.

  * Individual service Tiltfiles that include a library of common functions.

  * Conditional loading of sets of services based on what you have checked out.

  * Loading some services for editing and some services for running read-only.

  * Loading prebuilt services from other repos.

  * Checking out git repos or git submodules from the Tiltfile.

In this doc, weâll take a tour of the APIs that make these patterns
possible.

## Loading Library Functions

Suppose you have two services that share dev conventions. Maybe you run them
together sometimes! Or maybe you donât. But you want to factor out common
logic for setting up their dev environment.

This is where [`load()`](api.html#api.load) can help. You can use it to load
shared constants or functions from a relative path:

    
    
    load('../common/Tiltfile', 'VERSION', 'common_config_yaml')
    
    print('Loading version: ', VERSION)
    k8s_yaml(common_config_yaml())
    

## Loading sub-Tiltfiles

Another pattern is where two services have independent Tiltfiles. But
sometimes you want to load them together!

The [`include()`](api.html#api.include) function loads files that donât
export any helper functions.

    
    
    include('./frontend/Tiltfile')
    include('./backend/Tiltfile')
    

## Loading Services Conditionally

We have an example project with an auth service. Sometimes we want to run it
with fake user data. Sometimes we want to run it with real GitHub OAuth login.
Sometimes we want to run it with HTTPS instead of HTTP.

The [`load_dynamic()`](api.html#api.load_dynamic) function doesnât have the
nice syntax for loading constants, but does give you the flexibility to
conditionally load services.

Hereâs [an example](https://github.com/tilt-
dev/ephemerator/blob/3f4c3c7d045f1f012ad70afe3907c83b5645d565/ephconfig/Tiltfile)
that uses `os.path.exists` to see if you have OAuth client secrets or
localhost HTTPS certificates. If you do, it uses the real GitHub OAuth login
server. Otherwise, it uses fake user data.

    
    
    USE_OAUTH2 = os.path.exists('../.secrets/values-dev.yaml')
    USE_TLS = False
    if USE_OAUTH2:
      symbols = load_dynamic('../oauth2-proxy/Tiltfile')
      USE_TLS = symbols['USE_TLS']
    

## Configuring to-run vs to-edit Services

As you have more services, you may need to run subsets of them.

One way to handle this is to have a Tiltfile for each common configuration.

Other teams load all the services in a single Tiltfile, then add controls to
enable/disable sets of them.

Tilt has some built-in support for this!

  * `tilt enable a b`: enable service âaâ and âbâ
  * `tilt enable --only a b`: enable âaâ and âbâ, and disables all others
  * `tilt enable --all`: enable all services
  * `tilt disable a b`: disable âaâ and âbâ
  * `tilt disable --all`: disable all services

For more complicated configurations, you can define your own flags to `tilt
up` to specify sets of services to run or to edit. For more examples, see the
[per-user config guide](tiltfile_config.html).

## Managing other git Repositories

The simplest way to handle multi-repository projects is to ask the user to
check out other repos as a sibling directory.

    
    
    if not os.path.exists('../backend'):
      fail('Please "git clone" the backend repo in ../backend!')
      
    include('../backend/Tiltfile')
    

You can also supply the repository as an environment variable.

    
    
    backend_dir = os.environ.get('BACKEND_REPO_DIR', '../backend')
    if not os.path.exists(backend_dir):
      fail('Please "git clone" the backend repo in %s!' % backend_dir)
      
    include(os.path.join(backend_dir, 'Tiltfile'))
    

Many sophisticated projects use this approach, including [the ClusterAPI
project](https://cluster-api.sigs.k8s.io/developer/core/tilt.html) for loading
servers for each host they deploy to!

Other teams in the Tilt community handle multi-repo projects directly from
their Tiltfile. The `git_resource` extension has functions for checking out
arbitrary repos and deploying the resources they contain.

    
    
    load('ext://git_resource', 'git_checkout')
    git_checkout('git@github.com:tilt-dev/tilt-example-html.git#master', '/path/to/local/checkout')
    

Go to the [`git_resource` README](https://github.com/tilt-dev/tilt-
extensions/tree/master/git_resource) for more details.

## Managing Extension Repositories

Finally, Tilt has a set of community-contributed extensions in [the `tilt-
extensions` repo](https://github.com/tilt-dev/tilt-extensions).

The community extensions contain both common functions to define your dev
environment, and common servers you may want to use.

Many teams manage their own extension repos for extensions that are specific
to their orgs! You can read more about how to use them in the [Extensions
Guide](./extensions.html).

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/multiple_repos.md)







### Was this doc helpful?

Yes No

