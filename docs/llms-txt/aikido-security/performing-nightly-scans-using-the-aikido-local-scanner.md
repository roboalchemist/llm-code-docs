# Source: https://help.aikido.dev/code-scanning/local-code-scanning/performing-nightly-scans-using-the-aikido-local-scanner.md

# Performing Nightly Scans Using Local Scanner

When implementing the Aikido Local Scanner in your CI, it is recommended to perform scans on changes in your default branch. You might also consider performing scheduled scan at fixed intervals on some repositories, particularly those that do not regularly receive updates. This article will focus on setting up these recurring scans. If you need more details on setting up the Local Scanner for a specific CI/CD tool, please refer to the respective guides for these tools.

## Setting up a nightly scan in GitHub Actions <a href="#setting-up-a-nightly-scan-in-github-actions" id="setting-up-a-nightly-scan-in-github-actions"></a>

The example below creates a GitHub Action that will perform a scan on a push to the main branch and nightly at midnight.

```yaml
on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 0 * * *'

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
          path: my-repo 
      - name: Run scan
        run: aikido-local-scanner scan my-repo --apikey ${{ secrets.AIKIDO_API_KEY }} --repositoryname MyRepo --branchname main
```

Detailed info on how to setup a scan using GitHub Actions can be found [here](https://help.aikido.dev/code-scanning/local-code-scanning/github-action-setup-for-local-code-scanning).\
Detailed info on how to use the schedule option in a GitHub Action can be found [here](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule).

## Setting up a nightly scan in GitLab <a href="#setting-up-a-nightly-scan-in-gitlab" id="setting-up-a-nightly-scan-in-gitlab"></a>

You will already need to have setup a pipeline in your GitLab project, refer to [this article](https://help.aikido.dev/code-scanning/local-code-scanning/gitlab-self-managed-setup-for-local-code-scanning) for more info.\
After you have setup a pipeline for nightly scan, you'll need to schedule it.\
On the left side bar, select **Build > Pipeline schedules**.\
Fill in the form with your desired interval, timezone and your default branch. Click 'Create pipeline schedule'. After this, you will see your scheduled pipeline appear in the overview.

![Scheduled nightly Aikido scan on 'main' branch; next run in 21 hours.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ddac89fa5d6db4dff4cce8173d8c45a38f5b485d%2Fperforming-nightly-scans-using-the-aikido-local-scanner_165e3a66-d238-4ad6-8178-d5b7b5d4067c.png?alt=media)

More info on schedule pipelines can be found [here](https://archives.docs.gitlab.com/16.6/ee/ci/pipelines/schedules.html).

## Setting up a nightly scan in Jenkins <a href="#setting-up-a-nightly-scan-in-jenkins" id="setting-up-a-nightly-scan-in-jenkins"></a>

To set up a scheduled scan in Jenkins, select **Build Periodically** as the Build Trigger.\
The example below will schedule a scan, every night at midnight

![Jenkins build trigger set for daily execution at midnight using cron syntax.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4389a6c4cd930ac678e6949e439a60281d21c4a5%2Fperforming-nightly-scans-using-the-aikido-local-scanner_b7966951-f587-491d-ade9-e37fffc02be7.png?alt=media)

More info on setting up the Local Scanner in Jenkins can be found [here](https://help.aikido.dev/code-scanning/local-code-scanning/jenkins-setup-for-local-code-scanning).
