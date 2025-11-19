# Source: https://www.daytona.io/docs/en/declarative-builder.md

Daytona's declarative builder provides a powerful, code-first approach to defining dependencies for Sandboxes. Instead of importing images from a container registry, you can programmatically define them using the SDK.

## Overview

The declarative builder system supports two primary workflows:

1. [**Declarative Images**](#declarative-image-building): Build images with varying dependencies _on demand_ when creating Sandboxes
2. [**Pre-built Snapshots**](#creating-pre-built-snapshots): Create and register _ready-to-use_ [Snapshots](https://www.daytona.io/docs/snapshots.md) that can be shared across multiple Sandboxes

### Declarative Image Building

You can create declarative images on-the-fly when creating Sandboxes. This is ideal for iterating quickly without creating separate Snapshots.

Declarative images are cached for 24 hours, and will be automatically reused when running the same script. Thus, subsequent runs on the same Runner will be almost instantaneous.

```python
# Define a simple declarative image with Python packages
declarative_image = (
    Image.debian_slim("3.12")
    .pip_install(["requests", "pytest"])
    .workdir("/home/daytona")
)

# Create a new Sandbox with the declarative image and stream the build logs
sandbox = daytona.create(
    CreateSandboxFromImageParams(image=declarative_image),
    timeout=0,
    on_snapshot_create_logs=print,
)
```
```typescript
// Define a simple declarative image with Python packages
const declarativeImage = Image.debianSlim('3.12')
  .pipInstall(['requests', 'pytest'])
  .workdir('/home/daytona')

// Create a new Sandbox with the declarative image and stream the build logs
const sandbox = await daytona.create(
  {
    image: declarativeImage,
  },
  {
    timeout: 0,
    onSnapshotCreateLogs: console.log,
  }
)
```

See: [CreateSandboxFromImageParams (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/daytona.md#createsandboxfromimageparams), [CreateSandboxFromImageParams (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/daytona.md#createsandboxfromimageparams)

### Creating Pre-built Snapshots

For images that will be reused across multiple Sandboxes, create a pre-built Snapshot. This Snapshot will remain visible in the Daytona dashboard and be permanently cached, ensuring instant availability without rebuilding.

```python
# Create a simple Python data science image
snapshot_name = "data-science-snapshot"

image = (
    Image.debian_slim("3.12")
    .pip_install(["pandas", "numpy"])
    .workdir("/home/daytona")
)

# Create the Snapshot and stream the build logs
daytona.snapshot.create(
    CreateSnapshotParams(
        name=snapshot_name,
        image=image,
    ),
    on_logs=print,
)

# Create a new Sandbox using the pre-built Snapshot
sandbox = daytona.create(
  CreateSandboxFromSnapshotParams(snapshot=snapshot_name)
)
```
```typescript
// Create a simple Python data science image
const snapshotName = 'data-science-snapshot'

const image = Image.debianSlim('3.12')
  .pipInstall(['pandas', 'numpy'])
  .workdir('/home/daytona')

// Create the Snapshot and stream the build logs
await daytona.snapshot.create(
  {
      name: snapshotName,
      image,
  },
  {
      onLogs: console.log,
  }
)

// Create a new Sandbox using the pre-built Snapshot
const sandbox = await daytona.create({
  snapshot: snapshotName,
})
```

See: [CreateSnapshotParams (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/snapshot.md#createsnapshotparams), [CreateSnapshotParams (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/snapshot.md#createsnapshotparams)

## Image Configuration

The Daytona SDK provides methods to define images programmatically using the Daytona SDK. You can specify base images, install packages, add files, set environment variables, and more.

For a complete API reference and method signatures, check the [Python](https://www.daytona.io/docs/python-sdk/common/image.md) and [TypeScript](https://www.daytona.io/docs/typescript-sdk/image.md) SDK references.

### Base Image Selection

These examples demonstrate how to select and configure base images:

```python
# Create an image from a base
image = Image.base("python:3.12-slim-bookworm")

# Use a Debian slim image with Python 3.12
image = Image.debian_slim("3.12")
```
```typescript
// Create an image from a base
const image = Image.base('python:3.12-slim-bookworm')

// Use a Debian slim image with Python 3.12
const image = Image.debianSlim('3.12')
```

See: [base (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagebase), [debian_slim (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagedebian_slim), [base (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#base), [debianSlim (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#debianslim)

### Package Management

Use these methods to install Python packages and dependencies:

```python
# Add pip packages
image = Image.debian_slim("3.12").pip_install("requests", "pandas")

# Install from requirements.txt
image = Image.debian_slim("3.12").pip_install_from_requirements("requirements.txt")

# Install from pyproject.toml (with optional dependencies)
image = Image.debian_slim("3.12").pip_install_from_pyproject("pyproject.toml", optional_dependencies=["dev"])
```
```typescript
// Add pip packages
const image = Image.debianSlim('3.12').pipInstall(['requests', 'pandas'])

// Install from requirements.txt
const image = Image.debianSlim('3.12').pipInstallFromRequirements('requirements.txt')

// Install from pyproject.toml (with optional dependencies)
const image = Image.debianSlim('3.12').pipInstallFromPyproject('pyproject.toml', { 
  optionalDependencies: ['dev'] 
})
```

See: [pip_install (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install), [pip_install_from_requirements (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install_from_requirements), [pip_install_from_pyproject (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install_from_pyproject), [pipInstall (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstall), [pipInstallFromRequirements (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstallfromrequirements), [pipInstallFromPyproject (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstallfrompyproject)

### File System Operations

These examples show how to add files and directories to your image:

```python
# Add a local file
image = Image.debian_slim("3.12").add_local_file("package.json", "/home/daytona/package.json")

# Add a local directory
image = Image.debian_slim("3.12").add_local_dir("src", "/home/daytona/src")
```
```typescript
// Add a local file
const image = Image.debianSlim('3.12').addLocalFile('package.json', '/home/daytona/package.json')

// Add a local directory
const image = Image.debianSlim('3.12').addLocalDir('src', '/home/daytona/src')
```

See: [add_local_file (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageadd_local_file), [add_local_dir (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageadd_local_dir), [addLocalFile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#addlocalfile), [addLocalDir (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#addlocaldir)

### Environment Configuration

Configure environment variables and working directories with these methods:

```python
# Set environment variables
image = Image.debian_slim("3.12").env({"PROJECT_ROOT": "/home/daytona"})

# Set working directory
image = Image.debian_slim("3.12").workdir("/home/daytona")
```
```typescript
// Set environment variables
const image = Image.debianSlim('3.12').env({ PROJECT_ROOT: '/home/daytona' })

// Set working directory
const image = Image.debianSlim('3.12').workdir('/home/daytona')
```

See: [env (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageenv), [workdir (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageworkdir), [env (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#env), [workdir (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#workdir)

### Commands and Entrypoints

Execute commands during build and configure container startup behavior:

```python
# Run shell commands during build
image = Image.debian_slim("3.12").run_commands(
    'apt-get update && apt-get install -y git',
    'groupadd -r daytona && useradd -r -g daytona -m daytona',
    'mkdir -p /home/daytona/workspace'
)

# Set entrypoint
image = Image.debian_slim("3.12").entrypoint(["/bin/bash"])

# Set default command
image = Image.debian_slim("3.12").cmd(["/bin/bash"])
```
```typescript
// Run shell commands during build
const image = Image.debianSlim('3.12').runCommands(
    'apt-get update && apt-get install -y git',
    'groupadd -r daytona && useradd -r -g daytona -m daytona',
    'mkdir -p /home/daytona/workspace'
)

// Set entrypoint
const image = Image.debianSlim('3.12').entrypoint(['/bin/bash'])

// Set default command
const image = Image.debianSlim('3.12').cmd(['/bin/bash'])
```

See: [run_commands (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagerun_commands), [entrypoint (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageentrypoint), [cmd (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagecmd), [runCommands (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#runcommands), [entrypoint (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#entrypoint), [cmd (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#cmd)

### Dockerfile Integration

Integrate existing Dockerfiles or add custom Dockerfile commands:

```python
# Add custom Dockerfile commands
image = Image.debian_slim("3.12").dockerfile_commands(["RUN echo 'Hello, world!'"])

# Use an existing Dockerfile
image = Image.from_dockerfile("Dockerfile")

# Extend an existing Dockerfile
image = Image.from_dockerfile("app/Dockerfile").pip_install(["numpy"])
```
```typescript
// Add custom Dockerfile commands
const image = Image.debianSlim('3.12').dockerfileCommands(['RUN echo "Hello, world!"'])

// Use an existing Dockerfile
const image = Image.fromDockerfile('Dockerfile')

// Extend an existing Dockerfile
const image = Image.fromDockerfile("app/Dockerfile").pipInstall(['numpy'])
```

See: [dockerfile_commands (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagedockerfile_commands), [from_dockerfile (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagefrom_dockerfile), [dockerfileCommands (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#dockerfilecommands), [fromDockerfile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#fromdockerfile)

## Best Practices

Use the following best practices when working with the declarative builder:

1. **Layer Optimization**: Group related operations to minimize Docker layers
2. **Cache Utilization**: Identical build commands and context will be cached and subsequent builds will be almost instant
3. **Security**: Create non-root users for application workloads
4. **Resource Efficiency**: Use slim base images when appropriate
5. **Context Minimization**: Only include necessary files in the build context