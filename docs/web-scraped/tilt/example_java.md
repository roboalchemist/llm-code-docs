# Tilt Documentation
# Source: https://docs.tilt.dev/example_java.html
# Path: example_java.html

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

#  Example: Java

The best indicator of a healthy development workflow is a short feedback loop.

Kubernetes is a huge wrench in the works.

Letâs fix this.

In this example, weâre going to take you through a simple server that uses
[Spring Boot](https://spring.io/projects/spring-boot) and templates to serve
HTML. Our example is loosely based on [Serving Web Content with Spring
MVC](https://spring.io/guides/gs/serving-web-content/).

Weâll use Tilt to:

  * Run the server on Kubernetes
  * Measure the time from a code change to a new process
  * Optimize that time for faster feedback

All the code is in this repo:

[tilt-example-java](https://github.com/tilt-dev/tilt-example-java)

To skip straight to the fully optimized setup, go to this subdirectory:

[Recommended Setup](https://github.com/tilt-dev/tilt-example-
java/blob/master/4-recommended)

## Step 0: The Simplest Deployment

Our server uses Spring Web for routing requests.

    
    
    package dev.tilt.example;
    
    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestParam;
    
    @Controller
    public class IndexController {
    
      @GetMapping("/")
      public String index(Model model) {
        // Serves the index.html template under
        // src/main/resources/templates/index.html
        return "index";
      }
    
    }
    

To start this server on Kubernetes, we need three config files:

1) A [Dockerfile](https://github.com/tilt-dev/tilt-example-
java/blob/master/0-base/Dockerfile) that builds the image

2) A [Kubernetes deployment](https://github.com/tilt-dev/tilt-example-
java/blob/master/0-base/kubernetes.yaml) that runs the image

3) And finally, a [Tiltfile](https://github.com/tilt-dev/tilt-example-
java/blob/master/0-base/Tiltfile) that ties them together:

    
    
    docker_build('example-java-image', '.')
    k8s_yaml('kubernetes.yaml')
    k8s_resource('example-java', port_forwards=8000)
    

The first line tells Tilt to build an image with the name `example-java-image`
in the current directory.

The second line tells Tilt to load the Kubernetes
[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-
a-deployment) YAML. The image name in the `docker_build` call must match the
container `image` reference in the `example-java` Deployment.

The last line configures port-forwarding so that your server is reachable at
`localhost:8000`. The resource name in the `k8s_resource` call must match the
Deploymentâs `metadata.name` in `kubernetes.yaml`.

Try it! Run:

    
    
    git clone https://github.com/tilt-dev/tilt-example-java
    cd tilt-example-java/0-base
    tilt up
    

Tilt will open a browser showing the web UI, a unified view that shows you app
status and logs. Your terminal will also turn into a status box if youâd
like to watch your server come up there.

When itâs ready, you will see the status icon turn green. The logs in the
bottom pane will display âTomcat initialized with port(s): 8000.â

[ ![](assets/docimg/example-java-image-1.png)
](https://cloud.tilt.dev/snapshot/AfbdiucLHi33cqQwrG4=) The server is up!
(Click the screenshot to see an interactive view.)

## Step 1: Letâs Add Benchmark Trickery

Before we try to make this faster, letâs measure it.

Using [`local_resource`](local_resource.html), you can direct Tilt to execute
existing scripts or arbitrary shell commands on your own machine, and manage
them from your sidebar like any other Tilt resource. Weâre going to use this
functionality to benchmark our deployments.

First, we add a `local_resource` to our [Tiltfile](https://github.com/tilt-
dev/tilt-example-java/blob/master/1-measured/Tiltfile) that records the start
time in a Java file.

    
    
    k8s_resource(
        'example-java', 
        port_forwards=8000, 
        resource_deps=['deploy'])
    
    # Records the current time, then kicks off a server update.
    # Normally, you would let Tilt do deploys automatically, but this
    # shows you how to set up a custom workflow that measures it.
    local_resource(
        'deploy',
        './record-start-time.sh',
    )
    

The `local_resource()` call creates a local resource named `deploy`. The
second argument is the script that it runs.

Weâve also modified our server to read that start time, calculate the time
elapsed, then display this in both logs and HTML.

Letâs click the button on the `deploy` resource and see what happens!

[ ![](assets/docimg/example-java-image-2.png) ](https://cloud.tilt.dev/snapshot/AeDqiucLr-00XLJpiWc=) Clicking the button triggers the 'deploy' local_resource, which in turn kicks off an update to the server. (Click the screenshot to see an interactive view.) Approach | Deploy Time1  
---|---  
Naive | 87.7s  
  
If you look closely, the elapsed time displayed in the Tilt sidebar is
different than the benchmark our app logged. Thatâs OK! In microservice
development, there are many benchmarks we care about â the time to build the
image, the time to schedule the process, and the time until the server is
ready to serve traffic.

Tilt offers you some default benchmarks, _and_ the tools to capture your own.

Our benchmarks show this is slow. Can we do better?

## Step 2: Letâs Optimize for the Java Toolchain

Whatâs taking up so much time? The logs show that when we make the change to
a file, we:

1) Copy the source files to the image.

2) Download Gradle.

3) Download all the Spring dependencies.

4) Compile the Java jar from scratch.

But the Java community has done a lot of work to make caching dependencies and
incremental compiles fast. How can we better use the tools how theyâre meant
to be used?

With `local_resource`, we can compile the executable Jar locally, and copy it
to the container.

Hereâs our [new Tiltfile](https://github.com/tilt-dev/tilt-example-
java/blob/master/2-optimized/Tiltfile) with the following new code:

    
    
    local_resource(
      'example-java-compile',
      './gradlew bootJar',
      deps=['src', 'build.gradle'],
      resource_deps = ['deploy'])
      
    docker_build(
      'example-java-image',
      './build/libs',
      dockerfile='./Dockerfile')
    

Weâve added a `local_resource()` that compiles the executable Jar locally
with Gradle.

Weâve adjusted the Docker context so that it only includes the build
artifacts under `./build/libs`.

Finally, weâve modified the Dockerfile to only copy the executable jar.

Letâs see what this looks like!

[ ![](assets/docimg/example-java-image-3.png) ](https://cloud.tilt.dev/snapshot/AabuiucL7NKgfiTa1uI=) Step 2 complete. (Click the screenshot to see an interactive snapshot.) Approach | Deploy Time  
---|---  
Naive | 87.7s  
Local Compile | 13.4s  
  
## Step 3: Why Is the Docker Build So Slow?

Currently, our image contains a fat executable Jar.

If we unpacked the fat Jar, we would find that the Jar contains many files
internally. These files naturally lend themselves to Docker layers. Java Jars
were using layer caches before Docker made them cool. How can we take
advantage of this?

Weâve updated [our Tiltfile](https://github.com/tilt-dev/tilt-example-
java/blob/master/3-unpacked/Tiltfile) to unpack the Jar in the `build/jar`
directory:

    
    
    local_resource(
      'example-java-compile',
      './gradlew bootJar && ' +
      'unzip -o build/libs/example-0.0.1-SNAPSHOT.jar -d build/jar',
      deps=['src', 'build.gradle'],
      resource_deps = ['deploy'])
    

Weâve also updated our [Dockerfile](https://github.com/tilt-dev/tilt-
example-java/blob/master/3-unpacked/Dockerfile):

    
    
    FROM eclipse-temurin:17-jre-alpine
    
    WORKDIR /app
    ADD BOOT-INF/lib /app/lib
    ADD META-INF /app/META-INF
    ADD BOOT-INF/classes /app
    
    ENTRYPOINT java -cp .:./lib/* dev.tilt.example.ExampleApplication
    

This Dockerfile adds files from `build/jar` in order from least frequently
used to most frequently used, to improve caching.

The Dockerfile also has a new the entrypoint to load the main application
class, since weâre no longer using an executable Jar.

Letâs see what this looks like!

[ ![](assets/docimg/example-java-image-4.png) ](https://cloud.tilt.dev/snapshot/AcaQnucLOBUS4TGQauw=) Step 3 complete. (Click the screenshot to see an interactive snapshot.) Approach | Deploy Time  
---|---  
Naive | 87.7s  
Local Compile | 13.4s  
Optimized Dockerfile | 6.5s  
  
If you donât want to optimize the Dockerfile yourself, check out
[Jib](https://github.com/GoogleContainerTools/jib)!

Jib is a Java image builder that re-packs Java Jars as container images using
similar tricks. There are Jib plugins for Maven and Gradle. The [tilt-example-
java](https://github.com/tilt-dev/tilt-example-java) repo has an example
[Tiltfile](https://github.com/tilt-dev/tilt-example-
java/blob/master/101-jib/Tiltfile) that uses `custom_build` to generate images
with Jib.

## Step 4: Letâs Live Update It

When we make a change to a file, we currently have to build an image, deploy
new Kubernetes configs, and wait for Kubernetes to schedule the pod.

With Tilt, we can skip all of these steps, and instead `live_update` the pod
in place.

Hereâs our [new Tiltfile](https://github.com/tilt-dev/tilt-example-
java/blob/master/4-recommended/Tiltfile) with the following new code:

    
    
    load('ext://restart_process', 'docker_build_with_restart')
    ...
    local_resource(
      'example-java-compile',
      gradlew + ' bootJar && ' +
      'unzip -o build/libs/example-0.0.1-SNAPSHOT.jar -d build/jar-staging && ' +
      'rsync --inplace --checksum -r build/jar-staging/ build/jar',
      deps=['src', 'build.gradle'],
      resource_deps = ['deploy'])
    
    docker_build_with_restart(
      'example-java-image',
      './build/jar',
      entrypoint=['java', '-noverify', '-cp', '.:./lib/*', 'dev.tilt.example.ExampleApplication'],
      dockerfile='./Dockerfile',
      live_update=[
        sync('./build/jar/BOOT-INF/lib', '/app/lib'),
        sync('./build/jar/META-INF', '/app/META-INF'),
        sync('./build/jar/BOOT-INF/classes', '/app'),
      ],
    )
    

The first thing to notice is the `live_update` parameter, which consists of
some `sync` steps. They copy the library and compiled `.class `files from the
`./build/jar` directory into the container.

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
repo](https://github.com/tilt-dev/tilt-example-java).

Lastly, our `local_resource` first unzips the jar to `build/jar-staging`, and
then uses `rsync --checksum` to copy that to `build/jar`. Tiltâs live_update
will copy any files that have been touched. `rsync --checksum` copies the
directory, but doesnât touch any files that havenât changed.

Letâs see what this new configuration looks like in action:

[ ![](assets/docimg/example-java-image-5.png)
](https://cloud.tilt.dev/snapshot/AeKPnucLESM6hHyx8HY=) The result of a
live_update. (Click the screenshot to see an interactive view.)

Tilt was able to update the container in less than 5 seconds!

## Our Recommendation

### Final Score

Approach | Deploy Time  
---|---  
Naive | 87.7s  
Local Compile | 13.4s  
Optimized Dockerfile | 6.5s  
With live_update | 4.8s  
  
You can try the server here:

[Recommended Structure](https://github.com/tilt-dev/tilt-example-
java/blob/master/4-recommended)

Congratulations on finishing this guide!

## Further Reading

### CI

Once youâre done configuring your project, set up a CI test to ensure your
setup doesnât break! In the example repo, CircleCI uses
[`ctlptl`](https://github.com/tilt-dev/ctlptl) to create a single-use
Kubernetes cluster. The test script invokes `tilt ci`. The `tilt ci` command
deploys all services in a Tiltfile and exits successfully if theyâre
healthy.

  * [CircleCI config](https://github.com/tilt-dev/tilt-example-java/blob/master/.circleci/config.yml)
  * [Test script](https://github.com/tilt-dev/tilt-example-java/blob/master/test/test.sh)

### Optimizations

This guide recommends an approach to Java development that shines with Tilt.

There are even more optimizations you can add. Many are toolchain-specific.
Weâve heard that you can get the JVM to hot-reload class files (e.g. with
[Spring Loaded](https://github.com/spring-projects/spring-loaded)) but weâve
had mixed results using this with live_update.

For more discussion of build optimization, see:

  * [Spring Boot Docker](https://spring.io/guides/topicals/spring-boot-docker/), a discussion of how to better optimize Spring Boot apps for Docker. We used many of the lessons in this guide. There are still more tricks for improving performance in containers.
  * Tiltâs [Java Examples repo](https://github.com/tilt-dev/tilt-example-java/), which besides the code from this guide, contains examples of how to use Tilt with a number of different Java tools, including: 
    * [Jib](https://github.com/GoogleContainerTools/jib), a Java image builder that re-packs Java Jars as container images, and integrates well with existing Maven or Gradle builds ([example here](https://github.com/tilt-dev/tilt-example-java/blob/master/101-jib/Tiltfile)).
    * [Quarkus](https://quarkus.io/), a container-first, hot-reloading framework for writing Java applications ([example here](https://github.com/tilt-dev/tilt-example-java/tree/master/201-quarkus-live-update)).

### Examples in other languages:

  * [Plain Old Static HTML](/example_static_html.html)
  * [Go](/example_go.html)
  * [NodeJS](/example_nodejs.html)
  * [Python](/example_python.html)
  * [C#](/example_csharp.html)
  * [Bazel](/example_bazel.html)

  1. Tiltâs first deployment of a service takes a few seconds longer than subsequent ones, due to some behind-the-scenes setup. Measurements in this guide focus on non-initial builds.Â ↩

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/example_java.md)







### Was this doc helpful?

Yes No

