# Source: https://docs.datadoghq.com/containers/guide/docker-deprecation.md

---
title: Docker Deprecation in Kubernetes
description: >-
  Handle Docker runtime deprecation in Kubernetes by migrating to containerd or
  CRI-O container runtimes
breadcrumbs: Docs > Containers > Containers Guides > Docker Deprecation in Kubernetes
---

# Docker Deprecation in Kubernetes

Kubernetes is deprecating Docker as a runtime starting after version 1.20, and some cloud providers have deprecated Docker in their images.

- AKS 1.19 [deprecated Docker and uses containerd by default](https://github.com/Azure/AKS/releases/tag/2020-11-16).

- GKE 1.19 [deprecated Docker and uses containerd by default, on new nodes](https://cloud.google.com/kubernetes-engine/docs/release-notes#December_08_2020).

- EKS 1.22 [deprecated Docker and uses containerd by default](https://aws.amazon.com/blogs/containers/amazon-eks-1-21-released/).

- OKE 1.20 [deprecated Docker and uses CRI-O by default](https://docs.oracle.com/en-us/iaas/releasenotes/changes/52d34150-0cb8-4a0f-95f3-924dec5a3c83/).

If you are running a version of Kubernetes where Docker has been deprecated, the Docker socket is no longer present, or has no information about the containers running by Kubernetes, and the Docker check does not work. You can find details about Docker runtime on [kubernetes.io](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-deprecation-affects-you/#role-of-dockershim). This means that you must enable either the [containerd](https://docs.datadoghq.com/integrations/containerd/) or the [CRI-O](https://docs.datadoghq.com/integrations/crio/) check depending on the container runtime you are using. The container metrics collected from the new container runtime replace the Docker metrics.

With version 7.27+ of the Datadog Agent, the Agent automatically detects the environment you are running, and you do not need to make any configuration changes.

**If you are using Agent < v7.27, you must specify your container runtime socket path:**

**Note**: You may need to update your existing monitors, dashboards, and SLOs because metrics names changeâfor example, from `docker.*` to `containerd.*`.

{% tab title="Helm" %}
Set the path to your container runtime socket with the `datadog.criSocketPath` parameter in the [Helm chart](https://github.com/DataDog/helm-charts/blob/d8817b4401b75b1a064481da989c451633249ea9/charts/datadog/values.yaml#L262-L263).

For example:

```gdscript3
criSocketPath:  /var/run/containerd/containerd.sock
```

{% /tab %}

{% tab title="DaemonSet" %}
Remove any references to the Docker socket, as well as any Docker socket volume mounts.

Use the environment variable `DD_CRI_SOCKET_PATH` to point to your container runtime socket path. Set on all Agent containers if using dedicated containers:

```gdscript3
env:
  - name: DD_CRI_SOCKET_PATH
    value: /var/run/containerd/containerd.sock
```

Mount the socket from your host to the Agent container:

```gdscript3
volumeMounts:
  - name: containerdsocket
    mountPath: /var/run/containerd/containerd.sock
  - mountPath: /host/var/run
    name: var-run
    readOnly: true
volumes:
  - hostPath:
      path: /var/run/containerd/containerd.sock
    name: containerdsocket
  - hostPath:
      path: /var/run
    name: var-run
```

{% /tab %}
