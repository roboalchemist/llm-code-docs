# Tilt Documentation
# Source: https://docs.tilt.dev/example_csharp.html
# Path: example_csharp.html

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

#  Example: C#

The best indicator of a healthy development workflow is a short feedback loop.

Kubernetes is a huge wrench in the works.

Letâs fix this.

In this example, weâre going to take you through a simple âhello worldâ
web server written in C# that uses [ASP.NET
Core](https://docs.microsoft.com/en-us/aspnet/core/?view=aspnetcore-3.1) as a
Model View Controller framework.

Weâll use Tilt to:

  * Run the server on Kubernetes
  * Measure the time from a code change to a new process
  * Optimize that time for faster feedback

This particular example server doesnât do much, but itâs useful to confirm
that Tilt is working as expected in your environment.

All the code is in this repo:

[tilt-example-csharp](https://github.com/tilt-dev/tilt-example-csharp)

To skip straight to the fully optimized setup, go to this subdirectory:

[Recommended Setup](https://github.com/tilt-dev/tilt-example-
csharp/tree/master/3-live-update)

# Step 0: The Simplest Deployment

Our server has only one page, and all it does is serve us an almost entirely
static HTML page:

    
    
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.RazorPages;
    using Microsoft.Extensions.Logging;
    
    namespace hello_tilt.Pages
    {
        public class IndexModel : PageModel
        {
            private readonly ILogger<IndexModel> _logger;
    
            public IndexModel(ILogger<IndexModel> logger)
            {
                _logger = logger;
            }
    
            public void OnGet()
            {
    
            }
        }
    }
    

To start this server on Kubernetes, we need three config files:

  1. A [Dockerfile](https://github.com/tilt-dev/tilt-example-csharp/blob/master/0-base/hello-tilt/Dockerfile) that builds the image
  2. A [Kubernetes deployment](https://github.com/tilt-dev/tilt-example-csharp/blob/master/0-base/kubernetes.yaml) that runs the image
  3. And finally, a [Tiltfile](https://github.com/tilt-dev/tilt-example-csharp/blob/master/0-base/Tiltfile) that ties them together:

    
    
    docker_build('hello-tilt', './hello-tilt')
    k8s_yaml('kubernetes.yaml')
    k8s_resource('hello-tilt', port_forwards='8080:80')
    

The first line tells Tilt to build an image with the name `hello-tilt` in the
directory `./hello-tilt`.

The second line tells Tilt to load the Kubernetes Deployment YAML. The image
name in the `docker_build` call must match the container `image` reference in
the `hello-tilt` Deployment.

The last line configures port-forwarding so that your server is reachable at
`localhost:8080`. The resource name in the `k8s_resource` call must match the
Deploymentâs `metadata.name`.

Try it! Run:

    
    
    git clone https://github.com/tilt-dev/tilt-example-csharp
    cd tilt-example-csharp/0-base
    tilt up
    

Tilt will open a browser showing the web UI, a unified view that shows you app
status and logs. Your terminal will also turn into a status box if youâd
like to watch your server come up there.

When the server is ready, you will see the status icon turn green. The log
pane will display:

    
    
    info: Microsoft.Hosting.Lifetime[0]
          Now listening on: http://[::]:
    

[ ![](assets/docimg/example-csharp-0-base.png)
](https://cloud.tilt.dev/snapshot/AeCx3ucLBiMYtPnPTuc=) The server is up!
(Click the screenshot to see an interactive view.)

## Step 1: Letâs Add Benchmark Trickery

Before we try to make this faster, letâs measure it.

Using [`local_resource`](local_resource.html), you can direct Tilt to execute
existing scripts or arbitrary shell commands on your own machine, and manage
them from your sidebar like any other Tilt resource. Weâre going to use this
functionality to benchmark our deploys.

First we add a `local_resource` to our [Tiltfile](https://github.com/tilt-
dev/tilt-example-csharp/blob/master/1-measure/Tiltfile) that records the start
time in a C# file.

    
    
    local_resource(
        'deploy',
        './record-start-time.sh',
        deps=['./record-start-time.sh']
    )
    

The `local_resource()` call creates a local resource named `deploy`. The
second argument is the script that it runs.

Weâve also modified our server to read that start itme, calculate the time
elapsed, then display this in the rendered HTML.

Letâs click the button on the `deploy` resource and see what happens!

[ ![](assets/docimg/example-csharp-image-2.png) ](https://cloud.tilt.dev/snapshot/AdKa5ucLVfFH0lRxn7I=) Step 1 complete. Click the screenshot to see an interactive snapshot Approach | Deploy Time1  
---|---  
Naive | 10.4s  
  
If you look closely, the elapsed time displayed in the Tilt sidebar is
different than the benchmark our app logged. Thatâs OK! In microservice
development there are many benchmarks we care about â the time to build the
image, the time to schedule the process, and the time until the server is
ready to serve traffic.

Tilt offers you some default benchmarks _and_ the tools to capture your own.

Our benchmarks show this is slow. Can we do better?

## Step 2: Letâs Optimize for the C# Toolchain

Whatâs taking up so much time? The logs show that when we make a change to a
file, we:

1) Copy the csproj file, run `dotnet restore` to install any dependencies 2)
Copy the rest of the code and run a build from scratch with `dotnet publish`
3) Copy the build output to the ASP.NET runtime image

But the C# community has done a lot of work to make caching dependendencies
and incremental compiles fast. How can we better use the tools how theyâre
meant to be used?

With `local_resource`, we can compile the project locally, and copy the build
output files to the container.

Hereâs our [new Tiltfile](https://github.com/tilt-dev/tilt-example-
csharp/blob/master/2-build-locally/Tiltfile) with the following new code:

    
    
    local_resource(
        'build',
        'dotnet publish -c Release -o out',
        deps=['hello-tilt'],
        ignore=['hello-tilt/obj'],
        resource_deps=['deploy'],
    )
    

Weâve added a `local_resource()` that compiles the executable locally with
`dotnet`.

Weâve adjusted the [Dockerfile](https://github.com/tilt-dev/tilt-example-
csharp/blob/master/2-build-locally/Dockerfile) so that it only includes the
build output under `out`:

    
    
    FROM mcr.microsoft.com/dotnet/core/aspnet:3.1
    COPY . /app/out
    WORKDIR /app/out
    ENTRYPOINT ["dotnet", "hello-tilt.dll"]
    

We also modified the context that we pass the `docker_build` call to only
include the output directory:

    
    
    docker_build('hello-tilt', 'out', dockerfile='Dockerfile')
    

Letâs see what this looks like!

[ ![](assets/docimg/example-csharp-image-3.png) ](https://cloud.tilt.dev/snapshot/AdC35ucLJSe0a4XNTFc=) Step 2 complete. Click the screenshot to see an interactive snapshot Approach | Deploy Time  
---|---  
Naive | 10.4s  
Local Compile | 8.2s  
  
# Step 3: Letâs Live Update It

When we make a change to a file, we currently have to build an image, deploy
new Kubernetes configs, and wait for Kubernetes to schedule the pod.

With Tilt, we can skip all of these steps, and instead `live_update` the pod
in place.

Hereâs our [new Tiltfile](https://github.com/tilt-dev/tilt-example-
csharp/blob/master/3-live-update/Tiltfile) with the following new code:

    
    
    load('ext://restart_process', 'docker_build_with_restart')
    ...
    docker_build_with_restart(
        'hello-tilt',
        'out',
        entrypoint=['dotnet', 'hello-tilt.dll'],
        dockerfile='Dockerfile',
        live_update=[
            sync('out', '/app/out'),
        ],
    )
    

The first thing to notice is the `live_update` parameter, which consists of
one `sync` step. This copies the build output from the `out` directory into
the container.

After syncing the files, we want to restart our updated binary.

In this example, we restart the binary with the [`restart_process`
extension](https://github.com/tilt-dev/tilt-
extensions/tree/master/restart_process), which we imported with the `load`
call on the first line. We swap out our `docker_build` call for the
`docker_build_with_restart` function we imported: itâs almost exactly the
same as `docker_build`, only it knows to restart our process at the end of a
`live_update`. The `entrypoint` parameter specifies what command to re-
execute.

The `restart_process` extension is a lowest-common-denominator reload tool.
Tiltâs `live_update` API tries to be flexible enough so that you can use
native hot reload support if your framework supports it. If you have more
examples for specific frameworks, weâd be happy to add them to [the example
repo](https://github.com/tilt-dev/tilt-example-csharp).

Letâs see what this new configuration looks like in action:

[ ![](assets/docimg/example-csharp-image-4.png)
](https://cloud.tilt.dev/snapshot/AYSC5-cLzxRU0Wiuvrg=) Step 3 complete. Click
the screenshot to see an interactive snapshot

Tilt was able to update the container in less than 5 seconds!

## Our Recommendation

### Final Score

Approach | Deploy Time  
---|---  
Naive | 10.4s  
Local Compile | 8.2s  
With live_update | 4.8s  
  
You can try the server here:

[Recommended Structure](https://github.com/tilt-dev/tilt-example-
csharp/tree/master/3-live-update)

Congratulations on finishing this guide!

## Further Reading

### CI

Once youâre done configuring your project, set up a CI test to ensure your
setup doesnât break! In the example repo, CircleCI uses
[`ctlptl`](https://github.com/tilt-dev/ctlptl) to create a single-use
Kubernetes cluster. The test script invokes `tilt ci`. The `tilt ci` command
deploys all services in a Tiltfile and exits successfully if theyâre
healthy.

  * [CircleCI config](https://github.com/tilt-dev/tilt-example-csharp/blob/master/.circleci/config.yml)
  * [Test script](https://github.com/tilt-dev/tilt-example-csharp/blob/master/test/test.sh)

### Examples in other languages:

  * [Plain Old Static HTML](/example_static_html.html)
  * [Go](/example_go.html)
  * [NodeJS](/example_nodejs.html)
  * [Python](/example_python.html)
  * [Java](/example_java.html)
  * [Bazel](/example_bazel.html)

  1. Tiltâs first deployment of a service takes a few seconds longer than subsequent ones, due to some behind-the-scenes setup. Measurements in this guide focus on non-initial builds.Â ↩

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/example_csharp.md)







### Was this doc helpful?

Yes No

