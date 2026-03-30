# Source: https://www.speakeasy.com/md/docs/speakeasy-reference/generation/ci-cd-pipeline.md

# Workflow matrix

> **Tip**
> To quickly set up the workflow, run `speakeasy configure github` in the root
> of the SDK repository. This automates the setup and commits the necessary
> files. For more complex or custom configurations, the following is supported.

## Workflow inputs

```yml
"on":
  workflow_dispatch:
    inputs:
      force:
        description: Force generation of SDKs
        type: boolean
        default: false
      set_version:
        description: optionally set a specific SDK version
        type: string
      runs-on:
        description: Runner to use for the workflow (e.g., large-ubuntu-runner)
        type: string
        default: ubuntu-latest
```

The inputs to the workflow determine how the SDKs will be generated.

| Input Name | Description | Type | Default |
| --- | --- | --- | --- |
| speakeasy_version | Version of the Speakeasy CLI to use. Use "latest" to always use the latest version. | string | latest |
| mode | Workflow mode: `direct` commits changes directly to the branch and publishes SDKs to configured package registries in the same run, `pr` creates a pull request (publishing is handled by the separate `sdk_publish.yaml` workflow when the PR is merged), or `test` fully runs through generation without modifying any GitHub state. | string | direct |
| force | Forces SDK generation, even if no changes are detected. | boolean | false |
| set_version | Manually set a specific version for the SDK being generated. | string | None |

## Workflow jobs

The generate job utilizes the Speakeasy SDK generation action. It references the `workflow-executor.yaml` from the `sdk-generation-action` repo, which handles the core operations like pulling the OpenAPI document, validating it, and generating the SDKs.

In `direct` mode, this workflow also handles publishing the generated SDKs to package registries (npm, PyPI, Maven, etc.) as part of the same run. In `pr` mode, publishing is handled separately by the `sdk_publish.yaml` workflow after the generated PR is merged.

### With

```yml
jobs:
  generate:
    uses: speakeasy-api/sdk-generation-action/.github/workflows/workflow-executor.yaml@v15
    with:
      force: ${{ github.event.inputs.force }}
      mode: pr
      set_version: ${{ github.event.inputs.set_version }}
      speakeasy_version: latest
      github_repository: acme-org/acme-sdk-typescript
      runs-on: ${{ github.event.inputs.runs-on }}
```

| Input Name | Description | Type | Default |
| --- | --- | --- | --- |
| speakeasy_version | Version of the Speakeasy CLI to use. Use "latest" to always use the latest version. | string | latest |
| mode | Workflow mode: `direct` commits changes directly to the branch and publishes SDKs to configured package registries in the same run, `pr` creates a pull request (publishing is handled by the separate `sdk_publish.yaml` workflow when the PR is merged), or `test` fully runs through generation without modifying any GitHub state. | string | direct |
| force | Forces SDK generation, even if no changes are detected. | boolean | false |
| set_version | Manually set a specific version for the SDK being generated. | string | None |
| github_repository | The GitHub repository path (e.g., 'owner/repo-name') that package registries should reference. This overrides the default repository detected from the current Git context. | string | None |
| runs-on | Specifies the runner to use for the workflow. Use this to configure larger GitHub-hosted runners for resource-intensive builds. Accepts runner labels like 'ubuntu-latest' or custom labels for larger runners. | string | ubuntu-latest |

### Secrets

```yml
secrets:
  github_access_token: ${{ secrets.GITHUB_TOKEN }}
  npm_token: ${{ secrets.NPM_TOKEN }}
  speakeasy_api_key: ${{ secrets.SPEAKEASY_API_KEY }}
```

| Secret Name | Description |
| --- | --- |
| github_access_token | GitHub access token with write access to the repository. Used to push changes and create PRs. |
| speakeasy_api_key | API key for authenticating with the Speakeasy CLI. |
| npm_token | Token to authenticate publishing to npm registry. |
| pypi_token | Token to authenticate publishing to PyPi for Python packages. |
| packagist_token | Token to authenticate publishing to Packagist for PHP packages. |
| ossrh_username | Username for publishing the Java package to Sonatype Central Portal. |
| ossrh_password | Password for publishing the Java package to Sonatype Central Portal. |
| java_gpg_secret_key | GPG secret key used for signing the Java package. |
| java_gpg_passphrase | Passphrase for the GPG secret key. |
| rubygems_auth_token | Auth token (API key) for publishing to RubyGems. |
| nuget_api_key | API key for publishing to the Nuget registry. |
| slack_webhook_url | Optional: Slack Webhook URL for posting workflow failure notifications. |
| terraform_gpg_secret_key | GPG secret key used for signing the Terraform provider. |
| terraform_gpg_passphrase | Passphrase for the Terraform GPG secret key. |

## PyPI trusted publishing job

For Python SDKs using [trusted publishing](/docs/sdks/publish-sdk#python-pypi-trusted-publishing), add a `publish-pypi` job that runs after the main publish job. This job uses OIDC to authenticate with PyPI, eliminating the need for a `PYPI_TOKEN` secret.

```yml
publish-pypi:
  needs: publish
  if: ${{ needs.publish.outputs.python_regenerated == 'true' &&
          needs.publish.outputs.publish_python == 'true' &&
          needs.publish.outputs.use_pypi_trusted_publishing == 'true' }}
  runs-on: ubuntu-latest
  permissions:
    id-token: write
    contents: read
  steps:
    - uses: actions/checkout@v4
    - uses: speakeasy-api/sdk-generation-action/publish-pypi@v15
      with:
        python-directory: ${{ needs.publish.outputs.python_directory }}
        speakeasy_api_key: ${{ secrets.SPEAKEASY_API_KEY }}
        github_access_token: ${{ secrets.GITHUB_TOKEN }}
```

| Input Name | Description | Type | Default |
| --- | --- | --- | --- |
| python-directory | Directory where the Python SDK was generated. Passed from the publish job outputs. | string | None |
| speakeasy_api_key | API key for authenticating with the Speakeasy CLI. | string | None |
| github_access_token | GitHub access token. Use the built-in GITHUB_TOKEN secret. | string | None |

> **Important**
> The `id-token: write` permission is required at the job level for the OIDC token exchange with PyPI. The trusted publisher must also be configured on pypi.org for the target package.

## Workflow outputs

The workflow provides outputs that indicate which SDKs were regenerated and can trigger further actions in the pipeline, such as validating, testing, and publishing the SDKs.

| Output Name | Description |
| --- | --- |
| python_regenerated | Indicates if the Python SDK was regenerated. |
| python_directory | Directory where the Python SDK was generated. |
| typescript_regenerated | Indicates if the TypeScript SDK was regenerated. |
| typescript_directory | Directory where the TypeScript SDK was generated. |
| java_regenerated | Indicates if the Java SDK was regenerated. |
| java_directory | Directory where the Java SDK was generated. |
| go_regenerated | Indicates if the Go SDK was regenerated. |
| go_directory | Directory where the Go SDK was generated. |
| php_regenerated | Indicates if the PHP SDK was regenerated. |
| php_directory | Directory where the PHP SDK was generated. |
| ruby_regenerated | Indicates if the Ruby SDK was regenerated. |
| ruby_directory | Directory where the Ruby SDK was generated. |
| terraform_regenerated | Indicates if the Terraform SDK was regenerated. |
| terraform_directory | Directory where the Terraform SDK was generated. |
| docs_regenerated | Indicates if the SDK documentation was regenerated. |
| branch_name | The branch name used for generating the SDK or the PR. |
| commit_hash | The commit hash generated for the SDK (in direct mode). |
| publish_python | Indicates if the Python SDK should be published. |
| use_pypi_trusted_publishing | Indicates if PyPI trusted publishing is configured for the Python SDK. |
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
