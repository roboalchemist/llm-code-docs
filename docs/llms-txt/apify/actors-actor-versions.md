# Source: https://docs.apify.com/api/v2/actors-actor-versions.md

# Actor versions - Introduction

The API endpoints in this section allow you to manage your Apify Actors versions.

* The version object contains the source code of a specific version of an Actor.
* The `sourceType` property indicates where the source code is hosted, and based on its value the Version object has the following additional property:

| **Value**        | **Description**                                                                                                                                                                                                                                                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"SOURCE_FILES"` | Source code is comprised of multiple files specified in the `sourceFiles` array. Each item of the array is an object with the following fields:<br />- `name`: File path and name<br />- `format`: Format of the content, can be either `"TEXT"` or `"BASE64"`<br />- `content`: File content<br /><br />Source files can be shown and edited in the Apify Console's Web IDE. |
| `"GIT_REPO"`     | Source code is cloned from a Git repository, whose URL is specified in the `gitRepoUrl` field.                                                                                                                                                                                                                                                                                |
| `"TARBALL"`      | Source code is downloaded using a tarball or Zip file from a URL specified in the `tarballUrl` field.                                                                                                                                                                                                                                                                         |
| `"GITHUB_GIST"`  | Source code is taken from a GitHub Gist, whose URL is specified in the `gitHubGistUrl` field.                                                                                                                                                                                                                                                                                 |

For more information about source code and Actor versions, check out [Source code](https://docs.apify.com/platform/actors/development/actor-definition/source-code) in Actors documentation.

<!-- -->

## [Get list of versions](https://docs.apify.com/api/v2/act-versions-get.md)

[/acts/{actorId}/versions](https://docs.apify.com/api/v2/act-versions-get.md)

## [Create version](https://docs.apify.com/api/v2/act-versions-post.md)

[/acts/{actorId}/versions](https://docs.apify.com/api/v2/act-versions-post.md)

## [Get version](https://docs.apify.com/api/v2/act-version-get.md)

[/acts/{actorId}/versions/{versionNumber}](https://docs.apify.com/api/v2/act-version-get.md)

## [Update version](https://docs.apify.com/api/v2/act-version-put.md)

[/acts/{actorId}/versions/{versionNumber}](https://docs.apify.com/api/v2/act-version-put.md)

## [Delete version](https://docs.apify.com/api/v2/act-version-delete.md)

[/acts/{actorId}/versions/{versionNumber}](https://docs.apify.com/api/v2/act-version-delete.md)

## [Get list of environment variables](https://docs.apify.com/api/v2/act-version-env-vars-get.md)

[/acts/{actorId}/versions/{versionNumber}/env-vars](https://docs.apify.com/api/v2/act-version-env-vars-get.md)

## [Create environment variable](https://docs.apify.com/api/v2/act-version-env-vars-post.md)

[/acts/{actorId}/versions/{versionNumber}/env-vars](https://docs.apify.com/api/v2/act-version-env-vars-post.md)

## [Get environment variable](https://docs.apify.com/api/v2/act-version-env-var-get.md)

[/acts/{actorId}/versions/{versionNumber}/env-vars/{envVarName}](https://docs.apify.com/api/v2/act-version-env-var-get.md)

## [Update environment variable](https://docs.apify.com/api/v2/act-version-env-var-put.md)

[/acts/{actorId}/versions/{versionNumber}/env-vars/{envVarName}](https://docs.apify.com/api/v2/act-version-env-var-put.md)

## [Delete environment variable](https://docs.apify.com/api/v2/act-version-env-var-delete.md)

[/acts/{actorId}/versions/{versionNumber}/env-vars/{envVarName}](https://docs.apify.com/api/v2/act-version-env-var-delete.md)
