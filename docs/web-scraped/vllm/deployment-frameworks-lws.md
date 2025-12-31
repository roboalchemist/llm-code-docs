# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/lws/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/lws.md "Edit this page")

# LWS[¶](#lws "Permanent link")

LeaderWorkerSet (LWS) is a Kubernetes API that aims to address common deployment patterns of AI/ML inference workloads. A major use case is for multi-host/multi-node distributed inference.

vLLM can be deployed with [LWS](https://github.com/kubernetes-sigs/lws) on Kubernetes for distributed model serving.

## Prerequisites[¶](#prerequisites "Permanent link")

-   At least two Kubernetes nodes, each with 8 GPUs, are required.
-   Install LWS by following the instructions found [here](https://lws.sigs.k8s.io/docs/installation/).

## Deploy and Serve[¶](#deploy-and-serve "Permanent link")

Deploy the following yaml file `lws.yaml`

Yaml

    apiVersion: leaderworkerset.x-k8s.io/v1
    kind: LeaderWorkerSet
    metadata:
      name: vllm
    spec:
      replicas: 1
      leaderWorkerTemplate:
        size: 2
        restartPolicy: RecreateGroupOnPodRestart
        leaderTemplate:
          metadata:
            labels:
              role: leader
          spec:
            containers:
              - name: vllm-leader
                image: docker.io/vllm/vllm-openai:latest
                env:
                  - name: HF_TOKEN
                    value: <your-hf-token>
                command:
                  - sh
                  - -c
                  - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=$(LWS_GROUP_SIZE); 
                    vllm serve meta-llama/Meta-Llama-3.1-405B-Instruct --port 8080 --tensor-parallel-size 8 --pipeline_parallel_size 2"
                resources:
                  limits:
                    nvidia.com/gpu: "8"
                    memory: 1124Gi
                    ephemeral-storage: 800Gi
                  requests:
                    ephemeral-storage: 800Gi
                    cpu: 125
                ports:
                  - containerPort: 8080
                readinessProbe:
                  tcpSocket:
                    port: 8080
                  initialDelaySeconds: 15
                  periodSeconds: 10
                volumeMounts:
                  - mountPath: /dev/shm
                    name: dshm
            volumes:
            - name: dshm
              emptyDir:
                medium: Memory
                sizeLimit: 15Gi
        workerTemplate:
          spec:
            containers:
              - name: vllm-worker
                image: docker.io/vllm/vllm-openai:latest
                command:
                  - sh
                  - -c
                  - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh worker --ray_address=$(LWS_LEADER_ADDRESS)"
                resources:
                  limits:
                    nvidia.com/gpu: "8"
                    memory: 1124Gi
                    ephemeral-storage: 800Gi
                  requests:
                    ephemeral-storage: 800Gi
                    cpu: 125
                env:
                  - name: HF_TOKEN
                    value: <your-hf-token>
                volumeMounts:
                  - mountPath: /dev/shm
                    name: dshm   
            volumes:
            - name: dshm
              emptyDir:
                medium: Memory
                sizeLimit: 15Gi
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: vllm-leader
    spec:
      ports:
        - name: http
          port: 8080
          protocol: TCP
          targetPort: 8080
      selector:
        leaderworkerset.sigs.k8s.io/name: vllm
        role: leader
      type: ClusterIP

    kubectl apply -f lws.yaml

Verify the status of the pods:

    kubectl get pods

Should get an output similar to this:

    NAME       READY   STATUS    RESTARTS   AGE
    vllm-0     1/1     Running   0          2s
    vllm-0-1   1/1     Running   0          2s

Verify that the distributed tensor-parallel inference works:

    kubectl logs vllm-0 |grep -i "Loading model weights took" 

Should get something similar to this:

    INFO 05-08 03:20:24 model_runner.py:173] Loading model weights took 0.1189 GB
    (RayWorkerWrapper pid=169, ip=10.20.0.197) INFO 05-08 03:20:28 model_runner.py:173] Loading model weights took 0.1189 GB

## Access ClusterIP service[¶](#access-clusterip-service "Permanent link")

    # Listen on port 8080 locally, forwarding to the targetPort of the service's port 8080 in a pod selected by the service
    kubectl port-forward svc/vllm-leader 8080:8080

The output should be similar to the following:

    Forwarding from 127.0.0.1:8080 -> 8080
    Forwarding from [::1]:8080 -> 8080

## Serve the model[¶](#serve-the-model "Permanent link")

Open another terminal and send a request

    curl http://localhost:8080/v1/completions \
    -H "Content-Type: application/json" \
    -d ''

The output should be similar to the following

Output

    
      ],
      "usage": 
    }

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 16, 2025] ]