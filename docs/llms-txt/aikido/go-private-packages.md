# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/go-private-packages.md

# Go - Private Packages

For Aikido to update dependencies that include private packages, it needs access to your private registries so it can generate accurate lockfile updates. Follow the steps below to configure private Go packages hosted on GitHub or GitLab.&#x20;

1. Navigate to the [autofix settings](https://app.aikido.dev/issues/fix/settings) page and click on "*Connect Registry*"
2. Select "*Go*" as your Package Manager

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FEMVbFvRVG1jiQm9H9NFi%2Fimage.png?alt=media&#x26;token=80e945c5-f859-41bc-942d-96b7965c0dc7" alt=""><figcaption></figcaption></figure>

3. In the modal below, enter the private registry host, this is the hostname with the path to the repo where the package is being hosted. Aikido will expose this as the `GOPRIVATE` env variable during the update process.
4. eg for GitHub: `github.com/[ORG]/[REPO]`
5. eg for Gitlab: `gitlab.com/[ORG]/[REPO]`

Aikido uses this value to set the `GOPRIVATE` environment variable, so it can be a list of comma-separated glob patterns of module path prefixes that should be considered private (eg. `github.com/myorg/*` or `gitlab.com/myorg/repo1,gitlab.com/myorg/repo2`.

1. Next create a personal access token in either GitHub or Gitlab with read-only access for that repository and it to the token field

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FxXKLeMN5X9XZts0w3RFz%2Fimage.png?alt=media&#x26;token=6b8d38ce-098c-4d34-8574-8f29826ba130" alt=""><figcaption></figcaption></figure>

5. Click on "*Connect Registry*"
