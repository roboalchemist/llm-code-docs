# Source: https://docs.datadoghq.com/security/default_rules/def-000-krp.md

---
title: Containers should not execute compilers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Containers should not execute compilers
---

# Containers should not execute compilers

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value                                                   |
| ------ | ---------------------- | -------- | ------------------------------------------------------------------- |
| 3      | 2                      | 3        | No compilers should be present or executed in production containers |

Compilers should not be present or executed in production containers. Container images should be built with pre-compiled binaries and follow immutable infrastructure principles.

## Compliance{% #compliance %}

- Remove unnecessary packages from containers ([found in CIS](https://www.cisecurity.org/cis-benchmarks))

## Documentation{% #documentation %}

Compilers such as `gcc`, `g++`, `clang`, `javac`, `rustc`, and others are development tools used to compile source code into executable binaries. In containerized production environments, compilers should not be present because containers should follow immutable infrastructure principles where all binaries are pre-compiled during the image build process.

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

You must have:

- Access to the container runtime (Docker, containerd, etc.)
- Access to container logs and host system audit logs
- Knowledge of container deployment and CI/CD pipeline
- Understanding of container image build processes
- Agent v7.27 or newer for Workload Security monitoring

### Step-by-step guide{% #step-by-step-guide %}

#### Step 1: Investigate the compiler execution{% #step-1-investigate-the-compiler-execution %}

Identify which compiler was executed and in which container:

**Docker:**

```bash
# Identify the container where compiler was executed
docker ps -a
docker inspect [container_id]

# Review container logs for compiler activity
docker logs [container_id] --tail 100

# Check what compiler was executed
docker exec [container_id] ps aux | grep -E "gcc|g\+\+|clang|javac|rustc|go build"

# Review container processes
docker top [container_id]

# Check for compilation artifacts
docker exec [container_id] find / -name "*.o" -o -name "*.so" -o -name "a.out" 2>/dev/null
```

**Kubernetes:**

```bash
# Identify the pod and container where compiler was executed
kubectl get pods -A
kubectl describe pod [pod_name] -n [namespace]

# Review container logs for compiler activity
kubectl logs [pod_name] -n [namespace] -c [container_name] --tail=100

# Check what compiler was executed
kubectl exec [pod_name] -n [namespace] -c [container_name] -- ps aux | grep -E "gcc|g\+\+|clang|javac|rustc|go build"

# Review container processes
kubectl exec [pod_name] -n [namespace] -c [container_name] -- ps aux

# Check for compilation artifacts
kubectl exec [pod_name] -n [namespace] -c [container_name] -- find / -name "*.o" -o -name "*.so" -o -name "a.out" 2>/dev/null
```

#### Step 2: Assess container image{% #step-2-assess-container-image %}

Determine if compilers are part of the base image or were installed at runtime:

**Docker:**

```bash
# Review container image layers
docker history [image_id]

# Check if compiler is in the base image
docker run --rm [image_id] which gcc g++ clang javac

# List installed packages in container
docker exec [container_id] dpkg -l | grep -E "gcc|g\+\+|clang|build-essential"
docker exec [container_id] rpm -qa | grep -E "gcc|g\+\+|clang"

# Check for recent package installations
docker diff [container_id]
```

**Kubernetes:**

```bash
# Get the image used by the pod
kubectl get pod [pod_name] -n [namespace] -o jsonpath='{.spec.containers[*].image}'

# Review container image layers (requires local image or registry access)
docker history [image_name]

# Check if compiler is in the base image
kubectl run temp-check --rm -i --restart=Never --image=[image_name] -- which gcc g++ clang javac

# List installed packages in container
kubectl exec [pod_name] -n [namespace] -c [container_name] -- dpkg -l | grep -E "gcc|g\+\+|clang|build-essential"
kubectl exec [pod_name] -n [namespace] -c [container_name] -- rpm -qa | grep -E "gcc|g\+\+|clang"

# Check pod events for anomalies
kubectl get events -n [namespace] --field-selector involvedObject.name=[pod_name]
```
