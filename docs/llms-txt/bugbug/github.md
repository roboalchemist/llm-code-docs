# Source: https://docs.bugbug.io/integrations/github.md

# GitHub

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FGQ9yQqBrF806pbfVfHJF%2FScreenshot%202022-04-12%20at%2011.23.14.png?alt=media\&token=63b9e3ff-656a-419c-8b24-4bcf31e7ca14)

Integrate with GitHub to streamline testing into your CI/CD pipeline, providing real-time feedback within your repository. Run tests and suites on BugBug Cloud to ensure that only high-quality, thoroughly tested code is deployed to production environments, reducing the risk of introducing regressions or bugs.

Currently, it is possible to integrate in two ways:

1. Using [official GitHub Action](#official-github-action) **(recommended)**
2. Via [BugBug Command Line Interface (CLI)](https://docs.bugbug.io/integrations/api)

## Official GitHub Action

GitHub Actions allows developers to create automated workflows directly within their GitHub repositories. Integrating with [BugBug Cloud Runner](https://github.com/marketplace/actions/bugbug-cloud-runner) lets them seamlessly incorporate testing into your CI/CD pipeline to receive instant feedback on test results and quickly identify issues.

{% hint style="warning" %}
Keep in mind that BugBug Cloud Runner is only available on paid plans. \
More information about pricing can be found here: <https://bugbug.io/pricing/>
{% endhint %}

To add BugBug action to your workflow:

1. Go to the "Integrations" page
2. Find GitHub on the integrations list
3. Click on the "Manage" button
4. Continue by clicking on the "Open Github Action" button
5. Follow the instructions on [GitHub Marketplace](https://github.com/marketplace/actions/bugbug-cloud-runner) to add BugBug Cloud Runner to your .yml files

{% hint style="info" %}
Find your API token by following the instructions provided [here](https://docs.bugbug.io/api#get-your-api-token).

Discover where to find your suite ID by referring to the information available on this [page](https://docs.bugbug.io/api#find-your-suite-id).
{% endhint %}
