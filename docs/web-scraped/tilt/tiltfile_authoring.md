# Tilt Documentation
# Source: https://docs.tilt.dev/tiltfile_authoring.html
# Path: tiltfile_authoring.html

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

#  Writing Your First Tiltfile

> ðï¸ **Need more direct guidance?**  
>  Check out our new [Editor Support page](./editor.html)

This tutorial walks you through setting up Tilt for your project.

It should take 15 minutes, and assumes youâve already [installed
Tilt](install.html). Before you begin, you may want to join the `#tilt`
channel in [Kubernetes Slack](http://slack.k8s.io) for technical and moral
support.

Start by `cd`âing into a project you can already build and deploy to
Kubernetes.

## Example Tiltfile

A Tiltfile configures tilt and is written in
[Starlark](https://docs.bazel.build/versions/main/skylark/language.html), a
simplified dialect of Python.

At the end of this guide, your Tiltfile will look something like this:

    
    
    # Deploy: tell Tilt what YAML to deploy
    k8s_yaml('app.yaml')
    
    # Build: tell Tilt what images to build from which directories
    docker_build('companyname/frontend', 'frontend')
    docker_build('companyname/backend', 'backend')
    # ...
    
    # Watch: tell Tilt how to connect locally (optional)
    k8s_resource('frontend', port_forwards=8080)
    

But donât create it yet; weâll be exploring how it works in the following
sections.

## Hello World

In your terminal, run `tilt up`. Tilt will offer to create a starter
`Tiltfile` for you. For the sake of this tutorial, we will decline by entering
`n`.

Hit `space` and a browser tab will open showing Tilt. Instead of writing your
Tilt configuration all at once, weâll use Tilt interactively. Each time you
save your configuration, Tilt will reexecute it.

Right now, Tilt should be complaining that thereâs no file named `Tiltfile`.

![No Tiltfile](/assets/img/no-tiltfile.png)

Create a new file named `Tiltfile` (note the capitalization) in your project
directory with a single line:

    
    
    print('Hello Tiltfile')
    

Now save the file. Congrats, you just ran your first Tiltfile since Tilt has
automatically reexecuted with it. Tiltâs configurations are programs in
[Starlark](https://github.com/bazelbuild/starlark#tour), a dialect of Python.
Go back to your browser to see âHello Tiltfileâ in Tilt. Tilt is also
warning you there are no declared resources. Letâs add some.

## Step 1: Deploy

The [Tiltfile API](api.html) function [`k8s_yaml`](api.html#api.k8s_yaml)
registers Kubernetes objects you want to deploy:

    
    
    k8s_yaml('app.yaml')
    

Tilt supports many deployment configuration practices (for more details, check
out the [Deploy](tiltfile_concepts.html#deploy) section of âTiltfile
Conceptsâ):

    
    
    # multiple YAML files; can be either a list or multiple calls
    k8s_yaml(['foo.yaml', 'bar.yaml'])
    
    # run a command to generate YAML
    k8s_yaml(local('gen_k8s_yaml.py')) # a custom script
    k8s_yaml(kustomize('config_dir')) # built-in support for popular tools
    k8s_yaml(helm('chart_dir'))
    

Use the pattern that matches your project (if youâre not sure, feel free to
ask in [Slack](index.html#community)). You can see when it works because Tilt
will display the registered objects.

## Step 2: Build

The function [`docker_build`](api.html#api.docker_build) tells Tilt how to
build a container image. Tilt automatically builds the image, injects the ID
into Kubernetes objects and deploys. (The
[Build](tiltfile_concepts.html#build) section of âTiltfile Conceptsâ
describes optional arguments.)

    
    
    # docker build -t companyname/frontend ./frontend
    docker_build('companyname/frontend', 'frontend')
    

Try editing a source file; you should see Tilt automatically build and deploy
as soon as you save. Add additional images; you should have one `docker_build`
call for each container image youâre developing.

## Step 3: Watch (Optional)

Tilt can give you consistent port forwards to running pods (whether theyâre
running locally or in the cloud). Call the function
[`k8s_resource`](api.html#api.k8s_resource) with the name of the resource you
want to access (taken from the UI):

    
    
    k8s_resource('frontend', port_forwards='9000')
    

(Note that the first parameter of `k8s_resource` must match the name of a pod-
having k8s object that was passed to `k8s_yaml`. If youâd like to name it
something else you can use the [`new_name`
parameter](api.html#api.k8s_resource) to change its name.)

You can also use `k8s_resource` to forward multiple ports. Cf. the
[Resources](tiltfile_concepts.html#resources) section of `Tiltfile Concepts`.

## Congrats

Tilt is now setup for your project. Explore Tilt further. Introduce a build
error and then a runtime crash; see Tilt respond and surface the relevant
problem.

## Next Steps

If you had any trouble using this guide, nowâs a great time to [file bugs or
feature requests](https://github.com/tilt-dev/tilt/issues).

If youâd like to see examples in your programming language, we have example
projects for:

  * [Plain Old Static HTML](/example_static_html.html)
  * [Go](/example_go.html)
  * [NodeJS](/example_nodejs.html)
  * [Python](/example_python.html)
  * [Java](/example_java.html)
  * [C#](/example_csharp.html)
  * [Bazel](/example_bazel.html)

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/tiltfile_authoring.md)







### Was this doc helpful?

Yes No

