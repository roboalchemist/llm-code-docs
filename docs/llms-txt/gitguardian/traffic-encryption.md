# Source: https://docs.gitguardian.com/self-hosting/security/traffic-encryption.md

# Traffic encryption

> Configure internal traffic encryption between GitGuardian self-hosted Kubernetes pods.

For some usecase, you may want to enable traffic encryption between pods to enhance security in your Kubernetes namespace.

The best approach to do this is by using a Service Mesh that will automatically manage mTLS for all TCP traffic between the pods.
In this guide, we will go through the two most famous ones, **Istio** and **LinkerD**.

## Prerequisites

Both Istio and LinkerD rely on the concept of sidecar containers to encrypt traffic. For Gitguardian application to work properly, we need [Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/).

1. The "native" (i.e included natively in Kubernetes) Sidecar container feature is available from **Kubernetes 1.29**. It is mandatory to have this minimum version for our mesh to work properly.
2. You need either [Istio](https://istio.io/latest/docs/setup/install/) or [LinkerD](https://linkerd.io/docs/) installed.

:::info
It is not recommended to use a Mesh with databases. As we will apply the Mesh to the whole Gitguardian namespace, if your databases (PostgreSQL and Redis) are embedded in the same namespace, you will need to add annotations to exclude them from the Mesh.
:::

## Istio

This example assumes you are using Istio in [Sidecar mode](https://istio.io/latest/docs/overview/dataplane-modes/) (which is the "default" one).

1. Label your Gitguardian namespace to tell Istio we want to enable the Mesh:
```bash
kubectl label namespace <namespace> istio-injection=enabled
```

2. If a database lies in the same namespace, use the annotation `sidecar.istio.io/inject: "false"` in related pod to exclude it from the Mesh

3. Add the following to your Helm value file to enable Kubernetes native sidecars in Istio:
```yaml
migration:
  podAnnotations:
    sidecar.istio.io/nativeSidecar: "true"
```

:::info
This will use native sidecars only for Jobs, which is enough to make the Gitguardian application to work. You may add this annotations to any pod in the namespace.
:::

4. Create a `PeerAuthentication` object to force mTLS over the namespace:
```yaml
apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: default
  namespace: <namespace>
spec:
  mtls:
    mode: STRICT
```

5. If you already installed the Gitguardian application, you will have to restart all pods to inject the sidecar:
```bash
kubectl rollout restart deployment -n <namespace>
```

6. You should now see all pods carrying, at least, 2 containers, one for the application itself, one for the Istio sidecar.

## LinkerD

1. Annotate your Gitguardian namespace to tell LinkerD we want to enable the Mesh and use native sidecars mode:
```bash
kubectl annotate namespace <namespace> linkerd.io/inject=enabled
kubectl annotate namespace <namespace> config.alpha.linkerd.io/proxy-enable-native-sidecar=true
```

2. If a database lies in the same namespace, use the annotation `linkerd.io/inject: "disabled"` in related pod to exclude it from the Mesh

5. If you already installed the Gitguardian application, you will have to restart all pods to inject the sidecar:
```bash
kubectl rollout restart deployment -n <namespace>
```

6. You should now see all pods carrying, at least, 2 containers, one for the application itself, one for the LinkerD sidecar.
