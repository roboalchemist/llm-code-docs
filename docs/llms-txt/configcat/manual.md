# Source: https://configcat.com/docs/advanced/code-references/manual.md

# CLI - Add to CI/CD pipelines manually

This section describes how to use the [ConfigCat CLI](https://configcat.com/docs/docs/advanced/cli/.md) to scan your source code for feature flag and setting usages and upload the found code references to ConfigCat.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Install](https://configcat.com/docs/docs/advanced/cli/.md#installation) the CLI in your CI/CD or local environment.
* [Setup](https://configcat.com/docs/docs/advanced/cli/.md#setup) the CLI with your ConfigCat Management API credentials.
* Get your selected [Config's ID](https://configcat.com/docs/docs/advanced/code-references/overview/.md#config-id).

## Scan & Upload[​](#scan--upload "Direct link to Scan & Upload")

To initiate the scanning with uploading the results, you can use the `scan` command with the `--upload` option.

### With Git VCS[​](#with-git-vcs "Direct link to With Git VCS")

The scan command detects when it's being executed on a Git repository and automatically [extracts additional information](https://configcat.com/docs/docs/advanced/code-references/overview/.md#scanning-git-repositories). The following snippet shows a minimal example that uses only the required parameters in the case of a Git repository.

```
configcat scan /path/to/your/repo \
    --config-id YOUR-CONFIG-ID \ # required
    --repo YOUR-REPOSITORY-NAME \ # required
    --upload # upload the scan report
```

You can use the optional template URL parameters for generating VCS links to your source code.

```
configcat scan /path/to/your/repo \
    --config-id YOUR-CONFIG-ID \ # required
    --repo YOUR-REPOSITORY-NAME \ # required
    --file-url-template "https://github.com/my/repo/blob/{commitHash}/{filePath}#L{lineNumber}" \ # optional, used to generate VCS file links
    --commit-url-template "https://github.com/my/repo/commit/{commitHash}" \ # optional, used to generate VCS commit links
    --upload # upload the scan report
```

info

The template parameters (`filePath`, `lineNumber`, and `commitHash`) are automatically replaced by the CLI based on the collected information from the Git repository.

### With Non-Git VCS[​](#with-non-git-vcs "Direct link to With Non-Git VCS")

As the `scan` command cannot determine such information as `branch` and `commitHash` when you execute it on a non-Git repository, you have to set these parameters manually.

```
configcat scan /path/to/your/repo \
    --config-id YOUR-CONFIG-ID \ # required
    --repo YOUR-REPOSITORY-NAME \ # required
    --branch BRANCH-NAME \ # required in case of non-git repository
    --commit-hash \ # optional, used to show it on the report and generate commit links
    --file-url-template "https://github.com/my/repo/blob/{commitHash}/{filePath}#L{lineNumber}" \ # optional, used to generate VCS file links
    --commit-url-template "https://github.com/my/repo/commit/{commitHash}" \ # optional, used to generate VCS commit links
    --upload # upload the scan report
```

### Docker[​](#docker "Direct link to Docker")

After [installing](https://configcat.com/docs/docs/advanced/cli/.md#installation) the ConfigCat CLI with Docker, you can scan your repository by mounting its folder as a volume and setting the [ConfigCat Management API credentials](https://app.configcat.com/my-account/public-api-credentials) as environment variables on the executing container.

```
docker run --rm \
    -v /path/to/your/repo:/repository \ # mount the repository as volume
    -e CONFIGCAT_API_USER=YOUR-API-USER \ # Management API username
    -e CONFIGCAT_API_PASS=YOUR-API-PASS \ # Management API password
    configcat/cli scan /repository \ # scan the mounted volume
    --config-id YOUR-CONFIG-ID \ # required
    --repo YOUR-REPOSITORY-NAME \ # required
    --upload # upload the scan report
```

## Reference[​](#reference "Direct link to Reference")

See the `scan` command's [reference documentation](https://configcat.github.io/cli/configcat-scan.html) for all available command parameters.
