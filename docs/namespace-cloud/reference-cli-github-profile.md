<!-- Source: https://namespace.so/docs/reference/cli/github-profile -->

# nsc github profile

Manage GitHub runner profiles.

`nsc github profile` provides commands to manage GitHub Actions runner profiles. Runner profiles define the configuration for ephemeral runners that execute GitHub Actions workflows, including instance shape, operating system, cache settings, custom images, and network policies.

## Usage

```
nsc github profile [command]
```

## Available Commands

- **[create](/docs/reference/cli/github-profile-create)** - Create a new GitHub runner profile
- **[delete](/docs/reference/cli/github-profile-delete)** - Delete a GitHub runner profile
- **[describe](/docs/reference/cli/github-profile-describe)** - Describe a GitHub runner profile in detail
- **[list](/docs/reference/cli/github-profile-list)** - List all GitHub runner profiles
- **[test-build-base-image](/docs/reference/cli/github-profile-test-build-base-image)** - Build the base image from a profile's Dockerfile
- **[update](/docs/reference/cli/github-profile-update)** - Update an existing GitHub runner profile

## Related Topics

- [GitHub Actions Runners](/docs/actions/runners) - Overview of Namespace runners for GitHub Actions

Last updated April 14, 2026
