# Source: https://docs.logrocket.com/docs/upgrading-from-v23-to-v24.md

# Upgrading from v23 to v24

## Upgrading from v23 to v24

**This upgrade path is intended for customers who are already on v23 of LogRocket.**

**In order to check the version you are running, open your`values.yaml` file and check the `image.version`.  If it states `23`, please proceed.**

**If you are on LogRocket v22 or below, you will *not* be able to upgrade directly to v24. [You will first need to upgrade to LogRocket v23](https://docs.logrocket.com/docs/upgrading-from-v22-to-v23)**

## Major Changes

<Callout icon="🚧" theme="warn">
  The NGINX changes in this chart upgrade require AWS Customers to consider their networking configuration.  We use the PROXY protocol on AWS Clusters and the `ingress-nginx` chart we use altered their behavior for IP capture for setups that use the PROXY protocol.

  By default, our AWS clusters set `nginx-ingress.controller.config.use-proxy-protocol: "true"` and rely on our global setting of `nginx-ingress.controller.config.use-forwarded-headers: "true"`to capture Client IP Addresses that you see in Session Playback.

  You can review their full Testing setup in the [PR for this change](https://github.com/kubernetes/ingress-nginx/pull/12768) but the simplest path is:

  If you use LogRocket's default configuration of a NLB and clients talk directly to the NLB, you must manually set `use-forwarded-headers: "false"` or IP address capture will fail (see examples below) - you can also follow one of the configurations using `proxy-real-ip-cidr` documented in their PR.

  If you run an HTTP Proxy like CloudFront or anything else in front of your NLB you will probably be ok keeping our default `values.yaml`although again there are a few configuration options available documented in their PR.
</Callout>

<Callout icon="🚧" theme="warn">
  This requires that ClickHouse pods have 10Gi of Ram available.  You will need to use a kubernetes Node type that has at least 12Gi of Memory (Kubernetes uses a small amount of memory on each Node so you cannot only provide 10Gi of memory - the helm chart will fail to upgrade because it cannot deploy the new ClickHouse pods.

  If you already have a custom setting for `inClusterClickhouse.resources.requests.memory` of `8Gi` or higher in your values.yaml file, you are safe for this upgrade (this changes the default for customers who have not already overridden this change to support larger query loads).

  The default GCP Node type of `e2-standard-4` and Azure Node type of `Standard_D8_v5` are large enough to support this upgrade.  The default AWS Node type of `m5.xlarge` is large enough for this upgrade, but a common configuration of `m5.large` or`c5.xlarge`will fail this upgrade.
</Callout>

### Other Changes

#### ClickHouse

This chart now requires that data ingested to ClickHouse write to 2 separate replicas of your ClickHouse cluster.  This makes cluster health problems obvious sooner and helps ensure data is written to your ClickHouse cluster.

This will not be enabled if you are running a Sharded ClickHouse cluster (in your `values.yaml` you have `inClusterClickHouse.shards` set to 2 - it defaults to 1 which is LogRocket's preferred configuration).

#### NGINX upgraded

This release includes a number of CVE Fixes ([CVE-2026-1580](https://github.com/kubernetes/kubernetes/issues/136677), [CVE-2026-24512](https://github.com/kubernetes/kubernetes/issues/136678), [CVE-2026-24513](https://github.com/kubernetes/kubernetes/issues/136679) and [CVE-2026-24514](https://github.com/kubernetes/kubernetes/issues/136680))

Reviewing our configuration notes above:

##### Client -> NLB -> LogRocket

Update your values.yaml file to set `use-forwarded-headers: "false"`- we have elided some of the other nginx-ingress configuration in your values.yaml - you should not remove anything.

```yaml
nginx-ingress:
  controller:
    config:
      use-forwarded-headers: "false" # add this line to the config block
      use-proxy-protocol: "true"
```

#### Client -> HTTP Proxy -> NLB -> LogRocket

You should be safe continuing to use our default configuration, but you will need to test after the upgrade to ensure new recorded sessions are correctly capturing Client IP Addresses.

### Updating your values.yaml file

Edit your `values.yaml` file and update `image.version` from 23 to 24.

### Helm and Kubectl commands

```
helm upgrade --values values.yaml --wait --timeout 1500s --version 24.x logrocket oci://us-central1-docker.pkg.dev/logrocket-artifacts/helm3/logrocket
```

To monitor the deploy, you can run `kubectl get pods --watch` in a separate terminal.

If things break during the deploy, please pull the information from our [Debugging Cluster Problems](https://docs.logrocket.com/docs/information-needed-to-support-your-logrocket-self-hosted-cluster) document along with the following two commands and include it in your message to support.

```
kubectl describe statefulset
kubectl get pods -A
```

<br />