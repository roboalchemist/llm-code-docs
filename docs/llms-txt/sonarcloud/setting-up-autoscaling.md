# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deploy-on-kubernetes/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling.md

# Setting up autoscaling

With Kubernetes’ Horizontal Pod Autoscaling (HPA), you can automatically scale your SonarQube Server out and in, resolving any performance issues you may have.

The HPA increases or decreases the number of deployment replicas according to the overall CPU consumption of the SonarQube Server Pods.

### Warning before you start <a href="#warning" id="warning"></a>

Currently, autoscaling targets only the Data Center Edition application nodes. The initial goal is to improve the pull request analysis time by ensuring that background tasks do not pile up.

This feature should be used with caution, as it can significantly increase costs. This is the first iteration, and future improvements will come.

{% hint style="info" %}
We suggest disabling autoscaling for long-running upgrades to prevent unnecessary scaling due to this initial upgrade load.
{% endhint %}

### Requirements <a href="#requirements" id="requirements"></a>

Make sure the [metric server](https://github.com/kubernetes-sigs/metrics-server) is installed in your Kubernetes cluster.

Autoscaling can function optimally only if the system does not have a bottleneck. You should monitor your system to avoid bottlenecks (see **Troubleshooting autoscaling** below).

### Enabling autoscaling <a href="#enabling" id="enabling"></a>

To enable autoscaling in your DCE cluster:

* In the `values.yaml` file of the SonarQube Server’s DCE Helm chart, set the `ApplicationNodes.hpa.enabled` to `true`.

### Testing autoscaling <a href="#testing" id="testing"></a>

To test autoscaling:

* Check the `pending_count` and `pending_time` of background tasks (see [instance](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/monitoring/instance "mention")). If they are increasing, SonarQube Server should scale up. If not (autoscaling is not triggered), perform the steps described below.

If the autoscaling test is negative, see [#troubleshooting](#troubleshooting "mention") below.

### Troubleshooting autoscaling <a href="#troubleshooting" id="troubleshooting"></a>

Autoscaling can function optimally only if the system does not have a bottleneck. You should monitor your system to avoid bottlenecks.

If autoscaling is not triggered properly:

1. Change the number of workers per node that will process background tasks. For the DCE Helm chart’s default request/limit resources (see Default configuration in Autoscaling configuration below), set this number to 3 ( 3 is the ideal number for maximizing performance and inducing a constant load to trigger autoscaling).
2. Check that your database is not under heavy load. This can be because the database’s CPU/RAM/IO are capped at the maximum value. Some databases also have an IO burst balance that can get exhausted (Database I/Os are very important for optimal performances.)
3. Perform the same checks regarding networking and resource cap on the reverse proxy, load balancer, network, and Kubernetes nodes I/Os.
4. If autoscaling still does not work properly, try to adjust the configuration with caution. See the Autoscaling configuration section below for details.

### Disabling autoscaling <a href="#disabling" id="disabling"></a>

* In the `values.yaml` file of the SonarQube Server’s DCE Helm chart, set the `ApplicationNodes.hpa.enabled` to `false`.

### Autoscaling configuration <a href="#configuration" id="configuration"></a>

<details>

<summary>Default configuration</summary>

The [default autoscaling configuration](https://github.com/SonarSource/helm-chart-sonarqube/blob/master/charts/sonarqube-dce/values.yaml#L374) in the SonarQube Server’s DCE Helm chart is shown below. Note that it’s designed to work with the default resources (see below the configuration).

```yaml
 hpa:
    enabled: false
    minReplicas: 2
    maxReplicas: 10
    metrics:
      - type: Resource
        resource:
          name: cpu
          target:
            type: Utilization
            averageUtilization: 80
    behavior:
      scaleDown:
        stabilizationWindowSeconds: 60
        policies:
          - type: Pods
            value: 1
            periodSeconds: 20
      scaleUp:
        stabilizationWindowSeconds: 0
        policies:
          - type: Percent
            value: 100
            periodSeconds: 600
```

**Default resources**

The default autoscaling setup is designed to work with the helm chart’s default resources block shown below.

```yaml
  resources:
    limits:
      cpu: 800m
      memory: 3072M
    requests:
      cpu: 400m
      memory: 3072M
```

</details>

<details>

<summary>Minimum number of deployment replicas</summary>

We highly recommend not setting `minReplicas` below 2, but you can adjust according to your availability needs.

</details>

<details>

<summary>Maximum number of deployment replicas</summary>

`maxReplicas` can be freely edited, but remember that this can induce a huge increase in costs.

</details>

<details>

<summary>Scale-up policy</summary>

The scale-up policy (`scaleUp:policies`) defines the extent to which the number of Pods increases (`value`) during a given period of time (`periodSeconds`) in case 80% of the CPU request is reached.

The default scale-up policy aims at best-effort efficiency over cost by **at most** doubling the number of Pods (`value` = 100%) every 10 minutes. We are aggressively scaling up to compensate for SonarQube Server long startup time (about a minute) and to let the stabilization happen after startup:

* The 10-minute period is important as it lets the new Pod stabilize its CPU consumption at startup, preventing an autoscaling loop in which the Pods are scaled up to the maximum number directly.
* Doubling allows for an exponential scale-up that can catch up with the load and ensure a 10-minute lag at most.

</details>

<details>

<summary>Scale-down policy</summary>

The scale-down policy (`scaleDown:policies`) defines the extent to which the number of Pods decreases (`value`) during a given period of time (`periodSeconds`) in case the CPU max value of the past 60 seconds is below the 80% CPU request.

The default scale-down policy removes 1 Pod every 20 seconds. It suits the aggressive default scale-up policy by scaling down quickly to the required number of Pods to accommodate the load.

</details>
