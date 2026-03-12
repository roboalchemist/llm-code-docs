# Source: https://docs.pinot.apache.org/release-0.4.0/operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-0.9.0/operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-0.10.0/operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-0.11.0/operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-0.12.0/operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-0.12.1/operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/tutorials/deployment-pinot-on-kubernetes.md

# Source: https://docs.pinot.apache.org/operators/tutorials/deployment-pinot-on-kubernetes.md

# Kubernetes Deployment

Pinot community has provided Helm based [Kubernetes deployment template](https://docs.pinot.apache.org/basics/getting-started/kubernetes-quickstart).

You can deploy it as simple as run a `helm install` command.

However there are a few things to be noted before starting the benchmark/production.

## Container Resources

We recommend to run Pinot with pre-defined resources for the container, and make requests and limits to be the same.

This will ensure the container won't be killed if there is a sudden bump of workload.

It will also be simpler to benchmark the system, e.g. get broker qps limit.

Below is an example for values to set in `values.yaml` file. Default resources is not set.

```
resources:
  requests:
    cpu: 1
    memory: 1G
  limits:
    cpu: 1
    memory: 1G
```

## JVM Setting

### Pinot Controller/Broker

JVM setting should be complaint with the container resources for Pinot Controller and Pinot Broker.

```
resources:
  requests:
    cpu: 1
    memory: 1G
  limits:
    cpu: 1
    memory: 1G
```

You can make JVM setting like below to make `-Xmx` the same size as your container.

```
jvmOpts: "-Xms256M -Xmx1G"
```

### Pinot Server

For Pinot Server, heap is majorly used for query processing, metadata management. It uses off-heap memory for data loading/persistence, memory mapped files page caching. So we recommend just keep minimal requirement for JVM, and leave the rest of the container for off-heap data operations.

E.g. Assuming data is 100 GB on disk, the container size is 4 CPU, 10GB Memory.

```
resources:
  requests:
    cpu: 4
    memory: 10G
  limits:
    cpu: 4
    memory: 10G
```

For JVM, limit `-Xmx` to not exceed 50% container memory limit, so that the rest of the container could be leveraged by the off-heap operations.

```
jvmOpts: "-Xms1G -Xmx4G"
```

## Deep storage

Pinot uses remote storage as deep storage to backup segments.

Default deployment creates a mount disk(e.g Amazon EBS) as deep storage in controller.

You can configure your own S3/Azure DataLate/Google Cloud Storage following this [link](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system#enabling-a-file-system).

## Security

{% hint style="danger" %}
The default Helm chart configuration does **not** enable authentication.

Do **not** expose Pinot services to the public Internet unless you add security controls.

At minimum, add an Ingress/API gateway with TLS + authentication, and lock down network access.
{% endhint %}

Default Helm installs are usually **not** production-safe. Lock down both transport and access.

### TLS

You have two common deployment patterns. Pick one and be consistent.

#### Option A: Terminate TLS at the edge (simple)

Terminate TLS at your Ingress / API gateway / L7 load balancer.

* Expose only the **controller** and **broker** externally.
* Keep internal Pinot services as `ClusterIP`.
* Add network policies so only the gateway can reach controller/broker.
* If you need encryption inside the cluster, use a service mesh for mTLS.

This keeps certificate management out of Pinot. It is the easiest path.

#### Option B: End-to-end TLS in Pinot (edge + internode)

Pinot 0.7.0+ supports TLS for both **client ↔ cluster** and **intra-cluster** traffic.

Use this when you want encryption and (optionally) identity checks between Pinot nodes.

1. Generate a keystore + truststore for each component.
2. Store them in Kubernetes `Secret`s and mount them into pods.
3. Configure Pinot listeners to add HTTPS alongside HTTP (migration-safe).
4. Switch egress to prefer HTTPS, then disable HTTP.

Follow the step-by-step property reference in:

* [Configuring TLS/SSL](https://docs.pinot.apache.org/operators/tutorials/configuring-tls-ssl)

{% hint style="info" %}
If you mount key/truststores into the container, you can also point the JVM at them with: `-Djavax.net.ssl.keyStore`, `-Djavax.net.ssl.keyStorePassword`, `-Djavax.net.ssl.trustStore`, `-Djavax.net.ssl.trustStorePassword`. This is useful when a plugin only reads the JVM default truststore.
{% endhint %}

#### 2-way TLS (mTLS)

If you need strong internode authentication at the transport layer, enable 2-way TLS.

* It forces clients to present certificates.
* It reduces the blast radius of a compromised pod IP.

Pinot supports this via `*.tls.client.auth.enabled=true`. See:

* [Configuring TLS/SSL](https://docs.pinot.apache.org/operators/configuring-tls-ssl#2-way-tls)

### Authentication and authorization (controller + broker)

TLS protects the channel. You still need authN/authZ on the APIs.

Pinot supports HTTP Basic Auth + ACLs for:

* **pinot-controller**: admin APIs + web UI
* **pinot-broker**: query APIs

Start here:

* [Authentication](https://docs.pinot.apache.org/operators/tutorials/authentication)

Then pick an implementation:

* [Basic auth access control](https://docs.pinot.apache.org/operators/tutorials/authentication/basic-auth-access-control) (file-based config)
* [ZkBasicAuthAccessControl](https://docs.pinot.apache.org/operators/tutorials/authentication/zkbasicauthaccesscontrol) (ZooKeeper-backed, supports hot updates, encrypted passwords)

#### Store secrets safely (Helm + Kubernetes)

Do not hardcode passwords or tokens in `values.yaml` or ConfigMaps.

* Put credentials in Kubernetes `Secret`s.
* Load them into Pinot config via env var templating.

See:

* [Dynamic Environment](https://docs.pinot.apache.org/configuration-reference/dynamic-environment)

{% hint style="warning" %}
When you enable controller/broker auth, internal Pinot components also need service tokens (segment fetchers, uploaders, minions). Plan a rolling restart and validate internode calls.
{% endhint %}

### Quick hardening checklist

* Enable TLS (edge termination or end-to-end).
* Enable auth on **controller** and **broker**.
* Restrict network access to controller/broker (Ingress + NetworkPolicy).
* Use Kubernetes `Secret`s + env templating for all sensitive values.
* Rotate certs and credentials. Treat Helm release history as sensitive.
