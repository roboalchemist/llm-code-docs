# Tilt Documentation
# Source: https://docs.tilt.dev/personal_registry.html
# Path: personal_registry.html

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

#  Setting up any Image Registry

If youâre building container images in dev, youâll need a place to put
those images from which your cluster can pull them.

## The Easy Way (for 95% of Users)

Hereâs how you set up a dev image registry.

Step 1) [Choose a cluster](choosing_clusters.html).

Step 2) There is no step 2!!!

### Your Registry is Usually Already Set Up For You

For almost all clusters, the cluster will have a registry for you.

  * If youâre using Docker for Desktop, thereâs no registry at all. You build directly into the container runtime.

  * If youâre using a local cluster like Kind, [our setup scripts](choosing_clusters.html) will set up a registry for you.

  * If youâre using a remote cluster (like AKS, EKS, GKE, and DigitalOcean Kubernetes), youâll have a registry thatâs colocated with your cluster and well-configured.

### Your Registry Secrets are Usually Already Set Up For You

You also donât have to worry about authentication.

Our local cluster guides set up registries without any auth (because theyâre
purely local).

If youâre using an authenticated registry, thatâs usually not a problem
either. Tilt never talks directly to a registry. When Tilt builds images, it
tells the image builder to push to the registry when itâs done. If you need
to login to a registry, youâll login with the image builder.

For [Docker Hub](https://docs.docker.com/engine/reference/commandline/login/),
you run:

    
    
    docker login
    

with a username and password (or token).

Other registries have their own login command, e.g.,

    
    
    docker login quay.io
    

Some managed Kubernetes services have their own credential helpers:

  * [Amazon ECR](https://github.com/awslabs/amazon-ecr-credential-helper)

  * [Google Artifact Registry](https://cloud.google.com/artifact-registry/docs/docker/quickstart)

  * [Google Container Registry](https://cloud.google.com/container-registry/docs/advanced-authentication)

These will ensure that your login credentials for kubectl and your login
credentials for the registry stay in-sync.

### What to Put in `docker_build`

The first argument to `docker_build` is an image _selector_.

    
    
    docker_build('my-image', '.')
    

`my-image` will match against any images in your deploy YAML (e.g., your
Kubernetes Deployment).

If youâre using a local cluster, donât worry what the host of the image
name is! The main rule is that it needs to match the image name in the YAML.
Tilt will automatically inject the fully-qualified image name for the local
registry into your deploy YAML.

If youâre using a remote cluster, you should use the registry name in both
the `docker_build` and in your YAML. For example, GKE registries look like
`gcr.io/my-project/my-image-nameâ.

## The Medium-Easy Way (for 4% of users)

If youâre using a cluster that doesnât have a registry, thereâs a
medium-easy option to get you unblocked fast.

[`ttl.sh`](https://ttl.sh/) is an anoymous, ephemeral image registry that you
can use for development. Itâs operated by our friends at
[Replicated](https://www.replicated.com/).

Add the following function to your Tiltfile:

    
    
    default_registry('ttl.sh/[my-user-name]-[random-string]')
    

First, Tilt will try to load the image directly to the cluster (if the cluster
supports this.)

If it canât do that, Tilt will rename the image under the ttl.sh URL, push
it to the ephemeral registry, and pull it into your cluster.

`ttl.sh` is encrypted over HTTPS but not authenticated. It will delete your
image after an hour. So itâs a good option if youâre trying out a sample
project (like one of the Tilt examples).

If you use `default_registry`, thereâs no need to have the registry host in
`docker_build()` or in your deploy YAML.

## The Medium Way (for 1% of users)

In almost all cases, itâs OK for a team to all share the same registry.

Tilt uses content-based image tags, so you donât have to worry about one
user overwriting another usersâ images if theyâre pushing dev images at
the same time.

But in some exotic cases, organizations may set up a registry per developer or
a registry per team.

Fortunately, the Tiltfile `default_registry` system can be scripted to support
this.

Weâre going to modify the `Tiltfile` to look for a file called
`tilt_option.json` next to the Tiltfile.

You can add more settings here (do different team members want different
services to behave differently? Put it in `tilt_option.json`). For now,
weâll expect the file to either be nonexistent, or JSON like:

    
    
    {
      "default_registry": "gcr.io/my-personal-project"
    }
    

Add this code to the `Tiltfile`:

    
    
    settings = read_json('tilt_option.json', default={})
    default_registry(settings.get('default_registry', 'gcr.io/shared-project-registry'))
    

Add a line to your `.gitignore`:

    
    
    # personal tilt settings
    tilt_option.json
    

Team members donât need to set anything, but new users can change it without
modifying the Tiltfile.

## Registries that are Special Snowflakes

### When Your Registry Has Multiple URLs

URLs on your laptop resolve differently than URLs in your cluster.

In some cases, the URL of a registry (as seen from your laptop) may be
different from the URL of the same registry (as seen from your cluster).

For example, your laptop might push your image to `localhost:5000/my-image`,
while your cluster pulls the image from `registry:5000/my-image`.

Most modern cluster setup tools try to set up DNS to prevent this from
happening. But if you do hit this scenario (and youâll usually know if you
are), you can use the `host_from_cluster` parameter of `default_registry` to
configure the registry host as referenced from your cluster.

    
    
    default_registry(
        'localhost:5000',
        host_from_cluster='registry:5000'
    )
    

### Elastic Container Registryâs Repository Dance

The AWS container registry, ECR, forces you to create a
[repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html)
ahead of time for each image name.

For teams that use ECR, Tilt offers the option to push all your images to a
single repository in the registry.

    
    
    default_registry(
      'aws_account_id.dkr.ecr.region.amazonaws.com',
      single_name='my-team-name/dev')
    

Teams can have a shared repository, or a repository per developer:

    
    
    default_registry(
      'aws_account_id.dkr.ecr.region.amazonaws.com',
      single_name='%s/dev' % os.environ.get('AWS_USERNAME'))
    

## The Hard Way (for 0% of users)

We donât expect setting up a registry to be hard!

Every single cloud provider is working to make it as easy as possible
(including cloud non-providers like Replicatedâs [ttl.sh](https://ttl.sh)
above).

If youâre struggling to set up and authenticate to a registry, come [talk to
us](index.html#community) and a support engineer will point you in the right
direction.

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/personal_registry.md)







### Was this doc helpful?

Yes No

