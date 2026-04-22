<!-- Source: https://namespace.so/docs/reference/github-actions/download-artifact -->

# namespace-actions/download-artifact

namespace-actions/download-artifact@v2

[namespace-actions/download-artifact](https://github.com/namespace-actions/download-artifact) downloads artifact archives
from Namespace high-performance storage. This action is 100% compatible with GitHub's [actions/download-artifact](https://github.com/actions/download-artifact).

To upload artifacts to Namespace, use [namespace-actions/upload-artifact](/docs/reference/github-actions/upload-artifact).

## Prerequisites

This action only works with Namespace GitHub Runners, if you haven't yet migrated your workflows to Namespace runners, checkout
the [runner documentation](/docs/solutions/github-actions) first.

## Example

```
jobs:
  deploy:
    name: Demo Download Archive
    runs-on: namespace-profile-default
    steps:
      - name: Download Archive
        uses: namespace-actions/download-artifact@v2
        with:
          name: test-archive
          path: /tmp/destination
```

## Options

### name

Name of the artifact to download.

Optional. If unspecified, all artifacts for the run are downloaded.

### path

Destination path. Supports basic tilde expansion.

Optional. Default is `$GITHUB_WORKSPACE`.

### pattern

A glob pattern to the artifacts that should be downloaded. Ignored if name is specified.

Optional.

### merge-multiple

When multiple artifacts are matched, this changes the behavior of the destination directories.
If `true`, the downloaded artifacts will be in the same directory specified by path.
If `false`, the downloaded artifacts will be extracted into individual named directories within the specified path.

Optional. Default is `false`.

### github-token

The GitHub token used to authenticate with the GitHub API.
This is required when downloading artifacts from a different repository or from a different workflow run.

Optional. If unspecified, the action will download artifacts from the current repo and the current workflow run.

### repository

The repository owner and the repository name joined together by `/`.
If github-token is specified, this is the repository that artifacts will be downloaded from.

Optional. Default is `${{ github.repository }}`.

### run-id

The id of the workflow run where the desired download artifact was uploaded from.
If github-token is specified, this is the run that artifacts will be downloaded from.

Optional. Default is `${{ github.run_id }}`.

## Outputs

### download-path

Absolute path where the artifact(s) were downloaded.

Last updated December 2, 2025
