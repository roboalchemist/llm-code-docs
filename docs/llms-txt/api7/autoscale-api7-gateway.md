# Source: https://docs.api7.ai/enterprise/production/scaling/autoscale-api7-gateway.md

# Source: https://docs.api7.ai/enterprise/3.8.x/production/scaling/autoscale-api7-gateway.md

# Autoscale API7 Gateway (K8s)

Autoscaling is a mechanism that automatically adjusts the resources available to the gateway, ensuring consistent performance under varying traffic loads.

This document guides you through setting CPU and memory requests, creating a Horizontal Pod Autoscaler (HPA) for API7 Gateway, and verifying scaling behavior with a simple load test, allowing your deployment to respond dynamically to workload changes.

The instructions below assume that API7 Gateway is already installed in a Kubernetes cluster.

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

Assuming that the gateway pod is running in the current namespace, you should see its CPU and memory metrics:

```
NAME                                 CPU(cores)   MEMORY(bytes)   
api7-ee-3-gateway-7998bf6dc6-2kh7q   16m          291Mi 
```

This confirms that metrics are being collected and available for the HPA.

## Configure Resource Requests and Limits[â](#configure-resource-requests-and-limits "Direct link to Configure Resource Requests and Limits")

To ensure proper resource allocation and enable HPA to scale API7 Gateway effectively, you should set CPU and memory requests and limits for the gateway pods.

To do so, export the current Helm values of your API7 Gateway release:

```
# update with your gateway name
helm get values api7-ee-3-gateway --all > values.yaml
```

Update the resources section to include CPU and memory requests and limits. This ensures the Kubernetes scheduler can allocate sufficient resources for each pod and that HPA can monitor pod usage accurately.

The values below are example settings. In production, you should adjust CPU and memory requests and limits based on your expected traffic, workload characteristics, and cluster resources.

values.yaml

```
apisix:
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
# update with your gateway name
helm upgrade api7-ee-3-gateway api7/gateway -f values.yaml
```

## Create an HPA[â](#create-an-hpa "Direct link to Create an HPA")

Create a `HorizontalPodAutoscaler` for the gateway deployment that automatically scales the number of pods between 2 and 10. Scaling is based on average CPU usage, with a target of 50%, to accommodate varying traffic loads. Adjust the number of replicas and the CPU target as needed to match your workload and cluster resources.

gateway-hpa.yaml

```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: gateway-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api7-ee-3-gateway   # update with your gateway deployment name
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
kubectl apply -f gateway-hpa.yaml
```

View the current status of HPA in the cluster:

```
kubectl get hpa
```

You should see an output similar to the following:

```
NAME          REFERENCE                      TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 7%/50%          2         10        2          30s
```

## Verify Autoscaling with Load Test[â](#verify-autoscaling-with-load-test "Direct link to Verify Autoscaling with Load Test")

To verify autoscaling, you will start 20 load pods to generate traffic against the gateway. Alternatively, you can also use load-testing tools such as k6 or wrk.

```
# update with your gateway service name
for i in $(seq 1 20); do
  kubectl run load-$i --image=busybox:1.28 --restart=Never \
    --labels=app=loadgen \
    -- /bin/sh -c "while true; do wget -q -O- http://api7-ee-3-gateway-gateway/ >/dev/null 2>&1; done" &
done
```

In a separate terminal, watch the status of the HPA, including current metrics, replica count, and scaling activity in real time:

```
kubectl get hpa gateway-hpa -w
```

You should see the CPU utilization rising. When the load is sustained and high enough, HPA starts to scale up the gateway deployment:

```
NAME          REFERENCE                      TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 59%/50%   2         10        2          4m30s
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 37%/50%   2         10        3          7m
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 60%/50%   2         10        3          9m16s
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 62%/50%   2         10        4          9m46s
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 52%/50%   2         10        5          11m
```

To observe the deployment scale down, delete all load-generating pods:

```
kubectl delete pod -l app=loadgen
```

You should see the CPU utilization decreasing and gateway deployment scales down the number of replicas:

```
NAME          REFERENCE                      TARGETS       MINPODS   MAXPODS   REPLICAS   AGE
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 6%/50%   2         10        6          17m
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 8%/50%   2         10        6          17m
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 9%/50%   2         10        5          17m
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 7%/50%   2         10        4          18m
gateway-hpa   Deployment/api7-ee-3-gateway   cpu: 7%/50%   2         10        2          18m
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

Kubernetes provides several autoscaling strategies beyond the CPU-based approach shown in this guide. Depending on your workload characteristics, API7 Gateway can be scaled based on memory utilization, custom metrics, or a combination of multiple metrics to achieve more accurate scaling decisions. Additionally, Kubernetes allows the configuration of scaling policies to control the rate of scale-up and scale-down events, which is important for maintaining stability in production environments.

For a full overview of supported metrics, scaling behaviors, and advanced configuration options, please consult the official Kubernetes documentation:

* [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale)
* [HorizontalPodAutoscaler Walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough)
