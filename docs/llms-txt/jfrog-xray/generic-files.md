# Source: https://docs.jfrog.com/artifactory/docs/generic-files.md

# Manage Generic Files in Artifactory with JFrog CLI

The generic files commands allow you to perform common file operations in JFrog Artifactory, including uploading, downloading, copying, moving, deleting files, and managing file properties.

All commands in this section use the `jf rt` prefix for Artifactory operations.

This topic covers the following tasks:

* [Upload files](#uploading-files)
* [Download files](#downloading-files)
* [Copy files](#copying-files)
* [Move files](#moving-files)
* [Delete files](#deleting-files)
* [Search for files](#searching-files)
* [Set file properties](#setting-file-properties)
* [Delete file properties](#deleting-file-properties)
* [Use File Specs](#using-file-specs)

***

## Uploading Files

Upload files from the local file system to Artifactory.

**To upload files to Artifactory:**

* Run `jf rt upload` (`jf rt u`) with a local source path, an Artifactory target path, and any options from the Command Options table (see Command and Examples below).

### Command

```
jf rt upload <source path> <target path> [command options]
```

**Abbreviation**: `jf rt u`

### Arguments

| Argument    | Description                                                                                                                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source path | Path to the local file system, including wildcards or a regular expression (if `--regexp` is used).                                                                         |
| Target path | Target path in Artifactory in the following format: `[repository name]/[repository path]`. If the target path ends with a `/` the source file/folder name will be appended. |

### Command Options

| Command option       | Description                                                                                                                                                                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spec`             | Path to a file spec. For more details, see Using File Specs.                                                                                                                                                                                                                |
| `--server-id`        | Server ID configured using the `jf c add` command. If not specified, the default configured Artifactory server is used.                                                                                                                                                     |
| `--build-name`       | Build name. For more details, see Build Integration.                                                                                                                                                                                                                        |
| `--build-number`     | Build number. For more details, see Build Integration.                                                                                                                                                                                                                      |
| `--project`          | JFrog project key.                                                                                                                                                                                                                                                          |
| `--module`           | Optional module name for the build-info.                                                                                                                                                                                                                                    |
| `--target-props`     | List of properties to attach to the uploaded artifacts, in the form of `key1=value1;key2=value2,...`.                                                                                                                                                                       |
| `--deb`              | Used for Debian packages only. Specifies the distribution/component/architecture of the package. Format: `d/c/a`. At least one file with the `deb` extension should be uploaded.                                                                                            |
| `--archive`          | Set to `zip` to pack and deploy the files to Artifactory inside a ZIP archive. The only supported value is `zip`. **Note:** The target path must be a file path, not a directory — do not use a trailing `/`. Example: `jf rt u "*.txt" my-repo/archive.zip --archive=zip`. |
| `--flat`             | Default: `false`. If true, files are uploaded to the exact target path specified and their hierarchy in the source file system is ignored. If false, files are uploaded to the target path while maintaining their file system hierarchy.                                   |
| `--recursive`        | Default: `true`. If true, files are also collected from sub-folders of the source directory for upload. If false, only files specifically in the source directory are uploaded.                                                                                             |
| `--regexp`           | Default: `false`. If true, the command will interpret the first argument as a regular expression which must match the path to files to be uploaded. The command will only use the captured groups as the file path in Artifactory.                                          |
| `--ant`              | Default: `false`. If true, the command will interpret the first argument as an ANT pattern.                                                                                                                                                                                 |
| `--threads`          | Default: `3`. The number of parallel threads used to upload the files.                                                                                                                                                                                                      |
| `--dry-run`          | Default: `false`. If true, the command only indicates what files would be uploaded, but does not actually upload them.                                                                                                                                                      |
| `--symlinks`         | Default: `false`. If true, the command will preserve the soft links structure in Artifactory. The `--symlinks` option is supported only on Linux and macOS.                                                                                                                 |
| `--explode`          | Default: `false`. If true, the command will extract an archive after it is deployed to Artifactory. Supported compression formats are: `zip`, `tar`, `tar.gz`, `tgz`.                                                                                                       |
| `--include-dirs`     | Default: `false`. If true, the source directory path is also taken into account when uploading.                                                                                                                                                                             |
| `--exclusions`       | A list of Semicolon-separated patterns (ANT, regular expression or wildcard depending on the command) that determine which files to exclude from the operation.                                                                                                             |
| `--sync-deletes`     | Specific path in Artifactory, under which to sync artifacts after upload. When this argument is provided, all artifacts under the specified path are removed from Artifactory, except for those matching the uploaded files pattern.                                        |
| `--quiet`            | Default: `false` (or `true` when the `CI` environment variable is set). If true, the `--sync-deletes` confirmation prompt is skipped.                                                                                                                                       |
| `--fail-no-op`       | Default: `false`. Set to true to fail the command with exit code 2 if no files are affected.                                                                                                                                                                                |
| `--retries`          | Default: `3`. Number of upload retries.                                                                                                                                                                                                                                     |
| `--retry-wait-time`  | Default: `0s`. Number of seconds or milliseconds to wait between retries. The numeric value should either end with `s` for seconds or `ms` for milliseconds.                                                                                                                |
| `--detailed-summary` | Default: `false`. Set to true to include a list of the affected files as part of the command output summary.                                                                                                                                                                |
| `--insecure-tls`     | Default: `false`. Set to true to skip TLS certificates verification.                                                                                                                                                                                                        |
| `--min-split`        | Default: `200`. Minimum file size in MiB required to attempt multi-part upload. Files larger than this value will be uploaded in parts.                                                                                                                                     |
| `--split-count`      | Default: `5`. Number of parts to split a file for multi-part upload. Requires `--min-split`.                                                                                                                                                                                |
| `--chunk-size`       | Default: `20`. Size of each part in MiB for multi-part upload.                                                                                                                                                                                                              |

### Examples

**Example 1**: Upload a single file to a repository:

```bash
jf rt u path/to/file.txt my-repo/path/
```

**Example 2**: Upload all `.zip` files from the current directory:

```bash
jf rt u "*.zip" my-repo/packages/
```

**Example 3**: Upload files while attaching properties:

```bash
jf rt u "*.jar" libs-release-local/org/acme/ --target-props="version=1.0;build=100"
```

**Example 4**: Upload and extract an archive:

```bash
jf rt u my-archive.zip my-repo/extracted/ --explode
```

**Example 5**: Upload using regular expression:

```bash
jf rt u "(.+)-sources\.jar" libs-release-local/{1}/ --regexp
```

***

## Downloading Files

Download files from Artifactory to the local file system.

**To download files from Artifactory:**

* Run `jf rt download` (`jf rt dl`) with an Artifactory source path, an optional local target path, and any options from the Command Options table (see Command and Examples below).

### Command

```
jf rt download <source path> [target path] [command options]
```

**Abbreviation**: `jf rt dl`

### Arguments

| Argument    | Description                                                                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source path | Path in Artifactory, in the following format: `[repository name]/[repository path]`. You can use wildcards to specify multiple files.              |
| Target path | (Optional) Path on the local file system to which the files should be downloaded. If not specified, files are downloaded to the current directory. |

### Command Options

| Command option                | Description                                                                                                                                                                                                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spec`                      | Path to a file spec. For more details, see [Using File Specs](/artifactory/docs/using-file-specs).                                                                                                                                                          |
| `--server-id`                 | Server ID configured using the `jf c add` command. If not specified, the default configured Artifactory server is used.                                                                                                                                     |
| `--build-name`                | Build name. For more details, see Build Integration.                                                                                                                                                                                                        |
| `--build-number`              | Build number. For more details, see Build Integration.                                                                                                                                                                                                      |
| `--project`                   | JFrog project key.                                                                                                                                                                                                                                          |
| `--module`                    | Optional module name for the build-info.                                                                                                                                                                                                                    |
| `--props`                     | List of semicolon-separated properties to filter artifacts by. Only artifacts with all of the specified properties are downloaded.                                                                                                                          |
| `--exclude-props`             | List of semicolon-separated properties to exclude artifacts by. Artifacts with any of these properties are not downloaded.                                                                                                                                  |
| `--build`                     | If specified, only artifacts of the specified build are downloaded. The format is `build-name/build-number`.                                                                                                                                                |
| `--bundle`                    | If specified, only artifacts from the specified release bundle are downloaded. The format is `bundle-name/bundle-version`.                                                                                                                                  |
| `--flat`                      | Default: `false`. If true, artifacts are downloaded to the exact target path specified and their hierarchy in the source repository is ignored. If false, artifacts are downloaded to the target path while maintaining their repository hierarchy.         |
| `--recursive`                 | Default: `true`. If true, artifacts are also downloaded from sub-paths under the specified source path. If false, only artifacts in the specified source path are downloaded.                                                                               |
| `--threads`                   | Default: `3`. The number of parallel threads used to download the files.                                                                                                                                                                                    |
| `--dry-run`                   | Default: `false`. If true, the command only indicates which artifacts would be downloaded, but does not actually download them. **Note:** The command still contacts Artifactory to resolve the artifact list, so a valid server connection is required.    |
| `--explode`                   | Default: `false`. If true, the command will extract an archive after it is downloaded. Supported compression formats are: `zip`, `tar`, `tar.gz`, `tgz`.                                                                                                    |
| `--bypass-archive-inspection` | Default: `false`. Set to true to bypass inspection of potentially malicious archive files during download.                                                                                                                                                  |
| `--validate-symlinks`         | Default: `false`. If true, the command will validate that symlinks are pointing to files within the download target directory.                                                                                                                              |
| `--include-dirs`              | Default: `false`. If true, the source directory path is also taken into account when downloading.                                                                                                                                                           |
| `--exclusions`                | A list of semicolon-separated patterns (ANT, regular expression or wildcard depending on the command) that determine which files to exclude from the operation.                                                                                             |
| `--sync-deletes`              | Specific local file system path to synchronize artifacts during download. All files under this path that are not downloaded from Artifactory will be deleted.                                                                                               |
| `--quiet`                     | Default: `false` (or `true` when the `CI` environment variable is set). If true, the `--sync-deletes` confirmation prompt is skipped.                                                                                                                       |
| `--fail-no-op`                | Default: `false`. Set to true to fail the command with exit code 2 if no files are affected.                                                                                                                                                                |
| `--retries`                   | Default: `3`. Number of download retries.                                                                                                                                                                                                                   |
| `--retry-wait-time`           | Default: `0s`. Number of seconds or milliseconds to wait between retries. The numeric value should either end with `s` for seconds or `ms` for milliseconds.                                                                                                |
| `--detailed-summary`          | Default: `false`. Set to true to include a list of the affected files as part of the command output summary.                                                                                                                                                |
| `--insecure-tls`              | Default: `false`. Set to true to skip TLS certificates verification.                                                                                                                                                                                        |
| `--gpg-key`                   | Path to the public GPG key file located on the file system. Used to validate downloaded release bundle files.                                                                                                                                               |
| `--sort-by`                   | List of semicolon-separated fields to sort by. The fields must be part of the [Artifactory Query Language (AQL) `items` domain](https://docs.jfrog.com/integrations/docs/artifactory-query-language). Common values: `created`, `modified`, `name`, `size`. |
| `--sort-order`                | Default: `asc`. The order by which fields in the `--sort-by` option should be sorted. Accepts `asc` (ascending) or `desc` (descending).                                                                                                                     |
| `--limit`                     | The maximum number of items to fetch. Usually used with `--sort-by`.                                                                                                                                                                                        |
| `--offset`                    | The offset from which to start fetching items. Usually used with `--sort-by`.                                                                                                                                                                               |
| `--archive-entries`           | **Deprecated.** No longer supported as of Artifactory 7.90.5. If specified, only archive entries matching this pattern are downloaded. The format is `path/inside/archive`.                                                                                 |
| `--min-split`                 | Default: `5120` (in KB, approximately 5 MB). Minimum file size in kilobytes (KB) required to attempt multi-part download. Files larger than this size will be downloaded in parts. Note: This differs from upload, which uses MiB.                          |
| `--split-count`               | Default: `3`. Number of parts to split a file for multi-part download. Requires `--min-split`.                                                                                                                                                              |
| `--skip-checksum`             | Default: `false`. Set to true to skip verifying checksums when downloading files. This can improve download performance but reduces integrity verification.                                                                                                 |

### Examples

**Example 1**: Download a single file:

```bash
jf rt dl my-repo/path/to/file.txt
```

**Example 2**: Download all `.jar` files to a local directory:

```bash
jf rt dl "libs-release-local/*.jar" ./libs/
```

**Example 3**: Download files filtered by properties:

```bash
jf rt dl "my-repo/releases/" ./downloads/ --props="version=1.0;status=released"
```

**Example 4**: Download and extract an archive:

```bash
jf rt dl my-repo/archives/package.zip ./extracted/ --explode
```

**Example 5**: Download the 10 most recently modified files:

```bash
jf rt dl "my-repo/builds/" ./latest/ --sort-by="modified" --sort-order="desc" --limit=10
```

***

## Copying Files

Copy files from one location in Artifactory to another location within the same Artifactory instance.

**To copy files within Artifactory:**

* Run `jf rt copy` (`jf rt cp`) with source and target paths in Artifactory and any options from the Command Options table (see Command and Examples below).

### Command

```
jf rt copy <source path> <target path> [command options]
```

**Abbreviation**: `jf rt cp`

### Arguments

| Argument    | Description                                                                                                                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source path | Path in Artifactory, in the following format: `[repository name]/[repository path]`. You can use wildcards to specify multiple files.                                               |
| Target path | Target path in Artifactory in the following format: `[repository name]/[repository path]`. If the target path ends with a `/`, the source path's last path element is concatenated. |

### Command Options

| Command option      | Description                                                                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spec`            | Path to a file spec. For more details, see Using File Specs.                                                                                                                                                                                                |
| `--server-id`       | Server ID configured using the `jf c add` command. If not specified, the default configured Artifactory server is used.                                                                                                                                     |
| `--project`         | JFrog project key.                                                                                                                                                                                                                                          |
| `--props`           | List of semicolon-separated properties to filter artifacts by. Only artifacts with all of the specified properties are copied.                                                                                                                              |
| `--exclude-props`   | List of semicolon-separated properties to exclude artifacts by. Artifacts with any of these properties are not copied.                                                                                                                                      |
| `--build`           | If specified, only artifacts of the specified build are copied. The format is `build-name/build-number`.                                                                                                                                                    |
| `--bundle`          | If specified, only artifacts from the specified release bundle are copied. The format is `bundle-name/bundle-version`.                                                                                                                                      |
| `--flat`            | Default: `false`. If true, artifacts are copied to the exact target path specified and their hierarchy in the source repository is ignored. If false, artifacts are copied to the target path while maintaining their repository hierarchy.                 |
| `--recursive`       | Default: `true`. If true, artifacts are also copied from sub-paths under the specified source path. If false, only artifacts in the specified source path are copied.                                                                                       |
| `--threads`         | Default: `3`. The number of parallel threads used to copy the files.                                                                                                                                                                                        |
| `--dry-run`         | Default: `false`. If true, the command only indicates which artifacts would be copied, but does not actually copy them. **Note:** The command still contacts Artifactory to resolve the artifact list, so a valid server connection is required.            |
| `--exclusions`      | A list of semicolon-separated patterns (ANT, regular expression or wildcard depending on the command) that determine which files to exclude from the operation.                                                                                             |
| `--fail-no-op`      | Default: `false`. Set to true to fail the command with exit code 2 if no files are affected.                                                                                                                                                                |
| `--retries`         | Default: `3`. Number of copy retries.                                                                                                                                                                                                                       |
| `--retry-wait-time` | Default: `0s`. Number of seconds or milliseconds to wait between retries.                                                                                                                                                                                   |
| `--insecure-tls`    | Default: `false`. Set to true to skip TLS certificates verification.                                                                                                                                                                                        |
| `--sort-by`         | List of semicolon-separated fields to sort by. The fields must be part of the [Artifactory Query Language (AQL) `items` domain](https://docs.jfrog.com/integrations/docs/artifactory-query-language). Common values: `created`, `modified`, `name`, `size`. |
| `--sort-order`      | Default: `asc`. The order by which fields in the `--sort-by` option should be sorted. Accepts `asc` (ascending) or `desc` (descending).                                                                                                                     |
| `--limit`           | The maximum number of items to copy. Usually used with `--sort-by`.                                                                                                                                                                                         |
| `--offset`          | The offset from which to start copying items. Usually used with `--sort-by`.                                                                                                                                                                                |

### Examples

**Example 1**: Copy a single file between repositories:

```bash
jf rt cp libs-snapshot-local/org/acme/1.0/ libs-release-local/org/acme/1.0/
```

**Example 2**: Copy all `.jar` files to another repository:

```bash
jf rt cp "libs-snapshot-local/*.jar" libs-release-local/releases/
```

**Example 3**: Copy files using placeholders:

```bash
jf rt cp "libs-snapshot-local/org/(.*)/(.*)/(.*)\.jar" "libs-release-local/org/{1}/{2}/{3}.jar" --regexp
```

***

## Moving Files

Move files from one location in Artifactory to another location within the same Artifactory instance.

**To move files within Artifactory:**

* Run `jf rt move` (`jf rt mv`) with source and target paths in Artifactory and any options from the Command Options table (see Command and Examples below).

### Command

```
jf rt move <source path> <target path> [command options]
```

**Abbreviation**: `jf rt mv`

### Arguments

| Argument    | Description                                                                                                                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source path | Path in Artifactory, in the following format: `[repository name]/[repository path]`. You can use wildcards to specify multiple files.                                               |
| Target path | Target path in Artifactory in the following format: `[repository name]/[repository path]`. If the target path ends with a `/`, the source path's last path element is concatenated. |

### Command Options

| Command option      | Description                                                                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spec`            | Path to a file spec. For more details, see Using File Specs.                                                                                                                                                                                                |
| `--server-id`       | Server ID configured using the `jf c add` command. If not specified, the default configured Artifactory server is used.                                                                                                                                     |
| `--project`         | JFrog project key.                                                                                                                                                                                                                                          |
| `--props`           | List of semicolon-separated properties to filter artifacts by. Only artifacts with all of the specified properties are moved.                                                                                                                               |
| `--exclude-props`   | List of semicolon-separated properties to exclude artifacts by. Artifacts with any of these properties are not moved.                                                                                                                                       |
| `--build`           | If specified, only artifacts of the specified build are moved. The format is `build-name/build-number`.                                                                                                                                                     |
| `--flat`            | Default: `false`. If true, artifacts are moved to the exact target path specified and their hierarchy in the source repository is ignored. If false, artifacts are moved to the target path while maintaining their repository hierarchy.                   |
| `--recursive`       | Default: `true`. If true, artifacts are also moved from sub-paths under the specified source path. If false, only artifacts in the specified source path are moved.                                                                                         |
| `--threads`         | Default: `3`. The number of parallel threads used to move the files.                                                                                                                                                                                        |
| `--dry-run`         | Default: `false`. If true, the command only indicates which artifacts would be moved, but does not actually move them. **Note:** The command still contacts Artifactory to resolve the artifact list, so a valid server connection is required.             |
| `--exclusions`      | A list of semicolon-separated patterns (ANT, regular expression or wildcard depending on the command) that determine which files to exclude from the operation.                                                                                             |
| `--fail-no-op`      | Default: `false`. Set to true to fail the command with exit code 2 if no files are affected.                                                                                                                                                                |
| `--retries`         | Default: `3`. Number of move retries.                                                                                                                                                                                                                       |
| `--retry-wait-time` | Default: `0s`. Number of seconds or milliseconds to wait between retries.                                                                                                                                                                                   |
| `--insecure-tls`    | Default: `false`. Set to true to skip TLS certificates verification.                                                                                                                                                                                        |
| `--sort-by`         | List of semicolon-separated fields to sort by. The fields must be part of the [Artifactory Query Language (AQL) `items` domain](https://docs.jfrog.com/integrations/docs/artifactory-query-language). Common values: `created`, `modified`, `name`, `size`. |
| `--sort-order`      | Default: `asc`. The order by which fields in the `--sort-by` option should be sorted. Accepts `asc` (ascending) or `desc` (descending).                                                                                                                     |
| `--limit`           | The maximum number of items to move. Usually used with `--sort-by`.                                                                                                                                                                                         |
| `--offset`          | The offset from which to start moving items. Usually used with `--sort-by`.                                                                                                                                                                                 |

### Examples

**Example 1**: Move a file between repositories:

```bash
jf rt mv libs-snapshot-local/org/acme/artifact-1.0.jar libs-release-local/org/acme/
```

**Example 2**: Move all snapshot builds to release:

```bash
jf rt mv "libs-snapshot-local/org/acme/*-SNAPSHOT.jar" libs-release-local/org/acme/
```

***

## Deleting Files

Delete files from Artifactory.

**To delete files from Artifactory:**

* Run `jf rt delete` (`jf rt del`) with the Artifactory path pattern and any options from the Command Options table (see Command and Examples below).

### Command

```
jf rt delete <delete path> [command options]
```

**Abbreviation**: `jf rt del`

### Arguments

| Argument    | Description                                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Delete path | Path in Artifactory, in the following format: `[repository name]/[repository path]`. You can use wildcards to specify multiple files. |

### Command Options

| Command option      | Description                                                                                                                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--spec`            | Path to a file spec. For more details, see Using File Specs.                                                                                                                                                                                                                                                                         |
| `--server-id`       | Server ID configured using the `jf c add` command. If not specified, the default configured Artifactory server is used.                                                                                                                                                                                                              |
| `--props`           | List of semicolon-separated properties to filter artifacts by. Only artifacts with all of the specified properties are deleted.                                                                                                                                                                                                      |
| `--exclude-props`   | List of semicolon-separated properties to exclude artifacts by. Artifacts with any of these properties are not deleted.                                                                                                                                                                                                              |
| `--build`           | If specified, only artifacts of the specified build are deleted. The format is `build-name/build-number`.                                                                                                                                                                                                                            |
| `--recursive`       | Default: `true`. If true, artifacts are also deleted from sub-paths under the specified path. If false, only artifacts in the specified path are deleted.                                                                                                                                                                            |
| `--threads`         | Default: `3`. The number of parallel threads used to delete the files.                                                                                                                                                                                                                                                               |
| `--dry-run`         | Default: `false`. If true, the command only indicates which artifacts would be deleted, but does not actually delete them. **Note:** The command still contacts Artifactory to resolve the artifact list, so a valid server connection is required.                                                                                  |
| `--quiet`           | Default: Depends on CI environment variable. Set to true to skip the delete confirmation message. When the CI environment variable is set (common in CI/CD pipelines), this flag defaults to true automatically. In interactive terminal sessions where CI is not set, the default is false and a confirmation prompt will be shown. |
| `--exclusions`      | A list of semicolon-separated patterns (ANT, regular expression or wildcard depending on the command) that determine which files to exclude from the operation.                                                                                                                                                                      |
| `--fail-no-op`      | Default: `false`. Set to true to fail the command with exit code 2 if no files are affected.                                                                                                                                                                                                                                         |
| `--retries`         | Default: `3`. Number of delete retries.                                                                                                                                                                                                                                                                                              |
| `--retry-wait-time` | Default: `0s`. Number of seconds or milliseconds to wait between retries.                                                                                                                                                                                                                                                            |
| `--insecure-tls`    | Default: `false`. Set to true to skip TLS certificates verification.                                                                                                                                                                                                                                                                 |
| `--sort-by`         | List of semicolon-separated fields to sort by. The fields must be part of the [Artifactory Query Language (AQL) `items` domain](https://docs.jfrog.com/integrations/docs/artifactory-query-language). Common values: `created`, `modified`, `name`, `size`.                                                                          |
| `--sort-order`      | Default: `asc`. The order by which fields in the `--sort-by` option should be sorted. Accepts `asc` (ascending) or `desc` (descending).                                                                                                                                                                                              |
| `--limit`           | The maximum number of items to delete. Usually used with `--sort-by`.                                                                                                                                                                                                                                                                |
| `--offset`          | The offset from which to start deleting items. Usually used with `--sort-by`.                                                                                                                                                                                                                                                        |

### Examples

**Example 1**: Delete a single file:

```bash
jf rt del my-repo/path/to/file.txt
```

**Example 2**: Delete all `.tmp` files:

```bash
jf rt del "my-repo/**/*.tmp"
```

**Example 3**: Delete files without confirmation (CI mode):

```bash
jf rt del "my-repo/old-builds/" --quiet
```

**Example 4**: Dry run to preview what would be deleted:

```bash
jf rt del "my-repo/snapshots/" --dry-run
```

***

## Searching Files

Search for files in Artifactory.

**To search for files in Artifactory:**

* Run `jf rt search` (`jf rt s`) with the Artifactory path pattern and any options from the Command Options table (see Command and Examples below).

### Command

```
jf rt search <search path> [command options]
```

**Abbreviation**: `jf rt s`

### Arguments

| Argument    | Description                                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Search path | Path in Artifactory, in the following format: `[repository name]/[repository path]`. You can use wildcards to specify multiple files. |

### Command Options

| Command option      | Description                                                                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spec`            | Path to a file spec. For more details, see Using File Specs.                                                                                                                                                                                                |
| `--server-id`       | Server ID configured using the `jf c add` command. If not specified, the default configured Artifactory server is used.                                                                                                                                     |
| `--props`           | List of semicolon-separated properties to filter artifacts by. Only artifacts with all of the specified properties are included in results.                                                                                                                 |
| `--exclude-props`   | List of semicolon-separated properties to exclude artifacts by. Artifacts with any of these properties are excluded from results.                                                                                                                           |
| `--build`           | If specified, only artifacts of the specified build are included. The format is `build-name/build-number`.                                                                                                                                                  |
| `--bundle`          | If specified, only artifacts from the specified release bundle are included. The format is `bundle-name/bundle-version`.                                                                                                                                    |
| `--recursive`       | Default: `true`. If true, artifacts are also searched in sub-paths under the specified path. If false, only artifacts in the specified path are searched.                                                                                                   |
| `--include-dirs`    | Default: `false`. If true, directories are also included in the search results.                                                                                                                                                                             |
| `--exclusions`      | A list of semicolon-separated patterns (ANT, regular expression or wildcard depending on the command) that determine which files to exclude from the search.                                                                                                |
| `--count`           | Default: `false`. If true, only the total count of matching artifacts is returned, rather than the full list.                                                                                                                                               |
| `--fail-no-op`      | Default: `false`. Set to true to fail the command with exit code 2 if no files are found.                                                                                                                                                                   |
| `--retries`         | Default: `3`. Number of search retries.                                                                                                                                                                                                                     |
| `--retry-wait-time` | Default: `0s`. Number of seconds or milliseconds to wait between retries.                                                                                                                                                                                   |
| `--insecure-tls`    | Default: `false`. Set to true to skip TLS certificates verification.                                                                                                                                                                                        |
| `--transitive`      | Default: `false`. If true, and the search path targets a remote repository, the command will search through the remote repository's cache as well as its source.                                                                                            |
| `--include`         | List of semicolon-separated fields to include in the output. By default, all fields are included. Available fields: name, repo, path, actual\_md5, actual\_sha1, sha256, size, created, modified, modified\_by, created\_by, props.                         |
| `--sort-by`         | List of semicolon-separated fields to sort by. The fields must be part of the [Artifactory Query Language (AQL) `items` domain](https://docs.jfrog.com/integrations/docs/artifactory-query-language). Common values: `created`, `modified`, `name`, `size`. |
| `--sort-order`      | Default: `asc`. The order by which fields in the `--sort-by` option should be sorted. Accepts `asc` (ascending) or `desc` (descending).                                                                                                                     |
| `--limit`           | The maximum number of items to return. Usually used with `--sort-by`.                                                                                                                                                                                       |
| `--offset`          | The offset from which to start returning items. Usually used with `--sort-by`.                                                                                                                                                                              |

### Examples

**Example 1**: Search for all `.jar` files:

```bash
jf rt s "libs-release-local/*.jar"
```

**Example 2**: Search with property filter:

```bash
jf rt s "my-repo/" --props="version=1.0;status=released"
```

**Example 3**: Count matching files:

```bash
jf rt s "my-repo/builds/" --count
```

**Example 4**: Search and return only specific fields:

```bash
jf rt s "my-repo/" --include="name;size;modified"
```

**Example 5**: Get the 5 largest files:

```bash
jf rt s "my-repo/" --sort-by="size" --sort-order="desc" --limit=5
```

***

## Setting File Properties

Set properties on files in Artifactory.

**To set properties on files in Artifactory:**

* Run `jf rt set-props` (`jf rt sp`) with a files pattern, a properties string, and any options from the Command Options table (see Command and Examples below).

### Command

```
jf rt set-props <files pattern> <files properties> [command options]
```

**Abbreviation**: `jf rt sp`

### Arguments

| Argument         | Description                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Files pattern    | Path in Artifactory, in the following format: `[repository name]/[repository path]`. You can use wildcards to specify multiple files. |
| Files properties | List of properties to attach to the matching artifacts, in the form of `key1=value1;key2=value2,...`.                                 |

### Command Options

| Command option      | Description                                                                                                                                                                                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spec`            | Path to a file spec. For more details, see Using File Specs.                                                                                                                                                                                                    |
| `--server-id`       | Server ID configured using the `jf c add` command. If not specified, the default configured Artifactory server is used.                                                                                                                                         |
| `--props`           | List of semicolon-separated properties to filter artifacts by. Only artifacts with all of the specified properties have their properties set.                                                                                                                   |
| `--exclude-props`   | List of semicolon-separated properties to exclude artifacts by. Artifacts with any of these properties do not have their properties set.                                                                                                                        |
| `--build`           | If specified, only artifacts of the specified build have their properties set. The format is `build-name/build-number`.                                                                                                                                         |
| `--bundle`          | If specified, only artifacts from the specified release bundle have their properties set. The format is `bundle-name/bundle-version`.                                                                                                                           |
| `--recursive`       | Default: `true`. If true, properties are also set on artifacts in sub-paths under the specified path. If false, only artifacts in the specified path are affected.                                                                                              |
| `--include-dirs`    | Default: `false`. If true, directories also have their properties set.                                                                                                                                                                                          |
| `--exclusions`      | A list of semicolon-separated patterns (ANT, regular expression or wildcard depending on the command) that determine which files to exclude from the operation.                                                                                                 |
| `--fail-no-op`      | Default: `false`. Set to true to fail the command with exit code 2 if no files are affected.                                                                                                                                                                    |
| `--threads`         | Default: `3`. The number of parallel threads used to set properties.                                                                                                                                                                                            |
| `--retries`         | Default: `3`. Number of retries.                                                                                                                                                                                                                                |
| `--retry-wait-time` | Default: `0s`. Number of seconds or milliseconds to wait between retries.                                                                                                                                                                                       |
| `--insecure-tls`    | Default: `false`. Set to true to skip TLS certificates verification.                                                                                                                                                                                            |
| `--repo-only`       | Default: `false`. Set to true to only set properties on artifacts in the repository matching the first part of the pattern, without traversing the full path pattern. This is useful when you want to set properties on all artifacts in a specific repository. |

### Examples

**Example 1**: Set a single property:

```bash
jf rt sp "my-repo/path/to/file.jar" "status=released"
```

**Example 2**: Set multiple properties:

```bash
jf rt sp "my-repo/builds/1.0/" "version=1.0;env=production;approved=true"
```

**Example 3**: Set properties on files matching a pattern:

```bash
jf rt sp "libs-release-local/*.jar" "type=library"
```

**Example 4**: Set properties only in the specified repository (without traversing paths):

```bash
jf rt sp "my-repo/" "scanned=true" --repo-only
```

***

## Deleting File Properties

Delete properties from files in Artifactory.

**To delete properties from files in Artifactory:**

* Run `jf rt delete-props` (`jf rt delp`) with a files pattern, a comma-separated property key list, and any options from the Command Options table (see Command and Examples below).

### Command

```
jf rt delete-props <files pattern> <properties list> [command options]
```

**Abbreviation**: `jf rt delp`

### Arguments

| Argument        | Description                                                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Files pattern   | Path in Artifactory, in the following format: `[repository name]/[repository path]`. You can use wildcards to specify multiple files. |
| Properties list | Comma-separated list of property keys to delete from the matching artifacts.                                                          |

### Command Options

| Command option      | Description                                                                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spec`            | Path to a file spec. For more details, see Using File Specs.                                                                                                               |
| `--server-id`       | Server ID configured using the `jf c add` command. If not specified, the default configured Artifactory server is used.                                                    |
| `--props`           | List of semicolon-separated properties to filter artifacts by. Only artifacts with all of the specified properties have their properties deleted.                          |
| `--exclude-props`   | List of semicolon-separated properties to exclude artifacts by. Artifacts with any of these properties do not have their properties deleted.                               |
| `--build`           | If specified, only artifacts of the specified build have their properties deleted. The format is `build-name/build-number`.                                                |
| `--bundle`          | If specified, only artifacts from the specified release bundle have their properties deleted. The format is `bundle-name/bundle-version`.                                  |
| `--recursive`       | Default: `true`. If true, properties are also deleted from artifacts in sub-paths under the specified path. If false, only artifacts in the specified path are affected.   |
| `--include-dirs`    | Default: `false`. If true, directories also have their properties deleted.                                                                                                 |
| `--exclusions`      | A list of semicolon-separated patterns (ANT, regular expression or wildcard depending on the command) that determine which files to exclude from the operation.            |
| `--fail-no-op`      | Default: `false`. Set to true to fail the command with exit code 2 if no files are affected.                                                                               |
| `--threads`         | Default: `3`. The number of parallel threads used to delete properties.                                                                                                    |
| `--retries`         | Default: `3`. Number of retries.                                                                                                                                           |
| `--retry-wait-time` | Default: `0s`. Number of seconds or milliseconds to wait between retries.                                                                                                  |
| `--insecure-tls`    | Default: `false`. Set to true to skip TLS certificates verification.                                                                                                       |
| `--repo-only`       | Default: `false`. Set to true to only delete properties from artifacts in the repository matching the first part of the pattern, without traversing the full path pattern. |

### Examples

**Example 1**: Delete a single property:

```bash
jf rt delp "my-repo/path/to/file.jar" "status"
```

**Example 2**: Delete multiple properties:

```bash
jf rt delp "my-repo/builds/1.0/" "temp,draft,wip"
```

**Example 3**: Delete properties from files matching a pattern:

```bash
jf rt delp "libs-release-local/*.jar" "snapshot,dev"
```

**Example 4**: Delete properties only in the specified repository:

```bash
jf rt delp "my-repo/" "temp-prop" --repo-only
```

***

## Using File Specs

File specs are JSON files that define the source and target paths for file operations. They provide a more flexible and reusable way to specify complex operations.

**To run an operation using a File Spec:**

* Pass `--spec=<path-to-json>` to `jf rt upload`, `jf rt download`, `jf rt copy`, `jf rt move`, `jf rt delete`, `jf rt search`, `jf rt set-props`, or `jf rt delete-props` (see Basic Structure, Using a File Spec, and the examples below).

### Basic Structure

```json
{
  "files": [
    {
      "pattern": "my-repo/path/to/files/*.jar",
      "target": "target-repo/path/",
      "props": "key1=value1;key2=value2",
      "recursive": "true",
      "flat": "false"
    }
  ]
}
```

### Common Properties

| Property      | Description                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| `pattern`     | Path pattern in Artifactory or local file system.                                                         |
| `target`      | Target path for upload, download, copy, or move operations.                                               |
| `props`       | Properties to filter artifacts by (download, copy, move, search, delete, set-props). Not used for upload. |
| `targetProps` | Properties to attach to uploaded artifacts (upload only). Use `key1=value1;key2=value2,...` format.       |
| `recursive`   | Whether to include sub-directories.                                                                       |
| `flat`        | Whether to preserve directory structure.                                                                  |
| `regexp`      | Whether to treat pattern as a regular expression.                                                         |
| `exclusions`  | Patterns to exclude.                                                                                      |
| `build`       | Build name and number filter.                                                                             |
| `bundle`      | Release bundle filter.                                                                                    |

### Using a File Spec

```bash
jf rt upload --spec=upload-spec.json
jf rt download --spec=download-spec.json
jf rt copy --spec=copy-spec.json
jf rt move --spec=move-spec.json
jf rt delete --spec=delete-spec.json
jf rt search --spec=search-spec.json
jf rt set-props --spec=setprops-spec.json
jf rt delete-props --spec=deleteprops-spec.json
```

### Example: Upload Spec

```json
{
  "files": [
    {
      "pattern": "./build/libs/*.jar",
      "target": "libs-release-local/org/acme/{1}/",
      "targetProps": "version=1.0;build.number=100"
    },
    {
      "pattern": "./build/docs/",
      "target": "docs-repo/acme/1.0/",
      "flat": "true"
    }
  ]
}
```

### Example: Download Spec

```json
{
  "files": [
    {
      "pattern": "libs-release-local/org/acme/*.jar",
      "target": "./libs/",
      "props": "version=1.0",
      "flat": "true"
    }
  ]
}
```

<br />