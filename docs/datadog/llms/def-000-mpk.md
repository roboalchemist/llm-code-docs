# Source: https://docs.datadoghq.com/security/default_rules/def-000-mpk.md

---
title: Verify Essential Linux Binary Modified in Container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Essential Linux Binary Modified
  in Container
---

# Verify Essential Linux Binary Modified in Container

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value             |
| ------ | ---------------------- | -------- | ----------------------------- |
| 2      | 3                      | 2        | No unauthorized modifications |

Essential system binaries in containers should remain unchanged unless modifications are part of authorized container image updates or patches. Container images should be immutable, and any binary modifications detected at runtime may indicate a compromise or drift from the intended image state.

## Compliance{% #compliance %}

- File Integrity Monitoring requirement, [Found in PCI DSS 11.5](https://www.pcisecuritystandards.org/)

## Documentation{% #documentation %}

Essential system binaries in containers are executable files that perform operating system functions and administrative tasks. These binaries typically reside in protected system directories such as `/bin`, `/sbin`, `/usr/bin`, and `/usr/sbin`. In containerized environments, these binaries are part of the container image layers and should be immutable during runtime. Any modification to these binaries in a running container may indicate container escape attempts, runtime tampering, or unauthorized access.

File Integrity Monitoring (FIM) tracks changes to essential system files by monitoring various file operations including:

- **chmod**: Permission changes that could weaken security controls or grant unauthorized access
- **chown**: Ownership changes that could allow unauthorized users to control critical binaries
- **link**: Creation of hard or symbolic links that could redirect execution to malicious code
- **rename**: Moving or renaming binaries, potentially to hide malicious replacements
- **open**: File modifications that alter the binary's behavior or inject malicious code
- **unlink**: Deletion of critical binaries, potentially as part of an attack to disable security controls
- **utimes**: Timestamp modifications that could be used to hide evidence of tampering

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

- Access to the container runtime (Docker, containerd, etc.)
- Ability to execute commands within the container
- Access to container logs and audit trails
- Reference to the original container image or image digest
- Access to the container orchestration platform (if applicable)

### Step-by-step guide{% #step-by-step-guide %}

**Step 1: Identify Modified Binary**

Review the Finding to determine which essential Linux binary was modified in the container and the nature of the change:

```bash
# Get container ID from the Finding
CONTAINER_ID=<container-id>

# Check file details within the container
docker exec $CONTAINER_ID ls -l /path/to/modified/binary
docker exec $CONTAINER_ID stat /path/to/modified/binary

# For Kubernetes environments
kubectl exec <pod-name> -c <container-name> -- ls -l /path/to/modified/binary
kubectl exec <pod-name> -c <container-name> -- stat /path/to/modified/binary
```

**Step 2: Verify Against Original Image**

Compare the modified binary against the original container image to determine if the change was introduced at runtime:

```bash
# Get the image used by the container
IMAGE=$(docker inspect $CONTAINER_ID --format='{{.Config.Image}}')

# Start a temporary container from the same image to compare
docker run --rm $IMAGE ls -l /path/to/modified/binary
docker run --rm $IMAGE stat /path/to/modified/binary

# Compare file checksums
RUNNING_CHECKSUM=$(docker exec $CONTAINER_ID sha256sum /path/to/modified/binary | awk '{print $1}')
IMAGE_CHECKSUM=$(docker run --rm $IMAGE sha256sum /path/to/modified/binary | awk '{print $1}')

if [ "$RUNNING_CHECKSUM" != "$IMAGE_CHECKSUM" ]; then
  echo "Binary has been modified at runtime"
fi
```

**Step 3: Check for Authorized Updates**

Verify if the modification was part of an authorized container image update:

```bash
# Check container image history
docker history $IMAGE

# Verify package installation within the container
docker exec $CONTAINER_ID dpkg -V package-name  # Debian/Ubuntu
docker exec $CONTAINER_ID rpm -V package-name   # RHEL/CentOS

# For Kubernetes, check deployment/pod specifications
kubectl describe pod <pod-name>
kubectl get pod <pod-name> -o yaml | grep image:
```
