# Source: https://docs.jfrog.com/artifactory/docs/distribution-through-cli.md

# Distribution CLI

<br />

This page describes how to use JFrog CLI with JFrog Distribution.

> **Read more about JFrog Distribution** [here](/docs/jfrog-distribution).

***

## Prerequisites

Before using JFrog Distribution commands, ensure:

1. **JFrog CLI is installed**: Run `jf --version` to verify installation
2. **Server is configured**: Run `jf config add` to configure your JFrog Platform, or pass `--url` and authentication flags with each command
3. **Distribution is enabled**: Your JFrog Platform must have Distribution enabled (version 2.0 or higher)
4. **For signing**: GPG key pair must be configured in JFrog Distribution
5. **For distribution**: At least one Edge Node must be configured and connected

### Configuring Your Server

```bash
# Option 1: Configure server interactively (recommended)
jf config add

# Option 2: Configure with environment variables
export JFROG_URL="https://acme.jfrog.io"
export JFROG_ACCESS_TOKEN="your-access-token"

# Option 3: Pass credentials with each command
jf ds rbc --url="https://acme.jfrog.io/distribution" --access-token="token" ...
```

***

## Overview

JFrog CLI provides a convenient interface for working with release bundles in JFrog Distribution. The Distribution commands are available under the `jf ds` namespace.

### Syntax

```
jf ds command-name [global-options] [command-options] [arguments]
```

### Commands Available

| Full Command              | Abbreviation | Description                                |
| ------------------------- | ------------ | ------------------------------------------ |
| release-bundle-create     | rbc          | Create a release bundle                    |
| release-bundle-update     | rbu          | Update an existing unsigned release bundle |
| release-bundle-sign       | rbs          | Sign a release bundle                      |
| release-bundle-distribute | rbd          | Distribute a release bundle to Edge nodes  |
| release-bundle-delete     | rbdel        | Delete a release bundle                    |

***

## Common Options

The following options are available for all distribution commands:

| Option           | Description                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `--server-id`    | \[Optional] Server ID configured using the `jf config` command. If not specified, the default configured server is used. |
| `--url`          | \[Optional] JFrog Distribution URL. Example: `https://acme.jfrog.io/distribution`                                        |
| `--user`         | \[Optional] JFrog username.                                                                                              |
| `--password`     | \[Optional] JFrog password.                                                                                              |
| `--access-token` | \[Optional] JFrog access token.                                                                                          |
| `--insecure-tls` | \[Default: false] Set to true to skip TLS certificates verification.                                                     |

***

## Creating a Release Bundle

Create a new release bundle with artifacts from Artifactory.

### Command

```
jf ds release-bundle-create <bundle-name> <bundle-version> [pattern]
```

Abbreviation: `rbc`

### Arguments

| Argument       | Description                                                                                                                                                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bundle-name    | The name of the release bundle.                                                                                                                                           |
| bundle-version | The release bundle version.                                                                                                                                               |
| pattern        | \[Optional] Specifies the source path in Artifactory in the following format: `<repository-name>/<repository-path>`. You can use wildcards to specify multiple artifacts. |

### Options

| Option                   | Description                                                                                                                                                                                                                                                       |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spec`                 | \[Optional] Path to a File Spec containing the artifacts to include.                                                                                                                                                                                              |
| `--spec-vars`            | \[Optional] List of semicolon-separated variables in the form of `key1=value1;key2=value2` to be replaced in the File Spec. Variables should be used as `${key1}` in the spec.                                                                                    |
| `--target`               | \[Optional] The target path for distributed artifacts on the edge node. If not specified, artifacts will have the same path as on the source Artifactory. Supports placeholders `{1}`, `{2}` which are replaced by tokens enclosed in parenthesis in the pattern. |
| `--target-props`         | \[Optional] List of semicolon-separated properties in the form of `key1=value1;key2=value2` to be added to artifacts after distribution.                                                                                                                          |
| `--dry-run`              | \[Default: false] Set to true to disable communication with JFrog Distribution. Validates the command without executing.                                                                                                                                          |
| `--sign`                 | \[Default: false] If set to true, automatically signs the release bundle version after creation.                                                                                                                                                                  |
| `--passphrase`           | \[Optional] The passphrase for the GPG signing key. Required if `--sign` is used and the key has a passphrase.                                                                                                                                                    |
| `--desc`                 | \[Optional] Description of the release bundle.                                                                                                                                                                                                                    |
| `--release-notes-path`   | \[Optional] Path to a file containing release notes for the release bundle version.                                                                                                                                                                               |
| `--release-notes-syntax` | \[Default: plain\_text] The syntax for the release notes. Can be one of: `markdown`, `asciidoc`, or `plain_text`.                                                                                                                                                 |
| `--exclusions`           | \[Optional] List of semicolon-separated exclusion patterns. Exclusions can include `*` and `?` wildcards.                                                                                                                                                         |
| `--repo`                 | \[Optional] A repository name at source Artifactory to store release bundle artifacts. If not provided, Artifactory will use the default repository.                                                                                                              |
| `--detailed-summary`     | \[Default: false] Set to true to get a command summary with details about the release bundle artifact.                                                                                                                                                            |

### Examples

**Example 1: Create a release bundle with a pattern**

```bash
jf ds rbc myApp 1.0.0 "my-repo/builds/*.zip"
```

**Example 2: Create a release bundle using a File Spec**

```bash
jf ds rbc --spec=/path/to/spec.json myApp 1.0.0
```

**Example 3: Create and automatically sign**

```bash
jf ds rbc --sign --passphrase="my-gpg-passphrase" myApp 1.0.0 "my-repo/releases/*"
```

**Example 4: Dry run to validate without executing**

```bash
jf ds rbc --dry-run myApp 1.0.0 "my-repo/builds/*.zip"
```

***

## Updating a Release Bundle

Update an existing **unsigned** release bundle version by adding or modifying artifacts.

### Command

```
jf ds release-bundle-update <bundle-name> <bundle-version> [pattern]
```

Abbreviation: `rbu`

### Arguments

| Argument       | Description                                                                                                                                                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bundle-name    | The name of the release bundle.                                                                                                                                           |
| bundle-version | The release bundle version to update.                                                                                                                                     |
| pattern        | \[Optional] Specifies the source path in Artifactory in the following format: `<repository-name>/<repository-path>`. You can use wildcards to specify multiple artifacts. |

### Options

Same options as `release-bundle-create` (see above).

> **Note**: You can only update release bundles that have not been signed. Once a release bundle is signed, it becomes immutable.

### Examples

**Example 1: Update with a pattern**

```bash
jf ds rbu myApp 1.0.0 "my-repo/additional-files/*.jar"
```

**Example 2: Update using a File Spec**

```bash
jf ds rbu --spec=/path/to/updated-spec.json myApp 1.0.0
```

***

## Signing a Release Bundle

Sign a release bundle using the GPG key configured in JFrog Distribution. Signing makes the release bundle immutable and ready for distribution.

### Command

```
jf ds release-bundle-sign <bundle-name> <bundle-version>
```

Abbreviation: `rbs`

### Arguments

| Argument       | Description             |
| -------------- | ----------------------- |
| bundle-name    | Release bundle name.    |
| bundle-version | Release bundle version. |

### Options

| Option               | Description                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--passphrase`       | \[Optional] The passphrase for the GPG signing key.                                                                                                  |
| `--repo`             | \[Optional] A repository name at source Artifactory to store release bundle artifacts. If not provided, Artifactory will use the default repository. |
| `--detailed-summary` | \[Default: false] Set to true to get a command summary with details about the release bundle artifact.                                               |

> **Note**: The `--dry-run` flag is not available for the sign command.

### Examples

**Example 1: Sign a release bundle**

```bash
jf ds rbs myApp 1.0.0
```

**Example 2: Sign with a passphrase**

```bash
jf ds rbs --passphrase="<passphrase>" myApp 1.0.0
```

***

## Distributing a Release Bundle

Distribute a signed release bundle to one or more Edge nodes.

### Command

```
jf ds release-bundle-distribute <bundle-name> <bundle-version>
```

Abbreviation: `rbd`

### Arguments

| Argument       | Description             |
| -------------- | ----------------------- |
| bundle-name    | Release bundle name.    |
| bundle-version | Release bundle version. |

### Options

| Option               | Description                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `--dist-rules`       | \[Optional] Path to a JSON file containing distribution rules. Cannot be used with `--site`, `--city`, or `--country-codes`.          |
| `--site`             | \[Optional] Wildcard filter for site name. When not specified, defaults to `*` (all sites).                                           |
| `--city`             | \[Optional] Wildcard filter for site city name. When not specified, defaults to `*` (all cities).                                     |
| `--country-codes`    | \[Optional] Semicolon-separated list of wildcard filters for site country codes. When not specified, defaults to `*` (all countries). |
| `--sync`             | \[Default: false] Set to true to enable synchronous distribution. The command will wait until the distribution process completes.     |
| `--max-wait-minutes` | \[Default: 60] Maximum minutes to wait for synchronous distribution. Only applicable when `--sync` is set to true.                    |
| `--create-repo`      | \[Default: false] Set to true to automatically create the repository on the Edge node if it does not exist.                           |
| `--dry-run`          | \[Default: false] Set to true to disable communication with JFrog Distribution. Validates the command without executing.              |

### Examples

**Example 1: Distribute to all Edge nodes**

```bash
jf ds rbd --site="*" myApp 1.0.0
```

**Example 2: Distribute to specific sites**

```bash
jf ds rbd --site="us-*" --city="New York" myApp 1.0.0
```

**Example 3: Distribute using rules file**

```bash
jf ds rbd --dist-rules=/path/to/rules.json myApp 1.0.0
```

**Example 4: Synchronous distribution with repository creation**

```bash
jf ds rbd --sync --create-repo --site="*" myApp 1.0.0
```

***

## Deleting a Release Bundle

Delete a release bundle from Edge nodes and optionally from JFrog Distribution itself.

### Command

```
jf ds release-bundle-delete <bundle-name> <bundle-version>
```

Abbreviation: `rbdel`

### Arguments

| Argument       | Description             |
| -------------- | ----------------------- |
| bundle-name    | Release bundle name.    |
| bundle-version | Release bundle version. |

### Options

| Option               | Description                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--dist-rules`       | \[Optional] Path to a JSON file containing distribution rules specifying where to delete.                                                            |
| `--site`             | \[Optional] Wildcard filter for site name. When not specified, defaults to `*` (all sites).                                                          |
| `--city`             | \[Optional] Wildcard filter for site city name. When not specified, defaults to `*` (all cities).                                                    |
| `--country-codes`    | \[Optional] Semicolon-separated list of wildcard filters for site country codes. When not specified, defaults to `*` (all countries).                |
| `--delete-from-dist` | \[Default: false] Set to true to also delete the release bundle version from JFrog Distribution itself after deletion is complete on the Edge nodes. |
| `--sync`             | \[Default: false] Set to true to enable synchronous deletion. The command will wait until the deletion process completes.                            |
| `--max-wait-minutes` | \[Default: 60] Maximum minutes to wait for synchronous deletion. Only applicable when `--sync` is set to true.                                       |
| `--quiet`            | \[Default: false, or true if `$CI` environment variable is set] Set to true to skip the delete confirmation message.                                 |
| `--dry-run`          | \[Default: false] Set to true to disable communication with JFrog Distribution. Validates the command without executing.                             |

### Examples

**Example 1: Delete from all Edge nodes**

```bash
jf ds rbdel --site="*" myApp 1.0.0
```

**Example 2: Delete from Edge nodes and Distribution**

```bash
jf ds rbdel --site="*" --delete-from-dist myApp 1.0.0
```

**Example 3: Delete silently (for CI/CD)**

```bash
jf ds rbdel --quiet --sync --site="*" myApp 1.0.0
```

***

## File Spec Schema

File Specs can be used with `release-bundle-create` and `release-bundle-update` commands to define which artifacts to include.

### Using Patterns

```json
{
  "files": [
    {
      "pattern": "my-local-repo/zips/*.zip"
    }
  ]
}
```

### Using AQL Queries

```json
{
  "files": [
    {
      "aql": {
        "items.find": {
          "repo": "my-local-repo",
          "$and": [
            {
              "name": { "$match": "*.jar" }
            },
            {
              "$or": [
                { "path": { "$match": "." } },
                { "path": { "$match": "*" } }
              ]
            }
          ]
        }
      }
    }
  ]
}
```

### Using Path Mapping

Path mapping allows you to change the artifact path in the release bundle:

```json
{
  "files": [
    {
      "pattern": "my-local-repo/(.*)",
      "pathMapping": {
        "input": "my-local-repo/(.*)",
        "output": "new-path/$1"
      }
    }
  ]
}
```

> **More about File Specs**: See the [File Spec documentation](https://jfrog.com/help/r/jfrog-cli/using-file-specs) for complete syntax reference.

***

## Distribution Rules Schema

Distribution rules define which Edge nodes receive the release bundle.

### JSON Structure

```json
{
  "distribution_rules": [
    {
      "site_name": "*",
      "city_name": "*",
      "country_codes": ["*"]
    }
  ]
}
```

### Fields

| Field           | Description                                                    |
| --------------- | -------------------------------------------------------------- |
| `site_name`     | Wildcard pattern for site names. Use `*` for all sites.        |
| `city_name`     | Wildcard pattern for city names. Use `*` for all cities.       |
| `country_codes` | Array of country code patterns. Use `["*"]` for all countries. |

### Example: Multiple Rules

```json
{
  "distribution_rules": [
    {
      "site_name": "us-*",
      "city_name": "*",
      "country_codes": ["US"]
    },
    {
      "site_name": "eu-*",
      "city_name": "*",
      "country_codes": ["DE", "FR", "GB"]
    }
  ]
}
```

***

## Environment Variables

The following environment variables can be used with distribution commands:

| Variable                 | Description                                                            |
| ------------------------ | ---------------------------------------------------------------------- |
| `JFROG_CLI_SERVER_ID`    | Default server ID to use                                               |
| `JFROG_URL`              | JFrog Platform URL                                                     |
| `JFROG_DISTRIBUTION_URL` | JFrog Distribution URL                                                 |
| `JFROG_ACCESS_TOKEN`     | JFrog access token for authentication                                  |
| `JFROG_USER`             | JFrog username                                                         |
| `JFROG_PASSWORD`         | JFrog password                                                         |
| `CI`                     | When set to `true`, enables non-interactive mode (skips confirmations) |

***

## Troubleshooting

### Common Issues

**Error: "no JFrog Distribution URL specified"**

The CLI cannot find a configured server. Solutions:

1. Run `jf config add` to configure your server
2. Pass `--url` with the Distribution URL
3. Set the `JFROG_URL` environment variable

**Error: "release bundle not found"**

* Verify the bundle name and version are correct
* Check if the bundle was created on the expected server

**Error: "signing failed"**

* Verify GPG keys are configured in JFrog Distribution
* Check if the passphrase is correct
* Ensure you have permission to sign release bundles

**Distribution stuck or slow**

* Use `--sync` with `--max-wait-minutes` to control timeout
* Check Edge node connectivity in the JFrog Platform UI
* Verify network connectivity between Distribution and Edge nodes

***

## Best Practices

1. **Version your bundles semantically**: Use semantic versioning (e.g., `1.0.0`, `1.0.1`) for release bundles
2. **Always sign before distributing**: Signed bundles are immutable and provide integrity verification
3. **Use File Specs for complex selections**: File Specs provide more flexibility than command-line patterns
4. **Use `--sync` in CI/CD**: Synchronous mode ensures the pipeline waits for distribution to complete
5. **Set `$CI` in automated environments**: This automatically enables `--quiet` mode

<br />