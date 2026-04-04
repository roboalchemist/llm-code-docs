# kubectl Quick Reference

Fast lookup for common kubectl commands and patterns.

## Installation & Setup

### Install kubectl

```bash
# macOS
brew install kubectl

# Linux (using curl)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Windows (using Chocolatey)
choco install kubernetes-cli

# Using package manager
# Ubuntu/Debian
sudo apt-get install -y kubectl

# RHEL/CentOS
sudo yum install -y kubectl
```

### Verify Installation

```bash
kubectl version --client
kubectl cluster-info
```

## Autocompletion

### Bash

```bash
# Permanent setup
echo 'source <(kubectl completion bash)' >> ~/.bashrc
source ~/.bashrc
```

### Zsh

```bash
# Permanent setup
echo 'source <(kubectl completion zsh)' >> ~/.zshrc
source ~/.zshrc
```

### Fish

```bash
# Permanent setup
echo 'kubectl completion fish | source' > ~/.config/fish/completions/kubectl.fish
source ~/.config/fish/completions/kubectl.fish
```

## Context & Kubeconfig

```bash
kubectl config view                        # Show merged kubeconfig
kubectl config current-context             # Show current context
kubectl config use-context CONTEXT_NAME    # Change context
kubectl config delete-context CONTEXT_NAME # Delete context
kubectl config rename-context OLD NEW      # Rename context
kubectl config set-context --current --namespace=NAMESPACE  # Set default namespace
kubectl config get-clusters                # List clusters
kubectl config get-contexts                # List contexts
```

## Viewing Resources

### List Resources

```bash
kubectl get pods                           # List pods
kubectl get svc                            # List services
kubectl get deploy                         # List deployments
kubectl get nodes                          # List nodes
kubectl get all                            # List all resources
kubectl get pods -A                        # All namespaces
kubectl get pods -n NAMESPACE              # Specific namespace
kubectl get pods -o wide                   # Extended output
kubectl get pods -o yaml                   # YAML output
kubectl get pods -o json                   # JSON output
kubectl get pods --sort-by=.metadata.name  # Sort by field
kubectl get pods -l app=nginx              # By label
kubectl get pods --field-selector=status.phase=Running  # By field
```

### Describe Resources

```bash
kubectl describe pod POD_NAME               # Pod details
kubectl describe node NODE_NAME             # Node details
kubectl describe svc SERVICE_NAME           # Service details
kubectl describe all                        # All resources
```

## Creating Resources

### From YAML Files

```bash
kubectl apply -f FILE.yaml                 # Create or update
kubectl apply -f DIRECTORY/                # Create from directory
kubectl create -f FILE.yaml                # Create (fails if exists)
kubectl apply -k KUSTOMIZATION_DIR/        # Apply kustomization
```

### From Command Line

```bash
kubectl run POD_NAME --image=IMAGE         # Run pod
kubectl create deployment NAME --image=IMAGE  # Create deployment
kubectl create service clusterip NAME --tcp=8080:8080  # Create service
kubectl expose deployment NAME --type=LoadBalancer --port=80  # Expose deployment
```

## Pod Management

### Container Access

```bash
kubectl logs POD_NAME                      # View logs
kubectl logs -f POD_NAME                   # Stream logs
kubectl logs POD_NAME -c CONTAINER         # Specific container
kubectl logs POD_NAME --tail=N              # Last N lines
kubectl logs POD_NAME --since=1h            # Last hour logs

kubectl exec POD_NAME -- COMMAND           # Run command
kubectl exec -it POD_NAME -- /bin/bash      # Interactive shell
kubectl exec POD_NAME -c CONTAINER -- CMD  # In specific container

kubectl attach POD_NAME -it                # Attach to container
kubectl port-forward POD_NAME LOCAL:REMOTE # Forward port
kubectl cp POD_NAME:/PATH ./LOCAL_PATH     # Copy from pod
kubectl cp ./LOCAL_PATH POD_NAME:/PATH     # Copy to pod
```

## Deployment Management

### Scaling & Updating

```bash
kubectl scale deployment NAME --replicas=N   # Scale deployment
kubectl autoscale deployment NAME --min=1 --max=10  # Autoscale
kubectl set image deployment/NAME CONTAINER=IMAGE   # Update image
kubectl set env deployment/NAME VAR=VALUE          # Set env var
kubectl rollout status deployment/NAME             # Check status
kubectl rollout history deployment/NAME            # View history
kubectl rollout undo deployment/NAME               # Rollback
kubectl rollout undo deployment/NAME --to-revision=N  # To specific revision
kubectl rollout restart deployment/NAME            # Restart
kubectl rollout pause deployment/NAME              # Pause rollout
kubectl rollout resume deployment/NAME             # Resume rollout
```

## Node Management

### Node Operations

```bash
kubectl get nodes                          # List nodes
kubectl describe node NODE_NAME            # Node details
kubectl get nodes -L LABEL_NAME            # Show label column
kubectl top node                           # Resource usage
kubectl top node NODE_NAME                 # Node resource usage

kubectl cordon NODE_NAME                   # Make unschedulable
kubectl uncordon NODE_NAME                 # Make schedulable
kubectl drain NODE_NAME                    # Drain for maintenance
kubectl drain NODE_NAME --force            # Force drain (ignore errors)
kubectl drain NODE_NAME --ignore-daemonsets  # Ignore daemonsets

kubectl taint nodes NODE_NAME KEY=VALUE:EFFECT  # Add taint
kubectl taint nodes NODE_NAME KEY:EFFECT-      # Remove taint
```

## Resource Management

### Labels & Annotations

```bash
kubectl label pods POD_NAME KEY=VALUE       # Add label
kubectl label --overwrite pods POD_NAME KEY=VALUE  # Update label
kubectl label pods POD_NAME KEY-             # Remove label
kubectl label nodes NODE_NAME KEY=VALUE     # Label node

kubectl annotate pods POD_NAME KEY=VALUE    # Add annotation
kubectl annotate --overwrite pods POD_NAME KEY=VALUE  # Update
kubectl annotate pods POD_NAME KEY-         # Remove annotation
```

### Patching & Editing

```bash
kubectl patch pod POD_NAME -p '{"spec":{"KEY":"VALUE"}}'  # Patch
kubectl edit pod POD_NAME                  # Edit in editor
kubectl apply -f FILE.yaml                 # Apply changes
kubectl replace -f FILE.yaml               # Replace resource
```

## Deletion

```bash
kubectl delete pod POD_NAME                # Delete pod
kubectl delete pods POD1 POD2              # Delete multiple
kubectl delete -f FILE.yaml                # Delete from file
kubectl delete pods --all                  # Delete all pods
kubectl delete pods -l KEY=VALUE           # By label
kubectl delete pod POD_NAME --now          # No grace period
kubectl delete pod POD_NAME --grace-period=0 --force  # Force delete
```

## Debugging & Troubleshooting

### Information

```bash
kubectl describe pod POD_NAME               # Pod details
kubectl logs POD_NAME                       # Container logs
kubectl logs -p POD_NAME                    # Previous container logs
kubectl get events --sort-by='.lastTimestamp'  # Cluster events
kubectl api-resources                      # Available resources
kubectl explain RESOURCE_TYPE               # Resource documentation
```

### Advanced Debugging

```bash
kubectl debug pod/POD_NAME -it --image=busybox  # Debug pod
kubectl debug node/NODE_NAME -it --image=busybox  # Debug node
kubectl get pod POD_NAME -o yaml           # Full pod YAML
kubectl diff -f FILE.yaml                  # Show differences
```

## Cluster Information

```bash
kubectl cluster-info                       # Cluster details
kubectl cluster-info dump                  # Dump cluster state
kubectl version                            # kubectl & server version
kubectl api-versions                       # Supported API versions
kubectl api-resources                      # Supported resources
kubectl auth can-i ACTION RESOURCE         # Check permissions
```

## Output Formatting

### Common Output Options

```bash
kubectl get pods -o json                   # JSON output
kubectl get pods -o yaml                   # YAML output
kubectl get pods -o wide                   # Extended table
kubectl get pods -o name                   # Just names
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase  # Custom
kubectl get pods -o jsonpath='{.items[*].metadata.name}'  # JSONPath
kubectl get pods -o go-template='{{.items[0].metadata.name}}'  # Go template
```

### Filtering & Sorting

```bash
kubectl get pods --sort-by=.metadata.name  # Sort by field
kubectl get pods -l KEY=VALUE              # Filter by label
kubectl get pods --field-selector=status.phase=Running  # Filter by field
kubectl get pods --all-namespaces          # All namespaces
```

## Helpful Tips

### Aliases

```bash
alias k=kubectl
alias kg='kubectl get'
alias kd='kubectl describe'
alias kl='kubectl logs'
alias kex='kubectl exec'
alias kaf='kubectl apply -f'
alias kdel='kubectl delete'
```

### Common Patterns

```bash
# List all pods with labels and nodes
kubectl get pods -A -o wide

# Find pods by image name
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"	"}{.metadata.name}{"	"}{.spec.containers[*].image}{"
"}{end}'

# Get resource usage
kubectl top nodes
kubectl top pods -A

# Find pods not running
kubectl get pods -A --field-selector=status.phase!=Running

# Get all resources in namespace
kubectl get all -n NAMESPACE

# Port forward to access service locally
kubectl port-forward -n NAMESPACE svc/SERVICE_NAME LOCAL_PORT:REMOTE_PORT
```

### Dry Run

```bash
kubectl run POD --image=IMAGE --dry-run=client              # Preview pod creation
kubectl apply -f FILE.yaml --dry-run=client                 # Preview apply
kubectl apply -f FILE.yaml --dry-run=server                 # Server-side preview
```

### Watch Mode

```bash
kubectl get pods -w                        # Watch pods
kubectl rollout status -w deployment/NAME  # Watch rollout
```

## Environment Variables

```bash
KUBECONFIG        # Path to kubeconfig file(s)
KUBECTL_PLUGINS_PATH  # Plugin directory path
KUBECTL_PLUGINS_DESCRIPTOR_VERSION  # Plugin descriptor version
```

## Useful Resources

- [Official kubectl Documentation](https://kubernetes.io/docs/reference/kubectl/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
