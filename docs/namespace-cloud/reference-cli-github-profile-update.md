<!-- Source: https://namespace.so/docs/reference/cli/github-profile-update -->

# nsc github profile update

Update an existing GitHub runner profile.

`nsc github profile update` modifies an existing runner profile. You can update individual fields like the machine type, OS, or builder mode, or replace the entire spec from a file. The update supports optimistic concurrency control via the `--version` flag to prevent concurrent modifications.

## Usage

```
nsc github profile update [flags]
```

### Examples

**Update the machine type:**

```
$ nsc github profile update \
  --profile_id <profile-id> \
  --machine_type 8x16
```

**Update the OS and add a custom Dockerfile:**

```
$ nsc github profile update \
  --profile_id <profile-id> \
  --os ubuntu-24.04 \
  --dockerfile Dockerfile.runner
```

**Update with optimistic concurrency control:**

```
$ nsc github profile update \
  --profile_id <profile-id> \
  --description "Updated runners" \
  --version 3
```

**Update from a spec file:**

```
$ nsc github profile update \
  --profile_id <profile-id> \
  --spec_file profile.json
```

## Required Flags

### --profile\_id string

Profile ID to update.

## Optional Flags

### --tag string

Stable user-configurable alias for the profile.

### --description string

Human-friendly description of the profile.

### --os string

Operating system label (e.g., `ubuntu-24.10`).

### --machine\_type string

Machine type in the format `CPUxMemoryGB` (e.g., `4x8` for 4 vCPU and 8 GB memory).

### --machine\_arch string

Machine architecture (`amd64` or `arm64`).

### --builder\_mode string

Builder mode controlling how container builds are executed. Default: `USE_REMOTE_BUILDER`.
Alternative options are `USE_LOCAL_CACHE` when a local build cache within the runner should be used or `NO_CACHING` when caching should be disabled.

### --emoji string

Optional emoji to visually identify the profile in the UI.

### --dockerfile string

Path to a Dockerfile for a custom runner image. The Dockerfile is applied as a layer on top of the base image.

### --egress\_policy string

Egress policy for outbound network access. Set to `DOMAIN_ALLOW_LIST` to restrict outbound access to specific domains, or `NONE` to disable filtering.

### --egress\_domain\_allow\_list strings

Comma-separated list of allowed egress domains. Supports wildcards (e.g., `*.example.org`). Only valid with `--egress_policy=DOMAIN_ALLOW_LIST`.

### --spec\_file string

Path to a JSON file containing the full profile spec. When provided, individual flags are ignored.

### --version int

Current version of the profile for optimistic concurrency control. If not provided, it will be fetched from the backend.

### -o, --output string

Output format. Default: `plain`.

Supported values: `plain`, `json`.

## Related Topics

- [nsc github profile](/docs/reference/cli/github-profile) - Manage GitHub runner profiles
- [nsc github profile describe](/docs/reference/cli/github-profile-describe) - Describe a profile
- [nsc github profile delete](/docs/reference/cli/github-profile-delete) - Delete a profile

Last updated April 14, 2026
