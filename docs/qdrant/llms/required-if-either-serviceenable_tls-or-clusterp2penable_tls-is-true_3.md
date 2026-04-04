# Required if either service.enable_tls or cluster.p2p.enable_tls is true.
tls:
  # Certificate authority certificate file.
  # This certificate will be used to validate the certificates
  # presented by other nodes during inter-cluster communication.
  #
  # If verify_https_client_certificate is true, it will verify
  # HTTPS client certificate
  #
  # Required if cluster.p2p.enable_tls is true.
  ca_cert: ./tls/cacert.pem

```

## [Anchor](https://qdrant.tech/documentation/guides/security/\#hardening) Hardening

We recommend reducing the amount of permissions granted to Qdrant containers so that you can reduce the risk of exploitation. Here are some ways to reduce the permissions of a Qdrant container:

- Run Qdrant as a non-root user. This can help mitigate the risk of future container breakout vulnerabilities. Qdrant does not need the privileges of the root user for any purpose.

  - You can use the image `qdrant/qdrant:<version>-unprivileged` instead of the default Qdrant image.
  - You can use the flag `--user=1000:2000` when running [`docker run`](https://docs.docker.com/reference/cli/docker/container/run/).
  - You can set [`user: 1000`](https://docs.docker.com/compose/compose-file/05-services/#user) when using Docker Compose.
  - You can set [`runAsUser: 1000`](https://kubernetes.io/docs/tasks/configure-pod-container/security-context) when running in Kubernetes (our [Helm chart](https://github.com/qdrant/qdrant-helm) does this by default).
- Run Qdrant with a read-only root filesystem. This can help mitigate vulnerabilities that require the ability to modify system files, which is a permission Qdrant does not need. As long as the container uses mounted volumes for storage ( `/qdrant/storage` and `/qdrant/snapshots` by default), Qdrant can continue to operate while being prevented from writing data outside of those volumes.

  - You can use the flag `--read-only` when running [`docker run`](https://docs.docker.com/reference/cli/docker/container/run/).
  - You can set [`read_only: true`](https://docs.docker.com/compose/compose-file/05-services/#read_only) when using Docker Compose.
  - You can set [`readOnlyRootFilesystem: true`](https://kubernetes.io/docs/tasks/configure-pod-container/security-context) when running in Kubernetes (our [Helm chart](https://github.com/qdrant/qdrant-helm) does this by default).
- Block Qdrant’s external network access. This can help mitigate [server side request forgery attacks](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery), like via the [snapshot recovery API](https://api.qdrant.tech/api-reference/snapshots/recover-from-snapshot). Single-node Qdrant clusters do not require any outbound network access. Multi-node Qdrant clusters only need the ability to connect to other Qdrant nodes via TCP ports 6333, 6334, and 6335.

  - You can use [`docker network create --internal <name>`](https://docs.docker.com/reference/cli/docker/network/create/#internal) and use that network when running [`docker run --network <name>`](https://docs.docker.com/reference/cli/docker/container/run/#network).
  - You can create an [internal network](https://docs.docker.com/compose/compose-file/06-networks/#internal) when using Docker Compose.
  - You can create a [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) when using Kubernetes. Note that multi-node Qdrant clusters [will also need access to cluster DNS in Kubernetes](https://github.com/ahmetb/kubernetes-network-policy-recipes/blob/master/11-deny-egress-traffic-from-an-application.md#allowing-dns-traffic).

There are other techniques for reducing the permissions such as dropping [Linux capabilities](https://www.man7.org/linux/man-pages/man7/capabilities.7.html) depending on your deployment method, but the methods mentioned above are the most important.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/security.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/security.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-131-lllmstxt|>
## async-api
- [Documentation](https://qdrant.tech/documentation/)
- [Database tutorials](https://qdrant.tech/documentation/database-tutorials/)
- Build With Async API