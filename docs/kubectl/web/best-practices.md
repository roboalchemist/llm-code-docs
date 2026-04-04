# kubectl Best Practices

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
