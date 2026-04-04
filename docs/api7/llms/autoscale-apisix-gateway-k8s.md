# Source: https://docs.api7.ai/apisix/production/scaling/autoscale-apisix-gateway-k8s.md

# Autoscale APISIX Gateway (K8s)

Autoscaling is a mechanism that automatically adjusts the resources available to the gateway, ensuring consistent performance under varying traffic loads.

This document guides you through setting CPU and memory requests, creating a Horizontal Pod Autoscaler (HPA) for APISIX, and verifying scaling behavior with a simple load test, allowing your deployment to respond dynamically to workload changes.

The instructions below assume that APISIX is already installed in a Kubernetes cluster.

## Deploy a Metrics Server[â](#deploy-a-metrics-server "Direct link to Deploy a Metrics Server")

The Horizontal Pod Autoscaler (HPA) requires CPU and memory metrics from the cluster. The Kubernetes Metrics Server collects these metrics from kubelets and exposes them through the Kubernetes API.

To deploy the Metrics Server, run:

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Patch the Metrics Server deployment to allow insecure TLS connections to kubelets, which may be required in some cluster configurations:

```
kubectl patch deployment metrics-server \
  -n kube-system \
  --type='json' \
  -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value":"--kubelet-insecure-tls"}]'
```

To verify that the Metrics Server is functioning correctly, you can inspect the CPU and memory usage of pods within the current namespace:

```
kubectl top pods
```

Assuming that the APISIX pod is running in the current namespace, you should see its CPU and memory metrics:

```
NAME                                         CPU(cores)   MEMORY(bytes)   
apisix-595698f9df-hmbwn                      19m          296Mi   
```

This confirms that metrics are being collected and available for the HPA.

## Configure Resource Requests and Limits[â](#configure-resource-requests-and-limits "Direct link to Configure Resource Requests and Limits")

To ensure proper resource allocation and enable HPA to scale APISIX effectively, you should set CPU and memory requests and limits for the APISIX Gateway pods.

To do so, export the current Helm values of your APISIX release:

```
helm get values apisix --all > values.yaml
```

Update the resources section to include CPU and memory requests and limits. This ensures the Kubernetes scheduler can allocate sufficient resources for each pod and that HPA can monitor pod usage accurately.

The values below are example settings. In production, you should adjust CPU and memory requests and limits based on your expected traffic, workload characteristics, and cluster resources.

values.yaml

```
resources:
  requests:
    cpu: "200m"       # Minimum CPU guaranteed (0.2 CPU cores)
    memory: "256Mi"   # Minimum memory guaranteed (256 MiB)
  limits:
    cpu: "1"          # Maximum CPU allowed (1 CPU core)
    memory: "512Mi"   # Maximum memory allowed (512 MiB)
```

Apply the updated configuration by upgrading the release:

```
helm upgrade apisix apisix/apisix -f values.yaml
```

## Create an HPA[â](#create-an-hpa "Direct link to Create an HPA")

Create a `HorizontalPodAutoscaler` for the APISIX deployment that automatically scales the number of pods between 2 and 10. Scaling is based on average CPU usage, with a target of 50%, to accommodate varying traffic loads. Adjust the number of replicas and the CPU target as needed to match your workload and cluster resources.

apisix-hpa.yaml

```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: apisix-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: apisix
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
```

Apply the configuration to create the HPA:

```
kubectl apply -f apisix-hpa.yaml
```

View the current status of HPA in the cluster:

```
kubectl get hpa
```

You should see an output similar to the following:

```
NAME         REFERENCE           TARGETS       MINPODS   MAXPODS   REPLICAS   AGE
apisix-hpa   Deployment/apisix   cpu: 6%/50%   2         10        2          10m
```

## Verify Autoscaling with Load Test[â](#verify-autoscaling-with-load-test "Direct link to Verify Autoscaling with Load Test")

To verify autoscaling, you will start 20 load pods to generate traffic against the gateway. Alternatively, you can also use load-testing tools such as k6 or wrk.

```
for i in $(seq 1 20); do
  kubectl run load-$i --image=busybox:1.28 --restart=Never \
    --labels=app=loadgen \
    -- /bin/sh -c "while true; do wget -q -O- http://apisix-gateway/ >/dev/null 2>&1; done" &
done
```

In a separate terminal, watch the status of the HPA, including current metrics, replica count, and scaling activity in real time:

```
kubectl get hpa apisix-hpa -w
```

You should see the CPU utilization rising. When the load is sustained and high enough, HPA starts to scale up the APISIX deployment:

```
NAME         REFERENCE           TARGETS         MINPODS   MAXPODS   REPLICAS   AGE
apisix-hpa   Deployment/apisix   cpu: 14%/50%    2         10        2          54m
apisix-hpa   Deployment/apisix   cpu: 37%/50%    2         10        2          55m
apisix-hpa   Deployment/apisix   cpu: 365%/50%   2         10        2          56m
apisix-hpa   Deployment/apisix   cpu: 73%/50%    2         10        4          56m
apisix-hpa   Deployment/apisix   cpu: 21%/50%    2         10        7          56m
apisix-hpa   Deployment/apisix   cpu: 39%/50%    2         10        7          57m
```

To observe the deployment scale down, delete all load-generating pods:

```
kubectl delete pod -l app=loadgen
```

You should see the CPU utilization decreasing and APISIX deployment scales down the number of replicas:

```
NAME         REFERENCE           TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
apisix-hpa   Deployment/apisix   cpu: 26%/50%    2         10        7          62m
apisix-hpa   Deployment/apisix   cpu: 17%/50%    2         10        5          63m
apisix-hpa   Deployment/apisix   cpu: 6%/50%     2         10        4          64m
apisix-hpa   Deployment/apisix   cpu: 6%/50%     2         10        3          64m
apisix-hpa   Deployment/apisix   cpu: 6%/50%     2         10        2          64m
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

Kubernetes provides several autoscaling strategies beyond the CPU-based approach shown in this guide. Depending on your workload characteristics, APISIX can be scaled based on memory utilization, custom metrics, or a combination of multiple metrics to achieve more accurate scaling decisions. Additionally, Kubernetes allows the configuration of scaling policies to control the rate of scale-up and scale-down events, which is important for maintaining stability in production environments.

For a full overview of supported metrics, scaling behaviors, and advanced configuration options, please consult the official Kubernetes documentation:

* [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale)
* [HorizontalPodAutoscaler Walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough)
