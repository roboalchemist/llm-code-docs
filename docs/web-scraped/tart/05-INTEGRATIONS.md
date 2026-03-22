# Tart - Integration Guides

Source: https://tart.run/integrations

Integration guides for using Tart with popular CI/CD and VM management tools:

## Cirrus CLI Integration

**Guide:** `docs/integrations/cirrus-cli.md`

Tart itself is only responsible for managing virtual machines, but we've built Tart support into a tool called Cirrus CLI
also developed by Cirrus Labs. [Cirrus CLI](https://github.com/cirruslabs/cirrus-cli) is a command line tool with
one configuration format to execute common CI steps (run a script, cache a folder, etc.) locally or in any CI system.
We built Cirrus CLI to solve "But it works on my machine!" problem.

Here is an example of a `.cirrus.yml` configuration file which will start a Tart VM, will copy over working directory and
will run scripts and [other instructions](https://cirrus-ci.org/guide/writing-tasks/#supported-instructions) inside the virtual machine:

```yaml
task:
  name: hello
  macos_instance:
    # can be a remote or a local virtual machine
    image: ghcr.io/cirruslabs/macos-tahoe-base:latest
  hello_script:
    - echo "Hello from within a Tart VM!"
    - echo "Here is my CPU info:"
    - sysctl -n machdep.cpu.brand_string
    - sleep 15
```

Put the above `.cirrus.yml` file in the root of your repository and run it with the following command:

```bash
brew install cirruslabs/cli/cirrus
cirrus run
```

![](../assets/images/TartCirrusCLI.gif)

[Cirrus CI](https://cirrus-ci.org/) already leverages Tart to power its macOS cloud infrastructure. The `.cirrus.yml`
config from above will just work in Cirrus CI and your tasks will be executed inside Tart VMs in our cloud.

**Note:** Cirrus CI only allows [images managed and regularly updated by us](https://github.com/orgs/cirruslabs/packages?tab=packages&q=macos).

## Retrieving artifacts from within Tart VMs

In many cases there is a need to retrieve particular files or a folder from within a Tart virtual machine.
For example, the below `.cirrus.yml` configuration defines a single task that builds a `tart` binary and
exposes it via [`artifacts` instruction](https://cirrus-ci.org/guide/writing-tasks/#artifacts-instruction):

```yaml
task:
  name: Build
  macos_instance:
    image: ghcr.io/cirruslabs/macos-tahoe-xcode:latest
  build_script: swift build --product tart
  binary_artifacts:
    path: .build/debug/tart
```

Running Cirrus CLI with `--artifacts-dir` will write defined `artifacts` to the provided local directory on the host:

```bash
cirrus run --artifacts-dir artifacts
```

Note that all retrieved artifacts will be prefixed with the associated task name and `artifacts` instruction name.
For the example above, `tart` binary will be saved to `$PWD/artifacts/Build/binary/.build/debug/tart`.

## Packer Integration

**Guide:** `docs/integrations/packer.md`

---
title: Automating VM image building with Packer
description: Use Packer to build custom VM images, configure VMs and work with remote OCI registries.
---

Please refer to [Tart Packer Plugin repository](https://github.com/cirruslabs/packer-plugin-tart) for setup instructions.
Here is an example of a template to build a local image based of a remote image:

```hcl
packer {
  required_plugins {
    tart = {
      version = ">= 0.5.3"
      source  = "github.com/cirruslabs/tart"
    }
  }
}

source "tart-cli" "tart" {
  vm_base_name = "ghcr.io/cirruslabs/macos-tahoe-base:latest"
  vm_name      = "my-custom-tahoe"
  cpu_count    = 4
  memory_gb    = 8
  disk_size_gb = 70
  ssh_password = "admin"
  ssh_timeout  = "120s"
  ssh_username = "admin"
}

build {
  sources = ["source.tart-cli.tart"]

  provisioner "shell" {
    inline = ["echo 'Disabling spotlight indexing...'", "sudo mdutil -a -i off"]
  }

  # more provisioners
}
```

Here is a [repository with Packer templates](https://github.com/cirruslabs/macos-image-templates) used to build [all the images managed by us](https://github.com/orgs/cirruslabs/packages?tab=packages&q=macos).

## GitLab Runner Integration

**Guide:** `docs/integrations/gitlab-runner.md`

It is possible to run GitLab jobs in isolated ephemeral Tart Virtual Machines via [Tart Executor](https://github.com/cirruslabs/gitlab-tart-executor).
Tart Executor utilizes [custom executor](https://docs.gitlab.com/runner/executors/custom.html) feature of GitLab Runner.

# Basic Configuration

Configuring Tart Executor for GitLab Runner is as simple as installing `gitlab-tart-executor` binary from Homebrew:

```bash
brew install cirruslabs/cli/gitlab-tart-executor
```

And updating configuration of your self-hosted GitLab Runner to use `gitlab-tart-executor` binary:

```toml
concurrent = 2

[[runners]]
  # ...
  executor = "custom"
  builds_dir = "/Users/admin/builds" # directory inside the VM
  cache_dir = "/Users/admin/cache"
  [runners.feature_flags]
    FF_RESOLVE_FULL_TLS_CHAIN = false
  [runners.custom]
    prepare_exec = "gitlab-tart-executor"
    prepare_args = ["prepare"]
    run_exec = "gitlab-tart-executor"
    run_args = ["run"]
    cleanup_exec = "gitlab-tart-executor"
    cleanup_args = ["cleanup"]
```

Now you can use Tart Images in your `.gitlab-ci.yml`:

```yaml
# You can use any remote Tart Image.
# Tart Executor will pull it from the registry and use it for creating ephemeral VMs.
image: ghcr.io/cirruslabs/macos-tahoe-base:latest

test:
  tags:
    - tart-installed # in case you tagged runners with Tart Executor installed
  script:
    - uname -a
```

For more advanced configuration please refer to [GitLab Tart Executor repository](https://github.com/cirruslabs/gitlab-tart-executor).

## Buildkite Integration

**Guide:** `docs/integrations/buildkite.md`

It is possible to run [Buildkite](https://buildkite.com/) pipeline steps in isolated ephemeral Tart Virtual Machines with the help of [Tart Buildkite Plugin](https://github.com/cirruslabs/tart-buildkite-plugin):

![](../assets/images/BuildkiteTartPlugin.png)

## Configuration

The most basic configuration looks like this:

```yaml
steps:
- command: uname -a
  plugins:
  - cirruslabs/tart#main:
    image: ghcr.io/cirruslabs/macos-tahoe-base:latest
```

This will run `uname -r` in a macOS Tart VM cloned from `ghcr.io/cirruslabs/macos-tahoe-base:latest`.

See plugin's [Configuration section](https://github.com/cirruslabs/tart-buildkite-plugin#configuration) for the full list of available options.

