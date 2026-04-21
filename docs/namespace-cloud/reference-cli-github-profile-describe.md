<!-- Source: https://namespace.so/docs/reference/cli/github-profile-describe -->

# nsc github profile describe

Describe a GitHub runner profile in detail.

`nsc github profile describe` shows detailed information about a specific runner profile, including its full specification, cache volume settings, custom image build status, and network policy configuration.

## Usage

```
nsc github profile describe [flags]
```

### Examples

**Describe a profile:**

```
$ nsc github profile describe --profile_id <profile-id>
```

**Describe a profile as JSON:**

```
$ nsc github profile describe --profile_id <profile-id> -o json
```

## Required Flags

### --profile\_id string

Profile ID to describe.

## Optional Flags

### -o, --output string

Output format. Default: `plain`.

Supported values: `plain`, `json`.

## Related Topics

- [nsc github profile](/docs/reference/cli/github-profile) - Manage GitHub runner profiles
- [nsc github profile list](/docs/reference/cli/github-profile-list) - List all profiles
- [nsc github profile update](/docs/reference/cli/github-profile-update) - Update a profile

Last updated April 14, 2026
