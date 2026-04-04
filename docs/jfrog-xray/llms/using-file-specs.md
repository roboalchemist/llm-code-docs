# Source: https://docs.jfrog.com/artifactory/docs/using-file-specs.md

# Use File Specs with JFrog CLI

You can perform complex file operations using multiple CLI commands. For example, you can upload different sets of files to different repositories. To simplify these operations, use the JFrog CLI download, upload, move, copy, and delete commands with the `--spec` option.

The `--spec` option replaces inline command arguments and options with a File Spec. Similarly, you can create and update release bundles using the `--spec` command option.

File Specs are supported by the following commands:

* **`jf rt upload`** -- Upload files from the local file system to Artifactory
* **`jf rt download`** -- Download files from Artifactory to the local file system
* **`jf rt copy`** -- Copy files between Artifactory repositories
* **`jf rt move`** -- Move files between Artifactory repositories
* **`jf rt delete`** -- Delete files from Artifactory
* **`jf rt search`** -- Search for files in Artifactory
* **`jf rt set-props`** -- Set properties on artifacts in Artifactory
* **`jf rt build-add-dependencies`** -- Add dependencies to a build
* **`jf ds rbc`** / **`jf ds rbu`** -- Create / update Release Bundles v1 *(requires the JFrog Distribution module to be enabled on your JFrog Platform instance)*

<Callout icon="❗️" theme="error">
  Important

  Some fields have different meanings depending on the command. For example, `pattern` refers to local file paths for upload, but Artifactory repository paths for download. Each field's per-command behavior is documented in the [Field Reference](#field-reference) section below.
</Callout>

Each command uses a file specification array in JSON format. The schema for each command is described in the following sections. If a command is issued with both inline options and a File Spec, the inline options override the corresponding settings in the File Spec.

***

## Parameterizing File Specs with `--spec-vars`

You can make a File Spec reusable across environments by using the `--spec-vars` option. This option substitutes `${variable}` placeholders inside a spec file at runtime.

**To substitute variables into a File Spec at runtime:**

1. Add `${variable}` placeholders to your JSON spec where values should be injected.
2. Run `jf rt <command> --spec <spec-file> --spec-vars "key1=value1;key2=value2;..."` (see Syntax and Example below).

**Syntax:**

```
jf rt <command> --spec <spec-file> --spec-vars "key1=value1;key2=value2;..."
```

**Example:** The following spec uses `${repo}` and `${version}` as variables.

**myspec.json**

```json
{
  "files": [
    {
      "pattern": "${repo}/releases/${version}/",
      "target": "downloads/${version}/"
    }
  ]
}
```

Run the same spec against different repositories without editing the file:

```
jf rt download --spec myspec.json --spec-vars "repo=my-prod-repo;version=2.1.0"
jf rt download --spec myspec.json --spec-vars "repo=my-staging-repo;version=2.1.0-rc1"
```

`--spec-vars` is supported by all commands that accept `--spec`: `jf rt upload`, `jf rt download`, `jf rt copy`, `jf rt move`, `jf rt delete`, `jf rt search`, and `jf rt set-props`.

***

## File Spec Schemas

The following sections show the JSON schema for the different commands that support File Specs.

### Copy and Move Commands Spec Schema

The file spec schema for the copy and move commands is as follows:

<Callout icon="📘" theme="info">
  Note

  Provide either `pattern` or `aql` — not both. They are mutually exclusive. Use `pattern` for wildcard-based path matching, or `aql` for advanced AQL query syntax.
</Callout>

```json
{
  "files": [
    {
      "pattern": "[Mandatory if 'aql' not used]",
      "aql": "[Mandatory if 'pattern' not used]",
      "target": "[Mandatory]",
      "props": "[Optional]",
      "excludeProps": "[Optional]",
      "recursive": "[Optional, Default: 'true']",
      "flat": "[Optional, Default: 'false']",
      "exclusions": "[Optional, Applicable only when 'pattern' is specified]",
      "archiveEntries": "[Deprecated — not supported since Artifactory 7.90.5. Using this field produces no results without any error.]",
      "build": "[Optional]",
      "bundle": "[Optional]",
      "validateSymlinks": "[Optional]",
      "sortBy": "[Optional]",
      "sortOrder": "[Optional, Default: 'asc']",
      "limit": "[Optional]",
      "offset": "[Optional]",
      "includeDeps": "[Optional, Default: 'false']",
      "excludeArtifacts": "[Optional, Default: 'false']",
      "project": "[Optional]"
    }
  ]
}
```

### Download Command Spec Schema

The file spec schema for the download command is as follows:

<Callout icon="📘" theme="info">
  Note

  Provide either `pattern` or `aql` — not both. They are mutually exclusive. Use `pattern` for wildcard-based path matching, or `aql` for advanced AQL query syntax.
</Callout>

```json
{
  "files": [
    {
      "pattern": "[Mandatory if 'aql' not used]",
      "aql": "[Mandatory if 'pattern' not used]",
      "target": "[Optional]",
      "props": "[Optional]",
      "excludeProps": "[Optional]",
      "recursive": "[Optional, Default: 'true']",
      "flat": "[Optional, Default: 'false']",
      "exclusions": "[Optional, Applicable only when 'pattern' is specified]",
      "archiveEntries": "[Deprecated — not supported since Artifactory 7.90.5. Using this field produces no results without any error.]",
      "build": "[Optional]",
      "bundle": "[Optional]",
      "sortBy": "[Optional]",
      "sortOrder": "[Optional, Default: 'asc']",
      "limit": "[Optional]",
      "offset": "[Optional]",
      "explode": "[Optional, Default: 'false']",
      "bypass-archive-inspection": "[Optional, Default: 'false']",
      "validateSymlinks": "[Optional, Default: 'false']",
      "includeDirs": "[Optional, Default: 'false']",
      "includeDeps": "[Optional, Default: 'false']",
      "excludeArtifacts": "[Optional, Default: 'false']",
      "gpg-key": "[Optional]",
      "project": "[Optional]"
    }
  ]
}
```

### Create and Update Release Bundle V1 Commands Spec Schema

The file spec schema for the create and update Release Bundle v1 commands is as follows:

<Callout icon="📘" theme="info">
  Note

  Provide either `pattern` or `aql` — not both. They are mutually exclusive. Use `pattern` for wildcard-based path matching, or `aql` for advanced AQL query syntax.
</Callout>

```json
{
  "files": [
    {
      "pattern": "[Mandatory if 'aql' not used]",
      "aql": "[Mandatory if 'pattern' not used]",
      "pathMapping": "[Optional, Applicable only when 'aql' is specified]",
      "target": "[Optional]",
      "props": "[Optional]",
      "targetProps": "[Optional]",
      "excludeProps": "[Optional]",
      "recursive": "[Optional, Default: 'true']",
      "flat": "[Optional, Default: 'false']",
      "exclusions": "[Optional, Applicable only when 'pattern' is specified]",
      "archiveEntries": "[Deprecated — not supported since Artifactory 7.90.5. Using this field produces no results without any error.]",
      "build": "[Optional]",
      "bundle": "[Optional]",
      "sortBy": "[Optional]",
      "sortOrder": "[Optional, Default: 'asc']",
      "limit": "[Optional]",
      "offset": "[Optional]",
      "project": "[Optional]"
    }
  ]
}
```

### Upload Command Spec Schema

The file spec schema for the upload command is as follows:

```json
{
  "files": [
    {
      "pattern": "[Mandatory]",
      "target": "[Mandatory]",
      "targetProps": "[Optional]",
      "recursive": "[Optional, Default: 'true']",
      "flat": "[Optional, Default: 'false']",
      "regexp": "[Optional, Default: 'false']",
      "ant": "[Optional, Default: 'false']",
      "archive": "[Optional, Must be: 'zip']",
      "exclusions": "[Optional]",
      "symlinks": "[Optional, Default: 'false']",
      "includeDirs": "[Optional, Default: 'false']",
      "explode": "[Optional, Default: 'false']",
      "project": "[Optional]"
    }
  ]
}
```

### Search, Set-Props and Delete Commands Spec Schema

The file spec schema for the search, set-props, and delete commands is as follows:

<Callout icon="📘" theme="info">
  Note

  Provide either `pattern` or `aql` — not both. They are mutually exclusive. Use `pattern` for wildcard-based path matching, or `aql` for advanced AQL query syntax.
</Callout>

```json
{
  "files": [
    {
      "pattern": "[Mandatory if 'aql' not used]",
      "aql": "[Mandatory if 'pattern' not used]",
      "props": "[Optional]",
      "excludeProps": "[Optional]",
      "recursive": "[Optional, Default: 'true']",
      "exclusions": "[Optional, Applicable only when 'pattern' is specified]",
      "archiveEntries": "[Deprecated — not supported since Artifactory 7.90.5. Using this field produces no results without any error.]",
      "build": "[Optional]",
      "bundle": "[Optional]",
      "sortBy": "[Optional]",
      "sortOrder": "[Optional, Default: 'asc']",
      "limit": "[Optional]",
      "offset": "[Optional]",
      "includeDirs": "[Optional, Default: 'false']",
      "includeDeps": "[Optional, Default: 'false']",
      "excludeArtifacts": "[Optional, Default: 'false']",
      "project": "[Optional]"
    }
  ]
}
```

### Build Add Dependencies Command Spec Schema

The file spec schema for the build-add-dependencies command is as follows:

```json
{
  "files": [
    {
      "pattern": "[Mandatory]",
      "recursive": "[Optional, Default: 'true']",
      "exclusions": "[Optional]",
      "regexp": "[Optional, Default: 'false']",
      "from-rt": "[Optional, Default: 'false']"
    }
  ]
}
```

***

## File Spec Examples

The following examples can help you get started with File Specs.

### Example 1: Download -- All Files from a Directory

Download all files from the `all-my-frogs/` directory in the `my-local-repo` repository to the local `froggy/` directory.

```json
{
  "files": [
    {
      "pattern": "my-local-repo/all-my-frogs/",
      "target": "froggy/"
    }
  ]
}
```

### Example 2: Download -- Files Filtered by Build

Download all files from `all-my-frogs/` in `my-local-repo`, but only include files that are artifacts of build number 5 of the `my-build` build.

```json
{
  "files": [
    {
      "pattern": "my-local-repo/all-my-frogs/",
      "target": "froggy/",
      "build": "my-build/5"
    }
  ]
}
```

### Example 3: Download -- Using AQL Query

Download all files retrieved by the AQL query to the `froggy/` directory.

```json
{
  "files": [
    {
      "aql": {
        "items.find": {
          "repo": "my-local-repo",
          "$or": [
            {
              "$and": [
                {
                  "path": {
                    "$match": "."
                  },
                  "name": {
                    "$match": "a1.in"
                  }
                }
              ]
            },
            {
              "$and": [
                {
                  "path": {
                    "$match": "*"
                  },
                  "name": {
                    "$match": "a1.in"
                  }
                }
              ]
            }
          ]
        }
      },
      "target": "froggy/"
    }
  ]
}
```

### Example 4: Upload -- Files with Properties

Upload all `.zip` files from the `resources` directory to the `zip/` folder and all `.tgz` files to the `tgz/` folder within the `all-my-frogs` repository. Tag `.zip` files with `type=zip; status=ready` and `.tgz` files with `type=tgz; status=ready`.

```json
{
  "files": [
    {
      "pattern": "resources/*.zip",
      "target": "all-my-frogs/zip/",
      "targetProps": "type=zip;status=ready"
    },
    {
      "pattern": "resources/*.tgz",
      "target": "all-my-frogs/tgz/",
      "targetProps": "type=tgz;status=ready"
    }
  ]
}
```

### Example 5: Upload -- Files by Extension

Upload all zip files located under the `resources` directory to the `zip` folder, under the `all-my-frogs` repository.

```json
{
  "files": [
    {
      "pattern": "resources/*.zip",
      "target": "all-my-frogs/zip/"
    }
  ]
}
```

### Example 6: Upload -- Archive and Deploy

Package all files located (including subdirectories) under the `resources` directory into a zip archive named `archive.zip`, and upload it into the root of the `all-my-frogs` repository.

```json
{
  "files": [
    {
      "pattern": "resources/",
      "archive": "zip",
      "target": "all-my-frogs/"
    }
  ]
}
```

### Example 7: Download -- With Exclusions

Download all files located under the `all-my-frogs` directory in the `my-local-repo` repository except for files with the `.txt` extension and all files inside the `all-my-frogs` directory with the `props.` prefix.

Notice that the exclude patterns do not include the repository.

```json
{
  "files": [
    {
      "pattern": "my-local-repo/all-my-frogs/",
      "exclusions": ["*.txt", "all-my-frog/props.*"]
    }
  ]
}
```

### Example 8: Download -- Most Recent File

Download the most recently uploaded file from the `all-my-frogs/` directory in the `my-local-repo` repository.

```json
{
  "files": [
    {
      "pattern": "my-local-repo/all-my-frogs/",
      "target": "all-my-frogs/files/",
      "sortBy": ["created"],
      "sortOrder": "desc",
      "limit": 1
    }
  ]
}
```

### Example 9: Search -- Largest Files with Sorting

Search for the three largest files located under the `all-my-frogs` directory in the `my-local-repo` repository. If there are files with the same size, sort them "internally" by creation date.

```json
{
  "files": [
    {
      "pattern": "my-local-repo/all-my-frogs/",
      "sortBy": ["size", "created"],
      "sortOrder": "desc",
      "limit": 3
    }
  ]
}
```

### Example 10: Download -- With Offset and Sorting

Download the second-latest file uploaded to the `all-my-frogs` directory in the `my-local-repo` repository.

```json
{
  "files": [
    {
      "pattern": "my-local-repo/all-my-frogs/",
      "target": "all-my-frogs/files/",
      "sortBy": ["created"],
      "sortOrder": "desc",
      "limit": 1,
      "offset": 1
    }
  ]
}
```

### Example 11: Delete -- Old Artifacts via AQL

This example shows how to delete artifacts in Artifactory under specified path based on how old they are.

The following File Spec finds all the folders which match the following criteria:

1. They are under the `myrepo` repository.
2. They are inside a folder with a name that matches `abc-*-xyz` and is located at the root of the repository.
3. Their name matches `ver*`
4. They were created more than 7 days ago.

```json
{
  "files": [
    {
      "aql": {
        "items.find": {
          "repo": "myrepo",
          "path": { "$match": "abc-*-xyz" },
          "name": { "$match": "ver*" },
          "type": "folder",
          "$or": [
            {
              "$and": [
                {
                  "created": { "$before": "7d" }
                }
              ]
            }
          ]
        }
      }
    }
  ]
}
```

### Example 12: Upload -- With Placeholders

This example uses [placeholders](#using-placeholders-in-file-specs). For each `.tgz` file in the source directory, create a corresponding folder in the target repository and upload the file there. For example, `froggy.tgz` is uploaded to `my-local-repo/froggy/`.

```json
{
  "files": [
    {
      "pattern": "(*).tgz",
      "target": "my-local-repo/{1}/"
    }
  ]
}
```

### Example 13: Upload -- Rename with Placeholders

This example uses [placeholders](#using-placeholders-in-file-specs). Upload all files whose name begins with `frog` to folder `frogfiles` in the target repository, but append its name with the text `-up`. For example, a file called `froggy.tgz` should be renamed `froggy.tgz-up`.

```json
{
  "files": [
    {
      "pattern": "(frog*)",
      "target": "my-local-repo/frogfiles/{1}-up",
      "recursive": "false"
    }
  ]
}
```

### Example 14: Download -- Placeholders vs Flat

The following two examples lead to the exact same outcome.

The first one uses [placeholders](#using-placeholders-in-file-specs), while the second one does not. Both examples download all files from the `generic-local` repository to be under the `my/local/path/` local file-system path, while maintaining the original Artifactory folder hierarchy. Notice the different flat values in the two examples.

```json
{
  "files": [
    {
      "pattern": "generic-local/{*}",
      "target": "my/local/path/{1}",
      "flat": "true"
    }
  ]
}
```

```json
{
  "files": [
    {
      "pattern": "generic-local/",
      "target": "my/local/path/",
      "flat": "false"
    }
  ]
}
```

### Example 15: Release Bundle -- Path Mapping

This example creates a Release Bundle v1 and applies `pathMapping` to the artifact paths after distributing the Release Bundle.

All occurrences of the `a1.in` file are fetched and mapped to the `froggy` repository at the edges.

1. Fetch all artifacts retrieved by the AQL query.
2. Create the Release Bundle v1 with the artifacts and apply the path mappings at the Edge nodes after distribution.

The `pathMapping` option is provided, allowing users to control the destination of the Release Bundle artifacts at the edges.

For more information, see [Create Release Bundle v1](/docs/create-release-bundles-v1).

```json
{
  "files": [
    {
      "aql": {
        "items.find": {
          "repo": "my-local-repo",
          "$and": [
            {
              "name": {
                "$match": "a1.in"
              }
            },
            {
              "$or": [
                {
                  "path": {
                    "$match": "."
                  }
                },
                {
                  "path": {
                    "$match": "*"
                  }
                }
              ]
            }
          ]
        }
      },
      "pathMapping": {
        "input": "my-local-repo/(.*)",
        "output": "froggy/$1"
      }
    }
  ]
}
```

***

## Schema Validation

[JSON schemas](https://json-schema.org/) allow you to annotate and validate JSON files. The JFrog File Spec schema is available in the [JSON Schema Store](https://www.schemastore.org/) catalog and at this link:

[https://github.com/jfrog/jfrog-cli/blob/v2/schema/filespec-schema.json](https://github.com/jfrog/jfrog-cli/blob/v2/schema/filespec-schema.json)

### Using JetBrains IDEs

JetBrains IDEs (IntelliJ IDEA, WebStorm, and so on) automatically apply the File Spec schema to files matching these patterns: `**/filespecs/*.json`, `*filespec*.json`, and `*.filespec`.

### Using Visual Studio Code

**To enable File Spec schema validation in Visual Studio Code:**

* **Option A:** Install the [JFrog VS Code extension](https://marketplace.visualstudio.com/items?itemName=JFrog.jfrog-vscode-extension), which applies the schema to matching File Spec files automatically.
* **Option B:** Open **Preferences: Open User Settings (JSON)** and merge the following object into the `json.schemas` array in your `settings.json`:

**settings.json**

```json
"json.schemas": [
  {
    "fileMatch": ["**/filespecs/*.json", "*filespec*.json", "*.filespec"],
    "url": "https://raw.githubusercontent.com/jfrog/jfrog-cli/v2/schema/filespec-schema.json"
  }
]
```

<Callout icon="📘" theme="info">
  Note

  If you already have a `json.schemas` array in your `settings.json`, add the object above as a new entry inside your existing array rather than replacing the entire array.
</Callout>

***

## Field Reference

### Common Fields

The following fields are available across most file spec commands:

| Field            | Type    | Default   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------- | ------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pattern`        | string  | -         | **Upload / build-add-dependencies:** Specifies a path on the local file system to files to be uploaded. Supports wildcards, and also regular expressions (when `regexp` is `"true"`) or ANT patterns (when `ant` is `"true"`). **Download / copy / move / search / delete / set-props:** Specifies a path in Artifactory in the format `[repository_name]/[repository_path]`. Supports wildcards. Cannot be used together with `aql`.                       |
| `aql`            | object  | -         | An AQL query that specifies artifacts in Artifactory.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `target`         | string  | `./`      | **Upload:** Specifies the destination path in Artifactory in the format `[repository_name]/[repository_path]`. Mandatory. **Download:** Specifies the local file system path to download files to. Optional; defaults to `./` (current directory). **Copy / Move:** Specifies the destination path in Artifactory. Mandatory. Supports [placeholders](#using-placeholders-in-file-specs) (`{1}`, `{2}`, and so on) referencing capture groups in `pattern`. |
| `props`          | string  | -         | **Not applicable to upload.** List of `key=value` pairs separated by semicolons. Only artifacts with all specified properties are matched. Used as a filter for download, copy, move, search, delete, and set-props commands. To set properties on uploaded artifacts, use `targetProps` instead.                                                                                                                                                           |
| `excludeProps`   | string  | -         | List of `key=value` pairs separated by semicolons. Artifacts with any of these properties are excluded.                                                                                                                                                                                                                                                                                                                                                     |
| `recursive`      | string  | `"true"`  | If `"true"`, files are also collected from sub-folders.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `flat`           | string  | `"false"` | If `"true"`, artifacts are placed at the exact target path, ignoring source hierarchy.                                                                                                                                                                                                                                                                                                                                                                      |
| `exclusions`     | array   | -         | Array of patterns to exclude from the operation.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `archiveEntries` | string  | -         | **Deprecated.** Not supported since Artifactory 7.90.5. Using this field silently produces no results without any error message. Do not use in new File Specs.                                                                                                                                                                                                                                                                                              |
| `build`          | string  | -         | If specified, only artifacts of the specified build are matched. Format: `build-name/build-number`.                                                                                                                                                                                                                                                                                                                                                         |
| `bundle`         | string  | -         | If specified, only artifacts of the specified bundle are matched. Format: `bundle-name/bundle-version`.                                                                                                                                                                                                                                                                                                                                                     |
| `sortBy`         | array   | -         | List of fields to sort by (for example, `["created"]`, `["size", "name"]`).                                                                                                                                                                                                                                                                                                                                                                                 |
| `sortOrder`      | string  | `"asc"`   | The order by which fields in `sortBy` should be sorted. Accepts `"asc"` or `"desc"`.                                                                                                                                                                                                                                                                                                                                                                        |
| `limit`          | integer | -         | The maximum number of items to fetch. Usually used with `sortBy`.                                                                                                                                                                                                                                                                                                                                                                                           |
| `offset`         | integer | -         | The offset from which to fetch items (how many items to skip). Usually used with `sortBy`.                                                                                                                                                                                                                                                                                                                                                                  |
| `project`        | string  | -         | JFrog project key.                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Copy and Move-Specific Fields

| Field              | Type   | Default   | Description                                                                                             |
| ------------------ | ------ | --------- | ------------------------------------------------------------------------------------------------------- |
| `validateSymlinks` | string | `"false"` | If `"true"`, validates that symlinks point to existing and unchanged files by comparing SHA1 checksums. |

### Upload-Specific Fields

| Field         | Type   | Default   | Description                                                                                                                                                                                                                                                                               |
| ------------- | ------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `targetProps` | string | -         | List of `key=value` pairs separated by semicolons (for example, `version=1.0;status=ready`). Sets these as JFrog properties on the uploaded artifacts. This is the upload equivalent of using `jf rt set-props` after uploading. Also available in release bundle create/update commands. |
| `regexp`      | string | `"false"` | If `"true"`, the pattern is interpreted as a regular expression.                                                                                                                                                                                                                          |
| `ant`         | string | `"false"` | If `"true"`, the pattern is interpreted as an ANT pattern.                                                                                                                                                                                                                                |
| `archive`     | string | -         | Set to `"zip"` to pack and deploy files inside a ZIP archive.                                                                                                                                                                                                                             |
| `symlinks`    | string | `"false"` | If `"true"`, preserves symbolic links structure in Artifactory.                                                                                                                                                                                                                           |
| `includeDirs` | string | `"false"` | If `"true"`, directories are also uploaded.                                                                                                                                                                                                                                               |
| `explode`     | string | `"false"` | If `"true"`, archives are extracted after upload.                                                                                                                                                                                                                                         |

### Download-Specific Fields

| Field                       | Type   | Default   | Description                                                                                        |
| --------------------------- | ------ | --------- | -------------------------------------------------------------------------------------------------- |
| `explode`                   | string | `"false"` | If `"true"`, archives are extracted after download. Supported formats: zip, tar, tar.gz, tgz.      |
| `bypass-archive-inspection` | string | `"false"` | If `"true"`, bypasses security inspection of archives before extraction.                           |
| `validateSymlinks`          | string | `"false"` | If `"true"`, validates that symlinks point to existing and unchanged files by comparing SHA1.      |
| `includeDirs`               | string | `"false"` | If `"true"`, directories are also downloaded.                                                      |
| `includeDeps`               | string | `"false"` | If `"true"`, dependencies of the specified build are also matched. Requires `build` field.         |
| `excludeArtifacts`          | string | `"false"` | If `"true"`, build artifacts are excluded (only dependencies are matched). Requires `build` field. |
| `gpg-key`                   | string | -         | Path to the public GPG key file for validating downloaded release bundles.                         |

### Release Bundle Fields

| Field                | Type   | Default | Description                                                                             |
| -------------------- | ------ | ------- | --------------------------------------------------------------------------------------- |
| `pathMapping`        | object | -       | Defines source and target paths for artifacts after distribution. Requires `aql` field. |
| `pathMapping.input`  | string | -       | Input regex pattern for path mapping.                                                   |
| `pathMapping.output` | string | -       | Output replacement pattern for path mapping.                                            |

### Build Add Dependencies Fields

| Field     | Type   | Default   | Description                                                                  |
| --------- | ------ | --------- | ---------------------------------------------------------------------------- |
| `from-rt` | string | `"false"` | If `"true"`, searches files in Artifactory instead of the local file system. |