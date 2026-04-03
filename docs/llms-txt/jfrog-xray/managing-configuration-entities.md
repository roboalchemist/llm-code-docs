# Source: https://docs.jfrog.com/artifactory/docs/managing-configuration-entities.md

# Manage configuration entities

JFrog CLI offers a set of commands for managing Artifactory repositories. You can create, update and delete repositories. To make it easier to manage repositories, the commands which create and update the repositories accept a pre-defined configuration template file. This template file can also include variables, which can be later replaced with values, when creating or updating the repositories. The configuration template file is created using the `jf rt repo-template` command.

### Create a repository configuration template

The `jf rt repo-template` (or `jf rt rpt`) command provides interactive prompts for building a JSON configuration template.

**To create a repository configuration template interactively:**

1. Run `jf rt repo-template <filename>.json` (or `jf rt rpt <filename>.json`).
2. Respond to each CLI prompt (template type, repository key, class, package type, and optional settings) as described below.
3. When you are done configuring optional settings, enter `:x` to save the JSON template and exit.

On running `jf rt repo-template <filename>.json`, the CLI prompts as follows:

**Template Type**

Select the template type. Following are the possible options:

* **create:** Template for creating a new repository
* **update:** Template for updating an existing repository

```
Select the template type (press Tab for options):
```

For example:

```
Select the template type (press Tab for options): create
```

**Repository Key**

Enter a unique identifier for the repository key. This is the key field in the final JSON.

```
Insert the repository key >
```

For example:

```
Insert the repository key > npm-local
```

<Callout icon="📘" theme="info">
  Note

  If you want to reuse the template for creating multiple repositories, use a variable as follows:

  ```
  Insert the repository key > ${repo-key-var}
  ```
</Callout>

**Repository Class**

Select the repository class. Following are the possible options:

* **local:** A physical, locally-managed repository into which you can deploy artifacts.
* **remote:** A caching proxy for a repository managed at a remote URL. For remote repositories you need to enter a remote repository URL.
* **virtual:** An aggregation of several repositories with the same package type under a common URL.
* **federated:** A Federation is a collection of Federated repositories in different JPDs that are automatically configured for full bi-directional mirroring.

```
Select the repository class (press Tab for options):
```

For example:

```
Select the repository class (press Tab for options): local
```

**Repository Package Type**

Select the repository package type. Following are the possible options:

* alpine
* bower
* cargo
* chef
* cocoapods
* composer
* conan
* cran
* debian
* docker
* gems
* generic
* gitlfs
* go
* gradle
* helm
* ivy
* maven
* npm
* nuget
* opkg
* pypi
* puppet
* rpm
* sbt
* swift
* terraform
* vagrant
* yum

<Callout icon="📘" theme="info">
  Note

  After selecting the repository package type, you can exit by entering `:x` or proceed to make advanced configurations.
</Callout>

**Optional Repository Configurations**

This table explains the optional keys available for configuring your desired repository in JFrog Artifactory.

| Configuration Key                               | Description                                                                                        | Local | Remote | Virtual | Federated |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------- | :---- | :----- | :------ | :-------- |
| `allowAnyHostAuth`                              | Allows sending credentials to any host upon redirection.                                           |       | ✔️     |         |           |
| `archiveBrowseEnabled`                          | Enables viewing archive contents (for example, ZIPs) in the UI.                                    | ✔️    |        |         | ✔️        |
| `artifactoryRequestsCanRetrieveRemoteArtifacts` | Allows the virtual repository to resolve artifacts from its remote members.                        |       |        | ✔️      |           |
| `assumedOfflinePeriodSecs`                      | Sets the time (in seconds) to consider a remote repository offline after a connection failure.     |       | ✔️     |         |           |
| `blackedOut`                                    | Temporarily disables the repository, blocking all traffic.                                         | ✔️    | ✔️     |         | ✔️        |
| `blockMismatchingMimeTypes`                     | Blocks caching of remote files if their MIME type is incorrect.                                    |       | ✔️     |         |           |
| `blockPushingSchema1`                           | Blocks pushes from older Docker v1 clients, enforcing the v2 schema.                               | ✔️    | ✔️     |         | ✔️        |
| `bypassHeadRequests`                            | Skips initial HEAD requests and sends GET requests directly to the remote repository.              |       | ✔️     |         |           |
| `cdnRedirect`                                   | Redirects client download requests to a configured Content Delivery Network (CDN).                 | ✔️    | ✔️     |         | ✔️        |
| `checksumPolicyType`                            | Defines how the server handles artifact checksums during deployment.                               | ✔️    |        |         | ✔️        |
| `clientTlsCertificate`                          | Specifies a client-side TLS certificate to use for authenticating to the remote repository.        |       | ✔️     |         |           |
| `contentSynchronisation`                        | Configures properties for synchronizing content from a remote Artifactory instance.                |       | ✔️     |         |           |
| `defaultDeploymentRepo`                         | Sets the default local repository for artifacts deployed to this virtual repository.               |       |        | ✔️      |           |
| `description`                                   | Provides a short, human-readable summary of the repository's purpose.                              | ✔️    | ✔️     | ✔️      | ✔️        |
| `downloadRedirect`                              | Redirects client downloads directly to the source URL instead of proxying through Artifactory.     | ✔️    | ✔️     |         | ✔️        |
| `enableCookieManagement`                        | Enables stateful cookie handling for requests to the remote repository.                            |       | ✔️     |         |           |
| `environment`                                   | Adds a tag to classify the repository for a specific lifecycle stage (for example, dev, qa, prod). | ✔️    | ✔️     | ✔️      | ✔️        |
| `excludesPattern`                               | Defines a list of file path patterns to block from deployment.                                     | ✔️    | ✔️     | ✔️      | ✔️        |
| `failedRetrievalCachePeriodSecs`                | Sets the time (in seconds) to cache a "not found" response for a failed artifact download.         |       | ✔️     |         |           |
| `fetchJarsEagerly`                              | For remote Maven repositories, proactively fetches JAR files when the index is updated.            |       | ✔️     |         |           |
| `fetchSourcesEagerly`                           | For remote Maven repositories, proactively fetches source JARs when the index is updated.          |       | ✔️     |         |           |
| `forceMavenAuthentication`                      | For virtual Maven repositories, requires authentication for all requests.                          |       |        | ✔️      |           |
| `handleReleases`                                | Determines if the repository can host stable, final release versions of packages.                  | ✔️    | ✔️     |         | ✔️        |
| `handleSnapshots`                               | Determines if the repository can host development or pre-release versions of packages.             | ✔️    | ✔️     |         | ✔️        |
| `hardFail`                                      | Causes requests to fail immediately upon any network error with the remote repository.             |       | ✔️     |         |           |
| `includesPattern`                               | Defines a list of file path patterns that are allowed for deployment.                              | ✔️    | ✔️     | ✔️      | ✔️        |
| `keyPair`                                       | Assigns a GPG key pair to the virtual repository for signing metadata files.                       |       |        | ✔️      |           |
| `localAddress`                                  | Binds outgoing connections to the remote repository to a specific local IP address.                |       | ✔️     |         |           |
| `maxUniqueSnapshots`                            | Limits the number of unique snapshot or pre-release versions stored for an artifact.               | ✔️    |        |         | ✔️        |
| `missedRetrievalCachePeriodSecs`                | Sets the time (in seconds) to cache a "not found" response for remote repository metadata.         |       | ✔️     |         |           |
| `notes`                                         | Offers a space for longer, more detailed information about the repository.                         | ✔️    | ✔️     | ✔️      | ✔️        |
| `offline`                                       | Prevents Artifactory from making any network connections to the remote repository.                 |       | ✔️     |         |           |
| `optionalIndexCompressionFormats`               | Defines additional compression formats for repository index files to support various clients.      | ✔️    |        | ✔️      | ✔️        |
| `password`                                      | Sets the password for authenticating to the remote repository.                                     |       | ✔️     |         |           |
| `pomRepositoryReferencesCleanupPolicy`          | For virtual Maven repositories, controls how to handle repository references in POM files.         |       |        | ✔️      |           |
| `primaryKeyPairRef`                             | Specifies the primary GPG key pair to use for signing metadata.                                    |       |        | ✔️      |           |
| `priorityResolution`                            | Gives a repository priority during package resolution within a virtual repository.                 | ✔️    | ✔️     |         | ✔️        |
| `projectKey`                                    | Links the repository to a specific Project for organization and permission management.             | ✔️    | ✔️     | ✔️      | ✔️        |
| `propertySets`                                  | Associates required metadata fields (properties) with the repository to enforce governance.        | ✔️    | ✔️     |         | ✔️        |
| `proxy`                                         | Specifies a pre-configured network proxy to use for requests to the remote repository.             |       | ✔️     |         |           |
| `rejectInvalidJars`                             | For remote Java-based repositories, rejects and does not cache invalid or corrupt JAR files.       |       | ✔️     |         |           |
| `remoteRepoChecksumPolicyType`                  | Defines how to handle checksums for artifacts downloaded from the remote repository.               |       | ✔️     |         |           |
| `repoLayoutRef`                                 | Assigns a folder structure layout to the repository, enabling metadata parsing.                    | ✔️    | ✔️     | ✔️      | ✔️        |
| `repositories`                                  | Defines the list of underlying repositories aggregated by the virtual repository.                  |       |        | ✔️      |           |
| `retrievalCachePeriodSecs`                      | Sets the time (in seconds) to cache metadata for successfully downloaded remote artifacts.         |       | ✔️     |         |           |
| `shareConfiguration`                            | Shares the remote repository's configuration with other federated Artifactory instances.           |       | ✔️     |         |           |
| `snapshotVersionBehavior`                       | Defines how the server stores and manages snapshot versions.                                       | ✔️    |        |         | ✔️        |
| `socketTimeoutMillis`                           | Sets the timeout (in milliseconds) for network connections to the remote repository.               |       | ✔️     |         |           |
| `storeArtifactsLocally`                         | Controls whether artifacts downloaded from the remote repository are cached locally.               |       | ✔️     |         |           |
| `suppressPomConsistencyChecks`                  | For Maven repositories, disables validation checks on deployed POM files.                          | ✔️    | ✔️     |         | ✔️        |
| `synchronizeProperties`                         | Synchronizes artifact properties from a remote Artifactory instance.                               |       | ✔️     |         |           |
| `unusedArtifactsCleanupEnabled`                 | Enables the automatic cleanup of unused cached artifacts from the remote repository.               |       | ✔️     |         |           |
| `unusedArtifactsCleanupPeriodHours`             | Sets the time (in hours) an unused cached artifact must wait before cleanup.                       |       | ✔️     |         |           |

After adding your desired configurations, enter `:x` to save the template file. Creates and saves a json template and exits the interactive terminal.

The sample json template is as follows:

```json
{
  "description": "my npm local repository",
  "key": "my-npm-local",
  "packageType": "npm",
  "rclass": "local"
}
```

**Reuse Template with Variables**

Reuse the template by adding variables to the keys and provide value explicitly while executing the `jf rt repo-create` command.

For example:

```bash
jf rt repo-create repotemplate.json --vars "repo-name=my-npm-local"
```

If you want to pass multiple vars, enter the list of semicolon-separated(;) variables in the form of "key1=value1;key2=value2;..." (wrapped by quotes) to be replaced in the template. In the template, the variables should be used as follows: `${key1}`.

```bash
jf rt repo-create repotemplate.json --vars "repo-name=my-npm-local;package-type=npm;repo-type=local"
```

***

## Create / Update Repositories

These two commands create a new repository and updates an existing a repository. Both commands accept as an argument a configuration template, which can be created by the **jf rt repo-template** command. The template also supports variables, which can be replaced with values, provided when it is used.

**To create or update a repository from a template:**

1. Create or obtain a template JSON file (for example with `jf rt repo-template`).
2. Run `jf rt repo-create <template-path>` to create a new repository, or `jf rt repo-update <template-path>` to update an existing one.
3. Optionally pass `--vars "key1=value1;key2=value2"` to substitute `${key1}`-style placeholders in the template.

### Commands Params

| Command                | Parameter / Description                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Command-name           | `rt repo-create` / `rt repo-update`                                                                                                                                                                    |
| Abbreviation           | `rt rc` / `rt ru`                                                                                                                                                                                      |
| **Command options:**   |                                                                                                                                                                                                        |
| `--server-id`          | \[Optional] Artifactory Server ID configured using the 'jf config' command.                                                                                                                            |
| `--vars`               | \[Optional] List of semicolon-separated(;) variables in the form of "key1=value1;key2=value2;..." to be replaced in the template. In the template, the variables should be used as follows: `${key1}`. |
| **Command arguments:** |                                                                                                                                                                                                        |
| template path          | Specifies the local file system path for the template file to be used for the repository creation. The template can be created using the `jf rt rpt` command.                                          |

### Create / Update Repositories Examples

**Create a Repository Example**

Create a repository, using the **template.json** file previously generated by the **repo-template** command.

```bash
jf rt repo-create template.json
```

**Update a Repository Example 1**

Update a repository, using the **template.json** file previously generated by the **repo-template** command.

```bash
jf rt repo-update template.json
```

**Update a Repository Example 2**

Update a repository, using the **template.json** file previously generated by the **repo-template** command. Replace the repo-name variable inside the template with a name for the updated repository.

```bash
jf rt repo-update template.json --vars "repo-name=my-repo"
```

***

## Delete Repositories

This command permanently deletes a repository, including all of its content.

**To delete a repository:**

1. Run `jf rt repo-delete <repository-key>`. You can use wildcards in `<repository-key>` to match multiple repositories.
2. Confirm the prompt when running interactively, or set `--quiet=true` in automation (for example when `CI` is set).

### Commands Params

| Parameter              | Command / Description                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| Command name           | `rt repo-delete`                                                                                           |
| Abbreviation           | `rt rdel`                                                                                                  |
| **Command options:**   |                                                                                                            |
| `--server-id`          | \[Optional] Artifactory Server ID configured using the `jf config` command.                                |
| `--quiet`              | \[Default: `$CI`] Set to `true` to skip the delete confirmation message.                                   |
| **Command arguments:** |                                                                                                            |
| repository key         | Specifies the repositories that should be removed. You can use wildcards to specify multiple repositories. |

### Delete Repositories Example

Delete a repository from Artifactory.

```bash
jf rt repo-delete generic-local
```

***

## Manage Replications

JFrog CLI offers commands creating and deleting replication jobs in Artifactory. To make it easier to create replication jobs, the commands which creates the replication job accepts a pre-defined configuration template file. This template file can also include variables, which can be later replaced with values, when creating the replication job. The configuration template file is created using the `jf rt replication-template` command.

### Create a Configuration Template

This command creates a configuration template file, which will be used as an argument for the `jf rt replication-create` command.

When using this command to create the template, you can also provide replaceable variable, instead of fixes values. Then, when the template is used to create replication jobs, values can be provided to replace the variables in the template.

**To create a replication configuration template:**

1. Run `jf rt replication-template <template-path>` (or `jf rt rplt <template-path>`), where `<template-path>` is the path for the new template file.
2. Follow the interactive prompts (job type, source and target repo keys, target server ID, cron expression, and properties), entering `:x` when finished to save.

### Commands Params

| Parameter              | Command / Description                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- |
| Command-name           | `rt replication-template`                                                                                     |
| Abbreviation           | `rt rplt`                                                                                                     |
| **Command options:**   | The command has no options.                                                                                   |
| **Command arguments:** |                                                                                                               |
| template path          | Specifies the local file system path for the template file created by the command. The file should not exist. |

### Manage Replications Example

Create a configuration template, with two variables for the source and target repositories. Then, create a replication job using this template, and provide source and target repository names to replace the variables.

```bash
$ jf rt rplt template.json
Select replication job type (press Tab for options): push
Enter source repo key > ${source}
Enter target repo key > ${target}
Enter target server id (press Tab for options): my-server-id
Enter cron expression for frequency (for example: 0 0 12 * * ? will replicate daily) > 0 0 12 * * ?
You can type ":x" at any time to save and exit.
Select the next property > :x
[Info] Replication creation config template successfully created at template.json.
$
$ jf rt rplc template.json --vars "source=generic-local;target=generic-local"
[Info] Done creating replication job.
```

***

## Create Replication Jobs

This command creates a new replication job for a repository. The command accepts as an argument a configuration template, which can be created by the `jf rt replication-template` command. The template also supports variables, which can be replaced with values, provided when it is used.

**To create or update a replication job from a template:**

1. Ensure you have a template file from `jf rt replication-template` (or `jf rt rplt`).
2. Run `jf rt replication-create <template-path>` (or `jf rt rplc <template-path>`).
3. Optionally pass `--vars "key1=value1;key2=value2"` to substitute variables in the template.

### Commands Params

| Parameter              | Command / Description                                                                                                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Command-name           | `replication-create`                                                                                                                                                                                   |
| Abbreviation           | `rt rplc`                                                                                                                                                                                              |
| **Command options:**   |                                                                                                                                                                                                        |
| `--server-id`          | \[Optional] Artifactory Server ID configured using the 'jf config' command.                                                                                                                            |
| `--vars`               | \[Optional] List of semicolon-separated(;) variables in the form of "key1=value1;key2=value2;..." to be replaced in the template. In the template, the variables should be used as follows: `${key1}`. |
| **Command arguments:** |                                                                                                                                                                                                        |
| template path          | Specifies the local file system path for the template file to be used for the replication job creation. The template can be created using the `jf rt rplt` command.                                    |

### Create Replication Jobs Examples

**Create a Replication Job Example 1**

Create a replication job, using the **template.json** file previously generated by the `replication-template` command.

```bash
jf rt rplc template.json
```

**Update a Replication Job Example**

Update a replication job, using the **template.json** file previously generated by the `replication-template` command. Replace the source and target variables inside the template with the names of the replication source and target repositories.

```bash
jf rt rplc template.json --vars "source=my-source-repo;target=my-target-repo"
```

***

## Delete Replication Jobs

This command permanently deletes a replication jobs from a repository.

**To delete replication jobs for a repository:**

1. Run `jf rt replication-delete <repository-key>` (or `jf rt rpldel <repository-key>`).
2. Confirm the prompt when running interactively, or use `--quiet` where appropriate.

### Commands Params

| Parameter              | Command / Description                                                       |
| ---------------------- | --------------------------------------------------------------------------- |
| Command name           | `rt replication-delete`                                                     |
| Abbreviation           | `rt rpldel`                                                                 |
| **Command options:**   |                                                                             |
| `--server-id`          | \[Optional] Artifactory Server ID configured using the `jf config` command. |
| `--quiet`              | \[Default: `$CI`] Set to `true` to skip the delete confirmation message.    |
| **Command arguments:** |                                                                             |
| repository key         | The repository from which the replications will be deleted.                 |

### Delete Replication Jobs Example

Delete a replication job from a repository.

```bash
jf rt rpldel my-repo-name
```

***

<br />

JFrog CLI offers a set of commands for managing Artifactory configuration entities.

Use these pages when you need to change identity or access configuration from the CLI:

* [Create users in bulk](/artifactory/docs/jf-rt-users-create) — `jf rt users-create`
* [Delete users](/artifactory/docs/jf-rt-users-delete) — `jf rt users-delete`
* [Create groups](/artifactory/docs/jf-rt-group-create) — `jf rt group-create`
* [Add users to groups](/artifactory/docs/jf-rt-group-add-users) — `jf rt group-add-users`
* [Delete groups](/artifactory/docs/jf-rt-group-delete) — `jf rt group-delete`
* [Permission targets](/docs/permission-targets) — template, create, update, and delete commands

***

## When to Use These Commands

| Task                                                 | Target Audience | Command(s)                                                   |
| ---------------------------------------------------- | --------------- | ------------------------------------------------------------ |
| Set up access control for a new team or project      | Platform Admin  | `permission-target-template` then `permission-target-create` |
| Onboard users in bulk during org migration           | Platform Admin  | `users-create` (CSV), `group-create`, `group-add-users`      |
| Create a single user for testing or service accounts | DevOps Engineer | `user-create`                                                |
| Clean up stale users or groups                       | Platform Admin  | `users-delete`, `group-delete`                               |
| Manage repository configurations in CI/CD            | DevOps Engineer | `repo-template` then `repo-create` / `repo-update`           |
| Set up replication between instances                 | Platform Admin  | `replication-create`                                         |

***

## Create Users

The `jf rt users-create` command creates users in bulk from a CSV file (usernames, passwords, and emails).

**To create users from a CSV file:**

* Follow the steps and CSV format in [jf rt users-create](/artifactory/docs/jf-rt-users-create).

***

## Delete Users

The `jf rt users-delete` command removes users by comma-separated usernames or from a CSV file.

**To delete users:**

* Follow the procedures in [jf rt users-delete](/artifactory/docs/jf-rt-users-delete).

***

## Create Groups

The `jf rt group-create` command creates a new user group in Artifactory.

**To create a group:**

* Follow the procedures in [jf rt group-create](/artifactory/docs/jf-rt-group-create).

***

## Add Users to Groups

The `jf rt group-add-users` command adds existing users to a group.

**To add users to a group:**

* Follow the procedures in [jf rt group-add-users](/artifactory/docs/jf-rt-group-add-users).

***

## Delete Groups

The `jf rt group-delete` command removes a group from Artifactory.

**To delete a group:**

* Follow the procedures in [jf rt group-delete](/artifactory/docs/jf-rt-group-delete).

<br />

***

<br />

## Manage Permission Targets

JFrog CLI offers commands creating, updating and deleting permission targets in Artifactory. To make it easier to create and update permission targets, the commands accept a pre-defined configuration template file.

**To manage permission targets with the CLI:**

* Use the linked command pages below in the order that matches your task (template first, then create or update, or delete when needed).

For the full command reference for permission target management, see the individual command pages:

* [jf rt permission-target-template](/artifactory/docs/jf-rt-permission-target-template) — Create a JSON configuration template interactively
* [jf rt permission-target-update](/artifactory/docs/jf-rt-permission-target-update) — Create or update a permission target from a template
* [jf rt permission-target-delete](/artifactory/docs/jf-rt-permission-target-delete) — Permanently delete a permission target

<br />