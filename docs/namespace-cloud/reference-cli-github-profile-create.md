<!-- Source: https://namespace.so/docs/reference/cli/github-profile-create -->

# nsc github profile create

Create a new GitHub runner profile.

`nsc github profile create` creates a new runner profile that defines the configuration for ephemeral GitHub Actions runners. A profile specifies the instance shape, operating system, cache volumes, builder mode, and optional custom image or network policy. The profile's tag must be unique within the workspace and is used to reference the profile in GitHub Actions workflow files via `runs-on` labels.

## Usage

```
nsc github profile create [flags]
```

### Examples

**Create a basic profile:**

```
$ nsc github profile create \
  --tag "my-runners" \
  --description "Standard CI runners" \
  --os ubuntu-24.10 \
  --machine_type 4x8
```

**Create a profile with ARM architecture:**

```
$ nsc github profile create \
  --tag "arm-runners" \
  --machine_arch arm64 \
  --machine_type 8x16
```

**Create a profile with egress restrictions:**

```
$ nsc github profile create \
  --tag "secure-runners" \
  --egress_policy DOMAIN_ALLOW_LIST \
  --egress_domain_allow_list "*.github.com,*.npmjs.org"
```

**Create a profile from a spec file:**

```
$ nsc github profile create --spec_file profile.json
```

## Flags

### --tag string

Stable user-configurable alias for the profile (required unless `--spec_file` is used). This is used in GitHub Actions workflow files to target runners (e.g., `runs-on: nscloud-my-runners`). Must be unique within the workspace.

### --description string (optional)

Human-friendly description of the profile.

### --os string (optional)

Operating system label. Determines the base image used for runners. Default: `ubuntu-24.04`.

**Examples:** `ubuntu-24.04`, `ubuntu-22.04`, `ubuntu-20.04`.

### --machine\_type string (optional)

Machine type in the format `CPUxMemoryGB`. Default: `4x8`.

For example, `4x8` means 4 vCPU and 8 GB memory.

### --machine\_arch string (optional)

Machine architecture. Default: `amd64`.

Supported values: `amd64`, `arm64`.

### --builder\_mode string (optional)

Builder mode controlling how container builds are executed. Default: `USE_REMOTE_BUILDER`.
Alternative options are `USE_LOCAL_CACHE` when a local build cache within the runner should be used or `NO_CACHING` when caching should be disabled.

### --emoji string (optional)

Optional emoji to visually identify the profile in the UI.

### --egress\_policy string (optional)

Egress policy for outbound network access. Set to `DOMAIN_ALLOW_LIST` to restrict outbound access to specific domains. Leave empty for no filtering. Only supported on Linux runners.

### --egress\_domain\_allow\_list strings (optional)

Comma-separated list of allowed egress domains. Supports wildcards (e.g., `*.example.org`). Only valid with `--egress_policy=DOMAIN_ALLOW_LIST`. A minimal set of GitHub- and Namespace-owned domains needed to run GitHub jobs is always added automatically.

### --spec\_file string (optional)

Path to a JSON file containing the full profile spec. When provided, individual flags are ignored.

### -o, --output string (optional)

Output format. Default: `plain`.

Supported values: `plain`, `json`.

## Related Topics

- [nsc github profile](/docs/reference/cli/github-profile) - Manage GitHub runner profiles
- [nsc github profile list](/docs/reference/cli/github-profile-list) - List profiles
- [nsc github profile update](/docs/reference/cli/github-profile-update) - Update a profile
- [nsc github profile delete](/docs/reference/cli/github-profile-delete) - Delete a profile

Last updated April 14, 2026
