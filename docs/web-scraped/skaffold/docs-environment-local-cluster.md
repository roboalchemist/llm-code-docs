# Source: https://skaffold.dev/docs/environment/local-cluster/

Title: Local Cluster

URL Source: https://skaffold.dev/docs/environment/local-cluster/

Markdown Content:
Skaffold supports fast deployments to supported locally-hosted clusters, such as [`minikube`](https://github.com/kubernetes/minikube/) and [`Docker Desktop`](https://www.docker.com/products/docker-desktop), by loading images directly into the cluster. Loading images is typically much faster than the roundtrip required to push an image to a remote registry and then for the cluster to pull that image again.

### Auto detection

Skaffold’s heuristic to detect local clusters is based on the Kubernetes context name set on kubectl. You can find your the current context name by running:

```
kubectl config current-context
```

Skaffold checks for the following context names:

| Kubernetes context | Local cluster type | Notes |
| --- | --- | --- |
| docker-desktop | [`Docker Desktop`](https://www.docker.com/products/docker-desktop) |  |
| docker-for-desktop | [`Docker Desktop`](https://www.docker.com/products/docker-desktop) | This context name is deprecated |
| minikube 1 | [`minikube`](https://github.com/kubernetes/minikube/) | See 1 |
| kind-(.*) | [`kind`](https://github.com/kubernetes-sigs/kind) | This pattern is used by kind >= v0.6.0 |
| (.*)@kind | [`kind`](https://github.com/kubernetes-sigs/kind) | This pattern was used by kind < v0.6.0 |
| k3d-(.*) | [`k3d`](https://github.com/rancher/k3d) | This pattern is used by k3d >= v3.0.0 |

For any other name, Skaffold assumes that the cluster is remote and that images have to be pushed.

1 Additionally, a Kubernetes context may be considered as `minikube` even if it’s not named `minikube` but it’s cluster certificate is stored at `$HOME/.minikube` or the `minikube profile list` command returns the Kubernetes context name.

### Manual override

For non-standard local setups, such as a custom `minikube` profile, some extra configuration is necessary. The essential steps are:

1.   Ensure that Skaffold builds the images with the same docker daemon that runs the pods’ containers.

2.   Tell Skaffold to skip pushing images either by configuring

```
build:
  local:
    push: false
``` 
or by marking a Kubernetes context as local (see the following example).

For example, when running `minikube` with a custom profile (e.g. `minikube start -p my-profile`):

1.   Set up the docker environment for Skaffold with `source <(minikube docker-env -p my-profile)`. This should set some environment variables for docker (check with `env | grep DOCKER`). **It is important to do this in the same shell where Skaffold is executed.**

2.   Tell Skaffold that the Kubernetes context `my-profile` refers to a local cluster with

```
skaffold config set --kube-context my-profile local-cluster true
``` 

Caveats
-------

There are some caveats to note with local clusters.

### Minikube has a separate Docker Daemon

Minikube has a separate Docker daemon that runs inside the minikube virtual machine, which is independent of the Docker installation that may be running on the host. Skaffold automatically uses `minikube docker-env` to configure image builders to use this internal Docker daemon as it [results in a dramatic speed-up as compared to other approaches](https://minikube.sigs.k8s.io/docs/benchmarks/imagebuild/minikubevsothers/).

The use of minikube’s internal daemon does means that images are not available from the host’s daemon:

```
# build the image `skaffold-example`
$ skaffold build
...
Starting build...
Found [minikube] context, using local docker daemon.
...
Successfully tagged skaffold-example:v1.35.0-37-g7ccebe58e
Build [skaffold-example] succeeded

# but the image is not found in the host docker!
$ docker images skaffold-example
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

You must instead configure the Docker CLI to use the Minikube daemon:

```
$ minikube docker-env
export DOCKER_HOST="tcp://127.0.0.1:54168"
...
$ eval $(minikube docker-env) && docker images skaffold-example
REPOSITORY         TAG                                                                IMAGE ID       CREATED       SIZE
skaffold-example   160fe3a3c1358ef7b3fbfd1ae19fc8c5ac096635c39171e22ad1e5242b6ad8fd   160fe3a3c135   3 weeks ago   7.43MB
skaffold-example   v1.35.0-37-g7ccebe58e                                              160fe3a3c135   3 weeks ago   7.43MB
```

Minikube also offers a set of helper commands to manage images through [`minikube image`](https://minikube.sigs.k8s.io/docs/commands/image/).

### Impacts of `imagePullPolicy`

Skaffold’s direct loading of images into a local cluster does mean that resources specifying an [`imagePullPolicy: Always`](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy) may fail as the images are not be pushed to the remote registry.
