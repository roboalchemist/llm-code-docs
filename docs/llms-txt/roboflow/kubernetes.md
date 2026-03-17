# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/enterprise-deployment/kubernetes.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/enterprise-deployment/kubernetes.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/enterprise-deployment/kubernetes.md

# Source: https://docs.roboflow.com/deploy/enterprise-deployment/kubernetes.md

# Kubernetes

***Update: if you are a Roboflow Enterprise Customer you can deploy Roboflow Inference Service in your Kubernetes environments using*** [***this Helm chart***](https://github.com/roboflow/inference/tree/main/inference/enterprise/helm-chart)***.***

Alternatively, here are simple Kubernetes manifests to deploy a pod and service to a Kubernetes cluster.

The Kubernetes manifest below shows a simple example of creating a single CPU-based roboflow infer pod and attaching a cluster-IP service to it.

```yaml
# Pod
---
apiVersion: v1
kind: Pod
metadata:
  name: roboflow
  labels:
    app.kubernetes.io/name: roboflow
spec:
  containers:
  - name: roboflow
    image: roboflow/roboflow-inference-server-cpu
    ports:
    - containerPort: 9001
      name: rf-pod-port


# Service
---
apiVersion: v1
kind: Service
metadata:
  name: rf-service
spec:
  type: ClusterIP
  selector:
    app.kubernetes.io/name: roboflow
  ports:
  - name: rf-svc-port
    protocol: TCP
    port: 9001
    targetPort: rf-pod-port
```

(the above example assumes your Kubernetes cluster can download images from Docker hub)

Save the blurb of yaml above as `roboflow.yaml` and use the `kubectl` cli to deploy the pod and service into the default namespace of your Kubernetes cluster.

```
kubectl apply -f roboflow.yaml
```

\
A service (of type ClusterIP) will be created; you can access Roboflow inference from within the Kubernetes cluster at this URI: `http://rf-service.default.svc:9001`

### Beyond this example

Kubernetes gives you the power to incorporate several advanced features and extensions into your Roboflow inference service. For example, you could extend the above example for more advanced use-cases such as

* Using nodeSelectors to host the pod(s) on GPU machines node pools within your Kubernetes environments and using the `roboflow/inference-server:gpu` image
* Creating Kubernetes deployments to horizontally autoscale the Roboflow inference service and setting up auto-scaling triggers based on specific metrics like CPU usage.
* Using different service types like nodePort and LoadBalancer to serve the Roboflow inference service externally
* Use ingress controllers to expose Roboflow inference over TLS (HTTPs) etc.
* Add monitoring and alerting to your Roboflow inference service
* Integrating the license server and offline modes
