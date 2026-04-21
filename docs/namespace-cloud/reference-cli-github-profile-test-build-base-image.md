<!-- Source: https://namespace.so/docs/reference/cli/github-profile-test-build-base-image -->

# nsc github profile test-build-base-image

Build the base image from a GitHub runner profile's Dockerfile.

`nsc github profile test-build-base-image` performs a test build of the custom runner image defined by a profile's Dockerfile. This is useful for validating that a custom image configuration builds successfully before it is used by runners.

## Usage

```
nsc github profile test-build-base-image [flags]
```

### Examples

**Test build for a profile:**

```
$ nsc github profile test-build-base-image --profile_id <profile-id>
```

**Test build for a specific OS and platform:**

```
$ nsc github profile test-build-base-image \
  --profile_id <profile-id> \
  --os-label ubuntu-24.04 \
  --platform linux/arm64
```

## Required Flags

### --profile\_id string

Profile ID to build from.

## Optional Flags

### -l, --os-label string

Specifies the OS version of the base image. Default: `ubuntu-22.04`.

### -p, --platform strings

Which platforms to build for. Default: `linux/amd64,linux/arm64`.

Supported values: `linux/amd64`, `linux/arm64`.

## Related Topics

- [nsc github profile](/docs/reference/cli/github-profile) - Manage GitHub runner profiles
- [nsc github profile update](/docs/reference/cli/github-profile-update) - Update a profile's Dockerfile
- [nsc github profile describe](/docs/reference/cli/github-profile-describe) - Describe a profile

Last updated April 14, 2026
