<!-- Source: https://namespace.so/docs/reference/cli/github-profile-delete -->

# nsc github profile delete

Delete a GitHub runner profile.

`nsc github profile delete` removes a runner profile from the workspace. Active runners using this profile will continue to run until completion, but no new runners will be created with it.

## Usage

```
nsc github profile delete [flags]
```

### Examples

**Delete a profile:**

```
$ nsc github profile delete --profile_id <profile-id>
```

## Required Flags

### --profile\_id string

Profile ID to delete.

## Related Topics

- [nsc github profile](/docs/reference/cli/github-profile) - Manage GitHub runner profiles
- [nsc github profile list](/docs/reference/cli/github-profile-list) - List profiles
- [nsc github profile create](/docs/reference/cli/github-profile-create) - Create a new profile

Last updated April 14, 2026
