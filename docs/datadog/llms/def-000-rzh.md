# Source: https://docs.datadoghq.com/security/default_rules/def-000-rzh.md

---
title: Containers should not execute mount system calls
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Containers should not execute mount
  system calls
---

# Containers should not execute mount system calls

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value                                |
| ------ | ---------------------- | -------- | ------------------------------------------------ |
| 4      | 3                      | 4        | Containers should not execute mount system calls |

Containers should not be able to execute mount system calls unless explicitly required for legitimate operations. Mount operations in containers indicate potentially dangerous security configurations that weaken container isolation.

## Compliance{% #compliance %}

- Container Security requirement, [Found in CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)

## Documentation{% #documentation %}

The mount system call allows processes to attach filesystems and devices to the system's directory tree.

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

- You must have administrative access to the container runtime environment
- Access to container orchestration configuration (Kubernetes, Docker Compose, etc.)

### Step-by-step guide{% #step-by-step-guide %}

**Step 1: Identify the Container and Configuration**

Review the Finding and inspect the container's security configuration:

```bash
# List running containers
docker ps

# Check AppArmor profile (should NOT be "unconfined" or empty)
docker inspect <container_id> | jq '.[0].AppArmorProfile'

# Inspect security options
docker inspect <container_id> | jq '.[0].HostConfig.SecurityOpt'
```

**Step 2: Verify Legitimate Requirement**

Determine if mount capability is actually needed for the container's function. In most cases, it is not required.

**Step 3: Remove Dangerous Configuration**

Stop and restart the container with proper security settings:

```bash
# Stop and remove the vulnerable container
docker stop <container_id> && docker rm <container_id>

# Restart with default AppArmor profile (remove --security-opt apparmor=unconfined)
docker run --name <container_name> <image>

# Or specify a custom restrictive profile
docker run --security-opt apparmor=<custom-profile> --name <container_name> <image>
```

For Kubernetes deployments, update pod specifications to use proper AppArmor profiles:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
  annotations:
    # Use runtime/default instead of unconfined
    container.apparmor.security.beta.kubernetes.io/<container-name>: runtime/default
spec:
  securityContext:
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
```

For Kubernetes 1.25+, enforce Pod Security Standards at the namespace level:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
```

**Step 6: Verify and Audit**

Confirm the remediation was successful:

```bash
# Verify AppArmor profile is applied (should show "docker-default" or custom profile)
docker inspect <container_id> | jq '.[0].AppArmorProfile'

# Verify mount is now denied
docker exec <container_id> mount /dev/sdb1 /mnt  # Should fail

# Audit infrastructure as code for similar misconfigurations
grep -r "apparmor=unconfined" .
grep -r "apparmor.*unconfined" k8s/
```
