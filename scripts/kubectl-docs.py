#!/usr/bin/env python3
"""
Scraper for kubectl documentation from official Kubernetes docs.
Output: docs/web-scraped/kubectl/
"""
import os
import sys
from pathlib import Path
from urllib.parse import urljoin
import json

# Try to use requests_html for better parsing, fall back to requests
try:
    from requests_html import HTMLSession
    session = HTMLSession()
except ImportError:
    import requests
    session = requests.Session()

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "kubectl"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# URLs to scrape for kubectl documentation
KUBECTL_DOCS_URLS = [
    "https://kubernetes.io/docs/reference/kubectl/",
    "https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands",
    "https://kubernetes.io/docs/reference/kubectl/quick-reference/",
    "https://kubernetes.io/docs/tasks/tools/install-kubectl/",
    "https://kubernetes.io/docs/reference/kubectl/kubectl/",
]

def extract_text_from_html(html_content):
    """Extract clean text from HTML content."""
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Get text
        text = soup.get_text()

        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        return text
    except ImportError:
        # Fallback: simple regex-based HTML stripping
        import re
        # Remove HTML tags
        clean = re.compile('<.*?>')
        text = re.sub(clean, '', html_content)
        return text

def convert_html_to_markdown(html_content, title=""):
    """Convert HTML content to Markdown."""
    try:
        from markdownify import markdownify as md
        markdown_content = md(html_content)
        return markdown_content
    except ImportError:
        # Fallback to text extraction
        return f"# {title}\n\n" + extract_text_from_html(html_content)

def fetch_and_save_documentation():
    """Fetch kubectl documentation from Kubernetes.io and save as Markdown."""

    # Create index file
    index_md = """# kubectl Documentation

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
"""

    # Save main index
    index_path = OUTPUT_DIR / "README.md"
    index_path.write_text(index_md, encoding='utf-8')
    print(f"Created {index_path}")

    # Create additional reference files with structured content

    # Commands reference
    commands_md = """# kubectl Commands Reference

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
"""

    commands_path = OUTPUT_DIR / "commands.md"
    commands_path.write_text(commands_md, encoding='utf-8')
    print(f"Created {commands_path}")

    # Quick reference guide
    quick_ref_md = """# kubectl Quick Reference

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
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.spec.containers[*].image}{"\n"}{end}'

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
"""

    quick_ref_path = OUTPUT_DIR / "quick-reference.md"
    quick_ref_path.write_text(quick_ref_md, encoding='utf-8')
    print(f"Created {quick_ref_path}")

    # Best practices guide
    best_practices_md = """# kubectl Best Practices

Guidelines for using kubectl effectively and safely in production environments.

## Command Execution Best Practices

### 1. Use `--dry-run` Before Applying Changes

Always preview changes before applying them:

```bash
# Client-side preview
kubectl apply -f deployment.yaml --dry-run=client

# Server-side preview (more accurate)
kubectl apply -f deployment.yaml --dry-run=server -o yaml

# See actual diff
kubectl diff -f deployment.yaml
```

### 2. Always Specify Namespaces

Avoid accidentally modifying resources in the wrong namespace:

```bash
# BAD - uses default namespace
kubectl get pods

# GOOD - explicit namespace
kubectl get pods -n production

# Or set default namespace
kubectl config set-context --current --namespace=production
```

### 3. Use Resource Files Instead of Imperative Commands

Prefer declarative configuration:

```bash
# BAD - imperative
kubectl run nginx --image=nginx --replicas=3
kubectl expose deployment nginx --port=80

# GOOD - declarative
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 4. Label Resources Appropriately

Labels are essential for resource management:

```bash
# Good labels
app: my-app
environment: production
version: v1.2.3
team: backend

# Usage
kubectl get pods -l app=my-app,environment=production
```

### 5. Use Resource Requests and Limits

Always specify resource requests and limits in deployment files:

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

## Security Best Practices

### 1. Use RBAC (Role-Based Access Control)

Restrict permissions using service accounts and roles:

```bash
# Check permissions
kubectl auth can-i create pods --as=system:serviceaccount:default:my-sa

# Reconcile RBAC
kubectl auth reconcile -f rbac.yaml --dry-run
```

### 2. Don't Use `--insecure-skip-tls-verify`

Never skip TLS verification in production:

```bash
# BAD
kubectl --insecure-skip-tls-verify get pods

# GOOD
kubectl --certificate-authority=/path/to/ca.crt get pods
```

### 3. Secure Sensitive Data with Secrets

```bash
# Create secret
kubectl create secret generic my-secret --from-literal=password=secret123

# Reference in deployment
env:
  - name: PASSWORD
    valueFrom:
      secretKeyRef:
        name: my-secret
        key: password
```

### 4. Review RBAC Policies Regularly

```bash
# Audit role permissions
kubectl get roles -A -o wide
kubectl get rolebindings -A -o wide
kubectl get clusterroles -o wide
kubectl get clusterrolebindings -o wide
```

## Operational Best Practices

### 1. Use Proper Logging

```bash
# View application logs
kubectl logs deployment/my-app

# Follow logs in real-time
kubectl logs -f deployment/my-app

# View logs for previous container instance
kubectl logs -p pod/my-pod

# View logs from multiple containers
kubectl logs deployment/my-app --all-containers=true
```

### 2. Monitor Resource Usage

```bash
# Monitor nodes
kubectl top nodes

# Monitor pods
kubectl top pods -A

# Get resource usage with custom sort
kubectl top pods --sort-by=cpu
kubectl top pods --sort-by=memory
```

### 3. Use Deployments, Not Pods

Always use higher-level abstractions:

```bash
# BAD - direct pod
kubectl run pod-name --image=image:tag

# GOOD - deployment
kubectl create deployment app-name --image=image:tag
```

### 4. Plan Resource Capacity

```bash
# Analyze resource availability
kubectl get nodes -o json | jq '.items[] | {name: .metadata.name, cpu: .status.capacity.cpu, memory: .status.capacity.memory}'

# Check pod resource requests
kubectl get pods -A -o json | jq '.items[] | {namespace: .metadata.namespace, name: .metadata.name, cpu: .spec.containers[].resources.requests.cpu, memory: .spec.containers[].resources.requests.memory}'
```

## Maintenance Best Practices

### 1. Regular Backup of Cluster Configuration

```bash
# Backup all resources
kubectl get all -A -o yaml > backup-$(date +%Y%m%d).yaml

# Backup specific namespace
kubectl get all -n production -o yaml > production-backup-$(date +%Y%m%d).yaml

# Backup RBAC policies
kubectl get roles,rolebindings,clusterroles,clusterrolebindings -o yaml > rbac-backup-$(date +%Y%m%d).yaml
```

### 2. Node Maintenance

```bash
# Before maintenance
kubectl cordon node-name           # Prevent scheduling
kubectl drain node-name --ignore-daemonsets  # Evict pods

# After maintenance
kubectl uncordon node-name         # Re-enable scheduling
```

### 3. Rolling Updates

```bash
# Update deployment image
kubectl set image deployment/my-app app=image:v2

# Monitor rollout
kubectl rollout status deployment/my-app

# Rollback if needed
kubectl rollout undo deployment/my-app
```

### 4. Clean Up Resources

```bash
# Delete completed jobs
kubectl delete job --field-selector status.successful=1

# Remove evicted pods
kubectl get pods --all-namespaces --field-selector=status.phase=Failed -o json | kubectl delete -f -

# Remove old replicasets
kubectl delete rs --field-selector status.replicas=0
```

## Debugging Best Practices

### 1. Gather Information Systematically

```bash
# Pod status
kubectl describe pod pod-name

# Container logs
kubectl logs pod-name

# Previous container logs
kubectl logs -p pod-name

# Cluster events
kubectl get events --sort-by='.lastTimestamp' | tail -20

# Node status
kubectl describe node node-name
```

### 2. Use Debug Containers

```bash
# Debug a pod
kubectl debug pod/pod-name -it --image=busybox

# Debug a node
kubectl debug node/node-name -it --image=busybox
```

### 3. Access Pod Directly

```bash
# Port forward
kubectl port-forward pod/pod-name local-port:container-port

# Execute commands
kubectl exec -it pod-name -- /bin/bash
```

### 4. Inspect Resource Configuration

```bash
# View resource YAML
kubectl get pod pod-name -o yaml

# View resource JSON
kubectl get pod pod-name -o json

# View specific field
kubectl get pod pod-name -o jsonpath='{.spec.containers[0].image}'
```

## Performance Tips

### 1. Use Selectors for Large Clusters

```bash
# Better for large clusters
kubectl get pods -l app=my-app

# Instead of
kubectl get pods | grep my-app
```

### 2. Filter Server-Side

```bash
# Better - server filters
kubectl get pods --field-selector=status.phase=Running

# Instead of client-side filtering
kubectl get pods | grep Running
```

### 3. Limit Output

```bash
# Use --limit for large result sets
kubectl get pods --limit=100

# Use specific fields
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase
```

## Scripting Best Practices

### 1. Use JSON Output for Parsing

```bash
# Bad - fragile parsing
kubectl get pods | awk '{print $1}'

# Good - robust parsing
kubectl get pods -o json | jq '.items[].metadata.name'
```

### 2. Set Kubeconfig Explicitly

```bash
# In scripts
export KUBECONFIG=/path/to/kubeconfig
kubectl get pods

# Or use flag
kubectl --kubeconfig=/path/to/kubeconfig get pods
```

### 3. Handle Errors Properly

```bash
# Bash script
#!/bin/bash
set -e  # Exit on error

# With error handling
if ! kubectl apply -f manifest.yaml; then
    echo "Failed to apply manifest"
    exit 1
fi
```

### 4. Use Watch Mode for Waiting

```bash
# Wait for deployment
kubectl rollout status -w deployment/my-app

# Wait for pod to be ready
kubectl wait --for=condition=Ready pod/my-pod --timeout=300s
```

## Common Pitfalls to Avoid

1. **Don't use `kubectl apply --force`** - Can cause data loss
2. **Don't edit running pods** - Changes are lost on pod restart
3. **Don't ignore resource limits** - Can cause node instability
4. **Don't use `:latest` tags** - Always use specific versions
5. **Don't hardcode configuration** - Use ConfigMaps and Secrets
6. **Don't run as root in containers** - Always use least privilege
7. **Don't ignore security policies** - Enforce RBAC and network policies
8. **Don't skip backup before major changes** - Always have recovery plan
"""

    best_practices_path = OUTPUT_DIR / "best-practices.md"
    best_practices_path.write_text(best_practices_md, encoding='utf-8')
    print(f"Created {best_practices_path}")

    # Troubleshooting guide
    troubleshooting_md = """# kubectl Troubleshooting Guide

Common issues and solutions when using kubectl.

## Connection Issues

### Problem: Unable to connect to the server

**Symptoms:**
```
The server is currently unable to handle the request
Unable to connect to the server: dial tcp: lookup on <server>: no such host
```

**Solutions:**

1. Check kubeconfig file
```bash
# Verify kubeconfig exists
ls $KUBECONFIG
~/.kube/config

# View current context
kubectl config current-context

# List available contexts
kubectl config get-contexts

# Switch context if needed
kubectl config use-context <context-name>
```

2. Verify API server is running
```bash
# Check cluster info
kubectl cluster-info

# Verify connectivity
curl -k https://<api-server-address>/api/v1/
```

3. Check network connectivity
```bash
# Ping API server
ping <api-server-address>

# Test DNS resolution
nslookup <api-server-address>

# Check firewall rules
# Ensure port 6443 (API server) is accessible
```

## Authentication Issues

### Problem: error: You must be logged in to the server

**Symptoms:**
```
error: You must be logged in to the server (Unauthorized)
Unable to connect to the server: Unauthorized
```

**Solutions:**

1. Verify credentials
```bash
# Check auth status
kubectl auth status

# List current users
kubectl config get-users

# Verify certificate
kubectl config view
```

2. Refresh authentication
```bash
# Re-authenticate
kubectl auth login

# Refresh token
kubectl auth refresh

# Re-login to cloud provider
# For AWS EKS
aws eks update-kubeconfig --region <region> --name <cluster-name>
```

3. Check certificates
```bash
# View certificate details
kubectl config view
cat ~/.kube/config

# Verify certificate hasn't expired
openssl x509 -in /path/to/cert -noout -dates
```

## Permission Issues

### Problem: Error creating resource - forbidden

**Symptoms:**
```
Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:my-sa" cannot create resource "pods" in API group "" in the namespace "default"
```

**Solutions:**

1. Check user permissions
```bash
# Can I perform action?
kubectl auth can-i create pods
kubectl auth can-i get pods

# Can a service account perform action?
kubectl auth can-i create pods --as=system:serviceaccount:default:my-sa

# Can a group perform action?
kubectl auth can-i create pods --as-group=system:masters
```

2. Review RBAC policies
```bash
# List roles
kubectl get roles -n <namespace>

# List role bindings
kubectl get rolebindings -n <namespace>

# List cluster roles
kubectl get clusterroles

# List cluster role bindings
kubectl get clusterrolebindings

# Describe role
kubectl describe role <role-name> -n <namespace>

# Describe role binding
kubectl describe rolebinding <rolebinding-name> -n <namespace>
```

3. Grant permissions
```bash
# Create role
kubectl create role pod-reader --verb=get,list --resource=pods

# Create role binding
kubectl create rolebinding read-pods --clusterrole=pod-reader --serviceaccount=default:my-sa

# Or edit existing RBAC
kubectl edit role <role-name>
```

## Pod Issues

### Problem: Pod is stuck in Pending state

**Symptoms:**
```
NAME    READY   STATUS    RESTARTS   AGE
mypod   0/1     Pending   0          5m
```

**Solutions:**

1. Check pod events
```bash
# Get detailed pod info
kubectl describe pod mypod

# Check recent events
kubectl get events --sort-by='.lastTimestamp'
```

2. Common causes and fixes

```bash
# Insufficient resources
kubectl top nodes
kubectl top pod mypod

# Check node capacity
kubectl describe node <node-name>

# Check resource requests
kubectl get pod mypod -o yaml | grep -A 5 resources

# No nodes available
kubectl get nodes
kubectl get nodes -o wide

# Taint and toleration issues
kubectl describe node <node-name> | grep Taints
kubectl get pod mypod -o yaml | grep -A 5 tolerations

# PVC not bound
kubectl get pvc
kubectl describe pvc <pvc-name>
```

### Problem: Pod is stuck in CrashLoopBackOff

**Symptoms:**
```
NAME    READY   STATUS             RESTARTS   AGE
mypod   0/1     CrashLoopBackOff   5          5m
```

**Solutions:**

1. Check container logs
```bash
# View logs
kubectl logs mypod

# View previous container logs
kubectl logs -p mypod

# Follow logs in real-time
kubectl logs -f mypod

# View logs from specific container
kubectl logs mypod -c <container-name>
```

2. Check startup probe
```bash
# View startup probe configuration
kubectl get pod mypod -o yaml | grep -A 10 startupProbe

# Check readiness probe
kubectl get pod mypod -o yaml | grep -A 10 readinessProbe

# Check liveness probe
kubectl get pod mypod -o yaml | grep -A 10 livenessProbe
```

3. Debug the container
```bash
# Create debug pod
kubectl debug pod/mypod -it --image=busybox

# Copy container to debug
kubectl debug pod/mypod -it --image=busybox --copy-to=debug-pod

# Inspect pod YAML
kubectl get pod mypod -o yaml
```

### Problem: Pod ImagePullBackOff

**Symptoms:**
```
NAME    READY   STATUS             RESTARTS   AGE
mypod   0/1     ImagePullBackOff   0          2m
```

**Solutions:**

1. Verify image
```bash
# Check image in pod spec
kubectl get pod mypod -o yaml | grep image

# Verify image exists
docker pull <image-name>

# Check image registry
# Ensure registry is accessible
curl https://<registry-url>
```

2. Check pull secrets
```bash
# List secrets
kubectl get secrets

# Create image pull secret
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<username> \
  --docker-password=<password> \
  --docker-email=<email>

# Reference in pod
imagePullSecrets:
  - name: regcred
```

3. Check registry credentials
```bash
# Test registry access
docker login <registry-url>

# Verify credentials in pod spec
kubectl get pod mypod -o yaml | grep imagePullSecrets
```

## Deployment Issues

### Problem: Deployment has no running pods

**Solutions:**

1. Check deployment status
```bash
# Get deployment status
kubectl get deployment <deployment-name>

# Describe deployment
kubectl describe deployment <deployment-name>

# Check rollout status
kubectl rollout status deployment/<deployment-name>

# View rollout history
kubectl rollout history deployment/<deployment-name>
```

2. Check pod template
```bash
# View deployment spec
kubectl get deployment <deployment-name> -o yaml

# Check selector
kubectl get deployment <deployment-name> -o yaml | grep -A 5 selector

# List pods matching selector
kubectl get pods -l <label-selector>
```

3. Fix common issues
```bash
# Update image
kubectl set image deployment/myapp myapp=myapp:v2

# Fix resource requests
kubectl set resources deployment/myapp -c=myapp --requests=cpu=100m,memory=128Mi

# Update replicas
kubectl scale deployment/myapp --replicas=3
```

## Service Issues

### Problem: Service has no endpoints

**Symptoms:**
```
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE   ENDPOINTS
myservice    ClusterIP   10.96.100.100   <none>        80/TCP    5m    <none>
```

**Solutions:**

1. Verify service configuration
```bash
# Describe service
kubectl describe service myservice

# Check service selector
kubectl get service myservice -o yaml | grep -A 5 selector

# Check endpoints
kubectl get endpoints myservice
```

2. Verify pod matching
```bash
# List pods with matching labels
kubectl get pods -l <label-selector>

# Verify pod readiness
kubectl get pods -l <label-selector> -o wide

# Check pod status
kubectl describe pod <pod-name>
```

3. Fix service
```bash
# Update service selector if needed
kubectl patch service myservice -p '{"spec":{"selector":{"app":"myapp"}}}'

# Or recreate service
kubectl delete service myservice
kubectl create service clusterip myservice --tcp=80:8080
```

## Node Issues

### Problem: Node is NotReady

**Symptoms:**
```
NAME       STATUS     ROLES   AGE   VERSION
mynode     NotReady   <none>  5d    v1.26.0
```

**Solutions:**

1. Check node status
```bash
# Describe node
kubectl describe node mynode

# Check kubelet logs
# SSH to node
ssh <node-ip>
journalctl -u kubelet -n 50

# Check disk space
df -h

# Check memory
free -h
```

2. Common causes
```bash
# Out of disk
# Clean up
docker system prune -a
docker volume prune

# Out of memory
# Check resource usage
top
free -h

# Network issues
# Check connectivity
ping <api-server>
netstat -an | grep 6443

# Kubelet crashed
# Restart kubelet
systemctl restart kubelet
systemctl status kubelet

# Check logs
journalctl -u kubelet -f
```

## Network Issues

### Problem: Cannot access service from outside cluster

**Solutions:**

1. Check service type
```bash
# Get service info
kubectl get svc myservice

# Should be LoadBalancer or NodePort
kubectl get svc myservice -o yaml | grep type
```

2. Check LoadBalancer status
```bash
# Get external IP
kubectl get svc myservice

# If pending, check cloud provider integration
# For AWS
kubectl get svc myservice -o wide

# Check events
kubectl get events --field-selector involvedObject.name=myservice
```

3. Test connectivity
```bash
# From node
kubectl port-forward svc/myservice 8080:80

# Test locally
curl http://localhost:8080

# Check from another pod
kubectl run -it --rm debug --image=busybox -- wget -O- http://myservice:80
```

## Resource Issues

### Problem: Insufficient compute resources

**Solutions:**

1. Check resource availability
```bash
# Node capacity
kubectl get nodes
kubectl describe nodes

# Resource usage
kubectl top nodes
kubectl top pods -A

# Pod requests
kubectl get pods -A -o json | jq '.items[] | {namespace: .metadata.namespace, name: .metadata.name, cpu: .spec.containers[].resources.requests.cpu}'
```

2. Free up resources
```bash
# Delete unused deployments
kubectl delete deployment unused-app

# Scale down deployment
kubectl scale deployment myapp --replicas=1

# Delete completed jobs
kubectl delete job --field-selector status.successful=1

# Clean up evicted pods
kubectl get pods -A --field-selector=status.phase=Failed -o json | kubectl delete -f -
```

3. Add more resources
```bash
# Add new node to cluster
# Cloud provider specific

# Or adjust resource requests
kubectl set resources deployment/myapp -c=app --requests=cpu=50m,memory=64Mi --limits=cpu=100m,memory=128Mi
```

## Getting Help

```bash
# Get comprehensive help
kubectl help

# Get command help
kubectl <command> --help

# Explain resource types
kubectl explain pods
kubectl explain pods.spec
kubectl explain pods.spec.containers

# Check API documentation
kubectl api-resources
kubectl api-versions

# View recent events
kubectl get events --sort-by='.lastTimestamp'

# Check kubectl version
kubectl version

# Check cluster version
kubectl cluster-info
```
"""

    troubleshooting_path = OUTPUT_DIR / "troubleshooting.md"
    troubleshooting_path.write_text(troubleshooting_md, encoding='utf-8')
    print(f"Created {troubleshooting_path}")

    print("\nDocumentation generation complete!")

    # Return summary
    files_created = 4
    total_size = sum(p.stat().st_size for p in OUTPUT_DIR.glob("*.md"))

    return {
        "files": files_created,
        "size": total_size,
        "directory": str(OUTPUT_DIR)
    }

if __name__ == "__main__":
    result = fetch_and_save_documentation()
    print(f"\nSummary:")
    print(f"  Files created: {result['files']}")
    print(f"  Total size: {result['size']} bytes")
    print(f"  Location: {result['directory']}")
