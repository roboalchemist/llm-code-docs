# Source: https://www.daytona.io/docs/en/declarative-builder.md

Declarative Builder provides a powerful, code-first approach to defining dependencies for Daytona Sandboxes. Instead of importing images from a container registry, you can programmatically define them using the Daytona SDK.

The declarative builder system supports two primary workflows:

1. [**Declarative images**](#declarative-image-building): build images with varying dependencies _on demand_ when creating sandboxes
2. [**Pre-built Snapshots**](#creating-pre-built-snapshots): create and register _ready-to-use_ [Snapshots](https://www.daytona.io/docs/snapshots.md) that can be shared across multiple sandboxes

## Build declarative images

Daytona provides an option to create declarative images on-the-fly when creating sandboxes. This is ideal for iterating quickly without creating separate snapshots.

Declarative images are cached for 24 hours, and are automatically reused when running the same script. Thus, subsequent runs on the same runner will be almost instantaneous.


```python
# Define a declarative image with python packages
declarative_image = (
  Image.debian_slim("3.12")
  .pip_install(["requests", "pytest"])
  .workdir("/home/daytona")
)

# Create a new sandbox with the declarative image and stream the build logs
sandbox = daytona.create(
  CreateSandboxFromImageParams(image=declarative_image),
  timeout=0,
  on_snapshot_create_logs=print,
)
```


```typescript
// Define a declarative image with python packages
const declarativeImage = Image.debianSlim('3.12')
  .pipInstall(['requests', 'pytest'])
  .workdir('/home/daytona')

// Create a new sandbox with the declarative image and stream the build logs
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


```ruby
# Define a simple declarative image with Python packages
declarative_image = Daytona::Image
  .debian_slim('3.12')
  .pip_install(['requests', 'pytest'])
  .workdir('/home/daytona')

# Create a new Sandbox with the declarative image and stream the build logs
sandbox = daytona.create(
  Daytona::CreateSandboxFromImageParams.new(image: declarative_image),
  timeout: 0,
  on_snapshot_create_logs: proc { |chunk| puts chunk }
)
```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md), [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md), and [Ruby SDK](https://www.daytona.io/docs/en/ruby-sdk.md) references:

> [**CreateSandboxFromImageParams (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/daytona.md#createsandboxfromimageparams)
>
> [**CreateSandboxFromImageParams (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/daytona.md#createsandboxfromimageparams)
>
> [**CreateSandboxFromImageParams (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/daytona.md#createsandboxfromimageparams)

:::note
Use the following best practices when working with the declarative builder:

- **Layer Optimization**: Group related operations to minimize Docker layers

- **Cache Utilization**: Identical build commands and context will be cached and subsequent builds will be almost instant

- **Security**: Create non-root users for application workloads

- **Resource Efficiency**: Use slim base images when appropriate

- **Context Minimization**: Only include necessary files in the build context
  :::

## Create pre-built Snapshots

Daytona provides an option to [create pre-built snapshots](https://www.daytona.io/docs/snapshots.md#create-snapshots) that can be reused across multiple sandboxes.

The snapshot remains visible in the [Daytona Dashboard ↗](https://app.daytona.io/dashboard/snapshots) and is permanently cached, ensuring instant availability without rebuilding.


```python
# Create a python data science image
snapshot_name = "data-science-snapshot"

image = (
  Image.debian_slim("3.12")
  .pip_install(["pandas", "numpy"])
  .workdir("/home/daytona")
)

# Create the snapshot and stream the build logs
daytona.snapshot.create(
  CreateSnapshotParams(
    name=snapshot_name,
    image=image,
  ),
on_logs=print,
)

# Create a new sandbox using the pre-built snapshot
sandbox = daytona.create(
CreateSandboxFromSnapshotParams(snapshot=snapshot_name)
)

```


```typescript
// Create a python data science image
const snapshotName = 'data-science-snapshot'

const image = Image.debianSlim('3.12')
  .pipInstall(['pandas', 'numpy'])
  .workdir('/home/daytona')

// Create the snapshot and stream the build logs
await daytona.snapshot.create(
  {
    name: snapshotName,
    image,
  },
  {
    onLogs: console.log,
  }
)

// Create a new sandbox using the pre-built snapshot
const sandbox = await daytona.create({
  snapshot: snapshotName,
})
```


```ruby
# Create a simple Python data science image
snapshot_name = 'data-science-snapshot'

image = Daytona::Image
  .debian_slim('3.12')
  .pip_install(['pandas', 'numpy'])
  .workdir('/home/daytona')

# Create the Snapshot and stream the build logs
daytona.snapshot.create(
  Daytona::CreateSnapshotParams.new(
    name: snapshot_name,
    image: image
  ),
  on_logs: proc { |chunk| puts chunk }
)

# Create a new Sandbox using the pre-built Snapshot
sandbox = daytona.create(
  Daytona::CreateSandboxFromSnapshotParams.new(snapshot: snapshot_name)
)
```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md), [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md), and [Ruby SDK](https://www.daytona.io/docs/en/ruby-sdk.md) references:

> [**CreateSnapshotParams (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/snapshot.md#createsnapshotparams)
>
> [**CreateSnapshotParams (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/snapshot.md#createsnapshotparams)
>
> [**CreateSnapshotParams (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/snapshot.md#createsnapshotparams)

## Image configuration

Daytona provides an option to define images programmatically using the Daytona SDK. You can specify base images, install packages, add files, set environment variables, and more.

For a complete API reference and method signatures, see the [Python](https://www.daytona.io/docs/python-sdk/common/image.md) and [TypeScript](https://www.daytona.io/docs/typescript-sdk/image.md) SDK references.

### Base image selection

Daytona provides an option to select base images. The following snippets demonstrate how to select and configure base images:


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


```ruby
# Create an image from a base
image = Daytona::Image.base('python:3.12-slim-bookworm')

# Use a Debian slim image with Python 3.12
image = Daytona::Image.debian_slim('3.12')
```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md) and [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md) references:

> [**base (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagebase)
>
> [**base (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#base)
>
> [**debian_slim (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagedebian_slim)
>
> [**debianSlim (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#debianslim)

### Package management

Daytona provides an option to install packages and dependencies to your image.
The following snippets demonstrate how to install packages and dependencies to your image:


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


```ruby
# Add pip packages
image = Daytona::Image.debian_slim('3.12').pip_install(['requests', 'pandas'])

# Install from requirements.txt
image = Daytona::Image.debian_slim('3.12').pip_install_from_requirements('requirements.txt')

# Install from pyproject.toml (with optional dependencies)
image = Daytona::Image.debian_slim('3.12').pip_install_from_pyproject('pyproject.toml', 
  optional_dependencies: ['dev']
)
```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md) and [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md) references:

> [**pip_install (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install)
>
> [**pipInstall (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstall)
>
> [**pip_install_from_requirements (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install_from_requirements)
>
> [**pipInstallFromRequirements (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstallfromrequirements)
>
> [**pip_install_from_pyproject (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install_from_pyproject)
>
> [**pipInstallFromPyproject (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstallfrompyproject)

### File system operations

Daytona provides an option to add files and directories to your image.
The following snippets demonstrate how to add files and directories to your image:


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


```ruby
# Add a local file
image = Daytona::Image.debian_slim('3.12').add_local_file('package.json', '/home/daytona/package.json')

# Add a local directory
image = Daytona::Image.debian_slim('3.12').add_local_dir('src', '/home/daytona/src')
```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md) and [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md) references:

> [**add_local_file (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imageadd_local_file)
>
> [**add_local_dir (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imageadd_local_dir)
>
> [**addLocalFile (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#addlocalfile)
>
> [**addLocalDir (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#addlocaldir)

### Environment configuration

Daytona provides an option to configure environment variables and working directories.
The following snippets demonstrate how to configure environment variables and working directories:


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


```ruby
# Set environment variables
image = Daytona::Image.debian_slim('3.12').env('PROJECT_ROOT': '/home/daytona')

# Set working directory
image = Daytona::Image.debian_slim('3.12').workdir('/home/daytona')
```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md) and [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md) references:

> [**env (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imageenv)
>
> [**workdir (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imageworkdir)
>
> [**env (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#env)
>
> [**workdir (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#workdir)

### Commands and entrypoints

Daytona provides an option to execute commands during build and configure container startup behavior.
The following snippets demonstrate how to execute commands during build and configure container startup behavior:


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


```ruby
# Run shell commands during build
image = Daytona::Image.debian_slim('3.12').run_commands(
  'apt-get update && apt-get install -y git',
  'groupadd -r daytona && useradd -r -g daytona -m daytona',
  'mkdir -p /home/daytona/workspace'
)

# Set entrypoint
image = Daytona::Image.debian_slim('3.12').entrypoint(['/bin/bash'])

# Set default command
image = Daytona::Image.debian_slim('3.12').cmd(['/bin/bash'])
```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md) and [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md) references:

> [**run_commands (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagerun_commands)
>
> [**entrypoint (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imageentrypoint)
>
> [**cmd (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagecmd)
>
> [**runCommands (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#runcommands)
>
> [**entrypoint (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#entrypoint)
>
> [**cmd (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#cmd)

### Dockerfile integration

Daytona provides an option to integrate existing Dockerfiles or add custom Dockerfile commands.
The following snippets demonstrate how to integrate existing Dockerfiles or add custom Dockerfile commands:


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


For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md) and [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md) references:

> [**dockerfile_commands (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagedockerfile_commands)
>
> [**from_dockerfile (Python SDK)**](https://www.daytona.io/docs/python-sdk/common/image.md#imagefrom_dockerfile)
>
> [**dockerfileCommands (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#dockerfilecommands)
>
> [**fromDockerfile (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/image.md#fromdockerfile)