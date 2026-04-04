# kubectl Troubleshooting Guide

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
kubectl create secret docker-registry regcred   --docker-server=<registry>   --docker-username=<username>   --docker-password=<password>   --docker-email=<email>

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
