# Source: https://help.aikido.dev/code-scanning/local-code-scanning/pr-gating-for-code-using-local-scanner.md

# PR Gating for Code Using Local Scanner

The Aikido Local Scanner can be used to enforce security gates in your CI pipeline.

{% hint style="info" %}
You can also use PR gating with your cloud-connected workspaces (GitHub, BitBucket, etc). Check out our CI [Integration section](https://help.aikido.dev/section/ci-integrations/sg3q6UrIf4qE).
{% endhint %}

PR gating ensures that new code meets your security standards before it is merged into the default branch. It scans only the changes introduced in the pull request. If the scan detects new issues that meet or exceed your configured severity threshold, the CI pipeline fails.

This prevents new vulnerabilities from being introduced while allowing existing findings to be addressed separately.

{% hint style="info" %}
We also support [release gating](https://help.aikido.dev/container-image-scanning/local-image-scanning/release-gating-for-container-images-using-local-image-scanner) for teams that want to enforce checks at release time.
{% endhint %}

To enable PR gating, add the `--fail-on <severity>` option to select your preferred severity level. Then, add the `--gating-mode pr` option to signify that you wish to perform PR gating. You must also specify the base (`--base-commit-id <commit-id>`) and head commit (`--head-commit-id <commit-id>`). If there a scan was previously performed on the base commit id, the scan results will be compared to those. If not, the results will be compared to the most recent scan on your default branch.

## Examples <a href="#examples" id="examples"></a>

### GitLab Self Managed <a href="#gitlab-self-managed" id="gitlab-self-managed"></a>

For general information about setting up the Local Scanner in a GitLab environment, check out [this article](https://help.aikido.dev/code-scanning/local-code-scanning/gitlab-self-managed-setup-for-local-code-scanning).

Example `.gitlab-ci.yml` for PR gating:

```yaml
default:
  image:
    name: aikidosecurity/local-scanner:latest
    entrypoint: [""]

run_aikido_selfscanner:
  script:
  - aikido-local-scanner scan ./ --apikey $AIKIDO_LOCAL_SCANNER_TOKEN --repositoryname $CI_PROJECT_NAME --branchname $CI_COMMIT_REF_NAME --gating-mode pr --fail-on critical --base-commit-id $CI_MERGE_REQUEST_DIFF_BASE_SHA --head-commit-id $CI_COMMIT_SHA
  rules:
    - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
```

### GitHub <a href="#github" id="github"></a>

For general information about setting up the Local Scanner in a GitHub environment, check out [this article](https://help.aikido.dev/code-scanning/local-code-scanning/github-action-setup-for-local-code-scanning).

Example `.github/workflows/aikido-scan.yml` for PR gating:

```yaml
on:
  pull_request:
    branches:
      - main

name: Aikido Scan
jobs:
  aikido-local-scan-repo:
    runs-on: ubuntu-latest
    container:
      image: aikidosecurity/local-scanner:latest
    steps: 
      - uses: actions/checkout@v4 
        with: 
          token: ${{ secrets.GITHUB_TOKEN }} 
          path: ${{ github.event.repository.name }}
          fetch-depth: 0 # Makes sure base and head commit are accessible in workflow
      - name: Run scan
        run: aikido-local-scanner scan ${{ github.event.repository.name }} --apikey ${{ secrets.AIKIDO_API_KEY }} --repositoryname ${{ github.event.repository.name }} --branchname ${{ github.event.pull_request.head.ref }} --gating-mode pr --fail-on critical --base-commit-id ${{ github.event.pull_request.base.sha }} --head-commit-id ${{ github.event.pull_request.head.sha }}
```

### Bitbucket

Example `bitbucket-pipelines.yml` for PR gating:

```yaml
image: aikidosecurity/local-scanner:latest

pipelines:
  pull-requests:
    "**":   # this applies the pipeline to all pull requests
      - step:
          name: Aikido PR Gating Scan
          script:
            - >- 
              aikido-local-scanner scan ./
              --apikey $AIKIDO_API_KEY
              --repositoryname $BITBUCKET_REPO_SLUG
              --branchname $BITBUCKET_BRANCH
              --gating-mode pr
              --fail-on critical
              --base-commit-id $BITBUCKET_PR_DESTINATION_COMMIT
              --head-commit-id $BITBUCKET_COMMIT
```

### Azure DevOps Server

For general information about setting up the Local Scanner in a Azure DevOps environment, check out [this article](https://help.aikido.dev/code-scanning/local-code-scanning/github-action-setup-for-local-code-scanning).\
Example setup for PR gated scan:

```yaml
trigger: none

pr:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

container:
  image: aikidosecurity/local-scanner:latest
  options: --entrypoint=""

steps:
  - checkout: self
    clean: true
    fetchDepth: 0

  - bash: |
      echo "PR Target Branch (full ref): $SYSTEM_PULLREQUEST_TARGETBRANCH"
      echo "PR Source Branch (full ref): $SYSTEM_PULLREQUEST_SOURCEBRANCH"

      # strip prefix
      TARGET_BRANCH=${SYSTEM_PULLREQUEST_TARGETBRANCH#refs/heads/}
      echo "Target branch stripped: $TARGET_BRANCH"

      # fetch target branch to compute merge base
      git fetch origin "$TARGET_BRANCH"

      BASE_COMMIT=$(git merge-base HEAD "origin/$TARGET_BRANCH")
      echo "Base commit SHA: $BASE_COMMIT"

      echo "##vso[task.setvariable variable=baseCommitId]$BASE_COMMIT"
    displayName: 'Get base commit SHA'

  - script: |
      aikido-local-scanner scan $BUILD_SOURCESDIRECTORY \
        --apikey $(AIKIDO_API_KEY) \
        --repositoryname $BUILD_REPOSITORY_NAME \
        --branchname $(System.PullRequest.SourceBranch) \
        --gating-mode pr \
        --fail-on critical \
        --base-commit-id $(baseCommitId) \
        --head-commit-id $(System.PullRequest.SourceCommitId)
    displayName: 'Run Aikido PR Scan'
```

Make sure to add this pipeline as a Build Validation to your main branch:

1. Go to Project Settings → Repositories → Policies → Branch Policies
2. Select your main branch
3. Add Build Validation
4. Choose this pipeline
5. Set:
   * Trigger: Automatic
