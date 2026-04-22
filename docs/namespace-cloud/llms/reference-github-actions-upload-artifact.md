<!-- Source: https://namespace.so/docs/reference/github-actions/upload-artifact -->

# namespace-actions/upload-artifact

namespace-actions/upload-artifact@v1

[namespace-actions/upload-artifact](https://github.com/namespace-actions/upload-artifact) stores artifact archives
to Namespace high-performance storage. This action is 100% compatible with GitHub's [actions/upload-artifact](https://github.com/actions/upload-artifact).

To download artifacts from Namespace, use [namespace-actions/download-artifact](/docs/reference/github-actions/download-artifact).

## Prerequisites

This action only works with Namespace GitHub Runners, if you haven't yet migrated your workflows to Namespace runners, checkout
the [runner documentation](/docs/solutions/github-actions) first.

## Example

```
jobs:
  upload:
    name: Demo Upload Archive
    runs-on: namespace-profile-default
    steps:
      - name: Upload Archive
        uses: namespace-actions/upload-artifact@v1
        with:
          name: test-archive
          path: ./archive
```

## Example when running within a container

When running the `upload-artifact` action within a container, the necessary credentials to upload the artifact need to be forwarded:

```
jobs:
  upload:
    container:
      image: <my-image-ref>
      env:
        NSC_TOKEN_FILE: ${{ env.NSC_TOKEN_FILE }}
        NAMESPACE_ACTIONS_RESULTS_URL: ${{ env.NAMESPACE_ACTIONS_RESULTS_URL }}
        NAMESPACE_ACTIONS_RESULTS_SERVICE: ${{ env.NAMESPACE_ACTIONS_RESULTS_SERVICE }}
        NAMESPACE_ACTIONS_DIRECT_ZIP_UPLOAD: ${{ env.NAMESPACE_ACTIONS_DIRECT_ZIP_UPLOAD }}
      volumes:
        - /var/run/nsc/:/var/run/nsc/
    name: Demo Upload Archive
    runs-on: namespace-profile-default
    steps:
      - name: Upload Archive
        uses: namespace-actions/upload-artifact@v1
        with:
          name: test-archive
          path: ./archive
```

This ensures that the correct environment variable is set and that the files containing the critical credentials are correctly mounted into the container.

## Options

### name

Name of the artifact to upload.

Optional. Default is `artifact`.

### path

A file, directory or wildcard pattern that describes what to upload.

Required.

### if-no-files-found

The desired behavior if no files are found using the provided path.

Available options:

- `warn`: Output a warning but do not fail the action
- `error`: Fail the action with an error message
- `ignore`: Do not output any warnings or errors, the action does not fail

Optional. Default is `warn`.

### retention-days

How long the artifact should be retained in days, after this the artifact will be expired and removed.

Optional. Default is `30` days

### compression-level

The level of compression for Zlib to be applied to the artifact archive.
The value can range from 0 to 9.
For large files that are not easily compressed, a value of 0 is recommended for significantly faster uploads.

Optional. Default is `6`.

### overwrite

If `true`, an artifact with a matching name will be deleted before a new one is uploaded.
If `false`, the action will fail if an artifact for the given name already exists. Does not fail if the artifact does not exist.

Optional. Default is `false`

## Outputs

### artifact-id

Namespace artifact ID that identifies the artifact within your workspace.

### artifact-url

(Coming soon) URL of where the artifact can be downloaded.

Last updated September 1, 2025
