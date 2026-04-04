# kubectl Documentation

kubectl is the Kubernetes command-line tool, which allows you to run commands against Kubernetes clusters.

## Quick Links

- [Official kubectl Reference](https://kubernetes.io/docs/reference/kubectl/)
- [kubectl Commands Reference](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
- [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
- [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## What is kubectl?

kubectl is a command-line tool used to control Kubernetes clusters. kubectl looks for a file named config in the $HOME/.kube directory. You can specify other kubeconfig files by setting the KUBECONFIG environment variable or by setting the --kubeconfig flag.

## Basic Syntax

```
kubectl [command] [TYPE] [NAME] [flags]
```

- **command**: Specifies the operation you want to perform on one or more resources
- **TYPE**: Specifies the resource type (case-insensitive)
- **NAME**: Specifies the name of the resource (case-insensitive)
- **flags**: Specifies optional flags

## Key Concepts

### Resource Types

Common Kubernetes resource types include:
- **pods** (po)
- **services** (svc)
- **deployments** (deploy)
- **daemonsets** (ds)
- **statefulsets** (sts)
- **jobs**
- **cronjobs**
- **configmaps** (cm)
- **secrets**
- **persistentvolumes** (pv)
- **persistentvolumeclaims** (pvc)
- **namespaces** (ns)
- **nodes**
- **roles**
- **rolebindings**
- **clusterroles**
- **clusterrolebindings**

### Common Commands

#### Deployment & Cluster Management
- **create**: Create a resource from a file or stdin
- **apply**: Apply a configuration to a resource
- **delete**: Delete resources
- **get**: Display one or many resources
- **describe**: Show detailed information about a resource

#### Pod & Container Interaction
- **logs**: Print the logs for a container
- **exec**: Execute a command in a container
- **port-forward**: Forward one or more local ports to a pod
- **attach**: Attach to a running container
- **cp**: Copy files and directories to and from containers

#### Cluster Management
- **cluster-info**: Display cluster information
- **top**: Display Resource (CPU/Memory/Storage) usage
- **drain**: Drain a node in preparation for maintenance
- **cordon**: Mark node as unschedulable
- **uncordon**: Mark node as schedulable
- **taint**: Update the taints on one or more nodes

#### Configuration & Scaling
- **scale**: Set a new size for a Deployment, ReplicaSet, or StatefulSet
- **autoscale**: Auto-scale a Deployment, ReplicaSet, or StatefulSet
- **set**: Set specific features on objects
- **patch**: Update field(s) of a resource using strategic merge patch
- **edit**: Edit a resource on the server
- **label**: Update the labels on a resource
- **annotate**: Update the annotations on a resource

#### Rollout Management
- **rollout status**: Show the status of the rollout
- **rollout history**: View rollout history
- **rollout undo**: Undo a previous rollout
- **rollout restart**: Restart a rollout
- **rollout pause/resume**: Pause/resume a rollout

### Flags & Options

#### Namespace & Context
- `-n, --namespace`: Specify the namespace
- `-A, --all-namespaces`: List resources across all namespaces
- `--context`: Specify the context to use

#### Output Formats
- `-o, --output`: Output format (json, yaml, name, wide, custom-columns, etc.)
- `--sort-by`: Sort list results by a specific field
- `--show-labels`: Show labels on output resources

#### Selection
- `-l, --selector`: Label selector
- `--field-selector`: Field selector

#### File Operations
- `-f, --filename`: Filename, directory, or URL to files
- `-k, --kustomize`: Process the kustomization directory
- `-R, --recursive`: Process directory recursively

#### Advanced Options
- `--dry-run`: Options are "none", "client", or "server"
- `--watch, -w`: Watch for changes
- `--force`: Force deletion (grace period = 0)
- `--grace-period`: Period of time in seconds given to the resource to terminate
- `--timeout`: The length of time to wait before giving up
- `-v, --v`: Set the level of log output

## Common Workflows

### View Resources
```bash
kubectl get pods                          # List pods in current namespace
kubectl get pods -n kube-system           # List pods in specific namespace
kubectl get pods --all-namespaces         # List pods in all namespaces
kubectl get pods -o wide                  # Show additional information
kubectl describe pod <pod-name>           # Show detailed pod information
```

### Deploy Applications
```bash
kubectl apply -f deployment.yaml          # Create/update deployment
kubectl create deployment nginx --image=nginx  # Quick deployment creation
kubectl set image deployment/nginx nginx=nginx:1.14  # Update image
kubectl rollout status deployment/nginx   # Check rollout status
```

### Access Containers
```bash
kubectl logs <pod-name>                   # View pod logs
kubectl logs -f <pod-name>                # Stream pod logs
kubectl exec -it <pod-name> -- /bin/bash  # Open interactive shell
kubectl exec <pod-name> -- <command>      # Run command in pod
kubectl port-forward pod/<pod> 5000:8000  # Forward port
```

### Scale & Update
```bash
kubectl scale deployment nginx --replicas=3  # Scale deployment
kubectl autoscale deployment nginx --min=1 --max=10  # Enable autoscaling
kubectl set env deployment/nginx ENV_VAR=value  # Set environment variable
kubectl patch deployment nginx -p '{"spec":{"replicas":5}}'  # Patch resource
```

### Node Management
```bash
kubectl get nodes                         # List cluster nodes
kubectl describe node <node-name>         # Show node details
kubectl cordon <node-name>                # Make node unschedulable
kubectl drain <node-name>                 # Evict pods from node
kubectl uncordon <node-name>              # Make node schedulable
```

### Configuration Management
```bash
kubectl config view                       # Show kubeconfig
kubectl config current-context            # Show current context
kubectl config use-context <context>      # Switch context
kubectl config set-context --current --namespace=<ns>  # Change namespace
```

### Debugging & Troubleshooting
```bash
kubectl describe pod <pod-name>           # Get pod details
kubectl logs <pod-name>                   # View container logs
kubectl exec -it <pod-name> -- /bin/bash  # Access container
kubectl get events --sort-by='.lastTimestamp'  # View events
kubectl top node                          # Show node resource usage
kubectl top pod                           # Show pod resource usage
```

## Exit Codes

kubectl returns the following exit codes:
- **0**: Success
- **1**: General errors
- **2**: Misuse of shell command

## Environment Variables

- **KUBECONFIG**: Set the kubeconfig file to use
- **KUBECTL_PLUGINS_PATH**: Set the plugin directory path
- **KUBECTL_PLUGINS_DESCRIPTOR_VERSION**: Set the plugin descriptor version

## Documentation Sources

- [Official Kubernetes Documentation](https://kubernetes.io/docs/)
- [kubectl Reference](https://kubernetes.io/docs/reference/kubectl/)
- [kubectl Command Reference](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
- [Kubernetes API Reference](https://kubernetes.io/docs/reference/kubernetes-api/)
