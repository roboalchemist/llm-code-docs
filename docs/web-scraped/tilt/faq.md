# Tilt Documentation
# Source: https://docs.tilt.dev/faq.html
# Path: faq.html

  * [ Getting Started ](/index.html) [ Getting Started ](/docs_nav_gettingstarted.html)
  * [ Guides ](/tiltfile_authoring.html) [ Guides ](/docs_nav_guides.html)
  * [ Tiltfile & CLI ](/api.html) [ Tiltfile & CLI ](/docs_nav_reference.html)
  * [ Tilt API ](https://api.tilt.dev) [ Tilt API ](https://api.tilt.dev)

Learn About Tilt

    

  * [ Getting Started ](/)
  * [ Is Tilt right for me? ](/product_faq.html)

First Look at Tilt

    

  * [ Overview ](/tutorial/index.html)
  * [ 1\. Preparation (optional) ](/tutorial/1-prerequisites.html)
  * [ 2\. Launching & Managing Resources ](/tutorial/2-tilt-up.html)
  * [ 3\. Tilt UI ](/tutorial/3-tilt-ui.html)
  * [ 4\. Code. Update. Repeat. ](/tutorial/4-code-update-repeat.html)
  * [ 5\. Smart Rebuilds with Live Update ](/tutorial/5-live-update.html)

Quick Links

    

  * [ Install ](/install.html)
  * [ Upgrade ](/upgrade.html)
  * [ Tiltfile Snippets ](/snippets.html)
  * [ Editor Support new ](/editor.html)

How Does Tilt Work?

    

  * [ The Control Loop ](/controlloop.html)
  * [ Choosing a Local Dev Cluster ](/choosing_clusters.html)
  * [ Local vs Remote Services ](/local_vs_remote.html)

FAQs

    

  * [ Frequently Asked Questions ](/faq.html)
  * [ Why is Tilt broken? ](/debug_faq.html)
  * [ What does Tilt send? ](/telemetry_faq.html)

#  Frequently Asked Questions

### Q: How do I get help with Tilt?

For real-time support, find us on the Kubernetes slack. Get an invite at
[slack.k8s.io](http://slack.k8s.io) and find us in [the **#tilt**
channel](https://kubernetes.slack.com/messages/CESBL84MV/).

You can also file an issue in [our GitHub repo](https://github.com/tilt-
dev/tilt/issues/new).

For help with private issues (like security vulnerabilities or just concerning
non-public code), please email [help@tilt.dev](mailto:help@tilt.dev).

* * *

## Common Error Messages

### Q: When I run `tilt version`, I see âtemplate engine not found for:
versionâ. What do I do?

There is another project called Tilt for [developing Ruby
templates](https://github.com/rtomayko/tilt).

Youâre accidentally running that Tilt instead.

Common fixes include deleting the other Tilt, always using an absolute path,
or renaming Tilt to `tlt` to avoid the conflict. Tilt is a static binary so it
is OK to rename it.

* * *

### Q: I immediately get error messages like âWARNING: Image not used in any
deploy configâ. What does this mean?

To start your app, Tilt needs both:

1) Instructions on how to build an image (like a `docker_build` config)

2) Instructions on how to run your image (like a `k8s_yaml` config)

This error message means that your Tiltfile has instructions for building an
image, but no instructions for how to run it. Itâs like an âunused
variableâ warning.

Did you forget the Kubernetes YAML? Or did you just misspell the image name?

* * *

### Q: Iâm getting push errors like âunauthorized: You donât have the
needed permissionsâ. What do I do?

If Tilt is trying to do a push, that means it thinks you wanted to deploy to a
remote cluster. See [below](faq.html#q-how-do-i-change-what-kubernetes-
cluster-tilt-uses) on how to configure for a local cluster.

* * *

### Q: Tilt fails with âUnable to connect to clusterâ errors. What do I
do?

The Kubernetes server that youâre trying to deploy to is misbehaving.

Two common things to try are:

  1. Turn it off and turn it back on again (really!).

  2. Reset the cluster state.

But the specific way to do these depend on your environment.

If youâre using Docker For Mac, click the Docker icon in the upper-right
hand corner of your screen. Choose âPreferencesâ¦â to open a dialog. The
âKubernetesâ tab has a button that allows you to enable/disable
Kubernetes. The âResetâ tab has a button that allows you to reset the
cluster state.

If youâre using Minikube, `minikube stop` and `minikube start` will restart
the environment. `minikube delete` will reset the cluster state.

* * *

## How do Iâ¦?

### Q: How do I configure my app dynamically?

The [Tiltfile API](api.html) has several built-in functions for reading
configuration:

  * Read an environment variable with `os.environ.get('ENV_VAR', '')`
  * Read a file with `read_file('./path/to/file')`
  * Read a JSON or YAML file with `read_json('./path/to/file')` or `read_yaml('./path/to/file')`
  * Use `local()` to run local shell commands.

You can even define your own flags to `tilt up` with the [config
api](tiltfile_config.html).

### Q: Tilt says itâs building images. But I canât find them with the
Docker CLI. Whatâs going on?

If you are using Minikube or MicroK8s, Tilt will automatically connect to the
Docker server inside the cluster. This helps performance because Tilt
doesnât need to waste time copying Docker images around.

To check which Docker server Tilt is connecting to, run:

    
    
    tilt doctor
    

Tilt will print the Docker host. You can then run commands against that Docker
host:

    
    
    DOCKER_HOST=tcp://my-url/ docker images
    

* * *

### Q: All the Tilt examples store the image at `gcr.io`. Isnât it really
slow to push images up to Googleâs remote repository for local development?

Youâre right, that would be slow!

Most local Kubernetes development solutions let you build images directly
inside the cluster. Thereâs no need to push the image to a remote
repository.

When youâre using Docker for Mac, Minikube, or MicroK8s, Tilt will
automatically build the images in-cluster. When it detects this case, it will
even modify your Kubernetes configs to set ImageNeverPull, so that Kubernetes
will emit an error if it even tries to pull an image from a remote server.

* * *

### Q: Docker BuildKit is cool! How do I use it?

[BuildKit](https://github.com/moby/buildkit) is a new build engine in Docker
for building container images.

Tilt will automatically enable BuildKit if your local Docker installation
supports it.

BuildKit is supported on Docker v18.06 when Experimental mode is enabled, and
on Docker v18.09+

If you want to disable BuildKit manually, set `DOCKER_BUILDKIT=0`.

* * *

### Q: How do I tell Tilt to build my images with a remote Docker server?

Tilt reads the same environment variables as the `docker` command for choosing
a server. Specifically:

  * `DOCKER_HOST`: Set the url to the docker server.
  * `DOCKER_API_VERSION`: Set the version of the API.
  * `DOCKER_CERT_PATH`: Set the path to load the TLS certificates from.
  * `DOCKER_TLS_VERIFY`: To enable or disable TLS verification when using `DOCKER_CERT_PATH`, off by default.
  * `DOCKER_DEFAULT_PLATFORM`: To set the architecture of built images.

This is helpful if you have a more powerful machine in the cloud which you
want to use to build your images.

* * *

### Q: How do I change what Kubernetes cluster Tilt uses?

Tilt uses the default Kubernetes cluster configured in `kubectl`.

To see what cluster `kubectl` uses, run:

    
    
    kubectl config current-context
    

To see what clusters are available, run:

    
    
    kubectl config get-contexts
    

To change the cluster youâre deploying to, run:

    
    
    kubectl config use-context docker-desktop
    

The most common options we see in local development are `microk8s`, `docker-
desktop` (Docker For Mac stable), and `docker-for-desktop` (older Docker for
Mac versions).

* * *

### Q: What local Kubernetes solution should I choose?

Check out our [Guide to Choosing a Local Cluster](choosing_clusters.html).

* * *

### Q: How does Tilt know which local Kubernetes cluster Iâm using?

To check which cluster Tilt is connecting to, run:

    
    
    tilt doctor
    

The `Env` is the type of cluster Tilt has detected. Tilt uses this to
determine which local dev features the cluster supports.

In the dev cluster community, a common convention is to use the cluster name
prefix to indicate the cluster type. For example,

  * Docker uses the `docker-` prefix
  * GKE uses the `gke_` prefix
  * KIND uses the `kind-` prefix
  * Minikube defaults to a cluster name `minikube` (if you use Minikube profiles, Tilt will accept any cluster name prefixed `minikube-`)

If Tilt canât detect the type of your cluster, check the cluster name!

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/faq.md)







### Was this doc helpful?

Yes No

