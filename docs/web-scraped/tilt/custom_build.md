# Tilt Documentation
# Source: https://docs.tilt.dev/custom_build.html
# Path: custom_build.html

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

#  Custom Image Builders

`docker build` is the common way to build container images, but there are many
others.

This guide will show you how to use them!

## The Easiest Way: Use a Tilt Extension

The Tilt community has contributed many extensions that let you define your
container images with many widely-used image builders.

The `tilt-example-builders` repo demonstrates how to use them.

[tilt-example-builders](https://github.com/tilt-dev/tilt-example-builders)

Each subdirectory of the repo uses a different image builder.

Each builder contains a test that spins up a real, ephemeral Kubernetes
cluster on CircleCI, builds the image, deploys it to the cluster, and verifies
that the image behaves as expected.

Also check out the [complete index of Tilt
extensions](https://github.com/tilt-dev/tilt-extensions). There are many more
image builder extensions that donât have official example projects yet.

## The Next Way: Running Your Own Image Builder

If thereâs no extension yet for your image builder, thatâs OK.

All image-builder extensions use the
[`custom_build`](api.html#api.custom_build) function, a more complete API for
running your image builds as subprocesses of Tilt.

Letâs take a look at how to use it.

### Usage

All `custom_build` calls require:

  * A name of the image to build (as a ref, e.g. `frontend` or `gcr.io/company-name/frontendâ)

  * A command to run (e.g. `bazel build //frontend:image` or `build_frontend.sh`)

  * Files to watch (e.g. `['frontend']` or `['frontend', 'util', 'data.txt']`). When a dependency changes, Tilt starts an update to build the image then apply the YAML.

There are a couple different image-building patterns.

### Custom Docker Builds

Suppose you have a script that wraps `docker build`, but adds some
application-specific abstractions.

Hereâs a simple example that invokes `docker build` to build an image named
`frontend` from the directory `frontend`:

    
    
    custom_build(
      'frontend',
      'docker build -t $EXPECTED_REF frontend',
      ['./frontend'],
    )
    

Tilt will run this command to build the image, verify that the image is in the
Docker image store, then push the image to the appropriate image registry.

You can also use this pattern to use `docker` flags that the `docker_build()`
function doesnât support.

### Jib, Bazel, or any other builder that interoperates with Docker

Many tools can create Docker images, then write them to the local Docker image
store.

For example, [Jib](https://github.com/GoogleContainerTools/jib) has plugins
that integrate with your existing Java tooling and create Java-based images.

The [tilt-example-java](https://github.com/tilt-dev/tilt-example-java) repo
has an example [Tiltfile](https://github.com/tilt-dev/tilt-example-
java/blob/master/101-jib/Tiltfile) that uses `custom_build` to generate images
with Gradle and Jib:

    
    
    custom_build(
      'example-java-image',
      './gradlew jibDockerBuild --image $EXPECTED_REF',
      deps=['src'])
    

[Bazel](https://github.com/google/bazel), the general-purpose build system,
also takes this approach. Bazelâs
[rules_docker](https://github.com/bazelbuild/rules_docker) extension assembles
Docker images and writes them to the local Docker image store.

See the tutorial on how to use `custom_build` to [build images with
Bazel](integrating_bazel_with_tilt.html).

### Buildah (or any image builder independent of Docker)

[Buildah](https://buildah.io/) is an independent Docker image builder.

Buildah has its own API and own image store. A `custom_build()` call needs to
both build and push the image.

    
    
    custom_build(
      'frontend',
      'buildah bud -t $EXPECTED_REF frontend && buildah push $EXPECTED_REF $EXPECTED_REF',
      ['./frontend'],
      skips_local_docker=True,
    )
    

The `skips_local_docker` parameter indicates that we donât expect the image
to ever show up in the local Docker image store. Tilt shouldnât try to
verify the image locally.

There are a couple of caveats you should be aware of with `buildah` (and
similar builders):

  * They often require privileged access. You may need to run Tilt with `sudo` or inside an appropriate sandbox

  * If youâre using Tilt to push to an insecure registry, you will need to configure your builder for that registry. For example, to use `buildah` with Microk8s, you need to add `localhost:32000` to [registries.insecure](https://github.com/containers/buildah/blob/master/install.md#registriesconf).

## How to Write Your Own

Weâve looked at a couple simple recipes for how to write a custom build
script.

To write more complex ones, we need to understand in more detail how they
work.

All the commands above contain `$EXPECTED_REF`. What is that?

Tilt always pushes a content-based, immutable tag, not a bare ref. (Instead of
`gcr.io/company-name/frontend`, Tilt injects `gcr.io/company-
name/frontend:tilt-ffd9c2013b5bf5d4`, where the `ffd9c2013b5bf5d4` part is
based on the contents of your image). Before explaining why (see below),
letâs describe what this means for your Tiltfile and build script.

There are two ways for Tilt and your build script to coordinate image builds.

### The Good Way

Most tools take a destination of the image as an argument (e.g. `docker
build`).

  * Before running your build script, Tilt sets the environment variable `$EXPECTED_REF` with a randomized tag (e.g. `EXPECTED_REF=gcr.io/company-name/frontend:tilt-12345`).

  * The custom build script builds the image and tags it with `$EXPECTED_REF`.

  * After the build script exits, Tilt reads the new image at `$EXPECTED_REF`, re-tags it with a content-based tag, and pushes it to the image registry.

### The Hacky Way

Other tools have an image ref hard-coded in configuration. Theyâll build to
the same tag each time.

Instead of writing a wrapper script around your tool, tell Tilt what tag the
build image will have with `custom_build(..., tag='gcr.io/company-
name/frontend:dev')`.

After Tilt runs your build command, it will find this image and retag and push
it with a content-based tag.

This method is generally less robust, because the script is building to a
mutable tag instead of an immutable tag.

### An Improvement on the Hacky Way

If youâre willing to invest more into your custom build script, you should
use content-based tags!

`custom_build(outputs_image_ref_to='ref.txt')` will tell Tilt that your custom
build script intends to write a tagged image reference to the file `ref.txt`.

Tilt will then inject that image into your deployments.

If Tilt has detected a local registry, it will populate the environment
variable `REGISTRY_HOST` (e.g., `REGISTRY_HOST=localhost:5000`) before calling
the build script.

### Determining the Content-based Tag

In rare cases, another script in your build system may need to know what tag
Tilt is going to deploy. This typically only comes up if your team has written
their own artisanal image build system thatâs closely coupled with
Kubernetes.

Tilt has a special command to help with this. After you build the image, run:

    
    
    tilt dump image-deploy-ref $EXPECTED_REF
    

Tilt will read the image, determine the hash of the context, and print out the
full name and content-based tag.

**NOTE:** This is not a common use-case. Usually, when teams ask about this,
theyâre writing a workflow engine that creates its own pods (like Airflow),
and need a way to get the deploy tag at runtime. So they hack custom_build to
grab the deploy tag at build-time, and plumb it through to their runtime pods.
Thereâs a better way to do this. Use [this
guide](custom_resource.html#advanced-pod-creation) instead.

## Live Update and Other Features

Tiltâs `docker_build` supports other options. The most impactful is
`live_update`, which lets you update code in Kubernetes without doing a full
image build. `custom_build` supports this as well, using the same syntax.

`custom_build` supports most other options of `docker_build`, and a few
specific to non-Docker container builders.

### Adjust File Watching with `ignore`

While most of the points in our [Debugging File Changes](/file_changes.html)
guide hold true for `custom_build`, the `ignore` parameter (which adjusts the
set of files watched for a given build) works a bit differently, and is worth
discussing briefly.

The `ignore` parameter takes a pattern or list of patterns (following
[`.dockerignore`
syntax](https://docs.docker.com/engine/reference/builder/#dockerignore-file);
files matching any of these patterns will _not_ trigger a build.

Of note, these patterns are evaluated relative to each `dep`. E.g. given the
following call:

    
    
    custom_build(
        'image-foo',
        'docker build -t $EXPECTED_REF .',
        deps=['dep1', 'dep2'],
        ignore=['baz']
    )
    

Tilt will ignore `dep1/baz` and `dep2/baz`.

## Why Tilt uses Immutable Tags

Immutable tags have a long history in the Kubernetes community.

The Knative team has this presentation that gives a good overview: [Why we
resolve tags in
Knative](https://docs.google.com/presentation/d/1gjcVniYD95H1DmGM_n7dYJ69vD9d6KgJiA-D9dydWGU/edit?usp=sharing)
(join [`knative-
users@googlegroups.com`](https://groups.google.com/d/forum/knative-users) for
access).

Mutable tags have good usability and security properties. For example, a
`registry:v2` image that has the latest, most secure minor version of the v2
major version.

Immutable tags have good reliability and caching properties. For example, if
youâre rolling out 3 pods of `registry:v2`, you want to be sure all pods
have the exact same version. Deploying with a mutable reference creates a race
condition. Pods created at different times from the same definition may end up
running different code as the reference is overwritten.

Tilt only deploys immutable tags. Instead of pushing to `gcr.io/company-
name/frontend`, Tilt re-tags the image as `gcr.io/company-name/frontend:tilt-
ffd9c2013b5bf5d4`. The unique bit is a
[Nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce) or a digest of the
contents. (Technically the tag isnât write-protected in any way, but the
improbability of collisions means we can pretend itâs immutable.)

Tilt then injects the new tag into the container spec. This makes the Tilt
experience faster and more reliable, because we can instruct Kubernetes to
cache the tag aggressively as if itâs immutable.

Knative uses [a similar strategy](https://knative.dev/docs/serving/tag-
resolution/), but the immutability is enforced by a Kuberentes operator,
instead of by client-side tooling.

## When Youâre Done

If you have a more complex build script that youâre not sure how to
integrate with Tilt, weâd love to hear about it. Come find us in the `#tilt`
channel in [Kubernetes Slack](http://slack.k8s.io) or [file an
issue](https://github.com/tilt-dev/tilt/issues) on GitHub.

Weâll love you even more if you share it with other Tilt users as an
[extension](extensions.html)!

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/custom_build.md)







### Was this doc helpful?

Yes No

