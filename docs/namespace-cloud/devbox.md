<!-- Source: https://namespace.so/docs/devbox -->

# High-Performance Developer Environments with Devboxes

Managed developer environments for humans and AI coding agents. Devboxes provide consistent, reproducible workspaces with enterprise-grade performance and intelligent lifecycle management.

## Why Namespace Devboxes?

[High-performance infrastructure running Linux AMD64](/docs/architecture/compute)

[Dockerfile-based base images define your tools with familiar Docker tooling](/docs/devbox/images)

[Automatic lifecycle management starts on-demand, pauses when idle](/docs/devbox/managing)

[Flexible resource allocation from lightweight to resource-intensive workloads](/docs/architecture/compute/machine-shapes)

[Cost-effective scaling pay only for what you use](/docs/workspaces/billing-and-limits)

[Enterprise ready SAML SSO, SCIM, SLAs, and audit logs](/docs/workspaces/access)

## Getting Started

### Enable GitHub integration

Enable the GitHub integration by visiting [Devboxes](https://cloud.namespace.so/workspace/devboxes), clicking **Connect Organization**, and following the instructions.

### Install the Devbox CLI

Install the Devbox CLI to create and manage devboxes:

![macOS icon](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ficons8-apple-logo-30.755b78bd.png&w=48&q=75)macOS![Linux icon](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ficons8-linux-48.39aa9017.png&w=48&q=75)Linux![Windows icon](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ficons8-windows-10-48.90e3d220.png&w=48&q=75)Windows

```
$

```
curl -fsSL get.namespace.so/devbox/install.sh | bash
```
```

### Authenticate with Namespace

Authenticate with Namespace using the Devbox CLI:

```
$

```
devbox login
```
```

This opens your browser to complete authentication. Once logged in, you're ready to create and manage devboxes.

### Create a devbox

Create a devbox with the default base image.

**Via the CLI:**

```
$

```
devbox create [--checkout=github.com/your-org/your-repo]
```
```

If `--checkout` is provided, the repository will be cloned into the devbox.

**Via the Dashboard:**

![Create new Devbox](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdevbox-create.fd5d2ee7.png&w=1920&q=75)

### Connect and develop

Once your devbox is ready, you can connect in multiple ways:

**Via the Dashboard:**

![Devbox dashboard with initialization log](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdevbox-dashboard.ab03376d.png&w=1920&q=75)

The dashboard shows your devbox status, initialization progress, and provides quick access to open the devbox in your preferred IDE.

**Via SSH:**

```
$

```
devbox ssh main
```
```

**Via your IDE:**

Devboxes have built-in support for popular code editors. From the dashboard, click the "Open VSCode" dropdown to open your devbox in VS Code, Cursor, or VS Code on the Web. Or use the CLI:

```
$

```
devbox open-ide main
```
```

See [Remote Development](/docs/devbox/remote-development) for the full list of supported IDEs including JetBrains and Zed.

## Lifecycle

Namespace manages your devbox lifecycle automatically:

- **Start on-demand**: Devboxes start when you connect or trigger them
- **Pause when idle**: After a period of inactivity, devboxes automatically pause to save costs
- **Persistence**: Your code, files, and configuration remain intact across pause/resume cycles
- **Fast resume**: Paused devboxes resume in seconds

## Use Cases

### Shared Environment Definitions

A key advantage of Devboxes is that **developers and AI coding agents share the same environment definition**. This ensures:

- **Consistent behavior**: Code that works in Claude Code will work for developers, and vice versa
- **Reproducible results**: Everyone sees the same build outputs, test results, and runtime behavior
- **Single source of truth**: One Dockerfile defines the environment for your entire team, including AI agents
- **No environment drift**: Eliminate "works on my machine" problems between humans and AI

### Developers

Devboxes provide consistent, high-performance environments for development teams:

- Onboard new team members instantly
- Work in the same environment as Claude Code and other AI agents
- Access powerful compute for resource-intensive workloads
- Switch between projects without managing local dependencies
- Built-in git access for seamless source control operations

### AI Coding Agents & Claude Code Workspaces

Devboxes are optimized for AI-powered development workflows. Claude Code can be enabled directly at instance creation, with the workspace configured automatically:

- **One-click enablement**: Enable Claude Code when you create an instance for automatic workspace configuration
- **Quick workspace creation**: Spin up isolated devboxes for each major change or feature
- **Shared environment definition**: AI agents use the same Dockerfile and tools as your developers
- **Parallel development**: Work on multiple features simultaneously, each in its own devbox
- **Clean slate**: Start fresh for each task without polluting your main environment
- **Isolated, sandboxed environments**: Complete isolation for secure code execution
- **Long-running sessions**: Support persistent state across agent sessions
- **Built-in git access**: Full git access for commits, branches, and pull requests
- **Automatic resource management**: Resources scale based on agent activity

**Security & Isolation:**

Each devbox environment is completely isolated, providing seamless operation while maintaining security through isolation. For added protection, network policies can be applied to limit the workspace's access to external resources.

This approach enables you to maintain multiple parallel workstreams without environment conflicts or setup overhead, with the guarantee that what works for Claude Code will work for your team.

## Builds on Namespace's infrastructure

Devboxes leverage Namespace's infrastructure capabilities out of the box:

- **Geographic optimization**: Automatically created in a location closer to you to minimize latency
- **Cache volumes**: Automatically used for fast incremental building and testing, with sub-second lookups and high IOPS
- **Persistent volumes**: Backed by our high-performance storage for reliable, fast access to your development files
- **High-performance Docker builds**: Pre-configured remote builders for optimal container build performance
- **Remote registry**: Built-in access to [nscr.io](/docs/architecture/storage/container-registry) for fast image pulls and pushes
- **Build tool caching**: Bazel and Turborepo caching pre-configured for maximum build acceleration
- **Network performance**: Optimized networking for fast git operations and package downloads
- **Compute isolation**: Each devbox runs on dedicated resources with guaranteed performance

No additional configuration required.

## Platform Support

Devboxes run **Linux AMD64** on high-performance hardware.

The Devbox CLI and VS Code extension are supported on **macOS**, **Linux**, and **Windows**. You can manage and connect to your devboxes from any of these operating systems.

## Next Steps

**[Managing Devboxes →](/docs/devbox/managing)**
Machine sizes, lifecycle operations, workspace defaults, and monitoring.

**[Remote Development →](/docs/devbox/remote-development)**
Connect to your devbox via SSH, VS Code, Cursor, Zed, or JetBrains.

**[Sessions →](/docs/devbox/sessions)**
Persistent terminal sessions that survive disconnections.

**[Custom Images →](/docs/devbox/images)**
Build custom base images with your tools and runtimes pre-installed.

## Enterprise Support

Need dedicated capacity, custom machine shapes, or specialized support for your development team?
Contact our [support team](mailto:support@namespace.so) for consultation on complex development environment requirements.

Last updated April 1, 2026
