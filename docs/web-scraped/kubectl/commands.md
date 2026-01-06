# kubectl Commands Reference

This is a comprehensive reference for all kubectl commands organized by category.

## Table of Contents

1. [Basic Commands](#basic-commands)
2. [Deployment Commands](#deployment-commands)
3. [Cluster Management](#cluster-management)
4. [Troubleshooting and Debugging](#troubleshooting-and-debugging)
5. [Advanced Commands](#advanced-commands)
6. [Settings Commands](#settings-commands)

## Basic Commands

### get

Display one or many resources.

```bash
kubectl get pods
kubectl get pods -o wide
kubectl get pods -n kube-system
kubectl get deployments,services
kubectl get pods --all-namespaces
kubectl get pods -l app=nginx
kubectl get pods --sort-by=.metadata.creationTimestamp
```

### create

Create a resource from a file or stdin.

```bash
kubectl create -f pod.yaml
kubectl create deployment nginx --image=nginx
kubectl create service clusterip my-service --tcp=5678:8080
kubectl create configmap my-config --from-literal=key=value
kubectl create secret generic my-secret --from-literal=password=secret
```

### apply

Apply a configuration to a resource by filename or stdin.

```bash
kubectl apply -f pod.yaml
kubectl apply -f .
kubectl apply -k ./kustomization/
cat pod.yaml | kubectl apply -f -
kubectl apply --dry-run=client -f pod.yaml
```

### delete

Delete resources by filenames, stdin, resources and names, or by resources and label selector.

```bash
kubectl delete pod my-pod
kubectl delete pods,services -l app=nginx
kubectl delete -f pod.yaml
kubectl delete pod my-pod --now
kubectl delete pod my-pod --force --grace-period=0
```

### describe

Show details of a specific resource or group of resources.

```bash
kubectl describe pod my-pod
kubectl describe nodes
kubectl describe svc my-service
kubectl describe deployment my-deployment
```

### logs

Print the logs for a container in a pod.

```bash
kubectl logs my-pod
kubectl logs my-pod -c container-name
kubectl logs my-pod -f
kubectl logs my-pod --tail=100
kubectl logs my-pod --since=1h
```

### exec

Execute a command in a container.

```bash
kubectl exec my-pod -- ls /
kubectl exec -it my-pod -- /bin/bash
kubectl exec my-pod -c container-name -- date
kubectl exec deployment/my-app -- date
```

## Deployment Commands

### create deployment

Create a deployment with a specified image.

```bash
kubectl create deployment nginx --image=nginx
kubectl create deployment nginx --image=nginx --replicas=3
kubectl create deployment nginx --image=nginx:1.14
```

### rollout

Manage the rollout of a resource.

```bash
kubectl rollout status deployment/nginx
kubectl rollout history deployment/nginx
kubectl rollout undo deployment/nginx
kubectl rollout undo deployment/nginx --to-revision=2
kubectl rollout restart deployment/nginx
kubectl rollout pause deployment/nginx
kubectl rollout resume deployment/nginx
```

### scale

Set a new size for a Deployment, ReplicaSet, Replication Controller, or Stateful Set.

```bash
kubectl scale deployment nginx --replicas=3
kubectl scale statefulset mysql --replicas=5
kubectl scale rs foo --replicas=3 --current-replicas=2
```

### autoscale

Autoscale a Deployment, ReplicaSet, or Replication Controller.

```bash
kubectl autoscale deployment nginx --min=1 --max=10
kubectl autoscale deployment nginx --min=2 --max=5 --cpu-percent=80
```

### set image

Update image of a pod template.

```bash
kubectl set image deployment/nginx nginx=nginx:1.14
kubectl set image deployment/nginx nginx=nginx:1.14 --record
```

### set env

Update environment variables.

```bash
kubectl set env deployment/nginx MYVAR=myvalue
kubectl set env deployment/nginx MYVAR-
```

### patch

Update one or more fields of a resource.

```bash
kubectl patch pod my-pod -p '{"spec":{"containers":[{"name":"nginx","image":"nginx:1.14"}]}}'
kubectl patch deployment nginx -p '{"spec":{"replicas":5}}'
```

### replace

Replace a resource by filename or stdin.

```bash
kubectl replace -f pod.yaml
kubectl replace -f pod.yaml --force --grace-period=0
```

## Cluster Management

### cluster-info

Display addresses of the master and services with label kubernetes.io/cluster-service=true.

```bash
kubectl cluster-info
kubectl cluster-info dump
kubectl cluster-info dump --output-directory=/path/to/cluster-state
```

### nodes

Get information about nodes.

```bash
kubectl get nodes
kubectl get nodes -o wide
kubectl describe node my-node
kubectl top node
kubectl top node my-node
```

### drain

Drain a node in preparation for maintenance.

```bash
kubectl drain my-node
kubectl drain my-node --force
kubectl drain my-node --grace-period=900
kubectl drain my-node --ignore-daemonsets
```

### cordon

Mark a node as unschedulable.

```bash
kubectl cordon my-node
```

### uncordon

Mark a node as schedulable.

```bash
kubectl uncordon my-node
```

### taint

Update taints on one or more nodes.

```bash
kubectl taint nodes my-node key=value:NoSchedule
kubectl taint nodes my-node key=value:NoExecute
kubectl taint nodes my-node key=value:PreferNoSchedule
kubectl taint nodes my-node key:NoSchedule-
```

## Troubleshooting and Debugging

### describe

Show detailed information about a resource.

```bash
kubectl describe pod my-pod
kubectl describe node my-node
kubectl describe service my-service
```

### logs

View container logs.

```bash
kubectl logs my-pod
kubectl logs my-pod -c container-name
kubectl logs my-pod -f
kubectl logs my-pod --tail=50
kubectl logs my-pod --since=10m
```

### exec

Execute a command inside a container.

```bash
kubectl exec -it my-pod -- /bin/bash
kubectl exec my-pod -- ps aux
kubectl exec my-pod -c container-name -- ls /
```

### port-forward

Forward local port to a pod or service.

```bash
kubectl port-forward pod/my-pod 5000:8080
kubectl port-forward svc/my-service 5000:8080
kubectl port-forward deployment/my-app 5000:8080
```

### attach

Attach to a running container.

```bash
kubectl attach pod/my-pod -it
kubectl attach deployment/my-app -it
```

### cp

Copy files and directories to and from containers.

```bash
kubectl cp pod/my-pod:/path/to/file ./local-file
kubectl cp ./local-file pod/my-pod:/path/to/file
kubectl cp namespace/my-pod:/path/to/file ./local-file
```

### events

Show events in the cluster.

```bash
kubectl get events
kubectl get events --all-namespaces
kubectl get events --sort-by='.lastTimestamp'
```

## Advanced Commands

### label

Update labels on resources.

```bash
kubectl label pods my-pod app=nginx
kubectl label --overwrite pods my-pod app=apache
kubectl label pods my-pod app-
kubectl label nodes my-node gpu=true
```

### annotate

Update annotations on resources.

```bash
kubectl annotate pods my-pod description='My pod'
kubectl annotate --overwrite pods my-pod description='Updated'
kubectl annotate pods my-pod description-
```

### auth

Inspect authorization.

```bash
kubectl auth can-i create pods
kubectl auth can-i create pods --as=system:serviceaccount:default:my-sa
kubectl auth reconcile -f rbac.yaml
```

### debug

Create debugging sessions for troubleshooting workloads and nodes.

```bash
kubectl debug pod/my-pod -it --image=busybox
kubectl debug node/my-node -it --image=busybox
```

### wait

Wait for conditions on resources.

```bash
kubectl wait --for=condition=Ready pod/my-pod
kubectl wait --for=jsonpath='{.status.phase}'=Running pod/my-pod
kubectl wait --for=delete pod/my-pod --timeout=60s
```

### diff

Show differences between desired and live state.

```bash
kubectl diff -f pod.yaml
kubectl diff -k ./kustomization/
```

## Settings Commands

### config

Configure kubeconfig.

```bash
kubectl config view
kubectl config current-context
kubectl config use-context my-context
kubectl config set-context --current --namespace=my-ns
kubectl config get-clusters
kubectl config get-contexts
```

### explain

Get documentation for a resource.

```bash
kubectl explain pods
kubectl explain pods.spec
kubectl explain pods.spec.containers
```

### version

Show version information.

```bash
kubectl version
kubectl version --client
kubectl version --short
```

### api-resources

Print supported API resources.

```bash
kubectl api-resources
kubectl api-resources -o wide
kubectl api-resources --sort-by=name
kubectl api-resources --namespaced=true
```

### api-versions

Print supported API versions.

```bash
kubectl api-versions
```

### completion

Generate shell completion code.

```bash
kubectl completion bash
kubectl completion zsh
kubectl completion fish
kubectl completion powershell
```

### plugin

List and manage kubectl plugins.

```bash
kubectl plugin list
```

## Global Flags

These flags are available for all commands:

```
      --as string                      Username to impersonate
      --as-group stringArray           Group to impersonate
      --cache-dir string               Default cache directory (default $HOME/.kube/cache)
      --certificate-authority string   Path to a cert file for CA authority
      --client-certificate string      Path to a client certificate file
      --client-key string              Path to a client key file
      --cluster string                 Cluster name to use
      --context string                 Context name to use
      --insecure-skip-tls-verify       Skip TLS verification
      --kubeconfig string              Kubeconfig file (default $HOME/.kube/config)
      --match-server-version          Require server version match
  -n, --namespace string              Namespace scope
      --password string                Password for basic auth
      --request-timeout string         Request timeout
      --server string                  Kubernetes API server URL
      --tls-server-name string         Server name for TLS validation
      --token string                   Bearer token for auth
      --user string                    User context to use
      --username string                Username for basic auth
  -v, --v Level                        Log level (0-9)
```
